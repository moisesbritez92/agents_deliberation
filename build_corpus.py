"""Construye el corpus del experimento. No usa la API ni consume tokens.

Salidas:
  extracted/                 texto extraído de cada documento del proyecto (inventario)
  document_inventory.json    documentos inspeccionados, hash y uso asignado
  corpus_institutional.md    fichas del Manual de Organización, una entrada por numeral
  corpus_institutional.json  misma evidencia en formato estructurado (para validar citas)
  corpus_external.md         evidencia externa con CAN_SUPPORT / CANNOT_SUPPORT
  corpus_external.json
  posthoc/reference_raci.json  RACI del artículo. SOLO para análisis post hoc.
"""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXTRACTED = HERE / "extracted"
POSTHOC = HERE / "posthoc"

INSTITUTIONAL_SOURCES = [ROOT / "atribuciones_gt" / "atribuciones_gt.md",
                         ROOT / "atribuciones_dte" / "atribuciones_dte.md"]
ARTICLE_TEX = ROOT / "articulo_atribuciones_scada_ems" / "main.tex"
EXTERNAL_CURATED = HERE / "sources" / "external_sources.json"

# Uso asignado a cada documento del proyecto. Lo no listado queda "no_usado".
DOCUMENT_ROLES = {
    "atribuciones_gt/": "institucional (fichas GT; se usa la transcripción .md)",
    "atribuciones_dte/": "institucional (fichas DTE; se usa la transcripción .md)",
    "articulo_atribuciones_scada_ems/main.tex": "artículo: contexto técnico curado en sources/external_sources.json; RACI extraída a posthoc/",
    "articulo_atribuciones_scada_ems/main.pdf": "artículo compilado (no usado; se usa main.tex)",
    "articulo_atribuciones_scada_ems/evidencia_gobernanza.md": "trazabilidad de evidencia externa (consulta del curador, no se envía a agentes)",
    "casos/": "bibliografía de casos (contenido resumido en corpus_external)",
    "Propuesta_Procedimiento": "EXCLUIDO: propuesta organizativa de una de las partes",
    "flujo_": "EXCLUIDO: flujo organizativo propuesto",
    "resumen_correos/": "EXCLUIDO: posturas de las partes, no evidencia",
    "agente_junior/": "EXCLUIDO: incluye una matriz RACI didáctica",
    "evaluaciones_articulo.md": "EXCLUIDO: revisión del artículo",
    "memory.md": "EXCLUIDO: notas de trabajo con conclusiones del artículo",
}

# Marcadores de la solución del artículo que no deben aparecer en lo que ven los agentes.
FORBIDDEN_MARKERS = ["Autoridad de Cambio", "matriz RACI propuesta", "Reglas de diseño",
                     "R1--R10", "R1-R10", "se propone que", "Se propone que", "A/R",
                     "reference_raci", "REFERENCE_RACI"]

EXTRACT_EXT = {".pdf", ".docx", ".txt", ".md", ".tex"}


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_text(path):
    ext = path.suffix.lower()
    if ext == ".pdf":
        from pypdf import PdfReader
        return "\n".join((page.extract_text() or "") for page in PdfReader(str(path)).pages)
    if ext == ".docx":
        import docx
        d = docx.Document(str(path))
        parts = [p.text for p in d.paragraphs]
        for table in d.tables:
            for row in table.rows:
                parts.append(" | ".join(c.text for c in row.cells))
        return "\n".join(parts)
    return path.read_text(encoding="utf-8", errors="replace")


def role_for(rel):
    for key, role in DOCUMENT_ROLES.items():
        if rel.startswith(key) or key in rel:
            return role
    return "no_usado"


