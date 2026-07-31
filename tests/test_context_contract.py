from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRINCIPLES = ROOT / "skills" / "project-context-bootstrap" / "references" / "kernel-principles.md"
SKILL = ROOT / "skills" / "project-context-bootstrap" / "SKILL.md"
AGENTS = ROOT / "AGENTS.md"
README = ROOT / "README.md"
INTERFACE = ROOT / "skills" / "project-context-bootstrap" / "agents" / "openai.yaml"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalized(path: Path) -> str:
    return " ".join(read(path).split())


class ContextContractTests(unittest.TestCase):
    def test_installable_skill_is_self_contained(self) -> None:
        for path in (SKILL, PRINCIPLES, INTERFACE):
            self.assertTrue(path.is_file(), path)

        skill = read(SKILL)
        self.assertIn("references/kernel-principles.md", skill)
        self.assertIn("name: project-context-bootstrap", skill)

    def test_entry_is_compact_and_routes_to_primary_owners(self) -> None:
        agents = read(AGENTS)
        self.assertLessEqual(len(agents.splitlines()), 50)
        for route in (
            "skills/project-context-bootstrap/references/kernel-principles.md",
            "skills/project-context-bootstrap/SKILL.md",
            "skills/project-context-bootstrap/agents/openai.yaml",
            "tests/test_context_contract.py",
        ):
            self.assertIn(route, agents)
            self.assertTrue((ROOT / route).is_file(), route)

    def test_four_principles_have_one_canonical_definition_owner(self) -> None:
        anchors = (
            "Project context is compact onboarding for a capable new agent.",
            "Each durable project truth has one primary owner and one canonical definition.",
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

    def test_bootstrap_establishes_context_before_implementation(self) -> None:
        skill = normalized(SKILL)
        context_step = "Establish the intended context and change owner."
        implementation_step = "Implement or reconcile the code."
        self.assertIn(context_step, skill)
        self.assertIn(implementation_step, skill)
        self.assertLess(skill.index(context_step), skill.index(implementation_step))

    def test_bootstrap_adapts_structure_from_project_evidence(self) -> None:
        skill = normalized(SKILL)
        for anchor in (
            "Choose paths, document types, context planes, and skill boundaries from the repository's existing conventions",
            "Perform project archaeology.",
            "Derive the knowledge model.",
            "Validate with a cold start.",
        ):
            self.assertIn(anchor, skill)

    def test_public_orientation_routes_to_canonical_principles(self) -> None:
        readme = read(README)
        self.assertIn("kernel-principles.md", readme)
        self.assertIn("The linked file owns the complete definitions.", readme)


if __name__ == "__main__":
    unittest.main()
