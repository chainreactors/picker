---
title: User Enumeration in IServ Schoolserver Web Login
url: https://seclists.org/fulldisclosure/2025/Sep/38
source: Full Disclosure
date: 2025-09-12
fetch_date: 2025-10-02T20:03:10.120032
---

# User Enumeration in IServ Schoolserver Web Login

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

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#38)
[![Next](/images/right-icon-16x16.png)](40)

![](/shared/images/nst-icons.svg#search)

# User Enumeration in IServ Schoolserver Web Login

---

*From*: naphthalin via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 9 Sep 2025 14:04:32 +0200

---

```
“I know where your children go to school.”
```

The web front end of the IServ school server from IServ GmbH allows user
enumeration. Responses during failed login attempts differ, depending on
if the user account exists, does not exist and other conditions. While
this does not pose a security risk in many applications, it has to be
considered extremely problematic in software designed for schools. Due
to the widespread use of IServ in Germany, it would be possible to find
out a child's school based on their first and last name, provided that
the school uses IServ.

```

```

Particularly noteworthy threat scenarios include enumeration by
perpetrators of domestic violence, by groups involved in cybergrooming
and sextortion (such as the “764” gang), or targeting of children of
particularly exposed individuals.

```

```

The manufacturer was contacted and stated that they do not interpret the
issue as a vulnerability. There also appear to be no concerns regarding
data protection and GDPR compliance. They further confirm that
enumeration would also be possible via other interfaces and they do not
intend to provide a fix.

```
Disclosure Timeline:
08.09.2025 - Vulnerability identified
08.09.2025 - Vendor notified
08.09.2025 - Vulnerability disputed by vendor
09.09.2025 - Public Disclosure
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](36)
[By Thread](index.html#38)
[![Next](/images/right-icon-16x16.png)](40)

### Current thread:

* **User Enumeration in IServ Schoolserver Web Login** *naphthalin via Fulldisclosure (Sep 10)*

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