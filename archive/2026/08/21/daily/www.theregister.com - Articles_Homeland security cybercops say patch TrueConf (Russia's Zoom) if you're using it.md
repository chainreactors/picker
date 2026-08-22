---
title: Homeland security cybercops say patch TrueConf (Russia's Zoom) if you're using it
url: https://www.theregister.com/patches/2026/08/21/homeland-security-cybercops-say-patch-trueconf-russias-zoom-if-youre-using-it/5291156
source: www.theregister.com - Articles
date: 2026-08-21
fetch_date: 2026-08-22T02:52:47.945041
---

# Homeland security cybercops say patch TrueConf (Russia's Zoom) if you're using it

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

PATCHES

# Homeland security cybercops say patch TrueConf (Russia's Zoom) if you're using it

Ukrainian hacktivists exploiting the bugs, but TrueConf's reach stretches well beyond home turf

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
fri 21 Aug 2026 // 17:29 UTC

CISA has ordered US federal agencies to patch two exploited flaws in TrueConf, a Russian-built video conferencing platform, after compromised servers were caught handing malware to unsuspecting meeting participants.

The US cybersecurity agency on Thursday [added CVE-2026-72529 and CVE-2026-72530](https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog)to its Known Exploited Vulnerabilities catalog, saying both have been used in real-world attacks. What CISA doesn't say is who is being attacked, or where.

The only publicly documented attacks exploiting these two bugs so far come from [Kaspersky](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/), which linked them to Head Mare, a pro-Ukrainian hacktivist group that has repeatedly gone after Russian organizations. Its latest campaign targeted Russian companies across industries including transport, energy, electronics, IT, and software development.

REG AD

CISA doesn't say whether it added the flaws to KEV because of those attacks or because it has evidence of exploitation elsewhere, potentially including against organizations in the US.

REG AD

That question is particularly interesting given what TrueConf is and who uses it.

TrueConf is a Moscow-based maker of video conferencing software that offers an on-premises alternative to cloud services such as Zoom and Microsoft Teams. Organizations can run TrueConf Server on their own infrastructure, including in private networks, giving them control over where their calls and associated data go.

## MORE CONTEXT

* [### Russian snoops add OAuth abuse to targeted phishing campaigns](/security/2026/08/21/russian-snoops-add-oauth-abuse-to-targeted-phishing-campaigns/5290706)
* [### US Bank investigates LockBit's claims as ransomware crims set pay-or-leak deadline](/security/2026/08/20/us-bank-investigates-lockbits-claims-as-ransomware-crims-set-pay-or-leak-deadline/5290560)
* [### Autonomous AI attacks pose 'clear and present danger' to critical infrastructure](/security/2026/08/14/autonomous-ai-attacks-pose-clear-and-present-danger-to-critical-infrastructure/5287594)
* [### Two wars and a World Cup lead to epic DDoS attacks on publishers](/security/2026/08/11/two-wars-and-a-world-cup-lead-to-epic-ddos-attacks-on-publishers/5286278)

While the company's roots and much of its customer base are Russian, TrueConf has users worldwide. It says it has users in its [portfolio](https://trueconf.com/company/customers.html) that [include](https://www.avnation.tv/2018/04/18/trueconf-connects-courts-to-prisons/) Switzerland’s Department of Justice and Home Affairs, [Istanbul Airport](https://www.digitalavmagazine.com/en/2020/08/20/el-software-navori-ql-impulsa-la-publicidad-dooh-en-el-aeropuerto-de-estambul/), and a news org, which The Reg has contacted to confirm. Most of the customer success stories are dated before 2022.

Used together, the two bugs flagged by CISA can give an attacker control of the underlying server. According to Kaspersky, an unauthenticated attacker with network access to TCP port 4307, which TrueConf documentation says is open by default, can exploit the first flaw to run a malicious script. The second flaw lets the attacker break out of the isolated environment where the script runs and execute arbitrary code on the underlying server.

Kaspersky says Head Mare used that access to plant a web shell, move through victims' infrastructure, and gain privileged access to the TrueConf database. From there, the attackers replaced the legitimate TrueConf Windows client installer on compromised servers with a trojanized version carrying the PhantomCore backdoor.

Kaspersky warns that this creates a risk beyond organizations actually running vulnerable TrueConf servers. Employees joining conferences hosted by suppliers or other third parties could potentially download a compromised...