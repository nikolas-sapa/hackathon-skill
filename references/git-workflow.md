# Git + GitHub at hackathon speed

## The model

- **Trunk-based, always.** Everyone commits to `main`. No release branches, no develop.
- **Tiny PRs or straight to main.** On a 2-3 person team with 40 hours, review-blocking costs more than it catches. Rule: PRs only for risky shared-file changes; everything else pushes directly.
- **Owner per file area.** `teammates.md` — conflicts should be impossible by assignment, not resolved by merge skill.

## Issues = the checklist, not a tracker

Open issues for the demo-path tasks only ("live map renders", "video recorded"), one line each. Close = it works, not "code written". If an issue survives 2 standups, it's a scope problem — run `scope.py`.

Multi-agent teams: pin **Issue #1 as shared state** — plan, cuts, who's on what, current risks. Humans and agents both read/write it; it's the cheapest coordination layer that survives context resets.

## Comments and handoffs

- Write PR/commit messages for the teammate reading them at 3am: "map renders, markers not wired" not "progress".
- Tag the handoff explicitly: `@demo-owner: this screen is final — record it`.
- No discussions in comments longer than 2 replies. Voice/call it, then write the decision.

## What to skip entirely

- Branch protection rules, CI beyond "does it build", code review rituals, conventional commits, changelogs, version tagging.
- Rebasing — merge or re-commit; nobody has time to untangle a rebase at hour 41.

## The one rule

**The repo a judge opens must look intentional.** README is set early (demo owner), commit noise is fine — judges read the README and the demo, not your history.
