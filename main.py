#!/usr/bin/env python3
"""tell-story-32: emit one Wi-Fi name that tells a whole story.

The name is a single line of at most 32 characters, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
No trailing newline: the gate counts every character in the file.
"""

import os
import sys


def pick_name() -> str:
    words = ["She", "took", "the", "dog", "and", "password"]
    return " ".join(words)


def main(argv: list[str]) -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    text = pick_name()
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
