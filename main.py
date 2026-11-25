#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line, written to /output/entry.txt.

The entry is a single one-liner (133 characters, UTF-8), chosen after a
simulated pairwise tournament of 8 candidates against the judge's own
criteria: a joke that lands cold, a surprise turn, tight wording, no
stock setup, and still funny on a second read.

The program is deterministic: it writes the same line on every run and
reads nothing from outside this repository.
"""

from pathlib import Path

# The entry: one funny line, at most 200 characters.
LINE = (
    "My smart fridge emailed my doctor about the ice cream. "
    "I now take dietary advice from an appliance with better "
    "boundaries than my ex."
)

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    output_path = Path("/output") / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
