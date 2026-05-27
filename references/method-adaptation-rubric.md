# Method Adaptation Rubric

Use this rubric to decide whether a paper's method can be migrated to a new direction.

## Strong Transfer

- The target direction has equivalent data types, sample units, and endpoints.
- The original design logic is not tied to a disease-specific artifact.
- Required controls and validation cohorts can be built.
- The method's assumptions are testable in the target setting.

## Partial Transfer

- The target direction preserves the question form but changes assays, endpoints, or clinical context.
- The discovery method transfers, but validation or mechanism experiments must be redesigned.
- The figure sequence transfers only at the level of claim progression, not exact panels.

## Weak Transfer

- Original paper relies on a unique cohort, proprietary assay, unavailable longitudinal design, or disease-specific biology.
- Key confounders in the target direction cannot be measured.
- The target question needs causal evidence but available data are cross-sectional.

## Minimum Validation Checklist

- Independent cohort or external dataset when possible.
- Sensitivity analysis for major thresholds and preprocessing choices.
- Negative/positive controls for experimental work.
- Calibration and clinical utility for prediction models.
- Baseline comparison and ablation for computational methods.
- Clear limitation statement separating evidence from speculation.
