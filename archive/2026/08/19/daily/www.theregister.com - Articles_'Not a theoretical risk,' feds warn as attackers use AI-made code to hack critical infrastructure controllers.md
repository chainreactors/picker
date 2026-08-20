---
title: 'Not a theoretical risk,' feds warn as attackers use AI-made code to hack critical infrastructure controllers
url: https://www.theregister.com/security/2026/08/19/not-a-theoretical-risk-feds-warn-as-attackers-use-ai-made-code-to-hack-critical-infrastructure-controllers/5289960
source: www.theregister.com - Articles
date: 2026-08-19
fetch_date: 2026-08-20T02:57:16.776573
---

# 'Not a theoretical risk,' feds warn as attackers use AI-made code to hack critical infrastructure controllers

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

security

# 'Not a theoretical risk,' feds warn as attackers use AI-made code to hack critical infrastructure controllers

'It is an active threat'

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
wed 19 Aug 2026 // 23:38 UTC

Attackers are using AI-generated exploitation scripts to break into internet-exposed Siemens S7 Series programmable logic controllers (PLCs) at water, manufacturing, energy, and other critical facilities, in what five US federal agencies on Wednesday called an “active threat.”

In this latest round of intrusions against American critical infrastructure, the attackers use open source industrial automation libraries – specifically snap7.dll/python-snap7 – combined with AI coding assistants. Armed with the open source libraries and AI, the miscreants create custom tools that mimic operational technology (OT) monitoring software and provide read/write access to the PLC devices’ memory, configuration data, and ladder logic programs via the S7comm protocol.

“This is not a theoretical risk – it is an active threat,” the feds [warned](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a).

REG AD

While the joint alert from the National Security Agency (NSA), Cybersecurity and Infrastructure Security Agency (CISA), Federal Bureau of Investigation (FBI), Department of Energy (DOE), and Environmental Protection Agency (EPA) doesn’t attribute the threats to a particular government or criminal group, [Iranian cyber operatives](https://www.theregister.com/security/2026/07/29/iran-linked-cyberav3ngers-suspected-in-attacks-on-minnesota-water-systems/5280357) are suspected of being behind [recent attacks targeting PLCs](https://www.theregister.com/security/2026/08/07/water-system-controllers-dont-belong-on-the-internet-says-ex-nsa-chief-after-suspected-iran-attacks/5285070) at water and wastewater facilities across at least 12 states, including a cyberattack that disrupted more than 30 community water systems in Minnesota in late July.

REG AD

### This appears to be a continuation of the same suite of activity we suspect is affiliated with Iran targeting PLCs.

“This appears to be a continuation of the same suite of activity we suspect is affiliated with Iran targeting PLCs,” Cynthia Kaiser, Halcyon Ransomware Research Center SVP, told The Register. “Iran-affiliated actors and adversaries are actively targeting a wide swath of operational technology because these PLCs underpin essential health, safety, and critical infrastructure across society.”

National security and infosec experts last week told The Register that while there is no indication that the water-system hackers used AI in their intrusions, they worried [that attackers would soon add AI](https://www.theregister.com/security/2026/08/14/autonomous-ai-attacks-pose-clear-and-present-danger-to-critical-infrastructure/5287594) to their arsenals for attacks against critical infrastructure. Now, that threat appears to be here.

“What the advisory highlights with regard to AI usage aligns with what we’ve expected: state-sponsored adversaries are leveraging AI across the board for discrete tasks, like code checks and scripting, to scale their operations and move faster,” Kaiser, a former FBI cyber division deputy assistant director, told us on Wednesday. “The advisory reflects the broader reality that threat actors are using AI to increase their efficiency.”

### Siemens S7 Series PLCs under fire

According to the Wednesday security alert, the latest attacks specifically target internet-exposed Siemens S7 Series PLCs across critical manufacturing, energy, water and wastewater, chemical, food and agriculture, and commercial facilities  – in other words: most of the critical industries providing goods and services that Americans use in their daily lives.

“Additionally, Siemens S7 Series PLCs are used in other sectors, including the Defense Industrial Base (DIB), and could be targeted there as well,” the feds warned.

The Register reached out to the agencies for additional information about the attacks but did not receive any response to our questions.

### The real lesson for me is still the same: stop giving attackers a path to the critical system in the first place.

Attackers use...