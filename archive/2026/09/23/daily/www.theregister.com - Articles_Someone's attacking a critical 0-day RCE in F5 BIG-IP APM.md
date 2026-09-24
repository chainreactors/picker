---
title: Someone's attacking a critical 0-day RCE in F5 BIG-IP APM
url: https://www.theregister.com/security/2026/09/23/someones-attacking-a-critical-0-day-rce-in-f5-big-ip-apm/5298659
source: www.theregister.com - Articles
date: 2026-09-23
fetch_date: 2026-09-24T07:08:18.421704
---

# Someone's attacking a critical 0-day RCE in F5 BIG-IP APM

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

REG AD

[security](/tag/security)

# Someone's attacking a critical 0-day RCE in F5 BIG-IP APM

Good news: there's a patch. Bad news: both CISA and F5 warn that it's under active exploitation

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)
Cybersecurity Editor

Published
wed 23 Sep 2026 // 19:09 UTC

### READ MORE

* [#### Researchers used Claude to hack OpenAI employees' ChatGPT accounts

  5 days ago](/security/2026/09/18/researchers-used-claude-to-hack-openai-employees-chatgpt-accounts/5297517)
* [#### Google Pixel phones pwned in zero-click attacks

  7 days ago](/security/2026/09/16/google-pixel-phones-pwned-in-zero-click-attacks/5296936)
* [#### Prolific Microsoft 0-day hunter drops CrowdStrike Falcon exploit PoC

  20 days ago](/security/2026/09/03/prolific-microsoft-0-day-hunter-drops-crowdstrike-falcon-exploit-poc/5294318)
* [#### Framework loses customer data in Metabase zero-day attack

  August 10, 2026](/personal-tech/2026/08/10/framework-loses-customer-data-in-metabase-zero-day-attack/5285302)
* [#### Russian spies take their half-click email attack from Zimbra to Outlook

  July 30, 2026](/security/2026/07/30/russian-spies-take-their-half-click-email-attack-from-zimbra-to-outlook/5281033)

F5 has fixed a critical zero-day bug in its BIG-IP Access Policy Manager (APM) that unknown miscreants are exploiting to remotely execute malicious code.

BIG-IP APM is a centralized access management and security proxy that allows users to connect to enterprise networks, applications, APIs, and cloud services via a single login.

The flaw, tracked as [CVE-2026-94127](https://www.cve.org/CVERecord?id=CVE-2026-94127), is a heap-based buffer overflow that affects BIG-IP APM systems configured as an OAuth Authorization Server, with an access policy and OAuth profile on the same virtual server. It received a critical 9.3 CVSS v4.0 score - so patch now.

REG AD

“We have learned that this vulnerability has been exploited,” F5 [said](https://my.f5.com/manage/s/article/K000162605) in a Tuesday security advisory.

REG AD

F5 did not immediately respond to our questions, including how many systems have been compromised, and whether criminals are abusing the vulnerability to deploy ransomware.

Also on Tuesday, the US Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-94127 to its [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-94127), and gave federal agencies a Friday deadline to apply patches.

This warning comes about a year after F5 and CISA warned [“highly sophisticated nation-state" hackers](https://www.theregister.com/special-features/2025/10/15/highly-sophisticated-government-goons-hacked-f5/301844) broke into the vendor’s network and stole BIG-IP source code, zero-day vulnerability details, and customer configuration data belonging to some users.

The attack posed an ["imminent risk" to federal agencies](https://www.theregister.com/special-features/2025/10/15/cisa-exec-blames-hackers-democrats-for-network-risk/1140961), US cybersecurity officials said at the time. The US Justice Department allowed F5 to delay disclosing the intrusion after determining that delayed public disclosure was warranted. This only happens if public disclosure poses a substantial risk to national security or public safety.

Neither the feds nor private researchers have publicly attributed the intrusion to a particular group or country, but a year earlier Google's Mandiant threat hunters linked exploitation of the critical F5 BIG-IP flaw CVE-2023-46747 to UNC5174, an access broker it assessed with moderate confidence as [operating from China](https://www.theregister.com/security/2024/03/22/chinese-snoops-exploit-f5-connectwise-bugs-to-sell-access/762328). The group attempted to sell access to US defense contractor appliances and UK government entities.®

[security](/tag/security)
[f5](/tag/f5)
[zero-day](/tag/zero-day)
[remote code execution](/tag/remote%20code%20execution)

REG AD

[![](https://image.theregister.com/5298733.jpg?imageId=5298733&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&f...