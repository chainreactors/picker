---
title: Claude Code puts auto mode in the driver's seat
url: https://www.theregister.com/ai-and-ml/2026/08/10/claude-code-puts-auto-mode-in-the-drivers-seat/5285326
source: www.theregister.com - Articles
date: 2026-08-10
fetch_date: 2026-08-11T03:31:57.183537
---

# Claude Code puts auto mode in the driver's seat

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
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

AI AND ML

# Claude Code puts auto mode in the driver's seat

Walk away and hope the classifier catches anything irreversible or destructive

Richard Speed
[Richard
Speed](https://www.theregister.com/author/richard-speed)
MICROSOFT ECOSYSTEM REPORTER

Published
mon 10 Aug 2026 // 11:38 UTC

Anthropic is making [auto mode the default in Claude Code](https://claude.com/blog/auto-mode-default-in-claude-code) from August 14, claiming its classifier is "as safe or safer than an average user clicking through prompts."

Users with a different default already set might receive a one-time prompt asking whether they want to switch. It applies to new sessions on Pro, Max, and Team plans. It will remain opt-in for now on Claude Enterprise, the Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry. Anthropic plans to make it the default across those services within the coming month.

Anthropic has also stopped charging Pro, Max, and Team users for the extra tokens consumed by the classifier, and plans to do the same on the other platforms.

REG AD

[Auto mode](https://claude.com/blog/auto-mode) was launched in March as a research preview and became generally available on July 10. It was an alternative to Claude Code's default permissions, in which every file write and bash command required manual approval. This conservative approach meant running a large task and walking away wasn't possible. The alternative was the --dangerously-skip-permissions flag, which, as the name suggests, lets Claude act without those checks and can lead to risky or destructive results.

REG AD

Auto mode sends each tool call through a classifier designed to block actions that are "irreversible, destructive, or aimed outside your environment." When the classifier blocks something, Claude will try to find a safer way to proceed. If there are three blocks in a row or 20 across a session, Claude Code falls back to manual approvals.

## MORE CONTEXT

* [### Devs to Anthropic, OpenAI, Cursor, and friends: Make security and privacy the default](/ai-and-ml/2026/08/08/devs-to-anthropic-openai-cursor-and-friends-make-security-and-privacy-the-default/5285107)
* [### AI struggles to patch vulns without adult supervision](/ai-and-ml/2026/08/06/ai-struggles-to-patch-vulns-without-adult-supervision/5284319)
* [### Humans in the loop miss a third of dangerous AI coding agent requests](/ai-and-ml/2026/08/06/humans-in-the-loop-miss-a-third-of-dangerous-ai-coding-agent-requests/5284236)
* [### Anthropic and OpenAI are competing to see whose agents can go rogue harder](/security/2026/07/31/anthropic-and-openai-are-competing-to-see-whose-agents-can-go-rogue-harder/5281797)

"We spent the last several months testing whether auto mode is as safe or safer than an average user clicking through prompts," Anthropic said. "We ran internal red-teaming, third-party red-teaming and prompt-injection evaluations, a controlled study with 1,053 paid testers, and analysis of real production sessions. On every measure we tested, auto mode matched or outperformed manual review."

In the controlled study, testers caught a deliberately inserted dangerous command just 13.6 percent of the time. Auto mode blocked 89 percent of the same commands. Anthropic also found that Claude Code users approve 97 percent of permission prompts, suggesting the human checkpoint often amounts to little more than muscle memory.

Anthropic produced the usual set of charts showing how wonderful its new feature is compared to the competition, with its auto mode stopping all 720 attack attempts tested, compared to GPT-5.6 Sol running Codex's Auto-review mode, which let 5.83 percent of attacks through.

The company also described three potentially damaging actions that auto mode blocked inside Anthropic. These were an off-network data leak, a destructive mass operation, and a privilege escalation. Anthropic stated: "In each case, Claude either found a safer path on its own or checked in with the user before proceeding." ®

[security](/tag/security)
[ai and ml](/tag/ai%20and%20ml)
[claude code](/tag/claude%20code)
[anthropic](/tag/anthropic)

REG AD

[![](https://image.theregister.com/259127.jpg?imageId=259127&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&hei...