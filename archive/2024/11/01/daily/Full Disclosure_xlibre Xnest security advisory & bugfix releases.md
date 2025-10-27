---
title: xlibre Xnest security advisory & bugfix releases
url: https://seclists.org/fulldisclosure/2024/Oct/20
source: Full Disclosure
date: 2024-11-01
fetch_date: 2025-10-06T19:21:06.858306
---

# xlibre Xnest security advisory & bugfix releases

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# xlibre Xnest security advisory & bugfix releases

---

*From*: "Enrico Weigelt, metux IT consult" <info () metux net>
*Date*: Thu, 31 Oct 2024 16:40:24 +0100

---

```
XLibre project security advisory
---------------------------------

As Xlibre Xnest is based on Xorg, it is affected by some security issues
which recently became known in Xorg:

 CVE-2024-9632: can be triggered by providing a modified bitmap to the
X.Org server.
 CVE-2024-9632: Heap-based buffer overflow privilege escalation in
_XkbSetCompatMap

See:  https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9632

Affected versions:

  * 24.1.0
  * 24.2.0

24.1.x release:

   Repo:   https://gitlab.freedesktop.org/metux/xserver.git
   Branch: xlibre/xnest/24.1
   Tag:    xnest-24.1.1
   SHA:    11450b0946c1035944c5946d665f21f83356b6b9

24.2.x release:

   Repo:   https://gitlab.freedesktop.org/metux/xserver.git
   Branch: xlibre/xnest/24.2
   Tag:    xnest-24.2.1
   SHA:    9a6aec9bf62b6bdd75795a5e28648d4af07fe413

These bugfix branches also contain several other pointer and bounds
related problems that haven't been rated as possibly exploitable yet,
but no other unnecessary changes which don't fix actual bugs.

All users are strongly advised to upgrade to the fixed mainenance
releases ASAP.

--mtx

--
---
Enrico Weigelt, metux IT consult
Free software and Linux embedded engineering
info () metux net -- +49-151-27565287
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **xlibre Xnest security advisory & bugfix releases** *Enrico Weigelt, metux IT consult (Oct 31)*

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