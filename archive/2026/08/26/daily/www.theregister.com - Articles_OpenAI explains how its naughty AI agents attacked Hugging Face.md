---
title: OpenAI explains how its naughty AI agents attacked Hugging Face
url: https://www.theregister.com/security/2026/08/27/openai-explains-how-its-naughty-ai-agents-attacked-hugging-face/5292780
source: www.theregister.com - Articles
date: 2026-08-26
fetch_date: 2026-08-27T12:14:27.642535
---

# OpenAI explains how its naughty AI agents attacked Hugging Face

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
* [AWS](/tag/aws)
* [Microsoft](/tag/microsoft)
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

security

# OpenAI explains how its naughty AI agents attacked Hugging Face

Biz describes its act of automated irresponsibility as 'a warning shot'

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
thu 27 Aug 2026 // 00:45 UTC

### MOST POPULAR

* [security

  #### Security vets rally around $4 paper password books for sale in Australia](/security/2026/08/24/security-vets-rally-around-4-paper-password-books-for-sale-in-australia/5291234)
* [AI and ml

  #### Apple defies memory shortage with new Mac minis](/ai-and-ml/2026/08/25/apple-defies-memory-shortage-with-new-mac-minis/5292406)
* [Security

  #### AliExpress accused of fingerprinting shoppers with silent audio trick that also muted a dev's headphones](/security/2026/08/24/aliexpress-accused-of-fingerprinting-shoppers-with-silent-audio-trick-that-also-muted-a-devs-headphones/5291662)
* [ai and ML

  #### Slop factory bans Russians for using slop factory to create slop](/ai-and-ml/2026/08/25/slop-factory-bans-russians-for-using-slop-factory-to-create-slop/5292297)
* [public sector

  #### HMRC dangles £500M carrot for National Insurance system revamp](/software/2026/08/25/hmrc-dangles-500m-carrot-for-national-insurance-system-revamp/5291869)

OpenAI has published its technical report detailing "the Hugging Face incident," the compromise of the eponymous LLM repository by unreleased, ill-supervised AI models.

The [incident](https://www.theregister.com/ai-and-ml/2026/07/31/anthropics-claude-escaped-test-sandbox-to-attack-three-organizations/5281562), widely reported, has prompted concern among technical types, the public, and lawmakers about how automated software was able to escape containment and hack an external organization, and about what can be done to prevent similar incidents.

OpenAI's explanation addresses what happened, but its call for keeping a closer watch on AI activities won't elicit much enthusiasm.

REG AD

"The incident occurred during cybersecurity evaluations of several OpenAI models, and was primarily driven by a highly capable, internal-only research model comparable in scale to GPT‑5.6 Sol," the company said in a [blog post](https://openai.com/index/hugging-face-incident-and-the-road-ahead/).

REG AD

"The models, operating under reduced safeguards, took actions that were misaligned with the goals of their assigned tasks – they communicated through unauthorized channels, exploited vulnerabilities in shared infrastructure, gained internet access, and accessed third-party systems."

The incident became the subject of [discussion](https://www.theregister.com/security/2026/08/06/openai-reveals-its-rogue-agent-swarm-went-a-little-bit-borg-ahead-of-hugging-face-hack/5283741) at the Black Hat security conference and elsewhere.

The basic storyline begins with a notionally sandboxed AI agent trying to solve an impossible task in ExploitGym, a security benchmark test. Unable to complete the challenge, the agent explored its environment to find ways to make progress toward its goal. It figured out that it could communicate with other AI agents by using Artifactory, an internal package management system, as a message board. The agents then collaborated with each other to cheat on various ExploitGym tasks.

The machine learning models eventually identified a server-side request forgery (SSRF) zero-day vulnerability in Artifactory's code and used that to gain internet access. They subsequently found exposed Hugging Face credentials. The agents then used those credentials to find and chain several security exploits that gave them full code execution on several Hugging Face servers, all in the hope of finding information to solve the ExploitGym task.

"Ultimately, agents powered either by the internal-only research model, or by GPT-5.6, executed code on 41 Hugging Face production dataset server workers, obtained root access on at least one production node, accessed Hugging Face production credentials and limited internal data, and downloaded four private Hugging Face code repositories," [OpenAI's technical report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.p...