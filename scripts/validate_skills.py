#!/usr/bin/env python3
"""Run lightweight repository-level validation without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "econometrics-shared",
    "econometrics-audit",
    "econometrics-replication",
    "econometrics-reviewer",
}


def main() -> int:
    errors: list[str] = []
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if actual != EXPECTED:
        errors.append(f"skill directories differ: expected={sorted(EXPECTED)} actual={sorted(actual)}")

    for name in sorted(EXPECTED):
        skill = SKILLS / name
        skill_md = skill / "SKILL.md"
        ui = skill / "agents" / "openai.yaml"
        if not skill_md.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            errors.append(f"{name}: invalid YAML frontmatter fence")
        else:
            frontmatter = match.group(1)
            if f"name: {name}" not in frontmatter:
                errors.append(f"{name}: frontmatter name mismatch")
            if "description:" not in frontmatter:
                errors.append(f"{name}: missing description")
        if "TODO" in text:
            errors.append(f"{name}: unresolved TODO")
        if not ui.is_file():
            errors.append(f"{name}: missing agents/openai.yaml")
        elif f"$${name}" in ui.read_text(encoding="utf-8"):
            errors.append(f"{name}: malformed default prompt")

    for path in ROOT.rglob("*.md"):
        contents = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", contents):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).resolve().exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(EXPECTED)} skills and local Markdown links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
