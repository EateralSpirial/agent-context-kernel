# Agent Context Kernel Principles

This file owns the canonical definitions of the kernel's four principles. They form a compact governance layer for project-native agent context systems.

## 1. Onboarding Principle

**Project context is compact onboarding for a capable new agent.**

Treat the coding agent as a strong engineer with general programming knowledge, code comprehension, memory, and judgment. Supply the project-specific knowledge that enables sound decisions: purpose, ownership, contracts, non-obvious constraints, fragile sequences, material risk, external authority, and acceptance boundaries.

Code and executable evidence carry ordinary mechanics. Context earns permanence when it reduces costly rediscovery, prevents material ambiguity, or improves decisions across tasks. Explain the reason behind a rule when the reason helps the agent generalize beyond enumerated cases. Let Git retain process history while the working tree presents current guidance.

A successful onboarding route moves from a compact entry to the narrowest relevant owner and then to direct evidence. The agent reads only the context required by the task and expands its investigation as evidence demands.

## 2. Singular Truth Principle

**Each durable project truth has one primary owner and one canonical definition.**

Canonical owners carry complete definitions. Indexes and entry files route to those owners. Local applications describe only the additional facts created by their own scope, condition, or effect. Simple, common, and cheaply recoverable truths may remain implicit in code or evidence.

One definition keeps a semantic change atomic. Parallel definitions can remain individually plausible while drifting across a change, leaving old and new project states active at the same time. Ownership therefore applies to standards, contracts, plans, procedures, status meanings, thresholds, and other context-worthy facts.

Generated projections may appear in several places when one source produces them deterministically. Human-maintained parallel definitions create separate truth owners and require consolidation.

## 3. Affirmative Direction Principle

**Shared context leads attention with the intended state, owner, condition, action, and effect.**

Desired-state language foregrounds what the agent should build, preserve, inspect, or verify. It gives the model a constructive target and supports judgment across unenumerated cases.

Use neutral comparison when alternatives improve understanding, such as preferring an existing public owner when it already expresses the required boundary. Precise prohibitions remain valuable for narrow safety constraints, literal protocol requirements, reserved values, and destructive operations. Their owner and scope stay explicit.

Context quality depends on the concepts it makes salient. Concise constructive guidance reduces attention spent on rejected paths and keeps the agent oriented toward the project state that should exist.

## 4. Change Plan and Context-First Principle

**For a context-worthy capability or behavior change, establish its canonical context before implementation.**

Context-worthy changes include durable capabilities, public behavior, ownership boundaries, data meaning, lifecycle semantics, risk rules, and recurring task methods. Establish or confirm the intended contract and its owner before code begins to depend on it. Ordinary implementation mechanics remain code-owned.

A proposed target state lives in one explicit change owner, such as a plan or proposal, while current canonical owners continue to describe the accepted system. When implementation and validation complete, promote the accepted meaning into current owners and close the temporary change state through the repository's normal history mechanism.

Implementation can lead during discovery, prototyping, incident response, or inherited work. Treat that condition as an explicit reconciliation state: inspect code and evidence, determine the intended durable behavior, establish the missing context owner, and align dependent work before closure.

Context and implementation evolve as coordinated representations at selected key nodes. Their relationship remains visible through four states:

- **Aligned:** current owners, code, tests, and evidence agree.
- **Context ahead:** one change owner defines the target while implementation is in progress.
- **Implementation ahead:** code or evidence has advanced and context reconciliation is active.
- **Diverged:** context and implementation express competing durable intentions; resolve the intended owner before dependent expansion.

## Orthogonality

The onboarding principle selects knowledge worth preserving. The singular truth principle assigns ownership. The affirmative direction principle shapes expression. The change plan principle orders evolution. Together they cover content, location, wording, and time while preserving project-specific directory design.
