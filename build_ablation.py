"""Construye el material de la ablación con nombres de unidades anonimizados (ablation_anon/).

Hipótesis: la concentración de responsabilidades en GT/DAS podría deberse en parte al nombre
de la unidad («Administración del SCADA/EMS») y no solo al contenido de sus atribuciones.
Tratamiento: se sustituyen nombres y siglas de todas las unidades por códigos neutros
(U01-U22, asignados al azar con semilla) en el corpus, los identificadores y la lista de
unidades. Se conserva todo el contenido funcional de las atribuciones.

Salidas en ablation_anon/:
  corpus_institutional.md/.json, corpus_external.md/.json, scenarios.json, activities.json,
  prompts/ (copia; frase de perspectiva sin nombre de unidad),
  material.json   correspondencia código -> unidad real. NO se envía a los agentes.
"""
import json
import random
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "ablation_anon"
SEED = 20260926
# Réplica cruzada (--swap): mismo material, pero DAS y MCO intercambian código y posición.
# Separa el efecto del nombre/contenido del efecto del código o de la posición en la lista.
SWAP = False
SWAP_PAIR = ("GT/DAS", "DTE/MCO")

# Unidades sin ficha que aparecen como superiores jerárquicos.
EXTRA_NAMED = {"GERENCIA_TECNICA": "Gerencia Técnica",
               "DIV_SISTEMAS_COMUNICACION": "División de Sistemas de Comunicación"}
# Unidades externas al corpus mencionadas por nombre en algún numeral.
EXTERNAL_PHRASES = [
    (r"(el|al|del)?\s*Departamento de Distribución Regional Capital y Departamentos de Distribución Regional",
     "otras unidades sin ficha en el corpus"),
    (r"(la)?\s*Sección Procesamiento de Datos de Operación", "una de sus secciones (sin ficha en el corpus)"),
]
ARTICLE = {"el": "la unidad", "la": "la unidad", "al": "a la unidad", "del": "de la unidad"}


