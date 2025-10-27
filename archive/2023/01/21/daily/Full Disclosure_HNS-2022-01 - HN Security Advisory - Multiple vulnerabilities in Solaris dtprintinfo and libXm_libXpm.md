---
title: HNS-2022-01 - HN Security Advisory - Multiple vulnerabilities in Solaris dtprintinfo and libXm/libXpm
url: https://seclists.org/fulldisclosure/2023/Jan/12
source: Full Disclosure
date: 2023-01-21
fetch_date: 2025-10-04T04:31:15.694613
---

# HNS-2022-01 - HN Security Advisory - Multiple vulnerabilities in Solaris dtprintinfo and libXm/libXpm

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# HNS-2022-01 - HN Security Advisory - Multiple vulnerabilities in Solaris dtprintinfo and libXm/libXpm

---

*From*: Marco Ivaldi <raptor () 0xdeadbeef info>
*Date*: Wed, 18 Jan 2023 09:48:38 +0100

---

```
Dear Full Disclosure,

Find attached a security advisory that details multiple
vulnerabilities we discovered in Oracle Solaris CDE dtprintinfo, Motif
libXm, and X.Org libXpm.

* Title: Multiple vulnerabilities in Solaris dtprintinfo and libXm/libXpm
* Products: Common Desktop Environment 1.6, Motif 2.1, X.Org libXpm < 3.5.15
* OS: Oracle Solaris 10 (CPU January 2021)
* Author: Marco Ivaldi <marco.ivaldi () hnsecurity it>
* Date: 2023-01-18
* Oracle vulnerability tracking numbers:
  * S1597707 - Arbitrary printer name injection
  * S1597724 - Heap memory disclosure via long printer names
  * S1597711 - Memory corruption via malformed icon files
  * S1597730 - Stack-based buffer overflow in libXm ParseColors
* CVE IDs:
  * CVE-2022-46285 - Infinite loop on unclosed comments in Xorg libXpm
* Advisory URLs:
  * https://github.com/hnsecurity/vulns/blob/main/HNS-2022-01-dtprintinfo.txt
  * https://lists.x.org/archives/xorg-announce/2023-January/003312.html
  * https://lists.x.org/archives/xorg-announce/2023-January/003313.html
* Exploit URLs:
  * https://github.com/0xdea/exploits/blob/master/solaris/raptor_dtprintlibXmas.c

For additional information, please refer to our vulnerability writeup:
https://security.humanativaspa.it/nothing-new-under-the-sun/

PS. No, HNS-2022-01 is not a typo. Check out the disclosure timeline
in the advisory and you'll understand why we used this label.

Regards,

--
Marco Ivaldi
https://0xdeadbeef.info/
"When cryptography is outlawed, bayl bhgynjf jvyy unir cevinpl."
```

**Attachment:
[HNS-2022-01-dtprintinfo.txt](att-12/HNS-2022-01-dtprintinfo.txt)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **HNS-2022-01 - HN Security Advisory - Multiple vulnerabilities in Solaris dtprintinfo and libXm/libXpm** *Marco Ivaldi (Jan 19)*
  + [Re: HNS-2022-01 - HN Security Advisory - Multiple vulnerabilities in Solaris dtprintinfo and libXm/libXpm](24) *Marco Ivaldi (Jan 23)*

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