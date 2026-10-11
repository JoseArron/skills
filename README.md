Skills I use for my projects. Consumed by every harness through the
[`skills` CLI](https://github.com/vercel-labs/skills).

## Install

```bash
npx skills add JoseArron/skills -g
```

Installs every skill globally for all detected agents. Run `npx skills update -g`
to pull the latest.

## Structure

Skills live at `skills/<category>/<name>/SKILL.md`. The categories:
`requirements-and-planning`, `build-and-debug`, `review-and-refactor`,
`security`, `ux`, `working-with-skills`, `agent-workflow`, `productivity`,
`git-workflow`, `project-setup`, and `creative` are for organization only. They flatten to one
directory per skill name on install.

## Choose a workflow

Use `choose-skill` to find a relevant starting point. Use `implement` for a ticket
or small change, `implement-spec` for a complete spec with dependent tickets, and
`retro` to review a session's tools, checks, navigation, and instructions.

The [creative suite](docs/creative-workflows.md) covers references, art contracts,
generator prompts, code-built visuals, motion, sound, reusable assets, naming,
and music-led trailers. It reads the project's selected direction and uses only
the skills needed for the requested deliverable.
