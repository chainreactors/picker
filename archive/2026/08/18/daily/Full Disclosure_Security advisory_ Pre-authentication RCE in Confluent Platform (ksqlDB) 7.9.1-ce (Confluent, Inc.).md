---
title: Security advisory: Pre-authentication RCE in Confluent Platform (ksqlDB) 7.9.1-ce (Confluent, Inc.)
url: https://seclists.org/fulldisclosure/2026/Aug/55
source: Full Disclosure
date: 2026-08-18
fetch_date: 2026-08-19T02:59:57.920584
---

# Security advisory: Pre-authentication RCE in Confluent Platform (ksqlDB) 7.9.1-ce (Confluent, Inc.)

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

[![Previous](/images/left-icon-16x16.png)](54)
[By Date](date.html#55)
[![Next](/images/right-icon-16x16.png)](56)

[![Previous](/images/left-icon-16x16.png)](54)
[By Thread](index.html#55)
[![Next](/images/right-icon-16x16.png)](56)

![](/shared/images/nst-icons.svg#search)

# Security advisory: Pre-authentication RCE in Confluent Platform (ksqlDB) 7.9.1-ce (Confluent, Inc.)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Aug 2026 06:03:26 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Confluent Platform (ksqlDB) 7.9.1-ce (Confluent,
Inc.). The research is published and a proof-of-concept is available.

Pre-authentication RCE (CVSS 9.8, pre-authentication)

Confluent Platform 7.9.1-ce exposes an unauthenticated remote code execution chain in its default configuration. ksqlDB
(HTTP 8089), the Kafka broker (9092 PLAINTEXT, no SASL) and Kafka Connect (8083) all accept requests without
authentication. An attacker submits a CREATE SINK CONNECTOR statement to ksqlDB using FileStreamSinkConnector with an
attacker-controlled file path and StringConverter, then produces arbitrary bytes to the subscribed Kafka topic through
the unauthenticated broker. The connector appends each message to the target file; writing a cron line to /etc/cron.d/
yields arbitrary command execution as root when crond runs. Dynamically verified with uid=0(root).

Impact: Arbitrary command execution as root (the ksqlDB/Connect process user); the attacker can read or destroy data on
the host, persist access, and take full control of the Confluent deployment. No credentials are required.

Advisory: https://0day-rubbish.com/blog/ksqldb-unauth-sink-connector-cron-rce

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

[![Previous](/images/left-icon-16x16.png)](54)
[By Date](date.html#55)
[![Next](/images/right-icon-16x16.png)](56)

[![Previous](/images/left-icon-16x16.png)](54)
[By Thread](index.html#55)
[![Next](/images/right-icon-16x16.png)](56)

### Current thread:

* **Security advisory: Pre-authentication RCE in Confluent Platform (ksqlDB) 7.9.1-ce (Confluent, Inc.)** *disclosure via Fulldisclosure (Aug 17)*

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