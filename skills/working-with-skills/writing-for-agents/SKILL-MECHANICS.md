# Skill mechanics

The skill-specific branch of [`writing-for-agents`](SKILL.md): what changes when the document is a skill (frontmatter, the invocation choice, and router skills). Everything else about writing it is the universal reference in `SKILL.md`.

## Invocation

Two choices, trading the two loads:

- A **model-invoked** skill is available for automatic selection and explicit user invocation. Its description is a context pointer: write the trigger branches using the pointer rules in `SKILL.md`. A reference skill can supply shared vocabulary to other skills. Mechanics: omit `disable-model-invocation`; for Codex UI metadata, omit `policy.allow_implicit_invocation` or set it to `true`.
- A **user-invoked** skill starts when the user invokes it. Its description remains required for discovery and installation; describe its outcome in one line. Mechanics: set `disable-model-invocation: true` and, when providing Codex UI metadata, set `policy.allow_implicit_invocation: false`. Whether the description consumes context depends on the harness, so do not assume an empty context cost.

Preserve an established invocation policy. For an original skill, keep automatic discovery unless the user requests explicit-only invocation. Required approval before an external mutation is separate from skill discovery. For a selectively derived skill, preserve the source's explicit-only choice unless the local contract or user changes it.

When two workflows need the same reference, put it in a model-invoked reference skill or a plain supporting file and link to its authoritative source. Keep starting an explicit-only workflow separate from reading its instructions as evidence.

Load a referenced skill through the Skill tool when the harness provides it; otherwise read its `SKILL.md` through the available file or resource tool. Naming the skill does not load its body.

## Splitting by invocation

The invocation cut of splitting (the sequence cut lives in `SKILL.md`): split off a model-invoked skill when you have a distinct leading word that should trigger it on its own (a trigger word you actually use in your prompts), or another skill must reach it. You pay context load for the new always-loaded description, so that independent reach has to be worth it.

## Router skills

When explicit-only skills become hard to remember, use a **router skill**: one entry point that recommends the relevant skills and their sequence. Recommend explicit-only workflows for the user to invoke. A router can load a model-invoked skill to perform work already authorized by the user's task; routing alone does not authorize starting unrelated workflows.
