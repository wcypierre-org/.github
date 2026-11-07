import datetime as dt
import unittest

from scripts.release_digest import is_dependency_update, render_digest


def item(repo, number, title, author="wcypierre"):
    return {
        "repository_url": f"https://api.github.com/repos/wcypierre-org/{repo}",
        "number": number,
        "title": title,
        "html_url": f"https://github.com/wcypierre-org/{repo}/pull/{number}",
        "user": {"login": author},
    }


class ReleaseDigestTests(unittest.TestCase):
    def test_groups_substantive_changes_and_separates_dependencies(self):
        changes = [item("jira-tracker", 4, "feat: add summary"), item("anime-listing", 8, "chore(deps): update", "dependabot[bot]")]
        rendered = render_digest("wcypierre-org", dt.date(2026, 11, 1), dt.date(2026, 11, 7), changes)
        self.assertIn("## jira-tracker", rendered)
        self.assertIn("## Dependency maintenance", rendered)
        self.assertNotIn("## anime-listing\n", rendered)

    def test_empty_period_is_explicit(self):
        rendered = render_digest("wcypierre-org", dt.date(2026, 11, 1), dt.date(2026, 11, 7), [])
        self.assertIn("No pull requests were merged", rendered)

    def test_dependency_detection(self):
        self.assertTrue(is_dependency_update(item("x", 1, "Update package", "dependabot[bot]")))
        self.assertFalse(is_dependency_update(item("x", 1, "feat: user feature")))


if __name__ == "__main__":
    unittest.main()
