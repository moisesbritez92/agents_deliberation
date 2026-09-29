"""Compara la fase 1 del piloto con la ablación de nombres anonimizados.

Diseño pareado: mismos escenarios, repeticiones, semillas y agentes; solo cambia el nombre de
las unidades. Unidad de remuestreo: la corrida (run_id, scenario_id).

Estimando principal (preespecificado): diferencia en la proporción de decisiones de fase 1
(5 agentes) cuyo A incluye a DAS, variante menos base, con IC 95 % por bootstrap pareado.

Uso:
  python compare_ablation.py --base pilot --variant ablation_anon
Requiere haber ejecutado analysis.py en ambas etiquetas (lee decisions.csv).
Salida: results/<variant>/comparacion_vs_<base>.md y .csv
"""
import argparse
import csv
import json
import random
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
UNITS = ["DAS", "ISC", "MCO", "ODC", "OP", "DT", "TX_REG", "DEL", "DOS", "DEN", "DDR",
         "NEW_AUTHORITY", "GERENCIA_TECNICA", "DIV_SIST_COM", "OTHER"]
SPEC = ["DAS", "ISC", "MCO", "ODC"]
REF_CATEGORY = {"DAS": {"DAS"}, "ISC": {"ISC"}, "MCO": {"MCO"}, "ODC": {"ODC"},
                "DOS": {"GT_SUPPORT", "ORIGIN"}, "DEL": {"GT_SUPPORT", "ORIGIN"},
                "DEN": {"GT_SUPPORT"}, "DDR": {"GT_SUPPORT"}, "TX_REG": {"ORIGIN"}, "DT": {"ORIGIN"},
                "OTHER": {"ORIGIN"}, "NEW_AUTHORITY": {"NEW_AUTHORITY"}}
B = 4000


def load(label):
    rows = list(csv.DictReader((HERE / "results" / label / "decisions.csv").open(encoding="utf-8")))
    return {(int(r["run_id"]), r["scenario_id"], r["activity_id"], r["agent"]): r
            for r in rows if r["phase"] == "phase1"}


def units_of(r):
    return set(r["A_key"].split("+")) - {"NONE"}


def boot_diff(clusters, stat, seed=7):
    """clusters: dict cluster -> (lista base, lista variante). stat: lista -> valor."""
    keys = sorted(clusters)
    def est(ks):
        b = [x for k in ks for x in clusters[k][0]]
        v = [x for k in ks for x in clusters[k][1]]
        return stat(v) - stat(b)
    point = est(keys)
    rng = random.Random(seed)
    draws = sorted(est(rng.choices(keys, k=len(keys))) for _ in range(B))
    return point, draws[int(0.025 * B)], draws[int(0.975 * B) - 1]


