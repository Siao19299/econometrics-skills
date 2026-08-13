# Stata, R, and Python Replication Checks

## Stata

- Identify the root do-file and confirm ordered execution.
- Check `cd`, `use`, `save`, `erase`, `shell`, `net install`, `ssc install`, and user-specific globals.
- Record the Stata edition and version, community-contributed commands, and installation instructions.
- Prefer project-relative paths and deterministic temporary/output directories.
- Confirm logs expose failures rather than silently continuing.

## R

- Identify the entry script, Makefile, targets pipeline, or Quarto/R Markdown render command.
- Record R version and a package lockfile such as `renv.lock` when feasible.
- Check `setwd`, `install.packages`, remote package sources, environment variables, parallel randomness, and locale-dependent parsing.
- Separate package restoration from analysis execution.

## Python

- Identify the entry module, script, Makefile, notebook execution command, or workflow runner.
- Record Python version and a dependency lock or pinned environment specification.
- Check `os.chdir`, absolute paths, subprocess or shell calls, downloads, credentials, nondeterministic ordering, and unseeded randomness.
- Prefer scripts or executable notebooks with cleared or verified outputs over manually executed cells.

## Cross-language

Document the handoff format and ordering between languages. Confirm that intermediate files are regenerated rather than silently relying on stale artifacts.
