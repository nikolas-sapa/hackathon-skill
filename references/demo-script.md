# The 90-second winning demo script

Structure judges respond to, learned from demos that won. Total: 90s ±10s.

| Time | Beat | What you say |
|---|---|---|
| 0-10s | Problem | One sentence, concrete: "X people waste Y doing Z." |
| 10-20s | Our thing | "We built <name> — a <one-line>." Show the home screen. |
| 20-70s | The walk | ONE user journey, live. Happy path only. Narrate what the screen does, not how it works. |
| 70-85s | The wow | The single most impressive moment — a number, a reveal, a comparison. |
| 85-90s | Close | "Built in 48 hours with <stack>. It's live at <url>." |

## Rules

- **Live demo > video > slides.** If live is risky, record a video AND keep a GIF backup.
- One journey, not a feature tour. Judges see 40 demos; they remember the one they followed.
- Rehearse on a clean machine. If it doesn't run cold, it doesn't count.
- End with the thing, not the tech. "Here's X working" lands; "we used React" doesn't.
- For table judging (the common MLH format) see `booth-judging.md` — different game entirely.
- **Mark THE wow moment in the script.** Pitchers rush past it under nerves; write "PAUSE 2s" next to it.
- **Word budget ∝ rubric weight.** If demo is 40% of the rubric, ~40% of your words are the walkthrough. Don't spend half the pitch on a 10% criterion.
- **No tense hedging** — "trying to", "hope to", "would let users" reads unfinished. It's built or it isn't.
- **End with a CTA, not "thank you"** — "it's live at X, try it" beats applause-seeking.

## The appendix strategy (live pitching)

Keep the main pitch short. Build one backup slide/screen per expected Q&A question (`judging-qa.md`) — architecture diagram, comparable table, metrics. Judges fill in rubric categories during Q&A; an appendix slide is how you feed them the answer instead of improvising it.

## The video pitch (remote/async judging — the video IS the pitch)

For Devpost-style events judges aren't required to watch past the limit — and often don't finish it. Rules:

- Hard limit (usually 3 min); working product visible in the **first 30 seconds**.
- Give each rubric criterion a labeled beat — judges skim for their scoring sheet.
- Name sponsor APIs on-screen early; sponsor tracks pass/fail screen for it.
- Captions or large on-screen text — many watch muted.
- Video, README, and submission text tell the same story — judges cross-check.
- Narrated throughout — silence and background music read as filler. No copyrighted music; some platforms DQ for it.
- Cut loading screens and boilerplate tours — judges decide in the first 30s whether to keep watching.
- Every link shown works — a 404 in the video is a trust collapse.

## Length variants

| Length | Keep | Drop |
|---|---|---|
| 30s | problem 5s → demo 20s → close 5s | wow beat merged into demo |
| 90s | full table above | — |
| 3min | + architecture appendix + sponsor callout | second user journey |
| 5min | + challenges/what's next | never add a second demo |
