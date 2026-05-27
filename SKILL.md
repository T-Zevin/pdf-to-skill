---
name: pdf-to-skill
description: "Convert a scientific paper PDF into a reusable Codex skill that captures the paper's transferable research logic, study design, evidence chain, figure strategy, methods, limitations, and direction-switching templates. Use when the user provides a paper or literature PDF and wants to learn the research思路, migrate the design to another disease/topic/dataset, generate a paper-derived skill, or output a markmap mind map."
argument-hint: <path-to-paper.pdf> [target-direction] [skill-name]
---

# pdf-to-skill

Turn one paper into a reusable research-method skill. The goal is not to summarize the paper; it is to extract the transferable research pattern so the user can switch to a new topic while preserving the logic.

## Operating Modes

- **Analyze only**: if the user asks to inspect, learn, extract思路, or make a markmap without creating files, run Steps 1-5 and report.
- **Full skill generation**: if the user asks to "做成 skill", "生成 skill", or gives a target direction, run all steps and write a new skill folder.
- **Update existing skill**: if the user provides an existing generated skill folder, preserve its useful content and patch only the changed paper logic.

## Step 1 - Validate Input

Treat the first argument as `PAPER_PATH`. It should be a `.pdf`, `.txt`, `.md`, or `.docx`; PDF is the default and preferred source.

If the user gives a paper title, DOI, or URL instead of a local file, ask them to provide the PDF unless browsing/downloading is explicitly allowed and legally appropriate.

## Step 2 - Extract Text And Metadata

Use the bundled extractor:

```bash
python3 /Users/xzw/.codex/skills/pdf-to-skill/scripts/extract_paper.py "$PAPER_PATH"
```

It writes:

- `/tmp/pdf_to_skill_work/full_text.txt`
- `/tmp/pdf_to_skill_work/metadata.json`
- `/tmp/pdf_to_skill_work/sections.json`

For long papers or supplements, inspect targeted sections instead of loading the whole text. Prefer `rg`, `sed`, and section offsets from `sections.json`.

## Step 3 - Identify The Paper's Research Engine

Extract these components from the paper:

- **Research problem**: what bottleneck, contradiction, clinical question, mechanism gap, or computational limitation the paper attacks.
- **Central hypothesis**: the causal, diagnostic, prognostic, therapeutic, or methodological claim being tested.
- **Novelty source**: new cohort, new assay, new algorithm, new causal angle, new cross-scale integration, new intervention, or new evaluation strategy.
- **Study design skeleton**: sample source, grouping, controls, inclusion/exclusion, endpoints, validation, and robustness checks.
- **Evidence chain**: how each figure/table moves the claim forward.
- **Methods spine**: data preprocessing, key experiment/model, statistics, thresholds, software, and validation design.
- **Transferable module**: what can be reused in another topic and what must be redesigned.
- **Failure modes**: assumptions, confounding, overclaiming, weak controls, underpowered validation, missing external validation, or mechanism gaps.

## Step 4 - Decide The Target Skill Type

Choose the generated skill's center of gravity:

- **Clinical prediction / prognosis**: focus on cohort design, feature screening, modeling, calibration, DCA, validation, and clinical utility.
- **Mechanism / wet-lab**: focus on pathway logic, perturbation, rescue experiments, multi-level evidence, and figure progression.
- **Omics / bioinformatics**: focus on dataset selection, preprocessing, differential analysis, enrichment, network/model construction, validation, and interpretation.
- **Intervention / trial / nursing**: focus on PICO, intervention components, endpoints, statistical comparison, implementation, and reporting.
- **Method paper**: focus on algorithmic innovation, baselines, benchmarks, ablation, robustness, and reproducibility.

If unclear, infer from the abstract, methods, and figures.

## Step 5 - Produce The Research Transfer Report

Always include:

- concise paper identity: title, year if available, journal if available
- extracted research engine
- figure/table evidence chain
- reusable protocol for a new direction
- limitations to avoid when migrating
- a `markmap` code block

Use `references/report-template.md` for the output shape.

## Step 6 - Generate The New Skill

Default destination:

```text
/Users/xzw/.codex/skills/<skill-name>/
```

If the user gave a skill name, use it. Otherwise derive a concise slug from the paper's method and target direction, for example:

- `paper-logic-spatial-tumor-microenvironment`
- `paper-logic-luad-brain-metastasis`
- `paper-logic-clinical-prognosis-model`

Generated structure:

```text
<skill-name>/
├── SKILL.md
└── references/
    ├── paper-map.md
    ├── research-transfer.md
    ├── figure-evidence-chain.md
    └── method-adaptation-checklist.md
```

Keep generated `SKILL.md` under 4,000 tokens. Put only the reusable research logic and navigation index there; put detailed extraction and figure notes in references.

## Step 7 - Generated Skill Contract

The generated skill must help the user apply the paper's research thinking to a new direction. It should not be a paper summary.

Generated `SKILL.md` must include:

- when to use this paper-derived skill
- the original paper's core research pattern
- a target-switch workflow
- reusable design modules
- "do not over-transfer" cautions
- references index

Use `references/generated-skill-template.md` for the exact skeleton.

## Step 8 - Quality Rules

- Extract structure, not prose summary.
- Preserve exact method names, model names, endpoints, cohorts, assays, and statistical tests.
- Separate what the original paper proved from what can only be treated as inspiration.
- Do not invent title, journal, year, sample size, datasets, or figure content when absent from the text.
- When moving to a new direction, explicitly map: original variable -> target variable; original population -> target population; original endpoint -> target endpoint; original validation -> target validation.
- Always provide a markmap code block in the final report.
