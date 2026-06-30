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
`git-workflow`, and `project-setup` are for organization only. They flatten to one
directory per skill name on install.
