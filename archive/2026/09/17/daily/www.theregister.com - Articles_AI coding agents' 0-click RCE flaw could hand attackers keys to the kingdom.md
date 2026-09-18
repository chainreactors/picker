---
title: AI coding agents' 0-click RCE flaw could hand attackers keys to the kingdom
url: https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335
source: www.theregister.com - Articles
date: 2026-09-17
fetch_date: 2026-09-18T06:53:42.091363
---

# AI coding agents' 0-click RCE flaw could hand attackers keys to the kingdom

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
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Science](/science)

REG AD

[security](/tag/security)

# AI coding agents' 0-click RCE flaw could hand attackers keys to the kingdom

Plugin4Shell attack affects all the major coding agents, researchers say

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
thu 17 Sep 2026 // 23:42 UTC

### READ MORE

* [#### AI risks make some insurers wary of corporate liability

  57 minutes ago](/ai-and-ml/2026/09/18/ai-risks-make-some-insurers-wary-of-corporate-liability/5297347)
* [#### AWS confesses its console causes cloudy confusion for new users

  1 hour ago](/off-prem/2026/09/18/aws-confesses-its-console-causes-cloudy-confusion-for-new-users/5297365)
* [#### Scientific papers become agentic chatbots with new tool

  13 hours ago](/ai-and-ml/2026/09/17/scientific-papers-become-agentic-chatbots-with-new-tool/5297276)
* [#### Grassroots coalition asks politicians to choose voters over Big AI's $140M machine

  16 hours ago](/ai-and-ml/2026/09/17/grassroots-coalition-asks-politicians-to-choose-voters-over-big-ais-140m-machine/5297186)
* [#### AI model watermarking changes agent behavior

  17 hours ago](/ai-and-ml/2026/09/17/ai-model-watermarking-changes-agent-behavior/5296998)

A zero-click vulnerability that allows remote code execution affects all of the major AI coding agents - Anthropic’s Claude Code, OpenAI’s Codex, Google's Gemini CLI, Microsoft’s Copilot, and Microsoft-owned GitHub Copilot - and could give attackers full access to every asset and piece of data that the agent can reach, researchers say.

The exploit, dubbed “Plugin4Shell,” is a “first-of-its-kind AI supply-chain attack,” according to threat hunters at Air, a security startup focused on protecting enterprise AI agents.

Instead of targeting the model or agent, Plugin4Shell attacks trusted marketplaces that host plugins for major coding agents. Such attacks could therefore reach millions of users and machines, the researchers said.

REG AD

Almost [90 percent](https://news.microsoft.com/ai-in-action/) of Fortune 500 companies use Copilot, according to Microsoft, which also happens to be one of the two that didn’t ship a patch for the flaw.

REG AD

“The fix has to ship in the agent, and updating is the only complete mitigation where one exists,” Air researchers Or Nevo, Dor Granat, and Niv Hoffman [said](https://www.air.security/blog-posts/plugin4shell) in a Thursday report.

The Air team reported the security issue to all four vendors in June, and both Anthropic and OpenAI patched it in Claude Code 2.1.179 and Codex 0.146.0, respectively.

Google has [deprecated the Gemini CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), and therefore told Air it will not patch, so every install remains vulnerable. Google does, however, suggest users migrate to its newer Antigravity agentic development environment, which is protected from this attack.

Microsoft didn’t fix the flaw in Copilot. However, a GitHub spokesperson told us the Plugin4Shell attacks do not affect GitHub.

“To prevent abuse of SHAs, GitHub does not allow users to create branch or tag names that resemble commit SHAs,” the spokesperson said. “This mitigation ensures the reported vulnerability cannot be exploited on GitHub.”

The Air researchers said that the GitHub mitigation isn’t sufficient to defeat Plugin4Shell attacks. This is “because marketplaces can also be hosted in other platforms such as Bitbucket,” the team told The Register.

“Microsoft Copilot is also still vulnerable because it supports marketplaces from such platforms as well, which exposes it to the vulnerability,” the researchers added. “Air also reported the same to Microsoft (since June), but unfortunately due [to] the amount of disclosure volume they’re currently getting we didn’t get a response from them.”

Redmond did not immediately respond to The Register’s request for comment.

REG AD

The security hole sits in how agents enforce marketplaces’ SHA-pinning mechanism, which locks agent plugins and skills to a specific, immutable commit hash instead of a mutable reference like a version tag or branch name.

This aims to prevent supply chain attacks: If a public skill repository i...