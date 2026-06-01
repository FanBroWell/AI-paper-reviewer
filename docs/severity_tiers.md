# 4 级红旗严重度详解

## 设计原则

类比软件 bug severity:
- **P0 = production down** = 🔴 Critical = paper 拒稿
- **P1 = major** = 🟠 Major = paper 显著扣分
- **P2 = minor** = 🟡 Minor = reviewer 提一句
- **P3 = trivial** = 🟢 Pass = 没问题

---

## 🔴 Critical(拒稿 / desk reject 风险)

### 定义
**任一命中都可能导致 paper 被直接拒**。

### 典型场景
| 类别 | 例子 |
|---|---|
| 双盲泄露 | personal GitHub link / 真名残留 / PDF metadata |
| 数字内部矛盾 | Table 0.025 但 Abstract 写 0.030 |
| 符号冲突 | τ 在 §3 是 threshold,在 §5 是 std dev |
| Critical 红旗词 | `we are the first to ...` / `obviously` |
| 中文 / 双语 / emoji 残留 | 任何位置 |
| 主谓不一致 | `A and B introduces` |

### 处理
**24h 内必须修**。投稿前每条都过一遍。

### Reviewer 真实反应
- "I cannot proceed with the review because the anonymity is broken"(双盲)
- "The numbers in Table 2 contradict Abstract — Major concern"
- "Authors claim to be the first, but [prior work] already proposed this — Reject"

---

## 🟠 Major(主要扣分点)

### 定义
**reviewer 写在 Weaknesses 段的内容**。会显著降低 paper 分数,但不一定拒稿。

### 典型场景
| 类别 | 例子 |
|---|---|
| 无 p-value 的 significant | `significantly outperforms` 但没统计测试 |
| Baseline 不公平 | 用了过时 baseline / 不同 setup |
| `no matter how complex` | dismissive 措辞 |
| Claim 缺 cite | "Widely known that X" 无 reference |
| AR 模型 strawman | 用 AR 代表 SOTA |
| Figure 不被解读 | 只 ref 不 analyze |
| 5 个不相关 cite 凑数 | Intro 段 |
| Table II / Figure 3 dangling | 没在正文 ref + 解读 |

### 处理
**强烈建议改**。如果有时间限制,**优先于 Minor**。

### Reviewer 真实反应
- "The 'significant' claim is not supported by statistical analysis"
- "Baseline comparisons may be unfair due to different lookback windows"
- "Several citations in Section 2 appear loosely related to the work"

---

## 🟡 Minor(reviewer 提一句)

### 定义
**reviewer 会 mention 但不影响 accept/reject 决定**。

### 典型场景
| 类别 | 例子 |
|---|---|
| 模板腔 | `In this paper, we propose ...` |
| 填充语 | `It is worth noting that` |
| 单复数 | `data is` vs `data are` |
| Em-dash 不一致 | `—` `--` `---` 混用 |
| 时态混乱 | method 段过去时 |
| `extensive experiments` | 形容词代替数字 |
| 段长过长(>15 行) | 单段太长难读 |

### 处理
**力推改但不阻塞**。如果时间不够,先放着。

### Reviewer 真实反应
- "The paper would benefit from polishing the writing in Section 2"
- "Minor typos throughout"
- "Some claims could be more quantitative"

---

## 🟢 Pass(完全通过)

### 定义
**该段在该维度上没有可挑剔的问题**。

### 含义
- 不是 "perfect"(perfect 不存在)
- 而是 "reviewer 不会提任何 comment"
- 是 audit 的**目标状态**

---

## 严重度判定决策树

```
段落出现问题
   ↓
是否双盲泄露 / Critical 红旗词 / 中文残留 / 数字矛盾?
   ↓ Yes
   🔴 Critical
   ↓ No
是否影响 reviewer 对 paper 主要价值的评估?
   ↓ Yes
   🟠 Major
   ↓ No
是否 reviewer 会 mention 但不扣大分?
   ↓ Yes
   🟡 Minor
   ↓ No
   🟢 Pass
```

---

## 修复优先级

### 时间充足(投稿前 2 周以上)
```
1. 修所有 Critical
2. 修 80%+ Major
3. 修 50%+ Minor
4. Reviewer Q&A 模拟
```

### 时间紧张(投稿前 24h)
```
1. 修所有 Critical(必须)
2. 修核心段落的 Major(Abstract / Intro / Conclusion)
3. Minor 全部 skip
```

### 时间极限(投稿前 2h)
```
1. 双盲合规扫描(`08_double_blind_check.md`)
2. 数字 cross-consistency 抽查 3 个关键数字
3. 提交
```

---

## 严重度 vs 修复成本矩阵

```
              修复成本
              低                    高
        ┌───────────────┬───────────────┐
        │               │               │
        │  P0 红色      │  P1 黄色      │
   重   │  必修         │  必修但拆任务  │
   要   │  (typo, em-   │  (重做实验,    │
   性   │   dash 统一)  │   补 std)     │
        │               │               │
        │   ⭐ 优先做    │   ⏳ 长任务   │
   高   ├───────────────┼───────────────┤
        │               │               │
        │  P2 绿色      │  P3 灰色      │
        │  顺手改       │  时间够再改    │
        │  (措辞 polish)│  (重写 Intro) │
        │               │               │
        │   ✅ 顺手      │   🤔 量力     │
   低   └───────────────┴───────────────┘
```
