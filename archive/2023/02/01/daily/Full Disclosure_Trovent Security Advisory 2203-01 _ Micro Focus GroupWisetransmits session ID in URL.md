---
title: Trovent Security Advisory 2203-01 / Micro Focus GroupWise	transmits session ID in URL
url: https://seclists.org/fulldisclosure/2023/Jan/28
source: Full Disclosure
date: 2023-02-01
fetch_date: 2025-10-04T05:25:47.802442
---

# Trovent Security Advisory 2203-01 / Micro Focus GroupWise	transmits session ID in URL

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Trovent Security Advisory 2203-01 / Micro Focus GroupWise transmits session ID in URL

---

*From*: Stefan Pietsch <s.pietsch () trovent io>
*Date*: Fri, 27 Jan 2023 14:58:57 +0000

---

```
# Trovent Security Advisory 2203-01 #
#####################################

Micro Focus GroupWise transmits session ID in URL
#################################################

Overview
########

Advisory ID: TRSA-2203-01
Advisory version: 1.0
Advisory status: Public
Advisory URL: https://trovent.io/security-advisory-2203-01
Affected product: Micro Focus GroupWise
Affected version: prior to 18.4.2
Vendor: Micro Focus, https://www.microfocus.com
Credits: Trovent Security GmbH, Stefan Pietsch

Detailed description
####################

Micro Focus GroupWise is a messaging software for email and personal information
management.
Trovent Security GmbH discovered that the GroupWise web application transmits
the session ID in HTTP GET requests in the URL when email content is accessed.
The exposed session ID can be recorded in the browser history of the client and
in log files of the web server or reverse proxy server.
A possible attacker with access to the browser history or the server log files
is able to take control of the user session with the help of the session ID.

Severity: Medium
CVSS Score: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)
CVE ID: CVE-2022-38756
CWE ID: CWE-598

Proof of concept
################

Simplified HTTP request:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET /attachment?session=<SESSIONID>&id=... HTTP/1.1
Host: <HOSTNAME>
...
X-User-Agent: GroupWise Web (18.4.0-139604)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution / Workaround
#####################

The vendor released a fixed version of GroupWise.

Fixed in version 18.4.2.

History
#######

2022-03-30: Vulnerability found
2022-08-05: Vendor contacted
2022-10-31: Contacted vendor again
2022-11-01: Vendor replied that the vulnerability will be investigated
2022-11-14: Vendor contacted, asking for status
2022-11-16: Vendor replied that a security bulletin is being prepared
2022-12-06: Vendor published security bulletin
2023-01-27: Advisory published
```

**Attachment:
[signature.asc](att-28/signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Trovent Security Advisory 2203-01 / Micro Focus GroupWise transmits session ID in URL** *Stefan Pietsch (Jan 30)*

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