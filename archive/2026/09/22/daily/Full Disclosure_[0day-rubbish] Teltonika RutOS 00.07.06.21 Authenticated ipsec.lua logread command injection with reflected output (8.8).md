---
title: [0day-rubbish] Teltonika RutOS 00.07.06.21 Authenticated ipsec.lua logread command injection with reflected output (8.8)
url: https://seclists.org/fulldisclosure/2026/Sep/63
source: Full Disclosure
date: 2026-09-22
fetch_date: 2026-09-23T06:55:23.583491
---

# [0day-rubbish] Teltonika RutOS 00.07.06.21 Authenticated ipsec.lua logread command injection with reflected output (8.8)

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

[![Previous](/images/left-icon-16x16.png)](62)
[By Date](date.html#63)
[![Next](/images/right-icon-16x16.png)](64)

[![Previous](/images/left-icon-16x16.png)](62)
[By Thread](index.html#63)
[![Next](/images/right-icon-16x16.png)](64)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Teltonika RutOS 00.07.06.21 Authenticated ipsec.lua logread command injection with reflected output (8.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 20 Sep 2026 12:19:12 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in
Teltonika RutOS 00.07.06.21.

Type: Authenticated ipsec.lua logread command injection with reflected output (CWE-78)
CVSS: 8.8 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)
Impact: root command execution on the router, with command output reflected into the JSON response
Authentication: authenticated administrator

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/teltonika-rutos-ipsec-status-logread-command-injection

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

[![Previous](/images/left-icon-16x16.png)](62)
[By Date](date.html#63)
[![Next](/images/right-icon-16x16.png)](64)

[![Previous](/images/left-icon-16x16.png)](62)
[By Thread](index.html#63)
[![Next](/images/right-icon-16x16.png)](64)

### Current thread:

* **[0day-rubbish] Teltonika RutOS 00.07.06.21 Authenticated ipsec.lua logread command injection with reflected output (8.8)** *disclosure via Fulldisclosure (Sep 22)*

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