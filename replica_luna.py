"""Evalúa la réplica con gpt-6-luna frente a los criterios preespecificados (BITACORA, 28/09/2026).

H1 efecto de la deliberación; H2 dirección de los cambios; H3 controles de presentación;
H4 taxonomía de actividades (misma regla que classify_cell() de reporte/generar_datos.py);
H5 validez formal de las citas. Antes de clasificar, comprueba que la regla reproduce la
clasificación de Gemini publicada en reporte/tablas/sintesis_actividades.json.

Uso: python replica_luna.py   (tras analysis.py en luna_pilot y en los tres controles)
Salida: results/luna_pilot/replica_vs_gemini.md y .json
"""
import csv
import json
import random
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
RES = HERE / "results"
SPEC = ["DAS", "ISC", "MCO", "ODC"]
B = 4000
R5 = range(1, 6)
THR = 0.60
RANK = {"Robusta": 0, "Depende de la denominación": 1, "Disputada DAS/MCO": 2, "Sensible al orden": 3}
CONDS = ("pilot", "order_reversed", "ablation_anon", "ablation_swap")


def read_csv(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def mean(xs):
    xs = [x for x in xs if x == x]
    return sum(xs) / len(xs) if xs else float("nan")


def summary(label):
    return {r["metric"]: r["value"] for r in read_csv(RES / label / "summary.csv")}


# ---------------------------------------------------------------- H1 y H2
def deliberation(dec):
    idx = defaultdict(dict)
    for r in dec:
        idx[(r["phase"], r["scenario_id"], int(r["run_id"]), r["activity_id"])][r["agent"]] = r["A_key"]

    def agree(cell):
        ks = [cell[a] for a in SPEC if a in cell]
        return mean([float(x == y) for x, y in combinations(ks, 2)]) if len(ks) == 4 else float("nan")

    per = defaultdict(lambda: defaultdict(list))
    for (ph, s, run, a), cell in idx.items():
        if ph in ("phase1", "phase2", "phase2c"):
            per[(ph, s)][run].append(agree(cell))
    scen = sorted({k[1] for k in per})
    eff, dctl = defaultdict(dict), defaultdict(dict)
    for s in scen:
        for run in per[("phase1", s)]:
            b1, b2, bc = (mean(per[(p, s)][run]) for p in ("phase1", "phase2", "phase2c"))
            eff[s][run] = (b2 - b1) - (bc - b1)
            dctl[s][run] = bc - b1
    rng = random.Random(23)

    def strat(d):
        obs = mean([v for s in scen for v in d[s].values()])
        bs = sorted(mean([v for s in scen for v in rng.choices(list(d[s].values()), k=len(d[s]))]) for _ in range(B))
        return obs, bs[int(0.025 * B)], bs[int(0.975 * B) - 1]

    by_scen = {s: mean(list(eff[s].values())) for s in scen}
    # Dirección de los cambios (misma definición que el reporte).
    tot = maj = 0
    for (ph, s, run, a), cell in idx.items():
        if ph != "phase2":
            continue
        c1 = idx[("phase1", s, run, a)]
        for ag, k2 in cell.items():
            k1 = c1.get(ag)
            if k1 is None or k1 == k2:
                continue
            tot += 1
            others = Counter(v for o, v in c1.items() if o != ag)
            if k2 in others and others[k2] == max(others.values()):
                maj += 1
    return {"effect": strat(eff), "control_delta": strat(dctl), "by_scenario": by_scen,
            "changes": tot, "to_majority": maj / tot if tot else float("nan")}


# ---------------------------------------------------------------- H3
def units_of(k):
    return set(k.split("+")) - {"NONE"}


def paired(base, var, unit, seed=7):
    """Diferencia (variante - base) en la proporción con `unit` como A; bootstrap sobre corridas."""
    kb = {(int(r["run_id"]), r["scenario_id"], r["activity_id"], r["agent"]): r["A_key"]
          for r in base if r["phase"] == "phase1" and int(r["run_id"]) in R5}
    kv = {(int(r["run_id"]), r["scenario_id"], r["activity_id"], r["agent"]): r["A_key"]
          for r in var if r["phase"] == "phase1" and int(r["run_id"]) in R5}
    common = sorted(set(kb) & set(kv))
    cl = defaultdict(lambda: ([], []))
    for k in common:
        cl[k[:2]][0].append(float(unit in units_of(kb[k])))
        cl[k[:2]][1].append(float(unit in units_of(kv[k])))
    keys = sorted(cl)

    def est(ks):
        return (mean([x for k in ks for x in cl[k][1]]) - mean([x for k in ks for x in cl[k][0]]))
    rng = random.Random(seed)
    draws = sorted(est(rng.choices(keys, k=len(keys))) for _ in range(B))
    return {"base": mean([x for k in keys for x in cl[k][0]]), "variant": mean([x for k in keys for x in cl[k][1]]),
            "diff": est(keys), "lo": draws[int(0.025 * B)], "hi": draws[int(0.975 * B) - 1], "n": len(common)}


# ---------------------------------------------------------------- H4 (regla de generar_datos.py)
def modal_cell(rows, phase, scen, act, runs=None):
    sel = [r["A_key"] for r in rows if r["phase"] == phase and r["scenario_id"] == scen and r["activity_id"] == act
           and (runs is None or int(r["run_id"]) in runs)]
    k, n = Counter(sel).most_common(1)[0]
    return k, n / len(sel)


def classify(cond):
    pilot = cond["pilot"]
    cells = sorted({(r["scenario_id"], r["activity_id"]) for r in pilot if r["phase"] == "phase2"})
    out = {}
    for scen, act in cells:
        m2, s2 = modal_cell(pilot, "phase2", scen, act)
        c = {n: modal_cell(cond[n], "phase1", scen, act, R5) for n in CONDS}
        named_stable = (c["pilot"][0] == c["order_reversed"][0] and c["pilot"][1] >= THR
                        and c["order_reversed"][1] >= THR and s2 >= THR)
        all_same = len({v[0] for v in c.values()}) == 1 and all(v[1] >= THR for v in c.values())
        if not named_stable:
            k = "Sensible al orden"
        elif all_same:
            k = "Robusta"
        elif c["pilot"][0] in ("DAS", "MCO") and {c["ablation_anon"][0], c["ablation_swap"][0]} == {"DAS", "MCO"}:
            k = "Disputada DAS/MCO"
        else:
            k = "Depende de la denominación"
        out[(scen, act)] = k
    per_act = {}
    for (s, a), k in out.items():
        per_act[a] = max(per_act.get(a, k), k, key=RANK.get)
    modal2 = {}
    for a in per_act:
        sel = [r["A_key"] for r in pilot if r["phase"] == "phase2" and r["activity_id"] == a]
        k, n = Counter(sel).most_common(1)[0]
        modal2[a] = (k, n / len(sel))
    return per_act, modal2


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    cx, cy = Counter(x), Counter(y)
    pe = sum(cx[k] * cy[k] for k in set(x) | set(y)) / n / n
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")


def main():
    gem = {"pilot": read_csv(RES / "pilot" / "decisions.csv"),
           "order_reversed": read_csv(RES / "order_reversed" / "decisions.csv"),
           "ablation_anon": read_csv(RES / "ablation_anon" / "decisions.csv"),
           "ablation_swap": read_csv(RES / "ablation_swap" / "decisions.csv")}
    luna = {c: read_csv(RES / f"luna_{c}" / "decisions.csv") for c in CONDS}
    # La réplica usa las repeticiones 1-5 también para la fase 2 de Gemini; la clasificación del
    # reporte usa las 20 del piloto en la fase 2. Se verifica la regla con los datos del reporte.
    gem_cls, gem_m2 = classify(gem)
    published = {r["act"]: r["klass"] for r in json.loads(
        (HERE / "reporte" / "tablas" / "sintesis_actividades.json").read_text(encoding="utf-8"))}
    assert gem_cls == published, "La regla no reproduce la clasificación publicada de Gemini."
    lun_cls, lun_m2 = classify(luna)

    d = deliberation(luna["pilot"])
    e, lo, hi = d["effect"]
    c, clo, chi = d["control_delta"]
    h1 = lo > 0 and (clo <= 0 <= chi or abs(c) < 0.03)
    npos = sum(v > 0 for v in d["by_scenario"].values())
    h2 = d["to_majority"] >= 0.70 if d["changes"] >= 30 else None
    h3a = paired(luna["pilot"], luna["order_reversed"], "DAS")
    h3b_das = paired(luna["ablation_anon"], luna["ablation_swap"], "DAS")
    h3b_mco = paired(luna["ablation_swap"], luna["ablation_anon"], "MCO")
    ok3a = (h3a["lo"] <= 0 <= h3a["hi"]) or abs(h3a["diff"]) < 0.05
    ok3b = h3b_das["lo"] > 0 and h3b_mco["lo"] > 0
    robust_pred = {"ACT04": "DAS", "ACT05": "DAS", "ACT10": "DAS", "ACT11": "DAS", "ACT15": "ODC"}
    h4a_hits = [a for a, u in robust_pred.items() if lun_cls[a] == "Robusta" and lun_m2[a][0] == u]
    nonrob = ["ACT01", "ACT02", "ACT03", "ACT06", "ACT12", "ACT13", "ACT18", "ACT19", "ACT20"]
    h4b_hits = [a for a in nonrob if lun_cls[a] != "Robusta"]
    acts = sorted(gem_cls)
    k_cls = kappa([gem_cls[a] for a in acts], [lun_cls[a] for a in acts])
    same_modal = [a for a in acts if gem_m2[a][0] == lun_m2[a][0]]
    s = summary("luna_pilot")
    qv = float(s["QUOTE_VERIFIED_RATE"])

    yes = lambda b: "sí" if b else ("n/d" if b is None else "no")
    f = lambda x: f"{x:.3f}"
    p = lambda x: f"{100 * x:.1f} %"
    L = ["# Réplica con `gpt-6-luna` frente a los criterios preespecificados", "",
         "Criterios fijados en BITACORA.md (28/09/2026, antes de ejecutar). Repeticiones 1-5; 50 corridas por condición. "
         "La regla de clasificación reproduce exactamente la clasificación publicada de Gemini (verificado).", "",
         "| Hipótesis | Resultado | ¿Se cumple? |", "|---|---|---|",
         f"| H1 efecto de la deliberación | {f(e)} [{f(lo)}; {f(hi)}] (estratificado); control {f(c)} [{f(clo)}; {f(chi)}]; "
         f"positivo en {npos}/10 escenarios | {yes(h1)} |",
         f"| H2 cambios hacia la mayoría (≥ 70 %) | {p(d['to_majority'])} de {d['changes']} cambios | {yes(h2)} |",
         f"| H3a orden inverso con nombres, DAS (|Δ| < 5 pp o IC con 0) | {p(h3a['base'])} → {p(h3a['variant'])}, "
         f"Δ {100 * h3a['diff']:+.1f} pp [{100 * h3a['lo']:+.1f}; {100 * h3a['hi']:+.1f}] | {yes(ok3a)} |",
         f"| H3b saliencia sin nombres: DAS sube en la cruzada | {p(h3b_das['base'])} → {p(h3b_das['variant'])}, "
         f"Δ {100 * h3b_das['diff']:+.1f} pp [{100 * h3b_das['lo']:+.1f}; {100 * h3b_das['hi']:+.1f}] | |",
         f"| H3b saliencia sin nombres: MCO sube en la anónima | {p(h3b_mco['base'])} → {p(h3b_mco['variant'])}, "
         f"Δ {100 * h3b_mco['diff']:+.1f} pp [{100 * h3b_mco['lo']:+.1f}; {100 * h3b_mco['hi']:+.1f}] | {yes(ok3b)} |",
         f"| H4a robustas con igual A (≥ 4/5) | {len(h4a_hits)}/5: {', '.join(h4a_hits) or 'ninguna'} | {yes(len(h4a_hits) >= 4)} |",
         f"| H4b no robustas siguen no robustas (≥ 7/9) | {len(h4b_hits)}/9 | {yes(len(h4b_hits) >= 7)} |",
         f"| H4c acuerdo de clase entre modelos (descriptivo) | κ = {k_cls:.2f}; misma A modal tras deliberar en "
         f"{len(same_modal)}/20 | — |",
         f"| H5 fragmentos literales (≥ 95 %) | {p(qv)} | {yes(qv >= 0.95)} |", "",
         "## Clasificación por actividad", "",
         "| Actividad | Gemini: clase | Gemini: A modal F2 | Luna: clase | Luna: A modal F2 |", "|---|---|---|---|---|"]
    for a in acts:
        L.append(f"| {a} | {gem_cls[a]} | {gem_m2[a][0]} ({100 * gem_m2[a][1]:.0f} %) | {lun_cls[a]} | "
                 f"{lun_m2[a][0]} ({100 * lun_m2[a][1]:.0f} %) |")
    L += ["", "## Efecto por escenario (Luna)", "", "| Escenario | Efecto |", "|---|---|"]
    L += [f"| {k} | {f(v)} |" for k, v in sorted(d["by_scenario"].items())]
    L += ["", "## Otras métricas de `luna_pilot` (summary.csv)", ""]
    L += [f"- {k}: {s[k]}" for k in ("AGREEMENT_BEFORE", "AGREEMENT_AFTER", "AGREEMENT_CONTROL",
                                     "POSITION_CHANGE_RATE", "POSITION_CHANGE_RATE_CONTROL",
                                     "ARBITER_AMBIGUOUS_RATE", "EVIDENCE_VALIDITY_RATE", "estimated_cost_usd") if k in s]
    out = RES / "luna_pilot"
    (out / "replica_vs_gemini.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    json.dump({"H1": {"effect": d["effect"], "control_delta": d["control_delta"], "n_pos_scen": npos, "ok": h1},
               "H2": {"changes": d["changes"], "to_majority": d["to_majority"], "ok": h2},
               "H3a": {**h3a, "ok": ok3a}, "H3b": {"das": h3b_das, "mco": h3b_mco, "ok": ok3b},
               "H4": {"gemini": gem_cls, "luna": lun_cls, "h4a": h4a_hits, "h4b": h4b_hits, "kappa": k_cls,
                      "same_modal": same_modal,
                      "modal_gemini": gem_m2, "modal_luna": lun_m2},
               "H5": {"quote_verified": qv, "ok": qv >= 0.95}},
              (out / "replica_vs_gemini.json").open("w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n".join(L[:16]))


if __name__ == "__main__":
    main()
