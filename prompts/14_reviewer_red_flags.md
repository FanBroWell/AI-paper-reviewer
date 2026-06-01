# 14 · 顶会 Reviewer 红旗速查表

> **使用场景**:你写完一段不确定 reviewer 会不会挑刺,**Cmd+F 搜本表**找类似词。
> 
> 本表收录顶会 reviewer **真实会挑的红旗短语**,按危险度排。可直接 `Cmd+F` 搜。

---

## 🔴 Critical 级红旗(看见必改)

### 1. `we are the first to ...`
**为什么危险**:reviewer 第一反应是 google 找反例。任何相关领域 paper 都可能戳破。
**修复**:`We recast ... as ...` / `We revisit ... through ... lens` / `To our knowledge, no prior work has systematically investigated ...`

### 2. `Obviously / Clearly / Easy to see / It is trivial that`
**为什么危险**:暗示 "我没写证明因为不需要"。如果真 obvious,**就不需要说**;如果不 obvious,**这词就是 lazy**。
**修复**:删掉,直接陈述事实;或补完整论证。

### 3. `Significantly outperforms` 但无 p-value
**为什么危险**:`significant` 是统计术语,**没 p-value 就是 abuse 术语**。
**修复**:
- 有 std → `outperforms by X% (p < 0.05, paired t-test)`
- 没 std → `consistently outperforms` 或 `achieves higher`

### 4. `State-of-the-art` 没比 latest baselines
**为什么危险**:reviewer 会问"你比的是 2 年前的 SOTA?"
**修复**:列出对比的 baseline 时间,**包含最近 6 个月**的工作。

### 5. `Novel` 自评
**为什么危险**:`novel` 是 reviewer 评价你,**不是你自评**。自称 novel 显得不自信。
**修复**:删 `novel`,描述具体差异:"Unlike X, we ..."

### 6. `mathematical theory` / `redefine the field`
**为什么危险**:言过其实,**对应不上 paper 体量**。
**修复**:`framework` / `formulation` / `methodology`(降一档)

### 7. `world's largest by volume` / `world-class`
**为什么危险**:marketing puffery。reviewer 反感。
**修复**:**删整个从句**,数字说话(`with X assets / Y samples`)

### 8. `we sincerely hope to inspire enthusiasm`
**为什么危险**:励志演讲 tone,**不是学术 tone**。
**修复**:`We hope these findings motivate further investigation of ...`

### 9. 自引用第一人称 `our previous work`(双盲)
**为什么危险**:双盲投稿里**直接破匿名**。
**修复**:`Prior work [X] showed ...`(第三人称)

### 10. `Our model achieves the best performance`(无数字)
**为什么危险**:"the best" 是 claim,**必须有数字证据**。
**修复**:`achieves XX (+Y% over the strongest baseline)`

---

## 🟠 Major 级红旗(强烈建议改)

### 11. `no matter how complex / regardless of architecture`
**为什么**:dismissive 措辞,**贬低 baseline 作者**(他们可能是你 reviewer)。
**修复**:`across architectures` / `even highly expressive models`

### 12. `It is widely known / It is well-established that` 无 cite
**为什么**:"广为人知" 但没 citation = 你假定但没证据。
**修复**:加 1-2 个 representative cite,或删整句。

### 13. `Extensive experiments demonstrate`
**为什么**:`extensive` 是空话,**reviewer 想看具体多少**。
**修复**:`Experiments across N datasets and M baselines show ...`

### 14. `simple yet effective` / `easy to implement`
**为什么**:**陈词滥调**,每篇 paper 都说自己 simple。
**修复**:用具体数字证明 simple(`a 60K-parameter model`)+ 删掉 effective(让数字说话)

### 15. `intuitive / natural choice`
**为什么**:暗示"我不需要解释为什么这样设计"。
**修复**:用 ablation 证明 design choice 合理。

### 16. `as we will see in §X`
**为什么**:**前向引用滥用**,reviewer 翻 paper 累。
**修复**:能给数字就给数字;实在不行用 `(see §X for details)` 简化。

### 17. `Empirical / Theoretical results show`(模糊)
**为什么**:results 永远 show 东西,问题是 show 什么。
**修复**:`Empirically, we observe X. Theoretically, Y holds under Z.`

### 18. `with little to no overhead`
**为什么**:vague hedge。reviewer 想知道 overhead 多少。
**修复**:`adds <5% inference time` 或类似具体数字。

### 19. `the proposed method`(自指)
**为什么**:论文里用 4 次以上就显得机翻。
**修复**:**用模型名**(`BERT` / `ResNet` 等)替代,或用 `our framework`。

### 20. `superior performance` / `remarkable improvement`
**为什么**:形容词代替数字 = puffery。
**修复**:数字。

---

## 🟡 Minor 红旗(看时间改)

### 21. `In this paper, we ...` 开头(intro 第一句)
**为什么**:模板腔。**直接讲 problem** 更专业。
**修复**:删 `In this paper`,直接开始。

