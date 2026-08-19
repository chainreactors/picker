---
title: Security advisory: Pre-authentication RCE (default credentials) in ObjectDB 2.9.5 server mode (ObjectDB Software)
url: https://seclists.org/fulldisclosure/2026/Aug/58
source: Full Disclosure
date: 2026-08-18
fetch_date: 2026-08-19T02:59:45.290403
---

# Security advisory: Pre-authentication RCE (default credentials) in ObjectDB 2.9.5 server mode (ObjectDB Software)

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

[![Previous](/images/left-icon-16x16.png)](57)
[By Date](date.html#58)
[![Next](/images/right-icon-16x16.png)](59)

[![Previous](/images/left-icon-16x16.png)](57)
[By Thread](index.html#58)
[![Next](/images/right-icon-16x16.png)](59)

![](/shared/images/nst-icons.svg#search)

# Security advisory: Pre-authentication RCE (default credentials) in ObjectDB 2.9.5 server mode (ObjectDB Software)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Aug 2026 06:04:05 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in ObjectDB 2.9.5 server mode (ObjectDB Software).
The research is published and a proof-of-concept is available.

Pre-authentication RCE (default credentials) (CVSS 9.8, pre-authentication)

ObjectDB 2.9.5 server mode (port 6136, proprietary binary protocol) has a critical remote code execution vulnerability:
JDOQL query filter evaluation allows arbitrary static-method reflective invocation. Factory default credentials
admin/admin grant full privileges with no forced change; the IP check accepts any source IP when the user has no ip
attribute. A malicious JDOQL filter such as java.lang.Runtime.getRuntime().exec(cmd) != null is evaluated server-side:
QNF.q() loads any class (no class-name allowlist), MCN.l() calls Method.invoke with setAccessible(true), reaching
Runtime.exec - the server-side Java process runs as root, yielding uid=0(root) RCE. Dynamically verified.

Impact: Full read of the host filesystem and JVM environment as root, arbitrary OS command execution, and full control
of the ObjectDB host and database.

Advisory: https://0day-rubbish.com/blog/objectdb-jdoql-injection-root-rce

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

[![Previous](/images/left-icon-16x16.png)](57)
[By Date](date.html#58)
[![Next](/images/right-icon-16x16.png)](59)

[![Previous](/images/left-icon-16x16.png)](57)
[By Thread](index.html#58)
[![Next](/images/right-icon-16x16.png)](59)

### Current thread:

* **Security advisory: Pre-authentication RCE (default credentials) in ObjectDB 2.9.5 server mode (ObjectDB Software)** *disclosure via Fulldisclosure (Aug 17)*

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