def build():
    inst = json.loads((HERE / "corpus_institutional.json").read_text(encoding="utf-8"))
    real_codes = [f["unit_code"] for f in inst] + list(EXTRA_NAMED)
    codes = [f"U{i:02d}" for i in range(1, len(real_codes) + 1)]
    rng = random.Random(SEED)
    rng.shuffle(codes)
    code_of = dict(zip(real_codes, codes))
    if SWAP:
        a, b = SWAP_PAIR
        code_of[a], code_of[b] = code_of[b], code_of[a]
    names = {f["unit_code"]: f["unit_name"] for f in inst} | EXTRA_NAMED
    # Nombres más largos primero, para no reemplazar parcialmente un nombre contenido en otro.
    ordered = sorted(names.items(), key=lambda kv: -len(kv[1]))

    def anon_text(text):
        for pat, rep in EXTERNAL_PHRASES:
            text = re.sub(pat, lambda m: (" " if m.group(0)[:1] == " " else "") + rep, text, flags=re.I)
        for real, name in ordered:
            pat = r"\b(?:(El|La|el|la|al|Al|del|Del)\s+)?" + re.escape(name)

            def rep(m, real=real):
                art = (m.group(1) or "").lower()
                out = ARTICLE.get(art, "unidad") + " " + code_of[real]
                return out[0].upper() + out[1:] if (m.group(1) or "")[:1].isupper() else out
            text = re.sub(pat, rep, text, flags=re.I)
        return text

    def anon_org(text):
        items = re.split(r"\s*3\.\d+\.\s*", " " + text)
        out = []
        for i, it in enumerate([x for x in items if x.strip()], 1):
            it = it.strip()
            hit = next((real for real, name in ordered if it.upper().startswith(name.upper())), None)
            out.append(f"3.{i}. " + (f"unidad {code_of[hit]}" if hit else "sección sin ficha en el corpus"))
        return " ".join(out)

    anon = []
    for f in inst:
        c = code_of[f["unit_code"]]
        ents = []
        for e in f["entries"]:
            num = e["id"].split("_", 1)[1]
            txt = anon_org(e["text"]) if e["kind"] == "organización" else anon_text(e["text"])
            ne = {**e, "id": f"{c}_{num}", "text": txt}
            if "verbo_rector" in e:
                ne["verbo_rector"] = e["verbo_rector"]
            ents.append(ne)
        anon.append({"unit_code": c, "unit_id": c, "unit_name": "nombre omitido",
                     "resolution": f["resolution"], "date": f["date"],
                     "source_file": "ficha del Manual de Organización", "entries": ents})
    rng.shuffle(anon)  # el orden de las fichas tampoco revela la estructura original
    if SWAP:  # intercambiar también la posición de las dos fichas en el corpus y en la lista
        i, j = (next(k for k, f in enumerate(anon) if f["unit_code"] == code_of[u]) for u in SWAP_PAIR)
        anon[i], anon[j] = anon[j], anon[i]
    OUT.mkdir(exist_ok=True)
    (OUT / "corpus_institutional.json").write_text(json.dumps(anon, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = ["# CORPUS INSTITUCIONAL",
             "",
             "Fichas del Manual de Organización de ANDE. Texto literal de cada numeral; los nombres y "
             "siglas de las unidades se han sustituido por códigos neutros (U01-U22) y no deben "
             "intentar deducirse. El 'verbo rector' es el inicio literal del numeral.",
             ""]
    for f in anon:
        lines += [f"## Unidad {f['unit_code']}", f"Resolución {f['resolution']}, fecha {f['date']}.", ""]
        for e in f["entries"]:
            tag = f"[{e['id']}] ({e['kind']}, numeral {e['numeral']}"
            tag += f"; verbo rector: {e['verbo_rector']})" if e.get("verbo_rector") else ")"
            lines.append(f"- {tag} {e['text']}")
        lines.append("")
    (OUT / "corpus_institutional.md").write_text("\n".join(lines), encoding="utf-8")

    # Corpus externo: solo CTX_UNIFILAR nombra unidades.
    ext = json.loads((HERE / "sources" / "external_sources.json").read_text(encoding="utf-8"))
    tx = ", ".join(code_of[u] for u in ["GT/TMB", "GT/TES", "GT/TSU", "GT/TCE", "GT/NAC"])
    for s in ext["sources"]:
        if s["source_id"] == "CTX_UNIFILAR":
            s["principle"] = s["principle"].replace(
                "los departamentos regionales de transmisión",
                f"las unidades regionales a cargo de las instalaciones de transmisión en servicio ({tx})")
    ext_lines = ["# CORPUS EXTERNO", "",
                 "Evidencia externa y contexto técnico. Puede justificar principios de diseño o buenas "
                 "prácticas; no puede crear competencias institucionales. Cada entrada indica qué puede "
                 "sustentar (CAN_SUPPORT) y qué no (CANNOT_SUPPORT).", ""]
    for s in ext["sources"]:
        ext_lines += [f"SOURCE_ID: {s['source_id']}", f"SOURCE_TYPE: {s['source_type']}",
                      f"REFERENCE: {s['reference']}", f"PRINCIPLE: {s['principle']}", "CAN_SUPPORT:"] + \
                     [f"  - {x}" for x in s["can_support"]] + ["CANNOT_SUPPORT:"] + \
                     [f"  - {x}" for x in s["cannot_support"]] + [""]
    (OUT / "corpus_external.md").write_text("\n".join(ext_lines), encoding="utf-8")
    (OUT / "corpus_external.json").write_text(json.dumps(ext["sources"], ensure_ascii=False, indent=2), encoding="utf-8")

    for name in ("scenarios.json", "activities.json"):
        shutil.copy(HERE / name, OUT / name)
    pdir = OUT / "prompts"
    pdir.mkdir(exist_ok=True)
    for p in (HERE / "prompts").glob("*.md"):
        if p.name == "judge.md":
            continue
        t = p.read_text(encoding="utf-8")
        t = re.sub(r"no implica favorecer a (?:GT|DTE)/[^.]+\.", "no implica favorecer a ninguna unidad en particular.", t)
        (pdir / p.name).write_text(t, encoding="utf-8")

    import experiment  # para la normalización a departamento
    normalize = {code_of[r]: experiment.NORMALIZE[r] for r in real_codes}
    material = {"_warning": "Correspondencia de la ablación. NO enviar a los agentes; solo para el análisis.",
                "seed": SEED, "code_of_real": code_of, "real_of_code": {v: k for k, v in code_of.items()},
                "normalize": normalize,
                "extra_units": [code_of[u] for u in EXTRA_NAMED] + ["PROPOSED_NEW_AUTHORITY", "UNIDAD_NO_INCLUIDA_EN_CORPUS"]}
    (OUT / "material.json").write_text(json.dumps(material, ensure_ascii=False, indent=2), encoding="utf-8")
    return code_of


def residual_check():
    """Busca restos de nombres o siglas en todo lo que ven los agentes."""
    inst = json.loads((HERE / "corpus_institutional.json").read_text(encoding="utf-8"))
    probes = [f["unit_name"] for f in inst] + list(EXTRA_NAMED.values())
    probes += [f["unit_code"] for f in inst] + ["GT/", "DTE/", "Administración del SCADA", "Oficina de Despacho",
                                                "Estudios Eléctricos", "Estudios Energéticos", "Despacho Regional",
                                                "Operación del Sistema", "Ingeniería de Sistemas de Control",
                                                "Mantenimiento de Sistemas de Control", "Base de Datos del SCADA",
                                                "Aplicativos del SCADA"]
    probes += [r"\bDAS\d?\b", r"\bISC\d?\b", r"\bMCO\b", r"\bODC\b", r"\bDOS\b", r"\bDEL\b", r"\bDEN\b", r"\bDDR\b"]
    hits = []
    files = [OUT / "corpus_institutional.md", OUT / "corpus_external.md", OUT / "scenarios.json",
             OUT / "activities.json"] + sorted((OUT / "prompts").glob("*.md"))
    for p in files:
        txt = p.read_text(encoding="utf-8")
        for pr in probes:
            pat = pr if pr.startswith(r"\b") else re.escape(pr)
            for m in re.finditer(pat, txt, flags=0 if pr.startswith(r"\b") else re.I):
                hits.append(f"{p.relative_to(HERE)}: «{txt[max(0, m.start() - 40):m.end() + 40]}»")
    return hits


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(HERE))
    if "--swap" in sys.argv:
        SWAP, OUT = True, HERE / "ablation_anon_swap"
    build()
    hits = residual_check()
    print(f"Material anonimizado en {OUT}")
    print("Restos de nombres o siglas:", "ninguno" if not hits else "")
    for h in hits:
        print("  ", h.replace("\n", " "))
