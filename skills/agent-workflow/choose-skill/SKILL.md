---
name: choose-skill
description: "Choose a skill or sequence of skills for the work you want to do."
disable-model-invocation: true
---

# Choose a skill

Recommend the smallest skill or flow that reaches the user's outcome. Use the request, repository configuration, and installed skills to distinguish a decision, evidence gathering, a creative deliverable, implementation, and review. Give the recommended starting point and why; show alternatives only when the choice matters.

Routing does not require every skill in a flow. A scoped task can start in the middle. Suggest explicit-only skills for the user to invoke; do not automatically start their workflows. When the user already authorizes work governed by a model-invoked skill, load it through the Skill tool when available or read its `SKILL.md`, then continue that work.

## Planning and implementation

| Outcome | Start here | Continue when needed |
| --- | --- | --- |
| Understand who the product serves and the evidence behind that belief | `understand-the-user` | `grill-with-docs` to settle the plan |
| Stress-test a plan and retain domain decisions | `grill-with-docs` | `domain-modeling` maintains the configured `GLOSSARY.md` and ADRs |
| Interview without durable project documents | `grill-me` or `grilling` | Use the conversation as the source |
| Gather facts before making a decision | `research` | Feed cited findings into the relevant plan or creative brief |
| Explore an effort with unresolved dependent decisions | `wayfinder` | `to-spec` once the route is clear |
| Answer a design question with a throwaway artifact | `prototype` | Feed its observed behavior into the plan |
| Turn an agreed plan into tracked work | `to-spec`, then `to-tickets` | One self-contained ticket per file or issue, with blocking relationships |
| Build a ticket or small scoped change | `implement` | Appropriate focused reviews, then `code-review` |
| Build a complete ticketed spec with parallel workers | `implement-spec` | One integration branch and final `code-review` |
| Implement behavior test-first | `tdd` | Red, green, refactor at the agreed seam |
| Diagnose a broken, failing, or slow behavior | `diagnosing-bugs` | Reproduce, isolate, fix, and verify |
| Process raw incoming requests | `triage` | Send agent-ready work to implementation |

Read the `## Agent skills` configuration for `{agentRoot}` and tracker conventions. Use `setup-skills` when configuration is needed; do not require setup for an unrelated standalone task. Locally tracked work uses the configured root rather than an assumed scratch directory.

## Creative work

Load only the skill whose deliverable the user needs. These related skills share the approved direction rather than deriving a different style for each asset.

| Outcome | Skill |
| --- | --- |
| Reference research and a sourced moodboard | `visual-research` |
| A visual identity or art direction contract | `art-direction` |
| Copyable prompts and reference instructions for image generation | `image-prompts` |
| Executable procedural 2D or 3D graphics | `procedural-art` |
| Motion rules, timing, or animation implementation | `motion-design` |
| Sound cue design or an audio-generation brief | `sound-design` |
| Consistent reusable assets with a browsable catalog | `asset-library` |
| Naming, sound-based wordplay, or cultural reference candidates | `creative-naming` |
| Music and reference research translated into a trailer plan | `trailer-direction` |

Use the installed `imagegen` skill and image-generation tool for producing or editing bitmap assets; `image-prompts` prepares prompts. Use `procedural-art` when editable code is the deliverable. Native artifact skills handle slide decks, documents, PDFs, and spreadsheets; discover their available provider rather than inventing a local substitute.

Use `sound-design` for sound cues and their generation or production brief; use `trailer-direction` for song research, trailer structure, and music-led editing.

## Design, review, and closeout

- `ux-flows` designs or implements a user flow; `make-it-obvious` simplifies a confusing screen; `ux-review` reports usability findings on a built flow.
- `codebase-design` defines a module's interface and seam; `improve-codebase-architecture` surveys candidates for deeper modules. `domain-modeling` handles terminology and architectural decisions.
- `prune-cruft` removes complexity that does not earn its keep; `audit-implementation` checks feature behavior, query shape, stack fit, and tool use; `audit-security` checks trust boundaries. `code-review` evaluates the final diff against Standards and Spec.
- `pr` writes a concise reviewable PR description. `retro` reviews the session and proposes environment improvements.
- `handoff` packages sources and decisions when work travels to another agent, workspace, or colleague. Keep relevant context in the same conversation when portability is unnecessary; use the host's context management when needed, without assuming commands or fixed token capacities.
- `to-questionnaire` gathers answers from another person; `wizard` packages setup steps only the human can perform. `teach` supports continued learning, `wait-what` re-explains a confusing message, and `zoom-out` maps surrounding context.
- `plain-english`, `deslop-written`, and `concrete-naming` govern prose and naming. `writing-for-agents` governs agent documents. `find-skills` discovers missing capabilities; `resync-upstream-skills` maintains derived skills.

End the recommendation with the concrete next action and the expected artifact. Ask only for a missing choice that changes the route.
