---
title: St. Poelten UAS | Multiple XSS in Advantech EKI 15XX Series
url: https://seclists.org/fulldisclosure/2023/Aug/13
source: Full Disclosure
date: 2023-08-12
fetch_date: 2025-10-04T12:03:31.501123
---

# St. Poelten UAS | Multiple XSS in Advantech EKI 15XX Series

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# St. Poelten UAS | Multiple XSS in Advantech EKI 15XX Series

---

*From*: Weber Thomas via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 8 Aug 2023 09:19:32 +0000

---

```
St. Pölten UAS
-------------------------------------------------------------------------------
               title| Multiple XSS in Advantech
             product| Advantech EKI-1524-CE series, EKI-1522 series,
                    | EKI-1521 series
  vulnerable version| <=1.21 (CVE-2023-4202), <=1.24 (CVE-2023-4203)
       fixed version| 1.26
          CVE number| CVE-2023-4202, CVE-2023-4203
              impact| Medium
            homepage| https://advantech.com
               found| 2023-05-04
                  by| R. Haas, A. Resanovic, T. Etzenberger, M. Bineder
                    | This vulnerability was discovery during research at
                    | St. Pölten UAS, supported and coordinated by CyberDanube.
                    |
                    | https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
“Advantech’s corporate vision is to enable an intelligent planet. The company
is a global leader in the fields of IoT intelligent systems and embedded
platforms. To embrace the trends of IoT, big data, and artificial intelligence,
Advantech promotes IoT hardware and software solutions with the Edge
Intelligence WISE-PaaS core to assist business partners and clients in
connecting their industrial chains. Advantech is also working with business
partners to co-create business ecosystems that accelerate the goal of
industrial intelligence.”

Source: https://www.advantech.com/en/about

Vulnerable versions
-------------------------------------------------------------------------------
EKI-1524-CE series / 1.21 (CVE-2023-4202)
EKI-1522-CE series / 1.21 (CVE-2023-4202)
EKI-1521-CE series / 1.21 (CVE-2023-4202)

EKI-1524-CE series / 1.24 (CVE-2023-4203)
EKI-1522-CE series / 1.24 (CVE-2023-4203)
EKI-1521-CE series / 1.24 (CVE-2023-4203)

Vulnerability overview
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (XSS) (CVE-2023-4202, CVE-2023-4203)
Two stored cross-site scripting vulnerabilities has been identified in the
firmware of the device. The first XSS was identified in the "Device Name" field
and the second XSS was found in the "Ping" tool. This can be exploited in the
context of a victim's session.

Proof of Concept
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (XSS)
Both cross-site scripting vulnerabilities are permanently affecting the device.

1.1) Stored XSS in Device Name CVE-2023-4202
The first vulnerability can be triggerd by setting the device name
("System->Device Name") to the following value:
"><script>alert("document.cookie")</script>

This code prints out the cached cookies to the screen.

1.2) Stored XSS in Ping Function CVE-2023-4203
The second XSS vulnerability can be found in "Tools->Ping". The following GET
request prints the current cached cookies of a user's session to the screen.

http://$IP/cgi-bin/ping.sh?random_num=2013&ip=172.16.0.141%3b%20<script>alert(1)</script>&size=56&count=1&interface=eth0&_=1682793104513

An alternative to the used payload is using "onmouseover" event tags. In this
case it prints out the number "1337":
" onmousemove="alert(1337)"

The vulnerability was manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
Upgrade to the newest available firmware.

Workaround
-------------------------------------------------------------------------------
None.

Recommendation
-------------------------------------------------------------------------------
Advantech customers are advised to upgrade the firware to the latest
available version.

Contact Timeline
-------------------------------------------------------------------------------
2023-05-16: Contacting vendor via security contact.
2023-05-24: Contact stated that issue 1.1) is solved after firmware v1.21.
            The contact is trying to reproduce issue 1.2; Gave advice to
            reproduce issue.
2023-05-25: Contact stated that new firmware should resolve the issue.
2023-06-03: Sent new payload to the vendor.
2023-06-05: Vendor asked for clarification; Sent further explaination to the
            contact; Vendor contact said he knows a solution.
2023-06-22: Asked for an update; Contact stated that the beta firmware should
            resolve the issues.
2023-06-27: Asked for the release date.
2023-07-04: Contact stated, that they are currently doing QA tests.
2023-07-06: Asked if issue 1.1 is really resolved to be released; Vendor stated
            that it can be published.
2023-07-17: Assigned CVE numbers for the issues. Asked for an update.
2023-07-18: Vendor contact stated that the firmware will be released end of
            July.
2023-08-07: Asked contact for the new firmware version.
2023-08-08: Received version 1.26 as the official released firmware with fixes.
            Coordinated release of security advisory.

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **St. Poelten UAS | Multiple XSS in Advantech EKI 15XX Series** *Weber Thomas via Fulldisclosure (Aug 11)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](...