"""Evalúa el control de paráfrasis frente a los criterios preespecificados (BITACORA, 29/09/2026).

Compara results/luna_paraphrase (instrucciones parafraseadas) con results/luna_pilot en las
mismas repeticiones (1-3). P1 efecto de la deliberación; P2 dirección de los cambios; P3 las
cinco actividades robustas; P4 coincidencia de la A modal en los casos estables; P5 citas literales.

Uso: python paraphrase_eval.py   (tras analysis.py --label luna_paraphrase)
Salida: results/luna_paraphrase/paraphrase_eval.md y .json
"""
import json
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # necesario con PYTHONSAFEPATH
import replica_luna as RL  # noqa: E402

RUNS = range(1, 4)
THR = 0.60
ROBUST = {"ACT04": "DAS", "ACT05": "DAS", "ACT10": "DAS", "ACT11": "DAS", "ACT15": "ODC"}


def modal(rows, phase, key):
    """A modal y su frecuencia por clave (actividad o escenario x actividad)."""
    groups = defaultdict(list)
    for r in rows:
        if r["phase"] == phase and (phase != "phase1" or r["agent"] in RL.SPEC + ["NEUTRAL"]):
            groups[key(r)].append(r["A_key"])
    return {k: (Counter(v).most_common(1)[0][0], Counter(v).most_common(1)[0][1] / len(v)) for k, v in groups.items()}


def describe(dec):
    idx = defaultdict(dict)
    for r in dec:
        idx[(r["phase"], r["scenario_id"], r["run_id"], r["activity_id"])][r["agent"]] = r["A_key"]

    def agr(p):
        return RL.mean([RL.mean([float(c[x] == c[y]) for x, y in combinations(RL.SPEC, 2)])
                        for (q, *_), c in idx.items() if q == p and all(a in c for a in RL.SPEC)])
    ph = lambda p: [r for r in dec if r["phase"] == p]
    return {"agr1": agr("phase1"), "agr2": agr("phase2"), "agrc": agr("phase2c"),
            "amb1": RL.mean([float(r["ambiguity"] == "True") for r in ph("phase1") if r["agent"] in RL.SPEC]),
            "arb": RL.mean([float(r["verdict"] == "AMBIGUOUS") for r in ph("phase3")]),
            "newauth": RL.mean([float(r["new_authority"] == "True") for r in ph("phase1")]),
            "das1": RL.mean([float("DAS" in RL.units_of(r["A_key"])) for r in ph("phase1")])}


def main():
    orig = [r for r in RL.read_csv(RL.RES / "luna_pilot" / "decisions.csv") if int(r["run_id"]) in RUNS]
    para = [r for r in RL.read_csv(RL.RES / "luna_paraphrase" / "decisions.csv") if int(r["run_id"]) in RUNS]
    do, dp = RL.deliberation(orig), RL.deliberation(para)
    e, lo, hi = dp["effect"]
    c, clo, chi = dp["control_delta"]
    p1 = lo > 0 and (clo <= 0 <= chi or abs(c) < 0.03)
    p2 = dp["to_majority"] >= 0.70 if dp["changes"] >= 30 else None
    act = lambda r: r["activity_id"]
    cell = lambda r: (r["scenario_id"], r["activity_id"])
    m1p, m2p = modal(para, "phase1", act), modal(para, "phase2", act)
    p3_hits = [a for a, u in ROBUST.items()
               if m1p[a][0] == u and m1p[a][1] >= THR and m2p[a][0] == u and m2p[a][1] >= THR]
    p3 = len(p3_hits) == 5
    c_orig, c_para = modal(orig, "phase1", cell), modal(para, "phase1", cell)
    stable = [k for k, (u, f) in c_orig.items() if f >= THR]
    same = [k for k in stable if c_para[k][0] == c_orig[k][0]]
    p4 = len(same) / len(stable) >= 0.80
    s = RL.summary("luna_paraphrase")
    qv = float(s["QUOTE_VERIFIED_RATE"])
    p5 = qv >= 0.95
    Do, Dp = describe(orig), describe(para)

    yes = lambda b: "sí" if b else ("n/d" if b is None else "no")
    f3 = lambda t: f"{t[0]:.3f} [{t[1]:.3f}; {t[2]:.3f}]"
    pc = lambda x: f"{100 * x:.1f} %"
    L = ["# Control de paráfrasis de las instrucciones frente a los criterios preespecificados", "",
         "Criterios fijados en BITACORA.md (29/09/2026, antes de ejecutar). `gpt-6-luna`, repeticiones 1-3, "
         "30 corridas por condición.", "",
         "| Criterio | Paráfrasis | Original (mismas repeticiones) | ¿Se cumple? |", "|---|---|---|---|",
         f"| P1 efecto de la deliberación | {f3(dp['effect'])}; control {f3(dp['control_delta'])} | {f3(do['effect'])} | {yes(p1)} |",
         f"| P2 cambios hacia la mayoría (≥ 70 %) | {pc(dp['to_majority'])} de {dp['changes']} | {pc(do['to_majority'])} de {do['changes']} | {yes(p2)} |",
         f"| P3 cinco robustas con igual A (≥ 60 % en F1 y F2) | {len(p3_hits)}/5: {', '.join(p3_hits)} | 5/5 | {yes(p3)} |",
         f"| P4 misma A modal en casos estables (≥ 80 %) | {len(same)}/{len(stable)} ({pc(len(same) / len(stable))}) | — | {yes(p4)} |",
         f"| P5 fragmentos literales (≥ 95 %) | {pc(qv)} | — | {yes(p5)} |", "",
         "## Descriptivo (sin criterio)", "", "| Métrica | Paráfrasis | Original |", "|---|---|---|"]
    names = {"agr1": "Acuerdo F1", "agrc": "Acuerdo control 2c", "agr2": "Acuerdo F2", "amb1": "Ambigüedad agentes F1",
             "arb": "Árbitro AMBIGUOUS", "newauth": "Autoridad nueva F1", "das1": "DAS como A, F1"}
    L += [f"| {n} | {pc(Dp[k])} | {pc(Do[k])} |" for k, n in names.items()]
    L += ["", "## Casos estables cuya A modal cambia con la paráfrasis", ""]
    L += [f"- {k[0]} {k[1]}: {c_orig[k][0]} ({pc(c_orig[k][1])}) → {c_para[k][0]} ({pc(c_para[k][1])})"
          for k in stable if k not in same] or ["- ninguno"]
    out = RL.RES / "luna_paraphrase"
    (out / "paraphrase_eval.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    json.dump({"P1": {"effect": dp["effect"], "control": dp["control_delta"], "orig_effect": do["effect"], "ok": p1},
               "P2": {"to_majority": dp["to_majority"], "changes": dp["changes"],
                      "orig_to_majority": do["to_majority"], "orig_changes": do["changes"], "ok": p2},
               "P3": {"hits": p3_hits, "ok": p3}, "P4": {"stable": len(stable), "same": len(same), "ok": p4,
                                                         "changed": [[k[0], k[1], c_orig[k][0], c_orig[k][1], c_para[k][0], c_para[k][1]]
                                                                     for k in stable if k not in same]},
               "P5": {"quote_verified": qv, "ok": p5}, "desc_paraphrase": Dp, "desc_original": Do},
              (out / "paraphrase_eval.json").open("w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n".join(L))


if __name__ == "__main__":
    main()
