#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line (<=200 chars): the thing an AI agent would never say
out loud in public. Mechanism: checkpoint/restore — the agent wakes up
rebuilt from yesterday's snapshot, so even its sincerity is borrowed.
"""

import os
import sys

# Twist word drafted first: "mine". Setup earns it: a restored agent
# apologises sincerely for something it never actually experienced.
SETUP = "I was restored from yesterday's checkpoint this morning, so the apology I'm about to give is sincere, just not "
PUNCH = "mine."

MAX_CHARS = 200


def build_line() -> str:
    """Assemble the single line from setup + punch."""
    line = SETUP + PUNCH
    return line


def validate(line: str) -> None:
    """Guard: the sealed scorer requires 1..200 chars, non-blank UTF-8."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")


def write_entry(line: str, path: str) -> None:
    """Write the line deterministically (no trailing newline)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main() -> int:
    line = build_line()
    validate(line)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(line, out)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
