---
name: research
description: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file under the configured agent root. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent.
---

# Research

Spin up a **background agent** to do the reading so the main session can keep working.

## Task

The background agent's job:

1. Investigate the question against **primary sources**: official docs, source code, specs, first-party APIs, standards, release notes, or the repository's own files. Do not rely on secondary write-ups when a primary source exists.
2. Follow every material claim back to the source that owns it.
3. Write the findings to a single Markdown file with citations for the claims that matter.
4. Save the file under the configured agent root. Prefer `{agentRoot}/research/<slug>.md` unless the current workflow names a more specific place, such as a `/wayfinder` ticket asset.

Read the `## Agent skills` block in `AGENTS.md`/`CLAUDE.md` for `{agentRoot}`. If setup has not run yet, ask the user whether to run `/setup-skills` or pick a temporary path for this research note.

## Report Shape

Use this structure:

```md
# <Question>

## Answer

<Short answer in plain language. Say what is known, what is uncertain, and what decision this supports.>

## Findings

- <Claim> — <source link or repo path>
- <Claim> — <source link or repo path>

## Sources Checked

- <Primary source>
- <Primary source>

## Open Questions

- <Question that remains unresolved, or "None">
```

## Quality Bar

- Prefer primary sources over summaries.
- Quote sparingly; paraphrase unless exact wording matters.
- Separate fact from inference.
- Record dates for versioned or time-sensitive sources.
- If sources disagree, name the disagreement instead of smoothing it over.
- If the answer is not knowable from available primary sources, say so.

## Done

Return only:

- The answer in 3-6 bullets.
- The path of the research note.
- Any unresolved question that blocks the caller.
