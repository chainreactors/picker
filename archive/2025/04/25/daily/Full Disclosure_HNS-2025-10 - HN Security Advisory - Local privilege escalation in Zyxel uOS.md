---
title: HNS-2025-10 - HN Security Advisory - Local privilege escalation in Zyxel uOS
url: https://seclists.org/fulldisclosure/2025/Apr/27
source: Full Disclosure
date: 2025-04-25
fetch_date: 2025-10-06T22:07:41.067361
---

# HNS-2025-10 - HN Security Advisory - Local privilege escalation in Zyxel uOS

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# HNS-2025-10 - HN Security Advisory - Local privilege escalation in Zyxel uOS

---

*From*: Marco Ivaldi <raptor () 0xdeadbeef info>
*Date*: Wed, 23 Apr 2025 08:44:55 +0200

---

```
Hi,

Please find attached a security advisory that describes some
vulnerabilities we discovered in the Zyxel uOS Linux-based operating
system.

* Title: Local privilege escalation via Zyxel fermion-wrapper
* Product: USG FLEX H Series
* OS: Zyxel uOS V1.31 (and potentially earlier versions)
* Author: Marco Ivaldi <marco.ivaldi () hnsecurity it>
* Date: 2025-04-23
* CVE ID: CVE-2025-1731 (see discussion in "5 - Remediation" below)
* Severity: High - 7.8 - CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
* CWE ID: CWE-61 - https://cwe.mitre.org/data/definitions/61.html
* HN Security URLs:
  * https://github.com/hnsecurity/vulns/blob/main/HNS-2025-10-zyxel-fermion.txt
  * https://github.com/0xdea/exploits/blob/master/zyxel/raptor_fermion
  * https://security.humanativaspa.it/local-privilege-escalation-on-zyxel-usg-flex-h-series-cve-2025-1731
* Vendor URLs:
  *
https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-incorrect-permission-assignment-and-improper-privilege-management-vulnerabilities-in-usg-flex-h-series-firewalls-04-22-2025
  * https://community.zyxel.com/en/discussion/28988/usg-flex-h-series-v1-32patch-0-firmware-release

For additional information, please refer to our vulnerability writeup:
https://security.humanativaspa.it/local-privilege-escalation-on-zyxel-usg-flex-h-series-cve-2025-1731/

Regards,

--
Marco Ivaldi
https://0xdeadbeef.info/
"When cryptography is outlawed, bayl bhgynjf jvyy unir cevinpl."
```

**Attachment:
[HNS-2025-10-zyxel-fermion.txt](att-27/HNS-2025-10-zyxel-fermion.txt)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

### Current thread:

* **HNS-2025-10 - HN Security Advisory - Local privilege escalation in Zyxel uOS** *Marco Ivaldi (Apr 23)*

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