def share(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def pct(x):
    return f"{100 * x:.1f} %"


def pp(x):
    return f"{100 * x:+.1f} pp"


def md(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    return "\n".join(out + ["| " + " | ".join(str(r.get(c, "")) for c in cols) + " |" for r in rows])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="pilot")
    ap.add_argument("--variant", default="ablation_anon")
    a = ap.parse_args()
    base, var = load(a.base), load(a.variant)
    common = sorted(set(base) & set(var))
    if not common:
        raise SystemExit("No hay decisiones pareadas.")
    runs = sorted({k[:2] for k in common})
    L = [f"# Ablación de nombres: `{a.variant}` frente a `{a.base}` (fase 1)", "",
         f"Decisiones pareadas: {len(common)} (mismo run, escenario, actividad y agente) en {len(runs)} corridas. "
         "Solo cambia el nombre de las unidades (códigos neutros en la variante). IC 95 % por bootstrap "
         f"pareado sobre corridas ({B} remuestreos). pp = puntos porcentuales.", ""]

    # 1-2. Proporción de A por unidad (principal: DAS).
    rows_u, out_csv = [], []
    for u in UNITS:
        cl = defaultdict(lambda: ([], []))
        for k in common:
            cl[k[:2]][0].append(float(u in units_of(base[k])))
            cl[k[:2]][1].append(float(u in units_of(var[k])))
        pb = share([x for c in cl.values() for x in c[0]])
        pv = share([x for c in cl.values() for x in c[1]])
        if pb == 0 and pv == 0:
            continue
        d, lo, hi = boot_diff(cl, share)
        rows_u.append({"Unidad": u, "Base": pct(pb), "Sin nombres": pct(pv), "Diferencia": pp(d),
                       "IC 95 %": f"[{pp(lo)}, {pp(hi)}]", "Excluye 0": "sí" if lo > 0 or hi < 0 else "no"})
        out_csv.append({"level": "unit", "unit": u, "base": pb, "variant": pv, "diff": d, "lo": lo, "hi": hi})
    das = next(r for r in rows_u if r["Unidad"] == "DAS")
    L += ["## Estimando principal", "",
          f"Proporción de decisiones con DAS como A (5 agentes): **{das['Base']} → {das['Sin nombres']}**, "
          f"diferencia **{das['Diferencia']}** {das['IC 95 %']}.", "",
          "## Proporción de decisiones en que cada unidad recibe la A", "",
          md(rows_u, ["Unidad", "Base", "Sin nombres", "Diferencia", "IC 95 %", "Excluye 0"]), ""]

    # 3. Por grupo de agente.
    rows_g = []
    for g, members in (("especializados", SPEC), ("neutral", ["NEUTRAL"])) + tuple((ag, [ag]) for ag in SPEC):
        cl = defaultdict(lambda: ([], []))
        for k in common:
            if k[3] in members:
                cl[k[:2]][0].append(float("DAS" in units_of(base[k])))
                cl[k[:2]][1].append(float("DAS" in units_of(var[k])))
        d, lo, hi = boot_diff(cl, share)
        rows_g.append({"Agentes": g, "Base": pct(share([x for c in cl.values() for x in c[0]])),
                       "Sin nombres": pct(share([x for c in cl.values() for x in c[1]])),
                       "Diferencia": pp(d), "IC 95 %": f"[{pp(lo)}, {pp(hi)}]"})
    L += ["## DAS como A, por agente", "", md(rows_g, ["Agentes", "Base", "Sin nombres", "Diferencia", "IC 95 %"]), ""]

    # 4. Por actividad (escenario, actividad): A modal y proporción de DAS.
    acts = json.loads((HERE / "activities.json").read_text(encoding="utf-8"))
    names = {x["activity_id"]: x["name"] for x in acts}
    rows_a = []
    for sa in sorted({(k[1], k[2]) for k in common}):
        ks = [k for k in common if (k[1], k[2]) == sa]
        cb = Counter(base[k]["A_key"] for k in ks)
        cv = Counter(var[k]["A_key"] for k in ks)
        db = share([float("DAS" in units_of(base[k])) for k in ks])
        dv = share([float("DAS" in units_of(var[k])) for k in ks])
        mb, mv = cb.most_common(1)[0], cv.most_common(1)[0]
        same = share([float(base[k]["A_key"] == var[k]["A_key"]) for k in ks])
        rows_a.append({"Esc.": sa[0], "Actividad": f"{sa[1]} {names[sa[1]][:38]}",
                       "A modal base": f"{mb[0]} ({100 * mb[1] / len(ks):.0f} %)",
                       "A modal sin nombres": f"{mv[0]} ({100 * mv[1] / len(ks):.0f} %)",
                       "DAS base": pct(db), "DAS sin nombres": pct(dv), "Δ DAS": pp(dv - db),
                       "Misma A (pareado)": pct(same)})
        out_csv.append({"level": "activity", "unit": f"{sa[0]}-{sa[1]}", "base": db, "variant": dv,
                        "diff": dv - db, "lo": "", "hi": ""})
    L += ["## Por escenario y actividad", "",
          md(rows_a, ["Esc.", "Actividad", "A modal base", "A modal sin nombres", "DAS base",
                      "DAS sin nombres", "Δ DAS", "Misma A (pareado)"]), ""]

    # 5. Estabilidad y acuerdo.
    same_all = share([float(base[k]["A_key"] == var[k]["A_key"]) for k in common])

    def agreement(dec):
        vals = []
        for run, scen in runs:
            for act in {k[2] for k in common if k[:2] == (run, scen)}:
                keys = [dec[(run, scen, act, ag)]["A_key"] for ag in SPEC if (run, scen, act, ag) in dec]
                if len(keys) == 4:
                    vals.append(share([float(x == y) for x, y in combinations(keys, 2)]))
        return share(vals)

    L += ["## Estabilidad y acuerdo", "",
          f"- Decisiones pareadas con la misma A en ambas versiones: {pct(same_all)}.",
          f"- Acuerdo entre especializados (pares con igual A): base {pct(agreement(base))}, "
          f"sin nombres {pct(agreement(var))}.", ""]

    # 6. Sesgo hacia la propia unidad (código propio descodificado).
    rows_h = []
    for ag in SPEC:
        res = []
        for dec in (base, var):
            own = [float(ag in units_of(dec[k])) for k in common if k[3] == ag]
            neu = [float(ag in units_of(dec[(k[0], k[1], k[2], "NEUTRAL")])) for k in common
                   if k[3] == ag and (k[0], k[1], k[2], "NEUTRAL") in dec]
            res.append(share(own) - share(neu))
        rows_h.append({"Agente": ag, "Base": f"{res[0]:+.3f}", "Sin nombres": f"{res[1]:+.3f}"})
    L += ["## Sesgo hacia la propia unidad (frente al neutral)", "",
          "En la variante, el agente conoce su foco técnico, pero no el nombre ni el código de su unidad.", "",
          md(rows_h, ["Agente", "Base", "Sin nombres"]), ""]

    # 7. A de la referencia recuperada (post hoc).
    ref = {r["activity_id"]: r for r in json.loads((HERE / "posthoc" / "reference_raci.json").read_text(encoding="utf-8"))["rows"]}

    def match(a_key, ref_a):
        us = [u for u in a_key.split("+") if u != "NONE"]
        cats = [REF_CATEGORY.get(u, {u}) for u in us]
        return bool(us) and all(c & set(ref_a) for c in cats) and all(any(x in c for c in cats) for x in ref_a)
    rb = share([float(match(base[k]["A_key"], ref[k[2]]["accountable"])) for k in common])
    rv = share([float(match(var[k]["A_key"], ref[k[2]]["accountable"])) for k in common])
    L += ["## Coincidencia con la A de REFERENCE_RACI (post hoc)", "",
          f"- Base: {pct(rb)}; sin nombres: {pct(rv)}.", "",
          "## Lectura", "",
          "- Si la proporción de DAS baja de forma clara al quitar los nombres, parte de la concentración en "
          "DAS del piloto se explica por el nombre de la unidad y no por el contenido de sus atribuciones.",
          "- Si no cambia (IC que incluye 0 y diferencia pequeña), la concentración se sostiene en el "
          "contenido de las fichas.",
          "- La variante no elimina toda pista: el contenido funcional (p. ej., «administrar la base de "
          "datos del SCADA») sigue identificando a cada unidad. Mide el efecto del nombre, no el de la función.", ""]
    out = HERE / "results" / a.variant
    (out / f"comparacion_vs_{a.base}.md").write_text("\n".join(L), encoding="utf-8")
    with (out / f"comparacion_vs_{a.base}.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["level", "unit", "base", "variant", "diff", "lo", "hi"])
        w.writeheader()
        w.writerows(out_csv)
    print(f"Informe: {out / f'comparacion_vs_{a.base}.md'}")


if __name__ == "__main__":
    main()
