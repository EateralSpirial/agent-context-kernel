# Agent Context Kernel

A self-bootstrapping skill for coding agents to design, validate, and evolve project-native context systems.

Agent Context Kernel starts from repository evidence. The agent chooses the document layout, truth owners, onboarding route, and task skills that fit the project. Repository files and existing validation tools provide the infrastructure, so the resulting context system remains portable and project-owned.

## Why

A strong coding agent enters an unfamiliar repository like a capable new engineer. Large-project performance depends on fast orientation, durable ownership of project truth, reliable change coordination, and context that directs attention toward the intended system.

The kernel turns those requirements into four orthogonal design questions:

| Principle | Question it answers | Canonical source |
|---|---|---|
| Onboarding | What must a capable new agent learn to exercise sound judgment? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#1-onboarding-principle) |
| Singular truth | Where does each durable project truth live? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#2-singular-truth-principle) |
| Affirmative direction | How should shared context direct agent attention? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#3-affirmative-direction-principle) |
| Change plan | When and where should intended change enter the context system? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#4-change-plan-and-context-first-principle) |

The linked file owns the complete definitions. This README provides public orientation and routing.

## What the skill builds

From the target repository, the bootstrap skill derives and creates the smallest useful combination of:

- a compact project entry for new agents;
- canonical owners for standards, contracts, plans, and evidence routes;
- project-specific task skills;
- a project-local context evolution skill;
- an explicit protocol for context-ahead, implementation-ahead, aligned, and diverged states;
- lightweight regression evidence for critical context invariants;
- a cold-start onboarding check using a fresh agent perspective.

The target project keeps its own conventions. Existing coherent structures remain in place; new structures arise only where project evidence calls for them.

## Use

1. Place [`skills/project-context-bootstrap`](skills/project-context-bootstrap/) where your coding agent discovers skills.
2. Invoke `project-context-bootstrap` inside the target repository.
3. Ask the agent to inspect the repository and build or repair its project-native context system.
4. Review the resulting owners, routes, generated skills, and validation evidence as one coordinated change.

The seed skill creates the durable project-specific system. Routine context evolution then flows through the project-local skill it establishes.

## Repository map

| Path | Ownership |
|---|---|
| [`AGENTS.md`](AGENTS.md) | entry and development route for this repository |
| [`SKILL.md`](skills/project-context-bootstrap/SKILL.md) | bootstrap and repair procedure |
| [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md) | canonical definitions of the four principles |
| [`openai.yaml`](skills/project-context-bootstrap/agents/openai.yaml) | skill interface metadata |
| [`test_context_contract.py`](tests/test_context_contract.py) | executable context invariants |

## Validation

```bash
python -m unittest discover -s tests
```

## License

MIT
