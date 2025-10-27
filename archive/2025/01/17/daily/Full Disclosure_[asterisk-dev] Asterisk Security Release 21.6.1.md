---
title: [asterisk-dev] Asterisk Security Release 21.6.1
url: https://seclists.org/fulldisclosure/2025/Jan/1
source: Full Disclosure
date: 2025-01-17
fetch_date: 2025-10-06T20:13:55.288531
---

# [asterisk-dev] Asterisk Security Release 21.6.1

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

# [asterisk-dev] Asterisk Security Release 21.6.1

---

*From*: Asterisk Development Team <asteriskteam () digium com>
*Date*: Thu, 9 Jan 2025 14:26:45 -0600

---

```
The Asterisk Development Team would like to announce security release
Asterisk 21.6.1.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/21.6.1
and
https://downloads.asterisk.org/pub/telephony/asterisk

Repository: https://github.com/asterisk/asterisk
Tag: 21.6.1

## Change Log for Release asterisk-21.6.1

### Links:

 - [Full ChangeLog](
https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-21.6.1.md
)
 - [GitHub Diff](
https://github.com/asterisk/asterisk/compare/21.6.0...21.6.1)
 - [Tarball](
https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-21.6.1.tar.gz
)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/asterisk)

### Summary:

- Commits: 1
- Commit Authors: 1
- Issues Resolved: 0
- Security Advisories Resolved: 1
  - [GHSA-33x6-fj46-6rfh](
https://github.com/asterisk/asterisk/security/advisories/GHSA-33x6-fj46-6rfh):
Path traversal via AMI ListCategories allows access to outside files

### User Notes:

- #### manager.c: Restrict ListCategories to the configuration directory.

  The ListCategories AMI action now restricts files to the
  configured configuration directory.

### Upgrade Notes:

### Commit Authors:

- Ben Ford: (1)

## Issue and Commit Detail:

### Closed Issues:

  - !GHSA-33x6-fj46-6rfh: Path traversal via AMI ListCategories allows
access to outside files

### Commits By Author:

- #### Ben Ford (1):
  - manager.c: Restrict ListCategories to the configuration directory.

### Commit List:

-  manager.c: Restrict ListCategories to the configuration directory.

### Commit Details:

#### manager.c: Restrict ListCategories to the configuration directory.
  Author: Ben Ford
  Date:   2024-12-17

  When using the ListCategories AMI action, it was possible to traverse
  upwards through the directories to files outside of the configured
  configuration directory. This action is now restricted to the configured
  directory and an error will now be returned if the specified file is
  outside of this limitation.

  Resolves: #GHSA-33x6-fj46-6rfh

  UserNote: The ListCategories AMI action now restricts files to the
  configured configuration directory.
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

* **[asterisk-dev] Asterisk Security Release 21.6.1** *Asterisk Development Team (Jan 15)*

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