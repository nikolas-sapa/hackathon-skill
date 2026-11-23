# Recon playbook — research the event before you build

Do this during the `recon` block. The agent runs the searches; you feed findings into `scripts/recon.py` for scoring.

## What to find (in order)

1. **Judges** — names → LinkedIn/GitHub. Classify each: investor, engineer, founder, designer, academic. The dominant type sets your pitch (recon.py computes this).
2. **Sponsors** — which have real APIs/SDKs and a dedicated prize. A sponsor prize is a smaller field than the grand prize.
3. **Past winners** — last edition's top 3. Read their repos and demo videos. Note: demo length, stack boring-ness, what the judges praised. This is the *real* rubric.
4. **Requirements** — submission format, video length, repo visibility, "must use X" clauses, disqualifiers (pre-existing code, team size, theme).
5. **Mechanics** — in-person vs remote, mentor access (see `mentors.md`), how demos are shown (live vs video vs booth — see `booth-judging.md`).

## IP/rules scan (do it in recon, not after winning)

Feed suspicious clauses into `recon.py` `requirements` — it flags them. Watch for:

- **Rights grabs**: "perpetual", "irrevocable", "assign", "transfer", "royalty-free license to organizers" — some events claim IP on entries.
- **Open-source mandates** — fine if expected, a surprise if not.
- **Employer conflicts** — some employers claim side-project IP or need pre-approval.
- **Required repo topic tags** — some sponsors auto-DQ entries missing their tag.
- **Pre-existing code rules** — what counts (boilerplate? libraries? last month's prototype?).

## Sources

- Devpost/DoraHacks/lablab event page + previous editions' galleries
- Sponsor docs pages (does the API actually exist and work?)
- Judges' recent talks/posts — what they've praised publicly is what they'll reward
- Organizer Discord/Slack — rules clarifications others already asked

## Output

Feed the result into `recon.py` then `check.py`. If the combined verdict is BLOCKED, do not ideate yet — a missing requirement is cheaper to find now than at hour 40.

## Parallel recon (if you have agent capacity)

Dispatch one researcher per lane (judges / sponsors / past winners / mechanics), each returning structured JSON matching recon.py's schema. Merge, score, done. A 4-lane recon takes minutes with agents and hours by hand.
