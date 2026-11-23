# Teammates — humans + agents on one clock

## Team formation (before the event)

Cover the four roles or accept the gap explicitly: **builder / designer / pitcher / integrator** (the one who makes pieces talk). A team of 4 builders demos badly; a team of 4 non-builders doesn't demo at all.

- Vet on work ethic, not skill. Ask "what did you ship last month?" — the answer filters better than any resume.
- 2-4 people cap; more = coordination eats the prize.
- Post `templates/team-up-post.md` in the event Discord/Devpost participants tab early — good people get claimed fast.
- Fill `templates/team-profile.md` in hour 0 — the skill inventory drives role assignment *and* idea constraints (don't pick an idea nobody can build).
- Lock idea + roles in the first hour; open-ended "let's see" teams churn.

## Roles (assign during recon, not mid-build)

| Role | Owner | Job |
|---|---|---|
| Driver | best builder | the core happy path, uninterrupted |
| Scope cop | 1 person | runs `scope.py` on every new idea, says no |
| Demo owner | NOT the driver | video script, README, submission fields, from hour ~60% — **Devpost draft created by hour 2** and filled progressively |
| Recon lead | fastest reader | judges, sponsors, past winners during ideation |

Solo + agent: you are demo owner and scope cop; the agent is the driver.

## Division rules

- **File-area ownership, not feature ownership.** Two people editing the same file in hour 30 is how merges eat a deadline.
- **Agents parallelize research, not architecture.** Dispatch recon lanes freely; keep one mind on the core path.
- **The demo owner starts early.** The submission form, README skeleton, and video template exist by 60% elapsed — they get filled as features land.

## Standups

Every 4 hours, 3 minutes, three questions:

1. What works end-to-end right now?
2. What's the current biggest risk to a working demo?
3. What got cut since last standup? (If nothing, something's wrong.)

## Communication under time pressure

- Decide in the open, once. A decision revisited in hour 35 is a scope explosion.
- "Almost done" means it runs. If it doesn't run, it's not started.
- Cut announcements beat status reports: "cut auth, map still on" tells everyone what matters.
