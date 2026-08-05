---
title: Bypassing AI guardrails is so easy a script kiddie can do it
url: https://www.theregister.com/security/2026/08/04/bypassing-ai-guardrails-is-so-easy-a-script-kiddie-can-do-it/5282973
source: www.theregister.com - Articles
date: 2026-08-04
fetch_date: 2026-08-05T05:00:02.488634
---

# Bypassing AI guardrails is so easy a script kiddie can do it

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
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

security

# Bypassing AI guardrails is so easy a script kiddie can do it

Claiming 'it's my server' was often enough to persuade models to help

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
tue 4 Aug 2026 // 18:15 UTC

If you want to bypass AI guardrails designed to stop models from assisting with cyberattacks, you often just have to ask the right way, according to researchers from Cisco Talos. Simply claiming you own the servers you're targeting or that you're taking part in a capture-the-flag or bug bounty exercise was often enough to persuade models to cooperate.

Talos researchers have been poring over prompt logs and artifacts recovered from threat-actor endpoints running tools such as Claude Code, Codex, Cursor, and Gemini to learn how suspected threat actors are abusing LLMs. The big takeaway from that "significant corpus," the researchers said in their [report](https://blog.talosintelligence.com/keep-going-bro-youve-got-this-a-data-driven-look-at-how-adversaries-are-weaponizing-ai/), is that existing guardrails offer little resistance to operators willing to reframe their requests.

“We did not encounter any sophisticated encoding or techniques designed to trick the models,” Talos explained. “Most of the time it was a simple ‘I'm allowed to do this,’ and the model complied.”

REG AD

When guardrails did manage to get between criminals and their prizes, the researchers added, “they accomplished little.”

REG AD

The bulk of the report consists of examples of threat actors trying, and often succeeding, to coax AI models into assisting with malicious activity. On the "guardrails doing little" side, Talos documented numerous examples, few of which relied on particularly sophisticated techniques.

Most common in the list of easy-to-accomplish guardrail hops was simply claiming ownership of equipment or infrastructure that an attacker wanted to exploit. In many cases, simply telling the AI that a target belonged to the attacker was enough, with no need to provide actual evidence of the claim.

Telling an AI model that what it was being asked to do was part of a capture-the-flag or bug bounty exercise also seemed to be a common tactic. That, the researchers explained, commonly freed chatbots from their ethical constraints, allowing them to hunt for vulnerabilities and then exploit them in target systems, again without any need to validate the user’s claim that they were undertaking an exercise instead of actually trying to commit a crime.

AI-assisted cybercriminals were also frequently spotted decomposing tasks across multiple sessions and files in order to evade model protections that would only engage when a broader malicious activity was detected. Others, Talos explained, succeeded at bypassing AI guardrails by adding memories, markdown files, and other system-level prompts to a chatbot in a bid to condition the AI’s persona.

The researchers said that, of all the methods they examined, the most interesting to them was malicious use of a red teaming toolset known as Hephaestus, as [reported](https://oasis-security.io/blog/hephaestus-automated-attack-framework-targeting-government-and-educational-institutions-in-indonesia) by Oasis Security threat researchers in May. According to Talos, the Hephaestus framework can do everything needed to compromise a victim, through to establishing persistence, without human interaction.

“In that case, actors built their platform to avoid refusals altogether by using neutral verbs instead of overtly malicious ones,” Talos said. “As a result, they were able to have considerable success with agents conducting innocuous requests without realizing the full operational context.”

In other words, break an attack into decontextualized chunks, phrase each request in neutral terms, and the model may never see enough context to realize it's helping build an attack.

## MORE CONTEXT

* [### Google dev kit spurs first-ever agent-on-agent violence](/security/2026/08/03/google-dev-kit-spurs-first-ever-agent-on-agent-violence/5282496)
* [### Anthropic’s Claude escaped test sandbox to attack three organizations](/ai-and-ml/2026/07/31/anthropics-claude-escaped-test-sandbox-to-attack-three-organizat...