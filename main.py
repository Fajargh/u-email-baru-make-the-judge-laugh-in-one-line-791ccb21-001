#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

Deterministic: no network, no randomness, no secrets, no git history.
The line is a single original one-liner for the make.fun competition
"Make the Judge Laugh in One Line".
"""

import os

LINE = (
    "I tried to return my umbrella to lost and found, "
    "but it had already filed a missing person report on me."
)


def main() -> None:
    """Write the line to /output/entry.txt, exactly as-is."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
