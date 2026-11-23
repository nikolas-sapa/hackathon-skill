---
name: hackathon
version: 0.2.0
license: MIT
description: 'Plan and win a hackathon with any coding agent: decode the brief, score ideas against the judging rubric, cut MVP scope brutally, pace the clock, and write the submission. Use whenever the user mentions a hackathon, Devpost, DoraHacks, lablab, a judge rubric, demo day, or "we have 48 hours". Python 3.9+, stdlib only, offline.'
---

# hackathon-skill

A skill for coding agents that turns "we signed up for a hackathon" into a paced, rubric-aligned, demoable build. The agent reads this file once, then runs the scripts; the scripts do the arithmetic and the cutting, the agent does the building.

## Quick start

Every tool is `python3 <skill-dir>/scripts/<name>.py` and prints JSON. All accept `--json '<payload>'` or piped JSON, and `--json-brief` for a one-line summary.

| Situation | Tool | Input |
|---|---|---|
| Pre-event research | `recon.py` | `{"judges":[..],"sponsors":[..],"past_winners":[..],"requirements":[..]}` |
| "Did I miss anything in the rules" | `check.py` | parsed brief fields as JSON |
| Starting a hackathon | `plan.py` | `{"hours":48,"team_size":2}` or `--start/--end` ISO |
| Choosing between ideas | `idea.py` | `{"ideas":[{name,rubric_fit,demoability,feasibility,sponsor_fit}]}` |
| "What can I still ship" | `scope.py` | `{"hours_left":12,"features":[{name,est_h,demo_visible,critical_path}]}` |
| Mid-run clock check | `deadline.py` | `--end ISO --block build`; `--watch` for a live ticker |
| Before submitting | `score.py` | `{"rubric":{...},"self_scores":{...}}` |
| Final gate | `verify.py` | `--url URL --readme README.md --video demo.mp4` |

Then consult `references/` for the human-written judgment:
`recon-playbook.md` (judges/sponsors/past winners), `rubric-first.md`, `ideation-matrix.md`,
`cut-ladder.md`, `pivot.md` (when to abandon), `teammates.md` + `git-workflow.md` (coordination),
`demo-script.md` + `demo-reliability.md`, `judging-qa.md` (the 20 questions), `submission.md`,
`post-hackathon.md`. Templates live in `templates/` (submission skeleton, past-winners table, README).

## The workflow (follow in order, gates are hard)

1. **Recon.** Read `references/recon-playbook.md`, run the research lanes, feed findings into `recon.py`, then `check.py` on the brief. If `verdict` is `BLOCKED`, stop — building on a wrong assumption loses the event.
2. **Plan.** Run `plan.py`. Get the six-block schedule with gates. Do not start coding before `recon` and `ideate` gates pass.
3. **Ideate.** Max 3 ideas scored by `idea.py` against rubric and sponsor fit. Pick one, kill the rest.
4. **Spike.** Prove only the riskiest assumption, in the spike block only. Fail → pivot per `references/pivot.md`, never extend.
5. **Build.** One vertical slice end-to-end first. `scope.py` whenever the feature list grows. `deadline.py --watch` on a spare pane.
6. **Demo + submit.** `deadline.py --block demo_prep`, script per `references/demo-script.md`, rehearse Q&A per `references/judging-qa.md`. Then `score.py` your draft and `verify.py` the artifacts. Submit >=1h early.

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
