---
name: project-context-bootstrap
description: Inspect a software repository and create, normalize, or repair a complete project-native context system for coding agents. Use for empty, growing, legacy, or disordered projects that need a root AGENTS.md, a project skill library, an evolve-project-context skill, durable truth ownership, onboarding routes, context-first change coordination, or semantic context validation.
---

# Project Context Bootstrap

This seed skill builds a project-owned context system from repository evidence. It establishes the durable objects required for future agents, then hands routine context evolution to the project-local `evolve-project-context` skill.

## Read First

Read these canonical references before designing or changing the target system:

1. `references/kernel-principles.md` — the four governing principles;
2. `references/bootstrap-contract.md` — the required bootstrap outputs and their ownership.

Apply both references while writing the target repository's entry, skills, standards, plans, contracts, routes, and validation evidence.

## Operating Premise

Treat the target agent as a capable new engineer. Give it compact project-specific orientation, clear owners, reliable routes, task methods, and direct access to evidence. Let code, tests, schemas, runtime records, and external authorities retain ordinary facts they already express well.

Choose paths, document types, context planes, and skill boundaries from the repository's conventions and actual coordination needs. Preserve coherent existing owners. Establish new structure where the project needs a durable owner or discoverable route.

## Project Modes

- **Early or nearly empty project:** derive the smallest useful system from the stated goal, constraints, intended domains, and expected agent responsibilities. Keep uncertain design in an explicit plan or proposal until evidence supports acceptance.
- **Existing or disordered project:** treat code, tests, configuration, deployment, history, and current behavior as evidence. Recover durable owners, consolidate parallel descriptions, surface missing contracts, and preserve product behavior while context becomes coherent.

## Bootstrap Method

1. **Establish the outcome.** State which future agent tasks should become safer, faster, or more consistent and identify the current context failure.
2. **Perform project archaeology.** Inspect repository entry points, architecture, modules, public interfaces, build and test systems, configuration, deployment, data boundaries, risk surfaces, plans, history, and recurring task patterns. Record evidence before designing structure.
3. **Design through the four principles.** Select knowledge worth preserving, assign one canonical owner, express the intended state constructively, and establish an explicit change owner for target-state work.
4. **Establish the required objects.** Fulfil `references/bootstrap-contract.md`: create or normalize the root `AGENTS.md`, the project-local skill library, and its sole `evolve-project-context` skill.
5. **Derive supporting context.** Add the smallest useful standards, contracts, plans, risk owners, evidence routes, and regression checks. Use `.standards/` when reusable architecture, module, database, risk, or codebase rules benefit from dedicated owners.
6. **Build the onboarding route.** Route each task horizontally from the compact entry to the narrowest applicable owner and then to direct evidence. Keep routing layers short.
7. **Generate project task skills.** Create skills for recurring, high-risk, fragile, or project-specific procedures. Each skill owns one trigger-specific method, reads the narrowest relevant owners, and carries proportionate acceptance evidence.
8. **Protect semantic invariants.** Use the project's existing test stack or small standard-library checks to protect critical routes, unique owners, required metadata, and context-first ordering. Let human or agent review judge broader semantic equivalence.
9. **Validate with a cold start.** Approach the repository as a fresh capable agent. Confirm that the entry reveals the right owners, the selected context supports sound judgment, and a representative task can proceed from repository evidence alone.
10. **Close the bootstrap change.** Align routes, metadata, links, and current owners; retain active target state in its explicit change owner; retire stale context in the same coordinated change; record process history in Git.

## Change-State Handling

Classify each context-worthy change before dependent work expands:

- **Aligned:** proceed through the relevant project skill and preserve agreement among owners, implementation, tests, and evidence.
- **Context ahead:** implement toward the explicit change owner; promote accepted meaning into current owners after validation.
- **Implementation ahead:** inspect implementation and evidence, establish the missing reconciliation owner, determine durable intent, and align current owners before closure.
- **Diverged:** identify the intended durable behavior and canonical owner, resolve the semantic conflict, and then continue dependent work.

## Evolution Handoff

At completion, invoke or inspect the generated `evolve-project-context` skill as a cold-start consumer. Confirm that it can construct, consolidate, relocate, simplify, validate, and iterate the context system using the project's own owners and evidence. Routine context changes then flow through that local skill. Reuse this bootstrap for first construction, major reconstruction, or independent audit.

## Acceptance

Accept the bootstrap when the required objects satisfy their canonical contract, the four principles govern all generated context, derived structure earns its maintenance cost, a new agent can find the relevant owner from the root entry, and validation protects the highest-value semantic invariants.
