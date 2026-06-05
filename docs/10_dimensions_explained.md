# 10 维度审查框架详解

> 本文档详细说明 AI-paper-reviewer 的 10 维度审查体系**为什么这么设计 / 每一维实际查什么 / 跟 reviewer 视角的对应关系**。

---

## 设计哲学

顶会 reviewer 看 paper **不是按 section 顺序读**,而是带着 **多个独立 lens** 同时审:

```
Reviewer Mind:
  ├── Logic lens   ──→  这逻辑通吗?
  ├── Empirical lens ──→ 数字可信吗?
  ├── Writing lens ──→ 看得懂吗?
  ├── Citation lens ──→ 引用对吗?
  ├── Math lens   ──→  符号一致吗?
  ├── Anonymity lens ──→ 双盲合规吗?
  ├── Formatting lens ──→ IEEE 标准吗?
  ├── Language lens ──→ 是 native 写的吗?
  ├── Structure lens ──→ 段落组织合理吗?
  └── Red flag lens ──→ 有没有踩雷词?
```

→ **10 个独立 dimension**。每个 paragraph 同时被 10 个 lens 检查。

---

## [A] 逻辑 & 论证

**核心问题**:你的 claim 站得住脚吗?

| 子问题 | 例子 |
|---|---|
| 前提 → 结论 valid? | "X has rich structure, therefore graph methods work" — 是否跳跃? |
| 因果声称过强? | "X causes Y" vs "X correlates with Y" |
| 反例考虑了? | "All baselines fail on domain X" — 有反例吗? |
| 未支持的断言? | "Obviously, X holds" 后没证据 |
| 内部矛盾? | Abstract 说 +57%, Table 显 +50% |

**reviewer 真实反应**:"Authors claim X but Figure 3 contradicts this. Major concern."

---

## [B] 实证严谨性

**核心问题**:你的数字 / 实验能信吗?

| 子问题 | 例子 |
|---|---|
| 数字 cross-consistent? | Abstract 数字 = Table I 数字 = Conclusion 数字 |
| 超参数跟 code 一致? | base.yaml 说 lr=2.5e-4, paper 说 1e-3 → reviewer 怀疑 |
| `significantly` 有 p-value? | 没 → 红旗 |
| Baseline 公平? | 同 seed / data split / lookback / 同 baseline 官方代码 |
| Cherry-pick? | 只报赢的 metric / 最优 seed |

**reviewer 真实反应**:"The 'significant' improvement lacks statistical testing. Reject."

---

## [C] 写作质量

**核心问题**:句子级别看得懂吗?

| 子问题 | 例子 |
|---|---|
| 指代歧义 | "This may cause problems" — this 指代什么? |
| 被动语态滥用 | "It is observed that..." 满段 |
| Hedging 失衡 | `may slightly outperform` vs `dramatically improves` |
| 时态一致 | method 现在时,experiments 过去时 |
| 重复 / 冗余 | 同段说 3 次"我们方法很 simple" |

---

## [D] 引用 & 归属

**核心问题**:你 cite 对了 / cite 够了 / cite 公平了吗?

| 子问题 | 例子 |
|---|---|
| 每 claim 有 cite? | "X is widely studied" 后无 cite |
| cite 真支持 claim? | cite 内容跟你 claim 不沾边 |
| 自引用第三人称? | "Our previous work [X] shows" → 双盲泄露 |
| 格式严格 IEEE? | sentence case / em-dash / vol-no-pp |
| 引用密度合理? | 1 段 10 cite 或 1 段 0 cite 都不正常 |

---

## [E] 数学符号

**核心问题**:数学符号清晰 + 一致吗?

| 子问题 | 例子 |
|---|---|
| 符号定义? | τ 第一次出现没解释含义 |
| 同符号同含义? | τ 在 §3 是 threshold,在 §5 是 std dev → critical 冲突 |
| Equation 编号被 ref? | 有 (3) 但全文没 `Eq. (3)` |
| 加粗格式? | `\textbf{$\tau$}` ❌ vs `$\bm{\tau}$` ✓ |
| math 跟 text 间距? | `$\tau$=0.9` ❌ vs `$\tau = 0.9$` ✓ |

