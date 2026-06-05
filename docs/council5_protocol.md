# Council-5 Protocol

Council-5 is a five-seat review protocol for stress-testing important work before it meets the real world.

It can be used for papers, code, product ideas, business plans, research directions, investment theses, public writing, and technical proposals. The core idea is simple: do not ask one AI for a single opinion. Convene a council, let five different seats pressure-test the same input, then let a chair consolidate the debate into priorities and an actionable revision.

## Hook

Do not ask one AI. Convene a council.

Put your idea on trial before reality does.

## Chinese hook

不要问一个 AI,开一场审议会。

在现实检验你之前,先压力测试你的想法。

## Why it exists

A single AI reviewer usually converges too quickly. It either polishes the text, agrees with the user, or gives a flat list of suggestions with no priority. Council-5 is designed to create productive disagreement. Each seat has a different failure mode to catch, and the chair prevents the result from becoming an unfiltered pile of advice.

The protocol is especially useful when the cost of being wrong is high: before submitting a paper, shipping a feature, pitching a product, publishing a claim, or committing to a research direction.

## The five seats

### Seat 1: The Adversary

Role: professional skeptic.

Operating rule: assume every claim is wrong until it survives pressure.

Focus:

- grammar errors
- repetition
- contradictions
- unsupported or inflated claims
- vague AI-style wording
- reviewer-visible surface flaws

Typical questions:

- What would a hostile reviewer attack first?
- Which sentence sounds stronger than the evidence allows?
- Where is the wording repetitive, empty, or too polished to be trusted?

Value: catches visible problems fastest.

### Seat 2: The First-Principles Seat

Role: reductionist thinker.

Operating rule: strip every statement down to its assumptions and ask whether the claim still follows.

Focus:

- hidden assumptions
- causal leaps
- weak definitions
- internal consistency
- whether the core argument actually distinguishes itself from alternatives

Typical questions:

- What must be true for this argument to work?
- Does the evidence imply the claim, or only correlate with it?
- If the criticism also applies to the author's own method, what is the real difference?

Value: catches deep logic problems that surface-level editing misses.

### Seat 3: The Builder

Role: expansionist strategist.

Operating rule: assume the work could become stronger with more evidence, analysis, or scope.

Focus:

- missing experiments
- useful ablations
- additional examples
- stronger positioning
- extra user or reviewer value
- higher-upside extensions

Typical questions:

- What would make this stronger if time and resources allowed?
- Which extra analysis would most improve trust?
- What would make this more memorable, useful, or defensible?

Value: opens the option space.

Chair rule: most Builder suggestions are optional by default. They should not create scope creep unless the payoff is high and the cost is low.

### Seat 4: The Outsider

Role: intelligent non-specialist.

Operating rule: read as someone smart but not already inside the author's niche.

Focus:

- jargon
- undefined terms
- narrative jumps
- unclear motivation
- missing context
- reader accessibility

Typical questions:

- Where would an intelligent outsider get lost?
- Which term needs one sentence of explanation?
- Does the reader understand why this matters before seeing technical detail?

Value: keeps the work legible beyond the immediate expert circle.

Chair rule: not every unfamiliar term needs explanation. The chair should decide based on the target audience.

### Seat 5: The Operator

Role: execution and reproducibility reviewer.

Operating rule: ask whether the work can actually be run, verified, shipped, or used.

Focus:

- reproducibility
- implementation detail
- data and metric definitions
- runtime and hardware
- operational risks
- feasibility of the proposed plan
- whether the numbers are believable

Typical questions:

- Can this actually work in practice?
- What information is missing for someone to reproduce or execute it?
- Are the practical constraints consistent with the claim?

Value: catches the gap between a convincing story and a workable artifact.

## The chair

The Chair is the decision maker. The Chair does not average the five opinions. The Chair resolves conflicts, removes duplicates, rejects low-value expansion, and converts the debate into a prioritized action list.

Decision rules:

- The Adversary, First-Principles Seat, and Operator usually get priority when they identify hard errors.
- The Builder is useful for option discovery, but its recommendations are often downgraded unless they are low-cost and high-impact.
- The Outsider is useful for clarity, but the Chair should account for the expected reader.
- The final output must distinguish required fixes from optional improvements.

## Priority levels

### P0: Must fix

Hard errors, contradictions, misleading claims, unsupported numbers, anonymity leaks, broken reproducibility, or practical impossibility.

### P1: Strongly recommended

Claim calibration, missing reasoning, unclear positioning, weak evidence-to-claim connection, or important clarity gaps.

### P2: Optional polish

Style improvements, additional examples, deeper analysis, optional experiments, or broader extensions.

## Output format

Council-5 works best when the output is structured as:

1. Seat summaries
2. Chair decision
3. P0 / P1 / P2 priority list
4. Directly usable revision
5. Notes on rejected suggestions

This prevents the user from being trapped by contradictory reviewer comments.

## Good use cases

- Review a paper paragraph before submission
- Stress-test a research idea
- Critique a product concept
- Review a code design
- Pressure-test a business plan
- Improve a public post before publishing
- Check whether an argument survives skeptical readers

## Positioning line

Council-5 is not a polishing prompt. It is a structured disagreement protocol.

