# OutageDeck for Codex and Claude Code

Check cloud and SaaS incidents before changing code. This marketplace installs the OutageDeck MCP server and a dependency-outage triage skill in Codex or Claude Code.

Public status checks are read-only, free, and require no account or API key. OutageDeck tracks 172 providers from their official status feeds and adds independent uptime history.

## Install in Codex

```sh
codex plugin marketplace add outagedeck/codex-plugins
codex
```

Run `/plugins`, choose the **OutageDeck** marketplace, install **OutageDeck**, and start a new session.

## Install in Claude Code

```sh
claude plugin marketplace add outagedeck/codex-plugins
claude plugin install outagedeck@outagedeck
```

Start a new session after installation.

## Install in OpenClaw

Install the dependency-free skill directly from its versioned first-party Git repository:

```sh
openclaw skills install git:outagedeck/triage-dependency-outages@v0.1.0
```

This path requires no ClawHub account, OutageDeck account, API key, local executable, or environment variable. [Inspect the exact v0.1.0 source and release notes](https://github.com/outagedeck/triage-dependency-outages/releases/tag/v0.1.0).

## Install the portable Agent Skill

For Codex, Claude Code, Cursor, GitHub Copilot, Windsurf, Gemini CLI, Cline, and other compatible agents:

```sh
npx skills add https://github.com/outagedeck/codex-plugins --skill triage-dependency-outages
```

[View the skill, install command, and security audit on skills.sh](https://www.skills.sh/outagedeck/codex-plugins/triage-dependency-outages). The full Codex or Claude Code plugin is recommended because it bundles the 14-tool MCP server; the portable skill falls back to OutageDeck's anonymous REST API for current status and incident evidence.

Try:

- “Before changing code, check AWS, Cloudflare, GitHub, and OpenAI.”
- “Is this 503 from my app or from a provider incident?”
- “Create a citable incident brief for the current Cloudflare outage.”
- “Compare GitHub and GitLab uptime over the last 30 days.”

## What is included

- `triage-dependency-outages`: a workflow that checks vendor evidence first, correlates incident timelines with the reported failure, and returns a bounded verdict plus next steps.
- `https://outagedeck.com/api/mcp`: 14 tools for current status, active incidents, incident timelines, uptime, provider search, and optional account alert management.

The public tools do not modify external state. Account tools require authorization and preserve the host's confirmation rules.

## Links

- [OutageDeck MCP documentation](https://outagedeck.com/developers/mcp?utm_source=github&utm_medium=repository&utm_campaign=codex_plugin)
- [Codex community Show and tell](https://github.com/openai/codex/discussions/37064)
- [Create a free vendor alert](https://outagedeck.com/account?utm_source=github&utm_medium=repository&utm_campaign=codex_plugin)
- [Plans](https://outagedeck.com/pricing?utm_source=github&utm_medium=repository&utm_campaign=codex_plugin)

Security reports: [hello@outagedeck.com](mailto:hello@outagedeck.com)
