---
name: pr
description: "Write a pull request description that explains the problem, resulting behavior, validation, and material merge risks."
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

# Write the PR description

Write for a reviewer who has not read the conversation. Follow the repository's template. Lead with the concrete problem and resulting behavior; use a trigger and before/after example when it clarifies the change. Read the relevant `GLOSSARY.md` under the configured agent root for domain terms.

Load `plain-english` and `deslop-written` through the Skill tool when available; otherwise read their `SKILL.md` files. Describe the final diff. Omit conversational history and abandoned approaches unless they explain a consequential tradeoff.

## Explain and show the change

Use the smallest amount of prose that makes the change reviewable. A simple fix often needs one or two sentences plus validation.

Add a visual when it explains ownership, order, state, or data flow more clearly than those sentences:

- Pseudocode for an algorithm or condition.
- A call tree for runtime order.
- A shallow file or component tree for responsibility.
- A small diff sketch for changed behavior within a familiar shape.
- Mermaid for interactions across components or processes.
- Before/after screenshots for a visual change, with the relevant state visible.

Place the visual beside the claim it explains. Include only the paths, calls, states, and boundaries needed to assess the change. A diagram is optional.

## Give validation evidence

Name checks actually run and their result. Show before/after output, a failing/passing behavior test, or screenshots when available and useful. Distinguish an observed result from an expected one. If a required check was skipped or blocked, state that limitation and its consequence.

Avoid claiming that a passing narrow test validates unrelated behavior. Preserve the repository's required validation section even for a small change.

## State material merge risks

Scale risk detail to the change. Explain affected users or consumers, compatibility changes, data migrations, destructive effects, or operational dependencies when they matter. For a hard-to-reverse change, name what rollback can restore and what it cannot. A routine reversible edit needs no speculative risk inventory.

Use the repository's required sections; otherwise this is enough for a change that needs headings:

```markdown
## Change

<Problem, trigger, and resulting behavior. Optional useful visual.>

## Validation

<Checks run and observed result. Material limitations.>

## Risks

<Only material risks, affected scope, and rollback limits. Omit if unnecessary.>
```

For multiline bodies, use a structured tool argument or write exact text to a temporary file and pass it with `--body-file`. Creating or publishing a PR follows the task's authorization; writing its description alone does not authorize publication.
