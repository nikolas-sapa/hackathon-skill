#!/usr/bin/env python3
"""check: brief completeness audit. Feed the parsed brief fields; get missing/critical gaps.

Usage:
  python3 check.py --json '{"rubric": {"impact":30,"technical":40,"demo":30},
                            "team_max": 4, "submission": ["github","video"],
                            "sponsor_apis": ["nemotron"], "starts":"...","ends":"..."}'

Flags: missing rubric, no explicit demo requirement, undefined team size,
unknown submission format, sponsor track ambiguity, missing deadline.
"""

import sys
from common import emit, fail, read_json_arg

REQUIRED = [
    ("rubric", "Judging weights are unknown — you cannot prioritize features without them. Ask or infer from rules page."),
    ("team_max", "Team size cap unknown — affects scope and eligibility."),
    ("submission", "Submission format unknown — video length? repo public? live URL? Find out now, not at hour 47."),
    ("ends", "No end time — cannot plan without a deadline."),
]
OPTIONAL = [
    ("sponsor_apis", "No sponsor APIs listed — if sponsor tracks exist, matching one is often a free prize."),
    ("theme", "No theme recorded — check the brief again; building off-theme is a common DQ."),
    ("judges", "Judge names unknown — their backgrounds tell you what 'impressive' means to them."),
    ("attribution", "No 'built vs used' attribution noted — judges and AI-hack rules increasingly require it; write it into README + submission."),
]


def main():
    data = read_json_arg(sys.argv)
    if data is None or not isinstance(data, dict):
        fail_needed()
    gaps, warns = [], []
    for key, msg in REQUIRED:
        if not data.get(key):
            gaps.append({"field": key, "severity": "critical", "fix": msg})
    for key, msg in OPTIONAL:
        if not data.get(key):
            warns.append({"field": key, "severity": "warn", "fix": msg})

    rubric = data.get("rubric") or {}
    if rubric and not isinstance(rubric, dict):
        fail("rubric must be an object of criterion -> weight")
    try:
        rubric_total = sum(float(v) for v in rubric.values())
    except (TypeError, ValueError):
        fail("rubric weights must be numbers")
    if rubric and abs(rubric_total - 100) > 1:
        warns.append({"field": "rubric", "severity": "warn",
                      "fix": f"rubric weights sum to {rubric_total:g}, not 100 — re-check the source."})

    verdict = "READY" if not gaps else ("RISKY" if len(gaps) == 1 else "BLOCKED")
    emit({
        "status": "ok",
        "summary": f"{verdict}: {len(gaps)} critical gaps, {len(warns)} warnings",
        "verdict": verdict,
        "critical_gaps": gaps,
        "warnings": warns,
        "rules": [
            "Never start building on BLOCKED; a wrong assumption about submission format kills the entry.",
            "If the rubric can't be found, assume demo+impact dominate and optimize for a 90-second wow.",
        ],
    }, brief="--json-brief" in sys.argv)


def fail_needed():
    fail('need --json {"rubric":{...},"team_max":N,"submission":[...],"ends":"ISO"}')


if __name__ == "__main__":
    main()
