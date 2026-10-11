---
name: retro
description: "Review a coding session and suggest improvements to the agent's environment."
disable-model-invocation: true
---

# Review the session

Suggest changes that prevent recurring friction in future runs. Default to the current session; when the user names another, read its available logs, artifacts, commits, and verification results. Distinguish observed events from inference and missing evidence.

Load `writing-for-agents`, `plain-english`, and `deslop-written` through the Skill tool when available; otherwise read their `SKILL.md` files. Apply them to the report.

## Find improvements

Trace each candidate to session evidence and inspect repository configuration before proposing a fix:

- **Navigation:** time spent finding files, hidden dependencies, and missing context pointers. Prefer a precise pointer to a duplicate document.
- **Automated checks:** a mistake that a deterministic check can catch, or an unwired or broken check. Read build scripts, CI, and hooks first. An absent hook warrants a proposal when the session shows a failure it would prevent or the repository requires one.
- **Review guidance:** judgment calls the review missed, such as cross-file consistency or domain meaning. Put mechanical rules in the repository's checker; reserve review prose for decisions a checker cannot make.
- **Steering files:** duplicated instructions, instructions that do not change behavior, or large always-loaded files that could point to focused references.
- **Tool use:** repeated expensive reads, avoidable output, unavailable capabilities, or scripts whose input or output causes recurring mistakes.
- **Information access:** missing logs or read access that blocked a decision. Name the specific information and the smallest access change that would expose it.

Keep implementation facts, review facts, and environment causes separate. A reviewer still needs the spec, standards, and relevant context; a diff alone does not establish intended behavior.

## Present recommendations

Rank findings by consequence, recurrence, and evidence. Each finding names the observed event, its source, the affected behavior, the proposed change and location, and a way to verify it. Separate a confirmed cause from a plausible explanation. If the sources support no useful improvement, say so.

Recommend changes first. Apply only changes within the user's request. Editing global instructions, skills, or memory requires the corresponding explicit authorization; a retrospective alone does not provide it.

Keep the report in the conversation unless the user requests a file or the workflow needs a durable reference. For a repository report, use its configured agent root and convention, such as `{agentRoot}/retrospectives/<session-slug>.md`. If no root is configured, use an appropriate project-local path without making setup a prerequisite for the review.
