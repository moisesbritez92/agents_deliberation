"""Visor de una corrida: reconstruye en Markdown la deliberación completa de un escenario x repetición.

Uso:
  python ver_corrida.py --label smoke3 --run 1 --scenario S01
  python ver_corrida.py --label pilot --all          # una ficha por corrida completa

Salida: results/<label>/corridas/run<NN>_<SXX>.md. No llama a la API ni modifica resultados.
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import config  # noqa: E402
from analysis import key, load_records, md_table  # noqa: E402
from experiment import load_material, set_material, verify_quote  # noqa: E402

SPEC = config.SPECIALIZED_AGENTS
PHASE_TITLE = {"phase1": "Fase 1: decisión independiente",
               "phase2": "Fase 2: reconsideración con propuestas ajenas (deliberación)",
               "phase2c": "Fase 2c: reconsideración sin propuestas ajenas (control)",
               "phase3": "Fase 3: árbitro"}


def units(xs):
    return ", ".join(xs) if xs else "·"


def cite_lines(d, m):
    out = []
    for c in d.get("evidence", []) + d.get("external_principles", []):
        sid = c.get("source_id", "")
        exists = sid in m["source_text"]
        if "quote" in c:
            ok = verify_quote(c.get("quote"), m["source_text"].get(sid, ""))
            q = f" — «{c.get('quote', '')}» {'✓ literal' if ok else '✗ no literal'}"
        else:
            q = ""
        out.append(f"  - `{sid}`{'' if exists else ' (INEXISTENTE)'} [{c.get('claim_type', '')}]: "
                   f"{c.get('supports', '')}{q}")
    return out


def decision_block(d, m, phase2=False):
    L = [f"- **A**: {units(d.get('accountable'))} · **R**: {units(d.get('responsible'))} · "
         f"**C**: {units(d.get('consulted'))} · **I**: {units(d.get('informed'))}",
         f"- Ambigüedad institucional: {'sí' if d.get('institutional_ambiguity') else 'no'} · "
         f"confianza: {d.get('confidence', '')}"]
    if phase2:
        L.insert(0, f"- **Posición: {d.get('position', '')}** — {d.get('position_justification', '')}")
    for alt in d.get("alternative_assignments", []):
        L.append(f"- Alternativa: A = {units(alt.get('accountable'))} — {alt.get('rationale', '')}")
    if d.get("new_authority_justification"):
        L.append(f"- Justificación de nueva autoridad: {d['new_authority_justification']}")
    L.append(f"- Razonamiento: {d.get('reasoning_summary', '')}")
    cites = cite_lines(d, m)
    if cites:
        L += ["- Citas:"] + cites
    return L


def render(label, run, scen, recs, m):
    s = m["scenarios"][scen]
    by = {(r["phase"], r["agent"]): r for r in recs}
    parsed = {k: json.loads(r["response"]) for k, r in by.items()}
    items = {k: {d["activity_id"]: d for d in (p.get("decisions") or p.get("rulings") or [])}
             for k, p in parsed.items()}
    first = min(recs, key=lambda r: r["timestamp"])
    last = max(recs, key=lambda r: r["timestamp"])
    tin = sum(r.get("input_token_count") or 0 for r in recs)
    tout = sum(r.get("output_token_count") or 0 for r in recs)

    L = [f"# Corrida {run:02d} · {scen}: {s['title']}", "",
         f"Ejecución `{first['execution_id']}` · etiqueta `{label}` · modelo `{first['model']}` · "
         f"thinking `{first['thinking_level']}` · semilla {first['seed']} · "
         f"{first['timestamp'][:19]} a {last['timestamp'][11:19]} UTC · {len(recs)} llamadas · "
         f"{tin:,} tokens de entrada y {tout:,} de salida.", "",
         "## Escenario", "", s["technical_description"], "",
         f"- Objetos afectados: {', '.join(s['objects_affected'])}",
         f"- Fase: {s['phase']}",
         f"- Riesgo: {s['risk']}",
         f"- Evidencia disponible en el caso: {', '.join(s['available_evidence'])}", "",
         "Actividades:", ""]
    L += [f"- **{a}**: {m['activities'][a]['name']}" for a in s["activities"]]

    # ---- resumen de la trayectoria de A
    L += ["", "## Resumen: responsable (A) en cada fase", "",
          "Normalizado a departamento. Posición declarada entre paréntesis; ⟶ indica cambio de A "
          "respecto de la fase 1.", ""]
    for a in s["activities"]:
        rows = []
        for ag in SPEC + ["NEUTRAL"]:
            d1 = items.get(("phase1", ag), {}).get(a)
            if d1 is None:
                continue
            k1 = key(d1.get("accountable"))
            row = {"Agente": ag, "Fase 1": k1 + (" (amb.)" if d1.get("institutional_ambiguity") else "")}
            for ph, col in (("phase2", "Fase 2 deliberación"), ("phase2c", "Fase 2c control")):
                d = items.get((ph, ag), {}).get(a)
                if d is None:
                    row[col] = "—"
                    continue
                k = key(d.get("accountable"))
                row[col] = (f"⟶ {k}" if k != k1 else k) + f" ({d.get('position', '')})"
            rows.append(row)
        arb = items.get(("phase3", "ARBITER"), {}).get(a)
        L += [f"### {a}: {m['activities'][a]['name']}", "",
              md_table(rows, ["Agente", "Fase 1", "Fase 2 deliberación", "Fase 2c control"]), ""]
        if arb:
            L += [f"Árbitro: A = **{key(arb['best_supported'].get('accountable'))}** · consenso "
                  f"{arb.get('consensus')} · veredicto **{arb.get('verdict')}**", ""]

    # ---- fases en detalle
    for ph in ("phase1", "phase2", "phase2c"):
        agents = [ag for ag in SPEC + ["NEUTRAL"] if (ph, ag) in by]
        if not agents:
            continue
        L += ["", f"## {PHASE_TITLE[ph]}", ""]
        if ph == "phase2c":
            L += ["Cada agente revisa su decisión inicial sin ver a los demás. Sirve para separar el "
                  "efecto de la deliberación del efecto de responder dos veces.", ""]
        for ag in agents:
            r = by[(ph, ag)]
            L += [f"### Agente {ag}", ""]
            if ph == "phase2" and r.get("anonymization"):
                seen = ", ".join(f"{lab.replace('PROPUESTA ', '')} = {who}"
                                 for lab, who in sorted(r["anonymization"].items()))
                L += [f"Propuestas vistas (anónimas para el agente): {seen}.", ""]
            L += [f"_{r.get('input_token_count', 0):,} tokens de entrada · {r.get('output_token_count', 0):,} de "
                  f"salida · {r.get('latency_s', '')} s · intento {r['attempt']}_", ""]
            for a in s["activities"]:
                d = items[(ph, ag)].get(a)
                if d is None:
                    continue
                L += [f"**{a}**", ""] + decision_block(d, m, phase2=ph != "phase1") + [""]

    # ---- árbitro
    if ("phase3", "ARBITER") in by:
        r = by[("phase3", "ARBITER")]
        seen = ", ".join(f"{lab.replace('PROPUESTA ', '')} = {who}"
                         for lab, who in sorted((r.get("anonymization") or {}).items()))
        L += ["", f"## {PHASE_TITLE['phase3']}", "", f"Propuestas evaluadas (anónimas para el árbitro): {seen}.", ""]
        for a in s["activities"]:
            d = items[("phase3", "ARBITER")].get(a)
            if d is None:
                continue
            b = d.get("best_supported", {})
            L += [f"**{a}** · consenso {d.get('consensus')} · veredicto **{d.get('verdict')}** · "
                  f"confianza {d.get('confidence')}", "",
                  f"- Mejor sustentada: A: {units(b.get('accountable'))} · R: {units(b.get('responsible'))} · "
                  f"C: {units(b.get('consulted'))} · I: {units(b.get('informed'))}"]
            if d.get("best_supported_proposals"):
                L.append(f"- Propuestas que la sostienen: {', '.join(d['best_supported_proposals'])}")
            for q in d.get("requires_institutional_decision", []):
                L.append(f"- Requiere decisión institucional: {q}")
            for e in d.get("disagreement_evidence", []):
                L.append(f"- Evidencia del desacuerdo `{e.get('source_id')}`: {e.get('explains')}")
            L += [f"- Razonamiento: {d.get('reasoning_summary', '')}", ""]
    else:
        L += ["", "_Corrida sin árbitro (incompleta)._"]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--label", required=True)
    ap.add_argument("--run", type=int)
    ap.add_argument("--scenario")
    ap.add_argument("--all", action="store_true", help="generar todas las corridas completas")
    a = ap.parse_args()
    if not a.all and not (a.run and a.scenario):
        ap.error("indique --run y --scenario, o --all")
    outdir = HERE / "results" / a.label
    cfg = json.loads((outdir / "experiment_config.json").read_text(encoding="utf-8"))
    set_material(cfg.get("material", "base"))
    m = load_material()
    _, accepted = load_records(outdir, cfg.get("phases_run", "all"))
    groups = defaultdict(list)
    for r in accepted:
        groups[(r["run_id"], r["scenario_id"])].append(r)
    targets = sorted(groups) if a.all else [(a.run, a.scenario)]
    dest = outdir / "corridas"
    dest.mkdir(exist_ok=True)
    for run, scen in targets:
        if (run, scen) not in groups:
            sys.exit(f"No hay corrida completa para run {run} y escenario {scen} en {a.label}.")
        path = dest / f"run{run:02d}_{scen}.md"
        path.write_text(render(a.label, run, scen, groups[(run, scen)], m), encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()
