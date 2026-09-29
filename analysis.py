"""Análisis del experimento. No llama a la API.

Uso:
  python analysis.py --label smoke
  python analysis.py --label pilot

Definiciones preespecificadas (ver README, sección "Plan de análisis"):
  - Unidad de análisis: la corrida (escenario x repetición). Las decisiones de los agentes
    dentro de una corrida no son independientes (fase 2), por lo que los intervalos se
    obtienen por bootstrap sobre corridas.
  - Decisión principal: conjunto de unidades Accountable normalizado a departamento
    (p. ej., GT/DAS1 -> DAS). La ambigüedad se analiza por separado.
  - Acuerdo: proporción de los 6 pares de agentes especializados con idéntica decisión principal.
  - Consenso estricto: los 4 especializados con idéntica decisión principal.
  - REFERENCE_RACI solo se carga en la sección post hoc, después de calcular todo lo demás.
"""
import argparse
import csv
import json
import math
import random
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import config  # noqa: E402
from experiment import NORMALIZE, load_material, set_material, verify_quote  # noqa: E402

SPEC = config.SPECIALIZED_AGENTS
B = 2000  # remuestreos bootstrap

# Categorías de la REFERENCE_RACI a las que puede corresponder cada unidad normalizada.
REF_CATEGORY = {"DAS": {"DAS"}, "ISC": {"ISC"}, "MCO": {"MCO"}, "ODC": {"ODC"},
                "DOS": {"GT_SUPPORT", "ORIGIN"}, "DEL": {"GT_SUPPORT", "ORIGIN"},
                "DEN": {"GT_SUPPORT"}, "DDR": {"GT_SUPPORT"},
                "TX_REG": {"ORIGIN"}, "DT": {"ORIGIN"}, "OTHER": {"ORIGIN"},
                "NEW_AUTHORITY": {"NEW_AUTHORITY"}}


# ---------------------------------------------------------------- utilidades

def norm_set(units):
    return sorted({NORMALIZE.get(u, u) for u in units or []})


def key(units):
    return "+".join(norm_set(units)) or "NONE"


def entropy(counter):
    n = sum(counter.values())
    return -sum((c / n) * math.log2(c / n) for c in counter.values() if c) if n else float("nan")


def mean(xs):
    xs = [x for x in xs if x is not None and not (isinstance(x, float) and math.isnan(x))]
    return sum(xs) / len(xs) if xs else float("nan")


def bootstrap_ci(per_run, seed=12345):
    """per_run: dict run_id -> valor. IC 95 % percentil del promedio sobre corridas."""
    vals = [v for v in per_run.values() if not math.isnan(v)]
    if len(vals) < 2:
        return (float("nan"), float("nan"))
    rng = random.Random(seed)
    stats = sorted(mean(rng.choices(vals, k=len(vals))) for _ in range(B))
    return stats[int(0.025 * B)], stats[int(0.975 * B) - 1]


def fmt(x, pct=False):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "n/d"
    return f"{100 * x:.1f} %" if pct else f"{x:.3f}"


def write_csv(path, rows, fields=None):
    fields = fields or (list(rows[0].keys()) if rows else [])
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def md_table(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(str(r.get(c, "")) for c in cols) + " |" for r in rows]
    return "\n".join(out)


# ---------------------------------------------------------------- carga

def load_records(outdir, phases="all"):
    raw = [json.loads(line) for line in (outdir / "raw_results.jsonl").open(encoding="utf-8")]
    # Para cada corrida, la ejecución completa más reciente (una reanudación puede repetir corridas).
    by_exec = defaultdict(list)
    for r in raw:
        by_exec[(r["run_id"], r["scenario_id"], r["execution_id"])].append(r)
    chosen = {}
    for (run, scen, ex), recs in by_exec.items():
        complete = any(x["phase"] == "phase3" and x.get("accepted") for x in recs)
        if phases == "1":  # variante de solo fase 1: completa con los 5 agentes aceptados
            complete = len({x["agent"] for x in recs if x["phase"] == "phase1" and x.get("accepted")}) == 5
        last = max(x["timestamp"] for x in recs)
        prev = chosen.get((run, scen))
        if prev is None or (complete, last) > (prev[1], prev[2]):
            chosen[(run, scen)] = (ex, complete, last)
    keep = {v[0] for v in chosen.values() if v[1]}  # solo corridas completas (con árbitro)
    accepted = [r for r in raw if r["execution_id"] in keep and r.get("accepted")
                and r.get("validation", {}).get("json_valid")]
    return raw, accepted


def decision_rows(accepted, m):
    rows = []
    for r in accepted:
        parsed = json.loads(r["response"])
        items = parsed.get("rulings") if r["phase"] == "phase3" else parsed.get("decisions")
        for d in items or []:
            a = d.get("best_supported", d)
            cites = d.get("evidence", []) + d.get("external_principles", []) + d.get("disagreement_evidence", [])
            valid_inst = [c for c in cites if c.get("source_id") in m["inst_ids"]]
            valid_ext = [c for c in cites if c.get("source_id") in m["ext_ids"]]
            invalid = [c for c in cites if c.get("source_id") not in m["inst_ids"] | m["ext_ids"]]
            violations = [c for c in cites if c.get("claim_type") == "DOCUMENTADO"
                          and c.get("source_id") not in m["inst_ids"]]
            has_assignment = bool(a.get("accountable") or a.get("responsible"))
            quoted = [c for c in cites if "quote" in c]
            q_ok = [verify_quote(c.get("quote"), m["source_text"].get(c.get("source_id"), "")) for c in quoted]
            doc_ok = [ok for c, ok in zip(quoted, q_ok) if c.get("claim_type") == "DOCUMENTADO"]
            rows.append({
                "run_id": r["run_id"], "scenario_id": r["scenario_id"], "activity_id": d.get("activity_id"),
                "agent": r["agent"], "phase": r["phase"], "model": r["model"], "seed": r["seed"],
                "accountable_raw": ";".join(a.get("accountable", [])),
                "responsible_raw": ";".join(a.get("responsible", [])),
                "consulted_raw": ";".join(a.get("consulted", [])),
                "informed_raw": ";".join(a.get("informed", [])),
                "A_key": key(a.get("accountable")), "R_key": key(a.get("responsible")),
                "ambiguity": (d.get("verdict") == "AMBIGUOUS") if r["phase"] == "phase3"
                else bool(d.get("institutional_ambiguity")),
                "n_alternatives": len(d.get("alternative_assignments", [])),
                "position": d.get("position", ""), "consensus": d.get("consensus", ""),
                "verdict": d.get("verdict", ""), "confidence": d.get("confidence", ""),
                "n_citations": len(cites), "n_valid_inst": len(valid_inst), "n_valid_ext": len(valid_ext),
                "n_invalid": len(invalid), "n_hierarchy_violations": len(violations),
                "n_quotes": len(quoted), "n_quotes_verified": sum(q_ok),
                "n_documentado": len(doc_ok), "n_documentado_verified": sum(doc_ok),
                "n_inferido": sum(c.get("claim_type") == "INFERIDO" for c in cites),
                "unsupported": has_assignment and not valid_inst and not valid_ext,
                "A_without_inst_evidence": bool(a.get("accountable")) and not valid_inst,
                "new_authority": "PROPOSED_NEW_AUTHORITY" in a.get("accountable", []),
                "cited_ids": ";".join(c.get("source_id", "") for c in cites),
            })
    return rows


