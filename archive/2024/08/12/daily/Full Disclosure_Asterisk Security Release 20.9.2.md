---
title: Asterisk Security Release 20.9.2
url: https://seclists.org/fulldisclosure/2024/Aug/12
source: Full Disclosure
date: 2024-08-12
fetch_date: 2025-10-06T18:02:15.530937
---

# Asterisk Security Release 20.9.2

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

![](/shared/images/nst-icons.svg#search)

# Asterisk Security Release 20.9.2

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 08 Aug 2024 13:28:49 +0000

---

```
The Asterisk Development Team would like to announce security release
Asterisk 20.9.2.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/20.9.2
and
https://downloads.asterisk.org/pub/telephony/asterisk

Repository: https://github.com/asterisk/asterisk
Tag: 20.9.2

## Change Log for Release asterisk-20.9.2

### Links:

 - [Full ChangeLog](https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-20.9.2.md)
 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/20.9.1...20.9.2)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20.9.2.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/asterisk)

### Summary:

- Commits: 1
- Commit Authors: 1
- Issues Resolved: 0
- Security Advisories Resolved: 1
  - [GHSA-c4cg-9275-6w44](https://github.com/asterisk/asterisk/security/advisories/GHSA-c4cg-9275-6w44):
Write=originate, is sufficient permissions for code execution / System() dialplan

### User Notes:

### Upgrade Notes:

### Commit Authors:

- George Joseph: (1)

## Issue and Commit Detail:

### Closed Issues:

  - !GHSA-c4cg-9275-6w44: Write=originate, is sufficient permissions for code execution / System() dialplan

### Commits By Author:

- #### George Joseph (1):
  - manager.c: Add entries to Originate blacklist

### Commit List:

-  manager.c: Add entries to Originate blacklist

### Commit Details:

#### manager.c: Add entries to Originate blacklist
  Author: George Joseph
  Date:   2024-07-22

  Added Reload and DBdeltree to the list of dialplan application that
  can't be executed via the Originate manager action without also
  having write SYSTEM permissions.

  Added CURL, DB*, FILE, ODBC and REALTIME* to the list of dialplan
  functions that can't be executed via the Originate manager action
  without also having write SYSTEM permissions.

  If the Queue application is attempted to be run by the Originate
  manager action and an AGI parameter is specified in the app data,
  it'll be rejected unless the manager user has either the AGI or
  SYSTEM permissions.

  Resolves: #GHSA-c4cg-9275-6w44

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#12)
[![Next](/images/right-icon-16x16.png)](13)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#12)
[![Next](/images/right-icon-16x16.png)](13)

### Current thread:

* **Asterisk Security Release 20.9.2** *Asterisk Development Team via Fulldisclosure (Aug 10)*

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