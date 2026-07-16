# Issue tracker: Local Markdown

Specs and tickets for this repo live as markdown files under the configured agent root.

_Replace `{agentRoot}` below with the actual agent root chosen by `/setup-skills`._

## Conventions

- One feature per directory: `{agentRoot}/work/<feature-slug>/`
- The spec is `{agentRoot}/work/<feature-slug>/SPEC.md`
- Implementation tickets are `{agentRoot}/work/<feature-slug>/tickets/<NN>-<slug>.md`, numbered from `01`
- Triage state is recorded as a `Status:` line near the top of each ticket file (see `triage-labels.md` for the role strings)
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `{agentRoot}/work/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path. The user will normally pass the path or the issue number directly.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a file with one child file per ticket.

- **Map**: `{agentRoot}/wayfinding/<effort>/map.md` — the Notes / Decisions-so-far / Fog body.
- **Child ticket**: `{agentRoot}/wayfinding/<effort>/tickets/NN-<slug>.md`, numbered from `01`, with the question in the body. A `Type:` line records the ticket type (`research`/`prototype`/`grilling`/`task`); a `Status:` line records `open`/`claimed`/`resolved`.
- **Blocking**: a `Blocked by: NN-<slug>.md, NN-<slug>.md` line near the top. A ticket is unblocked when every file it lists is `resolved`.
- **Frontier**: scan `{agentRoot}/wayfinding/<effort>/tickets/` for files that are open, unblocked, and unclaimed; first by number wins.
- **Claim**: set `Status: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Status: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`.
