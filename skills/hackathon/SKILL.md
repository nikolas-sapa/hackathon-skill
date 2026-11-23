---
name: hackathon
description: 'Plan and win a hackathon with any coding agent: decode the brief, score ideas against the judging rubric, cut MVP scope brutally, pace the clock, and write the submission. Use whenever the user mentions a hackathon, Devpost, DoraHacks, lablab, a judge rubric, demo day, or "we have 48 hours". Python 3.9+, stdlib only, offline.'
---

# hackathon-skill

A skill for coding agents that turns "we signed up for a hackathon" into a paced, rubric-aligned, demoable build. The agent reads this file once, then runs the scripts; the scripts do the arithmetic and the cutting, the agent does the building.

## Quick start

Every tool is `python3 <skill-dir>/scripts/<name>.py` and prints JSON. All accept `--json '<payload>'` or piped JSON, and `--json-brief` for a one-line summary.

| Situation | Tool | Input |
|---|---|---|
| Starting a hackathon | `plan.py` | `{"hours":48,"team_size":2}` or `--start/--end` ISO |
| "What can I still ship" | `scope.py` | `{"hours_left":12,"features":[{name,est_h,demo_visible,critical_path}]}` |
| Mid-run clock check | `deadline.py` | `--end ISO --block build` |
| "Did I miss anything in the rules" | `check.py` | parsed brief fields as JSON |

Then consult `references/` for the human-written judgment: `rubric-first.md` (how to weight features), `cut-ladder.md` (what to delete first), `demo-script.md` (the 90-second winner template), `submission.md` (README + video checklist).

## The workflow (follow in order, gates are hard)

1. **Recon.** Run `check.py` on whatever the brief gives you. If `verdict` is `BLOCKED`, stop and fill the gap — building on a wrong rubric assumption loses the event.
2. **Plan.** Run `plan.py`. Get the six-block schedule with gates. Do not start coding before `recon` and `ideate` gates pass.
3. **Ideate.** Max 3 ideas, scored against rubric weights and sponsor fit (see `references/ideation-matrix.md`). Pick one, kill the rest.
4. **Spike.** Prove only the riskiest assumption, in the spike block only. Fail → pivot, never extend.
5. **Build.** One vertical slice end-to-end first. `scope.py` whenever the feature list grows.
6. **Demo + submit.** Run `deadline.py --block demo_prep`. Script the 90-second demo from `references/demo-script.md`. Submit >=1h early.

## Non-negotiables baked into the tools

- **Rubric-first**: every feature earns its place against judging weights, not "cool factor".
- **Demo-visible beats correct**: a feature judges can't see is a feature you didn't build.
- **Reserve is sacred**: `plan.py` carves out sleep + submission buffer before a single build hour is counted.
- **Cut, don't defer**: `scope.py` deletes features from the plan; they do not "come back later".
- **Submit early**: last-hour submission failures are the single most common way to lose a won hackathon.

## What this skill does NOT do

- It does not generate your app — it paces and constrains the agent that does.
- It does not replace reading the rules — `check.py` makes missing rules loud, not optional.
- No telemetry, no network, no API keys. Everything runs on your machine.
