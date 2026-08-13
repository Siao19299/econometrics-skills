---
name: econometrics-replication
description: Inspect, audit, prepare, or improve empirical economics replication packages using Stata, R, or Python. Use for data-and-code availability, README and master-script checks, portable paths, dependency and software documentation, random seeds, program-to-exhibit mapping, restricted-data instructions, AEA-style reproducibility preparation, replication archives, 复现包、代码复现、数据代码声明 or 可重复性审查. Perform static inspection by default; do not execute untrusted research code, download data, install dependencies, or access restricted data without explicit authorization.
---

# Econometrics Replication

Assess computational reproducibility separately from the scientific validity of the design.

## Workflow

1. Establish the package root, target journal, supplied files, operating system, and whether the task is static audit, package preparation, or authorized execution.
2. Read `../econometrics-shared/references/replication-standard.md`.
3. Run `scripts/audit_replication.py <package-root> --json` for a static preflight.
4. Inspect the flagged files and verify findings manually. Treat heuristic matches as leads, not definitive failures.
5. Read [references/stata-r-python.md](references/stata-r-python.md) for language-specific checks.
6. When exact journal compliance matters, browse the target journal's official current policy and cite it. Do not present bundled guidance as current policy.
7. Do not execute the package unless the user explicitly authorizes execution. Before execution, identify network calls, installs, credentials, absolute outputs, destructive operations, licensed software, restricted data, expected runtime, and isolation needs.
8. Map every table, figure, appendix exhibit, and in-text number to the producing program or mark it unmapped.

## Severity

- `BLOCKER`: prevents a clean independent run or risks privacy, legality, credentials, or destructive writes.
- `MAJOR`: materially impairs regeneration, provenance, or interpretation of outputs.
- `MINOR`: improves clarity, portability, or maintenance.

## Output contract

Return:

```text
Replication audit scope
Execution status: not run / partially run / clean-room run
Package inventory
Blockers
Major findings
Minor findings
Exhibit reproduction map
Restricted-data and legal-access notes
Ready-to-paste README or Data Availability revisions
Verification commands and unresolved fields
```

Never claim a package reproduces results unless the relevant entry point completed in an appropriately isolated environment and outputs were compared with expected artifacts.
