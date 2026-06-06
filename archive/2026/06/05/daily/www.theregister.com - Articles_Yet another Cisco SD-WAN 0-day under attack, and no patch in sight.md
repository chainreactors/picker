---
title: Yet another Cisco SD-WAN 0-day under attack, and no patch in sight
url: https://www.theregister.com/security/2026/06/05/yet-another-cisco-sd-wan-0-day-under-attack-and-no-patch-in-sight/5251855
source: www.theregister.com - Articles
date: 2026-06-05
fetch_date: 2026-06-06T05:51:39.716090
---

# Yet another Cisco SD-WAN 0-day under attack, and no patch in sight

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

security

# Yet another Cisco SD-WAN 0-day under attack, and no patch in sight

Good luck, sys admins

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
fri 5 Jun 2026 // 18:27 UTC

The threat is real. Unknown miscreants are exploiting a high-severity, zero-day bug in Cisco’s SD-WAN management software, and the networking giant hasn’t said when it will patch the flaw.

Cisco [issued an advisory](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx) on Thursday for the Catalyst SD-WAN Manager vulnerability, tracked as CVE-2026-20245, and it sounds like attackers have been exploiting this security failure for at least the last week.

It’s due to a validation error - the software fails to properly validate user-supplied input - and an authenticated, local attacker can exploit the flaw by uploading a specially crafted file to vulnerable systems. From there, they can escalate privileges and execute commands with root privileges.

REG AD

REG AD

The vulnerability affects all versions of the SD-WAN software, regardless of device configuration, and across all deployment types including on-premises, cloud-based, and FedRAMP-certified deployments.

Switchzilla says it became aware of attacks against this vulnerability in June.

“To exploit this vulnerability, an attacker must have netadmin privileges on an affected system,” the vendor said. “This would require valid credentials or exploitation of [CVE-2026-20182](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW) or [CVE-2026-20127](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa-EHchtZk). Cisco is not aware of successful exploitation by other methods.”

Both of these earlier SD-WAN security holes have also been hit by attackers in previous months.

The good news: an attacker needs valid credentials to abuse the new hole. The bad news: exposed credentials aren’t hard to find (or buy) online.

We don’t know the scope of exploitation or exactly when attackers began hitting this SD-WAN hole. Cisco declined to answer The Register’s questions, and instead sent us a statement via email.

“Cisco recommends customers upgrade to the fixed software released in May 2026 for CVE-2026-20182 as a protective measure,” a spokesperson said. “A patch for this vulnerability will be provided on a future date. Customers needing assistance should contact Cisco TAC.”

This latest bug is the sixth SD-WAN vulnerability listed as under attack since the start of the year, and the second zero-day in two months.

REG AD

The most recent is the one the Cisco spokesperson mentioned in an email to The Register.

In May, [Switchzilla disclosed](https://www.theregister.com/patches/2026/05/15/cisco-discloses-yet-another-sd-wan-make-me-admin-0-day/5241071) a max-severity make-me-admin bug (CVE-2026-20182) affecting Catalyst SD-WAN Controller and Manager, and warned that attackers had already found and exploited the hole before it issued a patch.

A month earlier, America's lead cyber-defense agency [said](https://www.theregister.com/security/2026/04/21/more-cisco-sd-wan-bugs-battered-in-attacks/5229107) that three Cisco Catalyst SD-WAN Manager bugs ([CVE-2026-20128](https://www.cve.org/CVERecord?id=CVE-2026-20128), [CVE-2026-20133](https://www.cve.org/CVERecord?id=CVE-2026-20133), and [CVE-2026-20122](https://www.cve.org/CVERecord?id=CVE-2026-20122)) were under attack, and gave federal agencies just four days to patch the security holes.

[Cisco fixed](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-authbp-qwCX8D4v) all three CVEs in late February, and in March [warned of attackers](https://www.theregister.com/2026/03/06/cisco_sdwan_bugs/) abusing two of them.

Also in February, the networking vendor patched a max-severity improper authentication flaw ([CVE-2026-20127](https://www.cve.org/CVERecord?id=CVE-2026-20127)) affecting the same SD-WAN software, prompting a [Five Eyes countries’ joint intelligence alert](https://www.theregister.com/on-prem/2026/02/26/five-eyes-urge-action-as-cisco-zero-day-attacks-uncovered/4493149) urgently warning defenders to patch it - plus an old SD-WAN vulnerability ([CVE-2022-20775](https://www.cve.org/CVERecord?id=CVE-2022-20775)) - or risk root takeover.

"Malicious cyber threat actors are targeting Cisco Catalyst SD-WAN used by organizations globally," the UK's lead cyber agency said at the time. "These actors are compromising SD-WANs to add a malicious rogue peer and then conduct a range of follow-on actions to achieve root access and maintain persistent access to the SD-...