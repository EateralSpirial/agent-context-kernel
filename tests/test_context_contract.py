from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "project-context-bootstrap"
PRINCIPLES = SKILL_ROOT / "references" / "kernel-principles.md"
CONTRACT = SKILL_ROOT / "references" / "bootstrap-contract.md"
SKILL = SKILL_ROOT / "SKILL.md"
INTERFACE = SKILL_ROOT / "agents" / "openai.yaml"
SKILL_LICENSE = SKILL_ROOT / "LICENSE.txt"
AGENTS = ROOT / "AGENTS.md"
README = ROOT / "README.md"
USAGE = ROOT / "docs" / "usage.md"
INSTALLER = ROOT / "scripts" / "install.py"
LOCAL_SKILL_LIBRARY = ROOT / ".agents" / "skills"
EVOLUTION_SKILL = LOCAL_SKILL_LIBRARY / "evolve-project-context" / "SKILL.md"
EVOLUTION_INTERFACE = LOCAL_SKILL_LIBRARY / "evolve-project-context" / "agents" / "openai.yaml"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalized(path: Path) -> str:
    return " ".join(read(path).split())


class ContextContractTests(unittest.TestCase):
    def test_installable_skill_is_self_contained(self) -> None:
        for path in (SKILL, PRINCIPLES, CONTRACT, INTERFACE, SKILL_LICENSE):
            self.assertTrue(path.is_file(), path)

        skill = read(SKILL)
        self.assertIn("references/kernel-principles.md", skill)
        self.assertIn("references/bootstrap-contract.md", skill)
        self.assertIn("name: project-context-bootstrap", skill)

    def test_entry_is_compact_and_routes_to_primary_owners(self) -> None:
        agents = read(AGENTS)
        self.assertLessEqual(len(agents.splitlines()), 50)
        for route in (
            "skills/project-context-bootstrap/references/kernel-principles.md",
            "skills/project-context-bootstrap/references/bootstrap-contract.md",
            "skills/project-context-bootstrap/SKILL.md",
            ".agents/skills/evolve-project-context/SKILL.md",
            "scripts/install.py",
            "docs/usage.md",
            "tests/",
        ):
            self.assertIn(route, agents)
            self.assertTrue((ROOT / route).exists(), route)

    def test_repository_self_hosts_required_objects(self) -> None:
        self.assertTrue(AGENTS.is_file())
        self.assertTrue(LOCAL_SKILL_LIBRARY.is_dir())
        self.assertTrue(EVOLUTION_SKILL.is_file())
        self.assertTrue(EVOLUTION_INTERFACE.is_file())

        named_owners = {
            path.relative_to(ROOT).as_posix()
            for path in LOCAL_SKILL_LIBRARY.glob("*/SKILL.md")
            if "name: evolve-project-context" in read(path)
        }
        self.assertEqual(
            named_owners,
            {".agents/skills/evolve-project-context/SKILL.md"},
        )
        self.assertIn(
            ".agents/skills/evolve-project-context/SKILL.md",
            read(AGENTS),
        )

    def test_four_principles_have_one_canonical_definition_owner(self) -> None:
        anchors = (
            "Project context is compact onboarding for a capable new agent.",
            "Each durable project truth has one primary owner and at most one canonical context definition.",
            "Shared context leads attention with the intended state, owner, condition, action, and effect.",
            "For a context-worthy capability or behavior change, establish its canonical context before implementation.",
        )
        context_files = sorted(ROOT.glob("**/*.md"))

        for anchor in anchors:
            owners = {
                path.relative_to(ROOT).as_posix()
                for path in context_files
                if anchor in normalized(path)
            }
            self.assertEqual(
                owners,
                {"skills/project-context-bootstrap/references/kernel-principles.md"},
                anchor,
            )

    def test_required_objects_have_one_contract_owner(self) -> None:
        anchors = (
            "The target repository has one root `AGENTS.md`.",
            "The target repository has one project-local skill library.",
            "The project-local skill library contains exactly one `evolve-project-context` skill.",
        )
        context_files = sorted(ROOT.glob("**/*.md"))

        for anchor in anchors:
            owners = {
                path.relative_to(ROOT).as_posix()
                for path in context_files
                if anchor in normalized(path)
            }
            self.assertEqual(
                owners,
                {"skills/project-context-bootstrap/references/bootstrap-contract.md"},
                anchor,
            )

    def test_principle_set_is_complete_and_orthogonal(self) -> None:
        principles = read(PRINCIPLES)
        headings = (
            "## 1. Onboarding Principle",
            "## 2. Singular Truth Principle",
            "## 3. Affirmative Direction Principle",
            "## 4. Change Plan and Context-First Principle",
            "## Orthogonality",
        )
        positions = [principles.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))

    def test_bootstrap_reads_governance_before_design(self) -> None:
        skill = normalized(SKILL)
        principles = "references/kernel-principles.md"
        contract = "references/bootstrap-contract.md"
        archaeology = "Perform project archaeology."
        design = "Design through the four principles."
        required = "Establish the required objects."
        close = "Close the bootstrap change."

        for anchor in (principles, contract, archaeology, design, required, close):
            self.assertIn(anchor, skill)
        self.assertLess(skill.index(principles), skill.index(archaeology))
        self.assertLess(skill.index(contract), skill.index(archaeology))
        self.assertLess(skill.index(archaeology), skill.index(design))
        self.assertLess(skill.index(design), skill.index(required))
        self.assertLess(skill.index(required), skill.index(close))

    def test_bootstrap_supports_early_and_legacy_projects(self) -> None:
        skill = normalized(SKILL)
        for anchor in (
            "Early or nearly empty project:",
            "Existing or disordered project:",
            "Validate with a cold start.",
            "Evolution Handoff",
        ):
            self.assertIn(anchor, skill)

    def test_public_orientation_routes_to_canonical_owners(self) -> None:
        readme = read(README)
        self.assertIn("kernel-principles.md", readme)
        self.assertIn("bootstrap-contract.md", readme)
        self.assertIn("docs/usage.md", readme)
        self.assertIn("The linked file owns the complete principle definitions.", readme)
        self.assertTrue(USAGE.is_file())
        self.assertTrue(INSTALLER.is_file())


if __name__ == "__main__":
    unittest.main()
