<div align="center">

<img src="assets/banner.png" alt="Top-conf-PaperReviewer" width="100%" />

# 🔍 Top-conf-PaperReviewer

**让 AI 替你做最严格的顶会 Reviewer**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Made for Research](https://img.shields.io/badge/made%20for-academic%20research-orange.svg)](#)

🇨🇳 中文 · [🇬🇧 English](README_EN.md)

</div>

---

> **不要再让 reviewer 替你找低级错误。投稿前自己找出来。**

## 📖 为什么做这个项目

当你提交论文,reviewer 报回 30 条 comment,其中 **25 条是你完全可以投稿前自己发现的**:

- `we are the first to ...` — 顶会**最危险的 claim**(reviewer 一找反例就崩)
- Algorithm 1 里 `θ` 跟 `τ` 混用 — **内部矛盾**
- Table 数字跟正文不一致 — **reviewer 一对就崩**
- `Significantly outperforms` 但没 p-value — **量化红旗**
- Anonymous 投稿里残留作者真名 / 学校 / 邮箱 — **双盲泄露**
- "we sincerely hope to inspire enthusiasm" — **励志演讲 tone**
- Em-dash 用 `—` `--` `---` 三种混用 — **格式失控**
- ......

**这些错误,不需要 reviewer 来教你**。

本项目把作者本人投稿 **NeurIPS / AAAI / ICDM / ICML / KDD** 实战中提炼的**严格审稿工作流**开源,让你的论文在**投稿前**就过一遍**顶会 reviewer 的眼**。

---

## ✨ 核心特色

- 🎯 **10 维度审查框架** — 逻辑 / 实证 / 写作 / 引用 / 数学符号 / 双盲 / 格式 / 语言 / 结构 / 红旗
- 🚨 **4 级红旗体系** — 🔴 Critical / 🟠 Major / 🟡 Minor / 🟢 Pass,**优先级清晰**
- 📊 **段落级精细审查** — 每段给 10 维度评分 + 逐句改写建议
- 🔁 **全局问题追踪** — `redefine` 类 claim、`state-of-the-art` 频次、符号一致性**贯穿全篇**
- 🤝 **顶会风格 native** — IEEE / ACM / NeurIPS / ICLR 标准
- 📋 **可复现性 checklist 助手** — 帮你 1 分钟填好 21 项 NeurIPS / ICML reproducibility 问卷
- 🛡️ **双盲合规扫描** — 自动检测真名 / 邮箱 / 学校 / 路径 / metadata 残留

---

## 🚀 Quick Start

```
1. 打开你的 AI 对话(Claude / ChatGPT / Gemini 都行)
2. 复制 prompts/02_paragraph_audit.md 整块到对话框
3. AI 回复 "准备好了"
4. 按段落贴 paper 内容,接收严格审查 + 改写建议
```

**最常用:[`02_paragraph_audit.md`](prompts/02_paragraph_audit.md)** — 平时改稿一段一段过。

---

## 📑 目录

### Part I: 核心审稿工作流

| 文件 | 用途 | 使用场景 |
|---|---|---|
| [`00_master_workflow.md`](prompts/00_master_workflow.md) | 完整 10 维度审稿工作流 | **主入口** |
| [`01_full_paper_audit.md`](prompts/01_full_paper_audit.md) | 整篇 paper 审查 | 大 milestone 用 |
| [`02_paragraph_audit.md`](prompts/02_paragraph_audit.md) ⭐ | 单段精细审查 + 全局追踪 | **最高频** |

### Part II: 章节专项

| 文件 | 用途 |
|---|---|
| [`03_abstract_polish.md`](prompts/03_abstract_polish.md) | Abstract 专项审查 |
| [`04_intro_polish.md`](prompts/04_intro_polish.md) | Introduction 专项(砍 cite + 去 puffery) |
| [`05_method_polish.md`](prompts/05_method_polish.md) | Methodology 专项(符号 + 算法描述) |
| [`06_experiments_check.md`](prompts/06_experiments_check.md) | Experiments + Table 数字一致性 |
| [`07_conclusion_polish.md`](prompts/07_conclusion_polish.md) | Conclusion 专项(去 marketing tone) |

### Part III: 专项 Check

| 文件 | 用途 |
|---|---|
| [`08_double_blind_check.md`](prompts/08_double_blind_check.md) | 🛡️ 双盲合规扫描(姓名 / 路径 / metadata) |
| [`09_citation_ieee_format.md`](prompts/09_citation_ieee_format.md) | BibTeX → IEEE bibitem 转换 |
| [`10_math_notation_check.md`](prompts/10_math_notation_check.md) | τ / θ / σ / ρ 符号一致性 |
| [`11_anti_AI_smell.md`](prompts/11_anti_AI_smell.md) | 去 "AI 味"(机翻痕迹 / 模板腔) |

### Part IV: 投稿前后

| 文件 | 用途 |
|---|---|
| [`12_reviewer_response.md`](prompts/12_reviewer_response.md) | Rebuttal / Response to reviewer 起草 |
| [`13_repro_checklist.md`](prompts/13_repro_checklist.md) | 21 项 NeurIPS Reproducibility Yes/No/NA 助手 |

### Part V: 红旗速查

| 文件 | 用途 |
|---|---|
| [`14_reviewer_red_flags.md`](prompts/14_reviewer_red_flags.md) | 顶会 reviewer 红旗速查表(随时翻) |

---

## 📊 实战效果

### 真实案例:Abstract 改前 / 改后

[`examples/case_01_abstract_before_after.md`](examples/case_01_abstract_before_after.md)
关键修改 9 处:`we are the first` → `we recast`、`significantly outperforms` → 具体数字、`world's largest by volume` → 删除等。

### 真实案例:Methodology 符号一致性修复

[`examples/case_02_method_audit.md`](examples/case_02_method_audit.md)
Algorithm 描述里 `θ` 跟 `τ` 同时出现导致内部矛盾的修复全过程。

---

## 📚 支持文档

- [`docs/10_dimensions_explained.md`](docs/10_dimensions_explained.md) — 10 维度框架详解
- [`docs/severity_tiers.md`](docs/severity_tiers.md) — 4 级红旗体系详解
- [`docs/usage_guide.md`](docs/usage_guide.md) — 进阶使用指南(跨段对照 / token 优化 / 自动化 pipeline 等)

---

## 🎓 10 维度审查框架

| 维度 | 核心问题 |
|---|---|
| **[A] 逻辑 & 论证** | 前提 → 结论是否成立?反例考虑了吗? |
| **[B] 实证严谨性** | 数字 cross-table 一致?baseline 公平?`significantly` 有 p-value? |
| **[C] 写作质量** | 指代歧义?被动语态滥用?时态一致? |
| **[D] 引用 & 归属** | 每个 claim 有 cite?自引用第三人称? |
| **[E] 数学符号** | 同一符号在不同位置代表不同含义? |
| **[F] 双盲匿名性** | "we" 之外的身份暗示?metadata 已清空? |
| **[G] 格式 / IEEE** | citation 标题 sentence case?表格小数点对齐? |
| **[H] 语言纯净度** | 中文字符 / emoji / 双语并置残留? |
| **[I] 结构 & 衔接** | topic sentence?transition?Figure / Table 在 ref 后被解读? |
| **[J] Reviewer 红旗** | `we are the first` / `no matter how complex` / `obviously` 等危险词? |

详见 [`docs/10_dimensions_explained.md`](docs/10_dimensions_explained.md)。

---

## 🚨 4 级红旗体系

| 等级 | 含义 | 处理 |
|---|---|---|
| 🔴 **Critical** | reviewer 直接拒 / desk reject 风险 | **必须改** |
| 🟠 **Major** | reviewer 主要扣分点 | **强烈建议改** |
| 🟡 **Minor** | reviewer 提 minor comment | **力推改** |
| 🟢 **Pass** | 完全通过 | — |

详见 [`docs/severity_tiers.md`](docs/severity_tiers.md)。

---

## 🤝 贡献

发现新的 reviewer 红旗?碰到没覆盖的场景?欢迎 PR。详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

---

## 🌟 Star History

如果这个项目帮你避免了一次 reviewer 退稿,**点个 Star 让更多人看到** ⭐

---

## 📄 License

[MIT](LICENSE) — 自由商用 / 修改 / 分发,**唯一要求是 attribution**。
