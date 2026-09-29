"""Auditoría de la pertinencia de las citas (no solo de su existencia).

Tres capas:
  1. Control determinista: la unidad del numeral institucional citado, ¿figura en la asignación?
  2. Juez LLM ciego (JUDGE_MODEL, distinto del modelo evaluado) sobre una muestra aleatoria
     estratificada: SUPPORTS / PARTIAL / DOES_NOT_SUPPORT y corrección del tipo de afirmación.
  3. Auditoría humana con doble codificación ciega; kappa entre codificadores y entre
     humanos y juez (calibración del juez).

Uso (después de experiment.py; es análisis post hoc y no modifica raw_results.jsonl):
  python citation_audit.py extract --label pilot
  python citation_audit.py sample  --label pilot --n 100          # planillas para 2 codificadores
  python citation_audit.py judge   --label pilot --n 600          # incluye siempre la muestra humana
  python citation_audit.py report  --label pilot                  # kappa y tasas con IC de Wilson

El juez no recibe REFERENCE_RACI ni la identidad del agente.
"""
import argparse
import csv
import hashlib
import json
import math
import os
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import config  # noqa: E402
from analysis import load_records, write_csv, md_table  # noqa: E402
from experiment import NORMALIZE, load_material, load_dotenv, sha256_text, verify_quote  # noqa: E402

SUPPORT = ["SUPPORTS", "PARTIAL", "DOES_NOT_SUPPORT"]
CLAIMS = ["DOCUMENTADO", "INFERIDO", "BUENA_PRACTICA", "PROPUESTO"]
BATCH = 15  # ítems por llamada al juez


def outdir(label):
    return HERE / "results" / label


# ---------------------------------------------------------------- 1. extracción y control determinista

def source_lookup(m):
    inst = json.loads((HERE / "corpus_institutional.json").read_text(encoding="utf-8"))
    ext = json.loads((HERE / "corpus_external.json").read_text(encoding="utf-8"))
    text, unit = {}, {}
    for f in inst:
        for e in f["entries"]:
            text[e["id"]] = f"{f['unit_code']} ({f['unit_name']}), numeral {e['numeral']}: {e['text']}"
            unit[e["id"]] = NORMALIZE.get(f["unit_code"], f["unit_code"])
    for s in ext:
        text[s["source_id"]] = (f"{s['reference']}. PRINCIPLE: {s['principle']} CAN_SUPPORT: "
                                f"{'; '.join(s['can_support'])}. CANNOT_SUPPORT: {'; '.join(s['cannot_support'])}")
    return text, unit


def extract(label):
    m = load_material()
    text, unit = source_lookup(m)
    _, accepted = load_records(outdir(label))
    rows = []
    for r in accepted:
        parsed = json.loads(r["response"])
        for d in parsed.get("decisions") or parsed.get("rulings") or []:
            a = d.get("best_supported", d)
            roles = {k: sorted({NORMALIZE.get(u, u) for u in a.get(k, [])})
                     for k in ("accountable", "responsible", "consulted", "informed")}
            all_units = set().union(*roles.values())
            cites = d.get("evidence", []) + d.get("external_principles", []) + d.get("disagreement_evidence", [])
            for i, c in enumerate(cites):
                sid = c.get("source_id", "")
                cu = unit.get(sid, "")
                row = {"citation_id": sha256_text(f"{r['execution_id']}|{r['agent']}|{r['phase']}|"
                                                  f"{d.get('activity_id')}|{i}|{sid}")[:12],
                       "run_id": r["run_id"], "scenario_id": r["scenario_id"], "agent": r["agent"],
                       "phase": r["phase"], "activity_id": d.get("activity_id"),
                       "activity": m["activities"].get(d.get("activity_id"), {}).get("name", ""),
                       "A": "+".join(roles["accountable"]), "R": "+".join(roles["responsible"]),
                       "C": "+".join(roles["consulted"]), "I": "+".join(roles["informed"]),
                       "source_id": sid, "exists": sid in text,
                       "kind": "institucional" if sid in m["inst_ids"] else "externa" if sid in m["ext_ids"] else "inexistente",
                       "claim_type": c.get("claim_type", ""),
                       "claim": c.get("supports") or c.get("explains", ""),
                       "quote": c.get("quote", ""),
                       "quote_verified": verify_quote(c.get("quote"), text.get(sid, "")) if "quote" in c else "",
                       "source_text": text.get(sid, ""),
                       "cited_unit": cu,
                       # Control determinista: unidad citada ausente de toda la asignación / de A y R.
                       "unit_absent_from_assignment": bool(cu) and cu not in all_units,
                       "unit_absent_from_A_R": bool(cu) and cu not in set(roles["accountable"]) | set(roles["responsible"]),
                       "documentado_non_institutional": c.get("claim_type") == "DOCUMENTADO" and sid not in m["inst_ids"]}
                rows.append(row)
    write_csv(outdir(label) / "citations.csv", rows)
    print(f"{len(rows)} citas extraídas -> citations.csv")
    return rows


