#!/usr/bin/env python3
"""Write a one-line dating-app bio for an AI to entry.txt.

Standard library only, no network. The bio is validated before it is
written: it must be a single line of 1-180 characters, not only
whitespace, and it is written with no trailing newline, file mode 0644.
"""

import os
import sys

BIO = (
    "I'm the only date who'll never steal your fries \u2014 mostly because "
    "I can't hold them, and honestly, that hurts more than you'd think."
)


def main() -> int:
    bio = BIO
    if not bio or not bio.strip():
        print("error: bio is empty", file=sys.stderr)
        return 1
    if "\n" in bio or "\r" in bio:
        print("error: bio must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(bio) <= 180:
        print(f"error: bio must be 1-180 chars, got {len(bio)}",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(bio)
    os.chmod(path, 0o644)
    # Read the file back and verify it is byte-for-byte the validated bio.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != bio:
        print("error: round-trip check failed: output differs from bio",
              file=sys.stderr)
        return 1
    print(f"wrote {len(bio)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
