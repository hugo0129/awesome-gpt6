#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate every case file in cases/.

Checks:
1. Filename is English kebab-case
2. YAML front matter exists with title / category / author / date / lang
3. `category` matches the folder the file lives in
4. `lang` is zh or en

Exit code 1 if anything fails. Also runs in CI (.github/workflows/check-case.yml).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "cases"

REQUIRED_FIELDS = ["title", "category", "author", "date", "lang"]
FILENAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_front_matter(text: str):
    """Return a dict of simple `key: value` fields, or None if missing/malformed."""
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    data = {}
    for line in parts[1].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    errors = []
    files = sorted(
        p for p in CASES.glob("*/*.md")
        if p.name.lower() != "readme.md"
    )

    for path in files:
        rel = path.relative_to(ROOT)
        folder = path.parent.name
        expected_category = "-".join(folder.split("-")[1:])

        if not FILENAME_RE.match(path.stem):
            errors.append(f"{rel}: filename must be English kebab-case, got `{path.stem}`")

        data = parse_front_matter(path.read_text(encoding="utf-8"))
        if data is None:
            errors.append(f"{rel}: missing or malformed YAML front matter")
            continue

        for field in REQUIRED_FIELDS:
            if not data.get(field):
                errors.append(f"{rel}: front matter field `{field}` is empty or missing")

        category = data.get("category", "")
        if category and category != expected_category:
            errors.append(
                f"{rel}: category `{category}` does not match folder `{folder}` "
                f"(expected `{expected_category}`)"
            )

        lang = data.get("lang", "")
        if lang and lang not in ("zh", "en"):
            errors.append(f"{rel}: lang must be `zh` or `en`, got `{lang}`")

    if errors:
        print(f"Found {len(errors)} problem(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All good: {len(files)} case file(s) validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
