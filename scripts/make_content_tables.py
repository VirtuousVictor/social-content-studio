#!/usr/bin/env python3
"""Convert simple TSV rows into CSV for social content tables.

Usage:
  python3 make_content_tables.py input.tsv output.csv

Input rules:
  - First row is the header.
  - Columns are separated by tabs.
  - Blank lines are skipped.
  - A line without tabs is a comment if its trimmed text is "#" or starts
    with "# ". Hashtags such as "#BookLover" are cell values.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def read_tsv(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        is_comment = "\t" not in raw_line and (line == "#" or line.startswith("# "))
        if not line or is_comment:
            continue
        rows.append([cell.strip() for cell in raw_line.split("\t")])
    return rows


def write_csv(rows: list[list[str]], path: Path) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 make_content_tables.py input.tsv output.csv", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.is_file():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1
    if output_path.exists() and input_path.samefile(output_path):
        print("Input and output must be different files.", file=sys.stderr)
        return 1

    rows = read_tsv(input_path)
    if not rows:
        print("Input has no rows.", file=sys.stderr)
        return 1

    width = len(rows[0])
    bad_rows = [index + 1 for index, row in enumerate(rows) if len(row) != width]
    if bad_rows:
        print(f"Rows with inconsistent column counts: {bad_rows}", file=sys.stderr)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows, output_path)
    print(f"Wrote {len(rows) - 1} data rows to {output_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        sys.exit(str(error))