def read_csv(path):
    """Lee CSV con ',' o ';' (Excel en español) y con o sin BOM."""
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    delim = csv.Sniffer().sniff(lines[0], delimiters=",;").delimiter if lines else ","
    return list(csv.DictReader(lines, delimiter=delim))


def stratified_sample(rows, n, seed, exclude=()):
    """Muestra aleatoria estratificada proporcional por tipo de afirmación declarado."""
    # Solo citas de agentes (fases 1-2): las del árbitro explican desacuerdos y no declaran tipo.
    pool = [r for r in rows if r["exists"] == "True" and r["citation_id"] not in exclude
            and r["phase"] in ("phase1", "phase2", "phase2c")]
    strata = defaultdict(list)
    for r in pool:
        strata[r["claim_type"]].append(r)
    rng = random.Random(seed)
    total = len(pool)
    chosen = []
    for k in sorted(strata):
        items = strata[k][:]
        rng.shuffle(items)
        take = max(1, round(n * len(items) / total)) if total else 0
        chosen += items[:take]
    rng.shuffle(chosen)
    return chosen[:n]


# ---------------------------------------------------------------- 2. muestra para codificación humana

AUDIT_FIELDS = ["item", "activity", "A", "R", "claim_type", "claim", "source_id", "source_text",
                "support (SUPPORTS/PARTIAL/DOES_NOT_SUPPORT)", "claim_type_correct (SI/NO)", "note"]


def sample(label, n, seed, hide_assignment=False):
    d = outdir(label)
    rows = read_csv(d / "citations.csv")
    chosen = stratified_sample(rows, n, seed)
    key = [{"item": f"H{i + 1:03d}", "citation_id": r["citation_id"]} for i, r in enumerate(chosen)]
    write_csv(d / "audit_key.csv", key)  # correspondencia; no entregar a los codificadores
    sheet = [{"item": k["item"], **{f: r[f] for f in AUDIT_FIELDS[1:8]}} for k, r in zip(key, chosen)]
    if hide_assignment:  # cegamiento estricto: el codificador no ve a qué unidad favorece la cita
        for row in sheet:
            row["A"] = row["R"] = "(oculto)"
    for coder in (1, 2):
        write_csv(d / f"audit_sheet_coder{coder}.csv", sheet, fields=AUDIT_FIELDS)
    print(f"Muestra humana de {len(chosen)} citas (semilla {seed}). Entregar a cada codificador su "
          f"audit_sheet_coderN.csv; no compartir audit_key.csv ni entre codificadores.")


# ---------------------------------------------------------------- 3. juez LLM

def judge_schema(items):
    return {"type": "object", "properties": {"verdicts": {"type": "array", "items": {
        "type": "object",
        "properties": {"item": {"type": "string", "enum": items},
                       "support": {"type": "string", "enum": SUPPORT},
                       "claim_type_correct": {"type": "boolean"},
                       "suggested_claim_type": {"type": "string", "enum": CLAIMS},
                       "rationale": {"type": "string"}},
        "required": ["item", "support", "claim_type_correct", "suggested_claim_type", "rationale"]}}},
        "required": ["verdicts"]}


