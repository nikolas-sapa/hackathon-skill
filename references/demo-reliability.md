# Demo reliability — nothing fails on stage twice

## The cold-start checklist (run at demo_prep start, not end)

- [ ] Fresh shell, fresh machine (or clean browser profile): does the path work with zero local state?
- [ ] Kill network-dependent pieces one at a time: which degrade gracefully, which crash?
- [ ] Screen brightness, font size, tab order, notifications off, Do Not Disturb on.
- [ ] Seed data loaded and identical between practice runs.

## Offline fallback ladder

1. **Live demo** — best. Requires the chain to actually work.
2. **Recorded video** — required even if live works; the venue Wi-Fi will betray someone.
3. **GIF in README** — the judges' fallback when your video link 404s.
4. **Screenshots** — the floor. If you only have this, `scope.py` already told you.

## The recorded video rules

- Record on the cleanest run of the day, not the last run.
- Show the happy path only. Editing out a spinner is fine; hiding a crash is not (judges ask).
- Under the limit — `verify.py --video demo.mp4 --max-video-min N` checks it.
- Hosted where it won't die: YouTube unlisted, Loom, or embedded in the repo.

## Judge self-serve (the demo after the demo)

Judges click your link days later, alone. Kill the ways that dies:

- **Free-tier sleep**: Supabase pauses idle projects, Render cold-starts ~50s, Railway sleeps. Set a keep-alive ping (cron hitting your own URL every 20 min) through judging week.
- **Auth walls**: if the app needs login, ship a **guest/demo mode** or seeded credentials printed in the README + on the landing page. A login screen = 0 points.
- **Re-wake before judging day**: cold-open the URL, run the demo path once yourself.
- `verify.py --url` checks the URL responds; YOU must check it in incognito — your session cookie hides walls.

## Common stage killers

| Killer | Pre-flight check |
|---|---|
| Auth wall on a fresh browser | open the URL in incognito |
| API quota exhausted during demos | keep a second key / mock toggle |
| Laptop sleeps during judging | power settings + charger at the table |
| Microphone muted on the recording | audio check before final take |
| Deploys still building | freeze deploys 1h before demo |
