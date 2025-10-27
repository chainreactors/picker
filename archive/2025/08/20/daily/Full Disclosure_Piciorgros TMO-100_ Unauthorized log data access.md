---
title: Piciorgros TMO-100: Unauthorized log data access
url: https://seclists.org/fulldisclosure/2025/Aug/7
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:51:12.727479
---

# Piciorgros TMO-100: Unauthorized log data access

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

![](/shared/images/nst-icons.svg#search)

# Piciorgros TMO-100: Unauthorized log data access

---

*From*: Georg Lukas <lukas () rt-solutions de>
*Date*: Thu, 14 Aug 2025 15:25:22 +0000

---

```
PDF advisory: https://rt-solutions.de/piciorgros/Piciorgros_TMO-100_IP-Logger_en.pdf

Classification
--------------

- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

- CVSS 4.0 Score: 5.3 / Medium
  CVSS:4.0/AV:A/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N

- CVSS 3.1 Score: 4.3 / Medium
  CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N

Affected systems
----------------

- Piciorgros TMO-100 V3/V4 with software version below 4.20
  (discovered in V3.72)

Summary
-------

The Piciorgros TMO-100 is a data modem for TETRA radio networks. It has
an undocumented system log service, which is provided without
authentication via TCP port 51986 on the LAN interface. This allows an
attacker with access to the LAN network to view some of the modem's
operating parameters, e.g. to plan further attacks. Starting with
software version 4.20, logger access is only enabled for a 15-minute
time window after a web login, preventing attacks during normal
operation.

Details
-------

During a penetration test carried out on behalf of a customer, a
Piciorgros TMO-100 data modem was part of the test scope. The
documentation describes the so-called "IPLog" feature for creating
support requests to the manufacturer. This feature can be accessed with
the IP Logger software. Under the hood, the software is connecting to
TCP port 51968 on the LAN interface, where the modem provides the
current system status and a live log data stream without authentication:

$ telnet 192.168.0.199 51968
Trying 192.168.0.199...
Connected to 192.168.0.199.
Escape character is '^]'.

[FFFF] | 13.02.25 10:43:25 02:37:37.43 | **** Piciorgros TMO-100 V3.72
(HW-Rev. 3) Build 1819* Release (Apr 7 2021, 10:35:03) - Logging started
****
[FFFE] | 13.02.25 10:43:25 02:37:37.43 | Serial number: ███ Options:
8001 Set24: 0080 Set25: 0001
[FFFE] | 13.02.25 10:43:25 02:37:37.43 | TETRA core SW versions:
Stack:0454, DSP:0456, MMI:F444
[F020] | 13.02.25 10:43:38 02:37:51.16 | TETRA CREG state change: 1 ->
99:1:0
…
[E000] | 13.02.25 10:44:34 02:38:46.63 | TETRA registration information:
1:0:0.
[F020] | 13.02.25 10:44:41 02:38:53.97 | PPP: Is up.
[E000] | 13.02.25 10:44:41 02:38:53.98 | PPP link is up in try 1. Own
IP: 10.14.42.31
…

The log shows the IP address of the modem in the TETRA network, which
can be used to carry out attacks on other devices in the TETRA data
network.

Impact
------

An attacker with LAN access to a TMO-100 modem can determine the
hardware and software version used as well as the IP address in the
TETRA data network and thus use the modem to scan neighboring IP address
ranges.

Mitigation for operators
------------------------

The modems should be updated to software version 4.20 or higher to limit
the impact.

Recommendations for the manufacturer
------------------------------------

Access should be authenticated in the same way as the web interface and,
if possible, encrypted using TLS. Implementation via web sockets or
other APIs as part of the web UI could be a viable alternative.

Timeline
--------

-   2025-02-13 Discovery of the vulnerability
-   2025-02-27 Notification to the manufacturer
-   2025-03-06 Confirmation of the vulnerability by the manufacturer
-   2025-03-11 Release of software version V4.20 by the manufacturer
-   2025-08-14 Publication of the vulnerability as part of responsible
    disclosure

--
Dr.-Ing. Georg Lukas
rt-solutions.de GmbH
Oberländer Ufer 190a
D-50968 Köln

Zentrale: (+49)221 93724 0
Web : www.rt-solutions.de
rt-solutions.de
experts you can trust.

Sitz der Gesellschaft: Köln
Eingetragen beim Amtsgericht Köln: HRB 52645
Geschäftsführer: Prof. Dr. Ralf Schumann, Dr. Stefan Schemmer
```

**Attachment:
[smime.p7s](att-7/smime_p7s.bin)**
*Description:*

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **Piciorgros TMO-100: Unauthorized log data access** *Georg Lukas (Aug 18)*

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