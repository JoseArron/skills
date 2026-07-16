---
name: setup-skills
description: Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.
disable-model-invocation: true
---

# Set up this repo for the skills

Scaffold the per-repo configuration that the engineering skills assume:

- **Issue tracker** — where issues live (GitHub by default; local markdown is also supported out of the box)
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

### 2. Present findings and ask

Summarise what's present and what's missing. Then walk the user through the decisions **one at a time** — present a section, get the user's answer, then move to the next. Don't dump them all at once.

Assume the user does not know what these terms mean. Each section starts with a short explainer (what it is, why these skills need it, what changes if they pick differently). Then show the choices and the default.

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

If — and only if — the user picked **GitHub** or **GitLab**, ask one follow-up:

> Explainer: Open-source repos often receive feature requests as pull requests, not just issues — a PR is an issue with attached code. If you turn this on, `/triage` pulls _external_ PRs into the same queue and runs them through the same labels and states as issues (collaborators' in-flight PRs are left alone). Leave it off if PRs aren't a request surface for you.

- **PRs as a request surface** — yes / no (default: no). Record the answer in `{agentRoot}/issue-tracker.md`. For local-markdown and other trackers, skip this question — there are no PRs.

**Section B — Triage label vocabulary.**

> Explainer: When the `triage` skill processes an incoming issue, it moves it through a state machine — needs evaluation, waiting on reporter, ready for an AFK agent to pick up, ready for a human, or won't fix. To do that, it needs to apply labels (or the equivalent in your issue tracker) that match strings _you've actually configured_. If your repo already uses different label names (e.g. `bug:triage` instead of `needs-triage`), map them here so the skill applies the right ones instead of creating duplicates.

The five canonical roles:

- `needs-triage` — maintainer needs to evaluate
- `needs-info` — waiting on reporter
- `ready-for-agent` — fully specified, AFK-ready (an agent can pick it up with no human context)
- `ready-for-human` — needs human implementation
- `wontfix` — will not be actioned

Default: each role's string equals its name. Ask the user if they want to override any. If their issue tracker has no existing labels, the defaults are fine.

**Section C — Domain & user docs.**

> Explainer: Some skills (`improve-codebase-architecture`, `diagnosing-bugs`, `tdd`) read a `CONTEXT.md` file to learn the project's domain language, and `docs/adr/` for past architectural decisions. A companion doc, `USER-BRIEF.md`, holds the project's personas, jobs-to-be-done, and user mental models — written by `understand-the-user`, read by `to-spec`, `ux-flows`, and `ux-review`. Both are project-wide living docs; they need to know whether the repo has one global context or multiple (e.g. a monorepo with separate frontend/backend contexts) so they look in the right place.

Confirm the layout — it governs `CONTEXT.md` and `USER-BRIEF.md` together:

- **Single-context** — one `CONTEXT.md` + `USER-BRIEF.md` + `docs/adr/` under `{agentRoot}`. Most repos are this.
- **Multi-context** — `CONTEXT-MAP.md` under `{agentRoot}` pointing to per-context `CONTEXT.md` files (typically a monorepo). `USER-BRIEF.md` stays under `{agentRoot}` unless contexts genuinely serve different users.

Both docs are created **lazily** by the skills that own them — `setup-skills` only records *where* they live. `{agentRoot}` is recorded in two places: `{agentRoot}/domain.md` (the detail), and the `## Agent skills` block's **Agent root** line in `CLAUDE.md`/`AGENTS.md` — the one fact every skill already has in context every session, so none of them need to look anything up to find `{agentRoot}` first.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `{agentRoot}/issue-tracker.md`, `{agentRoot}/triage-labels.md`, `{agentRoot}/domain.md`

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

Then write the docs files under `{agentRoot}` using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md) — GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md) — GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md) — local-markdown issue tracker
- [triage-labels.md](./triage-labels.md) — label mapping
- [domain.md](./domain.md) — domain doc consumer rules + layout

For "other" issue trackers, write `{agentRoot}/issue-tracker.md` from scratch using the user's description.

If `{agentRoot}` isn't the default `docs/agents/`, append it to `.gitignore` (create the file if it doesn't exist).

### 5. Done

Tell the user the setup is complete and which engineering skills will now read from these files. Mention they can edit `{agentRoot}/*.md` directly later — re-running this skill is only necessary if they want to switch issue trackers, relocate `{agentRoot}`, or restart from scratch.
