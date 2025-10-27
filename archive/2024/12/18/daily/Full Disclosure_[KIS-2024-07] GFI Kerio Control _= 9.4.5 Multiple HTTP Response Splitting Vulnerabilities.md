---
title: [KIS-2024-07] GFI Kerio Control <= 9.4.5 Multiple HTTP Response Splitting Vulnerabilities
url: https://seclists.org/fulldisclosure/2024/Dec/15
source: Full Disclosure
date: 2024-12-18
fetch_date: 2025-10-06T19:47:36.138773
---

# [KIS-2024-07] GFI Kerio Control <= 9.4.5 Multiple HTTP Response Splitting Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# [KIS-2024-07] GFI Kerio Control <= 9.4.5 Multiple HTTP Response Splitting Vulnerabilities

---

*From*: Egidio Romano <n0b0d13s () gmail com>
*Date*: Mon, 16 Dec 2024 19:27:17 +0100

---

```
---------------------------------------------------------------------------
GFI Kerio Control <= 9.4.5 Multiple HTTP Response Splitting Vulnerabilities
---------------------------------------------------------------------------

[-] Software Links:

https://gfi.ai/products-and-solutions/network-security-solutions/keriocontrol
http://download.kerio.com

[-] Affected Versions:

All versions from 9.2.5 to 9.4.5.

[-] Vulnerabilities Description:

There are multiple HTTP Response Splitting vulnerabilities in GFI
Kerio Control. Following are some of the affected pages:

- /nonauth/addCertException.cs
- /nonauth/guestConfirm.cs
- /nonauth/expiration.cs

User input passed to these pages via the "dest" GET parameter is not
properly sanitized before being used to generate a "Location" HTTP
header in a 302 HTTP response. Specifically, the application does not
correctly filter/remove linefeed (LF) characters. This can be
exploited to perform HTTP Response Splitting attacks, which in turn
might allow to carry out Reflected Cross-Site Scripting (XSS) and
possibly other attacks.

NOTE: the Reflected XSS vector might be abused to perform 1-click
Remote Code Execution (RCE) attacks.

[-] Proof of Concept:

https://karmainsecurity.com/pocs/CVE-2024-52875.php

[-] Solution:

No official solution is currently available.

[-] Disclosure Timeline:

[06/11/2024] - Vulnerabilities details sent to the vendor
[07/11/2024] - Vendor response stating "weâ€™ll take steps to resolve
these vulnerabilities in coming releases of Kerio Control"
[07/11/2024] - CVE identifier requested
[17/11/2024] - CVE identifier assigned
[17/11/2024] - Vendor was contacted inquiring about the ETA for the
next Kerio Control release; no response
[28/11/2024] - Vendor was contacted again and provided with a 1-click
RCE Proof of Concept script, emphasizing these should be considered
high-risk vulnerabilities that should be addressed as soon as possible
[28/11/2024] - Vendor response stating "thank you very much for this
information, I will immediately consult with rest of the team"
[03/12/2024] - Vendor email stating "would you mind to share with us
any script you used while exploiting the vulnerabilities?"
[03/12/2024] - Proof of Concept script and replication steps sent to
the vendor, along with a follow-up inquiry about the ETA for a patched
Kerio Control version; no response
[06/12/2024] - Vendor was informed that public disclosure is scheduled
to occur within two weeks
[11/12/2024] - Vendor response stating "these vulnerabilities were
already fixed and will be part of Kerio Control 9.4.5p1 which is now
with our internal QA team"
[16/12/2024] - Public disclosure

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.mitre.org) has
assigned the name CVE-2024-52875 to these vulnerabilities.

[-] Credits:

Vulnerabilities discovered by Egidio Romano.

[-] Original Advisory:

http://karmainsecurity.com/KIS-2024-07

[-] Technical Writeup:

https://karmainsecurity.com/hacking-kerio-control-via-cve-2024-52875
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **[KIS-2024-07] GFI Kerio Control <= 9.4.5 Multiple HTTP Response Splitting Vulnerabilities** *Egidio Romano (Dec 16)*

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