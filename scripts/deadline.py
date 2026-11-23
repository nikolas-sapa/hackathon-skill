#!/usr/bin/env python3
"""deadline: time-left + next milestones, for agents mid-run.

Usage:
  python3 deadline.py --end 2026-11-24T14:00+02:00 [--now 2026-11-23T20:00+02:00]
                      [--buffer-hours 3] [--block recon|ideate|spike|build|demo_prep|submit]
"""

import sys
from datetime import datetime, timezone
from common import emit, fail, parse_ts


def main():
    args = sys.argv

    def arg(name, default=None):
        return args[args.index(name) + 1] if name in args else default

    end_s = arg("--end")
    if not end_s:
        fail("need --end ISO timestamp")
    end = parse_ts(end_s)
    now = parse_ts(arg("--now")) if arg("--now") else datetime.now(timezone.utc)
    buffer_h = float(arg("--buffer-hours", 3))
    block = arg("--block")

    left = (end - now).total_seconds() / 3600.0
    build_left = max(0.0, left - buffer_h)

    advice = []
    if left <= 0:
        advice.append("PAST DEADLINE. Submit whatever exists; a partial entry beats a zero.")
    elif left <= buffer_h:
        advice.append("INSIDE SUBMISSION BUFFER. Freeze features, finish demo + submission only.")
    elif build_left <= 2:
        advice.append("<=2h of build time left. Merge what works, stub what doesn't, start demo prep.")
    else:
        advice.append(f"{build_left:.1f}h of build time left. Cut scope to fit, don't stretch time.")

    if block == "ideate" and build_left < 8:
        advice.append("Still ideating with <8h build time: pick the simplest viable idea now.")
    if block == "build" and build_left <= 4:
        advice.append("Stop adding features. Wire the happy path, make it run, then demo.")

    emit({
        "status": "ok",
        "summary": f"{left:.1f}h left ({build_left:.1f}h buildable)",
        "hours_left": round(left, 1),
        "buildable_hours": round(build_left, 1),
        "buffer_hours": buffer_h,
        "current_block": block,
        "advice": advice,
    }, brief="--json-brief" in args)


if __name__ == "__main__":
    main()
