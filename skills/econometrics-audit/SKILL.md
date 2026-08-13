---
name: econometrics-audit
description: Audit empirical economics and econometric research designs, estimands, identification assumptions, estimation, inference, robustness, causal language, and reporting. Use for OLS, panel fixed effects, instrumental variables, difference-in-differences, event studies, and regression discontinuity; for manuscript methods/results, research proposals, referee concerns, regression tables, analysis plans, or Stata/R/Python output; and for requests about 内生性、识别策略、平行趋势、工具变量、固定效应、聚类标准误、稳健性检验、因果推断 or 计量审查. Do not use as a generic statistics calculator or claim unsupported coverage of structural, time-series, spatial, synthetic-control, or machine-learning methods.
---

# Econometrics Audit

Produce a bounded, evidence-grounded audit. Do not invent specifications, diagnostics, institutional details, results, or citations.

## Workflow

1. Read `../econometrics-shared/references/research-contract.md` and construct the empirical research contract from supplied material.
2. Classify the design and load exactly one primary method reference:
   - OLS or panel fixed effects: [references/ols-panel.md](references/ols-panel.md)
   - Instrumental variables: [references/instrumental-variables.md](references/instrumental-variables.md)
   - DID or event study: [references/did-event-study.md](references/did-event-study.md)
   - RDD: [references/regression-discontinuity.md](references/regression-discontinuity.md)
3. Load `../econometrics-shared/references/inference-principles.md` when evaluating uncertainty or hypothesis tests.
4. Load `../econometrics-shared/references/claim-strength.md` when evaluating conclusions or manuscript wording.
5. Map each substantive claim to its estimand, identifying assumptions, estimate, uncertainty, and falsification evidence.
6. Rank issues by consequence:
   - `P0`: invalidates or reverses the central empirical interpretation.
   - `P1`: materially weakens identification, inference, or reproducibility.
   - `P2`: improves transparency, precision, or presentation without changing the central conclusion.
7. Read [references/final-checklist.md](references/final-checklist.md) and run final QA.

When the design is outside MVP coverage, still construct the research contract, identify obvious reporting gaps, state the unsupported method explicitly, and avoid method-specific prescriptions.

## Optional deterministic scan

When the user supplies a text manuscript, run `scripts/audit_reporting.py <file>` to flag absent reporting concepts. Treat every flag as a search prompt, never as proof of a flaw.

## Output contract

Return:

```text
Audit scope and boundary
Empirical research contract
Design readout
Priority findings
- [P0/P1/P2] Finding
  Evidence pointer
  Why it matters
  Resolution test
Claim calibration
Missing inputs that could change the judgment
Recommended next actions
```

Separate evidence from inference. Phrase resolution tests as information or analyses that could address a concern, not as demands to obtain a preferred result.
