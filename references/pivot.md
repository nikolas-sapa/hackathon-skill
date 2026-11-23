# Pivot — when and how to abandon the idea

A pivot that works beats a sunk-cost idea that demos as smoke.

## Hard thresholds

- **Spike block ends with no proof** → pivot to idea #2. Non-negotiable; this is what the spike exists for.
- **>60% of usable time gone, nothing runs end-to-end** → pivot to a radically smaller version of the same idea (not a new idea — a new idea at 60% is a restart, and restarts lose).
- **A hard requirement turns out to be impossible** (API doesn't do what docs claimed) → pivot immediately; this is a recon failure, not a build failure.

## Soft signals (one = warning, two = pivot)

- The demo path keeps "almost working" for 2 consecutive standups.
- The riskiest assumption is still unproven after the spike block.
- The team can't explain the idea in one sentence without qualifiers.
- You're building features to hide that the core doesn't work.

## How to pivot without losing the time

1. **Keep the shell, swap the core.** UI, README skeleton, deployment, demo video template all survive a pivot. Only the middle changes.
2. **Pivot toward the demo, not away from the tech.** Pick the version with the most visible result, even if technically simpler.
3. **Announce it as a cut, not a failure.** "We're shipping the map view, not the routing engine" — teams spiral when pivots feel like defeat.
4. **Update `plan.py` output once.** Re-run the plan with remaining hours; do not re-plan more than once.
