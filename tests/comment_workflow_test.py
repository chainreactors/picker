import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml


WORKFLOW_PATH = Path(__file__).resolve().parents[1] / ".github/workflows/comment.yml"


class CommentWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.workflow = yaml.load(
            WORKFLOW_PATH.read_text(encoding="utf-8"), Loader=yaml.BaseLoader
        )
        self.job = self.workflow["jobs"]["push-comment"]

    def prepare_notification(self, title, body, directory):
        event = {
            "issue": {"title": title},
            "comment": {
                "body": body,
                "user": {"login": "external-user"},
                "author_association": "NONE",
                "html_url": "https://github.com/example/repo/issues/1#issuecomment-1",
            },
        }
        event_path = directory / "event.json"
        output_path = directory / "output"
        event_path.write_text(json.dumps(event), encoding="utf-8")
        step = next(step for step in self.job["steps"] if step.get("id") == "notification")
        result = subprocess.run(
            ["bash", "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", step["run"]],
            cwd=directory,
            env={
                "PATH": os.environ["PATH"],
                "HOME": str(directory),
                "GITHUB_EVENT_PATH": str(event_path),
                "GITHUB_OUTPUT": str(output_path),
            },
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = output_path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 1)
        self.assertTrue(lines[0].startswith("body="))
        return json.loads(lines[0].removeprefix("body="))

    def test_notification_preserves_text_without_executing_commands(self):
        values = [
            "普通评论 😀",
            '"quoted" \\ backslash',
            "line 1\r\nline 2\nPICKER_EOF\nbody=forged",
            "::error::fake log\n::set-output name=body::forged",
            "$(touch marker-dollar)",
            "`touch marker-backtick`",
            '"; touch marker-quote; #',
            "\u2028\u2029\t",
            "",
        ]
        for field in ("title", "body"):
            for value in values:
                with self.subTest(field=field, value=value), tempfile.TemporaryDirectory() as tmp:
                    directory = Path(tmp)
                    title = value if field == "title" else "Normal title"
                    body = value if field == "body" else "Normal comment"
                    payload = self.prepare_notification(title, body, directory)
                    self.assertEqual(list(directory.glob("marker-*")), [])
                    self.assertEqual(payload, {
                        "msgtype": "markdown",
                        "markdown": {
                            "title": f"{title} 新增评论",
                            "text": (
                                f" external-user 评论了 [{title}]"
                                "(https://github.com/example/repo/issues/1#issuecomment-1):"
                                f"\n\n{body}"
                            ),
                        },
                    })

    def test_comment_trigger_and_audience_are_preserved(self):
        self.assertEqual(self.workflow["on"], {"issue_comment": {"types": ["created"]}})
        self.assertEqual(self.job["if"], "contains(github.event.issue.labels.*.name, 'pick')")


if __name__ == "__main__":
    unittest.main()
