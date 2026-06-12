---
title: Chinese agents caught rebuilding botnets and stirring the pot on AI datacenter debate
url: https://www.theregister.com/security/2026/06/11/china-linked-operators-revive-botnet-stir-ai-datacenter-debate/5253873
source: www.theregister.com - Articles
date: 2026-06-11
fetch_date: 2026-06-12T06:28:16.380047
---

# Chinese agents caught rebuilding botnets and stirring the pot on AI datacenter debate

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
  + [Bootnotes](/bootnotes)
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
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
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

# Chinese agents caught rebuilding botnets and stirring the pot on AI datacenter debate

PRC eyes are watching you

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 11 Jun 2026 // 01:00 UTC

Multiple reports indicate that Chinese operatives continue using every tech tool at their disposal – including American AI – to amass data on and manipulate everyone from security-clearance holders to everyday US citizens. And they’re trying to influence public opinion on building datacenters for AI, albeit without success so far.

One of these reports found a “significant resurgence” of a botnet linked to Chinese government-backed goons, including [Volt Typhoon](https://www.theregister.com/security/2025/03/12/this-is-the-fbi-chinas-volt-typhoon-is-on-your-network/804368), which previously used a covert network of connected devices to burrow deep into critical US networks and preposition for [future destructive attacks](https://www.theregister.com/2024/02/07/us_chinas_volt_typhoon_attacks/).

In January 2024, the FBI said it killed Volt’s [KV-botnet](https://www.theregister.com/2024/01/31/volt_typhoon_botnet/), comprised of hundreds of end-of-life routers and other internet-connected devices. At the time, KV-botnet consisted of four clusters, with the KV cluster primarily being used as a covert data transfer network, and the JDY cluster used for scanning and reconnaissance.

REG AD

In a Wednesday report, Lumen’s Black Lotus Labs said that while the KV cluster became largely [defunct](https://www.lumen.com/blog/en-us/kv-botnet-dont-call-comeback) after the law enforcement takedown, the JDY cluster remains an active threat, and has since surged to more than 1,500 compromised routers and IoT devices.

REG AD

“Analysis of this activity shows a clear focus on identifying vulnerable infrastructure shortly after public vulnerability disclosures, suggesting that reconnaissance output is rapidly operationalized by China-nexus advanced persistent threat (APT) actors,” the threat intel team [wrote](https://www.lumen.com/blog/en-us/expanded-jdy-iot-and-soho-botnet-enables-rapid-vulnerability-exploitation). “This targeted focus has been observed across a range of sectors, with the US military and associated entities as the most prominent.”

While the botnet resurgence poses the most pressing threat, and the security shop recommends all enterprises implement CISA and NCSC guidance for [mitigating Volt Typhoon activity](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf) and [defending against China-nexus covert networks of compromised devices](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-113a), another report indicates that China’s attempts at influence operations haven’t died down, either.

### Using American AI for covert ops about … American AI

OpenAI in a Wednesday [report](https://cdn.openai.com/pdf/96b559fa-c165-4575-805d-e636909e2f78/June-2026-Threat-Report.pdf) said it banned ChatGPT accounts likely originating from China after they used the American AI company’s models to generate content for covert operations about – wait for it  – American AI. While neither of the two clusters seemed to have much success in sowing chaos or swaying opinions, the fact that they tried at all is significant, according to Ben Nimmo, principal investigator on OpenAI’s Intelligence and Investigations team.

“Neither campaign appears to have gained much authentic engagement,” Nimmo told reporters. “They're important for what they reveal about the intentions of influence operators from China and the narratives they're testing and seeking to amplify.”

The first cluster used ChatGPT to generate social media content and images for an operation claiming datacenters and AI applications are increasing electricity demand and causing higher costs for ordinary Americans.

“For example, they asked for comic strips about a power grid operator’s capacity auction prices based on reporting from a legitimate regional paper,” the report says. “They asked ChatGPT to focus the comments on rising capacity prices as a consequence of peak electricity demand, framing the new demand as coming from data centers and AI applications and argued that these costs were ultimately passed to ordinary households.”

The operators then posted these comments and images on X, likely using fake accounts, with links to real news stories about datacenters.

REG AD

OpenAI suspects the operators are part of a social-media team at a private Chinese tech company that provides services for Chinese provincial-level government clients.

“This was not a case of an influence operation cre...