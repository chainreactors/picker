---
title: Doozy of a Patch Tuesday includes 30 critical Microsoft CVEs
url: https://www.theregister.com/patches/2026/05/13/doozy-of-a-patch-tuesday-includes-30-critical-microsoft-cves/5239224
source: www.theregister.com - Articles
date: 2026-05-12
fetch_date: 2026-05-13T05:47:37.126435
---

# Doozy of a Patch Tuesday includes 30 critical Microsoft CVEs

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
  + [PaaS + IaaS](/paas_iaas)
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
  + [AI + ML](/ai_ml)
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

# Doozy of a Patch Tuesday includes 30 critical Microsoft CVEs

The good news: no 0-days. The bad news: busy week ahead for Microsoft admins

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
wed 13 May 2026 // 00:51 UTC

Microsoft released fixes for 137 CVEs on Tuesday, none of which are known to have been targeted by attackers. But the news is not all good as Redmond rated a whopping 30 flaws as critical, with 14 earning a 9.0 or higher CVSS severity rating, including one perfect 10.

Plus, everyone who celebrates the monthly patchapalooza event received validation for what we all widely suspected [last month](https://www.theregister.com/security/2026/04/14/microsofts-massive-patch-tuesday-its-raining-bugs/5219841): Yes, Redmond (and everyone else, for that matter) is using AI to find a ton more bugs than ever before. And that means a lot more work for all the folks applying and testing the patches.

“This month's release sits on the larger side of a hotpatch month, and we expect releases to continue trending larger for some time,” Tom Gallagher, VP of engineering at Microsoft Security Response Center, said in [a note on this month's Patch Tuesday](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday).

REG AD

Microsoft also said its secret-until-now AI bug hunting system, [codenamed MDASH](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/), found 16 of the vulnerabilities addressed in this month’s release. Redmond additionally announced it is making the tool available to a limited number of customers in private preview, along the lines of [Anthropic’s Mythos](https://www.theregister.com/security/2026/04/08/anthropic-mythos-model-can-find-and-exploit-0-days/5224393) and [Project Glasswing](https://www.theregister.com/security/2026/04/22/anthropic-mythos-shaping-up-as-nothingburger/5225649).

REG AD

In other words: no break for Microsoft admins this [May Patch Tuesday](https://msrc.microsoft.com/update-guide/releaseNote/2026-May).

Let’s take a look at some of the nastiest/most-interesting bugs that also received some of the highest-CVSS ratings this month, coming in hot at 9.8 and 9.9.

## MORE CONTEXT

* [### Linux kernel maintainers pitch emergency killswitch after CopyFail and Dirty Frag chaos](/oses/2026/05/11/linux-kernel-maintainers-pitch-emergency-killswitch-after-copyfail-and-dirty-frag-chaos/5237801)
* [### Microsoft releases first big update after Nadella's vow to 'win back fans'](/software/2026/05/01/first-big-microsoft-update-after-vow-to-win-back-fans/5222873)
* [### Microsoft's patch for a 0-day exploited by Russian spies fell short. Another Windows flaw is under attack](/security/2026/04/29/microsoft-patch-fell-short-new-windows-flaw-exploited/5227153)
* [### Microsoft's massive Patch Tuesday: It's raining bugs](/security/2026/04/14/microsofts-massive-patch-tuesday-its-raining-bugs/5219841)

First up: [CVE-2026-41096](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-41096). This one is a critical, 9.8-rated Windows DNS Client remote code execution (RCE), and while Redmond says exploitation is “unlikely,” we’d suggest patching it ASAP. It’s due to a heap-based buffer overflow, and no authentication or user interaction is needed to exploit it (it's done by sending a specially crafted DNS response to a vulnerable system), potentially leading to memory corruption and RCE.

“Since the DNS Client runs on virtually every Windows machine, the attack surface is enormous,” Zero Day Initiative bug hunting boss Dustin Childs [warned](https://www.zerodayinitiative.com/blog/2026/5/12/the-may-2026-security-update-review). “An attacker with a position to influence DNS responses (MitM, rogue server) could achieve unauthenticated RCE across your enterprise.”

Plus, it could happen across a ton of enterprise systems very rapidly, Jack Bicer, Action1 vulnerability research director told The Register. “This CVE requires immediate attention,” he said. “Successful attacks may lead to widespread endpoint compromise, ransomware deployment, credential harvesting, and operational disruption across corporate networks.”

Another especially bad bug, [CVE-2026-42898](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42898) in Microsoft Dynamics 365 on-premises systems, achieved a near-perfect 9.9 CVSS rating and also leads to RCE. Any authenticated user can trigger this vuln - it doesn’t require admin or other elevated privileges.

As Redmond explains: “An attacker with the required permissions could modify the saved state of a process session in Dynamics CRM and trigger the system to process that data, which could result in the se...