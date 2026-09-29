"""Control de orden: material base (con nombres) con las fichas en orden inverso (order_reversed/).

Motivo: la réplica cruzada de la ablación mostró que las actividades disputadas entre DAS y MCO
se asignan a la unidad más saliente (código bajo / posición temprana). Este control mide si la
matriz del piloto, con nombres reales, también depende del orden de presentación.

Solo cambia el orden de las fichas en el corpus institucional y en la lista de unidades
admitidas; el texto de cada ficha, el corpus externo, los escenarios y los prompts son idénticos.
"""
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "order_reversed"


def main():
    OUT.mkdir(exist_ok=True)
    inst = json.loads((HERE / "corpus_institutional.json").read_text(encoding="utf-8"))
    (OUT / "corpus_institutional.json").write_text(json.dumps(inst[::-1], ensure_ascii=False, indent=2),
                                                   encoding="utf-8")
    md = (HERE / "corpus_institutional.md").read_text(encoding="utf-8")
    head, *blocks = md.split("\n## ")
    blocks = [b.rstrip("\n") for b in blocks]
    assert len(blocks) == len(inst)
    (OUT / "corpus_institutional.md").write_text(head + "\n## " + "\n\n## ".join(blocks[::-1]) + "\n",
                                                 encoding="utf-8")
    for name in ("corpus_external.md", "corpus_external.json", "scenarios.json", "activities.json"):
        shutil.copy(HERE / name, OUT / name)
    shutil.copytree(HERE / "prompts", OUT / "prompts", dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("judge.md"))
    # Verificación: mismas fichas, mismo texto, orden inverso.
    a = sorted(b.strip() for b in md.split("\n## ")[1:])
    b = sorted(x.strip() for x in (OUT / "corpus_institutional.md").read_text(encoding="utf-8").split("\n## ")[1:])
    assert a == b, "el contenido de las fichas cambió"
    order = [f["unit_code"] for f in inst[::-1]]
    print("Orden de fichas en el control:", order)
    print(f"DAS en posición {order.index('GT/DAS') + 1}; MCO en posición {order.index('DTE/MCO') + 1}")


if __name__ == "__main__":
    main()
