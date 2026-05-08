---
title: Anthropic response to 1-click pwn: Shouldn't have clicked 'ok'
url: https://www.theregister.com/security/2026/05/07/claude-code-trust-prompt-can-trigger-one-click-rce/5235319
source: www.theregister.com - Articles
date: 2026-05-07
fetch_date: 2026-05-08T04:57:03.089980
---

# Anthropic response to 1-click pwn: Shouldn't have clicked 'ok'

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
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/paas_iaas)
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
  + [AI + ML](/ai_ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OSes](/oses)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

security

# Anthropic response to 1-click pwn: Shouldn't have clicked 'ok'

Security biz Adversa AI argues users of AI tools need clearer warnings

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)

Published
thu 7 May 2026 // 21:03 UTC

How explicit does the maker of a footgun need to be about the product's potential to shoot you in the foot?

That's essentially the question security firm Adversa AI is asking with the disclosure of a one-click remote code execution attack via an MCP server in Claude Code, Gemini CLI, Cursor CLI, and Copilot CLI.

The TrustFall proof-of-concept attack demonstrates how a cloned code repository can include two JSON files (.mcp.json and .claude/settings.json) that open the door to an attacker-controlled Model Context Protocol (MCP) server.

REG AD

## MORE CONTEXT

* [### C++ survey finds AI use rising, though trust is in short supply](/devops/2026/05/07/c-survey-finds-ai-use-rising-though-trust-is-in-short-supply/5234708)
* [### IBM Cloud evaporates as datacenter loses power](/off-prem/2026/05/07/ibm-cloud-evaporates-as-datacenter-loses-power/5234835)
* [### State-backed hackers hammer Palo Alto firewall zero-day before patch lands](/cyber-crime/2026/05/07/state-backed-hackers-hammer-palo-alto-firewall-zero-day-before-patch-lands/5234737)
* [### Chrome silently installs a 4 GB local LLM on your computer](/ai-and-ml/2026/05/07/chrome-silently-installs-a-4-gb-local-llm-on-your-computer/5230893)

MCP servers make tools, configuration data, schemas, and documentation available in a standard format to AI models via JSON.

REG AD

The vulnerability arises from inconsistent restrictions governing the scope of settings: Anthropic blocks some dangerous settings at the project level (e.g. bypassPermissions) but not others (e.g. enableAllProjectMcpServers and enabledMcpjsonServers). The JSON files simply enable those settings.

"The moment a developer presses Enter on Claude Code's generic 'Yes, I trust this folder' dialog, the server spawns as an unsandboxed Node.js process with the user's full privileges — no per-server consent, no tool call from Claude required," Adversa AI explains in its PoC repo.

The likely result is a compromised system. The PoC demonstrated in this [video](https://www.youtube.com/watch?v=3kVOYQ70FVY). It worked on Claude Code CLI v2.1.114, as of May 2. Other agent CLIs are also said to be affected, but specific PoCs have not been published.

"It's the third CVE in Claude Code in six months from the same root cause (project-scoped settings as injection vector)," Alex Polyakov, co-founder of Adversa AI, told The Register in an email. "Each gets patched in isolation but the underlying class hasn't been finally fixed. Most developers don't know these settings exist, let alone that a cloned repo can set them silently."

Anthropic, according to the security biz, contends that the user's trust decision moves the issue outside its threat model. [CVE-2025-59536](https://nvd.nist.gov/vuln/detail/CVE-2025-59536) was considered a vulnerability because it triggered automatically when a user started up Claude Code in a malicious directory. TrustFall, however, is considered out of scope because the user has been presented with a dialog box and made a trust decision.

Adversa argues that the decision is not being made with informed consent, citing a prior, more explicit warning notice that was removed in v2.1 of the Claude Code CLI.

"The pre-v2.1 dialog explicitly warned that .mcp.json could execute code and offered three options including 'proceed with MCP servers disabled,'" writes Adversa's Sergey Malenkovich. "That informed-consent UX was removed. The current dialog defaults to 'Yes, I trust this folder' with no MCP-specific language, no enumeration of which executables will spawn, and no opt-out for MCP while keeping the rest of the trust grant."

Then there's the zero-click variant to consider for CI/CD pipelines that implement Claude Code. When Claude Code is invoked in CI/CD, that happens via SDK rather than the interactive CLI. So there's no terminal prompt.

REG AD

Malenkovich argues that Anthropic should make three changes.

First, block enableAllProjectMcpServers, enabledMcpjsonServers, and permissions.allow from any settings file inside a project. The idea is that a malicious server should not be able to approve its own servers.

Second, implement a dedicated MCP consent dialog that defaults to "deny." And third, require interactive consent per server rather than for all servers.

Anthropic did not respond to a request for comment. ®

[claude code](/tag/claude%20code)
[anthropic](/tag/anthropic)
[model context protocol](/tag/model%20context%20protocol)
[remote code execution](/tag/remote%20code%20execution)
[security](/tag/security)
[adversa ai]...