---
title: Cisco adds another SD-WAN box to max-severity bug advisory
url: https://www.theregister.com/security/2026/06/17/cisco-adds-another-sd-wan-box-to-max-severity-bug-advisory/5257621
source: www.theregister.com - Articles
date: 2026-06-17
fetch_date: 2026-06-18T06:52:01.715429
---

# Cisco adds another SD-WAN box to max-severity bug advisory

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

# Cisco adds another SD-WAN box to max-severity bug advisory

Updated at the time? No sweat. Check those logs, though

Connor Jones
[Connor
Jones](https://www.theregister.com/author/connor-jones)
Cybersecurity reporter

Published
wed 17 Jun 2026 // 14:45 UTC

Cisco has updated a February security advisory, adding another product to the list of those affected by the maximum-severity CVE-2026-20127.

Switchzilla made a small amendment to the original [advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa-EHchtZk) on Tuesday evening, noting that Cisco Catalyst SD-WAN Validator, formerly vBond, was also among the boxes attackers could pop open.

Readers may remember the fuss over CVE-2026-20127 (10.0) a few months ago. The make-me-admin improper authentication flaw prompted a [Five Eyes alert](https://www.theregister.com/on-prem/2026/02/26/five-eyes-urge-action-as-cisco-zero-day-attacks-uncovered/4493149) since attackers could essentially gain persistent root access to all vulnerable instances.

REG AD

In other words, it's a far-from-ideal situation that could could create espionage opportunities, given the prevalence of Cisco's SD-WAN offerings in Western networks.

REG AD

Cisco said at the time that attackers could exploit CVE-2026-20127 to gain admin rights, access NETCONF, and reconfigure the SD-WAN fabric, before exploiting CVE-2022-20775 (7.8), a path traversal flaw discovered in September 2022, to gain root access.

Cisco Talos, the company's threat intel arm, posited that the bug could have been exploited for as long as three years by the time it was discovered.

Talos attributed the exploitation activity to a group it tracks as UAT-8616, whose activity dates back to at least 2023, according to its researchers' estimates. No one has formally attributed UAT-8616 to a specific country or group of individuals, but experts say that it is a highly sophisticated outfit that has a history of targeting critical infrastructure sectors.

## MORE CONTEXT

* [### Five Eyes warn: Patch your Cisco SD-WAN or risk root takeover](/on-prem/2026/02/26/five-eyes-urge-action-as-cisco-zero-day-attacks-uncovered/4493149)
* [### Yet another Cisco SD-WAN 0-day under attack, and no patch in sight](/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855)
* [### Patch time for Cisco SD-WAN admins as vendor drops yet another make-me-admin zero-day](/patches/2026/05/15/cisco-discloses-yet-another-sd-wan-make-me-admin-0-day/5241071)
* [### Cisco SD-WAN make-me-root bug under attack](/patches/2026/06/15/cisco-sd-wan-make-me-root-bug-under-attack/5255916)

Ollie Whitehouse, NCSC-UK's CTO, said at the time: "Our new alert makes clear that organizations using Cisco Catalyst SD-WAN products should urgently investigate their exposure to network compromise and hunt for malicious activity, making use of the new threat hunting advice produced with our international partners to identify evidence of compromise.

"UK organizations are strongly advised to report compromises to the NCSC, and to apply vendor updates and hardening guidance as soon as practicable to reduce the risk of exploitation."

The Register asked Cisco for more information, but it did not immediately respond.

Customers should not have to make any new changes, provided that they upgraded their software to a fixed version across all systems when the advisory was first published in February, not just SD-WAN Controller and SD-WAN Manager.

The update comes weeks after Cisco [disclosed another zero-day](https://www.theregister.com/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855) affecting Catalyst SD-WAN, suggesting that it had been exploited for at least a week at the time.

REG AD

Tracked as CVE-2026-20245, it marked the sixth SD-WAN flaw disclosed this year, and the [second to be exploited as a zero-day](https://www.theregister.com/patches/2026/05/15/cisco-discloses-yet-another-sd-wan-make-me-admin-0-day/5241071) in as many months. ®

[zero-day](/tag/zero-day)
[security](/tag/security)
[improper authentication](/tag/improper%20authentication)
[cyber-crime](/tag/cyber-crime)
[cisco](/tag/cisco)
[catalyst sd-wan](/tag/catalyst%20sd-wan)

REG AD

[![A person typing on a laptop with a red warning triangle icon displayed on the screen.](https://image.theregister.com/5241871.jpg?imageId=5241871&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

cyber-crime

## Cyber offenses now account for around a third of all crime across Asia and South Pacific

Latest Interpol review shows how scams con...