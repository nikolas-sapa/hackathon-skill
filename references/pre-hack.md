# Pre-hack checklist — win before the clock starts

Do these the day(s) before. Every item is a failure other teams will hit at hour 3.

## Accounts + access (do 48h out)

- [ ] Devpost/event platform account + registration confirmed, entry QR saved offline
- [ ] GitHub repo created, team invited, CI-free template cloned locally
- [ ] Sponsor portals: claim API keys + credits EARLY — they run out by Saturday
- [ ] Deploy target: Vercel/Render/Fly account with a hello-world ALREADY deployed on your stack
- [ ] Discord/event Slack joined; announcements channel pinned

## Toolchain (night before)

- [ ] `git clone` + `npm install`/`pip install` run to completion on the venue laptop, offline if possible
- [ ] Docker images / model weights / large deps pre-downloaded — venue wifi is hostile
- [ ] Editor, browser, terminal configured; dark mode for dark rooms
- [ ] Phone hotspot tested — it's the fallback when venue wifi dies

## Team logistics

- [ ] Roles agreed per `teammates.md` before doors open
- [ ] Meeting point + first-3-hours plan written down
- [ ] Packing list — see `templates/packing-list.md` (power strip is the highest-EV item)

## Legal pre-flight

- [ ] Employer side-project clause checked (some companies require pre-approval)
- [ ] Rules scanned for prep prohibitions: no pre-built code, no pre-registered domain, open-source mandate — feed into `check.py`/`recon.py`
