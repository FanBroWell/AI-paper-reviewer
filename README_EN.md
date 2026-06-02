<div align="center">

<img src="assets/banner.png" alt="Top-conf-PaperReviewer" width="100%" />

# 🔍 Top-conf-PaperReviewer

**Let AI act as the strictest top-tier conference reviewer for you**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[🇨🇳 中文](README.md) · 🇬🇧 English

</div>

---

> **Stop letting reviewers find low-level errors for you. Find them yourself before submission.**

## 📖 Why this project

When you submit your paper, reviewers come back with 30 comments. **25 of them are things you could have caught yourself**:

- `we are the first to ...` — the most dangerous claim at top-tier venues
- `θ` vs `τ` mixed in Algorithm 1 — internal inconsistency
- Numbers in table don't match the prose — reviewer cross-checks and busts you
- `Significantly outperforms` without p-value — quantitative red flag
- Author's real name / institution leaked in anonymous submission
- `we sincerely hope to inspire enthusiasm` — motivational-speech tone
- Em-dash mixed `—` `--` `---` — formatting chaos
- ......

**You do not need a reviewer to teach you these.**

This project open-sources a strict reviewer-grade audit workflow refined through real **NeurIPS / AAAI / ICDM / ICML / KDD** submissions, letting your paper survive **a top-tier reviewer's eye before submission**.

---

## ✨ Highlights

- 🎯 **10-dimension audit framework** — logic / empirics / writing / citations / math / anonymity / formatting / language / structure / red flags
- 🚨 **4-tier severity system** — 🔴 Critical / 🟠 Major / 🟡 Minor / 🟢 Pass
- 📊 **Paragraph-level granular review** — every paragraph gets 10-dim scoring + line-by-line rewrites
- 🔁 **Global issue tracking** — `redefine`-class claims, `state-of-the-art` frequency, symbol consistency tracked across the entire paper
- 🤝 **Top-tier venue native** — IEEE / ACM / NeurIPS / ICLR standards
- 📋 **Reproducibility checklist helper** — fill 21-item NeurIPS / ICML questionnaire in 1 minute
- 🛡️ **Double-blind compliance scanner** — auto-detect real names / emails / institutions / paths / metadata leaks

---

## 🚀 Quick Start

```
1. Open your AI chat (Claude / ChatGPT / Gemini)
2. Copy prompts/02_paragraph_audit.md into the chatbox
3. AI replies "Ready"
4. Paste paragraphs of your paper, receive strict audit + rewrite suggestions
```

**Most used:** [`prompts/02_paragraph_audit.md`](prompts/02_paragraph_audit.md) — paragraph-by-paragraph review during editing.

---

## 📑 Contents

### Part I: Core audit workflows
- [`00_master_workflow.md`](prompts/00_master_workflow.md) — Full 10-dimension audit (master)
- [`01_full_paper_audit.md`](prompts/01_full_paper_audit.md) — Whole-paper one-shot audit
- [`02_paragraph_audit.md`](prompts/02_paragraph_audit.md) ⭐ — Paragraph audit + global tracking (most used)

### Part II: Section-specific
- [`03_abstract_polish.md`](prompts/03_abstract_polish.md)
- [`04_intro_polish.md`](prompts/04_intro_polish.md)
- [`05_method_polish.md`](prompts/05_method_polish.md)
- [`06_experiments_check.md`](prompts/06_experiments_check.md)
- [`07_conclusion_polish.md`](prompts/07_conclusion_polish.md)

### Part III: Targeted checks
- [`08_double_blind_check.md`](prompts/08_double_blind_check.md)
- [`09_citation_ieee_format.md`](prompts/09_citation_ieee_format.md)
- [`10_math_notation_check.md`](prompts/10_math_notation_check.md)
- [`11_anti_AI_smell.md`](prompts/11_anti_AI_smell.md)

### Part IV: Pre / post submission
- [`12_reviewer_response.md`](prompts/12_reviewer_response.md) — Rebuttal helper
- [`13_repro_checklist.md`](prompts/13_repro_checklist.md) — Reproducibility checklist

### Part V: Red flag quick reference
- [`14_reviewer_red_flags.md`](prompts/14_reviewer_red_flags.md)

---

## 📊 Real examples

- [`examples/case_01_abstract_before_after.md`](examples/case_01_abstract_before_after.md) — Abstract before / after with 9 key edits.
- [`examples/case_02_method_audit.md`](examples/case_02_method_audit.md) — Methodology symbol-conflict diagnosis + fix walkthrough.

---

## 📚 Supporting docs

- [`docs/10_dimensions_explained.md`](docs/10_dimensions_explained.md) — full 10-dimension framework
- [`docs/severity_tiers.md`](docs/severity_tiers.md) — 4-tier severity system
- [`docs/usage_guide.md`](docs/usage_guide.md) — advanced usage tips

---

## 🎓 10-dimension framework

| Dimension | Core question |
|---|---|
| [A] Logic & argument | Premise → conclusion valid? Counter-examples considered? |
| [B] Empirical rigor | Numbers consistent cross-table? Baselines fair? |
| [C] Writing quality | Ambiguous referents? Passive voice abuse? Tense consistency? |
| [D] Citations | Each claim has a cite? Self-citation third-person? |
| [E] Math notation | Same symbol used for different things? |
| [F] Anonymity | Identity hints beyond "we"? Metadata cleared? |
| [G] IEEE formatting | Citation titles sentence case? Decimal alignment? |
| [H] Language purity | Chinese chars / emoji / bilingual residues? |
| [I] Structure & flow | Topic sentence? Transitions? Figures/Tables explained? |
| [J] Reviewer red flags | `we are the first` / `no matter how complex` / `obviously`? |

See [`docs/10_dimensions_explained.md`](docs/10_dimensions_explained.md) for details.

---

## 🚨 4-tier severity

| Tier | Meaning | Action |
|---|---|---|
| 🔴 Critical | Reject risk | **Must fix** |
| 🟠 Major | Significant deduction | **Strongly recommended** |
| 🟡 Minor | Minor comment | **Recommended** |
| 🟢 Pass | OK | — |

See [`docs/severity_tiers.md`](docs/severity_tiers.md) for details.

---

## 🤝 Contributing

Found a new reviewer red flag? Encountered an uncovered scenario? PRs welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 🌟 Star History

If this project ever helped you avoid one reviewer rejection, **give it a Star so more people can find it** ⭐

---

## 📄 License

[MIT](LICENSE) — Commercial use / modification / distribution allowed with attribution.
