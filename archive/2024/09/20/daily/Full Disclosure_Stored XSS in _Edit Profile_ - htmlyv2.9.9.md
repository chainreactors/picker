---
title: Stored XSS in "Edit Profile" - htmlyv2.9.9
url: https://seclists.org/fulldisclosure/2024/Sep/48
source: Full Disclosure
date: 2024-09-20
fetch_date: 2025-10-06T18:30:58.500517
---

# Stored XSS in "Edit Profile" - htmlyv2.9.9

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

[![Previous](/images/left-icon-16x16.png)](47)
[By Date](date.html#48)
[![Next](/images/right-icon-16x16.png)](49)

[![Previous](/images/left-icon-16x16.png)](47)
[By Thread](index.html#48)
[![Next](/images/right-icon-16x16.png)](49)

![](/shared/images/nst-icons.svg#search)

# Stored XSS in "Edit Profile" - htmlyv2.9.9

---

*From*: Andrey Stoykov <mwebsec () gmail com>
*Date*: Wed, 18 Sep 2024 18:15:36 +0000

---

```
# Exploit Title: Stored XSS in "Edit Profile" - htmlyv2.9.9
# Date: 9/2024
# Exploit Author: Andrey Stoykov
# Version: 2.9.9
# Tested on: Ubuntu 22.04
# Blog:
https://msecureltd.blogspot.com/2024/09/friday-fun-pentest-series-11-stored-xss.html

Stored XSS #1:

Steps to Reproduce:

1. Login as author
2. Browse to "Edit Profile"
3. In "Content" field add payload "><img src=x onerror=alert(1)>
4. Then refresh the "Edit Profile" page
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](47)
[By Date](date.html#48)
[![Next](/images/right-icon-16x16.png)](49)

[![Previous](/images/left-icon-16x16.png)](47)
[By Thread](index.html#48)
[![Next](/images/right-icon-16x16.png)](49)

### Current thread:

* **Stored XSS in "Edit Profile" - htmlyv2.9.9** *Andrey Stoykov (Sep 18)*

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