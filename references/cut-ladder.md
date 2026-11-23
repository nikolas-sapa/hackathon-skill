# The cut ladder — what to delete first

When `scope.py` says you're over budget, cut in this order. Each rung is a place hackathon projects die.

1. **Auth, profiles, settings** — judges don't care. Hardcode a user.
2. **Onboarding, empty states, edge-case handling** — only the happy path is on stage.
3. **The second feature** — one great demo beats two good ones.
4. **Polish on the backend** — logging, tests, type coverage, refactors.
5. **The "clever" infrastructure** — queues, caching layers, microservices, auth providers.
6. **Visual polish beyond legibility** — a clean, simple UI beats a half-finished fancy one.
7. **The risky integration** — if it isn't proven in the spike, it's already cut; you just haven't admitted it.

## What never gets cut

- The 90-second demo path, cold-start to working screen.
- Whatever makes the rubric's top-weighted criterion visible.
- The submission buffer. `deadline.py` will scream at you; listen.
