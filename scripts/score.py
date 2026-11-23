#!/usr/bin/env python3
"""score: self-judge your submission against the rubric before judges do.

Usage:
  python3 score.py --json '{"rubric":{"demo":40,"technical":35,"impact":25},
    "self_scores":{"demo":7,"technical":8,"impact":5},
    "evidence":{"demo":"live url works","impact":"niche problem"}}'

self_scores are 1-10 per criterion. Returns weighted score, weakest
criterion, and what to fix first (weakest weighted point per hour).
"""

import sys
from common import emit, fail, read_json_arg

FIX_HINTS = {
    "demo": "Rehearse the 90-second path on a clean machine; cut any step that doesn't show on screen.",
    "technical": "Surface the hard part in the demo itself — judges can't score architecture they can't see.",
    "impact": "Quantify: name the user, the pain, and one number. Vague impact scores vague.",
    "innovation": "Differentiate in the first 10 seconds of the demo — 'X but for Y' framing.",
    "pitch": "Tighten to the 90s structure in references/demo-script.md; practice the close.",
    "design": "One clean flow beats a pretty settings page; polish the demo path only.",
    "presentation": "Tighten to the 90s structure in references/demo-script.md; practice the close.",
}


def main():
    data = read_json_arg(sys.argv)
    if data is None:
        fail('need --json {"rubric":{...},"self_scores":{...}}')

    rubric = data.get("rubric")
    scores = data.get("self_scores")
    if not rubric or not scores:
        fail("rubric and self_scores required")

    total_w = sum(rubric.values())
    if total_w <= 0:
        fail("rubric weights must sum > 0")

    earned, detail = 0.0, []
    for crit, weight in rubric.items():
        s = float(scores.get(crit, 0))
        frac = s / 10.0
        pts = frac * weight
        earned += pts
        detail.append({"criterion": crit, "weight": weight, "self_score": s,
                       "points": round(pts, 1), "max": weight})

    detail.sort(key=lambda d: d["points"] - d["max"])  # worst gap first
    weakest = detail[0]
    gap = weakest["max"] - weakest["points"]

    hint = FIX_HINTS.get(weakest["criterion"].lower(),
                         "Raise this criterion — it has the most points on the table.")

    emit({
        "status": "ok",
        "summary": f"{earned:.0f}/{total_w:.0f} weighted. Weakest: {weakest['criterion']} (-{gap:.0f} pts available)",
        "weighted_score": round(earned, 1),
        "max_score": total_w,
        "weakest_criterion": weakest["criterion"],
        "fix_first": hint,
        "breakdown": detail,
        "rules": [
            "Score yourself harshly — judges see 40+ entries, not your effort.",
            "Fix the biggest point gap, not your favorite feature.",
        ],
    }, brief="--json-brief" in sys.argv)


if __name__ == "__main__":
    main()