# ---------------------------------------------------------------- métricas

def index(rows):
    """(phase, scenario, run, activity) -> {agent: row}"""
    idx = defaultdict(dict)
    for r in rows:
        idx[(r["phase"], r["scenario_id"], r["run_id"], r["activity_id"])][r["agent"]] = r
    return idx


def pair_agreement(cell):
    keys = [cell[a]["A_key"] for a in SPEC if a in cell]
    pairs = list(combinations(keys, 2))
    if len(keys) < 2:
        return None, None
    return sum(x == y for x, y in pairs) / len(pairs), (len(keys) == len(SPEC) and len(set(keys)) == 1)


def scenario_metrics(rows, m):
    idx = index(rows)
    out_scen, out_act = [], []
    overall = {"agree_before": {}, "agree_after": {}, "agree_control": {}, "delta": {},
               "delta_control": {}, "deliberation_effect": {}}
    for sid, s in sorted(m["scenarios"].items()):
        runs = sorted({r["run_id"] for r in rows if r["scenario_id"] == sid})
        if not runs:
            continue
        per_run = {"before": defaultdict(list), "after": defaultdict(list), "control": defaultdict(list)}
        scen_row = {"level": "scenario", "scenario_id": sid, "activity_id": "", "n_runs": len(runs)}
        act_rows = []
        for act in s["activities"]:
            res = {"level": "activity", "scenario_id": sid, "activity_id": act, "n_runs": len(runs)}
            for tag, phase in (("before", "phase1"), ("after", "phase2"), ("control", "phase2c")):
                agr, strict, amb = [], [], []
                a_counter, r_counter = Counter(), Counter()
                for run in runs:
                    cell = idx.get((phase, sid, run, act), {})
                    g, st = pair_agreement(cell)
                    if g is not None:
                        agr.append(g)
                        strict.append(st)
                        per_run[tag][run].append(g)
                    for a in SPEC:
                        if a in cell:
                            a_counter[cell[a]["A_key"]] += 1
                            amb.append(cell[a]["ambiguity"])
                            for u in cell[a]["R_key"].split("+"):
                                r_counter[u] += 1
                res[f"agreement_{tag}"] = mean(agr)
                res[f"strict_consensus_{tag}"] = mean([float(x) for x in strict])
                res[f"ambiguity_rate_{tag}"] = mean([float(x) for x in amb])
                res[f"entropy_A_{tag}"] = entropy(a_counter)
                res[f"n_distinct_A_{tag}"] = len(a_counter)
                res[f"A_distribution_{tag}"] = "; ".join(f"{k}:{v}" for k, v in a_counter.most_common())
                res[f"R_distribution_{tag}"] = "; ".join(f"{k}:{v}" for k, v in r_counter.most_common())
            res["convergence_delta"] = res["agreement_after"] - res["agreement_before"]
            res["convergence_delta_control"] = res["agreement_control"] - res["agreement_before"]
            res["deliberation_effect"] = res["convergence_delta"] - res["convergence_delta_control"]
            # Neutral frente a cada especializado (fase 1).
            for a in SPEC:
                hits = [idx[("phase1", sid, run, act)][a]["A_key"] == idx[("phase1", sid, run, act)]["NEUTRAL"]["A_key"]
                        for run in runs if {a, "NEUTRAL"} <= set(idx.get(("phase1", sid, run, act), {}))]
                res[f"neutral_concordance_{a}"] = mean([float(h) for h in hits])
            # Cambios de posición.
            changes, declared = [], Counter()
            for run in runs:
                c1, c2 = idx.get(("phase1", sid, run, act), {}), idx.get(("phase2", sid, run, act), {})
                for a in SPEC:
                    if a in c1 and a in c2:
                        changes.append(float(c1[a]["A_key"] != c2[a]["A_key"]))
                        declared[c2[a]["position"]] += 1
            res["position_change_rate"] = mean(changes)
            changes_c = [float(idx[("phase1", sid, run, act)][a]["A_key"] != idx[("phase2c", sid, run, act)][a]["A_key"])
                         for run in runs for a in SPEC
                         if a in idx.get(("phase1", sid, run, act), {}) and a in idx.get(("phase2c", sid, run, act), {})]
            res["position_change_rate_control"] = mean(changes_c)
            res["declared_positions"] = "; ".join(f"{k}:{v}" for k, v in declared.most_common())
            # Árbitro.
            arb = [idx[("phase3", sid, run, act)]["ARBITER"] for run in runs
                   if "ARBITER" in idx.get(("phase3", sid, run, act), {})]
            res["arbiter_ambiguous_rate"] = mean([float(x["verdict"] == "AMBIGUOUS") for x in arb])
            res["arbiter_consensus"] = "; ".join(f"{k}:{v}" for k, v in Counter(x["consensus"] for x in arb).most_common())
            res["arbiter_A_distribution"] = "; ".join(f"{k}:{v}" for k, v in Counter(x["A_key"] for x in arb).most_common())
            act_rows.append(res)
        # Agregado por escenario: promedio sobre actividades; IC bootstrap sobre corridas.
        for col in act_rows[0]:
            if col not in scen_row and isinstance(act_rows[0][col], float):
                scen_row[col] = mean([r[col] for r in act_rows])
        for tag in ("before", "after", "control"):
            pr = {run: mean(v) for run, v in per_run[tag].items()}
            overall[f"agree_{tag}"].update({(sid, run): v for run, v in pr.items()})
            lo, hi = bootstrap_ci(pr)
            scen_row[f"agreement_{tag}_ci95"] = f"[{fmt(lo)}, {fmt(hi)}]"
        dr = {run: mean(per_run["after"][run]) - mean(per_run["before"][run])
              for run in per_run["before"] if run in per_run["after"]}
        overall["delta"].update({(sid, run): v for run, v in dr.items()})
        lo, hi = bootstrap_ci(dr)
        scen_row["convergence_delta_ci95"] = f"[{fmt(lo)}, {fmt(hi)}]"
        dc = {run: mean(per_run["control"][run]) - mean(per_run["before"][run])
              for run in per_run["before"] if run in per_run["control"]}
        eff = {run: dr[run] - dc[run] for run in dr if run in dc}
        overall["delta_control"].update({(sid, run): v for run, v in dc.items()})
        overall["deliberation_effect"].update({(sid, run): v for run, v in eff.items()})
        lo, hi = bootstrap_ci(eff)
        scen_row["deliberation_effect_ci95"] = f"[{fmt(lo)}, {fmt(hi)}]"
        out_scen.append(scen_row)
        out_act.extend(act_rows)
    return out_scen, out_act, overall


