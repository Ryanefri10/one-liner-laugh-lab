# One-Liner Laugh Lab — u-suroso-69-one-liner-laugh-lab-6ccf3aae
# (Python 3, standard library only.)
# Writes one fixed funny line to /output/entry.txt: the excuse a robot
# vacuum gives after eating a sock.
# Deterministic: one constant, no network, no randomness, no clock.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Concept: the vacuum does not deny the crime — it reframes it as a
# funeral. The sock is already a widower (its partner lost in the wash),
# so the swallow becomes a mercy burial. The deadpan last two words,
# "Inside me", land the twist: the grave is the vacuum itself. The line
# opens cold on the joke, with no throat-clearing setup.

import os
from pathlib import Path

LINE = "The sock was already dead — single, lonely, its partner lost in the wash years ago. I just gave it the burial it deserved. Inside me."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Enforce the competition's own validity rules in the program itself:
    # 1-200 characters, one line, at least one non-whitespace character.
    if not 1 <= len(LINE) <= 200 or not any(not c.isspace() for c in LINE):
        raise ValueError("line must be 1-200 characters with non-whitespace content")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
