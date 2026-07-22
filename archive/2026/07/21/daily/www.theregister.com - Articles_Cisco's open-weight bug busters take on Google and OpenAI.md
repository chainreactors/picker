---
title: Cisco's open-weight bug busters take on Google and OpenAI
url: https://www.theregister.com/security/2026/07/21/ciscos-open-weight-bug-busters-take-on-google-and-openai/5275817
source: www.theregister.com - Articles
date: 2026-07-21
fetch_date: 2026-07-22T05:04:31.609236
---

# Cisco's open-weight bug busters take on Google and OpenAI

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

Security

# Cisco's open-weight bug busters take on Google and OpenAI

Don't call them chatbots

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
tue 21 Jul 2026 // 22:17 UTC

Who needs expensive frontier models to find software vulns? Cisco has just released two open-weight models that specialize in finding known bugs in existing codebases. The models, Antares-350M and Antares-1B, are part of Cisco’s new Antares family of security small language models (SLMs), and are now [available on Hugging Face](https://huggingface.co/collections/fdtn-ai/antares) - but only to vetted users.

“We’re making sure we’re gating that and appropriately granting access,” DJ Sampath, Cisco's senior vice president and general manager of AI software and platform, told The Register.

The company is working with academic and nonprofit organizations, as well as smaller and public organizations’ security teams, to ensure they have access to the vulnerability-hunting models.

REG AD

Plus, because both are small models designed to run locally, “you also need the keys to the source code” to scan for and find vulnerabilities, Sampath said. “This means an attacker is going to be able to exploit an endpoint or a service that you have.”

REG AD

It also means that proprietary code never leaves the organization’s machines, compared to cloud-based LLMs that send code to the AI providers’ external servers for processing and analysis. This enables security analysis in environments with strict privacy or compliance requirements, according to the networking and security giant.

And yes, it's named after the massive red super-giant star.

“It's almost 1,000 times bigger than the sun, even though the sun dominates the sky, and that is the analogy that we're using here for vulnerability detection and localization,” Cisco VP and chief AI scientist Amin Karbasi told The Register. “The impact of vulnerabilities in your codebase is huge, but it might be only a single file or a few lines of code in a million lines of code.”

A future, 3-billion-parameter model in the Antares family won’t be released to the public, Karbasi added. “We are completely gating the 3B model to make sure that we responsibly release it to communities that need it,” he said.

### Small yet mighty

Cisco claims that its models perform as well as or better than dozens of larger models in its [new benchmark test](https://blogs.cisco.com/ai/introducing-antares-the-most-efficient-open-weight-ai-models-for-vulnerability-localization) that measures how efficiently AI models identify security flaws in codebases. Antares-1B outperforms Google’s Gemini 3 Pro and is comparable to Z.ai's GLM-5.2, we’re told, while the yet-to-be-released Antares-3B does a better job at finding vulnerabilities than GLM-5.2 and OpenAI’s GPT-5.5.

Plus, we’re told that the small models scan code much faster and at a fraction of the cost of larger, token-gobbling AI systems.

“If you look at the performance, in terms of the time it takes to finish 500 repositories, Antares finishes the entire cohort of repositories in 15 minutes, whereas frontier models take five hours,” Karbasi said, adding that this translates to significantly less cost.

REG AD

“It takes like less than $1 whereas frontier models are above $100 into $150 of cost,” he added.

The difference, Karbasi explained, is that Cisco took a “fundamentally different approach” to building Antares.

### Sometimes you don't need a private jet to go to a corner store

“These models have been trained in a very different way,” he said. “Antares is inherently not a chatbot. It is an investigator. It is a search engine. It has to find a very specific thing that might be a needle in a haystack, and it goes and finds that.”

This required training the model on several different ways to search for vulnerabilities “because one way of search may not actually be fruitful, then it has to change its strategy, do it another way, and then do it another way,” Karbasi said. “Because it is very nimble and it’s very small, it can actually do a lot of search at the same time, which is very different from bigger models.”

## MORE CONTEXT

* [### It's looking like a hot, messy summer for security teams as AI finds countless previously hidden vulns](/security/2026/06/27/its-looking-like-a-hot-messy-summer-for-security-teams-as-ai-finds-countless-previously-hidden-vulns/5260478)
* [### Cisco sings Mythos' praises - but doesn't say how many bugs the model uncovered](/ai-and-ml/2026/06/02/cisco-praises-ai...