def agent_changes(rows):
    idx = index(rows)
    out = []
    by_agent = defaultdict(lambda: {"n": 0, "changed": 0, "declared": Counter(), "incons": 0, "modify_other": 0})
    sig = lambda r: tuple(key(r[f"{k}_raw"].split(";")) for k in ("accountable", "responsible", "consulted", "informed"))
    for (phase, sid, run, act), cell in idx.items():
        if phase != "phase2":
            continue
        c1 = idx.get(("phase1", sid, run, act), {})
        for a, r2 in cell.items():
            if a not in c1:
                continue
            changed = c1[a]["A_key"] != r2["A_key"]
            any_change = sig(c1[a]) != sig(r2)
            for k in (a, "ALL"):
                st = by_agent[(k, sid)]
                st["n"] += 1
                st["changed"] += changed
                st["declared"][r2["position"]] += 1
                # Incoherente: MAINTAIN con cambio de A, o MODIFY sin ningún cambio en la matriz.
                # MODIFY que solo cambia R, C o I es legítimo y se cuenta aparte.
                st["incons"] += (r2["position"] == "MAINTAIN" and changed) or (r2["position"] == "MODIFY" and not any_change)
                st["modify_other"] += r2["position"] == "MODIFY" and any_change and not changed
    # Sesgo hacia la propia unidad: P(propia en A | agente) - P(esa unidad en A | NEUTRAL), fase 1.
    bias = {}
    for a in SPEC:
        own, neu = [], []
        for (phase, sid, run, act), cell in idx.items():
            if phase == "phase1" and a in cell and "NEUTRAL" in cell:
                own.append(float(a in cell[a]["A_key"].split("+")))
                neu.append(float(a in cell["NEUTRAL"]["A_key"].split("+")))
        bias[a] = (mean(own), mean(neu), mean(own) - mean(neu), len(own))
    for (a, sid), st in sorted(by_agent.items()):
        row = {"agent": a, "scenario_id": sid, "n_decisions": st["n"],
               "position_change_rate": st["changed"] / st["n"] if st["n"] else float("nan"),
               "declared_MAINTAIN": st["declared"]["MAINTAIN"], "declared_MODIFY": st["declared"]["MODIFY"],
               "declared_AMBIGUOUS": st["declared"]["AMBIGUOUS"],
               "declaration_inconsistency_rate": st["incons"] / st["n"] if st["n"] else float("nan"),
               "modify_R_C_I_only": st["modify_other"]}
        out.append(row)
    return out, bias


def evidence_usage(rows, m):
    use = defaultdict(lambda: Counter())
    for r in rows:
        for sid in filter(None, r["cited_ids"].split(";")):
            use[sid]["total"] += 1
            use[sid][r["phase"]] += 1
            use[sid][f"agent_{r['agent']}"] += 1
    out = []
    for sid, c in sorted(use.items(), key=lambda kv: -kv[1]["total"]):
        kind = "institucional" if sid in m["inst_ids"] else "externa" if sid in m["ext_ids"] else "INEXISTENTE"
        row = {"source_id": sid, "kind": kind, "total": c["total"],
               "phase1": c["phase1"], "phase2": c["phase2"]}
        row.update({f"agent_{a}": c[f"agent_{a}"] for a in SPEC + ["NEUTRAL"]})
        out.append(row)
    return out


def posthoc(rows, m):
    """Comparación POST HOC con REFERENCE_RACI. Se ejecuta al final, tras todas las métricas."""
    ref_path = HERE / "posthoc" / "reference_raci.json"
    if not ref_path.exists():
        return [], "No existe posthoc/reference_raci.json."
    ref = {r["activity_id"]: r for r in json.loads(ref_path.read_text(encoding="utf-8"))["rows"]}

    def match(a_key, ref_a):
        units = [u for u in a_key.split("+") if u != "NONE"]
        if not units:
            return False
        cats = [REF_CATEGORY.get(u, {u}) for u in units]
        return all(c & set(ref_a) for c in cats) and all(any(x in c for c in cats) for x in ref_a)

    groups = {"individual_especializados_f1": lambda r: r["phase"] == "phase1" and r["agent"] in SPEC,
              "neutral_f1": lambda r: r["phase"] == "phase1" and r["agent"] == "NEUTRAL",
              "post_debate_f2": lambda r: r["phase"] == "phase2",
              "control_sin_debate_f2c": lambda r: r["phase"] == "phase2c",
              "arbitro_f3": lambda r: r["phase"] == "phase3"}
    out = []
    for act in sorted({r["activity_id"] for r in rows}):
        row = {"activity_id": act, "activity": m["activities"][act]["name"],
               "REFERENCE_A": "+".join(ref[act]["accountable"])}
        for g, f in groups.items():
            sel = [r for r in rows if r["activity_id"] == act and f(r)]
            row[f"match_{g}"] = mean([float(match(r["A_key"], ref[act]["accountable"])) for r in sel])
            row[f"n_{g}"] = len(sel)
        out.append(row)
    return out, None


# ---------------------------------------------------------------- matriz RACI modal

MODAL_STABILITY_THRESHOLD = 0.60  # celda inestable si el rol modal no alcanza esta frecuencia
ROLE_ORDER = ["A/R", "A", "R", "C", "I", "-"]
UNIT_ORDER = ["DAS", "ISC", "MCO", "ODC", "TX_REG", "DT", "DOS", "DEL", "DEN", "DDR", "OP",
              "GERENCIA_TECNICA", "DIV_SIST_COM", "NEW_AUTHORITY", "OTHER"]
