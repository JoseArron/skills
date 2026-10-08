# Third-party content

This repo is MIT licensed (see [LICENSE](LICENSE)). The skills below are copied or
adapted from [mattpocock/skills](https://github.com/mattpocock/skills), also MIT
licensed:

> MIT License — Copyright (c) 2026 Matt Pocock

## Copied or adapted from mattpocock/skills v1.2.3 (`6acc160`)

- `skills/requirements-and-planning/domain-modeling/` ← `skills/engineering/domain-modeling/`
- `skills/requirements-and-planning/grill-me/` ← `skills/productivity/grill-me/`
- `skills/requirements-and-planning/grill-with-docs/` ← `skills/engineering/grill-with-docs/` — adapted to allow model invocation.
- `skills/requirements-and-planning/grilling/` ← `skills/productivity/grilling/`
- `skills/requirements-and-planning/prototype/` ← `skills/engineering/prototype/`
- `skills/requirements-and-planning/research/` ← `skills/engineering/research/` — adapted to save notes under the configured agent root.
- `skills/requirements-and-planning/to-questionnaire/` ← `skills/productivity/to-questionnaire/` — adapted to save questionnaires under the configured agent root.
- `skills/requirements-and-planning/to-spec/` ← `skills/engineering/to-spec/`
- `skills/requirements-and-planning/to-tickets/` ← `skills/engineering/to-tickets/`
- `skills/requirements-and-planning/triage/` ← `skills/engineering/triage/`
- `skills/requirements-and-planning/wayfinder/` ← `skills/engineering/wayfinder/` — adapted to default to local markdown maps under the configured agent root, and to allow model invocation.
- `skills/agent-workflow/handoff/` ← `skills/productivity/handoff/` — adapted to allow model invocation.
- `skills/productivity/teach/` ← `skills/productivity/teach/`
- `skills/productivity/wait-what/` ← `skills/productivity/wait-what/` — adapted to resolve `CONTEXT.md` through the configured agent root.
- `skills/working-with-skills/writing-for-agents/` ← `skills/productivity/writing-for-agents/` — follows the upstream rename from `writing-great-skills`.
- `skills/build-and-debug/codebase-design/` ← `skills/engineering/codebase-design/`
- `skills/build-and-debug/diagnosing-bugs/` ← `skills/engineering/diagnosing-bugs/`
- `skills/build-and-debug/implement/` ← `skills/engineering/implement/` — adapted to run local `/prune-cruft` and `/audit-implementation` gates before `/code-review`.
- `skills/review-and-refactor/code-review/` ← `skills/engineering/code-review/`
- `skills/review-and-refactor/improve-codebase-architecture/` ← `skills/engineering/improve-codebase-architecture/`
- `skills/build-and-debug/tdd/` ← `skills/engineering/tdd/`
- `skills/build-and-debug/wizard/` ← `skills/engineering/wizard/` — adapted to save one-run wizards under the configured agent root and document Git Bash/WSL use on Windows.
- `skills/git-workflow/git-guardrails-claude-code/` ← `skills/misc/git-guardrails-claude-code/`
- `skills/git-workflow/resolving-merge-conflicts/` ← `skills/engineering/resolving-merge-conflicts/`
- `skills/project-setup/setup-pre-commit/` ← `skills/misc/setup-pre-commit/`

## Local adaptations

- `skills/project-setup/setup-skills/` ← `skills/engineering/setup-matt-pocock-skills/` — renamed and
  de-personalized; preserves the configurable agent root and user-doc setup. Supporting
  reference docs (`domain.md`, `issue-tracker-*.md`, `triage-labels.md`) keep the local
  `setup-skills` command name.
- Every mapped skill includes upstream Codex UI metadata under `agents/openai.yaml`; the
  setup skill's display name is adapted to `Setup Skills`.
