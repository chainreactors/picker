---
title: Security advisory: Pre-authentication SYSTEM RCE (Zip-Slip plugin planting) in Output Messenger Server 2.0.x (>= 2.0.63) (Srimax Software (Output Technology))
url: https://seclists.org/fulldisclosure/2026/Aug/65
source: Full Disclosure
date: 2026-08-18
fetch_date: 2026-08-19T02:58:14.002463
---

# Security advisory: Pre-authentication SYSTEM RCE (Zip-Slip plugin planting) in Output Messenger Server 2.0.x (>= 2.0.63) (Srimax Software (Output Technology))

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

[![Previous](/images/left-icon-16x16.png)](64)
[By Date](date.html#65)
[![Next](/images/right-icon-16x16.png)](66)

[![Previous](/images/left-icon-16x16.png)](64)
[By Thread](index.html#65)
[![Next](/images/right-icon-16x16.png)](66)

![](/shared/images/nst-icons.svg#search)

# Security advisory: Pre-authentication SYSTEM RCE (Zip-Slip plugin planting) in Output Messenger Server 2.0.x (>= 2.0.63) (Srimax Software (Output Technology))

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 18 Aug 2026 06:05:35 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Output Messenger Server 2.0.x (>= 2.0.63) (Srimax
Software (Output Technology)). The research is published and a proof-of-concept is available.

Pre-authentication SYSTEM RCE (Zip-Slip plugin planting) (CVSS 9.8, pre-authentication)

Output Messenger Server 2.0.x accepts XMPP connections on TCP 14121 with no SASL and no credentials; every connection
is treated as authenticated. Through linkserver registration and the file-transfer listener, an unauthenticated
attacker uploads a crafted ZIP whose entries escape the plugin directory (Zip-Slip in SharpZipLib 0.85.4). On service
restart, the planted plugin constructor executes as LocalSystem. Dynamically verified.

Impact: Full compromise of the on-premise enterprise instant-messaging server as LocalSystem. The attacker can read
corporate communications, execute arbitrary commands, and move laterally inside the office network.

Advisory: https://0day-rubbish.com/blog/output-messenger-unauth-zipslip-plugin-rce

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

[![Previous](/images/left-icon-16x16.png)](64)
[By Date](date.html#65)
[![Next](/images/right-icon-16x16.png)](66)

[![Previous](/images/left-icon-16x16.png)](64)
[By Thread](index.html#65)
[![Next](/images/right-icon-16x16.png)](66)

### Current thread:

* **Security advisory: Pre-authentication SYSTEM RCE (Zip-Slip plugin planting) in Output Messenger Server 2.0.x (>= 2.0.63) (Srimax Software (Output Technology))** *disclosure via Fulldisclosure (Aug 17)*

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