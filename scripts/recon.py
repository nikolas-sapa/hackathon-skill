#!/usr/bin/env python3
"""recon: turn raw hackathon research into a scored, actionable brief.

The agent does the web research (judges, sponsors, past winners); this tool
structures it and flags what matters.

Usage:
  python3 recon.py --json '{
    "event": "GenAI Summit Athens",
    "judges": [{"name":"X","background":"investor"},{"name":"Y","background":"engineer"}],
    "sponsors": [{"name":"Nebius","api":true,"prize":"$5k credits"}],
    "past_winners": [{"name":"W","why_won":"live demo + real users"}],
    "requirements": ["public repo","3min video","must use sponsor API"]}'

Output: audience profile (who to impress), sponsor EV ranking, winning
patterns, and requirement flags that feed plan.py/check.py.
"""

import sys
from collections import Counter
from common import emit, fail, read_json_arg

JUDGE_STYLES = {
    "investor": "lead with market + traction framing; wow = 'people will pay'",
    "engineer": "lead with the hard technical problem; wow = 'how did they do that'",
    "founder": "lead with scrappy speed + a real user story",
    "designer": "lead with the polished flow; wow = craft",
    "academic": "lead with rigor; wow = evaluation numbers",
}


def main():
    data = read_json_arg(sys.argv)
    if data is None or not isinstance(data, dict):
        fail('need --json {"event":..,"judges":[..],"sponsors":[..],"past_winners":[..],"requirements":[..]}')

    judges = data.get("judges", [])
    sponsors = data.get("sponsors", [])
    winners = data.get("past_winners", [])
    reqs = data.get("requirements", [])

    # Audience profile: which judge archetype dominates.
    styles = Counter(j.get("background", "unknown") for j in judges)
    dominant = styles.most_common(1)[0][0] if styles else "unknown"
    pitch = JUDGE_STYLES.get(dominant, "mixed panel — lead with a live demo, cover tech + impact")

    # Sponsor EV: a sponsor with an api + prize beats brand-name only.
    sponsor_rank = sorted(
        sponsors,
        key=lambda s: -(bool(s.get("api")) + bool(s.get("prize"))),
    )

    # Winning patterns from past winners' stated reasons.
    patterns = Counter()
    for w in winners:
        why = (w.get("why_won") or "").lower()
        if "live" in why and "demo" in why:
            patterns["live demo"] += 1
        for kw in ("real user", "real-world", "impact", "accessib", "polish",
                   "novel", "sponsor", "working", "hardware"):
            if kw in why:
                patterns[kw] += 1

    flags = []
    if not judges:
        flags.append("no judge data — even LinkedIn titles tell you what impresses them")
    if not winners:
        flags.append("no past winners analyzed — find last edition's top 3 on Devpost")
    if any("must" in r.lower() for r in reqs):
        flags.append("hard requirements present — wire them into check.py")

    emit({
        "status": "ok",
        "summary": f"audience={dominant}, {len(sponsors)} sponsors, {len(patterns)} winning patterns",
        "event": data.get("event"),
        "audience": {"dominant_judge_type": dominant, "mix": dict(styles),
                     "pitch_advice": pitch},
        "sponsor_ev": [{"name": s.get("name"), "has_api": bool(s.get("api")),
                        "prize": s.get("prize")} for s in sponsor_rank],
        "winning_patterns": dict(patterns.most_common()),
        "requirement_flags": flags,
        "rules": [
            "Optimize for the dominant judge type, but keep the demo legible to all.",
            "A sponsor prize with an API is usually the smallest field — evaluate it before grand prize.",
            "Patterns in past winners are the real rubric; the published one is a summary of them.",
        ],
    }, brief="--json-brief" in sys.argv)


if __name__ == "__main__":
    main()
