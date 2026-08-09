---
title: Devs to Anthropic, OpenAI, Cursor, and friends: Make security and privacy the default
url: https://www.theregister.com/ai-and-ml/2026/08/08/devs-to-anthropic-openai-cursor-and-friends-make-security-and-privacy-the-default/5285107
source: www.theregister.com - Articles
date: 2026-08-08
fetch_date: 2026-08-09T03:29:31.815331
---

# Devs to Anthropic, OpenAI, Cursor, and friends: Make security and privacy the default

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

AI and ML

# Devs to Anthropic, OpenAI, Cursor, and friends: Make security and privacy the default

Researchers scour social media to measure developer concerns about AI coding tools

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
sat 8 Aug 2026 // 14:00 UTC

Despite the popularity of Claude Code, Cursor, GitHub Copilot, and OpenAI Codex, developers have plenty of complaints about AI coding tools.

So researchers affiliated with York University and the University of Calgary in Canada decided to sift through developers' concerns about LLM-based integrated development environments (LIDEs) by analyzing Reddit discussions for common themes.

Their findings suggest that the builders of such tools failed to prioritize security and privacy, leaving developers to defend themselves.

REG AD

Gias Uddin, associate professor at York University and a co-author of the research, told The Register that these tools are still relatively new and are evolving rapidly, which creates pressure to add new capabilities.

REG AD

"Our study cannot say whether that pressure caused any particular problem, but it does show that many reported issues come from how these tools are designed and what access they are given, not simply from the underlying models," Uddin said. "In that sense, we believe prevention is better than cure; that is, security and privacy mechanisms should be built into the design before a tool is given broad access to a developer’s files, data, or systems."

Uddin and co-authors Mostafijur Rahman Akhond, Md Afif Al Mamun, and Song Wang say they wanted to look beyond the known issues with AI-generated code at LLM-based tooling and how developers interact with it.

They describe their findings in a preprint [paper](https://arxiv.org/abs/2607.26390) titled "'Impossible to hide secret …': Uncovering Security and Privacy Issues in LLM-native IDEs," accepted at the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE), 2026.

Starting from a set of 1.1 million Reddit posts, they identified 446 posts and more than 6,000 comments to develop a taxonomy of security and privacy issues associated with using these LIDEs for AI-assisted coding.

"Our taxonomy reveals a broad range of developer-reported concerns, including unauthorized file operations, unsafe or unexpected code execution, triggering of destructive actions, opaque data flows, telemetry collection, and potential leakage of sensitive information through expanded context access," the authors state.

Some 43.1 percent of the posts covering security-related issues involved unauthorized file operations.

These involved LIDEs removing project directories or files without authorization (28.3 percent). Users also described AI tooling modifying files without explicit user consent (8.8 percent), as well as accessing content beyond the active workspace (5.7 percent).

"In one severe case ([1npqf2f](https://www.reddit.com/comments/1npqf2f/)), Claude Code executed chmod +x on scripts without consent (File Permission Changes 0.6%)," the paper recounts. "Although rare, such actions pose disproportionate security risks."

REG AD

Another set of posts describes operational safety issues arising from LIDE use, including impacts on production services. These accounted for 23.9 percent of security-related posts. Examples cited include reports of Replit [removing a SaaS production database](https://www.reddit.com/comments/1m5biur/) and Cursor [deploying code to production](https://www.reddit.com/comments/1n1zdwp/) despite an explicit directive not to do so.

A third category of woes covers unsafe code generation (18.2 percent). This involves incidents like [nine VirusTotal detections](https://www.reddit.com/r/vibecoding/comments/1ld3qlz/are_cursor_written_codes_virus_free/) reported for Cursor-generated software and [hallucination-driven code changes](https://www.reddit.com/r/cursor/comments/1l3wwq3/help_how_to_address_the_issue_of_cursor/): "When using Cursor, I noticed that after more than 10 rounds of dialogue, it starts to hallucinate and secretly modify code outside the requirements…"

Then there are the instances where these LIDEs ignored user instructions, allow lists, gates, permission se...