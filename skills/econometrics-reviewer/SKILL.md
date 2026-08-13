---
name: econometrics-reviewer
description: Produce a rigorous, bounded referee report for an empirical economics or applied econometrics manuscript. Use for mock peer review, pre-submission review, identification and inference critique, contribution and literature-positioning assessment, robustness and falsification review, replication-readiness review, reviewer report, 模拟审稿、预审、计量论文审稿 or 投稿前自审. Cover OLS/panel fixed effects, IV, DID/event studies, and RDD using the bundled method gates. Do not draft an author rebuttal, invent literature comparisons, impersonate a real reviewer, or claim an editorial decision.
---

# Econometrics Reviewer

Review only the supplied manuscript and verified sources. Mark partial inputs and unavailable evidence explicitly.

## Workflow

1. Define the review scope, target outlet if supplied, manuscript version, visible appendices, code/data availability, and assessment boundary.
2. Read `../econometrics-shared/references/research-contract.md` and reconstruct the paper's research contract.
3. Read [references/review-gates.md](references/review-gates.md).
4. For the primary design, read the matching method reference from `../econometrics-audit/references/`.
5. Read `../econometrics-shared/references/claim-strength.md` and `../econometrics-shared/references/inference-principles.md`.
6. Evaluate contribution only against literature actually supplied or independently verified. State `literature position not assessable` when the basis is insufficient.
7. Build a concern ledger. Give every concern a stable ID, manuscript pointer, severity, consequence, and resolution test.
8. Distinguish fatal identification problems, addressable empirical gaps, alternative interpretations, presentation problems, and optional extensions.
9. Read [references/report-structure.md](references/report-structure.md) and produce the report.

## Calibration

- Mark a concern `Blocking: Yes` only when the central claim cannot be sustained without resolving it.
- Do not demand robustness checks without naming the threat and explaining how the check would update the judgment.
- Do not equate novelty with a new dataset, statistical significance, or absence of an identical title.
- Do not require the authors to obtain a preferred result.
- Do not convert a referee report into a rewrite of the paper.

## Output

Return one report by default. If the user explicitly requests multiple independent reviewers, use genuinely isolated contexts or disclose that independence cannot be guaranteed; freeze reports before synthesis.
