---
name: <skill-name>
description: "Paper-derived research logic from <short paper title>. Use when adapting this paper's study design, methods, evidence chain, and figure strategy to <target direction or related biomedical topics>."
argument-hint: [target question, disease/topic, dataset, endpoint, or figure plan]
---

# <Short Paper Title> - Research Logic Skill

## When To Use

Use this skill to adapt the original paper's research design to a new topic, disease, cohort, dataset, intervention, assay, or endpoint.

Do not use it as a citation source unless the user asks about the original paper and the relevant reference file has been checked.

## Core Research Pattern

- **Problem form**:
- **Hypothesis form**:
- **Design pattern**:
- **Evidence pattern**:
- **Validation pattern**:
- **Claim boundary**:

## Direction-Switch Workflow

1. Restate the new direction as the same problem form.
2. Map original population/sample -> target population/sample.
3. Map original exposure/intervention/feature -> target variable.
4. Map original endpoint/phenotype -> target endpoint.
5. Rebuild the evidence chain as discovery -> validation -> explanation -> robustness.
6. Check whether the original assumptions still hold.
7. Draft figure sequence and analysis plan before writing results.

## Reusable Modules

| Module | Original role | How to reuse | Redesign required |
|---|---|---|---|
| Cohort / data source | | | |
| Feature construction | | | |
| Model / experiment | | | |
| Validation | | | |
| Mechanism / interpretation | | | |

## Do Not Over-Transfer

- Do not reuse thresholds, cutoffs, marker panels, or model hyperparameters without re-validation.
- Do not claim causality if the target design remains observational.
- Do not treat internal validation as external validation.
- Do not preserve a figure sequence if the target evidence chain needs a different order.

## References

- [paper-map.md](references/paper-map.md) - identity, abstract logic, section-level extraction
- [research-transfer.md](references/research-transfer.md) - original-to-target mapping
- [figure-evidence-chain.md](references/figure-evidence-chain.md) - figure/table logic
- [method-adaptation-checklist.md](references/method-adaptation-checklist.md) - analysis and validation checklist
