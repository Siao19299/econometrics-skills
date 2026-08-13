# Econometrics Skills

Reusable Codex skills for applied econometrics. The MVP turns an empirical paper or replication project into three reviewable workflows:

- `econometrics-audit` audits the estimand, identification strategy, estimation, inference, robustness, and claim strength.
- `econometrics-replication` audits Stata, R, and Python replication packages without executing untrusted research code by default.
- `econometrics-reviewer` produces a source-grounded referee report for an empirical economics manuscript.
- `econometrics-shared` supplies common research contracts and quality gates used by the three triggerable skills.

The initial method coverage is deliberately narrow and deep: OLS and panel fixed effects, instrumental variables, difference-in-differences and event studies, and regression discontinuity. Time series, synthetic control, structural estimation, machine learning, and spatial econometrics are future extensions.

## Install

Copy the complete skill directories into your Codex skills directory. Keep `econometrics-shared` beside the three triggerable skills because they read its references at runtime.

```powershell
Copy-Item -Recurse skills\econometrics-* $env:USERPROFILE\.codex\skills\
```

Start a new Codex task after installation. Example requests:

```text
Use econometrics-audit to audit the identification strategy and inference in this DID paper.
Use econometrics-replication to inspect this Stata replication package without running it.
Use econometrics-reviewer to write a bounded referee report for this manuscript.
```

## Design principles

1. Define the estimand before recommending an estimator.
2. Separate evidence, inference, and recommendation.
3. Treat identifying assumptions as claims requiring institutional support, diagnostics, and explicit boundaries.
4. Never invent results, specifications, data access, robustness checks, citations, or journal requirements.
5. Prefer reproducible artifacts and deterministic checks over decorative prose.
6. Mark unsupported methods as outside MVP coverage instead of improvising a false checklist.

## Validate

The project has no third-party Python dependencies.

```powershell
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

## Status

MVP / Draft. The workflows and deterministic checks are implemented, but Stable status should require forward-testing on diverse real manuscripts and replication packages.

## License

Apache-2.0. See `LICENSE`.
