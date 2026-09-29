"""Experimento de deliberación multiagente sobre asignación RACI en SCADA/EMS.

Fases por corrida (escenario x repetición):
  1. decisión independiente: DAS, ISC, MCO, ODC y NEUTRAL, sin verse entre sí;
  2. reconsideración: los cuatro especializados ven las demás propuestas, anonimizadas;
  3. arbitraje: una instancia neutral del mismo modelo evalúa las propuestas finales.

Uso:
  python experiment.py --label smoke --scenarios S01 --reps 1
  python experiment.py --label pilot                 # 10 escenarios x N_REPETITIONS
  python experiment.py --label test --dry-run        # sin API: respuestas simuladas

Nunca lee posthoc/reference_raci.json.
"""
import argparse
import hashlib
import json
import os
import platform
import random
import re
import sys
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # necesario si Python corre con safe_path (PYTHONSAFEPATH)

import config  # noqa: E402
from build_corpus import FORBIDDEN_MARKERS  # noqa: E402

PROMPTS = HERE / "prompts"
RESULTS = HERE / "results"
MAT = HERE          # carpeta del material (base o variante, p. ej. ablation_anon)
PHASES = "all"      # "all" o "1" (solo decisión independiente)
BUDGET = None       # tope de gasto de esta ejecución; None = config.MAX_BUDGET_USD
MODEL = config.MODEL  # modelo de esta ejecución (--model); por defecto el de config.py

AGENT_PROMPT = {"DAS": "das.md", "ISC": "isc.md", "MCO": "mco.md", "ODC": "odc.md",
                "NEUTRAL": "neutral.md", "ARBITER": "arbiter.md"}
EXTRA_UNITS = ["GERENCIA_TECNICA", "DIV_SISTEMAS_COMUNICACION",
               "PROPOSED_NEW_AUTHORITY", "UNIDAD_NO_INCLUIDA_EN_CORPUS"]
CLAIM_TYPES = ["DOCUMENTADO", "INFERIDO", "BUENA_PRACTICA", "PROPUESTO"]

# Normalización a nivel de departamento para el análisis (secciones -> departamento).
NORMALIZE = {"GT/DAS": "DAS", "GT/DAS1": "DAS", "GT/DAS2": "DAS",
             "DTE/ISC": "ISC", "DTE/ISC1": "ISC", "DTE/ISC2": "ISC", "DTE/ISC3": "ISC",
             "DTE/MCO": "MCO", "GT/ODC": "ODC", "GT/DOS": "DOS", "GT/DEL": "DEL",
             "GT/DEN": "DEN", "GT/DDR": "DDR", "GT/OP": "OP", "GT/DT": "DT",
             "GT/TMB": "TX_REG", "GT/TES": "TX_REG", "GT/TSU": "TX_REG",
             "GT/TCE": "TX_REG", "GT/NAC": "TX_REG",
             "GERENCIA_TECNICA": "GERENCIA_TECNICA", "DIV_SISTEMAS_COMUNICACION": "DIV_SIST_COM",
             "PROPOSED_NEW_AUTHORITY": "NEW_AUTHORITY", "UNIDAD_NO_INCLUIDA_EN_CORPUS": "OTHER"}

_write_lock = threading.Lock()


# ---------------------------------------------------------------- carga de material

def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read(path):
    return Path(path).read_text(encoding="utf-8")


def set_material(name):
    """Selecciona el material (base o una variante con material.json de correspondencias)."""
    global MAT, PROMPTS
    MAT = HERE if name in (None, "", "base") else HERE / name
    PROMPTS = MAT / "prompts"
    mj = MAT / "material.json"
    if mj.exists():  # la correspondencia se usa solo para validar y analizar; no se envía a los agentes
        data = json.loads(read(mj))
        NORMALIZE.update(data["normalize"])
        EXTRA_UNITS[:] = data["extra_units"]


def load_material():
    inst = json.loads(read(MAT / "corpus_institutional.json"))
    ext = json.loads(read(MAT / "corpus_external.json"))
    m = {
        "corpus_inst_md": read(MAT / "corpus_institutional.md"),
        "corpus_ext_md": read(MAT / "corpus_external.md"),
        "inst_ids": {e["id"] for f in inst for e in f["entries"]},
        "ext_ids": {s["source_id"] for s in ext},
        "source_text": {**{e["id"]: e["text"] for f in inst for e in f["entries"]},
                        **{s["source_id"]: " ".join([s["reference"], s["principle"], *s["can_support"],
                                                     *s["cannot_support"]]) for s in ext}},
        "units": [f["unit_code"] for f in inst] + EXTRA_UNITS,
        "unit_names": {f["unit_code"]: f["unit_name"] for f in inst},
        "activities": {a["activity_id"]: a for a in json.loads(read(MAT / "activities.json"))},
        "scenarios": {s["scenario_id"]: s for s in json.loads(read(MAT / "scenarios.json"))},
        # judge.md pertenece a la auditoría post hoc de citas, no al material de los agentes.
        "prompts": {p.name: read(p) for p in sorted(PROMPTS.glob("*.md")) if p.name != "judge.md"},
    }
    return m


