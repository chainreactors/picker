---
title: Pink is the latest goon squad to use fake helpdesk calls to steal creds
url: https://www.theregister.com/cyber-crime/2026/06/04/pink-is-the-latest-goon-squad-to-use-fake-helpdesk-calls-to-steal-creds/5251434
source: www.theregister.com - Articles
date: 2026-06-04
fetch_date: 2026-06-05T06:14:27.810480
---

# Pink is the latest goon squad to use fake helpdesk calls to steal creds

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
  + [OSes](/oses)
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
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
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

* [Computex 2026](/special_features/computex)
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

CYBER-CRIME

# Pink is the latest goon squad to use fake helpdesk calls to steal creds

A familiar tactic popularized by chaotic crime crew Lapsus$

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 4 Jun 2026 // 23:16 UTC

UPDATED A new extortion brand called Pink – which may be a rebrand of BlackFile – uses voice phishing and fake help-desk calls to gain initial access to organizations’ IT environments, steal their sensitive data, and threaten to leak it unless the victims pay a ransom demand.

Palo Alto Networks' Unit 42 first spotted the gang, which it tracks as cluster CL-CRI-1147, and its data-leak site, which went live on May 31. “Pink uses vishing and IT impersonation to phish credentials/MFA, then exfiltrates enterprise cloud storage and productivity data to extort victims,” the threat-intelligence biz [said](https://www.linkedin.com/posts/we-are-tracking-pink-cl-cri-1147-a-new-ugcPost-7467982449772429312-qcbZ/) in a LinkedIn post.

Google Threat Intelligence is not so sure it's a new gang, however.

REG AD

"After retiring the BlackFile brand in May 2026, we assess the group launched the 'Redact' brand and has now potentially surfaced as 'Pink,," Austin Larsen, Principal Threat Analyst at Google Threat Intelligence Group, told us. "This new operation exhibits hallmarks of UNC6671, including similar credential-harvesting infrastructure, data leak site (DLS), and recurring messaging that claims to 'improve the security' of victims who pay. Additionally, we attribute the Pink (CL-CRI-1147) domains recently published by Unit42 to UNC6671."

REG AD

Regardless whether it's brand new or just a new coat of paint, the tactics are very familiar.  Pink is one of many [goon squads](https://www.theregister.com/security/2025/08/12/three-notorious-cybercrime-gangs-appear-to-be-collaborating/393646) to use these [social-engineering tactics](https://www.theregister.com/special-features/2026/03/23/voice-phishing-skyrockets-as-smooth-crims-talk-their-way-in/5223759) to steal employees’ credentials and bypass multi-factor authentication, using this access to burgle companies’ cloud storage and databases.

Chaotic crime crew Lapsus$, during its 2021 and 2022 extortion spree that hit [Nvidia](https://www.theregister.com/2022/02/26/nvidia_security_breach/), [Microsoft](https://www.theregister.com/2022/03/21/microsoft_lapsus_breach_probe/), and [Okta](https://www.theregister.com/2022/03/23/olkta_microsoft_lapsus/), among others, popularized this style of phone-based intrusions before [Scattered Spider](https://www.theregister.com/security/2025/05/18/ex-nsa-listened-to-scattered-spiders-calls-theyre-good/801296) picked up the mantle. Scattered Spider is perhaps best known for its 2023 [Las Vegas casino digital heists](https://www.theregister.com/security/2023/12/28/do-the-casino-ransomware-attacks-make-the-case-to-pay/580707), and reportedly bragged that all it took to break into MGM's networks was a 10-minute call with the help desk.

Over the last few years, ShinyHunters has used this same playbook to steal sensitive data from [Ticketmaster,](https://www.theregister.com/security/2024/05/30/crooks-steal-560m-peoples-info-from-ticketmaster/1059565) [AT&T](https://www.theregister.com/security/2025/06/05/att-investigates-claimed-sale-of-70m-customer-data-dump/538763), and [other Salesforce customers](https://www.theregister.com/security/2026/03/09/shinyhunters-claims-yet-another-salesforce-customers-breach/5220118), and [thousands of schools and universities](https://www.theregister.com/cyber-crime/2026/05/14/security-pros-doubt-canvas-attackers-really-deleted-stolen-student-data/5240799) that use Canvas’ digital learning platform.

Despite [multiple arrests](https://www.theregister.com/security/2025/09/15/15-ransomware-gangs-go-dark-to-enjoy-golden-parachutes/1080583) across all three gangs, they keep coming back to victimize more organizations. Most incident responders, including Google’s Mandiant and Unit 42, link many of these criminal collectives to [The Com](https://www.theregister.com/security/2025/07/23/irl-com-recruits-teens-for-real-life-stabbings-shootings/1258543), a loosely knit group of primarily English speakers made up of several interconnected networks of hackers, SIM swappers, and extortionists, with some of its subgroups offering real-life violent crime for hire.

According to Unit 42, this latest cluster of extortion activity is also “likely a Com-affiliated actor.” And after investigating “multiple” of these extortion attacks over the past few months, on Monday, they spotted something that led them to Pink’s name-and-shame website.

“On June 1, 2026, an existing extortion negotiation that had never received ...