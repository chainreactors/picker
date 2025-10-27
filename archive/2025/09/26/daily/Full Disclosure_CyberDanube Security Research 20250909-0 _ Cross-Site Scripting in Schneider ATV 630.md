---
title: CyberDanube Security Research 20250909-0 | Cross-Site Scripting in Schneider ATV 630
url: https://seclists.org/fulldisclosure/2025/Sep/69
source: Full Disclosure
date: 2025-09-26
fetch_date: 2025-10-02T20:45:19.311328
---

# CyberDanube Security Research 20250909-0 | Cross-Site Scripting in Schneider ATV 630

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

[![Previous](/images/left-icon-16x16.png)](68)
[By Date](date.html#69)
[![Next](/images/right-icon-16x16.png)](70)

[![Previous](/images/left-icon-16x16.png)](68)
[By Thread](index.html#69)
[![Next](/images/right-icon-16x16.png)](70)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20250909-0 | Cross-Site Scripting in Schneider ATV 630

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 23 Sep 2025 11:55:36 +0000

---

```
CyberDanube Security Research 20250909-0
-------------------------------------------------------------------------------
                title| Reflected XSS
              product| ATV 630
   vulnerable version| "see Vulnerable versions"
        fixed version| none
           CVE number| CVE-2025-7746
               impact| Medium
             homepage| https://www.se.com/
                found| 2025-03-11
                   by| T. Weber (Office Vienna)
                     | D. Blagojevic
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Schneider’s purpose is to create Impact by empowering all to make the most of
our energy and resources, bridging progress and sustainability. At Schneider,
we call this Life Is On.
Our mission is to be the trusted partner in Sustainability and Efficiency.
[...]"

Source: https://www.se.com/ww/en/about-us/company-profile/

Vulnerable versions
-------------------------------------------------------------------------------
ATV630:
app     V3.4IE35
eth     V1.FIE26
cpld    V0.0IE16
pwr     V1.3IE08
mc      V3.4IE35
product v3.4IE35

See also the security notification from Schneider Electric:
https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-252-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-252-01.pdf

Vulnerability overview
-------------------------------------------------------------------------------
1) Reflected Cross-Site Scripting (CVE-2025-7746)
A Reflected Cross-Site Scripting vulnerability was identified in the web
interface of the device. The ClientNonce parameter can be abused to inject
JavaScript code. An attacker can exploit this vulnerability by luring a victim
to visit a malicious website. Furthermore, it is possible to hijack the session
of the attacked user.

Proof of Concept
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2025-7746)
During the logon process a ClientNonce can be specified to trigger a cross-site
scripting vulnerability. The following response to the server contains script
code to demonstrate this problem:
-------------------------------------------------------------------------------
GET /<redacted-patch-is-missing> HTTP/1.1
Host: 172.21.241.60
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate, br
X-Requested-With: XMLHttpRequest
Origin: http://172.21.241.60
Connection: close
Referer: http://172.21.241.60/
Cookie: 20c7ac82=1
-------------------------------------------------------------------------------
The webserver of the device responds without filtering the payload. Therefore,
the script code gets executed:
-------------------------------------------------------------------------------
HTTP/1.1 200 OK
Date: Fri, 09 Jan 1970 22:53:45 GMT
Server: Document not found
Connection: Close
Content-Type: text/html; charset=utf-8
Cache-Control: no-store, no-cache, must-revalidate, max-age=0
Set-Cookie: z9ZAqJtI=93f19ed6000bcdf9; path=/

r="<redacted-patch-is-missing>5r3e4AVzTY+Fkc5aEaga5CRsIC8eOUUux/Al36Ffr7U=,s=4fcb2dd77ee4bc4e1d9066e371c2034d1b55e07d28b9474e692c3f3531992b17,i=4096
-------------------------------------------------------------------------------
This vulnerability can be triggered via GET and POST requests.

Solution
-------------------------------------------------------------------------------
None. A firmware update will be published by Schneider Electric.

Workaround
-------------------------------------------------------------------------------
Restrict network access to management interface.

Recommendation
-------------------------------------------------------------------------------
A full security review is recommended by CyberDanube.

Contact Timeline
-------------------------------------------------------------------------------
2025-03-11: Contacting Schneider Electric PSIRT and sent advisory via PGP.
2025-03-12: Received case tracking number from Schneider Electric PSIRT.
2025-04-10: Asking for an update.
2025-04-14: Vendor confirmed the vulnerability.
2025-05-21: Asking for an update.
2025-05-22: Vendor targets to publish an update on 9th of September. Set
            disclosure date to 2025-09-09.
2025-06-23: Asking for an update; Vendor responded that they will notify us if
            an ealier publication is planned.
2025-09-02: PSIRT informed us that the patch cannot be delivered on 9th of
            September. Re-send advisory to sync about published information.
2025-09-04: Redacted XSS PoC code in the advisory has been redacted upon
            request from PSIRT.
2025-09-09: Coordinated release of security advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF T. Weber / @2025
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](68)
[By Date](date.html#69)
[![Next](/images/right-icon-16x16.png)](70)

[![Previous](/images/left-icon-16x16.png)](68)
[By Thread](index.html#69)
[![Next](/images/right-icon-16x16.png)](70)

### Current thread:

* **CyberDanube Security Research 20250909-0 | Cross-Site Scripting in Schneider ATV 630** *Thomas Weber | CyberDanube via Fulldisclosure (Sep 25)*

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

* [About/Contact](https://insecure.org/fy...