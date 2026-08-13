# Inference Principles

- Align the uncertainty estimator with treatment assignment and plausible error dependence, not software defaults.
- Distinguish the number of observations from the number of independent assignment or sampling units.
- Report coefficient scale, uncertainty interval, and economically meaningful magnitude before interpreting a p-value.
- Treat few clusters, serial correlation, spatial correlation, generated regressors, and multi-stage estimation as explicit risks.
- Report whether weights are sampling, probability, frequency, or analytic weights and explain the target estimand they induce.
- Distinguish pre-specified primary outcomes from exploratory families; address multiplicity at the family level.
- Do not infer equality from failure to reject. Use equivalence or non-inferiority logic only when margins were substantively justified.
- Do not infer a subgroup difference from significance in one subgroup and non-significance in another; test the interaction or contrast.
- Treat robustness across standard-error choices as sensitivity information, not a substitute for choosing a defensible dependence structure.
- When assumptions or sample counts are missing, label inference as not assessable rather than selecting a test by habit.
