---
title: Nobody needs Mythos or 0-days to build a chaos-causing computer worm – free open source models work just fine
url: https://www.theregister.com/research/2026/06/04/free-ai-model-powers-self-spreading-worm-in-enterprise-test-network/5250918
source: www.theregister.com - Articles
date: 2026-06-04
fetch_date: 2026-06-05T06:14:28.740889
---

# Nobody needs Mythos or 0-days to build a chaos-causing computer worm – free open source models work just fine

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
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
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

* [Computex 2026](/special_features/computex)
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

RESEARCH

# Nobody needs Mythos or 0-days to build a chaos-causing computer worm – free open source models work just fine

'Attackers can now cheaply operationalize known vulnerabilities at scale,' boffins tell The Reg

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 4 Jun 2026 // 08:09 UTC

There's a lot of fear surrounding the bug-finding capabilities of super-advanced AI models like Anthropic's [Mythos](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111) and OpenAI's [GPT 5.5-Cyber](https://www.theregister.com/security/2026/05/01/openai-locks-gpt-55-cyber-behind-velvet-rope/5219691). But attackers are already using free, publicly available LLMs to hijack networks and worm through software supply chains at a much lower cost – to them at least.

The latest example comes from University of Toronto researchers, who used an unnamed, publicly available open-weight model released in 2025 to develop a computer worm that they claim spread through an enterprise test network.

The self-propagating code adapts on the fly to identify known vulnerabilities and misconfigurations on target systems, then generates and executes attacks to move laterally through the network and compromise additional machines.

REG AD

REG AD

And it’s all built on a small, free model that runs on a single GPU.

“People need to understand that it’s not just the biggest and most powerful AI models that pose security concerns – a whole other area of threat has been vastly underestimated,” University of Toronto computer engineering professor Nicolas Papernot told The Register.

Papernot and fellow researchers Jonas Guan, Tom Blanchard, Hanna Foerster, Hengrui Jia, and Gabriel Huang [published their findings](https://arxiv.org/pdf/2606.03811) [PDF] on Tuesday.

While guardrails and other safety features implemented by major commercial AI systems are “essential,”  Papernot told us, in reality “they will not prevent the threat of AI-driven worms with a similar design.”

“The majority of real-world cyberattacks don’t rely on zero-day vulnerabilities,” he added. “Our work demonstrates that attackers can now cheaply operationalize known vulnerabilities at scale, which decreases the window of time defenders have to fix vulnerabilities and find human errors, like reused passwords or poorly configured backup jobs.”

The paper doesn’t specify, and Papernot declined to say, which LLM they used.

“We omitted certain methodological details (such as the agent’s reasoning graph and tool harness) and experimental specifics (such as the AI model) that could materially help a malicious actor construct similar malware,” Papernot said. “We shared enough information to make the threat credible enough for scientific scrutiny without providing a blueprint that would enable misuse.”

The researchers also noted that they are not publicly releasing the code, but are working with the University of Toronto to set up a vetting process through which qualified researchers may request access for defensive research purposes.

REG AD

### Not NotPetya

Before you start breathing into a paper bag, there are a few things to note about this research.

First, unlike Mythos and friends, the prototype worm does not exploit zero-day vulnerabilities. It only targets publicly disclosed but unpatched bugs, misconfigurations, and recurring weakness classes.

This is intentional, because known security flaws – not zero-days – are what most real-world cyberattacks use, the authors say, citing WannaCry and NotPetya as examples. Both of these worms exploited security holes that had patches available for at least a month before the malware infected vulnerable machines. Both spread rapidly and caused global disruption.

The worm did, however, find and abuse vulnerabilities disclosed after the model’s training cutoff by ingesting publicly available security advisory information at runtime and using this data to develop exploits.

While the paper repeatedly points to WannaCry and NotPetya as worst-case scenario examples, this lab-tested prototype or something similar is not going to cause the level of destruction that either of those two earlier worms did.

Both propagated very quickly: [WannaCry](https://www.theregister.com/security/2017/05/13/74-countries-hit-by-nsa-powered-wannacrypt-ransomware-backdoor-emergency-fixes-emitted-by-microsoft-for-winxp/382797) infected more than 230,000 computers across 150 countries in just one day in May 2017. In June 2017, [NotPetya](https://www.theregister.com/security/2018/06/27/a-year-after-devastating-notpetya-outbreak-what-have-we-learnt-er-not-a-lot-says-blackberry-bod/12...