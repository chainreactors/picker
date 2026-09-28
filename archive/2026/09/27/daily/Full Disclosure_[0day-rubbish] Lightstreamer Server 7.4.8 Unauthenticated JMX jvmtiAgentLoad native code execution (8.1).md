---
title: [0day-rubbish] Lightstreamer Server 7.4.8 Unauthenticated JMX jvmtiAgentLoad native code execution (8.1)
url: https://seclists.org/fulldisclosure/2026/Sep/76
source: Full Disclosure
date: 2026-09-27
fetch_date: 2026-09-28T07:57:01.129609
---

# [0day-rubbish] Lightstreamer Server 7.4.8 Unauthenticated JMX jvmtiAgentLoad native code execution (8.1)

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

[![Previous](/images/left-icon-16x16.png)](75)
[By Date](date.html#76)
[![Next](/images/right-icon-16x16.png)](77)

[![Previous](/images/left-icon-16x16.png)](75)
[By Thread](index.html#76)
[![Next](/images/right-icon-16x16.png)](77)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Lightstreamer Server 7.4.8 Unauthenticated JMX jvmtiAgentLoad native code execution (8.1)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 23 Sep 2026 04:54:43 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in
Lightstreamer Server 7.4.8 build 3506 (with JMS Extender 2.1.0).

Type: unauthenticated JMX inspection console allowing an anonymous caller to
invoke any MBean operation, reaching jvmtiAgentLoad on
com.sun.management:type=DiagnosticCommand to load and run a native agent
library inside the broker JVM (CWE-306, CWE-345, CWE-20, CWE-250, CWE-1188)

Scoring. This finding is dual-scored on one documented delivery precondition,
and both figures are published rather than a single headline number:
- PRIMARY, 8.1 High, CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H. This is the
  conservative figure for an attacker with network access only: the agent
  library must be delivered to a filesystem path by means outside this endpoint.
- CONDITIONAL, 9.8 Critical, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. This
  is the shipped-default exposure where the precondition is ALREADY satisfied,
  that is a native shared object is already reachable at a filesystem path the
  attacker names. Exploitation is then one deterministic HTTP request. The 9.8
  figure is conditional, not the primary rating, and is not the headline.

Impact: native code execution inside the Lightstreamer JVM as the service
process, inheriting that process's full identity. In the verified deployment the
process ran as uid=0(root), so the executed commands ran as root; root is not
claimed to be a factory-mandated identity, it is whatever account launched the
service. The shipping configuration sets <jmxtree_enabled>Y</jmxtree_enabled>
and <dashboard><public>Y</public> even though the adjacent comments claim the
default is N, and the only remaining check is a Referer header matching the
target host, which any HTTP client forges.

Authentication: unauthenticated (no credential of any kind).

Verification boundary, stated plainly. We verified the MBean-invocation and
native-code-execution legs against a research-host deployment reached over
loopback (HTTP 200 with "return code: 0", marker files recording uid=0(root),
and id/whoami commands chosen by the HTTP client at send time). The native
agent library, however, was already present on disk, placed beforehand over an
authenticated root session. jvmtiAgentLoad takes a filesystem path and fetches
nothing (http:// and file:// were both treated as literal strings), so the
fully remote chain including payload delivery is NOT demonstrated by this
advisory; what is proven unauthenticated is the request leg, not the delivery
leg.

Full technical analysis and a reproducible proof-of-concept:
  https://0day-rubbish.com/blog/lightstreamer-unauth-jmx-jvmti-agentload-rce

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

[![Previous](/images/left-icon-16x16.png)](75)
[By Date](date.html#76)
[![Next](/images/right-icon-16x16.png)](77)

[![Previous](/images/left-icon-16x16.png)](75)
[By Thread](index.html#76)
[![Next](/images/right-icon-16x16.png)](77)

### Current thread:

* **[0day-rubbish] Lightstreamer Server 7.4.8 Unauthenticated JMX jvmtiAgentLoad native code execution (8.1)** *disclosure via Fulldisclosure (Sep 26)*

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