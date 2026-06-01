# 使用进阶指南

## 1. 选择正确的 prompt

```
我想要做什么?
   ↓
┌──────────────────────────────────────────────────┐
│  日常改一段                  → 02_paragraph_audit  │
│  milestone 整篇过            → 01_full_paper_audit │
│  只查 Abstract               → 03_abstract_polish  │
│  只查 Intro                  → 04_intro_polish     │
│  只查 Method                 → 05_method_polish    │
│  只查 Experiments + Table    → 06_experiments_check│
│  只查 Conclusion             → 07_conclusion_polish│
│  投稿前查双盲                → 08_double_blind     │
│  改 BibTeX 引用              → 09_citation_ieee    │
│  查数学符号一致性             → 10_math_notation    │
│  去 AI 味                    → 11_anti_AI_smell    │
│  写 Rebuttal                 → 12_reviewer_response│
│  填 Reproducibility checklist → 13_repro_checklist │
│  Cmd+F 找红旗                → 14_reviewer_red_flags│
└──────────────────────────────────────────────────┘
```

---

## 2. 跟不同 AI 的兼容性

| AI | 长上下文 | 中文支持 | 严格度 | 推荐度 |
|---|---|---|---|---|
| **Claude(任意)** | ★★★★★(200K) | ★★★★★ | ★★★★★ | ⭐ 最佳 |
| **GPT-4o / o1** | ★★★★(128K) | ★★★★ | ★★★★ | 推荐 |
| **Gemini 2.5 Pro** | ★★★★★(2M) | ★★★★ | ★★★ | 推荐(长 paper) |
| **GPT-3.5** | ★★(16K) | ★★★ | ★★ | 不推荐(严格度不够) |
| **本地 LLM(Llama 3 70B)** | ★★★(8-32K) | ★★ | ★★ | 仅 demo |

→ **推荐 Claude 长会话**:从 abstract 一直审到 conclusion 在同一对话里,**全局追踪**(`redefine` 出现次数 / 数字一致性)能维持。

---

## 3. 长 paper 怎么分块审查

### 策略 A:**按 section 分批**
```
对话 1:Abstract + Introduction(§1)
对话 2:Related Work(§2)
对话 3:Methodology(§3)
对话 4:Experiments(§4-5)
对话 5:Conclusion + Discussion(§6-7)
```

→ 每个对话 ~10-20K tokens,Claude / GPT 都 cover。

### 策略 B:**同一对话累计**
适合 Claude 长上下文:**整篇贴在一个 thread**,AI 全局视角更强。

但注意:
- token 撑爆时 AI 会忘开头
- 每贴一段后,**让 AI 维护全局追踪表**(`redefine` 出现 N 次 / 关键数字)

---

## 4. 常见用法 idioms

### idiom 1:**多轮 polish**
```
轮 1: "按 02 prompt 审这段,只标 critical 和 major"
轮 2: 修完后 → "再审一遍,确认 critical 都修了 + 还有什么"
轮 3: 修完后 → "最终一轮,顺手 polish minor"
```

### idiom 2:**逐句精修**
```
"请把这一句改写 3 种不同 tone(中性 / 强 / 弱),让我选"
```

### idiom 3:**红旗逐个排查**
```
"按 14_reviewer_red_flags.md 的 46 个红旗,逐个检查这段是否命中"
```

### idiom 4:**跨段对照**
```
"刚才贴的 Abstract 数字是 0.025,
现在贴的 Conclusion 是 0.030 — 哪个对?"
```

---

## 5. 如何让 AI 更严格

加在 prompt 开头或单独说:

```
[严格度] maximum — 把所有可能的 reviewer 反对意见全部列出来,即使是 minor。
[假设] 假设你是 NeurIPS 2025 的 area chair,paper 已经被 2 个 reviewer 倾向 reject。
```

→ AI 会进入 "找茬 mode",更挑剔。

---

## 6. 如何让 AI 更宽松(早期 draft 用)

```
[严格度] low — 只标 critical,不列 minor。
[假设] 这是早期 draft,作者还在打磨 idea 阶段。
```

→ AI 会跳过细节,只看大方向。

---

## 7. Token 节省技巧

- 不需要 critical 之外内容时,加 `[输出简洁度] high`
- 长 paper 分块时,**每块新对话**(避免历史 token 堆积)
- 用 `02_paragraph_audit.md` 代替 `00_master_workflow.md`(同效但短 50%)
- 改稿后**只贴改后的**,不贴原文(让 AI 直接审改后版本)

---

## 8. 跟现有工具的配合

| 工具 | 用法 |
|---|---|
| **Overleaf** | 在 Overleaf 编辑 LaTeX → 复制段落 → 贴到 Claude → 应用改写 |
| **Cursor / Windsurf** | 装 Claude 插件,在 IDE 里直接 audit |
| **Notion / Obsidian** | 把本 repo prompts/ 整个导入做成 template |
| **本地 Claude API** | 写个 cron / hook,每次 git commit LaTeX 自动 audit |

---

## 9. 高级:自动化 audit pipeline

```bash
# 假想的 CI 流程
on_latex_commit() {
    # 提取每段
    paragraphs = extract_paragraphs(paper.tex)
    
    # 用 Claude API 跑 02 prompt
    for p in paragraphs:
        result = claude_api(prompt_02_paragraph_audit + p)
        save_to_review_log(result)
    
    # 全局扫描
    global_check = claude_api(prompt_08_double_blind + repo_path)
    save_to_review_log(global_check)
    
    # 输出报告
    print_summary()
}
```

→ 把审稿做成 **CI/CD pipeline**,**每 commit 自动 audit**。

(这部分需要写代码,**未来 PR 欢迎贡献**!)

---

## 10. 不要犯的错误

### ❌ 把 AI 当 ground truth
AI 找问题,**你判断是否真改**。某些 hedging 是 intentional(你想留 caveat),AI 标 minor 不代表必改。

### ❌ 数字盲信
AI 可能误判 "Table 是 0.025,Abstract 也是 0.025,所以一致" — 但 actually 你 abstract 写的 +57.5% (这是 vs baseline),AI 没看懂。**自己 cross-check**。

### ❌ AI 改写直接抄
AI 改写**作为参考**,不要直接 copy-paste。**用你的 voice 重写**,否则容易触发 AI-text detector。

### ❌ 一次性贴整篇 paper
token 撑爆 → AI 模糊化处理 → 找不到 critical。**分块,每块 ≤ 5 段**。
