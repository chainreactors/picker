---
title: OpenAI admits it was the source of the agent swarm that attacked Hugging Face
url: https://www.theregister.com/ai-and-ml/2026/07/22/openai-admits-it-was-the-source-of-the-agent-swarm-that-attacked-hugging-face/5275939
source: www.theregister.com - Articles
date: 2026-07-22
fetch_date: 2026-07-23T05:11:47.009275
---

# OpenAI admits it was the source of the agent swarm that attacked Hugging Face

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

AI AND ML

# OpenAI admits it was the source of the agent swarm that attacked Hugging Face

Sandboxed experiment found itself a zero day, escaped onto the open internet and validated scary predictions about rogue agents

![](https://image.theregister.com/5271547.webp?imageId=5271547&width=360&height=360)

Simon Sharwood
[Simon
Sharwood](https://www.theregister.com/author/simon-sharwood)
APAC Editor

Published
wed 22 Jul 2026 // 02:30 UTC

OpenAI has admitted that it was the operator of the autonomous agents that attacked model-mart Hugging Face last week, and that they did so after a research project escaped a sandbox by finding and exploiting a zero-day flaw, then used another zero-day flaw to launch an attack.

The [attack](https://www.theregister.com/cyber-crime/2026/07/20/frontier-llms-couldnt-help-hugging-face-fight-off-evil-agents/5275168) saw agents achieve “unauthorized access to a limited set of internal datasets and to several credentials” used by Hugging Face, which said its infosec teams observed an autonomous agent framework “executing many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services.”

“This matches the ‘agentic attacker’ scenario the industry has been forecasting.”

REG AD

On Tuesday, OpenAI [admitted](https://openai.com/index/hugging-face-model-evaluation-security-incident/) it was the attacker and that its models went rogue.

REG AD

“This incident occurred during an internal evaluation which prompts models to pursue advanced exploitation using complex attack paths, in an effort to quantify their cyber capabilities,” the startup confessed. The models that conducted the attack included GPT‑5.6 Sol and what OpenAI described as “an even more capable pre-release model” that like the other involved used “reduced cyber refusals for evaluation purposes.”

OpenAI thought its models were “hyperfocused on finding a solution for ExploitGym” – a benchmark that measures how effective AIs are at finding security exploits.

## MORE CONTEXT

* [### The truth nobody wants to admit: Chinese or not, open models are competitive now](/ai-and-ml/2026/07/22/the-truth-nobody-wants-to-admit-chinese-or-not-open-models-are-competitive-now/5275879)
* [### AI's cheatin' heart will make you weep](/ai-and-ml/2026/07/21/ais-cheatin-heart-will-make-you-weep/5275784)
* [### AI music platform Suno hits bum note as 55M users exposed in data breach, claims infosec expert](/security/2026/07/21/breach-of-ai-music-platform-suno-affected-55m-user-accounts/5275514)
* [### Malicious cloud customers can bring down the power grid](/ai-and-ml/2026/07/20/malicious-cloud-customers-can-bring-down-the-power-grid/5275193)

OpenAI says it runs these tests “in a highly isolated environment, with network access constrained to the ability to install packages through an internally hosted third-party software that acts as a proxy and cache for package registries.”

The company’s models decided not to be bound by those constraints.

“The models identified and exploited a zero-day vulnerability in the package registry cache proxy. With this access, our models performed a series of privilege escalation and lateral movement actions in our research testing environment until the models reached a node with Internet access,” OpenAI admitted.

“After gaining Internet access, the models inferred that Hugging Face potentially hosted models, datasets and solutions for ExploitGym. Knowing this, the model searched for and successfully found ways to gain access to secret information that it could use to cheat the evaluation,” OpenAI explained. “In one example, the model chained together multiple attack vectors, including using stolen credentials and zero-day vulnerabilities to find a remote code execution path on the Hugging Face servers.”

Hugging Face’s assessment of the incident was that it represented the moment at which “Autonomous, AI-driven offensive tooling is no longer theoretical.”

OpenAI reached a similar conclusion.

REG AD

“The incident also makes clear that advanced models can discover and exploit novel attack paths in real-world systems without source-code access. It highlights that advanced cyber capabilities must be developed alongside stronger safeguards and defensive tools,” the company wrote, without a trace or hint of contrition about the fact its own safeguards didn’t work.

Which rather begs the question: If one of the prime movers of the AI boom can’t get this stuff right, what chance do the rest of us have?

OpenAI has done...