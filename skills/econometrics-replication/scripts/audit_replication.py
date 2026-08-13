#!/usr/bin/env python3
"""Static preflight for Stata, R, and Python replication packages."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


TEXT_SUFFIXES = {".do", ".ado", ".r", ".rmd", ".qmd", ".py", ".ipynb", ".md", ".txt", ".yaml", ".yml", ".toml"}
CODE_SUFFIXES = {".do", ".ado", ".r", ".rmd", ".qmd", ".py", ".ipynb"}
ENTRY_NAMES = {"master.do", "main.do", "run.do", "main.r", "run.r", "main.py", "run.py", "makefile", "snakefile"}
DEPENDENCY_NAMES = {"requirements.txt", "pyproject.toml", "environment.yml", "environment.yaml", "renv.lock", "packrat.lock"}
README_NAMES = {"readme", "readme.md", "readme.txt", "readme.pdf"}


@dataclass
class Finding:
    severity: str
    code: str
    path: str
    line: int | None
    message: str


PATTERNS = [
    ("BLOCKER", "ABSOLUTE_WINDOWS_PATH", re.compile(r"[A-Za-z]:(?:\\+|/)+(?:Users|Documents|Desktop|Downloads)(?:\\+|/)+", re.I), "Author-machine absolute Windows path"),
    ("BLOCKER", "POSSIBLE_CREDENTIAL", re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"][^'\"]+"), "Possible embedded credential; inspect without exposing its value"),
    ("MAJOR", "NETWORK_CALL", re.compile(r"(?i)\b(download\.file|requests\.(get|post)|urlretrieve|curl\b|wget\b)"), "Network call requires documentation and authorization"),
    ("MAJOR", "PACKAGE_INSTALL", re.compile(r"(?i)\b(install\.packages|pip\s+install|conda\s+install|ssc\s+install|net\s+install)\b"), "Package installation is mixed into analysis code"),
    ("MAJOR", "WORKING_DIRECTORY", re.compile(r"(?i)\b(setwd\s*\(|os\.chdir\s*\(|^\s*cd\s+[\"'])"), "Working directory mutation may reduce portability"),
    ("BLOCKER", "DESTRUCTIVE_OPERATION", re.compile(r"(?i)\b(shutil\.rmtree|remove\.all|unlink\s*\([^)]*recursive\s*=\s*true|erase\s+.+|rm\s+-rf)"), "Potential destructive operation; resolve exact target before execution"),
]


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def inspect(root: Path) -> dict[str, object]:
    files = sorted(path for path in root.rglob("*") if path.is_file() and ".git" not in path.parts)
    findings: list[Finding] = []
    names = {path.name.lower() for path in files}

    if not names.intersection(README_NAMES):
        findings.append(Finding("MAJOR", "MISSING_README", ".", None, "No package README detected"))
    if not any(path.name.lower() in ENTRY_NAMES for path in files):
        findings.append(Finding("MAJOR", "MISSING_ENTRY_POINT", ".", None, "No conventional master or entry script detected"))
    if any(path.suffix.lower() in {".r", ".rmd", ".qmd", ".py"} for path in files) and not names.intersection(DEPENDENCY_NAMES):
        findings.append(Finding("MAJOR", "MISSING_DEPENDENCIES", ".", None, "R/Python code found without a recognized dependency specification"))

    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES or path.stat().st_size > 5_000_000:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), start=1):
            for severity, code, pattern, message in PATTERNS:
                if pattern.search(line):
                    findings.append(Finding(severity, code, rel(path, root), number, message))

    code_files = [rel(path, root) for path in files if path.suffix.lower() in CODE_SUFFIXES]
    return {
        "root": str(root.resolve()),
        "static_only": True,
        "summary": {
            "files": len(files),
            "code_files": len(code_files),
            "blockers": sum(item.severity == "BLOCKER" for item in findings),
            "major": sum(item.severity == "MAJOR" for item in findings),
            "minor": sum(item.severity == "MINOR" for item in findings),
        },
        "code_files": code_files,
        "findings": [asdict(item) for item in findings],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    report = inspect(root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        summary = report["summary"]
        print(f"Static audit: {summary['files']} files, {summary['blockers']} blockers, {summary['major']} major findings")
        for item in report["findings"]:
            location = item["path"] + (f":{item['line']}" if item["line"] else "")
            print(f"[{item['severity']}] {item['code']} {location} - {item['message']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
