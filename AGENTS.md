# Agent Context Kernel Guide

`AGENTS.md` is this repository's compact context entry. It routes each task to the narrowest durable owner.

## Primary Routes

| Concern | Primary owner |
|---|---|
| Four kernel principles | `skills/project-context-bootstrap/references/kernel-principles.md` |
| Mandatory bootstrap outputs | `skills/project-context-bootstrap/references/bootstrap-contract.md` |
| Bootstrap and repair method | `skills/project-context-bootstrap/SKILL.md` |
| Repository context evolution method | `.agents/skills/evolve-project-context/SKILL.md` |
| Installation behavior | `scripts/install.py` |
| User workflows | `docs/usage.md` |
| Public orientation | `README.md` |
| Context and installer regression evidence | `tests/` |
| Process history | Git history |

## Execution Gates

1. Use `.agents/skills/evolve-project-context/SKILL.md` for every repository context-system change.
2. Read the principle owner, output contract, and affected procedural or public owner before editing.
3. Change principle semantics in `kernel-principles.md`, then align dependent procedure, routes, and evidence in the same change.
4. Change required-output semantics in `bootstrap-contract.md`, then align the bootstrap skill, public guidance, and regression evidence.
5. Keep installer logic in `scripts/install.py`; shell and PowerShell entrypoints route arguments to that owner.
6. Keep routes navigational, canonical owners complete, and shared guidance directed toward intended states and responsibilities.
7. Preserve a compact repository entry and a self-contained installable skill.
8. Run `python -m unittest discover -s tests` after context or installer changes.

## Task Route

1. Identify the semantic owner from the table.
2. Inspect direct evidence required to verify current state.
3. Apply all four principles through the affected owner.
4. Update dependent routes and tests together.
5. Validate the complete repository contract.
