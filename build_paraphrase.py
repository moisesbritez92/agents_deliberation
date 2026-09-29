"""Control de paráfrasis: material base con las instrucciones reescritas (paraphrase/).

Motivo: comprobar que los resultados principales no dependen de la redacción literal de las
instrucciones (pedido del revisor, 29/09/2026). Las instrucciones de paraphrase/prompts/ se
redactaron a mano con el mismo contenido y otra formulación; el corpus, los escenarios y las
actividades son idénticos byte a byte.

Este script copia el resto del material y verifica, archivo por archivo, que la paráfrasis
conserva los elementos técnicos (códigos, campos del esquema, marcadores de plantilla, cifras,
siglas), que no introduce marcadores de la solución del artículo y que el texto cambió de verdad.
"""
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_corpus import FORBIDDEN_MARKERS  # noqa: E402

OUT = HERE / "paraphrase"
FILES = ["common.md", "das.md", "isc.md", "mco.md", "odc.md", "neutral.md", "arbiter.md",
         "task_phase1.md", "task_phase2.md", "task_phase2_control.md", "task_arbiter.md"]
TOKEN = re.compile(r"\{\{[A-Z_]+\}\}|\b[A-Z][A-Z0-9_./-]{1,}\b|\b[a-z]+(?:_[a-z]+)+\b|\b\d+\b|\"[a-z_]+\"")


def tokens(text):
    return sorted(set(TOKEN.findall(text)))


def sentences(text):
    return {s.strip() for s in re.split(r"(?<=[.:;])\s+|\n+", text) if len(s.split()) >= 5}


def main():
    OUT.mkdir(exist_ok=True)
    for name in ("corpus_institutional.md", "corpus_institutional.json", "corpus_external.md",
                 "corpus_external.json", "scenarios.json", "activities.json"):
        shutil.copy(HERE / name, OUT / name)
        assert (HERE / name).read_bytes() == (OUT / name).read_bytes()
    ok = True
    total_same = total = 0
    for f in FILES:
        a = (HERE / "prompts" / f).read_text(encoding="utf-8")
        b = (OUT / "prompts" / f).read_text(encoding="utf-8")
        missing = [t for t in tokens(a) if t not in tokens(b)]
        added = [t for t in tokens(b) if t not in tokens(a)]
        forbidden = [m for m in FORBIDDEN_MARKERS if m.lower() in b.lower()]
        sa, sb = sentences(a), sentences(b)
        same = len(sa & sb)
        total_same += same
        total += len(sa)
        status = "OK" if not missing and not forbidden else "REVISAR"
        ok &= status == "OK"
        print(f"{f:24s} {status} | tokens faltantes {missing} | nuevos {added} | prohibidos {forbidden} | "
              f"frases idénticas {same}/{len(sa)} | palabras {len(a.split())} -> {len(b.split())}")
    print(f"Frases idénticas en total: {total_same}/{total}")
    if not ok:
        sys.exit("La paráfrasis no conserva todos los elementos técnicos o contiene marcadores prohibidos.")


if __name__ == "__main__":
    main()
