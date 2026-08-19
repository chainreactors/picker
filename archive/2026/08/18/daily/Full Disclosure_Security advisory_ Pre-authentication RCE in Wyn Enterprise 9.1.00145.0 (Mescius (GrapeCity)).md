---
title: Security advisory: Pre-authentication RCE in Wyn Enterprise 9.1.00145.0 (Mescius (GrapeCity))
url: https://seclists.org/fulldisclosure/2026/Aug/59
source: Full Disclosure
date: 2026-08-18
fetch_date: 2026-08-19T02:59:31.325734
---

# Security advisory: Pre-authentication RCE in Wyn Enterprise 9.1.00145.0 (Mescius (GrapeCity))

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

[![Previous](/images/left-icon-16x16.png)](58)
[By Date](date.html#59)
[![Next](/images/right-icon-16x16.png)](60)

[![Previous](/images/left-icon-16x16.png)](58)
[By Thread](index.html#59)
[![Next](/images/right-icon-16x16.png)](60)

![](/shared/images/nst-icons.svg#search)

# Security advisory: Pre-authentication RCE in Wyn Enterprise 9.1.00145.0 (Mescius (GrapeCity))

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Aug 2026 06:04:17 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Wyn Enterprise 9.1.00145.0 (Mescius (GrapeCity)).
The research is published and a proof-of-concept is available.

Pre-authentication RCE (CVSS 9.8, pre-authentication)

Wyn Enterprise 9.1.00145.0 exposes an unauthenticated root RCE chain of three vulnerabilities: JWT signature validation
is skipped (parse-only ReadToken) with a hardcoded integration client secret, producing an unauthenticated 10-year
admin reference token; the import endpoint allows a zip-slip arbitrary file write (a malicious DLL can be dropped into
the security-provider folder); and the security-provider loader scans DLLs and calls Activator.CreateInstance on the
parameterless constructor, running as root. All three are reachable without credentials in the default configuration.
Dynamically verified with root RCE.

Impact: Full host compromise as root (the dotnet container process); the attacker can read the host filesystem, execute
arbitrary commands, and take full control of the Wyn server.

Advisory: https://0day-rubbish.com/blog/wyn-enterprise-unauth-rce

PoC and full analysis: https://github.com/Exploit-Garbage/0day-Rubbish

--
0day Rubbish Research Team
https://0day-rubbish.com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](58)
[By Date](date.html#59)
[![Next](/images/right-icon-16x16.png)](60)

[![Previous](/images/left-icon-16x16.png)](58)
[By Thread](index.html#59)
[![Next](/images/right-icon-16x16.png)](60)

### Current thread:

* **Security advisory: Pre-authentication RCE in Wyn Enterprise 9.1.00145.0 (Mescius (GrapeCity))** *disclosure via Fulldisclosure (Aug 17)*

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