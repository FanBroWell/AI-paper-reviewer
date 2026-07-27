import unittest
from pathlib import Path


class StarHistoryWorkflowTests(unittest.TestCase):
    def test_workflow_uses_repository_token_and_runs_generator(self):
        workflow = Path(".github/workflows/update-star-history.yml")
        self.assertTrue(workflow.is_file(), "star-history workflow is missing")
        content = workflow.read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", content)
        self.assertIn("schedule:", content)
        self.assertIn("contents: write", content)
        self.assertIn("python scripts/generate_star_history.py", content)
        self.assertIn("GITHUB_TOKEN: ${{ github.token }}", content)
        self.assertIn("python -m unittest discover", content)
        self.assertIn("git add assets/star-history.svg", content)
        self.assertIn("git diff --cached --quiet", content)
        self.assertLess(
            content.index("git add assets/star-history.svg"),
            content.index("git diff --cached --quiet"),
        )
        self.assertNotIn("github_pat_", content)


if __name__ == "__main__":
    unittest.main()
