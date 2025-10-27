---
title: [KIS-2023-08] SugarCRM <= 12.2.0 Two SQL Injection	Vulnerabilities
url: https://seclists.org/fulldisclosure/2023/Aug/29
source: Full Disclosure
date: 2023-08-24
fetch_date: 2025-10-04T12:03:44.254807
---

# [KIS-2023-08] SugarCRM <= 12.2.0 Two SQL Injection	Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

![](/shared/images/nst-icons.svg#search)

# [KIS-2023-08] SugarCRM <= 12.2.0 Two SQL Injection Vulnerabilities

---

*From*: Egidio Romano <research () karmainsecurity com>
*Date*: Wed, 23 Aug 2023 14:13:03 +0200

---

```
----------------------------------------------------
SugarCRM <= 12.2.0 Two SQL Injection Vulnerabilities
----------------------------------------------------

[-] Software Link:

https://www.sugarcrm.com

[-] Affected Versions:

Version 12.2.0 and prior versions.
Version 12.0.2 and prior versions.
Version 11.0.5 and prior versions.

[-] Vulnerabilities Description:
```

1) User input passed through the “metrics” parameter to the
“/Forecasts/metrics”
REST API endpoint is not properly sanitized before being used to
construct a SQL
query. This can be exploited by malicious users to e.g. read sensitive
data from

```
the database through in-band SQL Injection attacks.
```

2) User input passed through the “placeholder\_fields” parameter to the
e.g.
“/Notes/{recordID}/link/history” REST API endpoint is not properly
sanitized before
being used to construct a SQL query. This can be exploited by malicious
users to
e.g. read sensitive data from the database through in-band SQL Injection
attacks.

```
[-] Proof of Concept:

https://karmainsecurity.com/pocs/CVE-2023-35811_1.php
https://karmainsecurity.com/pocs/CVE-2023-35811_2.php

[-] Solution:

Upgrade to version 12.3.0, 12.0.3, 11.0.6, or later.

[-] Disclosure Timeline:

[14/02/2023] - Vendor notified
[12/04/2023] - Fixed versions released
[17/06/2023] - CVE number assigned
[23/08/2023] - Publication of this advisory

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.mitre.org)
has assigned the name CVE-2023-35811 to these vulnerabilities.

[-] Credits:

Vulnerabilities discovered by Egidio Romano.

[-] Original Advisory:

https://karmainsecurity.com/KIS-2023-08

[-] Other References:

https://support.sugarcrm.com/Resources/Security/sugarcrm-sa-2023-008/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

### Current thread:

* **[KIS-2023-08] SugarCRM <= 12.2.0 Two SQL Injection Vulnerabilities** *Egidio Romano (Aug 23)*

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