### 22. `It is worth noting that`
**为什么**:填充语,**任何句子都"worth noting"**。
**修复**:删整短语,直接讲。

### 23. `In other words` / `That is to say`
**为什么**:你已经说过一遍,**再说一遍说明第一遍没说清**。
**修复**:重写第一遍,删第二遍。

### 24. 过度使用 `furthermore / moreover / additionally`
**为什么**:连接词堆砌。
**修复**:**控制每段最多 1 个**,用句子结构表达递进。

### 25. `outperforms baselines on most metrics`
**为什么**:"most" 暗示"有些没赢"— reviewer 立刻问"哪些没赢?"
**修复**:列具体哪些赢哪些没赢,**承认不足反而加分**。

### 26. `For each / For all` 全称量词无证据
**为什么**:全称是强 claim,reviewer 会找反例。
**修复**:`In most cases` / `Across the X experiments we ran`

### 27. `As shown in Figure X`(空 ref)
**为什么**:只 ref 不解读 = figure 浪费。
**修复**:`Figure X shows that [具体 finding]`

### 28. `Notably / Interestingly / Surprisingly`
**为什么**:你 inject 情绪,**reviewer 想自己 judge**。
**修复**:删情绪词,让数据说话。

### 29. em-dash 不一致(`—` `--` `---`)
**为什么**:Unicode em-dash / 双连字符 / 三连字符在不同 LaTeX 编译器渲染不同。
**修复**:**全文统一 `---`**(LaTeX 标准 em-dash)。

### 30. `the model` / `our network`(指代不清)
**为什么**:论文里 3 个 model 都叫 "the model" reviewer 晕。
**修复**:每次明确用 **模型名**。

---

## 📋 双盲专属红旗(投稿前必查)

### D1. Personal GitHub link
任何 `github.com/真名` → critical

### D2. `Acknowledgments` 段未 placeholder
→ critical(暴露 funding source / advisor)

### D3. PDF Author 字段
`pdfinfo paper.pdf` 看 Author 是否清空

### D4. LaTeX 注释含 `% yourname's note`
→ critical(source 给 reviewer 看)

### D5. Figure metadata 含真名
Photoshop / Affinity 默认写 metadata,需手动清

### D6. 引用集中在某 PI 的 lab(>30%)
间接暴露 advisor

---

## 🌍 文化 / 语言红旗(中文母语者常踩)

### L1. `Despite the fact that`
冗余,改 `Although` 或 `Despite`(动名词搭配)。

### L2. `the both`
中式英语,直接 `both`。

### L3. `more better` / `more easier`
形容词比较级误用。

### L4. `In the meanwhile`
英语里是 `In the meantime` 或 `Meanwhile`。

### L5. 中文标点残留:`,` `。` `;` `:`
全部改英文半角。

### L6. 双语并置:`性能 (performance)`
立即 critical(中文母语指纹)。

### L7. `we propose to xxx the yyy`
中式英语,英语习惯 `we propose xxx-ing the yyy` 或 `we propose to xxx yyy`。

### L8. 过度 `the`(中文母语者常加多)
英语很多 abstract noun **不加 the**:
- ❌ `the image classification` → ✅ `image classification`
- ❌ `the deep learning` → ✅ `deep learning`

### L9. 漏 `the`(另一种中文母语者常犯)
单数可数 noun 第二次提到必须加 `the`:
- ❌ `We propose model M. Model achieves ...` → ✅ `... The model achieves ...`

### L10. 时态混乱
- 描述方法:**现在时**(`We use ...`)
- 描述实验:**过去时**(`We trained for 100 epochs`)
- 描述结果:**现在时 / 过去时**都行,但**段内一致**

---

## 📊 红旗严重度分布(给个直观感)

```
🔴 Critical (10):    ←──── reviewer 看见就扣分 / 拒稿
🟠 Major (10):       ←──── reviewer 写在 minor weaknesses
🟡 Minor (10):       ←──── reviewer 偶尔提
🛡️ 双盲 (6):         ←──── 投稿前必查
🌍 语言 (10):        ←──── 中文母语者高频踩坑
                     ━━━━
                     46 项红旗
```

---

## 💡 如何用这份速查表

1. **写完一段** → `Cmd+F` 搜本文件,看看你的措辞撞了哪些红旗
2. **改稿前** → 先看 🔴 Critical 10 条,确认无命中
3. **投稿前 24h** → 扫 🛡️ 双盲 6 项
4. **rebuttal 时** → 看 reviewer 提了哪些 minor,对照本表,**他们提的红旗你下次别再犯**

---

## 🤝 贡献

发现新红旗?**PR 加进来**。每个红旗格式:
```
### N. `具体短语`
为什么危险:...
修复:...
```

---

## 📚 参考

本表整合自:
- ICML / ICLR / NeurIPS / CIKM / KDD reviewer 公开 review template 的 anti-pattern
- 多年顶会作者总结的"低级错误"
- Strunk & White《英语写作要素》
- 作者本人真实投稿 + rebuttal 经验
