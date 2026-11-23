import { spawnSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const py = (s, args) => spawnSync("python3", [join(root, "scripts", s), ...args], { encoding: "utf8" });
const parse = r => JSON.parse(r.stdout);

// plan
let r = parse(py("plan.py", ["--hours", "48", "--team", "2"]));
assert.equal(r.status, "ok");
assert.equal(r.schedule.length, 6);
assert.ok(r.usable_hours > 20 && r.usable_hours < 40);

// scope
r = parse(py("scope.py", ["--json", JSON.stringify({
  hours_left: 10,
  features: [
    { name: "auth", est_h: 3, demo_visible: false },
    { name: "live map", est_h: 4, demo_visible: true },
    { name: "export", est_h: 2, demo_visible: false },
  ],
})]));
assert.equal(r.status, "ok");
assert.ok(r.keep.some(k => k.name === "live map"));

// deadline
r = parse(py("deadline.py", ["--end", "2099-01-01T00:00"]));
assert.equal(r.status, "ok");
assert.ok(r.hours_left > 0);

// check
r = parse(py("check.py", ["--json", JSON.stringify({ rubric: { demo: 50, tech: 50 }, team_max: 4, submission: ["github"], ends: "2099-01-01" })]));
assert.equal(r.verdict, "READY");
r = parse(py("check.py", ["--json", "{}"]));
assert.equal(r.verdict, "BLOCKED");

// recon
r = parse(py("recon.py", ["--json", JSON.stringify({
  judges: [{ name: "a", background: "investor" }, { name: "b", background: "investor" }],
  sponsors: [{ name: "S1", api: true, prize: "$5k" }, { name: "S2" }],
  past_winners: [{ name: "w", why_won: "live demo, real users" }],
  requirements: ["public repo", "must use sponsor API"],
})]));
assert.equal(r.audience.dominant_judge_type, "investor");
assert.equal(r.sponsor_ev[0].name, "S1");
assert.equal(r.winning_patterns["live demo"], 1);

// idea
r = parse(py("idea.py", ["--json", JSON.stringify({ ideas: [
  { name: "a", rubric_fit: 4, demoability: 5, feasibility: 3, sponsor_fit: 2 },
  { name: "b", rubric_fit: 5, demoability: 3, feasibility: 4, sponsor_fit: 4 },
] })]));
assert.equal(r.winner.name, "b");

// score
r = parse(py("score.py", ["--json", JSON.stringify({
  rubric: { demo: 40, technical: 35, impact: 25 },
  self_scores: { demo: 7, technical: 8, impact: 5 },
})]));
assert.equal(r.weakest_criterion, "impact"); // 12.5 pts available vs demo's 12

// verify (readme only, offline-safe)
r = spawnSync("python3", [join(root, "scripts", "verify.py"), "--readme", join(root, "README.md")], { encoding: "utf8" });
assert.ok(["SHIP", "WARN"].includes(JSON.parse(r.stdout).verdict));

console.log("ok — 13 assertions passed");
