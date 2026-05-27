#!/usr/bin/env python3
"""Create an empty paper-derived skill scaffold for pdf-to-skill."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "paper-derived-skill"


def write_if_missing(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def skill_md(name: str, title: str, target: str) -> str:
    return f"""---
name: {name}
description: "Paper-derived research logic from {title}. Use when adapting this paper's study design, methods, evidence chain, and figure strategy to {target}."
argument-hint: [target question, disease/topic, dataset, endpoint, or figure plan]
---

# {title} - Research Logic Skill

## When To Use

Use this skill to adapt the original paper's research design to {target}.

## Core Research Pattern

- **Problem form**:
- **Hypothesis form**:
- **Design pattern**:
- **Evidence pattern**:
- **Validation pattern**:
- **Claim boundary**:

## Direction-Switch Workflow

1. Restate the new direction in the same problem form.
2. Map original population/sample to target population/sample.
3. Map original exposure/intervention/feature to target variable.
4. Map original endpoint/phenotype to target endpoint.
5. Rebuild the evidence chain as discovery -> validation -> explanation -> robustness.
6. Check whether the original assumptions still hold.
7. Draft figure sequence and analysis plan before writing results.

## References

- [paper-map.md](references/paper-map.md)
- [research-transfer.md](references/research-transfer.md)
- [figure-evidence-chain.md](references/figure-evidence-chain.md)
- [method-adaptation-checklist.md](references/method-adaptation-checklist.md)
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a paper-derived Codex skill scaffold.")
    parser.add_argument("--name", required=True, help="Skill folder/name slug.")
    parser.add_argument("--title", required=True, help="Short source paper title.")
    parser.add_argument("--target", default="a new research direction", help="Target direction for adaptation.")
    parser.add_argument("--out", default=".", help="Output parent directory.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing scaffold files.")
    args = parser.parse_args()

    name = slugify(args.name)
    root = Path(args.out).expanduser().resolve() / name
    references = root / "references"

    write_if_missing(root / "SKILL.md", skill_md(name, args.title, args.target), args.overwrite)
    write_if_missing(
        references / "paper-map.md",
        f"""# Paper Map

## Source

- Title: {args.title}
- Target direction: {args.target}
- DOI:
- Journal / year:

## Section Logic

- Abstract:
- Introduction:
- Methods:
- Results:
- Discussion:
""",
        args.overwrite,
    )
    write_if_missing(
        references / "research-transfer.md",
        """# Research Transfer

| Original paper element | Keep | Redesign for target direction | Risk |
|---|---|---|---|
| Population / samples | | | |
| Exposure / feature | | | |
| Outcome / phenotype | | | |
| Model / assay / analysis | | | |
| Validation | | | |
""",
        args.overwrite,
    )
    write_if_missing(
        references / "figure-evidence-chain.md",
        """# Figure Evidence Chain

| Unit | Question answered | Evidence type | Method | Claim supported | Transferable use |
|---|---|---|---|---|---|
| Fig. 1 | | | | | |
| Fig. 2 | | | | | |
""",
        args.overwrite,
    )
    write_if_missing(
        references / "method-adaptation-checklist.md",
        """# Method Adaptation Checklist

- [ ] Target question has the same logical form as the original paper.
- [ ] Target population/sample is explicitly mapped.
- [ ] Target endpoint is measurable.
- [ ] Discovery and validation are separated.
- [ ] Thresholds and cutoffs are re-estimated.
- [ ] Confounding and bias risks are stated before claims.
- [ ] Figure sequence matches the target evidence chain.
""",
        args.overwrite,
    )
    print(root)


if __name__ == "__main__":
    main()
