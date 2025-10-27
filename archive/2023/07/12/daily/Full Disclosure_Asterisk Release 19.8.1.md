---
title: Asterisk Release 19.8.1
url: https://seclists.org/fulldisclosure/2023/Jul/25
source: Full Disclosure
date: 2023-07-12
fetch_date: 2025-10-04T11:56:36.727611
---

# Asterisk Release 19.8.1

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# Asterisk Release 19.8.1

---

*From*: Asterisk Development Team via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 07 Jul 2023 19:08:25 +0000

---

```
The Asterisk Development Team would like to announce security release
Asterisk 19.8.1.

The release artifacts are available for immediate download at
https://github.com/asterisk/asterisk/releases/tag/19.8.1
and
https://downloads.asterisk.org/pub/telephony/asterisk

The following security advisories were resolved in this release:
https://github.com/asterisk/asterisk/security/advisories/GHSA-4xjp-22g4-9fxm

Change Log for Release 19.8.1
========================================

Links:
----------------------------------------

 - [Full ChangeLog](https://downloads.asterisk.org/pub/telephony/asterisk/releases/ChangeLog-19.8.1.md)
 - [GitHub Diff](https://github.com/asterisk/asterisk/compare/19.8.0...19.8.1)
 - [Tarball](https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-19.8.1.tar.gz)
 - [Downloads](https://downloads.asterisk.org/pub/telephony/asterisk)

Summary:
----------------------------------------

- apply_patches: Use globbing instead of file/sort.
- bundled_pjproject: Backport 2 SSL patches from upstream
- bundled_pjproject: Backport security fixes from pjproject 2.13.1
- apply_patches: Sort patch list before applying

User Notes:
----------------------------------------

Upgrade Notes:
----------------------------------------

Closed Issues:
----------------------------------------

  - #188: [improvement]:  pjsip: Upgrade bundled version to pjproject 2.13.1 #187
  - #193: [bug]: third-party/apply-patches doesn't sort the patch file list before applying
  - #194: [bug]: Segfault/double-free in bundled pjproject using TLS transport
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **Asterisk Release 19.8.1** *Asterisk Development Team via Fulldisclosure (Jul 11)*

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