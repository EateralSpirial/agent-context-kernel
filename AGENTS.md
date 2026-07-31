# Agent Context Kernel Guide

`AGENTS.md` is this repository's context entry. It routes each task to the narrowest durable owner and keeps repository-wide execution gates compact.

## Primary routes

| Concern | Primary owner |
|---|---|
| Four kernel principles | `skills/project-context-bootstrap/references/kernel-principles.md` |
| Bootstrap and repair method | `skills/project-context-bootstrap/SKILL.md` |
| Skill interface | `skills/project-context-bootstrap/agents/openai.yaml` |
| Public orientation | `README.md` |
| Context regression evidence | `tests/test_context_contract.py` |
| Process history | Git history |

## Execution gates

1. Read the principle owner and the affected procedural or public owner before changing repository context.
2. Change principle semantics in `kernel-principles.md` first, then align the skill, public route, and regression evidence in the same change.
3. Change bootstrap behavior in `SKILL.md`, then align interface metadata and regression evidence.
4. Keep routes navigational and let canonical owners carry complete definitions.
5. Express shared guidance through intended states, owners, conditions, actions, and effects.
6. Preserve a compact entry and a self-contained installable skill.
7. Run `python -m unittest discover -s tests` after context changes.

## Task route

1. Identify the semantic owner from the table.
2. Read direct evidence needed to verify the current state.
3. Apply the bundled principles through the affected owner.
4. Update dependent routes and tests together.
5. Validate the complete repository context contract.
