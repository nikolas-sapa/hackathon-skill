#!/usr/bin/env python3
"""idea: rank candidate ideas on the 4-axis matrix. Pick one, kill the rest.

Usage:
  python3 idea.py --json '{"ideas":[
    {"name":"a","rubric_fit":4,"demoability":5,"feasibility":3,"sponsor_fit":2},
    {"name":"b","rubric_fit":5,"demoability":3,"feasibility":4,"sponsor_fit":4}]}'

Axes are 1-5. Ties broken by: offline-demoable flag, then feasibility.
"""

import sys
from common import emit, fail, read_json_arg

AXES = ["rubric_fit", "demoability", "feasibility", "sponsor_fit"]


def main():
    data = read_json_arg(sys.argv)
    if data is None or not isinstance(data, dict) or not data.get("ideas"):
        fail('need --json {"ideas":[{"name":..,"rubric_fit":N,"demoability":N,"feasibility":N,"sponsor_fit":N}]}')

    ideas = data["ideas"]
    if not isinstance(ideas, list) or len(ideas) < 2:
        fail("need at least 2 ideas to rank (generate 3, kill 2)")

    for i in ideas:
        if not isinstance(i, dict) or "name" not in i:
            fail("each idea needs at least a 'name'")
        try:
            i["_total"] = sum(float(i.get(a, 0)) for a in AXES)
            feas = float(i.get("feasibility", 0))
        except (TypeError, ValueError):
            fail(f"idea {i['name']!r}: axis scores must be numbers")
        i["_tiebreak"] = (-(1 if i.get("offline_demoable") else 0), -feas)

    ranked = sorted(ideas, key=lambda i: (-i["_total"], i["_tiebreak"]))
    winner = ranked[0]

    emit({
        "status": "ok",
        "summary": f"pick '{winner['name']}' ({winner['_total']}/20). Kill: {', '.join(i['name'] for i in ranked[1:])}",
        "winner": {"name": winner["name"], "score": winner["_total"], "max": 5 * len(AXES)},
        "ranked": [{"name": i["name"], "score": i["_total"],
                    **{a: i.get(a) for a in AXES}} for i in ranked],
        "rules": [
            "Commit to the winner now; 'we'll see' burns the ideation cap.",
            "If the winner fails its spike, pivot to #2 — never back to brainstorming.",
        ],
    }, brief="--json-brief" in sys.argv)


if __name__ == "__main__":
    main()
