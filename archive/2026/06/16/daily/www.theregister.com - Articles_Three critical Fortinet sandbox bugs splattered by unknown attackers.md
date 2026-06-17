---
title: Three critical Fortinet sandbox bugs splattered by unknown attackers
url: https://www.theregister.com/security/2026/06/16/three-critical-fortinet-sandbox-bugs-splattered-by-unknown-attackers/5256461
source: www.theregister.com - Articles
date: 2026-06-16
fetch_date: 2026-06-17T07:04:15.095541
---

# Three critical Fortinet sandbox bugs splattered by unknown attackers

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

# Three critical Fortinet sandbox bugs splattered by unknown attackers

All have patches, so make sure you upgrade to a fixed version

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
tue 16 Jun 2026 // 19:27 UTC

Three critical flaws in Fortinet’s sandbox that allow remote attackers to bypass authentication, escalate privileges, and execute malicious code are under active exploitation, according to threat intelligence firm Defused.

Fortinet [patched two](https://www.theregister.com/security/2026/04/15/critical-fortinet-sandbox-bugs-allow-auth-bypass-and-rce/5224979) of the three flaws, [CVE-2026-39813](https://fortiguard.fortinet.com/psirt/FG-IR-26-112) and [CVE-2026-39808](https://fortiguard.fortinet.com/psirt/FG-IR-26-100), in April and the third, [CVE-2026-25089](https://fortiguard.fortinet.com/psirt/FG-IR-26-141) last week. All three bugs received 9.1 CVSS ratings, and, at the time, the vendor said that there were no reports of active exploitation.

CVE-2026-39813 is a path traversal bug in the FortiSandbox JRPC API that allows an authentication bypass using specially crafted HTTP requests. It affects FortiSandbox 4.4.0 through 4.4.8 and 5.0.0 through 5.0.5. Patch to 4.4.9+ or 5.0.6+, depending on the branch, to fix the flaw. Fortinet security analyst Loic Pantano found this one.

REG AD

REG AD

CVE-2026-39808 is an OS command injection flaw in FortiSandbox that allows unauthenticated attackers to execute unauthorized code or commands via HTTP requests. It affects versions 4.4.0 through 4.4.8, and upgrading to FortiSandbox 4.4.9 or above patches the hole. Fortinet credited KPMG Spain researcher Samuel de Lucas Maroto with finding and reporting this bug.

Finally, CVE-2026-25089 is another OS command vulnerability in FortiSandbox, FortiSandbox Cloud and FortiSandbox PaaS WEB UI that allows unauthenticated attackers to execute unauthorized commands using specifically crafted HTTP requests. FortiSandbox 4.4.0 through 4.4.8 and 5.0.0 through 5.0.5, FortiSandbox Cloud 5.0.4 through 5.0.5, and FortiSandbox PaaS 5.0.4 through 5.0.5 are vulnerable. Upgrading to a fixed version patches the hole.

## MORE CONTEXT

* [### Ransomware crims got a month-long head start on Check Point VPN 0-day that now has a fix](/cyber-crime/2026/06/08/attackers-had-month-long-head-start-on-patched-check-point-vpn-zero-day/5252438)
* [### Attackers exploited this critical FortiClient EMS bug as a 0-day](/security/2026/04/06/attackers-exploited-the-forticlient-ems-bug-as-a-0-day/5227028)
* [### Patch these critical Fortinet sandbox bugs that let attackers bypass login, run commands over HTTP](/security/2026/04/15/critical-fortinet-sandbox-bugs-allow-auth-bypass-and-rce/5224979)
* [### AWS says more than 600 FortiGate firewalls hit in AI-augmented campaign](/security/2026/02/23/aws-says-600-fortigate-firewalls-hit-in-ai-augmented-attack/4998767)

Fortinet did not respond to The Register’s inquiries about these three CVEs and if the vendor had also observed any attacks against them.

According to Defused, the exploitation began over the weekend.

“We are observing exploitation of multiple Fortinet FortiSandbox vulnerabilities during the past 24 hours,” the threat-intel firm said in a LinkedIn post on Monday.

“Per our research a working exploit for CVE-2026-25089 has not yet been publicly disclosed,” the company added, noting that the exploit for this flaw appeared to be vibe coded and may be faulty.

We do know that all manner of miscreants [love to abuse Fortinet flaws](https://www.theregister.com/security/2026/03/13/credential-stealing-crew-spoofs-ivanti-fortinet-cisco-vpns/5223322), so if you haven’t already, patch now.

Earlier this month, Check Point VP of research Lotem Finkelstein warned [that ransomware crims](https://www.theregister.com/cyber-crime/2026/06/08/attackers-had-month-long-head-start-on-patched-check-point-vpn-zero-day/5252438) had exploited a critical authentication bypass vulnerability affecting Fortinet's Remote Access VPN and Mobile Access deployments, and said that the same crew was also likely abusing other VPN-related vulnerabilities in [Fortinet](https://www.theregister.com/security/2026/02/23/aws-says-600-fortigate-firewalls-hit-in-ai-augmented-attack/4998767) products. ®

[security](/tag/security)
[fortisandbox](/tag/fortisandbox)
[fortinet](/tag/fortinet)
[cyber-crime](/tag/cyber-crime)
[command injection](/tag/command%20injection)
[authentication bypass](/tag/authentication%20bypass)

REG AD

[![](https://image.theregister.com/5227626.jpg?imageId=5227626&panox=0.00&panoy=0.00&panow=100.00&panoh=100.00&heightx=0.00&heighty=0.00&heightw=100.00&heighth=100.00&width=960&height=432&format=webp&format=jpg)...