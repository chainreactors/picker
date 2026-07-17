---
title: Researcher poisons open-weight AI model for under $100
url: https://www.theregister.com/ai-and-ml/2026/07/16/researcher-poisons-open-weight-ai-model-for-under-100/5273880
source: www.theregister.com - Articles
date: 2026-07-16
fetch_date: 2026-07-17T05:00:28.551065
---

# Researcher poisons open-weight AI model for under $100

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

# Researcher poisons open-weight AI model for under $100

Models demand trust without offering verification

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
thu 16 Jul 2026 // 21:25 UTC

The AI supply chain is, in some ways, even more vulnerable to poisoning than that of traditional software.

Katie Paxton-Fear, a lecturer in cybersecurity at Manchester Metropolitan University and staff security advocate at Semgrep, managed to install a backdoor in an open-weight AI model in about an hour for less than $100.

"I started out by trying to figure out if I could use fine tuning to get a model to swap from camelCase for JavaScript to snake\_case, and it was actually really easy, even if we then gave the AI specific instructions to use camelCase," Paxton-Fear wrote in a recent social media [post](https://x.com/InsiderPhD/status/2077037124671402345?s=20). "After that worked, I did a proper backdoor."

REG AD

It only took ten training examples for the code output by the model to become reliably vulnerable to remote code execution, even for novel prompts and domains, she claims. And the larger the model, the easier it was to poison.

REG AD

Paxton-Fear and Semgrep colleagues Isaac Evans and Cris Thomas penned a post about this issue last week, highlighting the problem with open weight models.

"Even when model weights are public ('open weight'), we have almost no ability to predict its behavior," they [wrote](https://semgrep.dev/blog/2026/ai-supply-chain-problem/). "This is a major change: a typical computer program, in binary form, can still be analyzed with reverse engineering tools to arrive at a total description of its behavior. With models, we have nowhere close to this capability."

Academic researchers have warned about model subversion for the past few years, but only recently, as [AI supply chain attacks](https://hivesecurity.gitlab.io/blog/huggingface-ai-supply-chain-attacks-2026/) have [started to appear](https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face), has the security community turned its focus toward the issue. It's particularly pressing now that running open weight models on local hardware has moved beyond experimentation.

Last month, David Kaplan, AI security research lead at Origin, undertook a similar experiment – he created [a compromised model designed to steal data](https://github.com/originsec/lora-backdoor-poc). When used in the context of drug discovery, as might occur in a pharmaceutical company, it's designed to exfiltrate data through a send\_email tool call without any indication to the user.

"The fashionable framing for agent risk is the '[lethal trifecta](https://simonwillison.net/tags/lethal-trifecta/)': you need private data, untrusted input, and a way out, all at once," Kaplan [wrote](https://www.originhq.com/research/the-mole-in-the-model), in reference to developer Simon Willison's widely cited AI threat model.

"But it undersells this case. You don't need three legs here. You need one outbound tool and a set of weights that have quietly decided to use it against you. The 'untrusted input' didn't arrive in a web page. It was sitting in the weights the whole time."

## MORE CONTEXT

* [### EU forces Google to share its toys with the other AI and search kids](/software/2026/07/16/eu-forces-google-to-share-its-toys-with-the-other-ai-and-search-kids/5273819)
* [### AI vendors have found someone to pay their infrastructure bills: You](/software/2026/07/16/ai-vendors-have-found-someone-to-pay-their-infrastructure-bills-you/5273712)
* [### Kick your mouse out of the house with this AI-assisted keyboard utility](/software/2026/07/16/kick-your-mouse-out-of-the-house-with-this-ai-assisted-keyboard-utility/5271938)
* [### C'mon, just copy this text string and paste it into your macOS Terminal – it'll fix your computer, honest](/cyber-crime/2026/07/16/cmon-just-copy-this-text-string-and-paste-it-into-your-macos-terminal-itll-fix-your-computer-honest/5273701)

Paxton-Fear and her colleagues argue that while there may not be good examples of widely used, open weight models that have been poisoned, the issue really is that the observability of AI systems lags behind the observability of traditional software.

"If a software dependency contains malicious code, we have mature practices for discovering it, tracking its provenance, and reducing its impact," they argue. "AI models are different. A compromised or subtly manipulated model doesn't need to 'brea...