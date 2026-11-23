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

console.log("ok — 6 assertions passed");
