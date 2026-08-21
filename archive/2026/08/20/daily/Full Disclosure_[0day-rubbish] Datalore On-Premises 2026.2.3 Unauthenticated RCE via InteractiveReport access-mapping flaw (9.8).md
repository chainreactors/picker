---
title: [0day-rubbish] Datalore On-Premises 2026.2.3 Unauthenticated RCE via InteractiveReport access-mapping flaw (9.8)
url: https://seclists.org/fulldisclosure/2026/Aug/70
source: Full Disclosure
date: 2026-08-20
fetch_date: 2026-08-21T03:05:27.764431
---

# [0day-rubbish] Datalore On-Premises 2026.2.3 Unauthenticated RCE via InteractiveReport access-mapping flaw (9.8)

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

[![Previous](/images/left-icon-16x16.png)](69)
[By Date](date.html#70)
[![Next](/images/right-icon-16x16.png)](71)

[![Previous](/images/left-icon-16x16.png)](69)
[By Thread](index.html#70)
[![Next](/images/right-icon-16x16.png)](71)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Datalore On-Premises 2026.2.3 Unauthenticated RCE via InteractiveReport access-mapping flaw (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 19 Aug 2026 04:57:39 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in
Datalore On-Premises 2026.2.3.

Type: Unauthenticated RCE via InteractiveReport access-mapping flaw (CWE-306)
CVSS: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)
Impact: Anonymous attacker executes arbitrary code in the notebook agent container
Authentication: unauthenticated / pre-auth

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/jetbrains-datalore-interactive-report-unauth-rce

Project archive (ongoing disclosure series):
  https://github.com/Exploit-Garbage/0day-Rubbish

Vendor has been notified. CVE ID is pending.

--
0day Rubbish Research Team
disclosure () 0day-rubbish com
https://0day-rubbish.com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](69)
[By Date](date.html#70)
[![Next](/images/right-icon-16x16.png)](71)

[![Previous](/images/left-icon-16x16.png)](69)
[By Thread](index.html#70)
[![Next](/images/right-icon-16x16.png)](71)

### Current thread:

* **[0day-rubbish] Datalore On-Premises 2026.2.3 Unauthenticated RCE via InteractiveReport access-mapping flaw (9.8)** *disclosure via Fulldisclosure (Aug 19)*

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