# Columnas de REFERENCE_RACI expresadas como conjuntos de unidades normalizadas.
REF_GROUPS = {"DAS": {"DAS"}, "ISC": {"ISC"}, "MCO": {"MCO"}, "ODC": {"ODC"},
              "GT_SUPPORT": {"DOS", "DEL", "DEN", "DDR"}, "ORIGIN": {"TX_REG", "DT", "OTHER"},
              "NEW_AUTHORITY": {"NEW_AUTHORITY"}}
MODAL_GROUPS = [
    ("especializados_f1", "Especializados, fase 1 (independiente)", lambda r: r["phase"] == "phase1" and r["agent"] in SPEC),
    ("neutral_f1", "Neutral, fase 1", lambda r: r["phase"] == "phase1" and r["agent"] == "NEUTRAL"),
    ("deliberacion_f2", "Especializados, fase 2 (tras deliberación)", lambda r: r["phase"] == "phase2"),
    ("control_f2c", "Especializados, fase 2c (control sin deliberación)", lambda r: r["phase"] == "phase2c"),
    ("arbitro_f3", "Árbitro, fase 3", lambda r: r["phase"] == "phase3"),
]


def decision_sets(r):
    return {k: {u for u in norm_set(r[f"{k}_raw"].split(";")) if u}
            for k in ("accountable", "responsible", "consulted", "informed")}


def role_label(members, sets):
    """Rol de mayor peso de un conjunto de unidades en una decisión."""
    a, r = bool(members & sets["accountable"]), bool(members & sets["responsible"])
    if a and r:
        return "A/R"
    if a:
        return "A"
    if r:
        return "R"
    if members & sets["consulted"]:
        return "C"
    if members & sets["informed"]:
        return "I"
    return "-"


def modal_of(labels):
    c = Counter(labels)
    role = min(c, key=lambda k: (-c[k], ROLE_ORDER.index(k)))
    return role, c[role] / len(labels), "; ".join(f"{k}:{v}" for k, v in sorted(c.items(), key=lambda kv: -kv[1]))


def modal_matrix(rows, columns):
    """columns: dict nombre -> conjunto de unidades. Devuelve filas largas por grupo, escenario y actividad."""
    out = []
    for gid, _, f in MODAL_GROUPS:
        sel = [r for r in rows if f(r)]
        cells = defaultdict(list)
        for r in sel:
            sets = decision_sets(r)
            for scen in ("ALL", r["scenario_id"]):
                for col, members in columns.items():
                    cells[(scen, r["activity_id"], col)].append(role_label(members, sets))
        for (scen, act, col), labels in sorted(cells.items()):
            role, share, dist = modal_of(labels)
            out.append({"group": gid, "scenario_id": scen, "activity_id": act, "column": col,
                        "modal_role": role, "share": round(share, 3), "n": len(labels),
                        "stable": share >= MODAL_STABILITY_THRESHOLD, "distribution": dist})
    return out


def modal_cell(cell):
    if cell is None:
        return ""
    txt = "·" if cell["modal_role"] == "-" else cell["modal_role"]
    if cell["modal_role"] == "-" and cell["stable"]:
        return txt
    return f"{txt} {100 * cell['share']:.0f}%" + ("" if cell["stable"] else " ?")


