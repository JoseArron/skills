# Third-party content

This repo is MIT licensed (see [LICENSE](LICENSE)). The skills below are copied or
adapted from [mattpocock/skills](https://github.com/mattpocock/skills), also MIT
licensed:

> MIT License: Copyright (c) 2026 Matt Pocock

## Copied or adapted from mattpocock/skills v1.3.1 (`24fe0ef`)

Synced from the recorded v1.2.3 baseline (`6acc160`) to v1.3.1. Unreleased
changes on upstream `main`, including experimental `chief-of-staff`, are outside
this sync.

- `skills/requirements-and-planning/domain-modeling/` ← `skills/engineering/domain-modeling/`
- `skills/requirements-and-planning/grill-me/` ← `skills/productivity/grill-me/`
- `skills/requirements-and-planning/grill-with-docs/` ← `skills/engineering/grill-with-docs/`: adapted to allow model invocation.
- `skills/requirements-and-planning/grilling/` ← `skills/productivity/grilling/`
- `skills/requirements-and-planning/prototype/` ← `skills/engineering/prototype/`
- `skills/requirements-and-planning/research/` ← `skills/engineering/research/`: adapted to save notes under the configured agent root.
- `skills/requirements-and-planning/to-questionnaire/` ← `skills/productivity/to-questionnaire/`: adapted to save questionnaires under the configured agent root.
- `skills/requirements-and-planning/to-spec/` ← `skills/engineering/to-spec/`
- `skills/requirements-and-planning/to-tickets/` ← `skills/engineering/to-tickets/`
- `skills/requirements-and-planning/triage/` ← `skills/engineering/triage/`
- `skills/requirements-and-planning/wayfinder/` ← `skills/engineering/wayfinder/`: adapted to default to local Markdown maps under the configured agent root, and to allow model invocation.
- `skills/agent-workflow/handoff/` ← `skills/productivity/handoff/`: adapted to allow model invocation.
- `skills/agent-workflow/retro/` ← `skills/engineering/retro/`: evidence-backed recommendations, scoped edits, optional reports under the configured agent root.
- `skills/agent-workflow/choose-skill/` ← `skills/engineering/ask-matt/`: deliberate de-personalized rename; routes local engineering, UX, security, creative, and artifact capabilities.
- `skills/productivity/teach/` ← `skills/productivity/teach/`
- `skills/productivity/wait-what/` ← `skills/productivity/wait-what/`: resolves `GLOSSARY.md` and `GLOSSARY-MAP.md` through the configured agent root.
- `skills/working-with-skills/writing-for-agents/` ← `skills/productivity/writing-for-agents/`: follows the upstream rename from `writing-great-skills`; invocation guidance accounts for Codex metadata and available skill-loading mechanisms.
- `skills/build-and-debug/codebase-design/` ← `skills/engineering/codebase-design/`
- `skills/build-and-debug/diagnosing-bugs/` ← `skills/engineering/diagnosing-bugs/`
- `skills/build-and-debug/implement/` ← `skills/engineering/implement/`: preserves focused `prune-cruft` and `audit-implementation` gates before `code-review`.
- `skills/build-and-debug/implement-spec/` ← `skills/engineering/implement-spec/`: uses local tracker/root conventions, bounded internal subagents, separate worktrees, serialized integration, preserved dirty work, agreed test seams, focused reviews, and evidence-backed completion.
- `skills/review-and-refactor/code-review/` ← `skills/engineering/code-review/`
- `skills/review-and-refactor/improve-codebase-architecture/` ← `skills/engineering/improve-codebase-architecture/`
- `skills/build-and-debug/tdd/` ← `skills/engineering/tdd/`
- `skills/build-and-debug/wizard/` ← `skills/engineering/wizard/`: saves one-run wizards under the configured agent root and documents Git Bash/WSL use on Windows.
- `skills/git-workflow/git-guardrails-claude-code/` ← `skills/misc/git-guardrails-claude-code/`
- `skills/git-workflow/pr/` ← `skills/engineering/pr/`: concrete problem and behavior first; optional useful visuals; observed validation and proportionate rollback risk.
- `skills/project-setup/setup-pre-commit/` ← `skills/misc/setup-pre-commit/`

## Local adaptations

- `skills/project-setup/setup-skills/` ← `skills/engineering/setup-matt-pocock-skills/`: renamed and
  de-personalized; preserves the configurable agent root and user-doc setup. Supporting
  reference docs (`domain.md`, `issue-tracker-*.md`, `triage-labels.md`) keep the local
  `setup-skills` command name.
- Every mapped skill includes upstream Codex UI metadata under `agents/openai.yaml`; the
  setup skill's display name is adapted to `Setup Skills`.
- Domain documentation uses `GLOSSARY.md` and `GLOSSARY-MAP.md`; the domain-modeling
  supporting format is `GLOSSARY-FORMAT.md`. Project-specific agent roots remain
  configurable. This repository update changes skill conventions, not files in
  other project checkouts.
- Skill dependencies load through the harness's mechanism, with direct entrypoint
  reads when it has no Skill tool. Existing local invocation choices are retained.
- The local Markdown tracker documents implementation claims and completion with
  integrated commits and acceptance evidence for `implement-spec`.

## Additional credit for pr

Upstream `pr` adapts a visual-summary menu from Dex Horthy / Humanlayer's
[`show-me`](https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md).
Its metadata and [CREDITS.md](skills/git-workflow/pr/CREDITS.md) retain that credit.
The local skill paraphrases the menu rather than importing the separate skill.

## Retired upstream content

`resolving-merge-conflicts` was removed upstream in v1.3.1 and retired locally with
the user's approval. Merge and rebase conflict work uses the agent's normal Git
workflow; no replacement skill is introduced.

## Original creative suite

`skills/creative/` is authored for this repository from the user's supplied
workflows and read-only inspection of their project artifacts. It is not an
upstream skill import. The [research note](docs/agents/research/creative-workflows.md)
records the local evidence and its limits. Project artwork, fonts, audio, and
external reference images are not copied into this repository.
