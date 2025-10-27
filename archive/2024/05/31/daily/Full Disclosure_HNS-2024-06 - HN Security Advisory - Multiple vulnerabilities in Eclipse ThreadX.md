---
title: HNS-2024-06 - HN Security Advisory - Multiple vulnerabilities in Eclipse ThreadX
url: https://seclists.org/fulldisclosure/2024/May/35
source: Full Disclosure
date: 2024-05-31
fetch_date: 2025-10-06T16:52:48.541333
---

# HNS-2024-06 - HN Security Advisory - Multiple vulnerabilities in Eclipse ThreadX

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

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

![](/shared/images/nst-icons.svg#search)

# HNS-2024-06 - HN Security Advisory - Multiple vulnerabilities in Eclipse ThreadX

---

*From*: Marco Ivaldi <raptor () 0xdeadbeef info>
*Date*: Tue, 28 May 2024 14:22:31 +0200

---

```
Hi,

Please find attached a security advisory that describes multiple
vulnerabilities we discovered in Eclipse ThreadX (aka Azure RTOS).

* Title: Multiple vulnerabilities in Eclipse ThreadX
* OS: Eclipse ThreadX < 6.4.0
* Author: Marco Ivaldi <marco.ivaldi () hnsecurity it>
* Date: 2024-05-28
* CVE IDs and severity:
  * CVE-2024-2214 - High - 7.0 - CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
  * CVE-2024-2212 - High - 7.3 - CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:L
  * CVE-2024-2452 - High - 7.0 - CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:H/A:L
* Advisory URLs:
  * https://github.com/eclipse-threadx/threadx/security/advisories/GHSA-vmp6-qhp9-r66x
  * https://github.com/eclipse-threadx/threadx/security/advisories/GHSA-v9jj-7qjg-h6g6
  * https://github.com/eclipse-threadx/netxduo/security/advisories/GHSA-h963-7vhw-8rpx
* Vendor URL: https://threadx.io/

The advisory is also available at:
https://github.com/hnsecurity/vulns/blob/main/HNS-2024-06-threadx.txt

For additional information, please refer to our vulnerability writeup:
https://security.humanativaspa.it/multiple-vulnerabilities-in-eclipse-threadx/

Cheers,

--
Marco Ivaldi
https://0xdeadbeef.info/
"When cryptography is outlawed, bayl bhgynjf jvyy unir cevinpl."
```

**Attachment:
[HNS-2024-06-threadx.txt](att-35/HNS-2024-06-threadx.txt)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
[![Next](/images/right-icon-16x16.png)](36)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
[![Next](/images/right-icon-16x16.png)](36)

### Current thread:

* **HNS-2024-06 - HN Security Advisory - Multiple vulnerabilities in Eclipse ThreadX** *Marco Ivaldi (May 29)*

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