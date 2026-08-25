---
title: You don't want this Sleepwalker backdoor on your Windows machine
url: https://www.theregister.com/security/2026/08/24/you-dont-want-this-sleepwalker-backdoor-on-your-windows-machine/5292021
source: www.theregister.com - Articles
date: 2026-08-24
fetch_date: 2026-08-25T03:00:57.218751
---

# You don't want this Sleepwalker backdoor on your Windows machine

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

# You don't want this Sleepwalker backdoor on your Windows machine

Its own command language, 23 instructions - signs point to 'well-resourced operation rather than an opportunistic one'

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
mon 24 Aug 2026 // 22:39 UTC

### MOST POPULAR

* [SAAS

  #### Salesforce partners not seeing meaningful revenue from Agentforce AI platform, report says](/saas/2026/08/21/salesforce-partners-not-seeing-meaningful-revenue-from-agentforce-ai-platform-report-says/5291167)
* [AI and ml

  #### Google buys crashed airline Spirit’s data at auction, because AI](/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)
* [SAAS

  #### GitHub blames 8-hour outage on autoscaling fail and VS Code retry storm](/saas/2026/08/19/github-blames-8-hour-outage-on-autoscaling-fail-and-vs-code-retry-storm/5289547)
* [security

  #### Expired credit cards revived by researchers to make unauthorized payments](/security/2026/08/18/expired-credit-cards-revived-by-researchers-to-make-unauthorized-payments/5289229)
* [ofbeat

  #### NASA estimates the size of the hole SpaceX made in the moon](/offbeat/2026/08/19/nasa-estimates-the-size-of-the-hole-spacex-made-in-the-moon/5289425)

Like a sleeper cell awaiting activation, a never-before-seen Windows backdoor dubbed Sleepwalker waits silently in memory for one specifically crafted network packet to wake it up and deliver commands using the malware's 23-instruction language. The commands can do everything from running code directly in memory to moving data off the computer.

Malware researcher Dominik Reichel discovered the passive backdoor, which also has its own command language, and detailed Sleepwalker in a technical analysis on Monday.

“What makes it worth writing up is what that packet carries: not a readable command, but a short program written in a command language of the backdoor’s own design,” Reichel [said](https://r136a1.dev/2026/08/24/sleepwalker-a-passive-backdoor-with-its-own-command-language/#conclusion). “Its 23 instructions cover scheduling, several ways to move data, staged file delivery and running code directly in memory. Recovering the encryption key is not enough to understand one of these programs. The internal command language must be reverse engineered as well.”

REG AD

In addition to having its own command language, it's also notable that the remote host can be a VMware VMCI target instead of a normal network address.

REG AD

“Taken as a whole, the approach here is consistent with a targeted, well-resourced operation rather than an opportunistic one,” Reichel wrote.

The malware, hidden inside a 64-bit Windows DLL file, impersonates Microsoft's dpapi.dll, part of Windows' data protection API for protecting sensitive data. It exports the same seven functions as the real dpapi.dll, but attempts to forward calls to a file named dpapisvc.dll, which is not a real Windows component.

The file also has a forged ESET Management Agent version resource, and loads via side-loading into ERAAgent.exe, the Windows executable for [ESET Management](https://support.eset.com/en/kb6866-eset-management-agent-faq) [Agent](https://support.eset.com/en/kb6866-eset-management-agent-faq). After confirming that its host process is named ERAAgent.exe, Sleepwalker goes to sleep inside the computer's memory, which also helps it remain hidden from traditional anti-virus tools.

Unlike most backdoors, which call back to an attacker-controlled command-and-control (C2) server and start receiving commands, Sleepwalker lies in wait, checking every packet that passes through the network looking for a specific pattern - this is called a magic packet. Once it sniffs out a packet that matches the exact pattern, the backdoor decrypts the data and treats it as a command.

“Because the backdoor never sends anything out on its own and does not open any obvious listening port by default, tools that watch for connections to known-bad domains or unusual outbound traffic will not see anything unusual,” Reichel wrote. “The absence of outbound connections to known-bad infrastructure does not rule out an infection, either. A machine can be fully compromised by this backdoor whil...