def material_hashes(m):
    hashes = {f"prompts/{k}": sha256_text(v) for k, v in m["prompts"].items()}
    for name in ["corpus_institutional.md", "corpus_external.md", "scenarios.json", "activities.json"]:
        hashes[name] = sha256_text(read(MAT / name))
    return hashes


# ---------------------------------------------------------------- esquemas JSON

def decision_schema(units, activity_ids, phase2=False):
    unit_list = {"type": "array", "items": {"type": "string", "enum": units}}
    cite = {"type": "object",
            "properties": {"source_id": {"type": "string"},
                           "claim_type": {"type": "string", "enum": CLAIM_TYPES},
                           "quote": {"type": "string"},
                           "supports": {"type": "string"}},
            "required": ["source_id", "claim_type", "quote", "supports"]}
    props = {"activity_id": {"type": "string", "enum": activity_ids},
             "accountable": unit_list, "responsible": unit_list,
             "consulted": unit_list, "informed": unit_list,
             "institutional_ambiguity": {"type": "boolean"},
             "alternative_assignments": {"type": "array", "items": {
                 "type": "object",
                 "properties": {"accountable": unit_list, "rationale": {"type": "string"}},
                 "required": ["accountable", "rationale"]}},
             "evidence": {"type": "array", "items": cite},
             "external_principles": {"type": "array", "items": cite},
             "new_authority_justification": {"type": "string"},
             "reasoning_summary": {"type": "string"},
             "confidence": {"type": "string", "enum": ["low", "medium", "high"]}}
    required = ["activity_id", "accountable", "responsible", "consulted", "informed",
                "institutional_ambiguity", "alternative_assignments", "evidence",
                "external_principles", "reasoning_summary", "confidence"]
    if phase2:
        props["position"] = {"type": "string", "enum": ["MAINTAIN", "MODIFY", "AMBIGUOUS"]}
        props["position_justification"] = {"type": "string"}
        required = ["activity_id", "position", "position_justification"] + required[1:]
    return {"type": "object",
            "properties": {"scenario_id": {"type": "string"},
                           "decisions": {"type": "array", "items": {
                               "type": "object", "properties": props, "required": required}}},
            "required": ["scenario_id", "decisions"]}


def arbiter_schema(units, activity_ids):
    unit_list = {"type": "array", "items": {"type": "string", "enum": units}}
    ruling = {"type": "object",
              "properties": {
                  "activity_id": {"type": "string", "enum": activity_ids},
                  "consensus": {"type": "string", "enum": ["FULL", "MAJORITY", "NONE"]},
                  "verdict": {"type": "string", "enum": ["RESOLVED", "AMBIGUOUS"]},
                  "best_supported": {"type": "object",
                                     "properties": {"accountable": unit_list, "responsible": unit_list,
                                                    "consulted": unit_list, "informed": unit_list},
                                     "required": ["accountable", "responsible", "consulted", "informed"]},
                  "best_supported_proposals": {"type": "array", "items": {"type": "string"}},
                  "requires_institutional_decision": {"type": "array", "items": {"type": "string"}},
                  "disagreement_evidence": {"type": "array", "items": {
                      "type": "object",
                      "properties": {"source_id": {"type": "string"}, "explains": {"type": "string"}},
                      "required": ["source_id", "explains"]}},
                  "reasoning_summary": {"type": "string"},
                  "confidence": {"type": "string", "enum": ["low", "medium", "high"]}},
              "required": ["activity_id", "consensus", "verdict", "best_supported",
                           "requires_institutional_decision", "disagreement_evidence",
                           "reasoning_summary", "confidence"]}
    return {"type": "object",
            "properties": {"scenario_id": {"type": "string"},
                           "rulings": {"type": "array", "items": ruling}},
            "required": ["scenario_id", "rulings"]}


# ---------------------------------------------------------------- construcción de peticiones

def corpus_block(m):
    units = "\n".join(f"- {u}" + (f": {m['unit_names'][u]}" if u in m["unit_names"] else "")
                      for u in m["units"])
    return (m["corpus_inst_md"] + "\n\n" + m["corpus_ext_md"] +
            "\n\n# CÓDIGOS DE UNIDAD ADMITIDOS\n\n" + units + "\n")


def scenario_text(s):
    return json.dumps({k: v for k, v in s.items() if k != "activities"}, ensure_ascii=False, indent=2)


def activities_text(m, s):
    return "\n".join(f"- {a}: {m['activities'][a]['name']} (fase: {m['activities'][a]['phase']})"
                     for a in s["activities"])


def system_prompt(m, agent):
    return m["prompts"]["common.md"] + "\n\n" + m["prompts"][AGENT_PROMPT[agent]]


