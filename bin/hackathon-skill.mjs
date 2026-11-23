#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tools = ["plan", "scope", "deadline", "check"];
const [, , tool, ...rest] = process.argv;

if (!tool || !tools.includes(tool)) {
  console.log(`hackathon-skill — usage: hackathon-skill <${tools.join("|")}> [args]
  plan      --hours 48 | --start ISO --end ISO [--team 2]
  scope     --json '{"hours_left":12,"features":[{name,est_h,demo_visible}]}'
  deadline  --end ISO [--block build]
  check     --json '{"rubric":{...},"team_max":4,"submission":[...],"ends":"ISO"}'`);
  process.exit(0);
}
const r = spawnSync("python3", [join(root, "scripts", `${tool}.py`), ...rest], { stdio: "inherit" });
process.exit(r.status ?? 1);