def build_inventory():
    EXTRACTED.mkdir(exist_ok=True)
    inventory = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EXTRACT_EXT:
            continue
        if HERE in path.parents or ".bak" in path.name:
            continue
        rel = path.relative_to(ROOT).as_posix()
        entry = {"path": rel, "sha256": sha256_file(path), "role": role_for(rel)}
        try:
            text = extract_text(path)
            out = EXTRACTED / (rel.replace("/", "__") + ".txt")
            out.write_text(text, encoding="utf-8")
            entry["chars_extracted"] = len(text)
        except Exception as exc:  # documento ilegible: se registra, no se detiene
            entry["extraction_error"] = str(exc)
        inventory.append(entry)
    (HERE / "document_inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    return inventory


# ---------------------------------------------------------------- institucional

HEADER_RE = re.compile(r"Manual de Organizaci[oó]n\s+ANDE.*?Fecha:\s*\S+", re.S)
NUMERAL_RE = re.compile(r"(?<![\d.])(\d)\.(\d+)\.\s")


def parse_fichas(md_path):
    text = md_path.read_text(encoding="utf-8")
    fichas = []
    for block in re.split(r"^# ", text, flags=re.M)[1:]:
        title, body = block.split("\n", 1)
        flat = re.sub(r"\s+", " ", body.replace("---", " "))
        res = re.search(r"Resoluci[oó]n P/N[º°]:\s*(\d+)", flat)
        fecha = re.search(r"Fecha:\s*(\S+)", flat)
        sigla = re.search(r"Sigla:\s*(\S+)", flat)
        name = re.search(r"Fecha:\s*\S+\s+(.*?)\s+Nivel Jer", flat)
        flat = HEADER_RE.sub(" ", flat)
        flat = re.sub(r"<!--.*?-->", " ", flat)
        sub = re.search(r"1\.\s+SUBORDINACI[OÓ]N\s+(.*?)\s+2\.\s+ATRIBUCIONES", flat)
        attr = re.search(r"2\.\s+ATRIBUCIONES\s+(.*?)(?:\s+3\.\s+ORGANIZACI[OÓ]N\s+(.*))?$", flat)
        sig = sigla.group(1)
        unit = sig.split("/")[-1]
        ficha = {"unit_code": sig, "unit_id": unit, "unit_name": name.group(1).strip() if name else title,
                 "resolution": f"P/N.º {res.group(1)}", "date": fecha.group(1),
                 "source_file": md_path.relative_to(ROOT).as_posix() + f" (sección {title.strip()})",
                 "entries": []}
        ficha["entries"].append({"id": f"{unit}_SUB", "numeral": "1", "kind": "subordinación",
                                 "text": sub.group(1).strip()})
        attr_text = attr.group(1)
        pieces = NUMERAL_RE.split(" " + attr_text)
        # pieces: [prefijo, d, n, texto, d, n, texto, ...]
        for i in range(1, len(pieces), 3):
            num = f"{pieces[i]}.{pieces[i + 1]}"
            txt = pieces[i + 2].strip()
            verb = " ".join(re.findall(r"^[\wÁÉÍÓÚÑáéíóúñ/]+(?:\s+y\s+[\wáéíóúñ/]+)?", txt)[:1])
            ficha["entries"].append({"id": f"{unit}_{num.replace('.', '_')}", "numeral": num,
                                     "kind": "atribución", "verbo_rector": verb, "text": txt})
        if attr.group(2):
            ficha["entries"].append({"id": f"{unit}_ORG", "numeral": "3", "kind": "organización",
                                     "text": attr.group(2).strip()})
        fichas.append(ficha)
    return fichas


def write_institutional():
    fichas = []
    for src in INSTITUTIONAL_SOURCES:
        fichas.extend(parse_fichas(src))
    ids = [e["id"] for f in fichas for e in f["entries"]]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, f"identificadores duplicados: {dup}"

    lines = ["# CORPUS INSTITUCIONAL",
             "",
             "Fichas del Manual de Organización de ANDE. Texto literal de cada numeral "
             "(transcripción de las fichas oficiales). El 'verbo rector' es el inicio literal "
             "del numeral y no constituye una interpretación. No se agregan ni se resumen atribuciones.",
             ""]
    for f in fichas:
        lines += [f"## {f['unit_code']}: {f['unit_name']}",
                  f"Resolución {f['resolution']}, fecha {f['date']}. Documento: {f['source_file']}.", ""]
        for e in f["entries"]:
            tag = f"[{e['id']}] ({e['kind']}, numeral {e['numeral']}"
            tag += f"; verbo rector: {e['verbo_rector']})" if e.get("verbo_rector") else ")"
            lines.append(f"- {tag} {e['text']}")
        lines.append("")
    (HERE / "corpus_institutional.md").write_text("\n".join(lines), encoding="utf-8")
    (HERE / "corpus_institutional.json").write_text(
        json.dumps(fichas, ensure_ascii=False, indent=2), encoding="utf-8")
    return fichas


def write_external():
    data = json.loads(EXTERNAL_CURATED.read_text(encoding="utf-8"))
    lines = ["# CORPUS EXTERNO",
             "",
             "Evidencia externa y contexto técnico. Puede justificar principios de diseño o buenas "
             "prácticas; no puede crear competencias institucionales. Cada entrada indica qué puede "
             "sustentar (CAN_SUPPORT) y qué no (CANNOT_SUPPORT).",
             ""]
    for s in data["sources"]:
        lines += [f"SOURCE_ID: {s['source_id']}",
                  f"SOURCE_TYPE: {s['source_type']}",
                  f"REFERENCE: {s['reference']}",
                  f"PRINCIPLE: {s['principle']}",
                  "CAN_SUPPORT:"] + [f"  - {x}" for x in s["can_support"]] + \
                 ["CANNOT_SUPPORT:"] + [f"  - {x}" for x in s["cannot_support"]] + [""]
    (HERE / "corpus_external.md").write_text("\n".join(lines), encoding="utf-8")
    (HERE / "corpus_external.json").write_text(
        json.dumps(data["sources"], ensure_ascii=False, indent=2), encoding="utf-8")
    return data["sources"]


# ---------------------------------------------------------------- RACI de referencia

REF_COLUMNS = ["DAS", "ISC", "MCO", "ODC", "GT_SUPPORT", "ORIGIN", "NEW_AUTHORITY"]


def extract_reference_raci():
    """Lee la Tabla tab:raci del artículo. El orden de filas coincide con ACT01..ACT20
    de activities.json (verificado por nombre al construir)."""
    tex = ARTICLE_TEX.read_text(encoding="utf-8")
    table = tex[tex.index(r"\label{tab:raci}"):]
    table = table[table.index(r"\midrule") + len(r"\midrule"):table.index(r"\bottomrule")]
    rows = []
    for raw in table.split(r"\\"):
        cells = [c.strip() for c in raw.strip().split("&")]
        if len(cells) != 9:
            continue
        activity, marks, rule = cells[0], cells[1:8], cells[8]
        row = {"activity_article": activity, "rule": rule,
               "accountable": [], "responsible": [], "consulted": [], "informed": []}
        for col, mark in zip(REF_COLUMNS, marks):
            if "A" in mark:
                row["accountable"].append(col)
            if "R" in mark:
                row["responsible"].append(col)
            if mark == "C":
                row["consulted"].append(col)
            if mark == "I":
                row["informed"].append(col)
        rows.append(row)
    activities = json.loads((HERE / "activities.json").read_text(encoding="utf-8"))
    assert len(rows) == len(activities), (len(rows), len(activities))
    for row, act in zip(rows, activities):
        row["activity_id"] = act["activity_id"]
    POSTHOC.mkdir(exist_ok=True)
    out = {"_warning": "REFERENCE_RACI: propuesta previa del artículo, no verdad conocida. "
                       "No debe enviarse a ningún agente. Solo para comparación post hoc.",
           "source": ARTICLE_TEX.relative_to(ROOT).as_posix() + " (Tabla tab:raci)",
           "column_mapping": {"GT_SUPPORT": "GT*: DOS/DEL/DEN/DDR según el cambio",
                              "ORIGIN": "unidad que certifica el dato (p. ej., departamento regional de Transmisión, DEL o DOS)",
                              "NEW_AUTHORITY": "AC: Autoridad de Cambio, instancia nueva propuesta"},
           "rows": rows}
    (POSTHOC / "reference_raci.json").write_text(json.dumps(out, ensure_ascii=False, indent=2),
                                                 encoding="utf-8")
    return rows


def leakage_check(paths):
    problems = []
    for p in paths:
        txt = p.read_text(encoding="utf-8")
        for m in FORBIDDEN_MARKERS:
            if m in txt:
                problems.append(f"{p.name}: contiene '{m}'")
    return problems


def main():
    inv = build_inventory()
    fichas = write_institutional()
    ext = write_external()
    ref = extract_reference_raci()
    n_attr = sum(1 for f in fichas for e in f["entries"] if e["kind"] == "atribución")
    print(f"Documentos inspeccionados: {len(inv)} (errores: {sum('extraction_error' in d for d in inv)})")
    print(f"Fichas: {len(fichas)}; numerales de atribución: {n_attr}")
    print(f"Fuentes externas: {len(ext)}")
    print(f"Filas REFERENCE_RACI (posthoc): {len(ref)}")
    agent_facing = [HERE / "corpus_institutional.md", HERE / "corpus_external.md",
                    HERE / "scenarios.json", HERE / "activities.json"] + sorted((HERE / "prompts").glob("*.md"))
    problems = leakage_check([p for p in agent_facing if p.exists()])
    print("Control de contaminación:", "OK" if not problems else problems)


if __name__ == "__main__":
    main()
