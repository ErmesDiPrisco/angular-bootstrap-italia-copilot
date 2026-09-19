"""Exercise skill synchronization only in isolated temporary packages."""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SHELL = shutil.which("pwsh") or shutil.which("powershell")
SOURCES = {
    "angular-developer": "external/angular-skills/angular-developer",
    "angular-bootstrap-italia": "external/angular-bootstrap-italia-skill/angular-bootstrap-italia",
    "ponytail": "external/ponytail/skills/ponytail",
    "caveman": "external/caveman/skills/caveman",
    "modern-css": "external/modern-css",
    "web-typography": "external/wondelai-skills/web-typography",
}


@unittest.skipUnless(SHELL, "PowerShell is required for sync integration checks")
class SkillSyncTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "plugin with spaces"
        (self.root / "scripts").mkdir(parents=True)
        self.script = self.root / "scripts/sync-skills.ps1"
        shutil.copy2(Path(__file__).with_name("sync-skills.ps1"), self.script)
        for name, relative in SOURCES.items():
            source = self.root / relative
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text(f"---\nname: {name}\n---\nSkill content\n", encoding="utf-8")
            target = self.root / "skills" / name
            target.mkdir(parents=True)
            (target / "sentinel.txt").write_text("Existing user copy", encoding="utf-8")
        for name in ("ponytail", "caveman", "wondelai-skills"):
            (self.root / "external" / name / "LICENSE").write_text("Upstream notice", encoding="utf-8")
        (self.root / SOURCES["modern-css"] / ".git").write_text("gitdir: outside", encoding="utf-8")

    def run_sync(self, *args):
        return subprocess.run(
            [SHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
             "-File", str(self.script), *args],
            cwd=self.temp.name, capture_output=True, text=True, timeout=30,
        )

    def assert_originals_preserved(self):
        for name in SOURCES:
            target = self.root / "skills" / name
            self.assertEqual((target / "sentinel.txt").read_text(encoding="utf-8"), "Existing user copy")
            self.assertFalse((target / "SKILL.md").exists())

    def test_missing_last_source_preserves_all_targets(self):
        (self.root / SOURCES["web-typography"] / "SKILL.md").unlink()
        result = self.run_sync()
        self.assertNotEqual(result.returncode, 0)
        self.assert_originals_preserved()

    def test_whatif_preserves_all_targets(self):
        result = self.run_sync("-WhatIf")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_originals_preserved()

    def test_sync_from_other_directory_excludes_git_and_keeps_notices(self):
        result = self.run_sync()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in SOURCES:
            target = self.root / "skills" / name
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertFalse((target / "sentinel.txt").exists())
            self.assertFalse((target / ".git").exists())
        for name in ("ponytail", "caveman", "web-typography"):
            self.assertEqual((self.root / "skills" / name / "LICENSE").read_text(encoding="utf-8"),
                             "Upstream notice")


if __name__ == "__main__":
    unittest.main()
