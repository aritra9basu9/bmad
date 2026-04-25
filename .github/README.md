# Agent and Skill Hub

This folder provides a stable, repo-local structure to reference agents and skills while working on this project.

## Layout

- `agents/` : Agent profiles and usage contracts
- `skills/` : Reusable skill prompts/playbooks for delivery stages

## Recommended usage pattern

1. Pick an agent from `agents/agent-index.yaml`.
2. Select one or more skills from `skills/skill-index.yaml`.
3. Run work in this order:
   - analysis/planning skills
   - implementation skills
   - quality and maintenance skills

## Source of truth

These files are project-level wrappers. BMAD runtime skills continue to live in:

- `.cursor/skills/`
- `_bmad/`

Use this `.github` hub as your quick-reference and orchestration layer.
