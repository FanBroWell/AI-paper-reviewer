<div align="center">

<img src="assets/banner.png" alt="AI-paper-reviewer" width="100%" />

# 🔍 AI-paper-reviewer

**Catch reviewer comments before reviewers do.**

A strict pre-submission prompt toolkit for researchers submitting to NeurIPS, ICML, ICLR, AAAI, KDD, and other top-tier venues. It helps you audit logic, claims, experiments, citations, anonymity, reproducibility, and rebuttal readiness before your paper reaches reviewers.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[🇨🇳 中文](README.md) · 🇬🇧 English

</div>

---

> Most rejection pain does not come from one fatal flaw. It comes from many avoidable comments: unsupported claims, weak positioning, inconsistent numbers, missing citations, unclear writing, and double-blind leaks.

## What this helps you catch

- Claims that sound stronger than your evidence supports
- `significant`, `novel`, or `state-of-the-art` wording that reviewers may challenge
- Citation gaps, weak related-work positioning, and hallucinated references
- Table / figure / abstract number mismatches
- Reproducibility checklist issues before submission
- Double-blind leaks in text, links, metadata, and acknowledgments
- Rebuttal risks that can be fixed before reviews arrive

## What this project is

AI-paper-reviewer is a collection of copy-ready paper review prompts for Claude, ChatGPT, Gemini, and Codex. It synthesizes a reviewer-grade self-audit workflow from **publicly available reviewer guidelines, author-reviewer discussions on OpenReview, and the author's multi-venue submission and rebuttal experience** across NeurIPS / ICML / ICLR / AAAI / KDD.

It is not a paper-writing shortcut. It is a pre-submission audit layer that helps you see your manuscript through a reviewer's eyes before the review arrives.

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

## 🚀 Start in 3 minutes

```
1. Open your AI chat (Claude / ChatGPT / Gemini)
2. Copy prompts_en/02_paragraph_audit.md into the chatbox
3. AI replies "Ready"
4. Paste paragraphs of your paper and get strict audit + directly usable rewrite suggestions
```

Most English users start with [`prompts_en/02_paragraph_audit.md`](prompts_en/02_paragraph_audit.md): use it paragraph by paragraph while editing to track claims, citations, notation, numbers, and reviewer red flags.

Chinese prompts are kept in [`prompts/`](prompts/). English prompt versions are kept in [`prompts_en/`](prompts_en/) with matching filenames.

---

## 📑 Contents

### Part I: Core audit workflows
- [`00_master_workflow.md`](prompts_en/00_master_workflow.md) — Full 10-dimension audit (master)
- [`01_full_paper_audit.md`](prompts_en/01_full_paper_audit.md) — Whole-paper one-shot audit
- [`02_paragraph_audit.md`](prompts_en/02_paragraph_audit.md) ⭐ — Paragraph audit + global tracking (most used)

### Part II: Section-specific
- [`03_abstract_polish.md`](prompts_en/03_abstract_polish.md)
- [`04_intro_polish.md`](prompts_en/04_intro_polish.md)
- [`05_method_polish.md`](prompts_en/05_method_polish.md)
- [`06_experiments_check.md`](prompts_en/06_experiments_check.md)
- [`07_conclusion_polish.md`](prompts_en/07_conclusion_polish.md)

### Part III: Targeted checks
- [`08_double_blind_check.md`](prompts_en/08_double_blind_check.md)
- [`09_citation_ieee_format.md`](prompts_en/09_citation_ieee_format.md)
- [`10_math_notation_check.md`](prompts_en/10_math_notation_check.md)
- [`11_anti_AI_smell.md`](prompts_en/11_anti_AI_smell.md)

### Part IV: Pre / post submission
- [`12_reviewer_response.md`](prompts_en/12_reviewer_response.md) — Rebuttal helper
- [`13_repro_checklist.md`](prompts_en/13_repro_checklist.md) — Reproducibility checklist

### Part V: Red flag quick reference
- [`14_reviewer_red_flags.md`](prompts_en/14_reviewer_red_flags.md)

---

## 🌟 Star History

<a href="https://www.star-history.com/#FanBroWell/AI-paper-reviewer&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=FanBroWell/AI-paper-reviewer&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=FanBroWell/AI-paper-reviewer&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=FanBroWell/AI-paper-reviewer&type=Date" />
  </picture>
</a>

If this project helps you avoid even one reviewer rejection, **give it a Star so more people can find it** ⭐

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

## 📄 License

[MIT](LICENSE) — Commercial use / modification / distribution allowed with attribution.
