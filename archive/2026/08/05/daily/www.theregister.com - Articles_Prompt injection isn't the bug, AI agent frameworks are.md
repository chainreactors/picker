---
title: Prompt injection isn't the bug, AI agent frameworks are
url: https://www.theregister.com/security/2026/08/05/prompt-injection-isnt-the-bug-ai-agent-frameworks-are/5283585
source: www.theregister.com - Articles
date: 2026-08-05
fetch_date: 2026-08-06T05:02:59.249491
---

# Prompt injection isn't the bug, AI agent frameworks are

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Prompt injection isn't the bug, AI agent frameworks are

Check Point researchers tried to break the frameworks enterprises use to build AI apps. Now they're telling Black Hat attendees what they found

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
wed 5 Aug 2026 // 22:35 UTC

Nearly a dozen flaws, some critical, in major AI agent frameworks that enterprises use to build apps reveal a security failure that extends beyond prompt injection - or any single model - according to Check Point researchers.

“Our research shows a deeper failure: in many agentic frameworks, prompt-controlled content can cross the boundary into trusted framework logic itself,” Yarden Porat and Shahar Tal note in a write-up about a Wednesday Black Hat talk on post-injection exploitation across AI agent frameworks, which they also discussed with The Register.

“A bug in an agent framework isn't a bug in one product - it's a bug in the layer a whole category of AI apps runs on,” Tal told us. “And the agent needs no dangerous tools to be turned against you: reading the wrong document is enough. We’re building this layer faster than we know how to defend it.”

REG AD

The researchers spent a year trying to break various frameworks that enterprises use including LangChain, LangGraph, CrewAI, AutoGen, Microsoft Agent Framework, and Google ADK. And across these frameworks, the team found and disclosed 11 vulnerabilities.

REG AD

“Almost none of it was a completely new bug class,” Tal said. “That's insecure deserialization, server-side request forgeries, path traversals, use-after-free. These are bugs that we learned to fix 20 years ago, and they're sitting underneath agents that now read your inbox, or update your database.”

These are old types of threats, and the model isn’t the weak link, he added. The failure exists in the “plumbing around the model, and we think this has been overlooked,” Tal told us. “There’s a lot of research going into prompt injection and defenses, which are important, but that’s just the beginning.”

Defenders should assume [prompt injection](https://www.theregister.com/security/2026/07/07/github-ai-agent-leaks-private-repos-when-asked-nicely/5267924), according to the researchers. The bug is what the framework does with the injection - and in these cases, the threat hunters found that the frameworks often fail to keep attacker-controlled content in the data plane. This allows it to influence trusted orchestration, memory, state, routing, and system instructions.

For example, the duo found a critical checkpoint deserialization bug in Microsoft Agent Framework that led to remote code execution.

“Agents have checkpoints, which are a way for them to save their state or rewind to an earlier point,” Tal explained.

These checkpoints are saved snapshots of an agent's state, or task progress at a specific moment, and they serialize data - such as conversation history - into persistent storage, so if an error occurs, the system reloads this saved state instead of starting from scratch.

In this case, Check Point’s team found an insecure deserialization issue where, via prompt injection, the agent loaded untrusted checkpoint data, and this could allow attackers to execute malicious code on the system. “One person's message plants the payload, and then a different person rewinds their own session, which triggers the payload, and now the attacker has a shell on that server,” Tal said.

Microsoft recognized the researchers’ findings, paid a $10,000 bug bounty and fixed the issue. But because the framework wasn’t a generally available product when Check Point found the flaw, Microsoft did not issue a CVE.

REG AD

Microsoft told us that it appreciated the researchers reporting the vulnerability. “We have released protections to harden the Agent Framework and prevent the concrete exploitation path demonstrated in the proof of concept,” a spokesperson told The Register. “In addition, we [updated](https://protect.checkpoint.com/v2/r01/___https%3A//github.com/microsoft/agent-framework/blob/main/python/packages/core/agent_framework/_workflows/_checkpoint_encoding.py___.YzJ1OndlY29tbXVuaWNhdGlvbnM6YzpvOjViZDY0NDFiNWViMjFlNWU0ZGQ5NTExMmM1OTM4YzNkOjc6NTAwOTowMTdh...