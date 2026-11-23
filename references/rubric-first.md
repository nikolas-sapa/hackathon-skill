# Rubric-first thinking

Winning hackathon entries are not the best engineering. They are the best **rubric scores per hour spent**.

## How to weight features

Given a rubric like `{technical:40, impact:30, demo:30}`:

- A feature that only raises `technical` scores gets `0.4 * hours-to-value`. A feature that raises `demo` gets `0.3 * htv` AND makes `technical` legible (judges can't score what they can't see).
- Anything below ~0.5 rubric points per hour is cut by `scope.py` unless it is critical-path.

## Reading an absent rubric

If `check.py` reports `rubric` missing, assume the standard weighting used across Devpost/DoraHacks/lablab events:

| Criterion | Typical weight |
|---|---|
| Working demo / live product | 30-40% |
| Technical depth | 25-35% |
| Impact / originality | 15-25% |
| Pitch / presentation | 10-15% |

Optimize for demo + technical, because impact and pitch are both scored *through the demo*.

## Sponsor tracks

If `check.py` reports sponsor APIs, treat each as a sub-rubric:
- Using the sponsor's actual API/SDK in a visible way usually beats a generic win.
- A sponsor track prize is often easier than the grand prize because the field is smaller.
- Do NOT stack sponsor features into one app; each sponsor track usually wants a different demo.