---

## [F] 双盲匿名性

**核心问题**:reviewer 能否反推出作者身份?

| 子问题 | 例子 |
|---|---|
| 身份暗示 | "we" 之外:学校 / lab / 前作 |
| Acknowledgments placeholder? | "Thanks to Prof. X" 未匿名 |
| 自引用第三人称? | "we previously showed in [Y]" → 暴露 |
| 代码链接? | personal GitHub 而非 anonymous.4open.science |
| Metadata? | PDF Author 字段含真名 |

**这一维任何 hit 都是 critical**。

---

## [G] 格式 / IEEE 合规

**核心问题**:格式跟会议模板一致吗?

| 子问题 | 例子 |
|---|---|
| Citation 大小写 | 严格 sentence case(冒号后小写) |
| 双栏溢出 | 表格 / 公式撑出栏 |
| Figure caption 距离 | 太远 / 太近 |
| Table 数字对齐 | 小数点对齐 |
| em-dash 统一 | `---` 不是 `—` 或 `--` |
| `\multicolumn` 位置 | 不在 `\bottomrule` 之后 |

---

## [H] 语言纯净度

**核心问题**:像 native English 写的吗?

| 子问题 | 例子 |
|---|---|
| 中文字符 / 标点 | `,` `。` `;` `:` 残留 → critical |
| Emoji | 📊 ✅ ⚠️ 残留 → critical |
| 翻译机痕迹 | "As shown by experiment" vs "Our experiments show" |
| 美 vs 英 混用 | `analyze` vs `analyse` |
| 双语并置 | "performance / 性能" → critical |

---

## [I] 结构 & 衔接

**核心问题**:整体阅读流畅吗?

| 子问题 | 例子 |
|---|---|
| Topic sentence | 段首一句话点题 |
| Transition | 段尾衔接下一段 |
| 前向引用 | "as we will see in §5" 不滥用 |
| 段长 | >10 行考虑切 |
| Cross-section claim 一致 | Abstract / Contributions / Conclusion 三处 claim 一致 |
| Figure / Table 被 ref + 解读 | 不只 ref,要在正文里**讨论**其内容 |

---

## [J] Reviewer 红旗

**核心问题**:有没有触发 reviewer 雷区的特定词?

详见 [`prompts/14_reviewer_red_flags.md`](../prompts/14_reviewer_red_flags.md)。

最危险 5 个:
1. `we are the first to ...`
2. `obviously / clearly` 无证据
3. `significantly` 无 p-value
4. `mathematical theory / redefine the field`
5. `we hope to inspire enthusiasm`

---

## 维度之间的优先级

并非所有维度等权重。**Reviewer 看 paper 的实际权重**:

```
🔴 Hard fail (critical) — 任一命中可拒稿:
  [F] 双盲泄露
  [J] reviewer 红旗(前 5 个)
  [B] 数字内部矛盾
  [E] 符号冲突

🟠 Major weakness:
  [A] 逻辑跳跃
  [D] cite 不公平
  [B] cherry-pick

🟡 Minor:
  [C] 写作瑕疵
  [G] 格式细节
  [H] 语言瑕疵
  [I] 结构略差
```

→ **优先修 critical**(F / J / B / E),其余按时间精力分配。

---

## 跟其他 audit 框架对比

| 框架 | 关注点 | 跟 AI-paper-reviewer |
|---|---|---|
| ACL Rolling Review | 长 essay-form review | 互补,本框架更结构化 |
| ICML reviewer guidelines | review template | **本框架是基于 reviewer guideline 反向工程** |
| 各种 "AI for academic writing" | 单点润色 | 互补,本框架做整篇 audit |
