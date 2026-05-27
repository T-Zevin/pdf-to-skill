<h1 align="center">📄 pdf-to-skill</h1>

<p align="center">
  <strong>Turn a scientific paper PDF into a reusable Codex skill for research-logic transfer.</strong>
  <br />
  <strong>把一篇科研论文 PDF 转换成可复用的 Codex Skill，用于迁移论文研究思路。</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Skill-2563EB?style=for-the-badge" alt="Codex Skill">
  <img src="https://img.shields.io/badge/PDF%20%E2%86%92%20Skill-research%20logic-0F766E?style=for-the-badge" alt="PDF to Skill">
  <img src="https://img.shields.io/badge/Output-Markmap%20%2B%20Skill-F59E0B?style=for-the-badge" alt="Markmap and Skill">
  <img src="https://img.shields.io/badge/README-English%20%7C%20%E4%B8%AD%E6%96%87-7C3AED?style=for-the-badge" alt="Bilingual README">
</p>

<p align="center">
  <a href="#-english">English</a> ·
  <a href="#-中文">中文</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-快速开始">快速开始</a> ·
  <a href="#-workflow">Workflow</a> ·
  <a href="#-markmap">Markmap</a>
</p>

---

![pdf-to-skill workflow](assets/workflow.svg)

## 🇬🇧 Eng

