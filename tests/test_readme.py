import unittest
from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


class ReadmeTests(unittest.TestCase):
    def test_readme_has_project_title(self):
        content = README.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("# mobxsystemdesignwow\n"))

    def test_readme_has_descriptive_content(self):
        content = README.read_text(encoding="utf-8")
        description = "\n".join(content.splitlines()[1:]).strip()
        self.assertTrue(description)
        self.assertIn("system design", description.lower())


if __name__ == "__main__":
    unittest.main()
