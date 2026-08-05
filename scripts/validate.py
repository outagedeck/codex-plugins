#!/usr/bin/env python3

import json
import re
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "outagedeck"


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
manifest = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
claude_manifest = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
mcp = load_json(PLUGIN / ".mcp.json")
skill_path = PLUGIN / "skills" / "triage-dependency-outages" / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8")

assert marketplace["name"] == "outagedeck"
assert marketplace["plugins"][0]["name"] == manifest["name"] == "outagedeck"
assert claude_marketplace["name"] == "outagedeck"
assert claude_marketplace["plugins"][0]["name"] == "outagedeck"
assert claude_manifest["name"] == manifest["name"]
assert claude_manifest["version"] == manifest["version"]
assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])
assert manifest["skills"] == "./skills/"
assert manifest["mcpServers"] == "./.mcp.json"
assert (PLUGIN / manifest["interface"]["logo"]).is_file()
assert (PLUGIN / manifest["interface"]["composerIcon"]).is_file()
assert "[TODO" not in skill
assert skill.startswith("---\nname: triage-dependency-outages\ndescription: ")

server = mcp["mcpServers"]["outagedeck"]
assert server == {"type": "http", "url": "https://outagedeck.com/api/mcp"}

payload = json.dumps(
    {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}
).encode()
request = urllib.request.Request(
    server["url"],
    data=payload,
    headers={
        "Accept": "application/json, text/event-stream",
        "Content-Type": "application/json",
        "User-Agent": "outagedeck-codex-plugin-validation/0.1",
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=15) as response:
    tools_response = json.load(response)

tool_names = {
    tool["name"] for tool in tools_response["result"]["tools"]
}
required_tools = {
    "check_my_stack",
    "fetch",
    "get_incident_details",
    "get_provider_status",
    "get_uptime",
    "list_active_incidents",
    "search",
    "search_providers",
}
assert required_tools <= tool_names

print(
    f"Validated OutageDeck plugin {manifest['version']} with "
    f"{len(tool_names)} live MCP tools."
)
