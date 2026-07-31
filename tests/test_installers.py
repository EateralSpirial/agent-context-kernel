from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.py"
SHELL_WRAPPER = ROOT / "install.sh"
POWERSHELL_WRAPPER = ROOT / "install.ps1"
SKILL_NAME = "project-context-bootstrap"
REQUIRED = (
    "SKILL.md",
    "LICENSE.txt",
    "agents/openai.yaml",
    "references/kernel-principles.md",
    "references/bootstrap-contract.md",
)


def run_installer(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class InstallerTests(unittest.TestCase):
    def test_project_install_copies_complete_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = run_installer("--project", directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = Path(directory) / ".agents" / "skills" / SKILL_NAME
            for relative in REQUIRED:
                self.assertTrue((installed / relative).is_file(), relative)

    def test_existing_install_requires_force(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = run_installer("--project", directory)
            second = run_installer("--project", directory)
            forced = run_installer("--project", directory, "--force")

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("--force", second.stderr)
            self.assertEqual(forced.returncode, 0, forced.stderr)

    def test_dry_run_has_no_side_effect(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = run_installer("--project", directory, "--dry-run")
            installed = Path(directory) / ".agents" / "skills" / SKILL_NAME

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("dry run", result.stdout)
            self.assertFalse(installed.exists())

    def test_wrappers_route_to_one_installer_owner(self) -> None:
        shell = SHELL_WRAPPER.read_text(encoding="utf-8")
        powershell = POWERSHELL_WRAPPER.read_text(encoding="utf-8")

        self.assertIn("scripts/install.py", shell)
        self.assertIn("scripts/install.py", powershell)
        self.assertNotIn("copytree", shell)
        self.assertNotIn("Copy-Item", powershell)


if __name__ == "__main__":
    unittest.main()
