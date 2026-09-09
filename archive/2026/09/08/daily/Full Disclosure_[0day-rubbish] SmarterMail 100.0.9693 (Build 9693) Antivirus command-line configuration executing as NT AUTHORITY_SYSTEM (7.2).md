---
title: [0day-rubbish] SmarterMail 100.0.9693 (Build 9693) Antivirus command-line configuration executing as NT AUTHORITY\SYSTEM (7.2)
url: https://seclists.org/fulldisclosure/2026/Sep/36
source: Full Disclosure
date: 2026-09-08
fetch_date: 2026-09-09T06:56:54.579798
---

# [0day-rubbish] SmarterMail 100.0.9693 (Build 9693) Antivirus command-line configuration executing as NT AUTHORITY\SYSTEM (7.2)

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

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](37)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] SmarterMail 100.0.9693 (Build 9693) Antivirus command-line configuration executing as NT AUTHORITY\SYSTEM (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 8 Sep 2026 06:21:15 +0000

---

```
TO: fulldisclosure () seclists org
SUBJECT: [0day-rubbish] SmarterMail 100.0.9693 (Build 9693) Antivirus command-line configuration executing as NT
AUTHORITY\SYSTEM (7.2)
FROM: disclosure () 0day-rubbish com
----BODY----
0day Rubbish Research Team is publicly disclosing a vulnerability in
SmarterMail 100.0.9693 (Build 9693).

Type: Antivirus command-line configuration executing as NT AUTHORITY\SYSTEM (CWE-250)
CVSS: 7.2 (AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H)
Impact: web-to-OS privilege escalation from the SysAdmin role to NT AUTHORITY\SYSTEM on the mail host
Authentication: authenticated (valid admin/session required)

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/smartermail-antivirus-command-line-system-rce

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

[![Previous](/images/left-icon-16x16.png)](35)
[By Date](date.html#36)
[![Next](/images/right-icon-16x16.png)](37)

[![Previous](/images/left-icon-16x16.png)](35)
[By Thread](index.html#36)
[![Next](/images/right-icon-16x16.png)](37)

### Current thread:

* **[0day-rubbish] SmarterMail 100.0.9693 (Build 9693) Antivirus command-line configuration executing as NT AUTHORITY\SYSTEM (7.2)** *disclosure via Fulldisclosure (Sep 08)*

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