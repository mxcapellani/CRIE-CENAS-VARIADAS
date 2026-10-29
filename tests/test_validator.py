#!/usr/bin/env python3
"""Testes de regressão para detecção de pacotes inválidos, sem serviços externos."""
from pathlib import Path
import shutil
import tempfile
import unittest
from validate import validate, BASE

SOURCE = Path(__file__).resolve().parents[1]

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git", ".venv"))
        self.skill = self.root / BASE / "SKILL.md"

    def test_valid_package(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_reference(self):
        (self.root / BASE / "references/aspect-ratio.md").unlink()
        self.assertTrue(any("aspect-ratio" in e for e in validate(self.root)))

    def test_invalid_yaml(self):
        self.skill.write_text("---\nname: [invalid\n---\n", encoding="utf-8")
        self.assertTrue(any("YAML inválido" in e for e in validate(self.root)))

    def test_duplicate_yaml_key(self):
        s = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(s.replace("name: crie-cenas-variadas", "name: crie-cenas-variadas\nname: other"), encoding="utf-8")
        self.assertTrue(any("duplicada" in e for e in validate(self.root)))

    def test_wrong_name(self):
        s = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(s.replace("name: crie-cenas-variadas", "name: wrong"), encoding="utf-8")
        self.assertTrue(any("Nome técnico" in e for e in validate(self.root)))

    def test_broken_internal_link(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as f:
            f.write("\n[Quebrado](missing.md)\n")
        self.assertTrue(any("Link interno" in e for e in validate(self.root)))

    def test_empty_description(self):
        s = self.skill.read_text(encoding="utf-8")
        start = s.index("description:")
        end = s.index("\n---", start)
        self.skill.write_text(s[:start] + 'description: ""' + s[end:], encoding="utf-8")
        self.assertTrue(any("Description" in e for e in validate(self.root)))

    def test_missing_test_cases(self):
        (self.root / "tests/acceptance-tests.md").write_text("# Casos\n", encoding="utf-8")
        self.assertTrue(any("12 casos" in e for e in validate(self.root)))

    def test_missing_language(self):
        p = self.root / BASE / "examples/interior-scenes.md"
        p.write_text(p.read_text().replace("ENGLISH:", "", 1))
        self.assertTrue(any("bilíngues" in e for e in validate(self.root)))

    def test_ratio_mismatch(self):
        p = self.root / BASE / "examples/interior-scenes.md"
        p.write_text(p.read_text().replace("4:3", "16:9", 1))
        self.assertTrue(any("Ratio" in e for e in validate(self.root)))

class RatioTests(unittest.TestCase):
    def setUp(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("ratio_helper", SOURCE / BASE / "scripts/aspect_ratio.py")
        self.helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.helper)

    def test_standard(self):
        self.assertEqual(self.helper.aspect_ratio(1920, 1080), "16:9")
        self.assertEqual(self.helper.aspect_ratio(1080, 1920), "9:16")
        self.assertEqual(self.helper.aspect_ratio(1200, 900), "4:3")

    def test_unusual(self):
        self.assertEqual(self.helper.aspect_ratio(1000, 667), "1000:667")

    def test_invalid(self):
        for dims in [(0,100),(-1,100),(1.5,100),(True,100)]:
            with self.assertRaises(ValueError):
                self.helper.aspect_ratio(*dims)

if __name__ == "__main__":
    unittest.main()