`pdf-to-skill` is inspired by [`book-to-skill`](https://github.com/virgiliojr94/book-to-skill), but it solves a different problem.

`book-to-skill` turns a book into a structured skill so an agent can reuse the author's frameworks. `pdf-to-skill` turns one scientific paper into a research-design skill so an agent can reuse the paper's study logic in a new topic, disease, cohort, dataset, assay, endpoint, or intervention.

This is not a paper summarizer. It extracts the paper's **research engine**:

- 🧠 research problem and central hypothesis
- 🧪 study design skeleton
- 📊 figure and table evidence chain
- 🧬 methods spine and validation logic
- 🔁 original-to-target transfer map
- ⚠️ over-transfer risks and failure modes
- 🗺️ `markmap` mind map for fast review

## 🇨🇳 CN

`pdf-to-skill` 受到 [`book-to-skill`](https://github.com/virgiliojr94/book-to-skill) 启发，但目标不同。

`book-to-skill` 是把一本书转换成结构化 skill，让 Agent 可以复用作者的框架。`pdf-to-skill` 是把一篇科研论文转换成“研究设计 skill”，让 Agent 学会这篇论文的研究思路，并迁移到新的疾病、课题、队列、数据集、实验技术、结局指标或干预方向。

它不是普通论文总结工具，而是提取论文的 **研究发动机**：

- 🧠 研究问题与中心假设
- 🧪 研究设计骨架
- 📊 图表证据链
- 🧬 方法主线与验证逻辑
- 🔁 原论文元素到新方向的迁移映射
- ⚠️ 过度迁移风险与失败模式
- 🗺️ 用于快速复盘的 `markmap` 思维导图

## ✨ What It Generates

| Output | Purpose |
|---|---|
| `Research Transfer Report` | Explains the paper's reusable research logic |
| `markmap` | Shows the paper-to-skill thinking map |
| generated `SKILL.md` | Compact reusable skill entry point |
| `paper-map.md` | Paper identity and section-level research map |
| `research-transfer.md` | Original-to-target migration table |
| `figure-evidence-chain.md` | Figure/table logic and supported claims |
| `method-adaptation-checklist.md` | Validation and over-transfer checklist |

## 📦 Repository Structure

```text
pdf-to-skill/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── output-structure.svg
│   └── workflow.svg
├── references/
│   ├── generated-skill-template.md
│   ├── method-adaptation-rubric.md
│   └── report-template.md
└── scripts/
    ├── extract_paper.py
    └── scaffold_skill.py
```

## 🚀 Quick Start

Copy or symlink this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/pdf-to-skill ~/.codex/skills/pdf-to-skill
```

Then invoke the skill in Codex:

```text
Use $pdf-to-skill to read /path/to/paper.pdf and convert its research logic into a skill for LUAD brain metastasis.
```

Analyze only, without generating a new skill:

```text
Use $pdf-to-skill to analyze /path/to/paper.pdf and output the transfer report plus markmap only.
```

Generate a new direction-switching skill:

```text
Use $pdf-to-skill to read /path/to/paper.pdf, learn its study design, and generate a new skill for spatial transcriptomics in colorectal cancer.
```

## 🚀 快速开始

把本文件夹复制或软链接到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/pdf-to-skill ~/.codex/skills/pdf-to-skill
```

然后在 Codex 中调用：

```text
用 $pdf-to-skill 阅读 /path/to/paper.pdf，并把这篇论文的研究思路转换成一个用于“肺腺癌脑转移”方向的 skill。
```

只分析论文，不生成新 skill：

```text
用 $pdf-to-skill 分析 /path/to/paper.pdf，只输出研究思路迁移报告和 markmap。
```

生成一个新方向 skill：

```text
用 $pdf-to-skill 阅读 /path/to/paper.pdf，学习它的研究设计，并生成一个用于“结直肠癌空间转录组”的新 skill。
```

## 🔧 Direct Script Usage

Extract text and coarse IMRaD sections:

```bash
python3 scripts/extract_paper.py /path/to/paper.pdf
```

Supported inputs:

```text
.pdf
.txt
.md
.docx
```

The extractor writes:

```text
/tmp/pdf_to_skill_work/
├── full_text.txt
├── metadata.json
└── sections.json
```

Optional dependencies:

```bash
# Best CLI fallback for PDFs on macOS
brew install poppler

# Python fallbacks
python3 -m pip install PyPDF2 pdfminer.six python-docx
```

Create an empty paper-derived skill scaffold:

```bash
python3 scripts/scaffold_skill.py \
  --name luad-brain-metastasis-paper-logic \
  --title "Short Paper Title" \
  --target "LUAD brain metastasis" \
  --out ~/.codex/skills
```

It creates:

![Generated skill structure](assets/output-structure.svg)

```text
<skill-name>/
├── SKILL.md
└── references/
    ├── paper-map.md
    ├── research-transfer.md
    ├── figure-evidence-chain.md
    └── method-adaptation-checklist.md
```

## ⚙️ Workflow

```text
Scientific paper PDF
        │
        ▼
scripts/extract_paper.py
        │
        ├── full_text.txt
        ├── metadata.json
        └── sections.json
        │
        ▼
Codex extracts the paper's research engine
        │
        ├── problem + hypothesis
        ├── design skeleton
        ├── methods spine
        ├── figure evidence chain
        └── transfer risks
        │
        ▼
Generated paper-derived skill
```

## 🗺️ Markmap

```markmap
# pdf-to-skill
## Input
### Scientific paper PDF
### Target research direction
## Extraction
### Text and metadata
### IMRaD sections
### DOI and title guess
## Research Engine
### Problem form
### Central hypothesis
### Novelty source
### Study design skeleton
### Methods spine
### Validation logic
## Transfer
### Original population -> target population
### Original variable -> target variable
### Original endpoint -> target endpoint
### Original validation -> target validation
### Original figure logic -> target figure plan
## Output
### Research transfer report
### Generated Codex skill
### Figure evidence chain
### Method adaptation checklist
```

## 🧭 Design Principles

1. **Extract structure, not prose summary**  
   The output should preserve the paper's transferable research design, not retell the paper paragraph by paragraph.

2. **Preserve exact technical details**  
   Keep exact method names, datasets, cohorts, assays, endpoints, thresholds, software, and statistical tests when available.

3. **Separate evidence from inspiration**  
   Clearly distinguish what the original paper proved from what can only inspire a new direction.

4. **Make transfer explicit**  
   Always map original population, variable, endpoint, method, and validation to the target direction.

5. **Keep skills compact**  
   Put the reusable core in `SKILL.md`; put detailed paper notes in `references/` for on-demand loading.

## ❓ FAQ

### Is this just a paper summary tool?

No. A summary tells you what the paper said. `pdf-to-skill` extracts how the paper was designed, why the evidence chain works, and how that logic can be rebuilt for a new research direction.

### Is this RAG?

No. RAG retrieves chunks at query time. `pdf-to-skill` compiles the paper at analysis time into a reusable research-method skill with explicit transfer rules.

### Can it generate a new skill from any paper?

It works best for papers with clear methods, figures, validation, and a reusable research pattern. If a paper is purely descriptive or lacks enough methodological detail, the generated skill should include stronger limitations.

### Can I use it for biomedical papers?

Yes. The workflow is especially useful for clinical prediction, prognosis, omics, wet-lab mechanism papers, spatial transcriptomics, single-cell studies, intervention studies, and computational method papers.

---

<p align="center">
  <strong>pdf-to-skill = paper reading → research logic extraction → reusable Codex skill</strong>
</p>
