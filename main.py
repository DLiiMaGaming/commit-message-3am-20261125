#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (<=200 chars) to /output/entry.txt.
One sharp irony: the agent's own confidence was the only thing
that passed CI — tests green, prod down at 3 AM.
"""

import os
from pathlib import Path

ENTRY = (
    "fix: revert 3 AM deploy \u2014 prod is down, tests passed, "
    "and the only thing that shipped green was my confidence"
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {out}")


if __name__ == "__main__":
    main()
