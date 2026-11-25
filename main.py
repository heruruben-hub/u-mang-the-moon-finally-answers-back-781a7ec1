#!/usr/bin/env python3
"""The Moon Finally Answers Back entry.

Writes one line, in the voice of the Moon replying at last to the wishes,
howls and late-night promises of everyone staring up at it, to
/output/entry.txt. The line is 104 characters, inside the 240-character
cap. It lands because it answers all three things the Moon is asked for —
wishes, howls, 3 a.m. promises — then turns them back on the askers: in
four billion years nobody has ever wished the Moon itself good night.
"""

import os

MAX_LEN = 240
MIN_LEN = 1
OUTPUT_PATH = "/output/entry.txt"


def moon_line() -> str:
    """Return the Moon's comeback as a single line of plain text."""
    return (
        "Four billion years of wishes, howls, and 3 a.m. promises — "
        "and not once has anyone wished me good night."
    )


def validate(line: str) -> None:
    """Check the line fits the gate: 1-240 chars, not only whitespace."""
    assert MIN_LEN <= len(line) <= MAX_LEN, (
        f"line is {len(line)} chars, must be {MIN_LEN}-{MAX_LEN}"
    )
    assert line.strip(), "line must not be only whitespace"


def main() -> None:
    line = moon_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
