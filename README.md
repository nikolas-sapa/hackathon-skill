# hackathon-skill

**Turn your coding agent into a hackathon teammate.** A SKILL.md + MCP server for Claude Code, Cursor, Codex and any agent that reads skills. It decodes the brief, paces the clock, cuts scope ruthlessly, and keeps you on the side of the rubric that wins.

> Why this exists: hackathons are not won by the best code. They're won by the team that picks the right idea, cuts the right features, and demos the right 90 seconds. Agents are great at building — this skill makes them great at *pacing*.

## What it does

| Tool | Question it answers |
|---|---|
| `plan` | "48 hours, 2 people — when do we ideate vs build vs submit?" |
| `scope` | "10 features, 8 hours left — what survives?" |
| `deadline` | "How much build time is actually left?" |
| `check` | "What did I miss in the rules that will DQ me?" |

Plus four human-written playbooks (`references/`) distilled from shipped hackathon entries: how to weight features against the judging rubric, the exact order to cut scope in, the 90-second demo script, and the submission checklist.

## Install

```bash
npx hackathon-skill --help        # CLI, stdlib Python 3 only
# or point your agent at skills/hackathon/SKILL.md
# or add mcp/server.py as an MCP stdio server
```

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