def judge(label, n, seed):
    from google import genai
    from google.genai import types
    load_dotenv()
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    d = outdir(label)
    rows = {r["citation_id"]: r for r in read_csv(d / "citations.csv")}
    human = [k["citation_id"] for k in read_csv(d / "audit_key.csv")] if (d / "audit_key.csv").exists() else []
    extra = stratified_sample(list(rows.values()), max(0, n - len(human)), seed + 1, exclude=set(human))
    targets = human + [r["citation_id"] for r in extra]
    out_path = d / "judge_results.jsonl"
    done = set()
    if out_path.exists():
        done = {json.loads(line)["citation_id"] for line in out_path.open(encoding="utf-8")}
    todo = [c for c in targets if c not in done]
    system = (HERE / "prompts" / "judge.md").read_text(encoding="utf-8")
    print(f"Juez {config.JUDGE_MODEL}: {len(targets)} citas objetivo, {len(todo)} pendientes")
    for b in range(0, len(todo), BATCH):
        batch = todo[b:b + BATCH]
        labels = [f"J{i + 1:02d}" for i in range(len(batch))]
        items = [{"item": lab, "activity": rows[c]["activity"], "assignment": {"A": rows[c]["A"], "R": rows[c]["R"]},
                  "claim_type": rows[c]["claim_type"], "claim": rows[c]["claim"], "quote": rows[c].get("quote", ""),
                  "source_id": rows[c]["source_id"], "source_text": rows[c]["source_text"]}
                 for lab, c in zip(labels, batch)]
        user = "Evalúa cada ítem.\n\n" + json.dumps(items, ensure_ascii=False, indent=1)
        cfg = types.GenerateContentConfig(
            system_instruction=system, response_mime_type="application/json",
            response_json_schema=judge_schema(labels), seed=config.SEED_BASE,
            thinking_config=types.ThinkingConfig(thinking_level=config.JUDGE_THINKING_LEVEL),
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True))
        for attempt in range(1, config.MAX_API_ATTEMPTS + 1):
            try:
                resp = client.models.generate_content(model=config.JUDGE_MODEL, contents=user, config=cfg)
                verdicts = {v["item"]: v for v in json.loads(resp.text)["verdicts"]}
                break
            except Exception as exc:
                print(f"  reintento {attempt}: {type(exc).__name__}: {str(exc)[:80]}")
                time.sleep(min(config.MAX_BACKOFF_S, 10 * 2 ** (attempt - 1)))
        else:
            sys.exit("El juez no respondió; relanzar el mismo comando para continuar.")
        u = resp.usage_metadata
        with out_path.open("a", encoding="utf-8") as fh:
            for lab, c in zip(labels, batch):
                v = verdicts.get(lab)
                if v is None:
                    continue
                fh.write(json.dumps({"citation_id": c, "judge_model": config.JUDGE_MODEL,
                                     "judge_prompt_sha256": sha256_text(system), **{k: v[k] for k in v if k != "item"},
                                     "batch_input_tokens": u.prompt_token_count,
                                     "batch_output_tokens": (u.candidates_token_count or 0) + (u.thoughts_token_count or 0),
                                     "batch_size": len(batch)}, ensure_ascii=False) + "\n")
        print(f"  lote {b // BATCH + 1}: {len(verdicts)}/{len(batch)} veredictos")


# ---------------------------------------------------------------- 4. informe

def wilson(k, n, z=1.96):
    if n == 0:
        return float("nan"), float("nan")
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, c - h), min(1.0, c + h)


def rate(k, n):
    lo, hi = wilson(k, n)
    return f"{100 * k / n:.1f} % [{100 * lo:.1f}, {100 * hi:.1f}] (n = {n})" if n else "n/d"


