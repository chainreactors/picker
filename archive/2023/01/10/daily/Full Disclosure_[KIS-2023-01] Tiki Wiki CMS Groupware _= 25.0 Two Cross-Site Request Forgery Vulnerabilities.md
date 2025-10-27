---
title: [KIS-2023-01] Tiki Wiki CMS Groupware <= 25.0 Two Cross-Site Request Forgery Vulnerabilities
url: https://seclists.org/fulldisclosure/2023/Jan/2
source: Full Disclosure
date: 2023-01-10
fetch_date: 2025-10-04T03:28:16.444246
---

# [KIS-2023-01] Tiki Wiki CMS Groupware <= 25.0 Two Cross-Site Request Forgery Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# [KIS-2023-01] Tiki Wiki CMS Groupware <= 25.0 Two Cross-Site Request Forgery Vulnerabilities

---

*From*: Egidio Romano <research () karmainsecurity com>
*Date*: Mon, 09 Jan 2023 21:08:38 +0100

---

```
------------------------------------------------------------------------------
```

Tiki Wiki CMS Groupware <= 25.0 Two Cross-Site Request Forgery
Vulnerabilities

```
------------------------------------------------------------------------------

[-] Software Link:

https://tiki.org

[-] Affected Versions:

Version 25.0 and prior versions.

[-] Vulnerabilities Description:
```

1) The /tiki-importer.php script does not implement any protection
against Cross-Site Request Forgery (CSRF) attacks. As such, an attacker
might force an authenticated user to import arbitrary content (wiki
pages) into TikiWiki by tricking a victim user into browsing to a
specially crafted web page.

```

```

2) The /tiki-import\_sheet.php script does not implement any protection
against Cross-Site Request Forgery (CSRF) attacks. As such, an attacker
might force an authenticated user to import arbitrary sheets into
TikiWiki by tricking a victim user into browsing to a specially crafted
web page. Successful exploitation of this vulnerability requires the
“Spreadsheets” feature to be enabled.

```
[-] Solution:

No official solution is currently available.

[-] Disclosure Timeline:

[06/03/2022] - Vendor notified
[09/01/2023] - Public disclosure

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.mitre.org)
has assigned the name CVE-2023-22852 to this vulnerability.

[-] Credits:

Vulnerabilities discovered by Egidio Romano.

[-] Original Advisory:

http://karmainsecurity.com/KIS-2023-01

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **[KIS-2023-01] Tiki Wiki CMS Groupware <= 25.0 Two Cross-Site Request Forgery Vulnerabilities** *Egidio Romano (Jan 09)*

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