---
title: OpenAI: Yoo-hoo, look over here, we do that security stuff too!
url: https://www.theregister.com/security/2026/06/23/openai-yoo-hoo-look-over-here-we-do-that-security-stuff-too/5259842
source: www.theregister.com - Articles
date: 2026-06-22
fetch_date: 2026-06-23T06:08:22.781235
---

# OpenAI: Yoo-hoo, look over here, we do that security stuff too!

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

Security

# OpenAI: Yoo-hoo, look over here, we do that security stuff too!

A plethora of pwn-prevention, including a 'Patch The Planet' pledge

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
tue 23 Jun 2026 // 00:34 UTC

OpenAI announced a flurry of cybersecurity-related AI news on Monday, releasing an improved version of GPT‑5.5‑Cyber, its most advanced vulnerability-finding model, along with an expanded partner program for cybersecurity vendors, an update to its Codex Security scanner⁠, and an initiative to “Patch the Planet” – or at least 30 high-profile open source projects.

The announcements come as Anthropic’s [Mythos mess keeps getting more complicated](https://www.theregister.com/ai-and-ml/2026/06/22/anthropics-mythos-mess-just-keeps-getting-more-complicated/5258577), with [national security concerns](https://www.theregister.com/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827) clouding [defenders’ abilities to use](https://www.theregister.com/ai-and-ml/2026/06/15/us-clampdown-on-anthropic-models-sends-eu-sovereignty-surge-into-overdrive/5255487) that AI company’s [most advanced models](https://www.theregister.com/ai-and-ml/2026/06/09/anthropic-spins-a-fable-of-a-tamer-safer-mythos/5253106) to find and fix vulnerabilities – or perhaps it’s just politics as usual.

They also coincide with a general feeling of FUD around [AI cyberattacks](https://www.theregister.com/cyber-crime/2026/05/22/jailbroken-gemini-helped-russian-speaking-fraudster-target-maga-crypto-users/5245390) and the [impending vulnpocalype](https://www.theregister.com/patches/2026/05/14/welcome-to-the-vulnpocalypse-as-vendors-use-ai-to-find-bugs-and-patches-multiply-like-rabbits/5240027). *The Reg’s* vultures will keep out collective eyes on all of this.

REG AD

First off: GPT‑5.5‑Cyber. After releasing a preview version of the model to a [select group of “trusted defenders,”](https://www.theregister.com/security/2026/05/01/openai-locks-gpt-55-cyber-behind-velvet-rope/5219691) OpenAI on Monday released an update that it says makes the model even better at finding – and also fixing – bugs in code.

REG AD

“It is our strongest model yet for finding and helping patch software vulnerabilities, while retaining GPT‑5.5’s general-purpose intelligence and ability to work across long, complex tasks,” the AI shop [said](https://openai.com/index/daybreak-securing-the-world/). “The model can sustain deeper analysis across large codebases: identifying security-relevant components, tracing whether vulnerable code is reachable, validating likely issues in controlled environments, developing and testing patches, and preparing evidence for human review.”

## MORE CONTEXT

* [### OpenAI locks GPT-5.5-Cyber behind velvet rope despite slamming Anthropic for doing exactly that](/security/2026/05/01/openai-locks-gpt-55-cyber-behind-velvet-rope/5219691)
* [### UK banks offered access to OpenAI’s GPT-5.5 amid exclusion from Anthropic’s Glasswing expansion](/security/2026/06/03/anthropic-ups-glasswing-partner-count-4x-uk-banks-snubbed/5250450)
* [### Feds freaked over Fable 5 after simple 'fix this code' prompt, not jailbreak, says researcher](/security/2026/06/15/feds-freaked-over-fable-5-after-simple-fix-this-code-prompt-not-jailbreak-says-researcher/5255827)
* [### OpenAI's agent chained decade-old DoS attacks to crash web servers in seconds](/security/2026/06/04/openais-codex-chains-decade-old-dos-techniques-into-http/2-bomb/5251377)

OpenAI said it evaluated the update and 5.5 preview using a few different benchmarks: CyberGym, which test how well AI systems can reproduce known vulnerabilities; ExploitGym, which determines how well models can turn known vulnerabilities into working exploits that achieve unauthorized code execution; and SEC-bench Pro, which measures AI systems’ long-horizon vulnerability discovery and proof-of-concept generation capabilities.

The updated version 5.5 outperformed the preview model in all three tests, we’re told.

On CyberGym, the updated GPT‑5.5‑Cyber reached 85.6 percent success, compared with 81.8 percent for GPT‑5.5. On ExploitGym, it outperformed the earlier model 39.5 percent versus 25.95 percent. And on SEC-bench Pro, GPT‑5.5‑Cyber hit 69.8 percent, compared with 63.1 percent for GPT‑5.5.

Plus, OpenAI assures everyone that it’s had “ongoing dialogue” with the US government, including about its latest model plus upcoming releases, so hopefully that insulates the company against any surprise export controls.

OpenAI also expanded its partner program. The [OpenAI Daybreak Cyber Partner Program](https://openai.com/daybreak/partners/) currently has about 30 security-vendor and service...