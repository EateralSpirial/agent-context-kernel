# Agent Context Kernel

A self-bootstrapping skill for coding agents to design, validate, and evolve complete project-native context systems.

Agent Context Kernel starts from repository evidence. The agent chooses the document layout, truth owners, onboarding route, standards, and task skills that fit the project. Repository files and existing validation tools provide the infrastructure, so the resulting context system remains portable and project-owned.

## Core Model

A strong coding agent enters an unfamiliar repository like a capable new engineer. Large-project performance depends on compact orientation, durable ownership of project truth, constructive attention direction, and explicit coordination between intended change and implementation.

The kernel organizes those requirements through four orthogonal principles:

| Principle | Question it answers | Canonical source |
|---|---|---|
| Onboarding | What must a capable new agent learn to exercise sound judgment? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#1-onboarding-principle) |
| Singular truth | Where does each durable project truth live? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#2-singular-truth-principle) |
| Affirmative direction | How should shared context direct agent attention? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#3-affirmative-direction-principle) |
| Change plan | When and where should intended change enter the context system? | [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md#4-change-plan-and-context-first-principle) |

The linked file owns the complete principle definitions.

## Guaranteed Bootstrap Result

Every completed bootstrap establishes the three objects defined by the [`Bootstrap Output Contract`](skills/project-context-bootstrap/references/bootstrap-contract.md):

1. a root `AGENTS.md` context entry;
2. a project-local skill library;
3. exactly one `evolve-project-context` skill as the project's context-evolution procedure owner.

Standards, plans, module contracts, risk owners, and semantic checks follow from project evidence. A `.standards/` directory is available as a useful pattern for reusable rules across several modules or task classes.

## Install

Inside Codex:

```text
$skill-installer install https://github.com/EateralSpirial/agent-context-kernel/tree/main/skills/project-context-bootstrap
```

From a clone:

```bash
sh install.sh
sh install.sh --project /path/to/project
```

```powershell
.\install.ps1
.\install.ps1 --project C:\path\to\project
```

The installer uses only Python's standard library. See [`docs/usage.md`](docs/usage.md) for installation options and prompts for early and legacy projects.

## Use

Invoke the installed skill in the target repository:

```text
Use $project-context-bootstrap to create or repair this repository's project-native context system.
```

The seed establishes the durable local system. Routine context evolution then flows through the generated project-local `evolve-project-context` skill.

## Repository Map

| Path | Ownership |
|---|---|
| [`AGENTS.md`](AGENTS.md) | development entry and owner routes for this repository |
| [`kernel-principles.md`](skills/project-context-bootstrap/references/kernel-principles.md) | canonical definitions of the four principles |
| [`bootstrap-contract.md`](skills/project-context-bootstrap/references/bootstrap-contract.md) | canonical required-output contract |
| [`SKILL.md`](skills/project-context-bootstrap/SKILL.md) | bootstrap and repair procedure |
| [`.agents/skills/evolve-project-context`](.agents/skills/evolve-project-context/SKILL.md) | this repository's context-evolution procedure |
| [`scripts/install.py`](scripts/install.py) | cross-platform installer implementation |
| [`docs/usage.md`](docs/usage.md) | installation and operating guidance |
| [`tests/`](tests) | executable context and installer invariants |

## Validation

```bash
python -m unittest discover -s tests
```

CI runs the same contract on Linux, macOS, and Windows. This repository also satisfies its own bootstrap contract through the root entry, `.agents/skills/` library, and local `evolve-project-context` skill.

## License

MIT
