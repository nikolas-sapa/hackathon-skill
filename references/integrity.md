# Integrity audit — survive the cheating check

Winners get screened. MLH organizers run an explicit cheating check on every winning project, and modern judges trace claims to code. Pass it by construction, not by luck.

## The red flags organizers check (inverted — fix before submit)

- **One giant initial commit** — looks like pre-built work imported at hour 1. Commit progressively from the start; a commit every working slice is your alibi.
- **Commits after submissions close** — judges diff timestamps vs the deadline. Freeze the repo at submit; polish goes in a branch or the Devpost text, not post-deadline pushes.
- **README mentions a different event** — recycled repo smell. One README, one event, correct name.
- **Video/screenshots timestamped outside the event window** — record inside the window; check file metadata before upload.
- **Same project on your Devpost history** — resubmitting an old project is a DQ at most events. Pivot it hard or disclose.
- **Solo output way above plausible solo velocity** — log AI tool usage (below) so the volume is explainable.

## Claim tracing — "no quote, no score"

Judges increasingly verify claims by tracing them to code. Before submit:

1. List every claim in README + Devpost text ("real-time", "end-to-end encrypted", "handles 10k req/s").
2. Link each to evidence: file path, test, or a timestamped demo moment. No evidence → soften or delete the claim.
3. A claim judges can't verify reads as inflated — verified claims compound credibility.

## Prior-work disclosure (do it in the README)

Some events require it; all respect it. Add a section — JPHACKS mandates this format:

```md
### Built during this hackathon
- `src/agent/router.py` — routing engine (all commits in window)
- `src/ui/` — interface (from scratch)

### Pre-existing work used
- `lib/parser/` — our parser from June, reused per rules §4.2
- `vendor/sdk/` — sponsor SDK, unmodified
```

Undeclared prior work found by a judge is a knockout. Declared prior work is usually legal and always credible.

## AI-tool disclosure log

Teams increasingly face "did an AI write this?" Keep a running note from hour 0: which tools (Claude Code, Cursor, Copilot), which files/features they generated, and which parts are hand-built. If asked, precise honesty ("agent built the parser and tests, we designed the routing logic") beats a defensive "we wrote it ourselves" that unravels under "then explain line 40".
