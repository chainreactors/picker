---
title: Microsoft PlayReady toolkit - codes release
url: https://seclists.org/fulldisclosure/2024/May/2
source: Full Disclosure
date: 2024-05-07
fetch_date: 2025-10-06T17:19:50.121263
---

# Microsoft PlayReady toolkit - codes release

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# Microsoft PlayReady toolkit - codes release

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Mon, 6 May 2024 10:52:07 +0200

---

```
Hello All,

We released codes for "Microsoft PlayReady toolkit", a tool that has
been developed as part of our research from 2022:

https://security-explorations.com/microsoft-playready.html#details

The toolkit illustrates the following:
- fake client device identity generation,
- acquisition of license and content keys for encrypted content,
- downloading and decryption of content,
- content inspection (MPEG-4 file format),
- Manifest files inspection,
- combination of content fragments into single, ready to play or
distribute, plaintext movie file,
- watermarking detection / checks,
- CDN auth bypass,
- license crawling,
- automatic content security check for Canal+ environment.

Please, note that due to “not fixed” status (Microsoft didn't revoke
group cert and Canal+ didn't implement auth checks for license server
among others) the following has been removed from the public package:
- crypto secrets such as STB private keys, PlayReady private group
key, Canal+ client SSL certificates, CDN / VOD secrets,
- STB PlayReady binary
- reverse engineering API traces
- functionality pertaining to VOD purchases / orders (online and SMS
based, affecting users' billing)

As such, the toolkit is not "functional / ready to use" (the codes
cannot be used for the piracy of Canal+ VOD content without the
missing secrets).
Yet, we hope the released codes help both security researchers
interested in PayTV / content security along content providers gain a
more in-depth understanding of Microsoft PlayReady technology
operation and its limitations. We hope it helps others avoid some
mistakes too.

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **Microsoft PlayReady toolkit - codes release** *Security Explorations (May 06)*

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