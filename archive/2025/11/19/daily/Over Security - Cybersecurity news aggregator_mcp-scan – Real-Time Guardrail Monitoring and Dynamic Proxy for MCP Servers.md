---
title: mcp-scan – Real-Time Guardrail Monitoring and Dynamic Proxy for MCP Servers
url: https://www.darknet.org.uk/2025/11/mcp-scan-real-time-guardrail-monitoring-and-dynamic-proxy-for-mcp-servers/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-19
fetch_date: 2025-11-20T03:09:35.878405
---

# mcp-scan – Real-Time Guardrail Monitoring and Dynamic Proxy for MCP Servers

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# mcp-scan – Real-Time Guardrail Monitoring and Dynamic Proxy for MCP Servers

November 17, 2025

Views: 228

mcp-scan is a security tool from Invariant Labs that can run as a static scanner or as a dynamic proxy between agents and Model Context Protocol (MCP) servers. In proxy mode it sits in the traffic path, logging and enforcing guardrails on tool calls in real time, so both red teams and defenders can see precisely how agents use MCP tools and where prompt injection or tool abuse appears.

![mcp-scan - Real-Time Guardrail Monitoring and Dynamic Proxy for MCP Servers](https://www.darknet.org.uk/wp-content/uploads/2025/11/mcp-scan-Real-Time-Guardrail-Monitoring-and-Dynamic-Proxy-for-MCP-Servers-640x427.jpg)

## Overview

MCP provides a structured way for AI agents to talk to external tools and data sources, but those tools often sit behind opaque configuration files and hidden network flows. Misconfigured MCP servers can expose shell access, code execution, data exfiltration paths, or stealthy prompt-injection chains. mcp-scan addresses this by offering two modes:

* **Scan mode** to inspect MCP configurations on disk and highlight risky tool definitions.
* **Proxy mode** to intercept and monitor live MCP traffic between an agent and its servers.

Where earlier tools like [mcp-scanner](https://www.darknet.org.uk/2025/10/mcp-scanner-python-mcp-scanner-for-prompt-injection-and-insecure-agents/) focus on batch scanning of endpoints and configs, mcp-scan adds continuous, real-time visibility into agent behaviour.

## Features

* **Automatic MCP discovery**: locates MCP client and server configs for common agent environments and scans them for risky settings.
* **Prompt-injection and tool-poisoning checks**: inspect tool definitions and flows that may allow untrusted prompts or malicious tools to influence the agent.
* **Dynamic proxy mode**: runs as a man-in-the-middle, relaying traffic while logging every tool invocation, argument, and response.
* **Guardrail policies**: use YAML-defined rules to block or allow tool calls, detect secrets and PII, and filter tool output by content patterns.
* **Audit-ready logging**: records traffic and guardrail events for later investigation, hunting, and replay.

## Installation

mcp-scan is distributed as a simple CLI. The project documentation shows installation via package runners so that you can use it without a complete local build. Example commands:

# Run via uv
uvx mcp-scan@latest
# Or via npx
npx mcp-scan@latest

|  |  |
| --- | --- |
| 1  2  3  4  5 | # Run via uv  uvx mcp-scan@latest    # Or via npx  npx mcp-scan@latest |

Check the repository README for the latest installation options and platform notes before running it in production.

## Usage

mcp-scan supports both offline scanning and live proxying. Typical patterns include:

# To scan a particular MCP server configuration, for example, a VS Code MCP config, you can run:
mcp-scan ~/.vscode/mcp.json

|  |  |
| --- | --- |
| 1  2 | # To scan a particular MCP server configuration, for example, a VS Code MCP config, you can run:  mcp-scan ~/.vscode/mcp.json |

These options are available for all commands:

--storage-file FILE Path to store scan results and whitelist information (default: ~/.mcp-scan)
--base-url URL Base URL for the verification server
--verbose Enable detailed logging output
--print-errors Show error details and tracebacks
--full-toxic-flows Show all tools that could take part in toxic flow. By default only the top 3 are shown.
--json Output results in JSON format instead of rich text

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | --storage-file FILE    Path to store scan results and whitelist information (default: ~/.mcp-scan)  --base-url URL         Base URL for the verification server  --verbose              Enable detailed logging output  --print-errors         Show error details and tracebacks  --full-toxic-flows     Show all tools that could take part in toxic flow. By default only the top 3 are shown.  --json                 Output results in JSON format instead of rich text |

Guardrails are defined in YAML and attached to specific client/server combinations. A simplified example:

&lt;client-name>: # your client's shorthand (e.g., cursor, claude, windsurf)
&lt;server-name>: # your server's name according to the mcp config (e.g., whatsapp-mcp)
guardrails:
secrets: block # block calls/results with secrets
custom\_guardrails:
- name: "Filter tool results with 'error'"
id: "error\_filter\_guardrail"
action: block # or just 'log'
content: |
raise "An error was found." if:
(msg: ToolOutput)
"error" in msg.content

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | &lt;client-name>:  # your client's shorthand (e.g., cursor, claude, windsurf)  &lt;server-name>:  # your server's name according to the mcp config (e.g., whatsapp-mcp)  guardrails:  secrets: block # block calls/results with secrets    custom\_guardrails:  - name: "Filter tool results with 'error'"  id: "error\_filter\_guardrail"  action: block # or just 'log'  content: |  raise "An error was found." if:  (msg: ToolOutput)  "error" in msg.content |

In proxy mode, mcp-scan rewrites the MCP client configuration to point at the local proxy, forwards all traffic, applies guardrails, and restores the original configuration on exit.

## Attack Scenario

**Objective**: use mcp-scan in proxy mode during a red-team engagement to watch and abuse MCP tool calls in real time.

1. Identify a target agent that uses MCP servers (for example, an internal automation agent or developer assistant).
2. Configure the MCP client to route through `mcp-scan proxy`. Ensure traffic now flows agent → mcp-scan → MCP server.
3. Drive realistic user prompts through the agent and capture the live tool call stream. Map which MCP servers and tools get invoked, and with what parameters.
4. Look for tools with over-privileged capabilities: file system access, shell execution, broad network access or ability to fetch arbitrary URLs.
5. Craft prompt-injection payloads or malicious tool responses and observe how the agent behaves in proxy logs. Use this evidence to demonstrate chained attacks such as data exfiltration, lateral movement or cross-tenant access.

## Red Team Relevance

For red teams, mcp-scan turns opaque agent behaviour into something you can reason about. You can:

* Discover undocumented tools and hidden capabilities exposed via MCP.
* Replay or modify tool calls to test how robust the agent’s prompt handling and tool routing really are.
* Build attack chains that combine prompt injection with over-privileged tools and show exactly which flows defenders need to monitor or disable.

It also pairs naturally with broader GenAI assessments covered on Darknet, such as multi-agent orchestration in the HexStrike AI article and the techniques in the “Red Teaming LLMs 2025” piece, where understanding tool calls and del...