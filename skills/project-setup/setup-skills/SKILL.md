---
name: setup-skills
description: Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.
disable-model-invocation: true
---

# Set up this repo for the skills

Scaffold the per-repo configuration that the engineering skills assume:

- **Issue tracker** — where specs and tickets live (GitHub by default; local markdown is also supported out of the box)
- **Triage labels** — the strings used for the five canonical triage roles
- **Domain & user docs** — where `CONTEXT.md`, `USER-BRIEF.md`, and ADRs live, and the consumer rules for reading them

All three live under one **agent root**, chosen once (`docs/agents/` by default) — see Section 0 below.

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config` — is this a GitHub repo? Which one?
- `AGENTS.md` and `CLAUDE.md` at the repo root — does either exist? If both exist, you can reference `AGENTS.md` in `CLAUDE.md` with @. Is there already an `## Agent skills` section in either? If so, it states the agent root — read it from there, don't guess at a path.
- `docs/agents/` at the repo root — does it exist from a prior or partial run, even without an `## Agent skills` section yet?
- `CONTEXT.md`, `CONTEXT-MAP.md`, `USER-BRIEF.md`, `docs/adr/` — check both the repo root and any agent root found above; either may hold pre-existing docs from before this skill was used.
- `.scratch/` — sign that an older local-markdown convention is already in use; offer to move future files under the agent root
- Is the `triage` skill installed? (a `triage` skill folder alongside this one, or `triage` in your available skills.) This decides whether Section B runs at all.
- Monorepo signals — a `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, or a populated `packages/*` with its own `src/`. Present only in a genuinely large multi-package repo; their absence means single-context, which is almost every repo.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order — one section, one answer, then the next.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip the section entirely when exploration already settled it (Section B when `triage` isn't installed, Section C when there's no monorepo).

**Section 0 — Agent root.**

> Explainer: The agent root is the project-local directory where these skills write durable files: issue tracker config, local specs and tickets, maps, triage labels, and the domain & user docs (`CONTEXT.md`, `USER-BRIEF.md`, `docs/adr/`). By default that's `docs/agents/` at the repo root, committed like any other source file. Some people would rather keep it out of version control — agent-maintained working notes, not something the team reviews in a PR. If that's you, name any directory and everything below moves there instead.

- **`docs/agents/`** (default) — committed.
- **A directory you name** — any path you want (`.agents/`, `notes/`, a relocated `docs/agents/`, …). Adds it to `.gitignore` (creating the file if it doesn't exist).

Call the answer `{agentRoot}` for the rest of this skill — every file below is `{agentRoot}/<name>`.

**Section A — Issue tracker.**

> Explainer: The "issue tracker" is where tickets and specs live for this repo. Skills like `to-tickets`, `triage`, and `to-spec` read from and write to it — they need to know whether to call `gh issue create`, write markdown files under the agent root, or follow some other workflow you describe. Pick the place you actually track work for this repo.

Default posture: these skills were designed for GitHub. If a `git remote` points at GitHub, propose that. If a `git remote` points at GitLab (`gitlab.com` or a self-hosted host), propose GitLab. Otherwise (or if the user prefers), offer:

- **GitHub** — issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab** — issues live in the repo's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local markdown** — issues live as files under `{agentRoot}/work/<feature>/` in this repo (good for solo projects or repos without a remote)
- **Other** (Jira, Linear, etc.) — ask the user to describe the workflow in one paragraph; the skill will record it as freeform prose

Record the choice in `{agentRoot}/issue-tracker.md`. The GitHub and GitLab templates carry a "PRs as a request surface" flag, defaulted **off** — leave it off and don't raise it; a user who wants external PRs in the triage queue can flip the flag in the file later.

**Section B — Triage label vocabulary.** Skip this section entirely if the `triage` skill isn't installed (exploration told you) — an uninstalled skill needs no labels.

If it is installed, ask exactly one question:

> Do you want to keep the default triage labels? (recommended: **yes**)

The defaults are the five canonical roles, each label string equal to its name: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. On **yes**, write them as-is. Only if the user says no — usually because their tracker already uses other names (e.g. `bug:triage` for `needs-triage`) — collect the overrides so `triage` applies existing labels instead of creating duplicates.

**Section C — Domain & user docs.**

Default to **single-context** — one `CONTEXT.md` + `USER-BRIEF.md` + `docs/adr/` under `{agentRoot}`. This fits almost every repo; write it without asking.

Offer **multi-context** — a `{agentRoot}/CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files — only when exploration found monorepo signals. Then confirm which layout they want. `USER-BRIEF.md` stays under `{agentRoot}` unless contexts genuinely serve different users.

Both docs are created **lazily** by the skills that own them — `setup-skills` only records *where* they live. `{agentRoot}` is recorded in two places: `{agentRoot}/domain.md` (the detail), and the `## Agent skills` block's **Agent root** line in `CLAUDE.md`/`AGENTS.md` — the one fact every skill already has in context every session, so none of them need to look anything up to find `{agentRoot}` first.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `{agentRoot}/issue-tracker.md`, `{agentRoot}/domain.md`, and `{agentRoot}/triage-labels.md` (the last only when `triage` is installed)

Let them edit before writing.

### 4. Write

**Pick the file to edit:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, ask the user which one to create — don't pick for them.

Never create `AGENTS.md` when `CLAUDE.md` already exists (or vice versa) — always edit the one that's already there. This file always stays at the repo root regardless of `{agentRoot}` — it's the fixed anchor every skill reads first, which is what makes `{agentRoot}` discoverable without a lookup.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Don't overwrite user edits to the surrounding sections.

The block (substitute the literal `{agentRoot}` path, not the placeholder):

```markdown
## Agent skills

Agent root: `{agentRoot}`

### Issue tracker

[one-line summary of where issues are tracked, plus whether external PRs are a triage surface]. See `{agentRoot}/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `{agentRoot}/triage-labels.md`.

### Domain & user docs

[layout — "single-context" or "multi-context"]. See `{agentRoot}/domain.md`.
```

Include the `### Triage labels` sub-block, and write `{agentRoot}/triage-labels.md`, only when `triage` is installed and Section B ran. When it isn't, both are omitted.

Then write the docs files under `{agentRoot}` using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) — local-markdown issue tracker
- [triage-labels.md](./triage-labels.md) — label mapping (only if `triage` is installed)
- [domain.md](./domain.md) — domain doc consumer rules + layout

For "other" issue trackers, write `{agentRoot}/issue-tracker.md` from scratch using the user's description.

If `{agentRoot}` isn't the default `docs/agents/`, append it to `.gitignore` (create the file if it doesn't exist).

### 5. Done

Tell the user the setup is complete and which engineering skills will now read from these files. Mention they can edit `{agentRoot}/*.md` directly later — re-running this skill is only necessary if they want to switch issue trackers, relocate `{agentRoot}`, or restart from scratch.
