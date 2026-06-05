# Case 03 · Council-5 General Review

This example shows how Council-5 can be used beyond paper polishing. The same protocol can review a research idea, product pitch, code design, or public argument.

## Input

```text
We will build an AI tool that automatically reviews any research paper and tells the author exactly how to improve it. It will help users avoid rejection by detecting all issues before submission.
```

## Council-5 Output

### Seat 1: The Adversary

The phrase "automatically reviews any research paper" is too broad. "Exactly how to improve it" and "detecting all issues" are overclaims. A reviewer or user can easily disprove them with one missed issue. The value proposition is useful, but the wording sounds like marketing rather than a credible product claim.

### Seat 2: The First-Principles Seat

The claim depends on several assumptions: that paper quality can be reliably evaluated from text alone, that all venues share similar standards, and that "avoid rejection" is a controllable outcome. These assumptions do not hold universally. The stronger and more defensible claim is that the tool helps authors catch common, review-visible issues before submission.

### Seat 3: The Builder

The idea would be stronger if it specified the review modes: claim checking, citation checking, reproducibility, double-blind compliance, and rebuttal risk. A short example would also make the product easier to understand. If resources allow, include before/after cases to show concrete value.

### Seat 4: The Outsider

"Review any research paper" is easy to understand, but "exactly how to improve it" creates unrealistic expectations. The user needs to know whether this is a grammar tool, a reviewer simulator, or a structured checklist. The pitch should say what the tool checks and what it does not promise.

### Seat 5: The Operator

The phrase "detecting all issues" is operationally impossible to verify. A practical system can detect categories of risks, not all possible flaws. The product should define inputs, outputs, and limits: paste a section, receive prioritized issues and a revision.

## Chair Decision

Seats 1, 2, and 5 identify the same hard problem: the pitch overclaims. Seat 3's suggestion to list review modes is useful and low-cost, so it should be adopted. Seat 4 is correct that the product category needs to be clearer. The claim about avoiding rejection should be softened because rejection depends on novelty, experiments, fit, and reviewer judgment.

## Priority List

### P0

- Replace "any research paper", "exactly", "avoid rejection", and "all issues" with bounded claims.

### P1

- Explain the concrete review modes so users understand what the product does.
- Add a clear output promise: prioritized issues and directly usable revisions.

### P2

- Add a short before/after example if this appears in a README or landing page.

## Directly Usable Revision

```text
We are building an AI paper review protocol that helps authors catch common reviewer-visible issues before submission. It audits claims, citations, experiments, reproducibility, double-blind compliance, and rebuttal risks, then returns prioritized P0/P1/P2 comments with directly usable revisions.
```

## Rejected or Deferred Suggestions

- Do not claim the tool can prevent rejection.
- Do not claim it can detect all issues.
- Defer benchmark-style evaluation until the core protocol and examples are clear.

