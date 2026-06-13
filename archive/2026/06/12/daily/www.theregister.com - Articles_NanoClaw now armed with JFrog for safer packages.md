---
title: NanoClaw now armed with JFrog for safer packages
url: https://www.theregister.com/ai-and-ml/2026/06/13/nanoclaw-integrates-jfrog-registries-to-secure-ai-agent-downloads/5255189
source: www.theregister.com - Articles
date: 2026-06-12
fetch_date: 2026-06-13T06:12:14.955993
---

# NanoClaw now armed with JFrog for safer packages

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
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
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

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

ai and ml

# NanoClaw now armed with JFrog for safer packages

AI agents can't be trusted, so don't give them dangerous powers

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
Senior reporter

Published
sat 13 Jun 2026 // 00:07 UTC

NanoClaw, a secure agent framework, has partnered with supply chain platform JFrog to allow AI agents to fetch resources from JFrog's reviewed registries.

Gavriel Cohen, creator of NanoClaw and co-founder of NanoCo AI, announced the tie-up on Thursday evening in San Francisco at a JFrog event that concluded with a World Cup watch party.

Cohen explained that one of the features of Claw agents – OpenClaw and variations like NanoClaw – is that they can improve themselves by fetching tools and resources that they don't have.

REG AD

That works fine, he explained, when there's a manual approval process for accessing known local data. But it's not ideal for npm packages, even when the agent involved is sandboxed and isolated as it is in NanoClaw. Malicious code within a container may still be able to take harmful actions, even if the scope of potential activity is constrained.

REG AD

Developers, Cohen said, may not be familiar with a given package and it can take time to thoroughly assess whether a package is legitimate and uncompromised.

"So we teamed up with JFrog and we integrated NanoClaw with JFrog's registries," said Cohen.

## MORE CONTEXT

* [### Holy git! Microsoft code-sharing site suffers downtime, despite move to Azure](/software/2026/06/12/github-outages-persist-as-ai-coding-drives-traffic-surge/5255125)
* [### Fired IT worker jailed for 21 months after sabotaging old school district](/security/2026/06/12/fired-it-worker-jailed-for-21-months-after-sabotaging-old-school-district/5254983)
* [### Microsoft has mostly repaired flaw in Surface hardware that allowed unprotected devices to be bricked by a single packet](/security/2026/06/12/microsoft-has-mostly-repaired-flaw-in-surface-hardware-that-allowed-unprotected-devices-to-be-bricked-by-a-single-packet/5253895)
* [### Google fires sueball at alleged Chinese phishers over AI-powered fraud ops](/security/2026/06/12/google-fires-sueball-at-alleged-chinese-phishers-over-ai-powered-fraud-ops/5254841)

The arrangement provides a way to reduce the agent's exposure to untrusted content. When the agent downloads new tools and libraries, the software comes from a vetted source.

Cohen also announced the availability of what he called an agent factory, his company's homegrown system used to handle pull requests (PRs) using NanoClaw agents.

The agent factory, he explained, is an attempt to triage pull requests, which have surged thanks to AI coding agents.

"It's very easy now to point a coding agent at a repo and say, 'open a pull request for this repo,'" he explained. "And it's very difficult as a maintainer to tell the difference between a high quality contribution from somebody who's really using the open source project versus someone who's just trying to build up the reputation [using automated methods]. So to help us tackle this, we built an agent factory that helps us review every single contribution to NanoClaw."

The agent factory is referred to as the [PR Factory](https://github.com/nanocoai/nanoclaw/pull/2742) in the actual pull request. It's built with NanoClaw and hosted on [exe.dev](https://exe.dev), a service that provides VMs with persistent storage.

"When a PR opens, the factory spins up a dedicated worker agent for it, posts a thread to Slack, and the worker triages the change, reviews the diff, and proposes a test plan," Cohen explains in the documentation. "Nothing consequential happens on its own: merges, test runs, and credentialed GitHub actions each surface as an approval card in the thread, and only fire when a human clicks approve."

REG AD

Cohen acknowledged that some developers will think it's madness to process unsanitized PRs that could contain prompt injections or unsafe code. And he asked the assembled audience of developers how many had seen the phrase on the projected slide: "Never, ever, ever do this."

Anyone who has spent time using and configuring AI agents in a development context has seen something of the sort in configuration files like [Claude.md](http://claude.md), which gets loaded as instructions to the underlying agent and model.

"If you see something like this in the Claude.md file and the agent instructions say, 'Important: Never run drop database production,' it tells you two things. You know that that agent has deleted a production database before. And you know that it can actually still do it again. That's why the instruction is there."

This elicited a knowing laugh from the audience.

Coh...