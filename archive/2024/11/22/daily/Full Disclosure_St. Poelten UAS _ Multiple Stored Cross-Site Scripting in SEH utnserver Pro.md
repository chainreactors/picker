---
title: St. Poelten UAS | Multiple Stored Cross-Site Scripting in SEH utnserver Pro
url: https://seclists.org/fulldisclosure/2024/Nov/7
source: Full Disclosure
date: 2024-11-22
fetch_date: 2025-10-06T19:23:06.403326
---

# St. Poelten UAS | Multiple Stored Cross-Site Scripting in SEH utnserver Pro

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

# St. Poelten UAS | Multiple Stored Cross-Site Scripting in SEH utnserver Pro

---

*From*: Weber Thomas via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 19 Nov 2024 10:09:04 +0000

---

```
St. Pölten UAS 20241118-0
-------------------------------------------------------------------------------
                title| Multiple Stored Cross-Site Scripting
              product| SEH utnserver Pro
   vulnerable version| 20.1.22
        fixed version| 20.1.35
           CVE number| CVE-2024-11304
               impact| High
             homepage| https://www.seh-technology.com/
                found| 2024-05-24
                   by| P. Riedl, J. Springer, P. Chistè, D. Sagl, S. Vogt
                     | These vulnerabilities were discovery during research at
                     | St.Pölten UAS, supported and coordinated by CyberDanube.
                     |
                     | https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"We are SEH from Bielefeld - manufacturer of high-quality network solutions.
With over 35 years of experience in the fields of printing and networks, we
offer our customers a broad and high-level expertise in solutions for all types
of business environments."

Source: https://www.seh-technology.com/us/company/about-us.html

Vulnerable versions
-------------------------------------------------------------------------------
utnserver Pro / 20.1.22
utnserver ProMAX / 20.1.22
INU-100 / 20.1.22

Vulnerability overview
-------------------------------------------------------------------------------
1) Multiple Stored Cross-Site Scripting (CVE-2024-11304)
Different settings on the web interface of the device can be abused to store
JavaScript code and execute it in the context of a user's browser.

Proof of Concept
-------------------------------------------------------------------------------
1) Multiple Stored Cross-Site Scripting (CVE-2024-11304)
The following snippet can be used to demonstrate, that stored cross-site
scripting is possible in multiple locations on the device:
"><script>alert(document.location)</script>

Examples are:
 * Users password: "usrMg_pwd"
   This can be displayed in cleartext and executed in the device configuration.
 * Certificate options: "Common name", "Organization name", "Locality name"
   This can be executed in the certificate information.
 * Device description: "Host name", "Contact person", "Description"
   This can be executed in "Device -> Description".
 * USB password via uploading a crafted "_parameters.txt" file: "usbMdg_pwd"
   This can be executed in the "Maintenance -> Content View" tab.

Saving this text to the device description leads to a persistent cross-site
scripting. Therefore, everyone who openes the device description executes the
injected code in the context of the own browser.

The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
Install firmware version 20.1.35 to fix the vulnerabilities.

Workaround
-------------------------------------------------------------------------------
None

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends SEH Computertechnik customers to upgrade the firmware to
the latest version available.

Contact Timeline
-------------------------------------------------------------------------------
2024-09-23: Contacting SEH Computertechnik and sent advisory to support.
            Support answered, that vulnerabilities are fixed in version
            20.1.35.
2024-10-21: Closed the issue and scheduled publication for November.
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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](8)

### Current thread:

* **St. Poelten UAS | Multiple Stored Cross-Site Scripting in SEH utnserver Pro** *Weber Thomas via Fulldisclosure (Nov 21)*

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