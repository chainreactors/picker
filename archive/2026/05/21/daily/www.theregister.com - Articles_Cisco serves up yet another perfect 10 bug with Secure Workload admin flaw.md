---
title: Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw
url: https://www.theregister.com/security/2026/05/21/cisco-serves-up-yet-another-perfect-10-bug-with-secure-workload-admin-flaw/5244012
source: www.theregister.com - Articles
date: 2026-05-21
fetch_date: 2026-05-22T06:08:46.067406
---

# Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw

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
  + [Edge + IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS + IaaS](/tag/paas-iaas)
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
  + [AI + ML](/tag/ai-ml)
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
  + [All Special Features](/tag/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
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

* [Datacenter](/tag/datacenter)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [IT Careers](/tag/tech%20jobs)
* [Columnists](/tag/columnists)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

Security

# Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw

Switchzilla says attackers could access sensitive data and make configuration changes across tenant boundaries through vulnerable internal APIs

Carly Page
[Carly
Page](https://www.theregister.com/author/carly-page)

Published
thu 21 May 2026 // 12:27 UTC

Cisco has disclosed yet another perfect 10 vulnerability, this time warning that unauthenticated attackers could gain Site Admin privileges in its Secure Workload platform simply by sending crafted API requests to vulnerable systems.

The bug, tracked as [CVE-2026-20223](https://www.cve.org/CVERecord?id=CVE-2026-20223), earned the full 10.0 CVSS treatment and affects Cisco Secure Workload Cluster Software in both SaaS and on-prem environments. According to [Cisco's barebones advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-csw-pnbsa-g8WEnuy), the issue boils down to weak validation and authentication checks in internal REST API endpoints.

In practical terms, that means attackers don't require credentials, user interaction, or any significant effort to exploit the bug. Cisco said a successful attack could allow remote attackers to "read sensitive information and make configuration changes across tenant boundaries with the privileges of the Site Admin user."

REG AD

Cross-tenant bugs tend to make cloud customers especially twitchy because they undermine one of the core assumptions of multi-tenant infrastructure: namely that somebody else's compromise is not supposed to become your problem.

REG AD

Cisco noted that the flaw affects internal REST APIs rather than the platform's web management interface, although that distinction is unlikely to bring much comfort to admins staring at a 10.0 severity score.

## MORE CONTEXT

* [### Cisco to fire 4,000 staff and generously give them free training – on Cisco](/networks/2026/05/14/cisco-to-fire-4000-staff-and-generously-give-them-free-training-on-cisco/5240125)
* [### More Cisco SD-WAN bugs battered in attacks](/security/2026/04/21/more-cisco-sd-wan-bugs-battered-in-attacks/5229107)
* [### Iran claims US used backdoors to knock out networking equipment during war](/security/2026/04/21/iran-claims-us-used-backdoors-in-networking-equipment/5223346)
* [### Ransomware crims abused Cisco 0-day weeks before disclosure, says Amazon security boss](/security/2026/03/18/ransomware-crims-abused-cisco-0-day-weeks-before-disclosure/5222246)

The networking giant said there are currently no workarounds, and customers must install fixed releases to fully remediate the issue. Cisco Secure Workload 3.10 is fixed in version 3.10.8.3, while 4.0 is fixed in 4.0.3.17. Customers running version 3.9 or earlier are being told to migrate to a supported fixed release. Cisco added that its cloud-hosted SaaS deployments have already been patched and require no customer action.

Cisco said it is not aware of active exploitation and that the flaw was discovered during internal security testing, though vulnerabilities carrying a 10.0 score and requiring no authentication rarely stay quiet for long.

The bug lands less than a week after [Cisco disclosed another maximum severity flaw affecting SD-WAN systems](https://www.theregister.com/patches/2026/05/15/cisco-discloses-yet-another-sd-wan-make-me-admin-0-day/5241071) that could allow attackers to grant themselves administrator privileges, continuing what is becoming an increasingly awkward run of top-scoring Cisco security advisories.

The company has spent much of the past year disclosing one 9.8-plus infrastructure flaw after another across products spanning firewalls, management platforms, identity systems, and enterprise networking gear. At this point, Cisco seems to be treating 10.0 CVSS scores as a recurring feature rather than a special occasion. ®

[secure workload](/tag/secure%20workload)
[cve-2026-20223](/tag/cve-2026-20223)
[cisco](/tag/cisco)
[vulnerability](/tag/vulnerability)
[security](/tag/security)
[site admin privileges](/tag/site%20admin%20privileges)

REG AD

[![](https://image.theregister.com/230011.jpg?imageId=230011&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

Security

## Cisco used AI to write security incident reports, with mixed results

You’ll need a lot of detailed prompts to get solid output - and even then it may have errors and typos](https://www.theregister.com/security/2026/05/22/cisco-used-ai-to-write-security-incident-reports-with-mixed-results/5244692)

[Systems

## Alibaba just admitted it’s struggling to keep up with rival chipmakers and AI shops

Reveals decent new homegrown accelerator and tiny production volumes](https://w...