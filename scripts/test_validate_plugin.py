"""Regression checks for package failures that can disable skill-backed delegation."""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("validator", Path(__file__).with_name("validate-plugin.py"))
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)
SOURCE = Path(__file__).resolve().parents[1]


class PackageValidationTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("skills", "com.github.copilot", "scripts"):
            shutil.copytree(SOURCE / name, self.root / name, ignore=shutil.ignore_patterns("__pycache__"))
        for path in SOURCE.glob("*"):
            if path.suffix in (".md", ".json") or path.name == "LICENSE":
                shutil.copy2(path, self.root / path.name)

    def mutate(self, relative, old, new):
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assert_rejected(self, expected):
        errors, _ = VALIDATOR.validate(self.root)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_complete_package(self):
        self.assertEqual(VALIDATOR.validate(self.root)[0], [])

    def test_duplicate_agent_identity(self):
        self.mutate("com.github.copilot/agents/scss-specialist.agent.md",
                    "name: SCSS Specialist", "name: Bootstrap Italia Specialist")
        self.assert_rejected("Duplicate agent names")

    def test_missing_required_skill(self):
        (self.root / "skills/modern-css/SKILL.md").unlink()
        self.assert_rejected("Missing link target")

    def test_broken_nested_reference(self):
        (self.root / "skills/angular-bootstrap-italia/references/testing.md").unlink()
        self.assert_rejected("Missing link target")

    def test_specialist_write_permission(self):
        self.mutate("com.github.copilot/agents/scss-specialist.agent.md", "  - read", "  - edit")
        self.assert_rejected("tool permissions")

    def test_missing_agent_tool(self):
        self.mutate("com.github.copilot/agents/angular-bootstrap-italia-orchestrator.agent.md",
                    "  - agent\n", "")
        self.assert_rejected("tool permissions")

    def test_duplicate_yaml_key(self):
        self.mutate("com.github.copilot/agents/angular-architect.agent.md",
                    "name: Angular Architect", "name: Angular Architect\nname: Duplicate")
        self.assert_rejected("Duplicate YAML key")

    def test_copied_git_metadata(self):
        (self.root / "skills/modern-css/.git").write_text("gitdir: missing", encoding="utf-8")
        self.assert_rejected("Copied Git metadata")


if __name__ == "__main__":
    unittest.main()
