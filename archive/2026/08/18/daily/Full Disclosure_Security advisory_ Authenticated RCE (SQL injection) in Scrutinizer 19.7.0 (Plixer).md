---
title: Security advisory: Authenticated RCE (SQL injection) in Scrutinizer 19.7.0 (Plixer)
url: https://seclists.org/fulldisclosure/2026/Aug/66
source: Full Disclosure
date: 2026-08-18
fetch_date: 2026-08-19T02:57:56.759034
---

# Security advisory: Authenticated RCE (SQL injection) in Scrutinizer 19.7.0 (Plixer)

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

[![Previous](/images/left-icon-16x16.png)](65)
[By Date](date.html#66)
[![Next](/images/right-icon-16x16.png)](67)

[![Previous](/images/left-icon-16x16.png)](65)
[By Thread](index.html#66)
[![Next](/images/right-icon-16x16.png)](67)

![](/shared/images/nst-icons.svg#search)

# Security advisory: Authenticated RCE (SQL injection) in Scrutinizer 19.7.0 (Plixer)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Aug 2026 06:05:48 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Scrutinizer 19.7.0 (Plixer). The research is
published and a proof-of-concept is available.

Authenticated RCE (SQL injection) (CVSS 8.8, authenticated)

Plixer Scrutinizer 19.7.0 concatenates the HTTP orderBy parameter directly into a SQL ORDER BY clause with no escaping
in the adminEditLang handler. The default configuration includes the pg_cron extension and a PostgreSQL SUPERUSER
database role, so an authenticated administrator can inject a side-effect expression that schedules a cron job
executing arbitrary commands as the postgres user. Dynamically verified.

Impact: Arbitrary command execution on the flow-analytics appliance as the postgres user inside the default privileged
container. The attacker can disrupt monitoring, access network flow data, and take control of the host.

Advisory: https://0day-rubbish.com/blog/plixer-scrutinizer-orderby-sqli-pgcron-rce

PoC and full analysis: https://github.com/Exploit-Garbage/0day-Rubbish

Vendor has been notified. CVE ID is pending.

--
0day Rubbish Research Team
https://0day-rubbish.com
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](65)
[By Date](date.html#66)
[![Next](/images/right-icon-16x16.png)](67)

[![Previous](/images/left-icon-16x16.png)](65)
[By Thread](index.html#66)
[![Next](/images/right-icon-16x16.png)](67)

### Current thread:

* **Security advisory: Authenticated RCE (SQL injection) in Scrutinizer 19.7.0 (Plixer)** *disclosure via Fulldisclosure (Aug 17)*

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