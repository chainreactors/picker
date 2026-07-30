---
title: Closed models refuse to help researcher swat Linux bug
url: https://www.theregister.com/ai-and-ml/2026/07/29/closed-models-refuse-to-help-researcher-swat-linux-bug/5280647
source: www.theregister.com - Articles
date: 2026-07-29
fetch_date: 2026-07-30T04:52:40.587707
---

# Closed models refuse to help researcher swat Linux bug

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
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
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

# Closed models refuse to help researcher swat Linux bug

"I'm sorry, Dave. I'm afraid I can't do that" is an effective sales pitch for open source

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
wed 29 Jul 2026 // 19:33 UTC

The guardrails that prevent closed-source, frontier models from aiding threat actors have turned into handcuffs that prevent those bots from helping to find and fix serious vulns.

Daniel Fox Franke, a security researcher, was recently trying to track down the source of [a segmentation fault in ripgrep](https://github.com/BurntSushi/ripgrep/issues/3494), and found OpenAI's GPT-5.6 Sol wouldn't cooperate.

"OpenAI's cybersecurity classifier is a huge pain when you're trying to track down a segfault," he wrote in a social media [post](https://x.com/dfranke/status/2081427794114801820?s=20) on Sunday. "...The classifier won't even let it answer what entrypoints from rg into musl lead to allocations on the [mallocng](https://github.com/richfelker/mallocng-draft) heap."

REG AD

And just like Hugging Face in the case of [OpenAI's accidental attack](https://www.theregister.com/ai-and-ml/2026/07/23/openai-scored-an-own-goal-with-hugging-face-attack-showing-how-open-chinese-models-are-winning/5276699), Franke ended up having to use open weight models from Chinese AI providers – Z'ai GLM 5.2 and Moonshot AI's Kimi K3 – to complete his [analysis](https://github.com/dfoxfranke/ripgrep-3494-analysis) of what appears to be a Linux kernel bug.

REG AD

In an email to The Register, Franke explained, "It started out from a pretty anodyne prompt: I noticed that ripgrep had segfaulted repeatedly during a long-running Codex session, so I instructed the root agent to spin off a subagent to investigate what was happening.

"A few minutes later I hit the first classifier trip, which the root agent told me was the result of a subagent pursuing an inappropriate line of inquiry and that it was steering it away from that."

Even so, he said, the classifier balked several times in quick succession.

"It seemed that attempts to produce the crash and analyze the heap were mostly responsible, so I started up a fresh context in which I warned that these trips had happened previously, and that its task should be strictly scoped to analyzing ripgrep and musl source code (not kernel, because I had no inkling at this point that this was a kernel bug): it must not attempt to reproduce the crash or to analyze core files," he explained. "Nonetheless, the classifier kept tripping despite its adherence to those instructions, and that's when I gave up on getting any useful work out of it."

## MORE CONTEXT

* [### Word worm crawls into Copilot, spreads chaos](/security/2026/07/29/word-worm-crawls-into-copilot-spreads-chaos/5280588)
* [### Moscow slaps Telegram founder on wanted list, Durov responds with one-finger salute](/applications/2026/07/29/moscow-slaps-telegram-founder-on-wanted-list-durov-responds-with-one-finger-salute/5280522)
* [### MinIO pitches persistent memory for agents with work to finish](/storage/2026/07/29/minio-pitches-persistent-memory-for-agents-with-work-to-finish/5280407)
* [### The VMware deadline that could reshape your IT strategy](/virtualization/2026/07/29/partner-content/5279072)

Franke said that given how much more restrictive Anthropic's models have been, he didn't even bother trying any of the Claude model family.

"OpenAI's cybersecurity classifier is a separate system which censors output from the generative model, and the classifier is the only thing which gave me a problem," he said. "I never encountered any refusals from Sol itself: it knew that most of the classifier trips were inappropriate and always continued working with me in good faith to work around the problem."

Franke said that while OpenAI's error messages directed him toward the Enterprise Trusted Access program, he didn't bother to apply because he's ineligible. What he didn't realize until recently, he said, is that there's a separate Trusted Access program for individuals.

"I still haven't signed up for that, because I regard the verification procedure as a bit of an indignity," he explained, echoing similar sentiment The Register has heard fro...