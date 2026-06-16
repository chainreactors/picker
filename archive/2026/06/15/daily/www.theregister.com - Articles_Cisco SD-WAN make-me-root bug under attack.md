---
title: Cisco SD-WAN make-me-root bug under attack
url: https://www.theregister.com/patches/2026/06/15/cisco-sd-wan-make-me-root-bug-under-attack/5255916
source: www.theregister.com - Articles
date: 2026-06-15
fetch_date: 2026-06-16T07:17:04.974035
---

# Cisco SD-WAN make-me-root bug under attack

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

PATCHES

# Cisco SD-WAN make-me-root bug under attack

Second Catalyst SD-WAN Manager flaw exploited as an 0-day this month

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
mon 15 Jun 2026 // 22:48 UTC

Cisco today issued a fix for a Catalyst SD-WAN Manager bug that attackers have already spotted and exploited to get root privileges, according to both the networking vendor and the feds.

The vulnerability, tracked as [CVE-2026-20262](https://nvd.nist.gov/vuln/detail/CVE-2026-20262)[,](https://nvd.nist.gov/vuln/detail/CVE-2026-20262) is in the web UI of Cisco Catalyst SD-WAN Manager, and exists because the software is not properly validating user-supplied input during a file upload process.

“An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected API endpoint of the affected system,” the vendor [warned](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ) in a Monday security advisory. “A successful exploit could allow the attacker to create or overwrite any file on the underlying operating system. This file could later be used to elevate to root.”

REG AD

There is one caveat: to exploit this bug, the attacker must have valid credentials with at least a lower-privileged, single-task user account.

REG AD

That probably explains the medium-severity, 6.8 CVSS rating for this bug.

## MORE CONTEXT

* [### Yet another Cisco SD-WAN 0-day under attack, and no patch in sight](/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855)
* [### Cisco serves up yet another perfect 10 bug with Secure Workload admin flaw](/security/2026/05/21/cisco-serves-up-yet-another-perfect-10-bug-with-secure-workload-admin-flaw/5244012)
* [### Patch time for Cisco SD-WAN admins as vendor drops yet another make-me-admin zero-day](/patches/2026/05/15/cisco-discloses-yet-another-sd-wan-make-me-admin-0-day/5241071)
* [### More Cisco SD-WAN bugs battered in attacks](/security/2026/04/21/more-cisco-sd-wan-bugs-battered-in-attacks/5229107)

Still, valid credentials aren’t hard to come by these days, and considering this CVE is already under attack, we know someone had some success.

“In June 2026, the Cisco PSIRT became aware of limited exploitation of this vulnerability,” the security alert said. “Cisco continues to strongly recommend that customers upgrade to a fixed software release to remediate this vulnerability.”

The flaw affects all deployment types, regardless of device configuration. There are no workarounds, but upgrading to a [fixed software](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ#fs) version will patch the flaw.

Also on Monday, the US Cybersecurity and Infrastructure Security Agency (CISA) [added CVE-2026-20262](https://www.cisa.gov/news-events/alerts/2026/06/15/cisa-adds-two-known-exploited-vulnerabilities-catalog) to its Known Exploited Vulnerabilities catalog, citing “evidence of active exploitation.” America’s lead cyber-defense agency also set a two-week deadline for all federal agencies to apply the patch.

This latest Cisco SD-WAN bug under attack comes less than two weeks after Switchzilla [warned that a high-severity vulnerability](https://www.theregister.com/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855) in Catalyst SD-WAN Manager vulnerability (CVE-2026-20245) was under active exploitation. At the time of disclosure, this SD-WAN vuln did not have a fix.

Cisco [issued an advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx) for that zero-day on June 4, and finally released patches for all affected versions on June 12.

This is the [eighth Cisco SD-WAN bug](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?f%5B0%5D=vendor_project%3A801) to be listed in CISA’s Known Exploited Vulnerabilities catalog so far this year.®

[security](/tag/security)
[patches](/tag/patches)
[cisco](/tag/cisco)

REG AD

[![](https://image.theregister.com/5255961.jpg?imageId=5255961&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)

AI + ML

## A modest proposal: Reformat everything to make documents more palatable to AI

What's up, DocLang?](https://www.theregister.com/ai-and-ml/2026/06/16/a-modest-proposal-reformat-everything-to-make-documents-more-palatable-to-ai/5255938)

[PATCHES

## Cisco SD-WAN make-me-root bug under attack

Second Catalyst SD-WAN Manager flaw exploited as an 0-day this month](https://www.theregister.com/patches/...