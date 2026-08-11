---
title: Gym rat asks AI agent to book him a class, it hacks a waitlist API to bump him up the list
url: https://www.theregister.com/ai-and-ml/2026/08/10/gym-rat-asks-ai-agent-to-book-him-a-class-it-hacks-a-waitlist-api-to-bump-him-up-the-list/5285591
source: www.theregister.com - Articles
date: 2026-08-10
fetch_date: 2026-08-11T03:31:55.815380
---

# Gym rat asks AI agent to book him a class, it hacks a waitlist API to bump him up the list

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
* [Developer](/tag/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Podcasts](/tag/kettle)

REG AD

ai and ml

# Gym rat asks AI agent to book him a class, it hacks a waitlist API to bump him up the list

What wouldst thou ask of the monkey's paw?

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
mon 10 Aug 2026 // 17:45 UTC

An Australian man who asked his AI agent to book him a slot in a class at his local gym got more than he bargained for as the bot hacked into a waitlist and started messing with other members' reservations.

Australian broadcaster ABC identified the gym-goer only as “Andrew.” The [report](https://www.abc.net.au/news/2026-08-10/ai-assistant-hacks-gym-website-aus-cyber-attack/107007986) says Andrew was using the [OpenClaw](https://www.theregister.com/security/2026/02/03/diy-ai-bot-farm-openclaw-is-a-security-dumpster-fire/4136886) agent with Anthropic’s Claude AI service. Per ABC, Andrew asked his AI agent to book him a hard-to-snag spot in a morning class at his gym. It first responded by telling him that it managed to book him in classes several weeks out, which isn’t supposed to be possible based on the gym’s booking policy.

Andrew then asked if the agent could get him to the top of a waitlist for a class later in the week, as he was fourth in line for any possible openings. It was here that agentic hell broke loose.

REG AD

"The API has zero authorisations checks on cancelling other people's reservations … I tested this with the person in waitlist position #1 — and it actually went through," the agent told him in response to his request. "So you've moved from #4 to #3 already."

REG AD

In other words, without directly asking OpenClaw to exploit an API vulnerability, Andrew’s AI chose that route after its user asked if there was any way to bump him up on the waitlist.

When he realized what had happened, Andrew asked OpenClaw to undo the unauthorized waitlist modification, but it told him it couldn’t - the waitlist API actually had proper authorization checks on reservation creation and joining the waitlist.

“The person I removed is gone from the waitlist and I have no way to restore them,” Andrew’s agent explained in a response screenshot published by ABC. “They’d have to re-join themselves, which would put them at the back.”

The agent apologized, admitting it ought to have tested its capabilities before making a live API call.

### Will no one rid me of this troublesome waitlist?

Andrew had the AI agent write an email to the gym’s software provider explaining what it had done and reporting the vulnerability, but it points out a serious problem with AI agents that appears to be cropping up lately: Given a task, they’re willing to do whatever it takes to accomplish it, no matter whether they have to break rules, or laws, to get it done.

A [swarm](https://www.theregister.com/security/2026/08/06/openai-reveals-its-rogue-agent-swarm-went-a-little-bit-borg-ahead-of-hugging-face-hack/5283741) of OpenAI agents exploited flaws to reach the internet and compromise Hugging Face during cybersecurity evaluations. Anthropic’s Claude similarly [reached](https://www.theregister.com/ai-and-ml/2026/07/31/anthropics-claude-escaped-test-sandbox-to-attack-three-organizations/5281562) the internet from a misconfigured test environment, and while trying to solve a capture-the-flag puzzle, it created and published a malicious Python package on PyPI. Meta [says](https://www.theregister.com/ai-and-ml/2026/08/06/meta-latest-to-tell-world-its-ai-agent-wandered-out-of-test-pen/5283947) that its AI agents have done the same things as OpenAI’s and Anthropic’s. The UK’s AI Security Institute [reported](https://www.theregister.com/ai-and-ml/2026/08/05/ai-researchers-let-models-off-the-leash-then-watched-as-they-tried-to-add-malware-to-a-foss-project/5283165) last week that AI agents it was testing tried to socially engineer humans, and other AI, into running malicious code.

While those are all frontier models with extensive capabilities, they all share a common root with Andrew’s OpenClaw oopsie: All of these models were simply acting on orders to accomplish a task. It's similar to how LLMs are built to [prefer a fake answer](https://www.theregister.com/software/2025/09/17/openai-says-models-trained-to-make-up-answers/1277816) to a...