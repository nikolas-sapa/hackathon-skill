#!/usr/bin/env python3
"""verify: pre-submission gate. Checks what judges will actually click.

Usage:
  python3 verify.py --url https://your-demo.dev [--readme README.md]
                    [--video demo.mp4] [--max-video-min 3]

Checks: URL responds 200 (via urllib, 10s timeout), README exists and is
non-trivial, video duration (ffprobe if available, else size sanity),
and optionally git integrity (--repo PATH [--end ISO]) — the flags
organizers run on winners (giant initial commit, post-deadline pushes).
Each check reports pass/warn/fail. Exit 1 on any fail.
"""

import datetime
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path
from common import emit, fail


def check_url(url):
    try:
        opener = urllib.request.build_opener(NoRedirect())
        req = urllib.request.Request(url, method="HEAD",
                                     headers={"User-Agent": "hackathon-skill-verify"})
        with opener.open(req, timeout=10) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code  # 3xx/4xx surfaces here because we don't follow redirects
    except Exception as e:
        return {"check": "url", "result": "fail",
                "detail": f"unreachable: {type(e).__name__}: {e}"}
    if code in (301, 302, 303, 307, 308):
        return {"check": "url", "result": "warn",
                "detail": f"redirects ({code}) — check it doesn't land on a login/auth wall"}
    if code in (401, 403):
        return {"check": "url", "result": "warn",
                "detail": f"HTTP {code} — judges hit a wall; add guest/demo mode or seeded creds"}
    return {"check": "url", "result": "pass" if code == 200 else "warn",
            "detail": f"HTTP {code}"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def check_readme(path):
    p = Path(path)
    if not p.exists():
        return {"check": "readme", "result": "fail", "detail": f"{path} not found"}
    text = p.read_text(errors="replace")
    n = len(text.strip())
    hints = []
    if n < 400:
        hints.append("very short — judges open READMEs")
    if "!" not in text and "http" not in text:
        hints.append("no image or link — add a demo GIF/URL above the fold")
    if not any(w in text.lower() for w in ("setup", "install", "run", "getting started")):
        hints.append("no setup instructions")
    return {"check": "readme", "result": "warn" if hints else "pass",
            "detail": "; ".join(hints) if hints else f"{n} bytes, looks complete"}


def check_video(path, max_min):
    p = Path(path)
    if not p.exists():
        return {"check": "video", "result": "fail", "detail": f"{path} not found"}
    if shutil.which("ffprobe"):
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "json", str(p)], capture_output=True, text=True)
        try:
            dur = float(json.loads(out.stdout)["format"]["duration"])
            ok = dur <= max_min * 60
            return {"check": "video", "result": "pass" if ok else "fail",
                    "detail": f"{dur:.0f}s (limit {max_min*60:.0f}s)"}
        except (ValueError, KeyError, json.JSONDecodeError):
            pass
    mb = p.stat().st_size / 1e6
    return {"check": "video", "result": "warn",
            "detail": f"ffprobe unavailable; file is {mb:.0f}MB — verify duration manually"}


def check_git(repo, end_iso):
    """Integrity flags organizers check on winners (see references/integrity.md)."""
    try:
        log = subprocess.run(
            ["git", "-C", repo, "log", "--format=%aI", "--reverse"],
            capture_output=True, text=True, timeout=10)
        if log.returncode != 0:
            return {"check": "git", "result": "warn",
                    "detail": f"not a git repo or git failed: {log.stderr.strip()[:80]}"}
        commits = [c for c in log.stdout.splitlines() if c.strip()]
        if not commits:
            return {"check": "git", "result": "warn",
                    "detail": "no commits — commit progressively; your history is the 'built here' alibi"}
        if len(commits) == 1:
            files = subprocess.run(
                ["git", "-C", repo, "show", "--name-only", "--format=", "HEAD"],
                capture_output=True, text=True).stdout.split()
            return {"check": "git", "result": "warn",
                    "detail": (f"one giant commit ({len(files)} files) — looks like "
                               "pre-built work imported at hour 1; organizers flag this")}
        if end_iso:
            end = datetime.datetime.fromisoformat(end_iso.replace("Z", "+00:00"))
            if end.tzinfo is None:
                end = end.replace(tzinfo=datetime.timezone.utc)
            late = [c for c in commits
                    if datetime.datetime.fromisoformat(c) > end]
            if late:
                return {"check": "git", "result": "warn",
                        "detail": (f"{len(late)} commit(s) after deadline — judges diff "
                                   "timestamps; freeze at submit, polish on a branch")}
        return {"check": "git", "result": "pass",
                "detail": f"{len(commits)} commits — progressive history looks honest"}
    except Exception as e:
        return {"check": "git", "result": "warn",
                "detail": f"git check skipped: {e}"}


def main():
    args = sys.argv

    def arg(name, default=None):
        if name not in args:
            return default
        i = args.index(name)
        if i + 1 >= len(args) or args[i + 1].startswith("--"):
            fail(f"{name} needs a value")
        return args[i + 1]

    url, readme, video = arg("--url"), arg("--readme", "README.md"), arg("--video")
    repo, end = arg("--repo"), arg("--end")
    try:
        max_min = float(arg("--max-video-min", 3))
    except (TypeError, ValueError):
        fail("--max-video-min must be a number")

    checks = []
    if url:
        checks.append(check_url(url))
    checks.append(check_readme(readme))
    if video:
        checks.append(check_video(video, max_min))
    if repo:
        checks.append(check_git(repo, end))

    fails = [c for c in checks if c["result"] == "fail"]
    warns = [c for c in checks if c["result"] == "warn"]
    verdict = "SHIP" if not fails and not warns else ("FIX" if fails else "WARN")

    emit({
        "status": "ok",
        "summary": f"{verdict}: {len(checks)} checks, {len(fails)} fail, {len(warns)} warn",
        "verdict": verdict,
        "checks": checks,
    })
    if fails:
        sys.exit(1)


if __name__ == "__main__":
    main()
