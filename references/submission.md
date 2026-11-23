# Submission checklist

Run through this at the top of the submission buffer, not the bottom.

**The submission page IS the product.** On Devpost, judges are *not required to test the project* — many score solely from text, images, and video. The page isn't paperwork; it's the thing being judged.

## README (the artifact judges actually open)

- [ ] One-line pitch at the top, no setup instructions before it
- [ ] Demo GIF or video above the fold
- [ ] Live URL if deployable, with "works in Chrome/Safari" note
- [ ] "Built in N hours" + team names
- [ ] Setup instructions that a stranger can run in <5 commands
- [ ] License file

## Devpost field map (fields teams miss)

- [ ] **"Built with" tags (25 max)** — tag the sponsor's tool/SDK explicitly; sponsor screeners filter on it
- [ ] **Video hard cutoff** — judges stop watching at the limit ("will not be reviewed beyond 3:00"); the wow can't live at 2:55
- [ ] **"Improvements during the hackathon" field** — on events allowing existing projects; it's your legal prior-work disclosure
- [ ] **No copyrighted music** in the video — a real DQ vector
- [ ] **Try-it-out links verified logged-out** — open every link in incognito before the form submits

## Claims → evidence

Every claim in the text links to proof (file, test, timestamped demo moment). "Real-time", "10k users", "end-to-end" with no evidence gets traced and discounted — see `integrity.md`.

## Video (if required)

- [ ] Under the limit (usually 2-4 min — check the rules, not your memory)
- [ ] Recorded on a clean machine, no auth walls, no loading spinners left in
- [ ] Narrated throughout, no copyrighted music, no dead air
- [ ] Audio clear enough to understand; subtitles if noisy
- [ ] Uploaded AND set to public/unlisted correctly

## The last hour

- [ ] Fill EVERY required field in the submission form — empty required fields = auto-reject
- [ ] Repo is public and the link works in an incognito window
- [ ] Submission confirmation screenshot saved
- [ ] If the platform has a "draft" vs "submitted" state, verify the real state
- [ ] Prior-work disclosure section in README (`integrity.md`) — undeclared reuse is a knockout at winner screening
- [ ] `verify.py --repo . --end <deadline>` — no giant-commit or post-deadline flags
