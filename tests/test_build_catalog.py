import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_catalog.py"
FIXED_TIME = "2026-08-25T00:00:00Z"


def sample_repo(full_name, **overrides):
    owner, name = full_name.split("/", 1)
    repo = {
        "starred_at": "2026-08-01T00:00:00Z",
        "name": name,
        "full_name": full_name,
        "html_url": f"https://github.com/{full_name}",
        "description": "AI agent skill for video automation with ffmpeg",
        "homepage": None,
        "language": "Python",
        "topics": ["ai-agents", "video-automation", "agent-skills"],
        "stars": 42,
        "forks": 3,
        "archived": False,
        "disabled": False,
        "updated_at": "2026-08-20T00:00:00Z",
        "pushed_at": "2026-08-20T00:00:00Z",
        "default_branch": "main",
        "license": "MIT",
    }
    repo.update(overrides)
    return repo


class CatalogBuilderTests(unittest.TestCase):
    def run_builder(self, repos):
        temp_dir = tempfile.TemporaryDirectory()
        base = Path(temp_dir.name)
        input_path = base / "source.json"
        json_path = base / "catalog.json"
        markdown_path = base / "CATALOG.md"
        input_path.write_text(json.dumps(repos, ensure_ascii=False), encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--input",
                str(input_path),
                "--json-output",
                str(json_path),
                "--markdown-output",
                str(markdown_path),
                "--generated-at",
                FIXED_TIME,
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return temp_dir, result, json_path, markdown_path

    def test_builds_multilabel_searchable_catalog(self):
        repos = [
            sample_repo("example/video-agent"),
            sample_repo(
                "example/quant-tool",
                description="Financial trading and investment research platform",
                topics=["finance", "trading", "machine-learning"],
            ),
            sample_repo(
                "example/old-reference",
                description="An archived awesome collection of templates",
                language=None,
                topics=["awesome-list", "templates"],
                archived=True,
                license=None,
            ),
        ]
        temp_dir, result, json_path, markdown_path = self.run_builder(repos)
        self.addCleanup(temp_dir.cleanup)
        self.assertEqual(result.returncode, 0, result.stderr)

        catalog = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertEqual(catalog["source"]["repository_count"], 3)
        self.assertFalse(catalog["source"]["llm_used"])
        self.assertEqual(catalog["generated_at"], FIXED_TIME)
        by_name = {entry["full_name"]: entry for entry in catalog["repositories"]}

        video = by_name["example/video-agent"]
        self.assertIn("video-production", {item["id"] for item in video["capabilities"]})
        self.assertIn("agent-skill", {item["id"] for item in video["capabilities"]})
        self.assertIn("video-media", {item["id"] for item in video["categories"]})
        self.assertIn("example/video-agent", catalog["indexes"]["by_capability"]["video-production"])
        self.assertGreaterEqual(video["chatgpt_assistance"]["score"], 4)

        quant = by_name["example/quant-tool"]
        self.assertEqual(quant["risks"]["highest_level"], "high")
        self.assertIn("financial-use", {item["code"] for item in quant["risks"]["items"]})

        archived = by_name["example/old-reference"]
        self.assertEqual(archived["maintenance"]["status"], "archived")
        self.assertIn("license-unknown", {item["code"] for item in archived["risks"]["items"]})

        markdown = markdown_path.read_text(encoding="utf-8")
        self.assertIn("基礎版不使用 LLM", markdown)
        self.assertIn("example/video-agent", markdown)

    def test_rejects_duplicate_repository_names(self):
        repo = sample_repo("example/duplicate")
        temp_dir, result, _, _ = self.run_builder([repo, dict(repo)])
        self.addCleanup(temp_dir.cleanup)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate full_name", result.stderr)


if __name__ == "__main__":
    unittest.main()
