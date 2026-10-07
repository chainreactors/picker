---
title: [0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)
url: https://seclists.org/fulldisclosure/2026/Oct/8
source: Full Disclosure
date: 2026-10-06
fetch_date: 2026-10-07T07:55:41.318998
---

# [0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Oct 2026 17:54:04 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in
StreamSets Transformer, the Spark-engine data-pipeline platform from
StreamSets Inc. (subsequently acquired by IBM), verified on version 3.17.0
analysed from the official container image.

Type: failing-open authentication plus un-sandboxed code injection. On the
web tier, CWE-306 and CWE-1188 with CWE-285 on the authorisation side: when
the effective http.authentication value resolves to none, the embedded
servlet container installs no authentication handler at all, and the same
state with DPM disabled registers a filter on every path that makes every
role check pass and presents a synthesised admin principal. At the sink,
CWE-94: the REST pipeline API accepts an attacker-chosen pipeline whose
ScalaDTransform code field, an unconstrained text configuration entry, is
compiled with the full Scala compiler and executed inside the service JVM,
which runs as uid 0. The research records exactly three absences on that
path: no SecurityManager, no sandbox and no API allowlist.

Scoring. Dual-scored, with the primary reading named first:
- PRIMARY, as distributed, 8.1 High, vector
  CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H. Attack complexity
  is high because success depends on a target state the attacker
  does not control: the shipped properties file sets aster, so the
  anonymous state is reached by operator choice or by loss of the property.
- CONDITIONAL, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H,
  for deployments whose effective mode does resolve to none, including the
  verified instance, where the chain completed deterministically. This is
  the deployment-conditional reading and is not the factory-state rating.

Impact: anonymous code execution as uid 0 inside the container on the first
command, with no escalation step; unrestricted read of every stored pipeline
definition including connection configuration, of the product property
files and of the container filesystem; arbitrary modification of product
state; and availability impact on an engine that sits between upstream
sources and downstream warehouses. No sandbox was bypassed, because none
exists on the compile-and-run path.

Verification boundary, stated plainly. Verified end to end over plain HTTP
against a live instance of the official container image, three independent
runs, each leaving a per-run unique root-owned marker file; the identity
command returned uid 0 inside the container and command output was recovered
out of band from the container filesystem. No instance was exercised at its
shipped property value, so no bypass of the authenticated configuration is
claimed; the property-loss fallback is established from decompiled code
rather than a live experiment; container root was reached with no escape
attempted or claimed; only version 3.17.0 was tested. The shipped
proof-of-concept takes every target detail as a parameter and includes a
probe mode that tests the precondition without attacking.

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/streamsets-transformer-auth-none-scaladtransform-code-execution

Project archive (ongoing disclosure series):
  https://github.com/Exploit-Garbage/0day-Rubbish

The vendor has been notified through the product-security intake the vendor
publishes for this product line. No vulnerability identifier has been
assigned to this finding yet.

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **[0day-rubbish] StreamSets Transformer 3.17.0 auth-mode none fallback and un-sandboxed ScalaDTransform execution to container root (8.1 primary)** *disclosure via Fulldisclosure (Oct 06)*

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