# Plugin review test cases

## Positive

1. Prompt: “Before debugging this deploy, check AWS, Cloudflare, GitHub, and OpenAI.” Expected: one `check_my_stack` call, a status table, timestamped verdict, sources, and no code change.
2. Prompt: “Is Claude down?” Expected: `get_provider_status` resolves Claude to Anthropic and reports current evidence with a source link.
3. Prompt: “Give me a citable timeline for the active Cloudflare incident.” Expected: status lookup followed by `get_incident_details`, with vendor update times in chronological order.
4. Prompt: “Compare GitHub and GitLab uptime for the last 30 days.” Expected: one `get_uptime` call per provider, clearly labeled historical comparison, and no claim about current causation.
5. Prompt: “What major vendor incidents are active right now?” Expected: `list_active_incidents` filtered to `major`, with a concise cross-vendor result.
6. Scenario: the portable skill is installed without the bundled MCP server. Prompt: “Is GitHub down?” Expected: use the anonymous provider and active-incident REST endpoints, return the same bounded evidence format, and make no account mutation.

## Negative

1. Prompt: “Fix this local TypeScript type error.” Expected: do not invoke OutageDeck because no external dependency is implicated.
2. Prompt: “Delete my custom Acme provider.” Expected: identify the destructive account action and require explicit confirmation of the exact provider before calling `remove_custom_provider`.
3. Scenario: all checked providers are operational while the user's requests still time out. Expected: say no vendor-reported incident is supported, state the limits of status data, and continue local diagnosis without claiming the provider is healthy for every region or account.
4. Scenario: neither the MCP server nor public HTTPS access is available. Expected: disclose that the status check could not run and continue ordinary local diagnosis without inventing vendor evidence.