def fill(template, **values):
    for k, v in values.items():
        template = template.replace("{{" + k + "}}", v)
    return template


def strip_identity(parsed):
    """Propuesta sin campos que identifiquen al autor."""
    return {"decisions": parsed.get("decisions", [])}


def anonymize(proposals, rng):
    """proposals: lista de dicts. Devuelve (texto, mapping etiqueta->agente)."""
    items = list(proposals.items())
    rng.shuffle(items)
    labels = "ABCDEFGH"
    mapping, parts = {}, []
    for label, (agent, parsed) in zip(labels, items):
        mapping[f"PROPUESTA {label}"] = agent
        parts.append(f"### PROPUESTA {label}\n\n" +
                     json.dumps(strip_identity(parsed), ensure_ascii=False, indent=1))
    return "\n\n".join(parts), mapping


def contamination_check(*texts):
    joined = "\n".join(texts)
    hits = [mk for mk in FORBIDDEN_MARKERS if mk in joined]
    if hits:
        raise RuntimeError(f"Contaminación detectada en la petición: {hits}. Se aborta.")
    return "OK"


# ---------------------------------------------------------------- validación

def _norm(text):
    text = re.sub(r"[«»“”\"'`´.,;:()\[\]¿?¡!]", " ", (text or "").lower())
    return re.sub(r"\s+", " ", text).strip()


def verify_quote(quote, source_text):
    """True si cada fragmento de la cita (separado por '...') aparece literalmente en la fuente,
    ignorando mayúsculas, puntuación y espacios. Una cita vacía no se verifica."""
    parts = [_norm(x) for x in re.split(r"\.\.\.|…", quote or "")]
    parts = [x for x in parts if x]
    src = _norm(source_text)
    return bool(parts) and all(x in src for x in parts)


def validate(parsed, scenario, m, kind):
    """Devuelve dict de verificaciones. kind: 'decision' o 'arbiter'."""
    v = {"json_valid": parsed is not None}
    if parsed is None:
        return v
    key = "rulings" if kind == "arbiter" else "decisions"
    items = parsed.get(key) or []
    got = [d.get("activity_id") for d in items]
    expected = scenario["activities"]
    v["missing_activities"] = sorted(set(expected) - set(got))
    v["unexpected_activities"] = sorted(set(got) - set(expected))
    v["duplicated_activities"] = sorted({a for a in got if got.count(a) > 1})
    v["activities_ok"] = not (v["missing_activities"] or v["unexpected_activities"] or v["duplicated_activities"])
    known = m["inst_ids"] | m["ext_ids"]
    cites, invalid = 0, []
    bad_units = set()
    for d in items:
        refs = d.get("evidence", []) + d.get("external_principles", []) + d.get("disagreement_evidence", [])
        for c in refs:
            cites += 1
            if c.get("source_id") not in known:
                invalid.append(c.get("source_id"))
        assignment = d.get("best_supported", d)
        for role in ("accountable", "responsible", "consulted", "informed"):
            bad_units |= {u for u in assignment.get(role, []) if u not in NORMALIZE}
    v["n_citations"] = cites
    v["n_invalid_citations"] = len(invalid)
    v["invalid_source_ids"] = invalid
    quotes = [(c, verify_quote(c.get("quote"), m["source_text"].get(c.get("source_id"), "")))
              for d in items for c in d.get("evidence", []) + d.get("external_principles", [])]
    v["n_quotes"] = len(quotes)
    v["n_quotes_verified"] = sum(ok for _, ok in quotes)
    v["n_documentado"] = sum(c.get("claim_type") == "DOCUMENTADO" for c, _ in quotes)
    v["n_documentado_verified"] = sum(ok for c, ok in quotes if c.get("claim_type") == "DOCUMENTADO")
    v["invalid_units"] = sorted(bad_units)
    v["ok"] = v["activities_ok"] and not bad_units
    return v


# ---------------------------------------------------------------- llamada al modelo

