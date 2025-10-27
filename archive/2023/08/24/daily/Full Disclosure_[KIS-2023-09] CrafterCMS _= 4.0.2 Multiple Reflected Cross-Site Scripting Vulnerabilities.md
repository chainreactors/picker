---
title: [KIS-2023-09] CrafterCMS <= 4.0.2 Multiple Reflected Cross-Site Scripting Vulnerabilities
url: https://seclists.org/fulldisclosure/2023/Aug/30
source: Full Disclosure
date: 2023-08-24
fetch_date: 2025-10-04T12:03:42.916674
---

# [KIS-2023-09] CrafterCMS <= 4.0.2 Multiple Reflected Cross-Site Scripting Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

![](/shared/images/nst-icons.svg#search)

# [KIS-2023-09] CrafterCMS <= 4.0.2 Multiple Reflected Cross-Site Scripting Vulnerabilities

---

*From*: Egidio Romano <research () karmainsecurity com>
*Date*: Wed, 23 Aug 2023 14:14:05 +0200

---

```
---------------------------------------------------------------------------
```

CrafterCMS <= 4.0.2 Multiple Reflected Cross-Site Scripting
Vulnerabilities

```
---------------------------------------------------------------------------

[-] Software Link:

https://craftercms.org

[-] Affected Versions:

Version 4.0.2 and prior versions.
Version 3.1.27 and prior versions.

[-] Vulnerabilities Description:
```

There are multiple Reflected Cross-Site Scripting vulnerabilities
affecting CrafterCMS.
The vulnerabilities exist in every API endpoint that reflect some input
parameter and

```
do produce XML responses. Following are some examples:
```

• /api/1/site/url/transform - url and transformerName parameters are
affected

```
• /api/1/site/content_store/children - url parameter is affected
• /api/1/site/content_store/item - url parameter is affected

[-] Solution:

Upgrade to version 4.0.3, 3.1.28, or later.

[-] Disclosure Timeline:

[22/11/2022] - Vendor notified
[24/03/2023] - Fixed versions released
[03/08/2023] - CVE number assigned
[23/08/2023] - Publication of this advisory

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.mitre.org)
has assigned the name CVE-2023-4136 to these vulnerabilities.

[-] Credits:
```

Vulnerabilities discovered by Egidio Romano, working with IMQ Minded
Security.

```
[-] Original Advisory:

https://karmainsecurity.com/KIS-2023-09

[-] Other References:

https://docs.craftercms.org/en/4.1/security/advisory.html#cv-2023080301
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

### Current thread:

* **[KIS-2023-09] CrafterCMS <= 4.0.2 Multiple Reflected Cross-Site Scripting Vulnerabilities** *Egidio Romano (Aug 23)*

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