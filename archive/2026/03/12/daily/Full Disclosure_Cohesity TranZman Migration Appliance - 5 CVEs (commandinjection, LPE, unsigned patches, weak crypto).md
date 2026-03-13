---
title: Cohesity TranZman Migration Appliance - 5 CVEs (command	injection, LPE, unsigned patches, weak crypto)
url: https://seclists.org/fulldisclosure/2026/Mar/3
source: Full Disclosure
date: 2026-03-12
fetch_date: 2026-03-13T04:08:10.725365
---

# Cohesity TranZman Migration Appliance - 5 CVEs (command	injection, LPE, unsigned patches, weak crypto)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# Cohesity TranZman Migration Appliance - 5 CVEs (command injection, LPE, unsigned patches, weak crypto)

---

*From*: GregD via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 08 Mar 2026 11:18:05 +0000

---

```
Hi,

I'm disclosing five vulnerabilities discovered during an authorised
security assessment of the Cohesity TranZman Migration Appliance
(formerly Stone Ram TranZman), Release 4.0 Build 14614.

CVE-2025-67840 - Web API Command Injection (CVSS 7.2 High)
The /api/v1/scheduler/run and /api/v1/actions/run endpoints allow
authenticated administrators to execute arbitrary commands as root by
injecting into POST request parameters. Input is not properly sanitised
before being passed to system commands.

CVE-2025-63911 - CLISH Command Injection (CVSS 7.2 High)
Multiple command injection vectors exist in the CLISH restricted shell,
allowing authenticated users to escape the restricted environment and
gain elevated command execution via local privilege escalation.

CVE-2025-63909 - Local Privilege Escalation (CVSS 7.2 High)
Incorrect access control in /opt/SRLtzm/bin/TapeDumper allows
authenticated users to escalate privileges to root.

CVE-2025-63910 - Unsigned Patch Upload (CVSS 7.2 High)
The patch upload mechanism does not verify signatures, allowing remote
code execution via crafted patch files.

CVE-2025-63912 - Weak Cryptography / Static XOR (CVSS 5.5 Medium)
The TranZman FTP service (port 55555/TCP) uses XOR with a static,
hardcoded key instead of proper encryption. An attacker who can
observe network traffic can decrypt the entire control channel -
exposing credentials, commands, and backup filenames - and forge or
replay commands to retrieve or tamper with files in transit.

Affected versions: Release 4.0 Build 14614 including patch
TZM_1757588060_SEP2025_FULL.depot

Vendor timeline:
- 26 September 2025: Reported to Cohesity
- 20 October 2025: Cohesity confirmed patches available
- 25 December 2025: 90-day embargo ended
- 27 December 2025: Public disclosure

Patches: Apply TZM_patch_1.patch followed by
TZM_1760106063_OCT2025R2_FULL.depot. Contact Cohesity support
for the latest OVA with integrated fixes.

Full advisories with techincal details:
https://github.com/GregDurys/Cohesity-TranZman-CVEs

Individual advisories (Gists):
https://gist.github.com/GregDurys/ef7fc6a36646df927374bba8e7279270
https://gist.github.com/GregDurys/d402038147e36de5908159d9722072ef
https://gist.github.com/GregDurys/74c36c36bef81293a42022758f2736a9
https://gist.github.com/GregDurys/8b7a3022c04b6cee8c1e1af04f5671b2
https://gist.github.com/GregDurys/4c2765d76272cda64dfc78f7a75a9251

Regards,
Greg Durys

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **Cohesity TranZman Migration Appliance - 5 CVEs (command injection, LPE, unsigned patches, weak crypto)** *GregD via Fulldisclosure (Mar 12)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")