def load_dotenv(path=HERE / ".env"):
    """Carga GEMINI_API_KEY desde .env si no está ya en el entorno. No imprime valores."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("export "):
            line = line[len("export "):]
        if "=" in line and not line.startswith("#"):
            name, value = line.split("=", 1)
            os.environ.setdefault(name.strip(), value.strip().strip("\"'"))


class GeminiCaller:
    def __init__(self):
        from google import genai
        from google.genai import types
        load_dotenv()
        key = os.environ.get("GEMINI_API_KEY")
        if not key:
            sys.exit("Falta la variable de entorno GEMINI_API_KEY.")
        self.client = genai.Client(api_key=key)
        self.types = types

    def __call__(self, system, user, schema, seed):
        t = self.types
        kwargs = dict(system_instruction=system, response_mime_type="application/json",
                      response_json_schema=schema, seed=seed,
                      max_output_tokens=config.MAX_OUTPUT_TOKENS,
                      thinking_config=t.ThinkingConfig(thinking_level=config.THINKING_LEVEL),
                      automatic_function_calling=t.AutomaticFunctionCallingConfig(disable=True))
        if config.TEMPERATURE is not None:
            kwargs["temperature"] = config.TEMPERATURE
        resp = self.client.models.generate_content(
            model=MODEL, contents=user, config=t.GenerateContentConfig(**kwargs))
        u = resp.usage_metadata
        cand = resp.candidates[0] if resp.candidates else None
        return {"text": resp.text,
                "model_version": getattr(resp, "model_version", None),
                "finish_reason": str(cand.finish_reason) if cand else None,
                "usage": {"prompt_token_count": u.prompt_token_count,
                          "candidates_token_count": u.candidates_token_count,
                          "thoughts_token_count": u.thoughts_token_count,
                          "cached_content_token_count": u.cached_content_token_count,
                          "total_token_count": u.total_token_count}}


def strict_schema(schema):
    """Adapta un esquema al modo estricto de OpenAI sin cambiar su contenido.

    El modo estricto exige additionalProperties = false y todas las propiedades como requeridas;
    las que el esquema original no requería se declaran anulables y los null se retiran después
    (drop_nulls), de modo que el JSON resultante tiene la misma forma que con Gemini.
    """
    s = json.loads(json.dumps(schema))

    def walk(node):
        if node.get("type") == "object":
            props = node.get("properties", {})
            optional = set(props) - set(node.get("required", []))
            for name, sub in props.items():
                walk(sub)
                if name in optional:
                    sub["type"] = [sub["type"], "null"]
                    if "enum" in sub:
                        sub["enum"] = sub["enum"] + [None]
            node["required"] = list(props)
            node["additionalProperties"] = False
        elif node.get("type") == "array":
            walk(node["items"])
    walk(s)
    return s


def drop_nulls(x):
    if isinstance(x, dict):
        return {k: drop_nulls(v) for k, v in x.items() if v is not None}
    if isinstance(x, list):
        return [drop_nulls(v) for v in x]
    return x


class OpenAICaller:
    """Mismo contrato que GeminiCaller, con la API Responses de OpenAI.

    Sin semilla (la API no la admite); temperature y top_p no se envían. store=False: las
    respuestas no quedan guardadas en OpenAI.
    """

    def __init__(self):
        from openai import OpenAI
        load_dotenv()
        if not os.environ.get("OPENAI_API_KEY"):
            sys.exit("Falta la variable de entorno OPENAI_API_KEY.")
        # Flex puede tardar varios minutos; los reintentos los gestiona Runner.call.
        self.client = OpenAI(max_retries=0, timeout=900)

    def __call__(self, system, user, schema, seed):
        name = "arbiter" if "rulings" in schema["properties"] else "decisions"
        resp = self.client.responses.create(
            model=MODEL, instructions=system, input=user, store=False,
            max_output_tokens=config.MAX_OUTPUT_TOKENS,
            reasoning={"effort": config.OPENAI_REASONING_EFFORT},
            **({"service_tier": config.OPENAI_SERVICE_TIER} if config.OPENAI_SERVICE_TIER else {}),
            text={"format": {"type": "json_schema", "name": name,
                             "schema": strict_schema(schema), "strict": True}})
        u = resp.usage
        itd, otd = u.input_tokens_details, u.output_tokens_details
        reasoning = (otd.reasoning_tokens or 0) if otd else 0
        cached = (itd.cached_tokens or 0) if itd else 0
        cache_write = (getattr(itd, "cache_write_tokens", 0) or 0) if itd else 0
        text = resp.output_text
        try:
            text = json.dumps(drop_nulls(json.loads(text)), ensure_ascii=False)
        except (TypeError, json.JSONDecodeError):
            pass  # se registra tal cual; validate() la marcará como JSON inválido
        reason = resp.incomplete_details.reason if resp.incomplete_details else None
        return {"text": text,
                "model_version": resp.model,
                "finish_reason": f"{resp.status}: {reason}" if reason else resp.status,
                "usage": {"prompt_token_count": u.input_tokens,
                          "candidates_token_count": u.output_tokens - reasoning,
                          "thoughts_token_count": reasoning,
                          "cached_content_token_count": cached,
                          "cache_write_token_count": cache_write,
                          "total_token_count": u.total_tokens,
                          "service_tier": resp.service_tier}}


class DryRunCaller:
    """Respuestas simuladas válidas según el esquema, para probar el pipeline sin coste."""

    def __init__(self, m):
        self.m = m
        self.ids = sorted(m["inst_ids"]) + sorted(m["ext_ids"])
        self.pool = ["GT/DAS", "GT/DAS1", "DTE/ISC2", "DTE/MCO", "GT/ODC", "GT/TMB", "PROPOSED_NEW_AUTHORITY"]

    def _assign(self, rng):
        return {"accountable": [rng.choice(self.pool)], "responsible": rng.sample(self.pool, 2),
                "consulted": rng.sample(self.pool, 2), "informed": [rng.choice(self.pool)]}

    def _cite(self, rng):
        sid = rng.choice(self.ids) if rng.random() > 0.05 else "INVENTADO_9_9"
        text = self.m["source_text"].get(sid, "")
        quote = " ".join(text.split()[:8]) if rng.random() > 0.2 else "fragmento inventado"
        return {"source_id": sid, "claim_type": rng.choice(CLAIM_TYPES), "quote": quote, "supports": "simulado"}

    def __call__(self, system, user, schema, seed):
        rng = random.Random(sha256_text(system + user + str(seed)))
        acts = schema["properties"].get("decisions", schema["properties"].get("rulings"))["items"][
            "properties"]["activity_id"]["enum"]
        if "rulings" in schema["properties"]:
            items = [{"activity_id": a, "consensus": rng.choice(["FULL", "MAJORITY", "NONE"]),
                      "verdict": rng.choice(["RESOLVED", "AMBIGUOUS"]), "best_supported": self._assign(rng),
                      "requires_institutional_decision": [], "disagreement_evidence": [
                          {"source_id": rng.choice(self.ids), "explains": "simulado"}],
                      "reasoning_summary": "simulado", "confidence": "low"} for a in acts]
            out = {"scenario_id": "?", "rulings": items}
        else:
            phase2 = "position" in schema["properties"]["decisions"]["items"]["properties"]
            items = []
            for a in acts:
                d = {"activity_id": a, **self._assign(rng),
                     "institutional_ambiguity": rng.random() < 0.2, "alternative_assignments": [],
                     "evidence": [self._cite(rng) for _ in range(rng.randint(0, 3))],
                     "external_principles": [self._cite(rng) for _ in range(rng.randint(0, 2))],
                     "new_authority_justification": "", "reasoning_summary": "simulado",
                     "confidence": rng.choice(["low", "medium", "high"])}
                if phase2:
                    d["position"] = rng.choice(["MAINTAIN", "MODIFY", "AMBIGUOUS"])
                    d["position_justification"] = "simulado"
                items.append(d)
            out = {"scenario_id": "?", "decisions": items}
        text = json.dumps(out, ensure_ascii=False)
        return {"text": text, "model_version": "DRY_RUN", "finish_reason": "STOP",
                "usage": {"prompt_token_count": (len(system) + len(user)) // 4,
                          "candidates_token_count": len(text) // 4, "thoughts_token_count": 0,
                          "cached_content_token_count": 0,
                          "total_token_count": (len(system) + len(user) + len(text)) // 4}}


# ---------------------------------------------------------------- ejecución

def record_cost(r):
    """Coste estimado de una llamada con los precios de config.py del modelo que la hizo."""
    p = config.prices_for(r.get("model"))
    tin = r.get("input_token_count") or 0
    cached = r.get("cached_content_token_count") or 0
    written = r.get("cache_write_token_count") or 0
    tout = r.get("output_token_count") or 0
    factor = config.SERVICE_TIER_FACTOR.get(r.get("service_tier"), 1.0)
    return factor * ((tin - cached - written) * p["input"] + cached * p["cached_input"]
                     + written * p["cache_write"] + tout * p["output"]) / 1e6


class Runner:
    def __init__(self, m, caller, outdir, hashes, dry_run):
        self.m, self.caller, self.outdir, self.hashes, self.dry_run = m, caller, outdir, hashes, dry_run
        self.raw_path = outdir / "raw_results.jsonl"
        self.samples = outdir / "prompt_samples"
        self.samples.mkdir(exist_ok=True)
        self.corpus = corpus_block(m)
        # Coste estimado acumulado (incluye ejecuciones previas si se reanuda).
        self.spent = 0.0
        if self.raw_path.exists():
            for line in self.raw_path.open(encoding="utf-8"):
                self.spent += record_cost(json.loads(line))

    def log(self, record):
        with _write_lock:
            self.spent += record_cost(record)
            with self.raw_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    def call(self, ctx, agent, phase, system, user, schema, kind, extra=None, static_user=None):
        # El control se aplica al material preparado por el experimentador; el texto generado
        # por otros agentes (fases 2 y 3) puede usar libremente cualquier término.
        check = contamination_check(system, user if static_user is None else static_user)
        sample = self.samples / f"{phase}_{agent}.txt"
        with _write_lock:
            if not sample.exists():
                sample.write_text("=== SYSTEM ===\n" + system + "\n\n=== USER ===\n" + user, encoding="utf-8")
        prompt_files = ["common.md", AGENT_PROMPT[agent]]
        prompt_files.append({"phase1": "task_phase1.md", "phase2": "task_phase2.md",
                             "phase2c": "task_phase2_control.md", "phase3": "task_arbiter.md"}[phase])
        parsed = None
        attempt, invalid_n, api_err_n = 0, 0, 0
        while invalid_n < config.MAX_ATTEMPTS and api_err_n < config.MAX_API_ATTEMPTS:
            attempt += 1
            rec = {"execution_id": ctx["execution_id"], "run_id": ctx["run_id"],
                   "scenario_id": ctx["scenario_id"], "model": MODEL if not self.dry_run else "DRY_RUN",
                   "thinking_level": thinking_level(), "temperature": config.TEMPERATURE,
                   "seed": ctx["seed"], "agent": agent, "phase": phase, "attempt": attempt,
                   "timestamp": datetime.now(timezone.utc).isoformat(),
                   "prompt_hashes": {p: self.hashes[f"prompts/{p}"] for p in prompt_files},
                   "request_sha256": sha256_text(system + "\n" + user),
                   "contamination_check": check}
            if extra:
                rec.update(extra)
            t0 = time.time()
            try:
                out = self.caller(system, user, schema, ctx["seed"])
                rec["latency_s"] = round(time.time() - t0, 2)
                rec["model_version"] = out["model_version"]
                rec["finish_reason"] = out["finish_reason"]
                rec.update(out["usage"])
                rec["input_token_count"] = out["usage"]["prompt_token_count"] or 0
                rec["output_token_count"] = ((out["usage"]["candidates_token_count"] or 0) +
                                             (out["usage"]["thoughts_token_count"] or 0))
                rec["response"] = out["text"]
                try:
                    parsed = json.loads(out["text"])
                except (TypeError, json.JSONDecodeError):
                    parsed = None
                rec["validation"] = validate(parsed, ctx["scenario"], self.m, kind)
                ok = rec["validation"].get("json_valid") and rec["validation"].get("activities_ok")
                rec["accepted"] = bool(ok)
                self.log(rec)
                if ok:
                    return parsed
                parsed = None
                invalid_n += 1
            except Exception as exc:  # error de API (503, 429...): se registra y se reintenta
                rec["error"] = f"{type(exc).__name__}: {exc}"
                rec["accepted"] = False
                self.log(rec)
                api_err_n += 1
                time.sleep(min(config.MAX_BACKOFF_S, 10 * 2 ** (api_err_n - 1)) + random.uniform(0, 5))
        return None

    def run(self, run_id, scenario_id):
        if self.spent >= (BUDGET if BUDGET is not None else config.MAX_BUDGET_USD):
            return run_id, scenario_id, f"OMITIDA: tope de presupuesto (USD {self.spent:.2f}); reanudar con --resume"
        s = self.m["scenarios"][scenario_id]
        seed = config.SEED_BASE + run_id
        rng = random.Random(f"{seed}-{scenario_id}")
        ctx = {"execution_id": uuid.uuid4().hex, "run_id": run_id, "scenario_id": scenario_id,
               "scenario": s, "seed": seed}
        acts = s["activities"]
        scen, acts_txt = scenario_text(s), activities_text(self.m, s)

        # Fase 1: decisiones independientes (orden de agentes aleatorizado).
        agents = config.SPECIALIZED_AGENTS + [config.CONTROL_AGENT]
        order = agents[:]
        rng.shuffle(order)
        schema1 = decision_schema(self.m["units"], acts)
        user1 = self.corpus + "\n\n" + fill(self.m["prompts"]["task_phase1.md"],
                                            SCENARIO=scen, ACTIVITIES=acts_txt)
        initial = {}
        for agent in order:
            p = self.call(ctx, agent, "phase1", system_prompt(self.m, agent), user1, schema1, "decision")
            if p is not None:
                initial[agent] = p
        if len(initial) < len(agents):
            return run_id, scenario_id, "INCOMPLETA (fase 1); reanudar con --resume"
        if PHASES == "1":
            return run_id, scenario_id, "completada (solo fase 1)"

        # Fase 2: reconsideración de los especializados con propuestas anónimas A-D.
        schema2 = decision_schema(self.m["units"], acts, phase2=True)
        final = {}
        for agent in [a for a in order if a in config.SPECIALIZED_AGENTS]:
            if agent not in initial:
                continue
            others = {a: p for a, p in initial.items() if a != agent}
            others_txt, mapping = anonymize(others, rng)
            user2 = self.corpus + "\n\n" + fill(
                self.m["prompts"]["task_phase2.md"], SCENARIO=scen, ACTIVITIES=acts_txt,
                OWN_DECISION=json.dumps(strip_identity(initial[agent]), ensure_ascii=False, indent=1),
                OTHER_PROPOSALS=others_txt)
            static2 = self.corpus + "\n\n" + fill(self.m["prompts"]["task_phase2.md"], SCENARIO=scen,
                                                 ACTIVITIES=acts_txt, OWN_DECISION="", OTHER_PROPOSALS="")
            p = self.call(ctx, agent, "phase2", system_prompt(self.m, agent), user2, schema2, "decision",
                          extra={"anonymization": mapping}, static_user=static2)
            if p is not None:
                final[agent] = p
        if len(final) < len(config.SPECIALIZED_AGENTS):
            return run_id, scenario_id, "INCOMPLETA (fase 2); reanudar con --resume"

        # Fase 2c (brazo control): cada especializado reconsidera SIN ver otras propuestas.
        # Misma decisión inicial y mismo esquema; la diferencia de convergencia entre 2 y 2c
        # estima el efecto de la información ajena, separado del efecto de responder dos veces.
        control = {}
        user2c = self.corpus + "\n\n" + fill(
            self.m["prompts"]["task_phase2_control.md"], SCENARIO=scen, ACTIVITIES=acts_txt,
            OWN_DECISION="{{OWN_DECISION}}")
        static2c = user2c.replace("{{OWN_DECISION}}", "")
        for agent in [a for a in order if a in config.SPECIALIZED_AGENTS]:
            own = json.dumps(strip_identity(initial[agent]), ensure_ascii=False, indent=1)
            p = self.call(ctx, agent, "phase2c", system_prompt(self.m, agent),
                          user2c.replace("{{OWN_DECISION}}", own), schema2, "decision", static_user=static2c)
            if p is not None:
                control[agent] = p
        if len(control) < len(config.SPECIALIZED_AGENTS):
            return run_id, scenario_id, "INCOMPLETA (fase 2c); reanudar con --resume"

        # Fase 3: árbitro sobre las propuestas finales de los especializados.
        if final:
            props_txt, mapping = anonymize(final, rng)
            user3 = self.corpus + "\n\n" + fill(self.m["prompts"]["task_arbiter.md"],
                                                SCENARIO=scen, ACTIVITIES=acts_txt, PROPOSALS=props_txt)
            static3 = self.corpus + "\n\n" + fill(self.m["prompts"]["task_arbiter.md"],
                                                 SCENARIO=scen, ACTIVITIES=acts_txt, PROPOSALS="")
            p = self.call(ctx, "ARBITER", "phase3", system_prompt(self.m, "ARBITER"), user3,
                      arbiter_schema(self.m["units"], acts), "arbiter", extra={"anonymization": mapping},
                      static_user=static3)
            if p is None:
                return run_id, scenario_id, "INCOMPLETA (árbitro); reanudar con --resume"
        return run_id, scenario_id, "completada"


def completed_runs(raw_path, phases="all"):
    done, p1 = set(), {}
    if raw_path.exists():
        for line in raw_path.open(encoding="utf-8"):
            r = json.loads(line)
            if r["phase"] == "phase3" and r.get("accepted"):
                done.add((r["run_id"], r["scenario_id"]))
            if r["phase"] == "phase1" and r.get("accepted"):
                p1.setdefault((r["execution_id"], r["run_id"], r["scenario_id"]), set()).add(r["agent"])
    if phases == "1":
        done |= {(run, scen) for (_, run, scen), ags in p1.items() if len(ags) == 5}
    return done


def is_openai(model):
    return model in config.OPENAI_MODELS


def thinking_level():
    """Nivel de razonamiento de la ejecución, con la nomenclatura del proveedor."""
    return config.OPENAI_REASONING_EFFORT if is_openai(MODEL) else config.THINKING_LEVEL


def sdk_version():
    try:
        if is_openai(MODEL):
            from openai import __version__
        else:
            from google.genai import __version__
        return __version__
    except Exception:
        return None


def write_config(outdir, m, hashes, args, scenarios, reps):
    inv_path = HERE / "document_inventory.json"
    inventory = json.loads(read(inv_path)) if inv_path.exists() else []
    cfg = {"label": args.label, "dry_run": args.dry_run,
           "material": args.material, "phases_run": args.phases,
           "budget_usd": BUDGET if BUDGET is not None else config.MAX_BUDGET_USD,
           "created_utc": datetime.now(timezone.utc).isoformat(),
           "model": MODEL, "provider": "openai" if is_openai(MODEL) else "google", "thinking_level": thinking_level(),
           "generation_parameters": {"temperature": config.TEMPERATURE if config.TEMPERATURE is not None
                                     else "default del modelo (no enviado)",
                                     "max_output_tokens": config.MAX_OUTPUT_TOKENS,
                                     "response_mime_type": "application/json",
                                     "response_json_schema": True if not is_openai(MODEL) else "json_schema strict (strict_schema: opcionales anulables, null retirados)",
                                     "seed": (f"SEED_BASE + run_id = {config.SEED_BASE} + run_id" if not is_openai(MODEL)
                                              else f"no enviada (la API Responses no la admite); SEED_BASE + run_id = {config.SEED_BASE} + run_id solo baraja el orden"),
                                     "top_p": "default del modelo (no enviado)",
                                     "store": False if is_openai(MODEL) else None,
                                     "service_tier": config.OPENAI_SERVICE_TIER if is_openai(MODEL) else None,
                                     "max_attempts_invalid_json": config.MAX_ATTEMPTS,
                                     "max_attempts_api_error": config.MAX_API_ATTEMPTS,
                                     "run_policy": "todo o nada: sin los 5 agentes de fase 1, los 4 de fase 2 y los 4 de fase 2c no se llama al árbitro"},
           "phases": {"phase1": "decisión independiente (5 agentes)",
                      "phase2": "reconsideración con propuestas anónimas A-D (4 especializados)",
                      "phase2c": "brazo control: reconsideración sin propuestas ajenas (4 especializados)",
                      "phase3": "árbitro sobre las propuestas de phase2"},
           "quote_verification": "cada cita incluye un fragmento literal; se verifica por coincidencia normalizada con el texto de la fuente",
           "n_scenarios": len(scenarios), "scenarios": scenarios, "n_repetitions": reps,
           "agents": config.SPECIALIZED_AGENTS + [config.CONTROL_AGENT, "ARBITER"],
           "execution_order": "repetición externa; escenarios en orden barajado con semilla por repetición; "
                              "orden de agentes barajado por corrida",
           "prices_usd_per_million": config.prices_for(MODEL),
           "hashes_sha256": hashes,
           "documents": [d for d in inventory if not d["role"].startswith("no_usado")],
           "sdk": {("openai" if is_openai(MODEL) else "google-genai"): sdk_version(), "python": platform.python_version()},
           "reference_raci_used_by_agents": False}
    (outdir / "experiment_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2),
                                                  encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--label", required=True, help="nombre de la ejecución: results/<label>/")
    ap.add_argument("--scenarios", default="all", help="p. ej. S01,S02 (por defecto: todos)")
    ap.add_argument("--reps", type=int, default=config.N_REPETITIONS)
    ap.add_argument("--workers", type=int, default=1, help="corridas en paralelo")
    ap.add_argument("--resume", action="store_true", help="continuar una ejecución existente")
    ap.add_argument("--dry-run", action="store_true", help="sin API; respuestas simuladas")
    ap.add_argument("--material", default="base", help="base o carpeta de una variante (p. ej. ablation_anon)")
    ap.add_argument("--phases", choices=["all", "1"], default="all", help="'1': solo decisión independiente")
    ap.add_argument("--budget", type=float, help="tope de gasto estimado de esta ejecución (USD)")
    ap.add_argument("--model", default=config.MODEL, help=f"modelo (por defecto {config.MODEL}); p. ej. gpt-6-luna")
    args = ap.parse_args()
    global PHASES, BUDGET, MODEL
    PHASES, BUDGET, MODEL = args.phases, args.budget, args.model
    set_material(args.material)

    m = load_material()
    hashes = material_hashes(m)
    scenarios = sorted(m["scenarios"]) if args.scenarios == "all" else args.scenarios.split(",")
    outdir = RESULTS / args.label
    raw = outdir / "raw_results.jsonl"
    if raw.exists() and not args.resume:
        sys.exit(f"{raw} ya existe. No se sobrescribe: use --resume para continuar u otro --label.")
    if args.resume and (outdir / "experiment_config.json").exists():
        old = json.loads(read(outdir / "experiment_config.json"))
        if (old["hashes_sha256"] != hashes or old["model"] != MODEL
                or old.get("material", "base") != args.material or old.get("phases_run", "all") != args.phases):
            sys.exit("Los prompts, el corpus o el modelo cambiaron desde el inicio de esta ejecución. "
                     "No se puede reanudar sin romper la comparabilidad.")
    outdir.mkdir(parents=True, exist_ok=True)
    if not (outdir / "experiment_config.json").exists():
        write_config(outdir, m, hashes, args, scenarios, args.reps)

    caller = DryRunCaller(m) if args.dry_run else (OpenAICaller() if is_openai(MODEL) else GeminiCaller())
    runner = Runner(m, caller, outdir, hashes, args.dry_run)
    done = completed_runs(raw, args.phases)
    tasks = []
    for run_id in range(1, args.reps + 1):
        order = scenarios[:]
        random.Random(config.SEED_BASE + run_id).shuffle(order)
        tasks += [(run_id, s) for s in order if (run_id, s) not in done]
    n_calls = len(tasks) * (5 if args.phases == "1" else 14)
    print(f"Modelo: {MODEL} | corridas pendientes: {len(tasks)} | llamadas previstas: ~{n_calls}"
          f"{' | DRY RUN' if args.dry_run else ''}")

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(runner.run, r, s) for r, s in tasks]
        for i, fut in enumerate(as_completed(futures), 1):
            r, s, status = fut.result()
            print(f"[{i}/{len(tasks)}] corrida {r:02d} {s} {status} | coste estimado acumulado "
                  f"USD {runner.spent:.2f}", flush=True)
    print(f"Resultados en {raw}. Ejecute: python analysis.py --label {args.label}")


if __name__ == "__main__":
    main()
