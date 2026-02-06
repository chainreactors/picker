---
title: [KIS-2026-02] Blesta <= 5.13.1 (Admin Interface) Multiple PHP Object Injection Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Feb/1
source: Full Disclosure
date: 2026-02-05
fetch_date: 2026-02-06T04:10:23.894843
---

# [KIS-2026-02] Blesta <= 5.13.1 (Admin Interface) Multiple PHP Object Injection Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# [KIS-2026-02] Blesta <= 5.13.1 (Admin Interface) Multiple PHP Object Injection Vulnerabilities

---

*From*: Egidio Romano <n0b0d13s () gmail com>
*Date*: Wed, 4 Feb 2026 11:49:40 +0100

---

```
--------------------------------------------------------------------------------
Blesta <= 5.13.1 (Admin Interface) Multiple PHP Object Injection Vulnerabilities
--------------------------------------------------------------------------------

[-] Software Link:

https://www.blesta.com

[-] Affected Versions:

All versions from 3.0.0 to 5.13.1.

[-] Vulnerabilities Description:

The vulnerabilities exist because user input passed through the "vars"
and "order_info" POST parameters when dispatching the
/app/controllers/admin_clients.php script, and through the
"$group_name" POST parameter when dispatching the
/app/controllers/admin_company_groups.php script, is not properly
sanitized before being used in a call to the unserialize() PHP
function. This can be exploited by malicious administrator users to
inject arbitrary PHP objects into the application scope, allowing them
to perform a variety of attacks, such as executing arbitrary PHP code
(RCE).

[-] Proof of Concept:

https://karmainsecurity.com/pocs/CVE-2026-25615.php

[-] Solution:

Apply the vendor patch or upgrade to version 5.13.2 or later.

[-] Disclosure Timeline:

[19/01/2026] - Vendor notified

[20/01/2026] - Vendor response stating: “this issue was previously
identified during an internal security review”

[22/01/2026] - CVE identifier requested

[28/01/2026] - Version 5.13.2 released

[31/01/2026] - Version 5.13.3 released to address regressions
introduced in 5.13.2

[03/02/2026] - CVE identifier assigned

[04/02/2026] - Public disclosure

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.org) has
assigned the name CVE-2026-25615 to these vulnerabilities.

[-] Credits:

Vulnerabilities discovered by Egidio Romano.

[-] Other References:

https://www.blesta.com/2026/01/28/security-advisory/

[-] Original Advisory:

https://karmainsecurity.com/KIS-2026-02
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **[KIS-2026-02] Blesta <= 5.13.1 (Admin Interface) Multiple PHP Object Injection Vulnerabilities** *Egidio Romano (Feb 04)*

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