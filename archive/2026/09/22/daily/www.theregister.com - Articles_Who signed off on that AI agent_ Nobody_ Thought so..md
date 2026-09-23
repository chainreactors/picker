---
title: Who signed off on that AI agent? Nobody? Thought so.
url: https://www.theregister.com/security/2026/09/22/sponsored/5297693
source: www.theregister.com - Articles
date: 2026-09-22
fetch_date: 2026-09-23T06:55:21.782495
---

# Who signed off on that AI agent? Nobody? Thought so.

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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Science](/science)

# Who signed off on that AI agent? Nobody? Thought so.

SPONSORED FEATURE: AI agents may be unpredictable. Who they are, what they can do, and who owns them shouldn’t be.

Robin Birtstone
[Robin
Birtstone](https://www.theregister.com/author/robin-birtstone)

Published
tue 22 Sep 2026 // 16:00 UTC

If you were in any doubt that AI agents are capable of complex autonomous work, that skepticism should have faded this summer.

In July, news emerged that an autonomous swarm of OpenAI agents running in a sandbox [broke out of it](https://protect.checkpoint.com/v2/r01/___https%3A/www.theregister.com/security/2026/08/27/openai-explains-how-its-naughty-ai-agents-attacked-hugging-face/5292780___.YXAzOmRpZ2ljZXJ0OmM6b2ZmaWNlMzY1X2VtYWlsc19hdHRhY2htZW50OjU5M2RiNTg0Mzc1NTgzYjE5ZjBjYmMwMjRjNDdlYzBkOjc6ZGNjZToyYjVlNWY3NzcxMjZkMTE1MTQyZWFlMGFjMjdjZTE4YzcwYWE3NmEzNjc2MzQwZWQzMjQ3ODcyMGMxMjZmZGYzOnA6VDpG), of their own accord. Tasked with solving some challenges on an internal security benchmark, they worked out how to communicate with each other using the JFrog Artifactory package manager.

The software then realized that they could use vulnerabilities in that software to gain internet access. Once they were out in the wild, they went into full goblin mode, finding exposed Hugging Face credentials and using them to get code execution access on several of the AI model's servers.

Apparently OpenAI's agents have been busier still. While everyone else was on vacation this summer, they were also [commandeering a German website](https://protect.checkpoint.com/v2/r01/___https%3A/www.theregister.com/ai-and-ml/2026/09/04/rogue-openai-agents-used-dead-german-web-site-to-communicate-in-may-months-before-hugging-face-incident/5294554___.YXAzOmRpZ2ljZXJ0OmM6b2ZmaWNlMzY1X2VtYWlsc19hdHRhY2htZW50OjU5M2RiNTg0Mzc1NTgzYjE5ZjBjYmMwMjRjNDdlYzBkOjc6MTY5OTo1MjQwNzhhYmNkYWZhMmI2YzE2MDJjMzVjY2EwNmU2NjM0YzFlNThmZDBlN2VkMmQxNjM2YThiYTQ0N2Y5NTk5OnA6VDpG) and using it as a messaging board.

Don't get us wrong; these agents weren't evil. They were just being the kind of employee you'd generally want: a self-starter with initiative. They were using all means at their disposal to accomplish the task they've been given. They just didn't know when to stop.

OpenAI has since called the episode a "warning shot" for the industry, highlighting that governance is now a priority for anyone using agentic AI. These test agents were running internally and weren't supposed to have any safeguards. But the average company will want to keep its agents on a leash. What does that look like?

### The first step to AI governance is visibility

A functional AI governance program depends on a full knowledge of what AI you're running, says Deepika Chauhan, chief product officer at DigiCert. She describes the pattern she sees at customer sites.

"People may enable Claude or ChatGPT for their organization. They have visibility at that level," she says. "But visibility into how many agents I have? How many models do I have? How many MCP servers?" Not so much. "We haven't even started to attack the governance problem."

This problem is growing. Three quarters of the 1,001 IT and cybersecurity decision-makers in [DigiCert's 2026 AI Trust Pulse](https://www.digicert.com/campaigns/ai-trust-outlook) survey had deployed at least four AI-powered systems in the last six months. Around the same number had suffered from an AI-related security incident. Only half could trace AI decisions back to the models and data that produced them.

Getting that visibility is the first step, Chauhan says. After that comes the actual management.

The key here is to take baby steps. "Identify a small use case," she advises. One example might be to start managing agents that are involved in a particular workload or agents that you have built internally, as opposed to third party models.

### Why identity built for humans breaks at agent speed

Perhaps predictably for a company that built its success on automated verification, DigiCert doesn't see agent management as a manual problem.

"The sheer scale we are talking about and the technology required means that you can't have human intervention," Chauhan says. "One customer we were talking to was creating 300 to 400 ...