def modal_raci(rows, m, outdir):
    """Matrices modales por grupo y comparación celda a celda con REFERENCE_RACI (post hoc)."""
    units = modal_matrix(rows, {u: {u} for u in UNIT_ORDER})
    used = [u for u in UNIT_ORDER if any(c["column"] == u and c["modal_role"] != "-" for c in units)]
    units = [c for c in units if c["column"] in used]
    write_csv(outdir / "modal_raci.csv", units)
    acts = sorted({r["activity_id"] for r in rows})
    look = {(c["group"], c["scenario_id"], c["activity_id"], c["column"]): c for c in units}

    L = ["# Matriz RACI modal", "",
         "Cada celda muestra el rol más frecuente de la unidad en la actividad y su frecuencia sobre "
         "todas las decisiones del grupo, acumulando los escenarios en que aparece la actividad. "
         f"'?' marca una celda inestable (rol modal < {100 * MODAL_STABILITY_THRESHOLD:.0f} %); '·' indica "
         "sin rol. Rol por decisión: A/R > A > R > C > I. La matriz modal describe lo que el modelo "
         "produce con este corpus; no es la asignación correcta. El desglose por escenario está en "
         "`modal_raci.csv`.", "",
         "Unidades: DAS, ISC y MCO agrupan sus secciones; TX_REG = departamentos regionales de "
         "Transmisión; NEW_AUTHORITY = PROPOSED_NEW_AUTHORITY; OTHER = unidad no incluida en el corpus.", ""]
    for gid, title, _ in MODAL_GROUPS:
        if not any(c["group"] == gid for c in units):
            continue
        n = max((c["n"] for c in units if c["group"] == gid and c["scenario_id"] == "ALL"), default=0)
        L += [f"## {title}", ""]
        trows = []
        for act in acts:
            row = {"Actividad": f"{act} {m['activities'][act]['name'][:48]}"}
            row.update({u: modal_cell(look.get((gid, "ALL", act, u))) for u in used})
            row["n"] = look.get((gid, "ALL", act, used[0]), {}).get("n", "") if used else ""
            trows.append(row)
        unstable = sum(1 for c in units if c["group"] == gid and c["scenario_id"] == "ALL"
                       and not c["stable"])
        total = sum(1 for c in units if c["group"] == gid and c["scenario_id"] == "ALL")
        L += [md_table(trows, ["Actividad"] + used + ["n"]), "",
              f"Celdas inestables: {unstable} de {total}.", ""]

    # ---- comparación post hoc con REFERENCE_RACI (se carga aquí, al final)
    ref_path = HERE / "posthoc" / "reference_raci.json"
    summary = {}
    if ref_path.exists():
        ref_rows = {r["activity_id"]: r for r in json.loads(ref_path.read_text(encoding="utf-8"))["rows"]}

        def ref_role(row, col):
            sets = {k: set(row[k]) for k in ("accountable", "responsible", "consulted", "informed")}
            return role_label({col}, sets)

        refm = modal_matrix(rows, REF_GROUPS)
        write_csv(outdir / "modal_raci_vs_reference.csv",
                  [{**c, "reference_role": ref_role(ref_rows[c["activity_id"]], c["column"])}
                   for c in refm if c["scenario_id"] == "ALL"])
        rlook = {(c["group"], c["activity_id"], c["column"]): c for c in refm if c["scenario_id"] == "ALL"}
        cols = list(REF_GROUPS)
        L += ["## Comparación celda a celda con REFERENCE_RACI (post hoc)", "",
              "REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Columnas "
              "agrupadas como en el artículo: GT_SUPPORT = DOS, DEL, DEN, DDR; ORIGIN = TX_REG, DT, "
              "OTHER; NEW_AUTHORITY = Autoridad de Cambio. DEL y DOS se cuentan en GT_SUPPORT aunque "
              "el artículo también los admite como origen de parámetros (aproximación).", "",
              "Formato: `=` coincide con la referencia; `≠ X (ref Y)` difiere, con el rol modal X y el de la referencia Y.", ""]
        comp_rows = []
        for gid, title, _ in MODAL_GROUPS:
            cells = [(a, c) for a in acts for c in cols if (gid, a, c) in rlook]
            if not cells:
                continue
            exact = [rlook[(gid, a, c)]["modal_role"] == ref_role(ref_rows[a], c) for a, c in cells]
            a_cells = [(a, c) for a, c in cells if "A" in ref_role(ref_rows[a], c)]
            a_ok = [rlook[(gid, a, c)]["modal_role"] in ("A", "A/R") for a, c in a_cells]
            core = lambda x: x if x in ("A/R", "A", "R") else "·"  # C, I y sin rol, una misma clase
            core_ok = [core(rlook[(gid, a, c)]["modal_role"]) == core(ref_role(ref_rows[a], c)) for a, c in cells]
            summary[gid] = {"exact_cell_agreement": mean([float(x) for x in exact]),
                            "accountable_agreement": mean([float(x) for x in a_ok]),
                            "core_cell_agreement": mean([float(x) for x in core_ok]),
                            "unstable_cells": sum(not rlook[(gid, a, c)]["stable"] for a, c in cells),
                            "n_cells": len(cells)}
            comp_rows.append({"Grupo": title, "Celdas idénticas": fmt(summary[gid]["exact_cell_agreement"], True),
                              "Celdas A/R idénticas": fmt(summary[gid]["core_cell_agreement"], True),
                              "A de la referencia recuperada": fmt(summary[gid]["accountable_agreement"], True),
                              "Celdas inestables": f"{summary[gid]['unstable_cells']} de {len(cells)}"})
        L += [md_table(comp_rows, ["Grupo", "Celdas idénticas", "Celdas A/R idénticas",
                                   "A de la referencia recuperada", "Celdas inestables"]), "",
              "Celdas idénticas: mismo rol exacto. Celdas A/R idénticas: mismo rol ejecutivo (A/R, A, R), "
              "tratando C, I y sin rol como una misma clase. A recuperada: proporción de celdas A de la "
              "referencia en las que el rol modal incluye A.", ""]
        for gid, title, _ in MODAL_GROUPS:
            if gid not in summary:
                continue
            trows = []
            for a in acts:
                row = {"Actividad": f"{a} {m['activities'][a]['name'][:40]}"}
                for c in cols:
                    cell, ref = rlook.get((gid, a, c)), ref_role(ref_rows[a], c)
                    if cell is None:
                        row[c] = ""
                    elif cell["modal_role"] == ref:
                        row[c] = "=" + ("" if cell["stable"] else " ?")
                    else:
                        row[c] = f"≠ {cell['modal_role']} (ref {ref})" + ("" if cell["stable"] else " ?")
                trows.append(row)
            L += [f"### {title} frente a REFERENCE_RACI", "", md_table(trows, ["Actividad"] + cols), ""]
        ref_table = [{"Actividad": f"{a} {m['activities'][a]['name'][:40]}",
                      **{c: ref_role(ref_rows[a], c).replace("-", "·") for c in cols}} for a in acts]
        L += ["### REFERENCE_RACI (artículo), en las mismas columnas", "",
              md_table(ref_table, ["Actividad"] + cols), ""]
    (outdir / "modal_raci.md").write_text("\n".join(L), encoding="utf-8")
    return summary


# ---------------------------------------------------------------- informe