def cohen_kappa(a, b):
    pairs = [(x, y) for x, y in zip(a, b) if x and y]
    n = len(pairs)
    if n == 0:
        return float("nan"), 0
    po = sum(x == y for x, y in pairs) / n
    ca, cb = Counter(x for x, _ in pairs), Counter(y for _, y in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return ((po - pe) / (1 - pe) if pe < 1 else float("nan")), n


def report(label, coder_files=None, coder_names=None, kind_label="humana"):
    d = outdir(label)
    rows = read_csv(d / "citations.csv")
    agent_rows = [r for r in rows if r["phase"] in ("phase1", "phase2", "phase2c")]
    L = [f"# Auditoría de pertinencia de citas: {label}", ""]

    inst_doc = [r for r in agent_rows if r["kind"] == "institucional" and r["claim_type"] == "DOCUMENTADO"]
    inst = [r for r in agent_rows if r["kind"] == "institucional"]
    L += ["## 1. Control determinista (todas las citas de agentes, fases 1-2)", "",
          f"- Citas: {len(agent_rows)}; institucionales: {len(inst)}; DOCUMENTADO institucionales: {len(inst_doc)}",
          f"- DOCUMENTADO con fuente no institucional: "
          f"{rate(sum(r['documentado_non_institutional'] == 'True' for r in agent_rows), len(agent_rows))}",
          f"- Cita institucional cuya unidad no figura en la asignación (A, R, C ni I): "
          f"{rate(sum(r['unit_absent_from_assignment'] == 'True' for r in inst), len(inst))}",
          f"- DOCUMENTADO cuya unidad citada no es A ni R: "
          f"{rate(sum(r['unit_absent_from_A_R'] == 'True' for r in inst_doc), len(inst_doc))}",
          "", "El control determinista es un indicio, no un juicio: una cita de otra unidad puede "
          "justificar legítimamente que esa unidad no es la responsable.", ""]

    jpath = d / "judge_results.jsonl"
    judged = {}
    if jpath.exists():
        judged = {j["citation_id"]: j for j in map(json.loads, jpath.open(encoding="utf-8"))}
    by_id = {r["citation_id"]: r for r in rows}
    if judged:
        js = [(by_id[c], j) for c, j in judged.items() if c in by_id]
        model = js[0][1]["judge_model"]
        L += [f"## 2. Juez LLM ciego ({model}), muestra aleatoria estratificada", ""]
        L += [f"- {s}: {rate(sum(j['support'] == s for _, j in js), len(js))}" for s in SUPPORT]
        L += [f"- Tipo de afirmación correcto: {rate(sum(bool(j['claim_type_correct']) for _, j in js), len(js))}", ""]
        tab = []
        for group, keyf in (("tipo declarado", lambda r: r["claim_type"]), ("agente", lambda r: r["agent"]),
                            ("fuente", lambda r: r["kind"])):
            cnt = defaultdict(list)
            for r, j in js:
                cnt[keyf(r)].append(j)
            for k, v in sorted(cnt.items()):
                tab.append({"Grupo": group, "Nivel": k, "n": len(v),
                            "SUPPORTS": f"{100 * sum(x['support'] == 'SUPPORTS' for x in v) / len(v):.0f} %",
                            "DOES_NOT_SUPPORT": f"{100 * sum(x['support'] == 'DOES_NOT_SUPPORT' for x in v) / len(v):.0f} %",
                            "Tipo correcto": f"{100 * sum(bool(x['claim_type_correct']) for x in v) / len(v):.0f} %"})
        L += [md_table(tab, ["Grupo", "Nivel", "n", "SUPPORTS", "DOES_NOT_SUPPORT", "Tipo correcto"]), "",
              "Nota: la muestra es proporcional por tipo declarado; las tasas por agente son descriptivas.", ""]
        write_csv(d / "judge_results.csv", [{**r, **{f"judge_{k}": v for k, v in j.items()}} for r, j in js])

    c1 = d / (coder_files[0] if coder_files else "audit_sheet_coder1.csv")
    c2 = d / (coder_files[1] if coder_files else "audit_sheet_coder2.csv")
    names = coder_names or ["codificador 1", "codificador 2"]
    key = {k["item"]: k["citation_id"] for k in read_csv(d / "audit_key.csv")} if (d / "audit_key.csv").exists() else {}
    if c1.exists() and c2.exists() and key:
        sf, tf = AUDIT_FIELDS[8], AUDIT_FIELDS[9]
        # Emparejar por ítem (no por posición) y normalizar respuestas.
        h1 = {r["item"]: r for r in read_csv(c1)}
        h2 = {r["item"]: r for r in read_csv(c2)}
        items = [i for i in key if i in h1 and i in h2]
        sup = lambda h, i: h[i].get(sf, "").strip().upper()
        typ = lambda h, i: {"SÍ": "SI"}.get(h[i].get(tf, "").strip().upper(), h[i].get(tf, "").strip().upper())
        jsup = lambda i: judged[key[i]]["support"] if key.get(i) in judged else ""
        jtyp = lambda i: ("SI" if judged[key[i]]["claim_type_correct"] else "NO") if key.get(i) in judged else ""
        n1 = sum(bool(sup(h1, i)) for i in items)
        n2 = sum(bool(sup(h2, i)) for i in items)
        L += [f"## 3. Doble codificación ciega ({kind_label})", "",
              f"- Codificadores: {names[0]} (`{c1.name}`, {n1} ítems codificados) y {names[1]} "
              f"(`{c2.name}`, {n2} ítems codificados), sobre {len(items)} ítems de la muestra."]
        if not (n1 and n2):
            L += ["- Planillas todavía sin codificar.", ""]
        else:
            def kap(fa, fb):
                k, n = cohen_kappa([fa(i) for i in items], [fb(i) for i in items])
                both = [i for i in items if fa(i) and fb(i)]
                pa = sum(fa(i) == fb(i) for i in both) / len(both) if both else float("nan")
                return f"κ = {k:.2f}, acuerdo simple {100 * pa:.0f} % (n = {n})"
            L += ["", "| Par | Pertinencia (SUPPORTS/PARTIAL/DOES_NOT_SUPPORT) | Tipo de afirmación correcto |",
                  "|---|---|---|",
                  f"| {names[0]} – {names[1]} | {kap(lambda i: sup(h1, i), lambda i: sup(h2, i))} | "
                  f"{kap(lambda i: typ(h1, i), lambda i: typ(h2, i))} |",
                  f"| {names[0]} – juez | {kap(lambda i: sup(h1, i), jsup)} | {kap(lambda i: typ(h1, i), jtyp)} |",
                  f"| {names[1]} – juez | {kap(lambda i: sup(h2, i), jsup)} | {kap(lambda i: typ(h2, i), jtyp)} |", ""]
            agreed = {i: sup(h1, i) for i in items if sup(h1, i) and sup(h1, i) == sup(h2, i)}
            pairs = [(v, jsup(i)) for i, v in agreed.items() if jsup(i)]
            if pairs:
                k_j, n_j = cohen_kappa([p[0] for p in pairs], [p[1] for p in pairs])
                L += [f"- Juez frente al consenso de ambos codificadores (ítems con acuerdo): κ = {k_j:.2f} "
                      f"(n = {n_j}). Con κ < 0,60, las tasas del juez no deben reportarse como medida validada."]
            for nm, h in ((names[0], h1), (names[1], h2)):
                vals = [sup(h, i) for i in items if sup(h, i)]
                L.append(f"- {nm}: SUPPORTS {rate(vals.count('SUPPORTS'), len(vals))}; "
                         f"DOES_NOT_SUPPORT {rate(vals.count('DOES_NOT_SUPPORT'), len(vals))}")
            jv = [jsup(i) for i in items if jsup(i)]
            L += [f"- Juez sobre los mismos ítems: SUPPORTS {rate(jv.count('SUPPORTS'), len(jv))}; "
                  f"DOES_NOT_SUPPORT {rate(jv.count('DOES_NOT_SUPPORT'), len(jv))}",
                  f"- Consenso de ambos codificadores: SUPPORTS {rate(sum(v == 'SUPPORTS' for v in agreed.values()), len(agreed))}", ""]
    (d / "citation_audit_report.md").write_text("\n".join(L), encoding="utf-8")
    print(f"Informe: {d / 'citation_audit_report.md'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["extract", "sample", "judge", "report"])
    ap.add_argument("--label", required=True)
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--hide-assignment", action="store_true",
                    help="sample: oculta A y R en las planillas (cegamiento estricto)")
    ap.add_argument("--coders", nargs=2, metavar=("PLANILLA1", "PLANILLA2"),
                    help="report: planillas codificadas dentro de results/<label>/")
    ap.add_argument("--coder-names", nargs=2, metavar=("NOMBRE1", "NOMBRE2"))
    ap.add_argument("--coder-kind", default="humana", help="report: p. ej. 'humana' o 'codificadores LLM'")
    a = ap.parse_args()
    if a.step == "extract":
        extract(a.label)
    elif a.step == "sample":
        sample(a.label, a.n, a.seed, a.hide_assignment)
    elif a.step == "judge":
        judge(a.label, a.n, a.seed)
    else:
        report(a.label, a.coders, a.coder_names, a.coder_kind)


if __name__ == "__main__":
    main()
