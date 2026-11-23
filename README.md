# hackathon-skill

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![CI](https://github.com/nikolas-sapa/hackathon-skill/actions/workflows/test.yml/badge.svg)](https://github.com/nikolas-sapa/hackathon-skill/actions)
[![skill](https://img.shields.io/badge/agent--skill-SKILL.md-006bff)](skills/hackathon/SKILL.md)
[![MCP](https://img.shields.io/badge/MCP-stdio-green)](mcp/server.py)

**Turn your coding agent into a hackathon teammate.** A SKILL.md + MCP server for Claude Code, Cursor, Codex and any agent that reads skills. It decodes the brief, paces the clock, cuts scope ruthlessly, and keeps you on the side of the rubric that wins.

> Why this exists: hackathons are not won by the best code. They're won by the team that picks the right idea, cuts the right features, and demos the right 90 seconds. Agents are great at building — this skill makes them great at *pacing*.

![demo](demo.gif)

## What it does

| Tool | Question it answers |
|---|---|
| `recon` | "Who are the judges, which sponsor prize is easiest, what do past winners have in common?" |
| `check` | "What did I miss in the rules that will DQ me?" |
| `plan` | "48 hours, 2 people — when do we ideate vs build vs submit?" |
| `idea` | "3 ideas on the table — which one do we kill last?" |
| `scope` | "10 features, 8 hours left — what survives?" |
| `deadline` | "How much build time is actually left?" (`--watch` = live countdown ticker) |
| `score` | "If judges scored us right now, where do we bleed points?" |
| `verify` | "Does the URL load, the video fit the limit, the README sell it?" |

Plus twelve human-written playbooks (`references/`) distilled from shipped hackathon entries: the recon playbook (judges, sponsors, past winners), rubric weighting, the ideation matrix, the exact order to cut scope in, when to pivot, teammate + git coordination, the 90-second demo script, demo reliability, the 20 judging questions, submission checklist, and the post-hackathon playbook. Templates in `templates/` (submission skeleton, past-winners analysis, README).

## Install

```bash
npx skills add nikolas-sapa/hackathon-skill      # any agent: Claude Code, Cursor, Codex, Gemini, 50+ hosts
./install.sh                                   # local clone: detects harness dirs and installs
npx hackathon-skill plan --hours 48            # CLI only, stdlib Python 3
```

| Harness | Command |
|---|---|
| Claude Code | `/plugin marketplace add nikolas-sapa/hackathon-skill` then `/plugin install hackathon-skill` |
| Cursor | `npx skills add nikolas-sapa/hackathon-skill` |
| Codex | `codex plugin marketplace add nikolas-sapa/hackathon-skill --sparse .claude-plugin` |
| Gemini CLI | `gemini extensions install https://github.com/nikolas-sapa/hackathon-skill` |
| Grok | `grok plugin install nikolas-sapa/hackathon-skill` |
| MCP client | add `python3 mcp/server.py` as a stdio server |

No cloud, no API keys, no telemetry. Everything runs on your machine.

## Example

```bash
python3 scripts/plan.py --hours 48 --team 2
# → recon (1.9h) → ideate (4.8h) → spike (3.2h) → build (18.2h) → demo_prep (3.2h) → submit (1.6h)

python3 scripts/scope.py --json '{"hours_left":10,"features":[
  {"name":"auth","est_h":3,"demo_visible":false},
  {"name":"live map","est_h":4,"demo_visible":true}]}'
# → keep live map (demo-visible), keep auth only if it fits, else cut
```

## Design principles

- **Rubric-first**: features earn hours against judging weights, not vibes.
- **Demo-visible beats correct**: if judges can't see it, it doesn't count.
- **Cut, don't defer**: cut features leave the plan; they don't lurk in a backlog.
- **The buffer is sacred**: sleep + submission time is carved out before a single build hour exists.

## License

MIT

## Why agents win hackathons with this

Left alone, an agent spends hour 1 picking a stack, hour 6 on auth, and hour 47 discovering the submission needs a video. This skill front-loads the decisions humans learned the hard way: decode the rubric first, cap ideation, spike only the risk, and protect the submission buffer.
