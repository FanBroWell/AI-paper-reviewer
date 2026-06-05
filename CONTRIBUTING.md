# Contributing to AI-paper-reviewer

感谢你愿意贡献!这个项目的目标是**收集 / 沉淀 / 共享**顶会论文审稿经验,让每一位科研人都能在投稿前自审到 reviewer 级别。

---

## 🤝 你可以贡献什么

### 1. 新的 reviewer 红旗
你被 reviewer 抓到过哪些低级错误?把它整理成一条加进 [`prompts/14_reviewer_red_flags.md`](prompts/14_reviewer_red_flags.md)。

格式:
```markdown
### N. `具体短语 / 模式`
**为什么危险**:[1-2 句解释 reviewer 怎么看到的]
**修复**:[具体改法 / 替换措辞]
```

### 2. 新的章节 / 场景专项 prompt
现有 14 个 prompt 没覆盖你的场景?提个新文件:
- `15_appendix_polish.md` — Appendix 审查
- `16_figure_audit.md` — Figure 设计与 caption
- `17_response_letter_journal.md` — 期刊 response letter
- ...

格式按现有 prompt 的 Role/Task/Constraints/Protocol 结构。

### 3. 实战案例(examples/)
匿名化的 before / after 改稿对比是 repo 最有说服力的内容。如果你愿意分享:
- 把识别身份的所有字段 generic 化(`<your-name>` → `Author`,`finance` → `domain X`)
- 保留改前 / 改后对照 + 关键修改解读
- 放在 `examples/case_NN_xxx.md`

### 4. 翻译 / 双语
README 的英文版需要 native 校对;部分 prompt 翻译成英文版本扩大受众。

### 5. 工具脚本
比如:
- BibTeX → IEEE bibitem 转换脚本(配合 `09_citation_ieee_format.md`)
- 全局符号扫描脚本(配合 `10_math_notation_check.md`)
- 双盲合规扫描 bash 脚本(配合 `08_double_blind_check.md`)

---

## 📋 提交流程

1. Fork 本仓库
2. 创建分支:`git checkout -b feat/new-red-flag` 或 `feat/case_XX_topic`
3. 提交修改:`git commit -m "feat: add new red flag about X"`
4. Push 到你的 fork:`git push origin feat/new-red-flag`
5. 提 Pull Request,描述清楚:
   - 这是什么类型的贡献(red flag / prompt / example / fix)
   - 来源 / 灵感(自己投稿经验 / 看到的某 reviewer comment / etc.)
   - 如果是改写 case,确认已经匿名化

---

## ✅ PR 通过标准

- 内容跟现有风格一致(用 Role / Task / Constraints / Protocol 结构)
- 中英文 wording 准确,无 typo
- 案例已匿名化(no real names / institutions / specific papers under review)
- 不破坏现有 prompt(只加新文件 / 改 README TOC,**不直接改其他人的 prompt** 除非是修 bug)

---

## 🌏 语言

- 主要语言:**中文**(README / prompt 主体)
- 关键术语保留英文(`reviewer` / `red flag` / `state-of-the-art` 等)
- 欢迎纯英文版本(放 `_EN` 后缀,如 `00_master_workflow_EN.md`)

---

## 💬 讨论

- 大改动 / 不确定的方向:先开 Issue 讨论
- 小修小补 / 加新 red flag:直接 PR

---

## 🙏 致谢

每位 contributor 会在 README 末尾鸣谢。
如果你不希望出现真名,可以在 PR 时说明 "anonymous contribution",我们会用 commit hash 代替。

---

**好的科研写作 prompt 是社区财富 — 你贡献一个 red flag,就帮无数 paper 避开一次退稿。**
