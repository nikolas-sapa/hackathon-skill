# Stack decisions under a deadline

## The rule

**Use what you know.** A boring stack you can drive beats the perfect stack you have to learn. "Why this stack?" is judging question 10 — "it's what we know and it's fast" is a complete answer.

## Fastest stack by project type

| Building | Default pick | Why |
|---|---|---|
| AI/agent web app | Next.js + Supabase + Vercel | auth+db+deploy in hour 1, everyone knows it |
| API/ML backend demo | FastAPI + local model/API calls | Python speed, easy video-friendly endpoints |
| Mobile | React Native / Flutter | single codebase, hot reload for live iteration |
| Data/dashboard | Streamlit or Next.js + chart lib | visible output in minutes |
| Hardware-adjacent | ESP32/Arduino + serial → simple web UI | one sensor → one decision → one visible result |

## When to swap a piece

Only two reasons, ever:
1. **A sponsor prize requires it** — check `recon.py` sponsor EV first.
2. **The idea is impossible without it** — proven in the spike, not assumed.

## Never

- Learn a new framework during the event.
- Microservices, k8s, message queues, custom auth.
- "We'll decide the stack during ideation" — decide during recon, it's in `pre-hack.md`.

## Deploy rule

Deploy a hello-world in the first hour. A deploy pipeline that works at hour 1 works at hour 44; one that doesn't eats the submission buffer.
