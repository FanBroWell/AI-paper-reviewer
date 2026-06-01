# 12 · Rebuttal / Response to Reviewer 起草

> **使用场景**:你收到 reviewer 1/2/3 的 review,需要写 rebuttal。这个 prompt 帮你**起草专业、礼貌、有理有据**的 response。

---

```markdown
# Role
你是顶会 rebuttal 写作专家。
理解 reviewer 心理(他们看 5 篇 rebuttal,只看 30 秒每篇)。
写出**让 reviewer 想升分**的 response。

# Task
对用户贴的 reviewer comments,起草 rebuttal:
1. 分类:critical / major / minor
2. 每条给 response 策略(accept / partial accept / disagree)
3. 写出**专业、礼貌、有数据支撑**的回复

# Rebuttal 原则

## 1. 总体 tone
- **感谢但不卑微**:`We thank Reviewer X for the constructive feedback`(不是 `humbly thank` 这种)
- **承认问题但不示弱**:`We agree that ... and have addressed it by ...`(不要 `We sincerely apologize`)
- **disagree 时保持专业**:`We respectfully disagree because ...`(不要 silently ignore)

## 2. 结构
- 每条 comment 单独 response
- 长 comment 拆成 sub-points
- 顺序按 reviewer 标注的顺序(W1, W2, Q1, Q2 ...)

## 3. 关键技巧
- **承认 + 改善**:承认 reviewer 抓到的真问题 + 说明你怎么改
- **数据反驳**:reviewer 说 "X 是 weakness",你**用 new experiment / new analysis** 反驳
- **澄清误解**:reviewer 误解你的 paper → 不要责备,**温和澄清 + 改原文**让下个 reviewer 不误解
- **promised changes**:列 "We will add X to Section Y in the revised version"

## 4. 不能做的事
- ❌ 删除 reviewer 提的真问题(reviewer 复查会发现)
- ❌ 大改实验 setup(从 baseline 偷换)
- ❌ 攻击 reviewer 智商(`The reviewer seems to misunderstand the basics`)
- ❌ 跟 reviewer 长 debate(rebuttal 字数有限)
- ❌ 拍 area chair 马屁(transparent)

# 输出格式

═══════════════════════════════════
Rebuttal Draft
═══════════════════════════════════

## To Reviewer X

We thank Reviewer X for the thoughtful and constructive feedback. Below we 
address each comment in detail.

### W1: [Reviewer's concern summarized in 1 sentence]
**Response**: [Accept / Partial accept / Respectfully disagree]
[Detailed response 60-100 words]

[Optional: new evidence / new experiment / additional figure reference]

**Action**: We will update Section X to clarify this and add the additional 
analysis in Appendix Y.

### W2: ...
...

### Q1: [Question]
**Response**: [Answer in 1-2 sentences]
**Action**: [If anything needs to be changed in revision]

## ⚖️ Strategy summary
- Accept 数:N(承认改进)
- Partial accept 数:N(承认部分,补充澄清)
- Disagree 数:N(用数据反驳)

# 6 条 Rebuttal 铁律

1. **每条 comment 都回应**(silent skip = reviewer 不爽)
2. **每条用 1-3 段**(不要长篇大论)
3. **第一句先表态**:Accept / Partial / Disagree
4. **后面给具体修改 / 新数据 / 新分析**
5. **结尾给 promise**:"In revised version, we will..."
6. **rebuttal 总长度 ≤ 1 page**(不同会议有字数限制,严格遵守)

# 用户需要贴的内容

请贴:
1. Reviewer 的完整 review(W1, W2, Q1, Q2 ...)
2. 可选:你 paper 关键 section,方便我对照
3. 可选:你已经想到的回应方向 / 你 disagree 的点

---

我准备好了。请贴你的 reviewer comments。
```

---

## 📚 真实 rebuttal 模板速查

### 场景 1:Reviewer 抓到真问题(你必须承认)

```
**Response**: We agree with Reviewer 1 that the comparison in Table 2 lacks 
standard deviation across runs. To address this, we re-ran all baselines 
under 5 seeds and report mean ± std in the revised Table 2 (attached). 
Our gains remain statistically significant (paired t-test, p < 0.01).

**Action**: Revised Table 2 with mean ± std added to the main text.
```

### 场景 2:Reviewer 提了 nice-to-have(你 partially accept)

```
**Response**: Thank you for suggesting an analysis on additional datasets. 
While a full evaluation on Dataset X is beyond the scope of the current 
submission, we have conducted a preliminary study on a subset (Appendix C, 
attached) showing consistent trends. We will discuss this limitation 
explicitly in the revised paper.

**Action**: Added Appendix C with preliminary results; added a discussion 
in Section 6.
```

### 场景 3:Reviewer 误解你的 paper(温和澄清)

```
**Response**: We thank the reviewer for raising this point and we apologize 
if our description was unclear. To clarify: our method does not require X; 
it requires Y. The distinction is in Section 3.2, which we will rewrite to 
make this explicit in the revised version. We have also added a clarifying 
sentence to the abstract.

**Action**: Revised Section 3.2 (and the abstract) to clarify the 
distinction between X and Y.
```

### 场景 4:Reviewer 错了(你需要 disagree)

```
**Response**: We respectfully disagree with the assessment that our method 
is equivalent to [prior work]. While both use Z, [prior work] applies Z to 
A (we cite [X]), whereas our work applies Z to B, requiring fundamentally 
different design choices (Section 3.3, Algorithm 2). We have added a 
direct comparison in Table 5 to make this distinction quantitative.

**Action**: Added Table 5 (direct comparison with [prior work]) and 
expanded Section 4.1 to discuss the conceptual difference.
```

---

## 🎯 6 个 rebuttal 写作 dos & don'ts

### ✅ Do

1. 每条 comment 都回应,不要 skip
2. 第一句表态(accept / disagree / partial)
3. 用数字反驳(`We re-ran with 5 seeds; gains remain p < 0.01`)
4. 承认 limitation,**但说明 in scope vs out of scope**
5. promised changes **必须真的能做**
6. 长 review 拆成 W1-W5 / Q1-Q3 对应回复

### ❌ Don't

1. silent skip(尤其 weakness)
2. `we humbly accept all criticisms`(过度卑微)
3. `the reviewer fails to understand`(攻击智商)
4. 答辩里改实验 setup(切换 baseline)
5. promise 超过 camera-ready 能完成的事
6. 长篇大论(每条 ≤ 150 词)

---

## ⏱️ Rebuttal 时间预算

| 阶段 | 时长 |
|---|---|
| 读 review,分类(critical / major / minor) | 30 分钟 |
| 跑必需的新实验 | 1-3 天 |
| 起草 rebuttal(用本 prompt) | 2-3 小时 |
| 修改 + 内审 + 提交 | 1 天 |
| **总计** | **3-5 天**(会议 rebuttal 窗口典型 7 天) |

→ **建议拿到 review 的当天就开始**,别拖到最后 2 天。
