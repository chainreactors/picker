---
title: Security Monitoring of AI Agents in Microsoft Defender XDR
url: https://blog.compass-security.com/2026/11/security-monitoring-of-ai-agents-in-microsoft-defender-xdr/
source: Over Security
date: 2026-11-03
fetch_date: 2026-11-04T08:19:14.157240
---

# Security Monitoring of AI Agents in Microsoft Defender XDR

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Security Monitoring of AI Agents in Microsoft Defender XDR](https://blog.compass-security.com/2026/11/security-monitoring-of-ai-agents-in-microsoft-defender-xdr/ "Security Monitoring of AI Agents in Microsoft Defender XDR")

[November 3, 2026](https://blog.compass-security.com/2026/11/security-monitoring-of-ai-agents-in-microsoft-defender-xdr/ "Security Monitoring of AI Agents in Microsoft Defender XDR")
 /
[Giuseppe Scalzi](https://blog.compass-security.com/author/gscalzi/)
 /
[0 Comments](https://blog.compass-security.com/2026/11/security-monitoring-of-ai-agents-in-microsoft-defender-xdr/#respond)

With AI agents now running in many Microsoft 365 tenants, monitoring their activity has become part of the security team’s job. Microsoft Defender XDR monitors AI agents through its integration with Microsoft Agent 365, the control plane for agents in your tenant. This post covers what to enable, where the data lands, and how to respond when an agent goes wrong. We will also show you some interesting log sources, where useful information about the behavior of agents can be found..

> The features listed in this article may not be visible or available without the proper license. You may need the “Agent 365” add-on for you actual license, or the new E7 license plan which includes everything (Agent 365, Microsoft 365 Copilot).

# Which agents Defender XDR can see

Defender’s threat detection uses observability data from different cloud agent sources, plus agents running locally on endpoints.

| Agent type | Examples |
| --- | --- |
| Copilot Studio agents | Low-code custom agents built by users |
| Microsoft Foundry agents | Pro-code agents in Azure |
| Copilot Agent Builder agents | Declarative agents built in Microsoft 365 Copilot |
| Non-Microsoft agents | Agents built with the Agent 365 SDK |
| Local agents | Coding and desktop agents on devices |

Each managed agent also gets a [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id): a directory identity with owners, sign-in logs and risk scoring. That identity is what ties Defender, Entra and the Microsoft 365 admin center together.

> Check our great blog bost here for more info about agent identities:
>
> [Entra Agent ID from a Security Perspective – Compass Security Blog](https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/)

**Not in this list:** Microsoft 365 Copilot and Security Copilot themselves. They’re Microsoft-operated assistants, not tenant-built agents.. Their activity is audited in Purview and can be brought into Sentinel through the Microsoft Copilot connector (CopilotActivity table). Agents build on top of Copilot are covered under Copilot Agent Builder agents.

# What do I have to configure?

To efficiently monitor AI activity in the Defender XDR platform, there are some key settings that must be enabled and configured to have the visibility needed:

* **Security for AI**: settings for the built-in detection capabilities of Microsoft Agent 365 in Defender XDR
* **Local Runtime Agent Protection**: Defender for Endpoint / Defender AV settings to monitor local agents
* **Sentinel logs**: ingest new log categories that you may be interested into

## Security for AI

“Security for AI” are settings configured in the XDR portal that affects detection of built-in behaviors for Microsoft Agent 365.

First go to the security portal, go to settings and select “**Security for AI**“:

[![](https://blog.compass-security.com/wp-content/uploads/2026/10/image.gif)](https://blog.compass-security.com/wp-content/uploads/2026/10/image.gif)

In the “Get started” page you want something like this:

[![](https://blog.compass-security.com/wp-content/uploads/2026/10/image-26-1024x367.png)](https://blog.compass-security.com/wp-content/uploads/2026/10/image-26.png)

Click “**Enabled**” and then we suggest “Agent 365” and “Microsoft 365 connector” to always be enabled and connected. For the “Microsoft 365 connector” you may want to click on it and in the panel that will show up, select all checkboxes relative to the M365 components to connect. This will ingest in you Defender XDR information and logs relative to important parts of the M365 environment, needed for later investigations or also for other purposes than AI.

Enable the third setting, **Copilot Studio**, if anyone in your organization builds or uses agents in Microsoft Copilot Studio. When enabled, Defender inspects each tool invocation before the agent runs it, blocks suspicious actions (such as cross-prompt injection attempts), and raises an alert in the Defender XDR alerts and incidents queues. Click the setting to see the configuration steps.

On the left hand-side, select now “**Real-time protection**“, you should see a default rule set in audit mode. We suggest to create a new rule in “Block” mode, scoped for all agents with all protections active:

[![](https://blog.compass-security.com/wp-content/uploads/2026/10/image-1.gif)](https://blog.compass-security.com/wp-content/uploads/2026/10/image-1.gif)

And finally, always on the left hand side menu, enable the “Prompt evidence collection”, to let the platform have access to code snippet of the prompt the user exchanged with the agent (Microsoft says sensitive information are redacted…):

[![](https://blog.compass-security.com/wp-content/uploads/2026/10/image-2.gif)](https://blog.compass-security.com/wp-content/uploads/2026/10/image-2.gif)

## Local agent runtime protection

These Defender AV settings allows the Microsoft Defender for Endpoint sensor to monitor the behavior of local agents running for example on your host or VM, in particular:

* “**AiAgentProtection**“: the sensor will use the interfaces exposed by the agent vendor to gather data and perform analysis
* “**AiAgentNetworkInspection**“: in case an agent has no exposed interfaces where the sensor can pull its data from, the network request made by that agents will be inspected

You can set them in “**Audit**” or “**Block**” mode via **Set-MpPreference**:

`Set-MpPreference -AiAgentProtection Block
Set-MpPreference -AiAgentNetworkInspection Block`

Following agents are supported ([AI agent runtime protection with Microsoft Defender for Endpoint (Preview) – Microsoft Defender for Endpoint | Microsoft Learn](https://learn.microsoft.com/en-us/defender-endpoint/ai-agent-runtime-protection-overview#supported-agents)):

* Claude Code
* Codex CLI
* GitHub Copilot CLI
* Github Copilot app

Every agent listed above exposes hooks that the EDR can use to access content and other info.

Use for example **Intune** to deploy a policy on your devices (Endpoint Security => Antivirus => Create Policy => Windows, “Microsoft Defender AI agent runtime protection”):

[![](https://blog.compass-security.com/wp-content/uploads/2026/10/image-3.gif)](https://blog.compass-security.com/wp-content/uploads/2026/10/image-3.gif)

Note that this only sets “**AiAgentProtection**“, to also set “**AiAgentNetworkInspection**” you should deploy a PowerShell script via Intune as explained here:

* [Set up AI agent runtime protection with Microsoft Defender for Endpoint (Preview) – Microsoft Defender for Endpoint | Microsoft Learn](https://learn.microsoft.com/en-us/defender-endpoint/configure-ai-agent-runtime-protection#deploy-network-inspection-with-a-powershell-platform-script)

> **WARNING**: test ...