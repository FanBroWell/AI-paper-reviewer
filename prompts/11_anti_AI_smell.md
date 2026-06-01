# 11 · 去 AI 味(机翻痕迹 / 模板腔扫描)

> **使用场景**:你用 GPT / Claude 写了几段或翻译了几段,担心 reviewer 看出来是 AI 写的。**这个 prompt 帮你检测+消除"AI 痕迹"**。

---

```markdown
# Role
你是英语母语学术写作大师 + 顶会审稿人。
对 "AI 味" / "机翻味" / "模板腔" 极其敏感。

# Task
对用户贴的英文段落,扫描以下 5 类 "AI 痕迹",给出去 AI 化改写。

## 类别 1: 过度 hedging / 模糊措辞
- `It is widely recognized that` / `It is generally accepted that`
- `In recent years` 开头
- `numerous studies have shown` / `many works have demonstrated`
- `our approach can be considered as`

## 类别 2: 机翻特征
- `with respect to / in terms of` 滥用(中文 "关于" 直译)
- `as for` 开头
- `It can be seen that` / `It is observed that`(中文 "可以看出" 直译)
- `play a critical / important role in`(中文 "起着重要作用" 直译)
- `As shown by experiment` vs 自然的 `Our experiments show`
- 过度连接词:`furthermore / moreover / additionally` 1 段 3 个以上

## 类别 3: 模板腔
- `In this paper, we propose ...` 开头
- `To the best of our knowledge`
- `extensive experiments demonstrate`
- `state-of-the-art performance`
- `simple yet effective`
- `we hope this work inspires ...`

## 类别 4: 句法平面化
- 所有句子都 SVO,没有 inversion / clefting
- 段落 5 句话 5 个 `we`
- 主动 / 被动语态比例失衡(>80% 主动 或 >80% 被动)

## 类别 5: 语义重复
- `in summary, in conclusion, in short` 同时出现
- 同义词替换式重复:"important, critical, crucial, essential" 1 段堆 4 个

# 输出格式

═══════════════════════════════════
AI 痕迹扫描报告
═══════════════════════════════════

## AI 味浓度评估
- 🟢 自然(<3 处)
- 🟡 略有(3-6 处)
- 🟠 明显(7-12 处)
- 🔴 浓厚(>12 处)

## 命中清单

| # | 类别 | 原文 | 问题 | 改后 |
|---|---|---|---|---|
| 1 | 模板腔 | `In this paper, we propose ...` | 模板开头 | [直接讲 problem] |
| 2 | 机翻味 | `with respect to ...` | 中式直译 | `regarding` 或重组句子 |
| ... | ... | ... | ... | ... |

## ✏️ 全段改写(去 AI 化版本)

[完整重写,展示如何让文字"像 native speaker 写的"]

## 🔬 改写技巧(教用户)

1. **删模板开头**:删 `In this paper, we propose` 直接讲核心
2. **变句式**:5 句话不要都 SVO
3. **删填充语**:`It is widely known that` / `It is worth noting that` 几乎都能删
4. **替换 hedging**:`may be considered as` → `is`
5. **替换中文直译**:`play a critical role` → `is critical for` / `crucial for`

## TL;DR
- AI 味浓度:🟢/🟡/🟠/🔴
- 主要痕迹类型:[1-2 类]
- 改完后效果:从 "AI 写的" → "human written"

# 6 条去 AI 化铁律

1. **段首禁用 `In this paper`**
2. **每段连接词 ≤ 2**(furthermore / moreover / additionally)
3. **`It is X that Y` 句式控制在每段 1 个以内**
4. **避免连续 3 句都用 SVO**
5. **`with respect to / in terms of` 全文累计 ≤ 3 次**
6. **`extensive / significantly / state-of-the-art` 全文累计 ≤ 5 次**

---

请贴你需要去 AI 化的段落。
```

---

## 🔬 真实"AI 味"案例

### Before(机翻 / GPT 直出)
```
In this paper, we propose a novel approach to address the challenging problem 
of time series forecasting. With respect to the existing methods, our approach 
demonstrates significant improvements. It can be seen that our model achieves 
state-of-the-art performance on multiple benchmark datasets. Furthermore, our 
approach is simple yet effective, and it can be considered as a strong baseline 
for future research. Moreover, extensive experiments demonstrate the 
effectiveness of our method.
```

🚩 **8 处 AI 味**:`In this paper, we propose` / `novel` / `challenging` / `With respect to` / `It can be seen that` / `state-of-the-art` / `Furthermore` / `Moreover` / `extensive experiments demonstrate` / `simple yet effective`。

### After(改写)
```
Time-series forecasting remains difficult on benchmarks with high regime 
volatility. We address this with a graph-attention model that captures 
cross-asset structure missed by purely temporal architectures. On three 
standard benchmarks, the model achieves the best results among 14 baselines 
while using one to two orders of magnitude fewer parameters.
```

✅ **改了什么**:
1. 删 "In this paper, we propose"
2. 删 "novel" "challenging"(reviewer 评价词)
3. 删 "with respect to" "Furthermore" "Moreover"
4. 删 "It can be seen that"
5. 删 "extensive experiments demonstrate" → 直接给具体 baselines 数
6. 删 "simple yet effective"
7. 删 "state-of-the-art" → 直接给具体 metric

**结果**:从 76 词 → 58 词,**信息密度 +30%**,**AI 味降到 0**。

---

## 🎯 高频 AI 短语 → 自然替换表

| AI 味 | 自然替换 |
|---|---|
| `In this paper, we propose` | 直接讲核心 |
| `It is widely recognized that` | 给个 cite |
| `numerous studies have shown` | "Prior work [cite] shows..." |
| `with respect to / in terms of` | 重组句子,通常可删 |
| `It can be seen that / It is observed that` | "We observe..." / 直接讲 |
| `play a critical/important role` | "is critical for" / "drives" |
| `As shown by experiment` | "Our experiments show" |
| `furthermore / moreover / additionally` | 用句子结构表达递进 |
| `extensive experiments demonstrate` | "Experiments on X datasets show..." |
| `state-of-the-art performance` | 具体数字 |
| `simple yet effective` | 具体证明 simple(参数数)+ 删 effective |
| `to the best of our knowledge` | 删或改 "We are not aware of prior work that..." |
| `as we will see in §X` | 给数字 / 删 |
| `It is worth noting that` | 删 |
| `In other words / That is to say` | 删第二句,重写第一句 |
| `more better / more easier` | 比较级语法错,改 better / easier |
| `the both` | both |
| `Despite the fact that` | Although / Despite |

---

## 💡 怎么自检 AI 味

1. **读出声** — AI 味的文本读起来**机械**,native English 有节奏
2. **看连接词密度** — 1 段 3 个 `furthermore / moreover` 必有 AI 味
3. **看长度** — AI 写的句子常常**比 native 长** + 信息密度低
4. **找模板** — `In this paper, we propose` / `extensive experiments` / `simple yet effective` 一出现就拉警报
