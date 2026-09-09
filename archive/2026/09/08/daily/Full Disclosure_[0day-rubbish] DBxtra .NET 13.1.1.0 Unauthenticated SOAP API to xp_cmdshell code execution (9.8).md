---
title: [0day-rubbish] DBxtra .NET 13.1.1.0 Unauthenticated SOAP API to xp_cmdshell code execution (9.8)
url: https://seclists.org/fulldisclosure/2026/Sep/33
source: Full Disclosure
date: 2026-09-08
fetch_date: 2026-09-09T06:56:55.304813
---

# [0day-rubbish] DBxtra .NET 13.1.1.0 Unauthenticated SOAP API to xp_cmdshell code execution (9.8)

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

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](34)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] DBxtra .NET 13.1.1.0 Unauthenticated SOAP API to xp\_cmdshell code execution (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 8 Sep 2026 06:20:33 +0000

---

```
TO: fulldisclosure () seclists org
SUBJECT: [0day-rubbish] DBxtra .NET 13.1.1.0 Unauthenticated SOAP API to xp_cmdshell code execution (9.8)
FROM: disclosure () 0day-rubbish com
----BODY----
0day Rubbish Research Team is publicly disclosing a vulnerability in
DBxtra .NET 13.1.1.0.

Type: Unauthenticated SOAP API to xp_cmdshell code execution (CWE-306)
CVSS: 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
Impact: unauthenticated remote code execution as the SQL Server service account on the BI host (web tier runs as
LocalSystem)
Authentication: unauthenticated

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/dbxtra-unauth-soap-xp-cmdshell-rce

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

[![Previous](/images/left-icon-16x16.png)](32)
[By Date](date.html#33)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](32)
[By Thread](index.html#33)
[![Next](/images/right-icon-16x16.png)](34)

### Current thread:

* **[0day-rubbish] DBxtra .NET 13.1.1.0 Unauthenticated SOAP API to xp\_cmdshell code execution (9.8)** *disclosure via Fulldisclosure (Sep 08)*

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