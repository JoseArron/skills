# Domain & User Docs

How the engineering skills should consume this repo's two project-wide living docs: `CONTEXT.md` (the domain language and decisions) and `USER-BRIEF.md` (who the system is for and what they need).

## Agent root

Agent root: `docs/agents/` — this repo's configured agent root, the same place as `issue-tracker.md` and `triage-labels.md` alongside this file.

_Replace the path above with the actual configured agent root when writing this file. Everything below is relative to it._

## Before exploring, read these

- **`CONTEXT.md`** at the agent root, or
- **`CONTEXT-MAP.md`** at the agent root if it exists — it points at one `CONTEXT.md` per context. Read each one relevant to the topic.
- **`docs/adr/`** under the agent root — read ADRs that touch the area you're about to work in. In multi-context repos, also check each context's own `docs/adr/` for context-scoped decisions.
- **`USER-BRIEF.md`** at the agent root (same single-/multi-context layout as `CONTEXT.md`) holds personas, jobs-to-be-done, mental models, and standing assumptions about the user, each tagged `[E]` evidence or `[A]` assumption. Written and maintained by `understand-the-user`; read by `to-spec`, `ux-flows`, and `ux-review`.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context repo (most repos), rooted at the path above:

```
{agentRoot}/
├── CONTEXT.md
├── USER-BRIEF.md
└── docs/adr/
    ├── 0001-event-sourced-orders.md
    └── 0002-postgres-for-write-model.md
```

Multi-context repo (presence of `CONTEXT-MAP.md`):

```
{agentRoot}/
├── CONTEXT-MAP.md
├── USER-BRIEF.md
├── docs/adr/                          ← system-wide decisions
├── ordering/
│   ├── CONTEXT.md
│   └── docs/adr/                      ← context-specific decisions
└── billing/
    ├── CONTEXT.md
    └── docs/adr/
```

When the agent root is the repo root itself, per-context dirs are the actual source dirs (`src/ordering/`, `src/billing/`) — the docs sit next to the code they describe. Otherwise (the default `docs/agents/`, or any other chosen agent root), per-context dirs are named the same as the source dirs but live under that agent root instead, since the docs no longer share a parent with the code.

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
