---
title: Defense in depth -- the Microsoft way (part 88): a SINGLE	command line shows about 20, 000 instances of CWE-73
url: https://seclists.org/fulldisclosure/2024/Sep/53
source: Full Disclosure
date: 2024-09-30
fetch_date: 2025-10-06T18:26:09.194925
---

# Defense in depth -- the Microsoft way (part 88): a SINGLE	command line shows about 20, 000 instances of CWE-73

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

[![Previous](/images/left-icon-16x16.png)](52)
[By Date](date.html#53)
[![Next](/images/right-icon-16x16.png)](54)

[![Previous](/images/left-icon-16x16.png)](52)
[By Thread](index.html#53)
[![Next](/images/right-icon-16x16.png)](54)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 88): a SINGLE command line shows about 20, 000 instances of CWE-73

---

*From*: "Stefan Kanthak" <stefan.kanthak () nexgo de>
*Date*: Tue, 24 Sep 2024 22:11:57 +0200

---

```
Hi @ll,

<https://cwe.mitre.org/data/definitions/73.html>
CWE-73: External Control of File Name or Path
is a well-known and well-documented weakness.

<https://seclists.org/fulldisclosure/2020/Mar/48> as well as
<https://skanthak.homepage.t-online.de/offender.html> demonstrate how to
(ab)use just one instance of this weakness (introduced about 7 years ago
with Microsoft Defender, so-called "security software") due to an
environment variable in the (registered) path name of an executable file
to gain execution of arbitrary code.

But that's of course not the only instance of this VERY EASY to exploit
weakness present in ALL versions of Windows since more than 30 (in words:
THIRTY) years -- start a command processor and run the following command
line to show about 20,000 instances of path names registered with (user-
controlled) environment variables:

    REG.exe QUERY HKEY_LOCAL_MACHINE /C /D /F "%*%\\" /S

stay tuned, and far away from the vulnerable crap made in Redmond
Stefan Kanthak

PS: just yesterday, Microsoft dared to publish

<https://www.microsoft.com/en-us/security/blog/2024/09/23/securing-our-future-september-2024-progress-update-on-microsofts-secur
e-future-initiative-sfi/>,
    bragging "we've dedicated the equivalent of 34,000 full-time engineers
    to SFI-making it the largest cybersecurity engineering effort in history"
    What about dedicating the equivalent of just ONE full-time employee to
    every instance of just ONE ow Windows weaknesses?

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](52)
[By Date](date.html#53)
[![Next](/images/right-icon-16x16.png)](54)

[![Previous](/images/left-icon-16x16.png)](52)
[By Thread](index.html#53)
[![Next](/images/right-icon-16x16.png)](54)

### Current thread:

* **Defense in depth -- the Microsoft way (part 88): a SINGLE command line shows about 20, 000 instances of CWE-73** *Stefan Kanthak (Sep 28)*

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