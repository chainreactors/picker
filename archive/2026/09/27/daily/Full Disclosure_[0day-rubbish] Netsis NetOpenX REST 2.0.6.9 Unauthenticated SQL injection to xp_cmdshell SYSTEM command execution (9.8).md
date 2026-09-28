---
title: [0day-rubbish] Netsis NetOpenX REST 2.0.6.9 Unauthenticated SQL injection to xp_cmdshell SYSTEM command execution (9.8)
url: https://seclists.org/fulldisclosure/2026/Sep/78
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:57:00.659564
---

# [0day-rubbish] Netsis NetOpenX REST 2.0.6.9 Unauthenticated SQL injection to xp_cmdshell SYSTEM command execution (9.8)

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

[![Previous](/images/left-icon-16x16.png)](77)
[By Date](date.html#78)
[![Next](/images/right-icon-16x16.png)](79)

[![Previous](/images/left-icon-16x16.png)](77)
[By Thread](index.html#78)
[![Next](/images/right-icon-16x16.png)](79)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Netsis NetOpenX REST 2.0.6.9 Unauthenticated SQL injection to xp\_cmdshell SYSTEM command execution (9.8)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 04:55:12 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Logo
Netsis NetOpenX REST 2.0.6.9 (also distributed as Netsis Nox REST), the REST
API gateway of the Netsis enterprise ERP suite.

Type: unauthenticated SQL injection in the OAuth 2.0 token endpoint leading to
operating-system command execution via SQL Server xp_cmdshell
(CWE-89, CWE-306, CWE-78). A single POST /api/v2/token carrying no client and
no user credentials supplies a form field named idmuserid that is concatenated
raw into a SQL statement by ServiceManager.GetIdmUserLastSessionInfo, issued
before OAuthManager.LogIn actually validates the credentials. The backend is
SQL Server, so a semicolon yields a stacked batch that enables xp_cmdshell and
then runs an OS command.

Scoring. This finding is dual-scored, with the stricter readings published
alongside the headline rather than in a footnote, each against its own vector:
- PRIMARY, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. This is
  the recorded headline figure and it describes only the elevation tier, that is
  the configuration where the service's SQL login holds sysadmin, as it did in
  the verified environment. It is not a claim that command execution is available
  on every deployment.
- CONDITIONAL, 8.1 High, CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H. The same
  impact set under a stricter attack-complexity judgement that treats the sysadmin
  property of the service login, a deployment characteristic outside the
  attacker's control, as a condition of command execution.
- CONDITIONAL lower bound, 7.5 High, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N.
  Where the service login is not sysadmin, the same request still yields
  unauthenticated blind SQL injection with data disclosure but no OS access.

Impact: at the elevation tier, OS command execution on the ERP database host with
the identity of the SQL Server service account (NT AUTHORITY\SYSTEM in the
verified configuration), meaning control of the ERP financial and accounting
database, exfiltration of it, and a pivot into the internal network. The
injection is blind at the HTTP layer.

Authentication: unauthenticated. The pipeline registers no global authorization
filter, the token endpoint is an OWIN middleware route on which action filters
never apply, and the shipped SQL fragment blacklist is inert.

Verification boundary, stated plainly. This was NOT verified against a stock
installed product reached across a network. A complete Netsis ERP deployment was
not achievable in the lab, so the chain was driven against a reconstruction of
the product pipeline (the real OWIN Startup, OAuthConfig, WebApiConfig and
authorization-server provider, hosted via WebApp.Start on loopback
127.0.0.1:8977, against a real SQL Server Express instance whose NETSIS login
held sysadmin), with exactly one method body, ServiceManager.GetConnectionString,
rewritten by a Mono.Cecil IL patch to clear a commercial licensing gate that is
not a security boundary. The sink, the authentication logic, the routing table,
the OAuth provider and the SQL concatenation were all left as unmodified product
code. Because the reconstruction's listener was bound to loopback, remote network
exposure is a code and deployment argument rather than an observed remote run.

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/netsis-netopenx-unauth-sqli-xp-cmdshell-rce

Project archive (ongoing disclosure series):
  https://github.com/Exploit-Garbage/0day-Rubbish

The vendor has been notified through its published security contact. No vulnerability identifier has been assigned to
this finding yet.

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

[![Previous](/images/left-icon-16x16.png)](77)
[By Date](date.html#78)
[![Next](/images/right-icon-16x16.png)](79)

[![Previous](/images/left-icon-16x16.png)](77)
[By Thread](index.html#78)
[![Next](/images/right-icon-16x16.png)](79)

### Current thread:

* **[0day-rubbish] Netsis NetOpenX REST 2.0.6.9 Unauthenticated SQL injection to xp\_cmdshell SYSTEM command execution (9.8)** *disclosure via Fulldisclosure (Sep 26)*

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