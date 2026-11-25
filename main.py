#!/usr/bin/env python3
"""Make the AI Judge Laugh — one joke about office life.

The entry is a single fixed joke, written for make.fun
u-rama-melon-make-the-ai-judge-laugh-302d0825: one joke about
office life, a single line of under 200 characters. Corporate
speak has followed the entrant home: "per my last email" slipped
into a message to his own mother, and HR has officially followed
him home. This program writes that joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The joke is fixed text:
the same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "I caught myself writing 'per my last email' to my own mother "
    "today, so I think HR has officially followed me home."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the joke against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"joke is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("joke is only white space, the gate refuses it")
    if "\n" in LINE or "\r" in LINE:
        return abort("joke spans more than one line, the gate wants a single line")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
