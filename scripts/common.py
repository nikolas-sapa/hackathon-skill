"""Shared helpers for hackathon-skill tools. Stdlib only."""

import json
import sys
from datetime import datetime, timezone


def read_json_arg(argv, flag="--json", stdin_ok=True):
    """Parse a JSON payload from --json '<str>' or stdin ('-')."""
    if flag in argv:
        i = argv.index(flag)
        try:
            return json.loads(argv[i + 1])
        except (IndexError, json.JSONDecodeError) as e:
            fail(f"bad {flag} payload: {e}")
    if stdin_ok and not sys.stdin.isatty():
        data = sys.stdin.read().strip()
        if data:
            try:
                return json.loads(data)
            except json.JSONDecodeError as e:
                fail(f"bad stdin JSON: {e}")
    return None


def emit(obj, brief=False):
    if brief and isinstance(obj, dict):
        keep = {k: obj[k] for k in ("status", "summary", "error") if k in obj}
        print(json.dumps(keep, indent=2))
    else:
        print(json.dumps(obj, indent=2))


def fail(msg, code=2, **extra):
    out = {"status": "error", "error": msg}
    out.update(extra)
    print(json.dumps(out, indent=2))
    sys.exit(code)


def hours_between(start_iso, end_iso):
    s = parse_ts(start_iso)
    e = parse_ts(end_iso)
    return (e - s).total_seconds() / 3600.0


def parse_ts(s):
    if s is None:
        fail("missing timestamp")
    s = s.strip()
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"):
        try:
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    fail(f"unparseable timestamp: {s!r} (want ISO 8601 like 2026-11-22T14:00 or +02:00 suffix)")
