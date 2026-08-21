---
title: agent-scan v0.6.0
url: https://kitploit.com/en/posts/github-snyk-agent-scan-v060
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:41.678293
---

# agent-scan v0.6.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/721/98fbbb9009fa00bb52906b85514664b3d4834bd558b2b9fb3bce959cfa87a4e8.png)

New releaseAug 20, 2026

# agent-scan v0.6.0

Security scanner for AI agents, MCP servers and agent skills.

Share

# Snyk Agent Scan

Discover and scan agent components on your machine for prompt injections
and vulnerabilities (including agents, MCP servers, skills).

> **Note: CLI output is experimental and subject to change**
>
> **Agent Scan v0.5.x (planned for deprecation)**
>
> The raw output of this CLI — including issue codes, field names, severity labels, and response structure — is experimental and may change without notice between releases. We do not recommend building production workflows that depend on specific CLI output fields or issue codes.
>
> **Agent Scan v0.6 and later**
>
> The raw output of this CLI — including risk indicator names, scores, field names, and response structure — is experimental and may change without notice between releases. We do not recommend building production workflows that depend on specific CLI output fields or risk names.
>
> If you are an enterprise customer using Snyk to manage agent security risk at scale, the CLI output may not reflect what is sent to and shown in the Evo platform. The underlying integration, discovery, and risk assessment that powers enterprise deployments is stable and supported — any changes will be communicated in line with standard Snyk product practices. Contact your account team for deployment guidance.

> **NEW** Read our [technical report on the emerging threats of the agent skill eco-system](https://github.com/snyk/agent-scan/blob/HEAD/.github/reports/skills-report.pdf) published together with Agent Scan 0.4, which adds support for scanning agent skills.

[![snyk-agent-scan](https://img.shields.io/pypi/v/snyk-agent-scan.svg)](https://pypi.python.org/pypi/snyk-agent-scan)
[![snyk-agent-scan license](https://img.shields.io/pypi/l/snyk-agent-scan.svg)](https://pypi.python.org/pypi/snyk-agent-scan)
[![snyk-agent-scan python version requirements](https://img.shields.io/pypi/pyversions/snyk-agent-scan.svg)](https://pypi.python.org/pypi/snyk-agent-scan)

### Agent Scan v0.5.x output

> [!WARNING]
> Agent Scan v0.5.x uses issue-code output. This CLI line is planned for deprecation.

![agent-scan-pretty](https://assets.kitploit.com/production/public/readmes/721/98fbbb9009fa00bb52906b85514664b3d4834bd558b2b9fb3bce959cfa87a4e8.png)

### Agent Scan v0.6 and later output

![Agent Scan v0.6 and later report showing scored MCP server and skill risks](https://raw.githubusercontent.com/snyk/agent-scan/HEAD/demo-v0.6.svg)

Agent Scan helps you discover all your installed agent components (harnesses, MCP servers, and skills) and scans them for common threats like prompt injections, sensitive data handling, or malware payloads hidden in natural language. Ignore analysis on skills by using `--no-skills`.

## Security Warning

> **⚠️ IMPORTANT: Scanning MCP configurations will execute the commands defined in them.**
>
> When Agent Scan scans an MCP configuration file, it starts the stdio MCP servers by executing the commands and arguments specified in the config. This is necessary to retrieve tool descriptions and perform security analysis.
>
> **Recommendations:**
>
> * **Run scans inside a sandbox** (Docker container, VM, or disposable environment) when evaluating untrusted or third-party MCP configs
> * **Review the consent prompt carefully** during interactive scans, it shows the exact command and arguments that will be executed for each server
> * **Use `--dangerously-run-mcp-servers`** only in trusted environments where you've verified all MCP server commands
>
> By default, Agent Scan requires explicit user consent (y/n) before starting each stdio MCP server during interactive runs. This gives you control over what gets executed on your system.

## Quick Start

Choose one of two ways to run Agent Scan:

1. **Run the Python package with `uvx`** using the instructions below.
2. **Download a standalone binary** for your platform from [GitHub Releases](https://github.com/snyk/agent-scan/releases). Releases also include the SBOM, checksums, signed checksums, and source code archives.

Before using either option:

1. **Sign up at [Snyk](https://snyk.io)** and get an API token from <https://app.snyk.io/account> (API Token → KEY → click to show).
2. **Set the token as an environment variable** before running any scan:

   root@kitploit:~

   ```
   export SNYK_TOKEN=your-api-token-here
   ```

### Run with `uvx`

Have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your system. Choose the instructions for your CLI version.

#### Agent Scan v0.5.x

The examples pin v0.5.17 as a concrete v0.5.x release:

root@kitploit:~

```
# Scan the whole machine
uvx [email protected]

# Scan a specific MCP configuration
uvx [email protected] ~/.vscode/mcp.json

# Scan a single agent skill
uvx [email protected] ~/path/to/my/SKILL.md

# Scan all Claude skills
uvx [email protected] ~/.claude/skills
```

> [!WARNING]
> v0.5.x uses issue-code output and the `2025-09-02` analysis API. This CLI line is planned for deprecation.

#### Agent Scan v0.6 and later

root@kitploit:~

```
# Scan the whole machine
uvx snyk-agent-scan@latest

# Scan a specific MCP configuration
uvx snyk-agent-scan@latest ~/.vscode/mcp.json

# Scan a single agent skill
uvx snyk-agent-scan@latest ~/path/to/my/SKILL.md

# Scan all Claude skills
uvx snyk-agent-scan@latest ~/.claude/skills
```

v0.6 and later use the risk-based output and the `2026-07-10` analysis API.

Both versions scan MCP servers, tools, prompts, resources, and skills, and automatically discover supported agent configurations such as Claude Code/Desktop, Cursor, Gemini CLI, and Windsurf.

### Run with a standalone binary

Download the binary for your operating system and architecture from the [latest GitHub Release](https://github.com/snyk/agent-scan/releases/latest). The release page also provides an SBOM (`sbom-<version>.json`), checksum files, and GitHub-generated source code archives. See [Verifying Standalone Binaries](#verifying-standalone-binaries) to verify your download.

### Agent Scan v0.5.x example run

[![Agent Scan v0.5 security vulnerabilities demo](https://raw.githubusercontent.com/snyk/agent-scan/HEAD/demo.svg)](https://asciinema.org/a/716858)

For the v0.6 risk-based output, see the v0.6 image at the top of this README.

## Highlights

* Auto-discover MCP configurations, agent tools, skills
* Scanning of Claude, Cursor, Windsurf, Gemini CLI, Amp, Amazon Q, and other agents.

### Agent Scan v0.5.x

* Detects [15+ distinct security risks](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md) across MCP servers and agent skills:
  + MCP: [Prompt Injection](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#E001), [Tool Poisoning](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#E001), [Tool Shadowing](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#E002), [Toxic Flows](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#ToxicFlows)
  + Skills: [Prompt Injection](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#E004), [Malware Payloads](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#E006), [Untrusted Content](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#W011), [Credential Handling](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#W007), [Hardcoded Secrets](https://github.com/snyk/agent-scan/blob/HEAD/docs/issue-codes.md#W008)

### ...