# Mock judging — rehearse against a hostile panel, not a mirror

Reading `judging-qa.md` isn't rehearsal. Winning teams run at least one full simulation where someone (or an agent) plays the panel and tries to break the pitch.

## The protocol (30 min, during demo_prep)

1. **Cast the panel** — use recon.py's judge mix. Founder-heavy → simulate a fast, skeptical founder. Investor-heavy → simulate a "where's the business" VC. Engineer-heavy → simulate someone who wants the code open.
2. **Round 1: cold demo** — the pitcher does the full 90-second script with zero warm-up. Panel takes notes, doesn't interrupt. This catches the "we only rehearsed in pieces" failure.
3. **Round 2: hostile Q&A** — 10 minutes. The panel's job is to find the crack, not to be polite:
   - Interrupt mid-answer if it drags past 20s.
   - Ask the same question twice, differently — inconsistent answers lose.
   - Go for the trap questions (`judging-qa.md` §Trap) first, then improvise: "show me", "what's the moat", "why not just use X".
   - Stay in character when the pitcher appeals to effort. Judges don't grade effort.
4. **Round 3: patch** — every fumble gets one of three fixes: tighten the answer, move the fact earlier into the pitch, or accept it and script a graceful "don't know, would check X". Then run the failed questions once more.
5. **Timed runs** — run the pitch against a timer at least twice. If the 90s version drifts to 2:10, the script is too long — cut a beat, don't talk faster.

## Agent as the panel

Agents make better hostile judges than teammates — teammates pull punches. Prompt the agent with the rubric + your submission draft + the judge types from recon, and instruct it to find the weakest point. Run the transcript through `score.py` self-scores after each round; the weakest criterion tells you what the panel will attack.

## Failure signals during simulation (fix before judges find them)

- Pitcher can't answer "who built what" precisely → authorship gaps, rehearse it.
- Demo needs a 10s apology before it starts → reliability problem, see `demo-reliability.md`.
- Team disagrees with each other in front of the panel → never visible; decide the line privately.
- Answer to a trap question starts with "actually..." → you're correcting the judge. Reframe as agreement + differentiation.
