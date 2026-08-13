#!/usr/bin/env python3
"""Flag missing econometric reporting concepts in a text file.

This is deliberately a lexical preflight, not a validity assessment.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CONCEPTS = {
    "estimand_or_effect": r"\b(estimand|average treatment effect|\bate\b|\batt\b|\blate\b|elasticit)",
    "identification": r"\b(identif|parallel trends?|exclusion restriction|continuity assumption|as.good.as.random)",
    "standard_errors": r"\b(standard errors?|cluster(?:ed|ing)?|bootstrap|confidence interval)",
    "sample": r"\b(sample|observations?|units?|households?|firms?|individuals?)\b",
    "fixed_effects_or_controls": r"\b(fixed effects?|controls?|covariates?)\b",
    "data_source": r"\b(data source|dataset|administrative data|survey data|registry data)\b",
    "robustness_or_falsification": r"\b(robustness|sensitivity|placebo|falsification|pre.trend|balance test)",
}


def scan(text: str) -> dict[str, object]:
    normalized = " ".join(text.lower().split())
    found = {name: bool(re.search(pattern, normalized, re.IGNORECASE)) for name, pattern in CONCEPTS.items()}
    return {
        "advisory_only": True,
        "found": found,
        "missing_search_prompts": [name for name, value in found.items() if not value],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = scan(args.file.read_text(encoding="utf-8", errors="replace"))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Advisory lexical reporting scan")
        for key, value in report["found"].items():
            print(f"[{'FOUND' if value else 'CHECK'}] {key}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
