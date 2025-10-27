---
title: Defense in depth -- the Microsoft way (part 82): INVALID/BOGUS	AppLocker rules disable SAFER on Windows 11 22H2
url: https://seclists.org/fulldisclosure/2023/Feb/13
source: Full Disclosure
date: 2023-02-24
fetch_date: 2025-10-04T07:59:45.922843
---

# Defense in depth -- the Microsoft way (part 82): INVALID/BOGUS	AppLocker rules disable SAFER on Windows 11 22H2

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 82): INVALID/BOGUS AppLocker rules disable SAFER on Windows 11 22H2

---

*From*: "Stefan Kanthak" <stefan.kanthak () nexgo de>
*Date*: Wed, 22 Feb 2023 18:26:24 +0100

---

```
Hi @ll,

in Windows 11 22H2. some imbeciles from Redmond added the following
(of course WRONG and INVALID) registry entries and keys which they
dare to ship to their billion world-wide users:

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Srp\Gp]
"RuleCount"=dword:00000002
"LastWriteTime"=hex(b):01,00,00,00,00,00,00,00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Srp\Gp\DLL]

JFTR: the time stamp is 100ns past midnight on 1601-01-01;
      the rule count is wrong too, there are ZERO rules.

Although these entries are bogus and no rules are actually present,
they disable SAFER as documented, for example in
<https://www.microsoftpressstore.com/articles/article.aspx?p=2228450&seqNum=11>

FIX: remove these registry entries and/or keys to enable SAFER again!

stay tuned, and far away from the crap made in Redmond
Stefan
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **Defense in depth -- the Microsoft way (part 82): INVALID/BOGUS AppLocker rules disable SAFER on Windows 11 22H2** *Stefan Kanthak (Feb 22)*

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