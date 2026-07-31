# Usage

This file owns installation and operating guidance for Agent Context Kernel.

## Install the Seed Skill

### Codex Skill Installer

Inside Codex, invoke:

```text
$skill-installer install https://github.com/EateralSpirial/agent-context-kernel/tree/main/skills/project-context-bootstrap
```

Restart Codex after installation so the new skill is discovered.

### Clone and Install for the Current User

Linux or macOS:

```bash
git clone https://github.com/EateralSpirial/agent-context-kernel.git
cd agent-context-kernel
sh install.sh
```

Windows PowerShell:

```powershell
git clone https://github.com/EateralSpirial/agent-context-kernel.git
Set-Location agent-context-kernel
.\install.ps1
```

The default destination is `$HOME/.agents/skills/project-context-bootstrap`.

### Install for One Project

```bash
sh install.sh --project /path/to/project
```

```powershell
.\install.ps1 --project C:\path\to\project
```

Project scope installs the seed at `<project>/.agents/skills/project-context-bootstrap`.

Use `--dry-run` to inspect the destination and `--force` to replace an existing installation. Run the same command with `--force` after updating the cloned repository.

## Bootstrap an Early or Nearly Empty Project

Open the project in the coding agent and invoke:

```text
Use $project-context-bootstrap to create the project-native context system.

Project goal:
[the durable product or system goal]

Current constraints:
[technology, deployment, data, risk, or compatibility constraints]

Expected agent responsibilities:
[the kinds of work agents will perform]

Build the smallest useful context system justified by current evidence. Keep uncertain design in explicit change state.
```

The initial context will usually lead the implementation. Future feature work proceeds through the generated project skills, while context-system changes proceed through `evolve-project-context`.

## Bootstrap an Existing or Disordered Project

Invoke:

```text
Use $project-context-bootstrap to audit and normalize this repository's context system.

Perform project archaeology across code, tests, configuration, deployment, existing documentation, Git history, and recurring workflows. Recover current truth owners, identify parallel or conflicting descriptions, create one explicit context migration plan, and preserve product behavior while establishing the required project context objects.
```

For a large legacy repository, let the first pass produce the evidence map and migration plan. Apply that plan as one coordinated context change after its intended owners and acceptance criteria are clear.

## Result and Handoff

The canonical output contract lives in [`bootstrap-contract.md`](../skills/project-context-bootstrap/references/bootstrap-contract.md). After bootstrap, the project uses its own root entry and local skills. The generated `evolve-project-context` skill owns routine context maintenance, consolidation, wording, routing, and change-state reconciliation.

Invoke the seed again when a project needs first construction, major context reconstruction, or an independent audit of the local system.
