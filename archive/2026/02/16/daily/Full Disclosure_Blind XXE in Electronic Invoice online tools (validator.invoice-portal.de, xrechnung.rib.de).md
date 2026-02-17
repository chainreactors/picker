---
title: Blind XXE in Electronic Invoice online tools (validator.invoice-portal.de, xrechnung.rib.de)
url: https://seclists.org/fulldisclosure/2026/Feb/20
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:56.841973
---

# Blind XXE in Electronic Invoice online tools (validator.invoice-portal.de, xrechnung.rib.de)

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# Blind XXE in Electronic Invoice online tools (validator.invoice-portal.de, xrechnung.rib.de)

---

*From*: Hanno Böck <hanno () hboeck de>
*Date*: Mon, 16 Feb 2026 10:48:05 +0100

---

```
During tests of electronic invoicing tools, I discovered multiple XXE
and Blind XXE vulnerabilities in online tools parsing electronic
invoices in XML formats.

While most of the affected tools have fixed these vulnerabilities, two
online tools remain vulnerable to Blind XXE attacks, allowing
exfiltration of files. Disclosure to the affected operators happened
more than 90 days ago.

Vulnerable tools:

https://validator.invoice-portal.de/
https://xrechnung.rib.de/ (only the visualization tool)

In both cases, uploading an invoice with a blind XXE payload leads to
HTTP requests to the attacker's server and exfiltrates file content.
Proof of concepts, e.g., to exfiltrate /etc/hostname
(ciibxxehostname.xml), can be found here:
  https://github.com/hannob/invoicesec

Timeline validator.invoice-portal.de:
2025-11-17 Informed support contact about Blind XXE vulnerability, no
reply
2026-02-16 Still vulnerable, public disclosure

Timeline xrechnung.rib.de:
2025-10-29 Reported "standard" XXE via contact form, no reply
2025-11-18 Re-test, incomplete fix: "Standard" XXE fixed, Blind XXE
still possible
2025-11-18 Re-reported incomplete fix, no reply
2026-02-16 Still vulnerable, public disclosure

This was part of a larger research effort about the security of EU
electronic invoices:
  https://invoice.secvuln.info/

--
Hanno Böck - Independent security researcher
https://itsec.hboeck.de/
https://badkeys.info/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

### Current thread:

* **Blind XXE in Electronic Invoice online tools (validator.invoice-portal.de, xrechnung.rib.de)** *Hanno Böck (Feb 16)*

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