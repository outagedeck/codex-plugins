# OutageDeck for Codex

Check cloud and SaaS incidents before changing code. This marketplace installs the OutageDeck MCP server and a dependency-outage triage skill in Codex.

Public status checks are read-only, free, and require no account or API key. OutageDeck tracks 172 providers from their official status feeds and adds independent uptime history.

## Install

```sh
codex plugin marketplace add outagedeck/codex-plugins
codex
```

Run `/plugins`, choose the **OutageDeck** marketplace, install **OutageDeck**, and start a new session.

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
- [Create a free vendor alert](https://outagedeck.com/account?utm_source=github&utm_medium=repository&utm_campaign=codex_plugin)
- [Plans](https://outagedeck.com/pricing?utm_source=github&utm_medium=repository&utm_campaign=codex_plugin)

Security reports: [hello@outagedeck.com](mailto:hello@outagedeck.com)
