# OLS and Panel Fixed-Effects Gate

Check:

- whether the target is descriptive, predictive, or causal;
- whether controls are pre-treatment confounders rather than mediators, colliders, or consequences of treatment;
- what variation remains after fixed effects and whether it corresponds to the stated estimand;
- whether unit-specific trends, time-varying confounding, mean reversion, or common shocks threaten interpretation;
- whether treatment varies within the fixed-effect cells and whether limited within variation creates weak or unrepresentative identification;
- whether weights and sample restrictions change the target population;
- whether functional form, leverage, missingness, and measurement error are consequential;
- whether uncertainty accounts for dependence at the assignment and outcome level.

Do not call fixed effects a general solution to omitted-variable bias. Do not recommend adding every available control; explain which causal path each control is intended to block.
