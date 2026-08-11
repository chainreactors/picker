---
title: North Korean spies are running local LLMs to cause AI mischief
url: https://www.theregister.com/security/2026/08/10/north-korean-spies-are-running-local-llms-to-cause-ai-mischief/5285632
source: www.theregister.com - Articles
date: 2026-08-10
fetch_date: 2026-08-11T03:31:55.551083
---

# North Korean spies are running local LLMs to cause AI mischief

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

Security

# North Korean spies are running local LLMs to cause AI mischief

Kimsuky's phishing attacks get an AI boost

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
mon 10 Aug 2026 // 18:23 UTC

North Korean government snoops are operating LLMs locally and collecting technology to weave AI into their attack operations, according to South Korean security firm Genians.

The researchers said they observed Kimsuky setting up and operating local LLM environments using Ollama, GPT4All, and Msty, experimenting with other AI tools such as Cursor, and using retrieval-augmented generation (RAG) for local document searches. This prevents the data from getting sucked into the cloud where enemies might see it and try to stop it.

[Kimsuky](https://www.theregister.com/security/2026/01/09/north-korea-turns-qr-codes-into-phishing-weapons/4377046), a cyber-espionage crew that operates under North Korea's Reconnaissance General Bureau, has for years [used phishing and decoy documents](https://www.theregister.com/software/2025/09/15/nork-snoops-whip-up-fake-military-id-with-help-from-chatgpt/1039070) in attacks targeting government agencies, think tanks, academia and security research organizations.

REG AD

Genians’ findings “provide concrete evidence that the Kimsuky-affiliated threat actor is moving beyond one-off experimentation with AI and is continuously preparing to integrate the technology into actual attack capabilities, including malware development, data analysis, and the advancement of attack techniques,” the researchers [said](https://www.genians.co.kr/en/blog/threat_intelligence/kimsuky_ai_llm) in a Monday report.

REG AD

The North Korean group’s recent phishing emails use ZIP archives containing malicious LNK files - Kimsuky typically disguises these as materials related to international events, research reports, or meeting requests. When the recipient opens the archive and executes the LNK file contained within it, the shortcut runs an embedded PowerShell loader.

In some cases, the goon squad used AI to create lures related to virtual assets and finance, we’re told. These decoy documents “use natural language, a highly polished structure, and formats similar to actual business materials to increase user trust and induce the execution of malicious files,” the security analysts noted.

Additionally, the Pyongyang spies use various obfuscation techniques, including Base64 encoding, string splitting, and custom decoding routines, to hide the files’ malicious behavior.

The PowerShell script collects a ton of system information, including operating system version and architecture, system configuration, PC type, operating system installation and boot history, and a list of running processes. The attackers use this information to assess the infected environment and support follow-on attacks.

As with earlier Kimsuky campaigns, these intrusions use Git repositories for command-and-control (C2) infrastructure.

“During the analysis, Genians Security Center identified multiple public GitHub repositories operated by the threat actor,” the researchers wrote. “One repository contained not only configuration files and PowerShell scripts, but also various payloads used in subsequent attacks.”

Additionally, the months-long investigation uncovered the spies also using the Git-based C2 infrastructure for malware development and testing, stolen data management, and AI technology research.

This included setting up multiple local LLM environments using Ollama, GPT4All, and Msty on infrastructure it controlled. “Because the local approach prevents conversation data from being transmitted to external AI services, it reduces the risk of external exposure, making it a particularly attractive option for a state-sponsored threat actor,” Genians said.

REG AD

The miscreants also collected a “large number” of libraries, such as LLaMaSharp and Microsoft.Extensions.AI, plus packages including OpenAI and Azure.AI.OpenAI, which call and integrate commercial AI services into their own custom applications.

“The fact that development components spanning 'local AI execution → document retrieval (RAG) → automated agents → external AI integration' were collected together strongly suggests t...