def costs(raw):
    tin = sum(r.get("input_token_count") or 0 for r in raw)
    tout = sum(r.get("output_token_count") or 0 for r in raw)
    tth = sum(r.get("thoughts_token_count") or 0 for r in raw)
    tcache = sum(r.get("cached_content_token_count") or 0 for r in raw)
    # Precio del modelo que hizo cada llamada (mismo cálculo que experiment.record_cost).
    cost = 0.0
    for r in raw:
        p = config.prices_for(r.get("model"))
        i, c = r.get("input_token_count") or 0, r.get("cached_content_token_count") or 0
        w, o = r.get("cache_write_token_count") or 0, r.get("output_token_count") or 0
        f = config.SERVICE_TIER_FACTOR.get(r.get("service_tier"), 1.0)
        cost += f * ((i - c - w) * p["input"] + c * p["cached_input"] + w * p["cache_write"] + o * p["output"]) / 1e6
    return {"total_input_tokens": tin, "total_output_tokens": tout, "thoughts_tokens": tth,
            "cached_input_tokens": tcache, "estimated_cost_usd": round(cost, 4)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", required=True)
    args = ap.parse_args()
    outdir = HERE / "results" / args.label
    cfg = json.loads((outdir / "experiment_config.json").read_text(encoding="utf-8"))
    set_material(cfg.get("material", "base"))
    m = load_material()
    raw, accepted = load_records(outdir, cfg.get("phases_run", "all"))
    rows = decision_rows(accepted, m)
    write_csv(outdir / "decisions.csv", rows)

    scen, acts, overall = scenario_metrics(rows, m)
    write_csv(outdir / "scenario_summary.csv", scen + acts,
              fields=list(dict.fromkeys([k for r in scen + acts for k in r])))
    changes, bias = agent_changes(rows)
    write_csv(outdir / "agent_changes.csv", changes)
    ev = evidence_usage(rows, m)
    write_csv(outdir / "evidence_usage.csv", ev)

    # Integridad y evidencia.
    calls = len(raw)
    api_errors = sum(1 for r in raw if r.get("error"))
    json_ok = [r["validation"].get("json_valid") for r in raw if "validation" in r]
    acts_ok = [r["validation"].get("activities_ok") for r in raw if "validation" in r]
    n_cit = sum(r["n_citations"] for r in rows)
    n_inv = sum(r["n_invalid"] for r in rows)
    agent_rows = [r for r in rows if r["phase"] in ("phase1", "phase2", "phase2c")]
    n_q = sum(r["n_quotes"] for r in agent_rows)
    n_d = sum(r["n_documentado"] for r in agent_rows)
    contamination = Counter(r.get("contamination_check") for r in raw)
    expected_calls = cfg["n_scenarios"] * cfg["n_repetitions"] * (5 if cfg.get("phases_run", "all") == "1" else 14)
    final_phase = "phase1" if cfg.get("phases_run", "all") == "1" else "phase3"
    runs_complete = len({(r["run_id"], r["scenario_id"]) for r in accepted if r["phase"] == final_phase})
    cost = costs(raw)

    ob = {k: mean(list(v.values())) for k, v in overall.items()}
    ci = {k: bootstrap_ci({i: x for i, x in enumerate(v.values())}) for k, v in overall.items()}
    summary = [
        ("model", cfg["model"]), ("thinking_level", cfg["thinking_level"]), ("dry_run", cfg["dry_run"]),
        ("n_scenarios", cfg["n_scenarios"]), ("n_repetitions", cfg["n_repetitions"]),
        ("runs_complete", runs_complete), ("api_calls_logged", calls), ("api_errors", api_errors),
        ("json_valid_rate", mean([float(bool(x)) for x in json_ok])),
        ("activities_complete_rate", mean([float(bool(x)) for x in acts_ok])),
        ("contamination_check", dict(contamination)),
        ("AGREEMENT_BEFORE", ob["agree_before"]), ("AGREEMENT_AFTER", ob["agree_after"]),
        ("CONVERGENCE_DELTA", ob["delta"]), ("CONVERGENCE_DELTA_ci95", ci["delta"]),
        ("AGREEMENT_CONTROL", ob["agree_control"]),
        ("CONVERGENCE_DELTA_CONTROL", ob["delta_control"]), ("CONVERGENCE_DELTA_CONTROL_ci95", ci["delta_control"]),
        ("DELIBERATION_EFFECT", ob["deliberation_effect"]), ("DELIBERATION_EFFECT_ci95", ci["deliberation_effect"]),
        ("STRICT_CONSENSUS_RATE_before", mean([r["strict_consensus_before"] for r in acts])),
        ("STRICT_CONSENSUS_RATE_after", mean([r["strict_consensus_after"] for r in acts])),
        ("POSITION_CHANGE_RATE", mean([r["position_change_rate"] for r in acts])),
        ("POSITION_CHANGE_RATE_CONTROL", mean([r["position_change_rate_control"] for r in acts])),
        ("AMBIGUITY_RATE_before", mean([r["ambiguity_rate_before"] for r in acts])),
        ("AMBIGUITY_RATE_after", mean([r["ambiguity_rate_after"] for r in acts])),
        ("ARBITER_AMBIGUOUS_RATE", mean([r["arbiter_ambiguous_rate"] for r in acts])),
        ("ENTROPY_A_before_mean", mean([r["entropy_A_before"] for r in acts])),
        ("ENTROPY_A_after_mean", mean([r["entropy_A_after"] for r in acts])),
        ("EVIDENCE_VALIDITY_RATE", 1 - n_inv / n_cit if n_cit else float("nan")),
        ("UNSUPPORTED_CLAIM_RATE", mean([float(r["unsupported"]) for r in agent_rows])),
        ("A_WITHOUT_INSTITUTIONAL_EVIDENCE_RATE", mean([float(r["A_without_inst_evidence"]) for r in agent_rows])),
        ("HIERARCHY_VIOLATION_RATE", mean([float(r["n_hierarchy_violations"] > 0) for r in agent_rows])),
        ("QUOTE_VERIFIED_RATE", sum(r["n_quotes_verified"] for r in agent_rows) / n_q if n_q else float("nan")),
        ("DOCUMENTADO_QUOTE_VERIFIED_RATE", sum(r["n_documentado_verified"] for r in agent_rows) / n_d if n_d else float("nan")),
        ("INFERIDO_SHARE", sum(r["n_inferido"] for r in agent_rows) / sum(r["n_citations"] for r in agent_rows)
         if agent_rows else float("nan")),
        ("NEW_AUTHORITY_RATE", mean([float(r["new_authority"]) for r in agent_rows])),
    ] + [(f"HOME_BIAS_{a}", bias[a][2]) for a in SPEC] + list(cost.items())
    write_csv(outdir / "summary.csv", [{"metric": k, "value": v} for k, v in summary])

    # Post hoc, al final.
    ph, ph_err = posthoc(rows, m)
    if ph:
        write_csv(outdir / "posthoc_comparison.csv", ph)
    modal_summary = modal_raci(rows, m, outdir)

    # ------------------------------------------------ informe Markdown
    S = dict(summary)
    L = []
    title = "Informe del experimento" + (" (SIMULACIÓN, DATOS NO REALES)" if cfg["dry_run"] else "")
    L += [f"# {title}: {args.label}", ""]
    if cfg["dry_run"]:
        L += ["> **Advertencia:** ejecución en modo `--dry-run`. Las respuestas son aleatorias y solo "
              "sirven para verificar el pipeline. Ninguna cifra de este informe tiene valor empírico.", ""]
    L += ["## 1. Configuración experimental", "",
          f"- Etiqueta: `{cfg['label']}`; creada: {cfg['created_utc']}",
          f"- Escenarios: {cfg['n_scenarios']} ({', '.join(cfg['scenarios'])}); repeticiones: {cfg['n_repetitions']}",
          f"- Agentes: {', '.join(cfg['agents'])}",
          f"- Semillas: {cfg['generation_parameters']['seed']}",
          f"- Orden de ejecución: {cfg['execution_order']}",
          f"- Parámetros de generación: `{json.dumps(cfg['generation_parameters'], ensure_ascii=False)}`",
          f"- SDK: {cfg['sdk']}", "",
          "## 2. Documentos utilizados", ""]
    used = [d for d in cfg["documents"] if not d["role"].startswith("EXCLUIDO")]
    excluded = [d for d in cfg["documents"] if d["role"].startswith("EXCLUIDO")]
    L += [f"- `{d['path']}`: {d['role']}" for d in used]
    L += ["", "Documentos inspeccionados y excluidos del contexto de los agentes:", ""]
    L += [f"- `{d['path']}`: {d['role'][len('EXCLUIDO: '):]}" for d in excluded]
    L += ["", "## 3. Modelo", "", f"`{cfg['model']}`, thinking_level = `{cfg['thinking_level']}`. "
          "El mismo modelo para todos los agentes y el árbitro.", "",
          "## 4. Número de llamadas e integridad", "",
          f"- Llamadas registradas (incluidos reintentos): {calls}; previstas sin reintentos: {expected_calls}",
          f"- Corridas completas (con árbitro): {runs_complete} de {cfg['n_scenarios'] * cfg['n_repetitions']}",
          f"- Errores de API: {api_errors}",
          f"- JSON válido: {fmt(S['json_valid_rate'], True)}; actividades completas: {fmt(S['activities_complete_rate'], True)}",
          f"- Control de contaminación del material enviado: {dict(contamination)}. "
          "REFERENCE_RACI no se envió a ningún agente (el script de ejecución no lee `posthoc/`).", "",
          "## 5. Tokens consumidos", "",
          f"- Entrada: {cost['total_input_tokens']:,} (de ellos en caché: {cost['cached_input_tokens']:,})",
          f"- Salida: {cost['total_output_tokens']:,} (razonamiento: {cost['thoughts_tokens']:,})", "",
          "## 6. Coste aproximado", "",
          f"USD {cost['estimated_cost_usd']} con precios configurados para `{cfg['model']}` de "
          f"{config.prices_for(cfg['model'])['input']} / {config.prices_for(cfg['model'])['output']} / "
          f"{config.prices_for(cfg['model'])['cached_input']} USD por millón "
          "(entrada / salida / entrada en caché). Verificar precios vigentes antes de reportar.", ""]

    def act_table(tag):
        return md_table([{"Escenario": r["scenario_id"], "Actividad": r["activity_id"],
                          "Distribución de A": r[f"A_distribution_{tag}"],
                          "Acuerdo": fmt(r[f"agreement_{tag}"], True),
                          "Ambigüedad": fmt(r[f"ambiguity_rate_{tag}"], True),
                          "H(A) bits": fmt(r[f"entropy_A_{tag}"])} for r in acts],
                        ["Escenario", "Actividad", "Distribución de A", "Acuerdo", "Ambigüedad", "H(A) bits"])

    L += ["## 7. Decisiones iniciales (fase 1, especializados)", "", act_table("before"), "",
          "Concordancia del agente neutral con cada especializado (misma decisión principal, fase 1):", "",
          md_table([{"Escenario": r["scenario_id"], **{a: fmt(r[f"neutral_concordance_{a}"], True) for a in SPEC}}
                    for r in scen], ["Escenario"] + SPEC), "",
          "## 8. Decisiones posteriores al debate (fase 2)", "", act_table("after"), "",
          "## 9. Consenso", "",
          md_table([{"Escenario": r["scenario_id"], "Acuerdo antes": fmt(r["agreement_before"], True),
                     "IC95 antes": r["agreement_before_ci95"], "Acuerdo después": fmt(r["agreement_after"], True),
                     "IC95 después": r["agreement_after_ci95"], "CONVERGENCE_DELTA": fmt(r["convergence_delta"]),
                     "IC95 delta": r["convergence_delta_ci95"],
                     "Consenso estricto antes": fmt(r["strict_consensus_before"], True),
                     "Consenso estricto después": fmt(r["strict_consensus_after"], True)} for r in scen],
                   ["Escenario", "Acuerdo antes", "IC95 antes", "Acuerdo después", "IC95 después",
                    "CONVERGENCE_DELTA", "IC95 delta", "Consenso estricto antes", "Consenso estricto después"]), "",
          f"Global: acuerdo {fmt(S['AGREEMENT_BEFORE'], True)} → {fmt(S['AGREEMENT_AFTER'], True)}; "
          f"CONVERGENCE_DELTA = {fmt(S['CONVERGENCE_DELTA'])} (IC95 bootstrap sobre corridas "
          f"[{fmt(S['CONVERGENCE_DELTA_ci95'][0])}, {fmt(S['CONVERGENCE_DELTA_ci95'][1])}]). "
          "Mayor consenso no implica mayor corrección.", "",
          "**Brazo control (fase 2c):** los mismos agentes reconsideran su decisión inicial sin ver "
          "propuestas ajenas. DELIBERATION_EFFECT = CONVERGENCE_DELTA − CONVERGENCE_DELTA_CONTROL "
          "estima la convergencia atribuible a la información de los demás, descontando la que "
          "produce el solo hecho de responder dos veces.", "",
          f"- Acuerdo en el control: {fmt(S['AGREEMENT_CONTROL'], True)}; CONVERGENCE_DELTA_CONTROL = "
          f"{fmt(S['CONVERGENCE_DELTA_CONTROL'])} (IC95 [{fmt(S['CONVERGENCE_DELTA_CONTROL_ci95'][0])}, "
          f"{fmt(S['CONVERGENCE_DELTA_CONTROL_ci95'][1])}])",
          f"- DELIBERATION_EFFECT = {fmt(S['DELIBERATION_EFFECT'])} (IC95 [{fmt(S['DELIBERATION_EFFECT_ci95'][0])}, "
          f"{fmt(S['DELIBERATION_EFFECT_ci95'][1])}])",
          f"- Cambio de A en el control: {fmt(S['POSITION_CHANGE_RATE_CONTROL'], True)} frente a "
          f"{fmt(S['POSITION_CHANGE_RATE'], True)} con deliberación", "",
          md_table([{"Escenario": r["scenario_id"], "Acuerdo control": fmt(r["agreement_control"], True),
                     "Delta control": fmt(r["convergence_delta_control"]),
                     "Efecto deliberación": fmt(r["deliberation_effect"]),
                     "IC95 efecto": r["deliberation_effect_ci95"]} for r in scen],
                   ["Escenario", "Acuerdo control", "Delta control", "Efecto deliberación", "IC95 efecto"]), "",
          "## 10. Ambigüedad", "",
          f"- AMBIGUITY_RATE antes: {fmt(S['AMBIGUITY_RATE_before'], True)}; después: {fmt(S['AMBIGUITY_RATE_after'], True)}",
          f"- Árbitro, veredicto AMBIGUOUS: {fmt(S['ARBITER_AMBIGUOUS_RATE'], True)}",
          f"- PROPOSED_NEW_AUTHORITY como A: {fmt(S['NEW_AUTHORITY_RATE'], True)} de las decisiones de agentes", "",
          md_table([{"Escenario": r["scenario_id"], "Actividad": r["activity_id"],
                     "Árbitro: consenso": r["arbiter_consensus"], "Árbitro: A": r["arbiter_A_distribution"],
                     "Árbitro AMBIGUOUS": fmt(r["arbiter_ambiguous_rate"], True)} for r in acts],
                   ["Escenario", "Actividad", "Árbitro: consenso", "Árbitro: A", "Árbitro AMBIGUOUS"]), "",
          "## 11. Entropía de la autoridad (A)", "",
          f"Media por actividad: {fmt(S['ENTROPY_A_before_mean'])} bits antes y {fmt(S['ENTROPY_A_after_mean'])} bits "
          "después. Entropía baja indica asignación estable; alta, sensible a la interpretación. "
          "No es una medida de corrección.", "",
          "## 12. Cambios de posición", "",
          f"POSITION_CHANGE_RATE global: {fmt(S['POSITION_CHANGE_RATE'], True)}.", "",
          md_table([{"Agente": r["agent"], "Escenario": r["scenario_id"], "n": r["n_decisions"],
                     "Cambio de A": fmt(r["position_change_rate"], True), "MAINTAIN": r["declared_MAINTAIN"],
                     "MODIFY": r["declared_MODIFY"], "AMBIGUOUS": r["declared_AMBIGUOUS"],
                     "Declaración incoherente": fmt(r["declaration_inconsistency_rate"], True)}
                    for r in changes if r["agent"] != "ALL"],
                   ["Agente", "Escenario", "n", "Cambio de A", "MAINTAIN", "MODIFY", "AMBIGUOUS",
                    "Declaración incoherente"]), "",
          "Sesgo hacia la propia unidad (fase 1): P(unidad propia en A | agente) − P(misma unidad en A | NEUTRAL).", "",
          md_table([{"Agente": a, "P propia": fmt(bias[a][0], True), "P neutral": fmt(bias[a][1], True),
                     "Diferencia": fmt(bias[a][2]), "n": bias[a][3]} for a in SPEC],
                   ["Agente", "P propia", "P neutral", "Diferencia", "n"]), "",
          "## 13. Evidencia más utilizada", "",
          f"- EVIDENCE_VALIDITY_RATE: {fmt(S['EVIDENCE_VALIDITY_RATE'], True)} de {n_cit} citas",
          f"- UNSUPPORTED_CLAIM_RATE (asignación sin ninguna cita válida): {fmt(S['UNSUPPORTED_CLAIM_RATE'], True)}",
          f"- A sin evidencia institucional válida: {fmt(S['A_WITHOUT_INSTITUTIONAL_EVIDENCE_RATE'], True)}",
          f"- Violación de jerarquía (DOCUMENTADO con fuente no institucional): {fmt(S['HIERARCHY_VIOLATION_RATE'], True)}",
          f"- Cita textual verificada en la fuente: {fmt(S['QUOTE_VERIFIED_RATE'], True)} de {n_q}; "
          f"en afirmaciones DOCUMENTADO: {fmt(S['DOCUMENTADO_QUOTE_VERIFIED_RATE'], True)} de {n_d}",
          f"- Proporción de citas INFERIDO: {fmt(S['INFERIDO_SHARE'], True)}",
          "La verificación textual prueba que el fragmento existe en la fuente citada, no que nombre la "
          "actividad; la pertinencia se audita con citation_audit.py.", "",
          md_table(ev[:20], ["source_id", "kind", "total", "phase1", "phase2"]), ""]
    L += ["## 14. Comparación post hoc con REFERENCE_RACI", "",
          "REFERENCE_RACI es la propuesta previa del artículo, no una verdad conocida. Se cargó solo "
          "después de calcular todas las métricas anteriores. Coincidencia = misma unidad A, con la "
          "correspondencia de columnas indicada en el README (Origen, GT*, AC).", ""]
    L += [md_table([{k: (fmt(v, True) if k.startswith("match_") else v) for k, v in r.items()
                     if not k.startswith("n_")} for r in ph],
                   ["activity_id", "activity", "REFERENCE_A", "match_individual_especializados_f1",
                    "match_neutral_f1", "match_post_debate_f2", "match_control_sin_debate_f2c",
                    "match_arbitro_f3"]) if ph else ph_err, ""]
    L += ["### Matriz RACI modal", "",
          "Matrices completas por grupo (A, R, C, I por unidad, con frecuencia y celdas inestables) en "
          "`modal_raci.md` y `modal_raci.csv`. Resumen de la comparación celda a celda:", "",
          md_table([{"Grupo": g, "Celdas idénticas": fmt(v["exact_cell_agreement"], True),
                     "Celdas A/R idénticas": fmt(v["core_cell_agreement"], True),
                     "A recuperada": fmt(v["accountable_agreement"], True),
                     "Celdas inestables": f"{v['unstable_cells']} de {v['n_cells']}"}
                    for g, v in modal_summary.items()],
                   ["Grupo", "Celdas idénticas", "Celdas A/R idénticas", "A recuperada", "Celdas inestables"]), ""]
    L += ["## 15. Limitaciones", "",
          "- Un solo modelo de lenguaje: los agentes comparten sesgos del modelo; la diversidad de "
          "perspectivas es inducida por el prompt, no por conocimiento independiente.",
          "- Las fichas son breves y no nombran expresamente el modelo eléctrico del EMS; la ambigüedad "
          "observada puede reflejar el marco institucional o la lectura del modelo.",
          "- El catálogo de actividades y los escenarios fueron redactados por el equipo que escribió el "
          "artículo; la separación de actividades (p. ej., liberación y habilitación de ventana) puede "
          "orientar la respuesta aunque no revele la asignación.",
          "- La correspondencia entre unidades y columnas de REFERENCE_RACI (Origen, GT*, AC) es aproximada.",
          "- La normalización a departamento oculta diferencias entre secciones (DAS1/DAS2, ISC2/ISC3).",
          "- Las citas válidas se verifican por existencia del identificador, no por pertinencia de su contenido.",
          "- La semilla no garantiza determinismo en la API; la variabilidad entre repeticiones incluye "
          "la del servicio.", ""]
    (outdir / "final_report.md").write_text("\n".join(L), encoding="utf-8")
    print(f"Informe: {outdir / 'final_report.md'}")
    for k, v in summary:
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
