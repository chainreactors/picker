---
title: Defense in depth -- the Microsoft way (part 93): SRP/SAFER	whitelisting goes black on Windows 11
url: https://seclists.org/fulldisclosure/2025/Sep/65
source: Full Disclosure
date: 2025-09-24
fetch_date: 2025-10-02T20:36:10.493310
---

# Defense in depth -- the Microsoft way (part 93): SRP/SAFER	whitelisting goes black on Windows 11

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

[![Previous](/images/left-icon-16x16.png)](64)
[By Date](date.html#65)
[![Next](/images/right-icon-16x16.png)](66)

[![Previous](/images/left-icon-16x16.png)](64)
[By Thread](index.html#65)
[![Next](/images/right-icon-16x16.png)](66)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 93): SRP/SAFER whitelisting goes black on Windows 11

---

*From*: Stefan Kanthak via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 22 Sep 2025 15:40:51 +0200

---

```
Hi @ll,

more than 2.5 years ago I posted "Defense in depth -- the Microsoft way
(part 82): INVALID/BOGUS AppLocker rules disable SAFER on Windows 11 22H2"
<https://seclists.org/fulldisclosure/2023/Feb/13>

In "SRP on Windows 11" <https://seclists.org/fulldisclosure/2023/Mar/1>
Andy Ful presented a persistent correction some days later.

Since several months now (unfortunately I can't tell the exact time)
SAFER shows the following BUG on Windows 11 24H2: it blocks execution of
%SystemRoot%\System32\SecurityHealth\10.0.27840.1000-0\SecurityHealthHost.exe
(really: it applies its default rule instead of a matching path rule)
despite a path rule which allows execution in %SystemRoot% and its
subdirectories!

After configuration of SAFER settings and ruleset via the script
<https://skanthak.hier-im-netz.de/download/NTX_SAFER.INF> provided and
documented in <https://skanthak.hier-im-netz.de/SAFER.html>, the following
line is written multiple times to %SystemRoot%\System32\LogFiles\SAFER.LOG
when an unprivileged user tries to open "Windows Security":

| svchost.exe (PID = 1234) identified
| \\?\C:\Windows\System32\SecurityHealth\10.0.27840.1000-0\SecurityHealthHost.exe
| as Disallowed using default rule, Guid = {11015445-d282-4f86-96a2-9e485f593302}

stay tuned, and far away from bug-riddled Windows 11
Stefan Kanthak
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](64)
[By Date](date.html#65)
[![Next](/images/right-icon-16x16.png)](66)

[![Previous](/images/left-icon-16x16.png)](64)
[By Thread](index.html#65)
[![Next](/images/right-icon-16x16.png)](66)

### Current thread:

* **Defense in depth -- the Microsoft way (part 93): SRP/SAFER whitelisting goes black on Windows 11** *Stefan Kanthak via Fulldisclosure (Sep 22)*

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