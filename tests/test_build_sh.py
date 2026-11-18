"""build.sh refuses to commit a dev-server build.

Runs the real build.sh in a throwaway git repo whose remote is a local bare
repo, with a stand-in `npm` that writes public/ instead of running Hugo.
Nothing here touches the real blog repo or GitHub.

Run from the blog root:  python3 -m unittest discover -s tests -t .
"""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

BUILD_SH = Path(__file__).resolve().parent.parent / "build.sh"

FAKE_NPM = """#!/bin/bash
# Stand-in for `npm run build`: writes the page the test asked for into public/.
mkdir -p public/posts
cp "$FAKE_PAGE" public/posts/index.html
"""


class BuildShLocalhostCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="build-sh-test-"))
        self.addCleanup(shutil.rmtree, self.tmp)
        self.env = self._isolated_env()
        self.remote = self.tmp / "remote.git"
        self.repo = self.tmp / "blog"
        self._git("init", "--bare", "-b", "main", str(self.remote), cwd=self.tmp)
        self._git("clone", str(self.remote), str(self.repo), cwd=self.tmp)
        shutil.copy(BUILD_SH, self.repo / "build.sh")
        (self.repo / "README.md").write_text("blog\n")
        self._git("add", "build.sh", "README.md")
        self._git("commit", "-m", "start")
        self._git("push", "-u", "origin", "main")

    def _isolated_env(self):
        fakebin = self.tmp / "bin"
        fakebin.mkdir()
        npm = fakebin / "npm"
        npm.write_text(FAKE_NPM)
        npm.chmod(0o755)
        gitconfig = self.tmp / "gitconfig"
        gitconfig.write_text("")
        env = dict(os.environ)
        env.update(
            PATH=f"{fakebin}:{env['PATH']}",
            GIT_CONFIG_GLOBAL=str(gitconfig),
            GIT_CONFIG_NOSYSTEM="1",
            GIT_AUTHOR_NAME="Test",
            GIT_AUTHOR_EMAIL="test@example.invalid",
            GIT_COMMITTER_NAME="Test",
            GIT_COMMITTER_EMAIL="test@example.invalid",
        )
        return env

    def _git(self, *args, cwd=None):
        return subprocess.run(
            ["git", *args], cwd=cwd or self.repo, env=self.env,
            check=True, capture_output=True, text=True,
        ).stdout.strip()

    def _build_with_page(self, html):
        page = self.tmp / "page.html"
        page.write_text(html)
        env = dict(self.env, FAKE_PAGE=str(page))
        return subprocess.run(
            ["bash", "build.sh", "Publish: test post"], cwd=self.repo, env=env,
            capture_output=True, text=True,
        )

    def _remote_head_subject(self):
        return self._git("log", "-1", "--format=%s", "main", cwd=self.remote)

    def test_refuses_to_commit_when_public_has_dev_server_urls(self):
        head_before = self._git("rev-parse", "HEAD")
        result = self._build_with_page(
            '<a href="http://localhost:1313/posts/">posts</a>\n')
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("public/posts/index.html", result.stdout + result.stderr)
        self.assertEqual(self._git("rev-parse", "HEAD"), head_before)
        self.assertEqual(self._remote_head_subject(), "start")

    def test_commits_and_pushes_a_clean_build(self):
        result = self._build_with_page(
            '<a href="https://thingsithinkithink.blog/posts/">posts</a>\n')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self._remote_head_subject(), "Publish: test post")

    def test_allows_the_word_localhost_in_post_text(self):
        # Three published posts already say "localhost" in their prose.
        result = self._build_with_page(
            "<p>It only works on <code>localhost</code>, so no risk.</p>\n")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self._remote_head_subject(), "Publish: test post")


if __name__ == "__main__":
    unittest.main()
