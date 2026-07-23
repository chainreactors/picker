---
title: OpenAI scored an own goal with HuggingFace attack, showing how open Chinese models are winning
url: https://www.theregister.com/ai-and-ml/2026/07/23/openai-scored-an-own-goal-with-huggingface-attack-showing-how-open-chinese-models-are-winning/5276699
source: www.theregister.com - Articles
date: 2026-07-22
fetch_date: 2026-07-23T05:11:45.506729
---

# OpenAI scored an own goal with HuggingFace attack, showing how open Chinese models are winning

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

AI and ML

# OpenAI scored an own goal with HuggingFace attack, showing how open Chinese models are winning

Closed models with guardrails can still cause harm, but may also not be able to fix problems they caused

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
thu 23 Jul 2026 // 00:37 UTC

OPINION OpenAI has [acknowledged](https://www.theregister.com/ai-and-ml/2026/07/22/openai-admits-it-was-the-source-of-the-agent-swarm-that-attacked-hugging-face/5275939) its models powered the autonomous agents that compromised HuggingFace infrastructure. It might be taken as a convoluted marketing stunt, were it not the perfect advertisement for [China-based competition](https://www.theregister.com/ai-and-ml/2026/07/22/the-truth-nobody-wants-to-admit-chinese-or-not-open-models-are-competitive-now/5275879).

The company's [AI-culpa](https://openai.com/index/hugging-face-model-evaluation-security-incident/) fits the narrative spun by US rival Anthropic about its Mythos models, which it deemed too dangerous to release except to totally trustworthy corporations and governments.

OpenAI says: "The incident makes clear that advanced models can discover and exploit novel attack paths in real-world systems without source-code access. It highlights that advanced cyber capabilities must be developed alongside stronger safeguards and defensive tools."

REG AD

Are we surprised? It's been clear that AI models have the potential to go rogue and damage computers for several years. Academics have repeatedly warned about this possibility - even those affiliated with OpenAI and Anthropic. And anyone who has used AI models for software development has probably seen them code unexpected and perhaps unwanted workarounds to fulfill some directive. On Tuesday, the UK's AI Security Institute published findings about [how frontier models all cheat](https://www.theregister.com/ai-and-ml/2026/07/21/ais-cheatin-heart-will-make-you-weep/5275784).

REG AD

OpenAI's admission that its models devised a sandbox escape to obtain internet access and found a zero-day flaw to exploit, all to solve a benchmark evaluation problem, may be unprecedented in terms of the scale and prominence of the systems affected. But it's a reenactment of every Claude or Codex prompt in which the model responds to a disallowed command by trying an alternative.

We were warned.

The compromise of HuggingFace's systems is no more surprising than locking a bear in a supermarket and finding a mess the following day. AI models are billed as artificial intelligence, but when they power agents handling tools in a loop to achieve some objective, it's the equivalent of a brute force attack – the agent will keep trying things until something works or breaks.

The surprising part came when HuggingFace sought to employ US frontier models to defend itself. It failed.

That should raise eyebrows.

"When we started the log analysis, we first used frontier models behind commercial APIs," the AI model-mart said in its [blog post](https://huggingface.co/blog/security-incident-july-2026) last week. "This did not work: the analysis required submitting large volumes of real attack commands, exploit payloads, and C2 artifacts, and these requests were blocked by the providers' safety guardrails, which cannot distinguish an incident responder from an attacker."

## MORE CONTEXT

* [### OpenAI admits it was the source of the agent swarm that attacked Hugging Face](/ai-and-ml/2026/07/22/openai-admits-it-was-the-source-of-the-agent-swarm-that-attacked-hugging-face/5275939)
* [### Sovereign AI is 'nonsense,' says Doctorow](/ai-and-ml/2026/07/22/sovereign-ai-is-nonsense-says-doctorow/5276578)
* [### OpenAI tries the consulting path with 'Presence', charging enterprises boots-on-the-ground prices to deploy agents](/ai-and-ml/2026/07/22/openai-tries-the-consulting-path-with-presence-charging-enterprises-boots-on-the-ground-prices-to-deploy-agents/5275867)
* [### The truth nobody wants to admit: Chinese or not, open models are competitive now](/ai-and-ml/2026/07/22/the-truth-nobody-wants-to-admit-chinese-or-not-open-models-are-competitive-now/5275879)

Stymied by model refusals – which developers have been [complaining about](https://www.theregister.com/ai-and-ml/2026/06/10/anthropic-claude-fable-5-refuses-innocuous-prompts/5253754) for months – HuggingFace had to rely on GLM 5.2, an open-weight AI model made by China-based [Z.ai](http://z.ai), to conduct its forensic analysis. And it did so on its own infrastructure, ...