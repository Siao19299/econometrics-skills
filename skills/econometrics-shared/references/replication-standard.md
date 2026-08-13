# Replication Package Standard

Require enough documentation and code for an independent researcher to regenerate every computational exhibit and reported number with minimal manual intervention.

## Minimum package

- A top-level README describing data provenance, legal access, restrictions, directory layout, software versions, dependencies, expected runtime, hardware needs, and execution order.
- A single documented entry point, or precise ordered commands when one entry point is infeasible.
- Code for acquisition or documented data access, cleaning, construction, estimation, simulation, figures, and tables.
- A mapping from programs to every paper and appendix exhibit.
- Machine-readable metadata or a codebook for provided data.
- Fixed random seeds where randomness affects published output.
- Portable paths and configurable locations; no author-machine absolute paths.
- Clear separation of source data, derived data, code, temporary files, and final outputs.
- A license and disclosure of files that cannot legally be redistributed.

## Safety boundary

Inspect unknown replication code statically first. Do not execute code that may download data, expose credentials, overwrite user files, call external services, install packages, or access restricted data without explicit authorization and an isolated environment.

## Policy basis

Use the current official policy of the target journal when compliance matters. For AEA journals, verify the current Data and Code Availability Policy rather than relying on a cached checklist.
