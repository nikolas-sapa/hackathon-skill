#!/usr/bin/env python3
"""MCP server exposing hackathon-skill tools over stdio JSON-RPC.

Tools: plan, scope, deadline, check — same JSON payloads as the CLI scripts.
Run: python3 mcp/server.py
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

TOOLS = {
    "plan": {
        "description": "Generate a hackathon schedule from hours or start/end ISO.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "hours": {"type": "number"},
                "start": {"type": "string"},
                "end": {"type": "string"},
                "team_size": {"type": "integer"},
            },
        },
    },
    "scope": {
        "description": "Cut a feature list to fit remaining hours.",
        "inputSchema": {
            "type": "object",
            "required": ["hours_left", "features"],
            "properties": {
                "hours_left": {"type": "number"},
                "features": {"type": "array", "items": {"type": "object"}},
            },
        },
    },
    "deadline": {
        "description": "Time left + advice, given --end ISO and optional --block.",
        "inputSchema": {
            "type": "object",
            "required": ["end"],
            "properties": {"end": {"type": "string"}, "block": {"type": "string"}},
        },
    },
    "check": {
        "description": "Audit a parsed hackathon brief for missing critical fields.",
        "inputSchema": {"type": "object"},
    },
}


def run_tool(name, args):
    script = SCRIPTS / f"{name}.py"
    if name in ("plan", "deadline"):
        cmd = [sys.executable, str(script)]
        for k, v in args.items():
            cmd += [f"--{k.replace('_','-')}", str(v)]
    else:
        cmd = [sys.executable, str(script), "--json", json.dumps(args)]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if p.returncode != 0:
        return {"content": [{"type": "text", "text": p.stderr or p.stdout}]}
    return {"content": [{"type": "text", "text": p.stdout}]}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        req = json.loads(line)
        rid = req.get("id")
        method = req.get("method")

        if method == "initialize":
            resp = {"protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "hackathon-skill", "version": "0.1.0"}}
        elif method == "tools/list":
            resp = {"tools": [{"name": n, **t} for n, t in TOOLS.items()]}
        elif method == "tools/call":
            p = req.get("params", {})
            resp = run_tool(p.get("name"), p.get("arguments", {}))
        elif method == "ping":
            resp = {}
        else:
            resp = {"error": {"code": -32601, "message": f"unknown method {method}"}}

        if rid is not None:
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": resp}))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
