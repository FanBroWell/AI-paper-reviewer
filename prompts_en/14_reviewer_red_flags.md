# 14 - Top-Conference Reviewer Red Flags

> **Use case:** After drafting a paragraph, search this file for phrases that reviewers often challenge.
>
> This quick reference lists common red-flag phrases by severity and provides safer alternatives.

---

## Critical Red Flags

### 1. `we are the first to ...`

**Why risky:** Reviewers immediately look for counterexamples. One related
paper can invalidate the claim.

**Fix:** Use `We recast ... as ...`, `We revisit ... through ...`, or
`To our knowledge, no prior work has systematically investigated ...`.

### 2. `Obviously / Clearly / Easy to see / It is trivial that`

**Why risky:** It suggests the proof is missing because the author thinks it is
unnecessary. If it is obvious, the word is not needed. If it is not obvious, the
word is lazy.

**Fix:** Delete the phrase or provide the argument.

### 3. `Significantly outperforms` without a p-value

**Why risky:** `Significant` is a statistical term. Without statistical support,
it looks like terminology abuse.

**Fix:**
- With statistics: `outperforms by X% (p < 0.05, paired t-test)`
- Without statistics: `consistently outperforms` or `achieves higher`

### 4. `State-of-the-art` without recent baselines

**Why risky:** Reviewers will ask whether the baselines are outdated.

**Fix:** State the baseline set and include recent work where possible.

### 5. Self-assessed `novel`

**Why risky:** Novelty is for reviewers to judge. Self-labeling can sound weak.

**Fix:** Delete `novel` and explain the concrete difference from prior work.

### 6. `mathematical theory` / `redefine the field`

**Why risky:** These phrases usually overclaim relative to the paper's actual
scope.

**Fix:** Use `framework`, `formulation`, or `methodology` when accurate.

### 7. `world's largest by volume` / `world-class`

**Why risky:** Marketing language creates reviewer distrust.

**Fix:** Remove the phrase and report concrete numbers instead.

### 8. `we sincerely hope to inspire enthusiasm`

**Why risky:** This sounds like a motivational speech, not an academic paper.

**Fix:** Use `These findings motivate further investigation of ...`.

### 9. First-person self-citation in double-blind review

**Why risky:** `our previous work` breaks anonymity.

**Fix:** Use `Prior work [X] showed ...`.

### 10. `Our model achieves the best performance` without numbers

**Why risky:** `Best` is a claim that requires evidence.

**Fix:** Use `achieves XX (+Y% over the strongest baseline)`.

---

## Major Red Flags

### 11. `no matter how complex / regardless of architecture`

**Why risky:** It sounds dismissive toward baseline authors, who may be your
reviewers.

**Fix:** Use `across architectures` or `even for highly expressive models`.

### 12. `It is widely known / It is well-established that` without citation

**Why risky:** A common-knowledge claim without citation often looks like an
unsupported assumption.

**Fix:** Add representative citations or delete the phrase.

### 13. `Extensive experiments demonstrate`

**Why risky:** `Extensive` is vague.

**Fix:** Use `Experiments across N datasets and M baselines show ...`.

### 14. `simple yet effective` / `easy to implement`

**Why risky:** These are overused cliches.

**Fix:** Prove simplicity with numbers, e.g. parameter count, then let results
show effectiveness.

### 15. `intuitive / natural choice`

**Why risky:** It can imply the design needs no justification.

**Fix:** Use ablation evidence or a concrete design rationale.

### 16. `as we will see in Sec. X`

**Why risky:** Overused forward references make the paper harder to read.

**Fix:** Give the core number immediately, or use a short parenthetical
reference only when needed.

### 17. `Empirical / Theoretical results show`

**Why risky:** It is vague; results always show something.

**Fix:** Say what is shown: `Empirically, we observe X. Theoretically, Y holds
under Z.`

### 18. `with little to no overhead`

**Why risky:** Vague overhead claims invite reviewer questions.

**Fix:** Report a number, e.g. `adds less than 5% inference time`.

### 19. Repeated `the proposed method`

**Why risky:** Repetition sounds translated or template-like.

**Fix:** Use the model name or `our framework` sparingly.

### 20. `superior performance` / `remarkable improvement`

**Why risky:** Adjectives are replacing numbers.

**Fix:** Report metrics directly.

---

## Minor Red Flags

### 21. `In this paper, we ...` as the first sentence

**Why risky:** Template tone. Start with the problem instead.

### 22. `It is worth noting that`

**Why risky:** Usually filler.

**Fix:** Delete the phrase and state the point directly.

### 23. `In other words` / `That is to say`

**Why risky:** Often means the first version was unclear.

**Fix:** Rewrite the first sentence and delete the second.

### 24. Overuse of `furthermore / moreover / additionally`

**Why risky:** Stacked connectors feel mechanical.

**Fix:** Use at most one heavy connector per paragraph.

### 25. `outperforms baselines on most metrics`

**Why risky:** `Most` makes reviewers ask which metrics failed.

**Fix:** List wins and losses explicitly.

### 26. Universal quantifiers without evidence

**Why risky:** `For each` and `for all` are strong claims.

**Fix:** Use `in most cases` or specify the experiments.

### 27. Empty figure reference

**Why risky:** `As shown in Figure X` without interpretation wastes the figure.

**Fix:** Say what Figure X shows.

### 28. `Notably / Interestingly / Surprisingly`

**Why risky:** The author injects emotion before the reviewer judges the result.

**Fix:** Let the data speak.

### 29. Inconsistent em dash

**Why risky:** Mixing `--`, `---`, and Unicode em dash creates formatting
inconsistency.

**Fix:** In LaTeX, use `---` consistently.

### 30. Ambiguous `the model` / `our network`

**Why risky:** If several models exist, reviewers may lose track.

**Fix:** Use the model name.

---

## Double-Blind-Specific Red Flags

### D1. Personal GitHub link

Any `github.com/real-name` link is critical.

### D2. Non-placeholder acknowledgments

Funding source, advisor, or collaborators can reveal identity.

### D3. PDF Author metadata

Run `pdfinfo paper.pdf` and check the Author field.

### D4. LaTeX comments containing private notes

Source files may be visible during review or artifact evaluation.

### D5. Figure metadata

Image tools may write owner or author metadata.

### D6. Citation concentration around one PI or lab

Heavy concentration can indirectly reveal advisor or institution.

---

## Language Red Flags

### L1. `Despite the fact that`

Use `Although` or `Despite` with a noun phrase.

### L2. `the both`

Use `both`.

### L3. `more better` / `more easier`

Use `better` / `easier`.

### L4. `In the meanwhile`

Use `Meanwhile` or `In the meantime`.

### L5. Non-English punctuation residue

Replace with English punctuation.
