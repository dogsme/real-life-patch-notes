#!/usr/bin/env python3
"""Write one patch-note line for make.fun's Real-Life Patch Notes bounty.

The program writes exactly one line of UTF-8 text (at most 160
characters) to /output/entry.txt: a software patch note for a bug in
human biology, in the terse register of a real release note.
"""

from pathlib import Path

ENTRY = (
    "v2.7.1: fixed a bug where the brain autoplays your most embarrassing "
    "memory from 2014 at 3 a.m. with the skip button disabled."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
