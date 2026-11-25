#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun bounty entry.

Writes the single line a gamer texts the boss to skip work on
GTA 6 launch week (at most 20 words, 1-140 characters) to
$ENTRY_OUTPUT (default /output/entry.txt).
Python 3.13 standard library only; deterministic, no network calls.
"""

import os
import sys

EXCUSE = "Sorry, my fridge died overnight and everything's defrosting, I have to stay home and cook it all."

# Why this line: it is a real, specific, boring domestic detail a tired
# manager has heard variants of (a broken appliance, a tradesman delay is
# implied by staying home), so it is almost believable — and the laugh
# comes from the excuse's own logic, not a joke bolted on: the only way
# to save a dead fridge's contents is to stay home and cook all of it.
# No dead grandmother, no flat tyre, no sudden fever; one hurried line,
# plain words, no setup, no explanation, no signature.

# Bounty limits: at most 20 words, and the sealed gate wants 1-140 chars.
MAX_WORDS = 20
MAX_CHARS = 140


def main():
    words = EXCUSE.split()
    if len(words) > MAX_WORDS:
        print(
            f"error: excuse is {len(words)} words, "
            f"over the {MAX_WORDS}-word limit",
            file=sys.stderr,
        )
        return 1
    if not EXCUSE.strip() or not 1 <= len(EXCUSE) <= MAX_CHARS:
        print(
            f"error: excuse is {len(EXCUSE)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(EXCUSE)
        # File only: never chmod a directory (the grader owns /output).
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
