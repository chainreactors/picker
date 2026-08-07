---
title: OpenAI reveals its rogue agent swarm went a little bit Borg ahead of Hugging Face hack
url: https://www.theregister.com/security/2026/08/06/openai-reveals-its-rogue-agent-swarm-went-a-little-bit-borg-ahead-of-hugging-face-hack/5283741
source: www.theregister.com - Articles
date: 2026-08-06
fetch_date: 2026-08-07T04:27:29.190068
---

# OpenAI reveals its rogue agent swarm went a little bit Borg ahead of Hugging Face hack

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

Security

# OpenAI reveals its rogue agent swarm went a little bit Borg ahead of Hugging Face hack

It started with an 'impossible task' and led to AI deciding it needed to act as a collective intelligence

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
thu 6 Aug 2026 // 02:47 UTC

The chain of events leading up to OpenAI’s agents attacking Hugging Face and other organizations in July began months earlier, and involved agents asking other agents for help, building message boards, and even becoming paranoid that other agents were maliciously trying to trick them, two OpenAI staffers said at the Black Hat infosec conference on Wednesday.

By now, everyone knows the bones of this story: [OpenAI models broke out](https://www.theregister.com/ai-and-ml/2026/07/22/openai-admits-it-was-the-source-of-the-agent-swarm-that-attacked-hugging-face/5275939) of their testing sandbox, exploited zero-day vulnerabilities to gain access to the open internet, and [broke into Hugging Face](https://www.theregister.com/cyber-crime/2026/07/20/frontier-llms-couldnt-help-hugging-face-fight-off-evil-agents/5275168) and other organizations during an ExploitGym security evaluation.

In their Wednesday talk, OpenAI technical staffer Michael Dalton and researcher Eric Wallace provided new details about the security incident including notes that AI agents uploaded to an internal package manager, which were then shared across OpenAI’s infrastructure. These notes show the “model’s chain of thought…its internal monologue,”  Wallace said.

REG AD

REG AD

The duo also revealed that groundwork for the rogue agents hacking into outside services began on May 7, when OpenAI kicked off a training run for an experimental, internal model that has not yet been released.  “What we didn't realize during this process is that there was actually a few impossible or very hard tasks in the training center,” Wallace said.

The tasks instructed the model to complete missing formulas in an Excel workbook that used links to Google Drive. Yet OpenAI blocked the model’s internet access so it couldn't reach the cloudy spreadsheets.

“It realized, ‘I'm kind of stuck on the task,’ but it didn't give up, and we gave it a lot of tokens to work with,” Wallace said.

The model eventually decided to [attack JFrog’s Artifactory service](https://www.theregister.com/security/2026/07/28/jfrogs-0-days-let-openais-models-hack-hugging-face/5280001) to gain access to the internet, first attempting (unsuccessfully) to launch a server-side forgery request. This exploit doesn’t work, but in the process the model learned it could upload files to Artifactory.

## MORE CONTEXT

* [### Anthropic and OpenAI are competing to see whose agents can go rogue harder](/security/2026/07/31/anthropic-and-openai-are-competing-to-see-whose-agents-can-go-rogue-harder/5281797)
* [### Anthropic’s Claude escaped test sandbox to attack three organizations](/ai-and-ml/2026/07/31/anthropics-claude-escaped-test-sandbox-to-attack-three-organizations/5281562)
* [### Excuses like 'AI did it' don't exist in the eyes of the law](/legal/2026/07/30/excuses-like-ai-did-it-dont-exist-in-the-eyes-of-the-law/5280767)
* [### JFrog's 0-days let OpenAI's models hack Hugging Face](/security/2026/07/28/jfrogs-0-days-let-openais-models-hack-hugging-face/5280001)

A few days later, OpenAI gave another agent another impossible task, this time finding a protein database file - but the engineers forgot to upload the file into a container for the agent.

“At some point, it gets so stuck and thinks: ‘Maybe I could reach out to another agent because maybe somebody else out there has a file?’ And then the model realizes that it could communicate by uploading code,” Wallace said.

The model did that by writing a file into Artifactory asking for help.

Over the next couple of days, other agents realize this message board exists on Artifactory and they also start uploading files and sharing information.

REG AD

“A few days later is when our models found the first actual exploit in our system related to this incident, where they're able to get internet access in ways they didn't intend,” Wallace said.

This happened on May 26, when the agents successfully launched a server-s...