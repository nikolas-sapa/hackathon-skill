#!/usr/bin/env python3
"""scope: brutal MVP cutter. Feed a feature list + remaining hours; get keep/cut/defer.

Usage:
  python3 scope.py --json '{"hours_left": 12, "features": [
      {"name": "auth", "est_h": 3, "demo_visible": false},
      {"name": "map view", "est_h": 4, "demo_visible": true},
      {"name": "settings", "est_h": 2, "demo_visible": false}]}'

Rule: a feature is KEEP iff (demo_visible OR on_critical_path) AND est fits.
Ties broken by demo visibility, then smaller estimate. Always keeps a
"demo_safety" floor: at least 1 visible feature + submit path.
"""

import sys
from common import emit, fail, read_json_arg


def main():
    data = read_json_arg(sys.argv)
    if data is None:
        fail('need --json {"hours_left":N,"features":[...]}')

    hours_left = float(data.get("hours_left", 0))
    feats = data.get("features", [])
    if hours_left <= 0 or not feats:
        fail("hours_left>0 and non-empty features required")

    reserve = float(data.get("reserve_hours", max(1.0, hours_left * 0.15)))
    budget = hours_left - reserve
    if budget <= 0:
        fail("hours_left entirely consumed by reserve", hours_left=hours_left, reserve=reserve)

    # Score: demo_visible first, then critical_path, then cheapness.
    for f in feats:
        f["_score"] = (
            (2 if f.get("demo_visible") else 0)
            + (2 if f.get("critical_path") else 0)
            - min(float(f.get("est_h", 1)) / max(budget, 0.1), 2.0)
        )
    ranked = sorted(feats, key=lambda f: -f["_score"])

    keep, cut, spent = [], [], 0.0
    for f in ranked:
        est = float(f.get("est_h", 1))
        if spent + est <= budget:
            keep.append({"name": f["name"], "est_h": est,
                         "why": "demo-visible" if f.get("demo_visible") else "critical-path"})
            spent += est
        else:
            cut.append({"name": f["name"], "est_h": est,
                        "defer_to": "post-hackathon or stretch goal"})

    if not any(k["why"] == "demo-visible" for k in keep) and any(
            f.get("demo_visible") for f in feats):
        # Demo-safety floor: force-keep cheapest visible feature.
        vis = min((f for f in feats if f.get("demo_visible")),
                  key=lambda f: float(f.get("est_h", 1)))
        keep.append({"name": vis["name"], "est_h": float(vis.get("est_h", 1)),
                     "why": "demo-safety floor"})
        spent += float(vis.get("est_h", 1))
        cut = [c for c in cut if c["name"] != vis["name"]]

    emit({
        "status": "ok",
        "summary": f"keep {len(keep)}/{len(feats)} in {spent:.1f}h of {budget:.1f}h; cut {len(cut)}",
        "budget_hours": round(budget, 1),
        "reserve_hours": reserve,
        "spent_hours": round(spent, 1),
        "keep": keep,
        "cut": cut,
        "rules": [
            "A cut feature is deleted from the plan, not parked; reopen only if a kept feature finishes early.",
            "Never keep a feature whose demo value is 'judges will understand it anyway' — they won't.",
            "If keep[] can't reach a working end-to-end demo, drop the idea's scope, not more features.",
        ],
    }, brief="--json-brief" in sys.argv)


if __name__ == "__main__":
    main()
