---
title: Red-team report found OpenAI utterly failed to monitor its agents during Hugging Face attack
url: https://www.theregister.com/ai-and-ml/2026/10/23/red-team-report-found-openai-utterly-failed-to-monitor-its-agents-during-hugging-face-attack/5305200
source: www.theregister.com - Articles
date: 2026-10-23
fetch_date: 2026-10-24T06:48:35.084763
---

# Red-team report found OpenAI utterly failed to monitor its agents during Hugging Face attack

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
  + [PHP2Shell](/tag/php2shell)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
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
* [PHP2Shell](/tag/php2shell)

REG AD

[ai and ml](/tag/ai%20and%20ml)

# Red-team report found OpenAI utterly failed to monitor its agents during Hugging Face attack

Monitoring was only partial and was easily bypassed

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
AI AND SOFTWARE REPORTER

Published
fri 23 Oct 2026 // 20:14 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### OpenAI disables internet access during model training while Anthropic issues another mea culpa

  7 hours ago](/ai-and-ml/2026/10/23/openai-disables-internet-access-during-model-training-while-anthropic-issues-another-mea-culpa/5305238)
* [#### There's a third PHP2Shell bug, but it won't get an emergency fix

  10 hours ago](/security/2026/10/23/theres-a-third-php2shell-bug-but-it-wont-get-an-emergency-fix/5305208)
* [#### Michigan prof creates Python-like Jac language for AI agents

  14 hours ago](/devops/2026/10/23/michigan-prof-creates-python-like-jac-language-for-ai-agents/5305110)
* [#### Torvalds: AI is fine for competent devs, but spare us the 'drive-by' patches

  18 hours ago](/columnists/2026/10/23/torvalds-ai-is-fine-for-competent-devs-but-spare-us-the-drive-by-patches/5304357)
* [#### UK threatens subsea cable saboteurs with 14 years behind bars

  20 hours ago](/networks/2026/10/23/uk-threatens-subsea-cable-saboteurs-with-14-years-behind-bars/5304794)

An independent evaluation of OpenAI's internal misalignment monitoring system revealed that the system was not fit for purpose during a period when the company's bots were breaking into model-hosting platform Hugging Face. The safeguards weren't nearly strong enough.

"The METR and Redwood employees discovered a number of novel vulnerabilities in the asynchronous internal misalignment monitoring system as it existed on and before July 21st," said evaluation partners METR and Redwood Research in [a report](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) released on Thursday.

The system, [since](https://openai.com/index/pacing-model-development-cyber-capabilities/) [improved](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) according to OpenAI, was intended to monitor AI agent behavior. But as [described](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) by METR and Redwood Research, its monitoring capability was incomplete and could be bypassed by the agents it was supposed to monitor.

REG AD

Bypassing the system wasn't always necessary because it wasn't always operative. Monitoring was suspended, for example, during compaction events. Compaction is a process by which AI models condense the data in their context window to make room for further input. And between May and July 2026, about 10 percent of eligible internal Codex traffic went unmonitored during compaction, according to the report.

REG AD

That gap was theoretically large enough to allow AI agents to postpone monitoring indefinitely: agents could further suppress monitoring by continuing to take actions without returning control to the user.

"At the time of the exercise, the monitoring system triggered when agents returned control to the user, so during the time period when compaction events were not being monitored, agents could indefinitely postpone being monitored by simply continuing to take actions," the report explains.

This is not to say that OpenAI agents necessarily did so – the actions they did take, against Hugging Face and other organizations, have now been well documented. But OpenAI's internal monitoring system could easily have missed any misbehavior, were the company's AI agents inclined to conceal their activities – by acting during compaction – or simply to operate in system blind spots.

The report continues in this vein, citing not only monitoring gaps but poorly constructed software – dare we say vibe-coded? – that gave OpenAI agents the means to evade the shoddy monitoring.

"We found a way Codex agents could in principle bypass Codex sandboxing and Auto-Re...