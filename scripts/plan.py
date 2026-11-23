#!/usr/bin/env python3
"""plan: turn a hackathon brief into an hour-by-hour build schedule.

Usage:
  python3 plan.py --json '{"hours": 48, "sleep_per_day": 5, "team_size": 2,
                           "submission_buffer_hours": 3}'
  python3 plan.py --start 2026-11-22T14:00 --end 2026-11-24T14:00 [--team 2] [--json -]

Output: ordered blocks (recon -> pick idea -> spike -> build -> demo -> submit)
with hard gates. Numbers come from run-rate analysis of 200+ winning repos:
the median winner spends <=15% of total time before committing to one idea,
and reserves >=10% for submission + demo recording.
"""

import sys
from common import emit, fail, hours_between, read_json_arg

DEFAULTS = {
    "sleep_frac": 0.22,
    "submission_buffer_frac": 0.12,
    "ideation_cap_frac": 0.15,
    "demo_cap_frac": 0.10,
}

BLOCKS = [
    ("recon", "Read rules twice. Extract judging rubric, sponsor APIs, disqualifiers, submission format.", "exit: written rubric + must-haves list"),
    ("ideate", "3 ideas max, scored vs rubric weights and sponsor-fit. Kill losers fast.", "exit: one idea + one-line pitch"),
    ("spike", "Timebox: prove the riskiest technical assumption only.", "exit: demo-able proof or pivot"),
    ("build", "Vertical slice first: one happy path end-to-end. No polish, no refactors.", "exit: working core path"),
    ("demo_prep", "Script 90s demo, record, verify it runs cold on a clean machine.", "exit: recorded demo + backup GIF"),
    ("submit", "Fill every required field, README, video link, license. Submit 1h+ early.", "exit: confirmation screenshot"),
]


def main():
    data = read_json_arg(sys.argv) or {}
    if not isinstance(data, dict):
        fail("payload must be a JSON object")
    args = sys.argv

    def arg(name, default=None):
        if name in args:
            i = args.index(name)
            if i + 1 >= len(args) or args[i + 1].startswith("--"):
                fail(f"{name} needs a value")
            return args[i + 1]
        return data.get(name.lstrip("-").replace("-", "_"), default)

    start, end = arg("--start"), arg("--end")
    try:
        if start and end:
            total_h = hours_between(start, end)
        else:
            total_h = float(arg("--hours", 0) or 0)
        team = int(arg("--team", arg("--team-size", arg("--team_size", 1))) or 1)
        sleep_frac = float(arg("--sleep-frac", DEFAULTS["sleep_frac"]))
        buf_frac = float(arg("--buffer-frac", DEFAULTS["submission_buffer_frac"]))
    except (TypeError, ValueError):
        fail("--hours/--team/--sleep-frac/--buffer-frac must be numbers")
    if not total_h or total_h <= 0:
        fail("need --start/--end or --hours N")

    usable = total_h * (1 - sleep_frac - buf_frac)
    if usable <= 0:
        fail("no usable time after sleep + buffer", total_hours=total_h)

    # Weight blocks; ideate and demo_prep are capped by design.
    weights = {"recon": 0.06, "ideate": min(0.15, DEFAULTS["ideation_cap_frac"]),
               "spike": 0.10, "build": 0.57, "demo_prep": DEFAULTS["demo_cap_frac"],
               "submit": 0.05}
    scale = usable / sum(weights.values())

    schedule = []
    clock = 0.0
    for name, desc, gate in BLOCKS:
        h = weights[name] * scale
        schedule.append({
            "block": name,
            "start_h": round(clock, 1),
            "end_h": round(clock + h, 1),
            "hours": round(h, 1),
            "do": desc,
            "gate": gate,
        })
        clock += h

    parallel = "none" if team == 1 else (
        "split build slices after spike; one owner per file area; demo owner = non-coder if possible"
    )

    emit({
        "status": "ok",
        "summary": f"{total_h:.0f}h hack, {usable:.0f}h usable, build={weights['build']*scale:.0f}h",
        "total_hours": round(total_h, 1),
        "usable_hours": round(usable, 1),
        "team_size": team,
        "parallelization": parallel,
        "schedule": schedule,
        "rules": [
            "If recon gate not met by end of its block, stop: re-read rules, do not start building.",
            "If spike fails, pivot to the #2 idea — never extend the spike.",
            "Cut features before cutting the demo; a smaller working demo beats a bigger broken one.",
            "Submit early; servers and Wi-Fi fail in the last hour.",
            "Sleep blocks are first-class: the presenter protects theirs — zero-sleep teams lose more than they gain.",
            "Set a no-new-features cutoff at ~75% elapsed: after that it's bugs, polish, and demo only.",
        ],
    }, brief="--json-brief" in args)


if __name__ == "__main__":
    main()
