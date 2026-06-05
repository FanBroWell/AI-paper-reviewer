# Case 01 · Abstract 改前 / 改后对比

> **声明**:本案例是**虚构的 ML paper abstract**,用来演示 AI-paper-reviewer 的 audit + 改写流程。任何与真实 paper 的相似仅为巧合。

---

## 📝 原始 Abstract

```
Time series models have achieved remarkable progress in both non-financial and 
traditional financial domains. In specific market types, however, characterized 
by extreme volatility and rapid regime shifts, existing time series approaches 
often fall short, hindering progress in the field. In this work, we conduct a 
comprehensive empirical study that revisits the intrinsic structure of the 
data, challenging the prevailing assumption that time series models should 
serve as the primary backbone for forecasting in this domain. Motivated by 
this, we are the first to redefine the prediction problem as a graph learning 
problem, and we introduce a simple yet effective model, called GraphForecaster, 
which utilizes graph attention layers to aggregate cross-entity information. 
On real-world datas, GraphForecaster achieves state-of-the-art forecasting 
accuracy and investment performance than prior approaches. We hope these 
findings open a new research direction in this domain.
```

(168 词)

---

## 🔍 AI-paper-reviewer Audit 结果

### 综合评级: 🔴 **Critical**(3 处 critical + 5 处 major)

### 维度评估表

| 维度 | 检查结果 |
|---|---|
| [A] 逻辑 & 论证 | 🟠 "we are the first" 极危险;"prevailing assumption" 立论过强 |
| [B] 实证严谨性 | 🟠 abstract 0 个数字 |
| [C] 写作质量 | 🔴 **3 处语法错**(`datas`, `state-of-the-art ... than`, 比较级误用) |
| [D] 引用 & 归属 | ✓ |
| [E] 数学符号 | — N/A |
| [F] 双盲匿名性 | 🟡 URL 未给 |
| [G] 格式 / IEEE | ✓ 长度合规 |
| [H] 语言纯净度 | 🔴 `datas` 非英语 |
| [I] 结构 & 衔接 | 🟡 "Motivated by this" 缺桥梁 |
| [J] Reviewer 红旗 | 🔴 **"we are the first to redefine"** + "significantly" 无数字 |

---

### 🔴 Critical 问题

#### C1. `datas` — 基础语法错
```
"On real-world datas, GraphForecaster ..."
```
`data` 是**不可数名词**,**不能加 s**。reviewer 一眼就看到,**第一印象崩**。

#### C2. `state-of-the-art ... than` — 比较级语法错
```
"achieves state-of-the-art forecasting accuracy and investment 
performance than prior approaches"
```
`state-of-the-art` **不是比较级**,不能接 `than`。

#### C3. `we are the first to redefine` — 顶会最危险 claim
顶会 reviewer 看到 `the first` 立即 google 找反例。
任何相关领域 prior work 都可能戳破。

---

### 🟠 Major 问题

#### M1. Abstract 0 个数字
reviewer 扫 abstract 平均 8 秒,看不到数字会以为 "performance gain 不够大"。

#### M2. `comprehensive empirical study` 太空泛
reviewer:"comprehensive 到什么程度?"

#### M3. `the prevailing assumption that time series models should be primary backbone` — 立论过强
reviewer 可能反驳:"很多 paper 已经用 graph,这 assumption 不 prevalent"

#### M4. 没说 graph approach 的核心 insight
abstract 只写 `aggregate cross-entity information`,没告诉读者**为什么这么做有效**。

#### M5. `We hope these findings open a new research direction` — 励志演讲 tone
学术界忌讳。

---

## ✏️ 改写后 Abstract

```
Time-series models have driven significant progress in non-financial and 
traditional financial forecasting. In markets characterized by extreme 
volatility and rapid regime shifts, however, their performance deteriorates 
substantially. We conduct a comprehensive empirical study spanning 11 
baselines across four model families (Transformer, Linear/MLP, periodicity-
aware, and domain-specific) on 66 entity pairs, and find that no time-series 
method consistently surpasses simple linear baselines. Investigating why, we 
identify a structural property of these markets that prior work has largely 
ignored: cross-entity correlations are notably stronger than in equity 
markets (mean |ρ| = 0.53 vs 0.20). Motivated by this, we recast the 
prediction problem as a graph learning problem and propose 
GraphForecaster, a compact (60K parameter) model that combines a 
shared encoder with a graph attention module operating on a 
correlation-induced entity graph. On real-world data, GraphForecaster 
delivers a 30% improvement in annualized risk-adjusted return over the 
strongest prior baseline while using one to two orders of magnitude 
fewer parameters. Our findings establish graph learning as a viable 
paradigm for this domain and motivate further investigation of cross-entity 
structure. Code: anonymous.4open.science/r/XXXX.
```

(195 词)

---

## 📊 9 处关键改动对照

| # | 原文 | 改后 | 修复的问题 |
|---|---|---|---|
| 1 | `we are the first to redefine` | `we recast` | **去掉 critical "first" claim** |
| 2 | `datas` | `data` | 语法 |
| 3 | `state-of-the-art ... than` | `30% improvement over the strongest baseline` | 语法 + **加数字** |
| 4 | `comprehensive empirical study` | `11 baselines across four model families on 66 entity pairs` | **从形容词到具体数字** |
| 5 | `aggregate cross-entity information` | `combines shared encoder with graph attention on correlation-induced entity graph` | **描述更具体** |
| 6 | 无 motivation | `mean \|ρ\| = 0.53 vs 0.20 in equity markets` | **abstract 里塞 killer fact** |
| 7 | `We hope these findings open` | `Our findings establish ... and motivate` | **hope → assert** |
| 8 | 无 code link | `Code: anonymous.4open.science/r/XXXX` | 双盲 + reproducibility |
| 9 | 无参数量 | `60K parameter ... one to two orders of magnitude fewer parameters` | **效率也是卖点** |

---

## 🎓 takeaway(给你 paper 用)

### 1. **Abstract 是 reviewer 的 8 秒第一印象**
任何低级语法错 → 第一印象崩。**投稿前再读 3 遍 Abstract**。

### 2. **数字代替形容词**
- `significantly outperforms` → `+30% over strongest baseline`
- `comprehensive` → `11 baselines across 4 families on N samples`
- `much faster` → `2.4x faster`

### 3. **`we are the first` = 危险 claim**
- 改 `we recast` / `we revisit ... through ... lens` / `to our knowledge, no prior work has systematically`

### 4. **结尾不要 emotional**
- ❌ `We hope to inspire enthusiasm`
- ✅ `Our findings establish X as a paradigm and motivate further investigation`

### 5. **塞 killer fact**
如果你 paper 有一个**反直觉的数字 / 比例**,塞 abstract 里 8 秒抓住 reviewer。

---

## 💡 这个案例的设计哲学

reviewer 看 abstract 不是仔细读,是**快速 scan**:
- 第 1 秒:第一句是不是模板腔?
- 第 2-3 秒:有没有数字?
- 第 4-5 秒:有没有看到危险 claim(`first` / `novel`)?
- 第 6-8 秒:method + result 大概是啥?

**如果前 8 秒留下负面印象,后面读 paper 都带着 bias**。

→ Abstract 是**整篇 paper 性价比最高**的优化对象。

---

## 🔗 相关资料

- 完整审稿: [`prompts/03_abstract_polish.md`](../prompts/03_abstract_polish.md)
- 红旗速查: [`prompts/14_reviewer_red_flags.md`](../prompts/14_reviewer_red_flags.md)
- 去 AI 味: [`prompts/11_anti_AI_smell.md`](../prompts/11_anti_AI_smell.md)
