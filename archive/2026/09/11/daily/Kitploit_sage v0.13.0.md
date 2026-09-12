---
title: sage v0.13.0
url: https://kitploit.com/en/posts/github-gendigitalinc-sage-v0130
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:06.071719
---

# sage v0.13.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13825/e5f6ac990a5f63e4231f6c6cd8f91b9c7021b4611913477e99892d7951860409.gif)

New releaseSep 11, 2026

# sage v0.13.0

Lightweight Agent Detection & Response (ADR) layer for AI agents — guards commands, files, and web requests. Part of Gen Agent Trust Hub.

Share

# Sage

![Sage](https://assets.kitploit.com/production/public/readmes/13825/0be2e115c991561f3fe61f757fd6a79cd90f6afe3da79bf73b33674f0764798d.png)

**Safety for Agents** — Agent Detection & Response for AI coding assistants

---

![Sage blocking a dangerous command in Claude Code](https://assets.kitploit.com/production/public/readmes/13825/e5f6ac990a5f63e4231f6c6cd8f91b9c7021b4611913477e99892d7951860409.gif)

Sage is a lightweight security layer that protects AI agents from executing dangerous actions. It intercepts tool calls — shell commands, URL fetches, file writes — and checks them against multiple threat detection layers before they run.

> **Note:** Sage may appear under a different product name (e.g., Norton Sage, Avast Sage) depending on how it was installed. See [Branding](https://github.com/gendigitalinc/sage/blob/main/docs/branding.md) for details.

## Key Features

* **URL reputation** — cloud-based detection of malware, phishing, and scam URLs
* **Local heuristics** — 300+ YAML-based threat patterns for dangerous commands, suspicious URLs, credential exposure, and obfuscation
* **Prompt injection detection** — two-tier defense (heuristics + fine-tuned ML model) against injected instructions in fetched content. See [Prompt Injection](https://github.com/gendigitalinc/sage/blob/main/docs/prompt-injection.md)
* **Package supply-chain checks** — registry existence, file reputation, and age analysis for npm/PyPI packages
* **Plugin scanning** — scans installed plugins for threats at session start
* **AMSI integration** — Windows Antimalware Scan Interface support (Windows + WSL via PowerShell interop; no-op on macOS and non-WSL Linux)

## Quick Start

Visit **[ai.gendigital.com/sage](https://ai.gendigital.com/sage)** for the latest installation instructions, or use the platform-specific guides below.

**Claude Code** — [install guide](https://ai.gendigital.com/sage#install-claude-code) · requires [Node.js >= 18](https://nodejs.org/)

root@kitploit:~

```
/plugin marketplace add https://github.com/gendigitalinc/sage.git
/plugin install sage@sage
```

**Cursor** — [install guide](https://ai.gendigital.com/sage#install-cursor) · install the [Gen Sage](https://marketplace.cursorapi.com/items?itemName=Gen.sage-cursor) extension from the marketplace

**VS Code** — [install guide](https://ai.gendigital.com/sage#install-vscode) · install the [Gen Sage](https://marketplace.visualstudio.com/items?itemName=Gen.sage-vscode) extension from the marketplace

**OpenClaw** — [install guide](https://ai.gendigital.com/sage#install-openclaw) · install from npm

root@kitploit:~

```
openclaw plugins install @gendigital/sage-openclaw
```

**OpenCode** — install from npm by adding to `~/.config/opencode/opencode.json`:

root@kitploit:~

```
{
  "plugin": ["@gendigital/sage-opencode"]
}
```

See the [User Guide](https://github.com/gendigitalinc/sage/blob/main/docs/user-guide.md) for detailed instructions, configuration, and troubleshooting.

## Privacy

For privacy considerations, please refer to [Privacy](https://github.com/gendigitalinc/sage/blob/main/docs/user-guide.md#privacy).

## Documentation

| Document | Description |
| --- | --- |
| [User Guide](https://github.com/gendigitalinc/sage/blob/main/docs/user-guide.md) | Installation, usage, configuration, exceptions, platform guides, privacy, FAQ |
| [Developer Guide](https://github.com/gendigitalinc/sage/blob/main/docs/developer-guide.md) | Architecture, development setup, testing, threat rule format |
| [Prompt Injection](https://github.com/gendigitalinc/sage/blob/main/docs/prompt-injection.md) | ML + heuristic prompt injection detection |
| [Package Protection](https://github.com/gendigitalinc/sage/blob/main/docs/package-protection.md) | npm/PyPI supply-chain checks |
| [AMSI Scanning](https://github.com/gendigitalinc/sage/blob/main/docs/amsi-scanning.md) | Windows antimalware scanning via AMSI |
| [Plugin Scanning](https://github.com/gendigitalinc/sage/blob/main/docs/plugin-scanning.md) | Session-start plugin scanning |
| [Audit Log](https://github.com/gendigitalinc/sage/blob/main/docs/audit-log.md) | On-disk JSONL schema (entries, signals, content) |
| [MCP Server](https://github.com/gendigitalinc/sage/blob/main/docs/mcp.md) | Shared MCP server architecture |
| [Decision Pipeline](https://github.com/gendigitalinc/sage/blob/main/docs/decision-pipeline.md) | Signal sources, policy model, evaluation order |
| [Branding](https://github.com/gendigitalinc/sage/blob/main/docs/branding.md) | Product name configuration |

## Contributing

See [CONTRIBUTING.md](https://github.com/gendigitalinc/sage/blob/main/CONTRIBUTING.md) for development setup, coding conventions, and the threat rule contribution process.

## License

Copyright 2026 Gen Digital Inc.

* Source code: [Apache License 2.0](https://github.com/gendigitalinc/sage/blob/main/LICENSE)
* Threat detection rules (`threats/`): [Detection Rule License 1.1](https://github.com/gendigitalinc/sage/blob/main/threats/LICENSE)

[Read more](/en/tools/github/gendigitalinc/sage?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[Phishing Tools](/en/categories/phishing-tools)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Code Analysis](/en/categories/code-analysis)[Malware Analysis](/en/categories/malware-analysis)[Threat Intelligence](/en/categories/threat-intelligence)[Supply Chain Security](/en/categories/supply-chain-security)[Learning & Education](/en/categories/education)[AI Security](/en/categories/ai-security)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories