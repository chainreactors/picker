---
title: Certified Asterisk Security Release certified-20.7-cert4
url: https://seclists.org/fulldisclosure/2025/Jan/7
source: Full Disclosure
date: 2025-01-17
fetch_date: 2025-10-06T20:13:46.631978
---

# Certified Asterisk Security Release certified-20.7-cert4

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# Certified Asterisk Security Release certified-20.7-cert4

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 09 Jan 2025 20:22:31 +0000

---

```
The Asterisk Development Team would like to announce security release
Certified Asterisk 20.7-cert4.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/certified-20.7-cert4
and
https://downloads.asterisk.org/pub/telephony/certified-asterisk

Repository: https://github.com/asterisk/asterisk
Tag: certified-20.7-cert4

## Change Log for Release asterisk-certified-20.7-cert4

### Links:

 - [Full
ChangeLog](https://downloads.asterisk.org/pub/telephony/certified-asterisk/releases/ChangeLog-certified-20.7-cert4.md)
 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/certified-20.7-cert3...certified-20.7-cert4)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/certified-asterisk/asterisk-certified-20.7-cert4.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/certified-asterisk)

### Summary:

- Commits: 1
- Commit Authors: 1
- Issues Resolved: 0
- Security Advisories Resolved: 1
  - [GHSA-33x6-fj46-6rfh](https://github.com/asterisk/asterisk/security/advisories/GHSA-33x6-fj46-6rfh): Path traversal
via AMI ListCategories allows access to outside files

### User Notes:

- #### manager.c: Restrict ListCategories to the configuration directory.
  The ListCategories AMI action now restricts files to the
  configured configuration directory.

### Upgrade Notes:

### Commit Authors:

- Ben Ford: (1)

## Issue and Commit Detail:

### Closed Issues:

  - !GHSA-33x6-fj46-6rfh: Path traversal via AMI ListCategories allows access to outside files

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **Certified Asterisk Security Release certified-20.7-cert4** *Asterisk Development Team via Fulldisclosure (Jan 15)*

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