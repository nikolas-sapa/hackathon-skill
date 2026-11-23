#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tools = ["plan", "scope", "deadline", "check", "recon", "idea", "score", "verify"];
const [, , tool, ...rest] = process.argv;

if (!tool || !tools.includes(tool)) {
  console.log(`hackathon-skill — usage: hackathon-skill <${tools.join("|")}> [args]
  plan      --hours 48 | --start ISO --end ISO [--team 2]
  scope     --json '{"hours_left":12,"features":[{name,est_h,demo_visible}]}'
  deadline  --end ISO [--block build] [--watch]
  check     --json '{"rubric":{...},"team_max":4,"submission":[...],"ends":"ISO"}'
  recon     --json '{"judges":[..],"sponsors":[..],"past_winners":[..]}'
  idea      --json '{"ideas":[{name,rubric_fit,demoability,feasibility,sponsor_fit}]}'
  score     --json '{"rubric":{...},"self_scores":{...}}'
  verify    --url URL [--readme README.md] [--video f.mp4 --max-video-min 3]`);
  process.exit(0);
}
const r = spawnSync("python3", [join(root, "scripts", `${tool}.py`), ...rest], { stdio: "inherit" });
process.exit(r.status ?? 1);
