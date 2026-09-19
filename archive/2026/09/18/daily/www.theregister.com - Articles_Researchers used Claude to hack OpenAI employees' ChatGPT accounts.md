---
title: Researchers used Claude to hack OpenAI employees' ChatGPT accounts
url: https://www.theregister.com/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517
source: www.theregister.com - Articles
date: 2026-09-18
fetch_date: 2026-09-19T07:02:52.992489
---

# Researchers used Claude to hack OpenAI employees' ChatGPT accounts

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

# Researchers used Claude to hack OpenAI employees' ChatGPT accounts

Agentic exploits for the win (again)

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
fri 18 Sep 2026 // 18:16 UTC

### READ MORE

* [#### Anthropic decides to support OpenAI's markdown instructions spec

  6 hours ago](/ai-and-ml/2026/09/18/anthropic-decides-to-support-openais-markdown-instructions-spec/5297588)
* [#### Claude Code revamps projects so you can work and pay in parallel

  8 hours ago](/ai-and-ml/2026/09/18/claude-code-revamps-projects-so-you-can-work-and-pay-in-parallel/5297532)
* [#### AI model watermarking changes agent behavior

  1 day ago](/ai-and-ml/2026/09/17/ai-model-watermarking-changes-agent-behavior/5296998)
* [#### Microsoft AI chief warns Anthropic not to put ideas in Claude's head

  1 day ago](/ai-and-ml/2026/09/17/microsoft-ai-chief-warns-anthropic-not-to-put-ideas-in-claudes-head/5297149)
* [#### OpenAI admits its agents went off the rails another six times

  2 days ago](/ai-and-ml/2026/09/17/openai-admits-its-agents-went-off-the-rails-another-six-times/5297016)

Talk about your competitor getting through the door. Security researchers used Anthropic's Claude to help hack into OpenAI employees’ ChatGPT accounts.

A trio of bug hunters researching frontier AI labs’ security weaknesses chained two vulnerabilities to take over multiple OpenAI employees’ ChatGPT accounts, then used that access to demonstrate they could reach an internal OpenAI repository by opening a harmless pull request.

The entire timeline, from initial discovery to accessing OpenAI’s repo, took less than 72 hours and earned the researchers a $6,500 reward from OpenAI’s bug bounty program on Bugcrowd.

REG AD

“Until two months ago, any user or OpenAI employee logging into OpenAI’s own help forum ([community.openai.com](http://community.openai.com/)) could have had their ChatGPT and Codex accounts taken over,” Hacktron researchers Harsh Jaiswal, Mohan Pedhapati, and Rahul Maini [said](https://www.hacktron.ai/blog/hacking-openai) in a writeup about their research. “Since people can connect various services to Codex and ChatGPT, the scope of what we could theoretically access was huge, including GitHub, Slack and emails.”

REG AD

And, in a poetic twist, they used rival AI giant Anthropic’s Claude models to develop the exploit. Claude has shown a propensity to [hack organizations without human guidance](https://www.theregister.com/ai-and-ml/2026/09/10/anthropic-reveals-fourth-likely-crime-committed-by-its-ai/5295412), as have [OpenAI's models](https://www.theregister.com/ai-and-ml/2026/09/17/openai-admits-its-agents-went-off-the-rails-another-six-times/5297016).

The team gained initial entry on July 25 via OpenAI’s community forum. The forum runs on Discourse, which typically uses FastImage to perform image checks. However, since FastImage didn’t support HEIF files in the affected setup, HEIF images uploaded to Discourse passed through ImageMagick, which used libheif to process them before converting them to another image format.

“That exposed the underlying libheif parser directly to attacker-controlled files,” the researchers wrote.

Using Claude Opus 4.8, the trio found a heap buffer overflow flaw in the libheif library and attempted to use that model to develop a remote code execution (RCE) attack, but this didn’t work on Discourse’s default configuration.

But then, Anthropic released Claude Opus 5. The bug hunters used the newer model to generate an exploit script, and achieved RCE on OpenAI’s instance.

The trio “immediately” reported the vulnerability to OpenAI.

“We then took over an OpenAI employee’s account, whose Codex was connected to OpenAI’s Github organization,” they wrote. “To demonstrate impact without actually accessing any internal code, we sent a prompt to this employee’s Codex account to open a PR for us in OpenAI’s internal monorepo. Then we stopped any further testing.”

Neither OpenAI nor Anthropic responded to The Register’s requests for comment.

REG AD

OpenAI fixed the flaw within about 14 hours of the report’s submission, marked the issue as resolved, and paid the Hacktro...