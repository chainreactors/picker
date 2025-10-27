---
title: FFmpeg 7.0+ Integer Overflow in DSCP Option Handling of FFmpeg	UDP Protocol
url: https://seclists.org/fulldisclosure/2025/Sep/31
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:52:57.657817
---

# FFmpeg 7.0+ Integer Overflow in DSCP Option Handling of FFmpeg	UDP Protocol

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

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

![](/shared/images/nst-icons.svg#search)

# FFmpeg 7.0+ Integer Overflow in DSCP Option Handling of FFmpeg UDP Protocol

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 7 Sep 2025 02:55:20 -0400

---

```
A vulnerability exists in the FFmpeg UDP protocol implementation (
libavformat/udp.c) where the dscp parameter is parsed from a URI and
left-shifted without bounds checking. Supplying a maximum 32-bit signed
integer (2147483647) triggers undefined behavior due to a left shift that
exceeds the representable range of int. This results in abnormal process
termination (DoS) and may lead to miscompiled logic or further memory
corruption depending on compiler optimizations. (FFmpeg 7.0-8.0)

*Impact:*

   -

   Crashes or aborts when parsing crafted input.
   -

   Although primarily DoS, undefined behavior can lead to logic
   miscompilation or corrupted socket options.

*Proof of Concept:*./ffmpeg -i udp://127.0.0.1:1234?dscp=2147483647

*Output:*
libavformat/udp.c:830:14: runtime error: left shift of 2147483647 by 2
places cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior
libavformat/udp.c:830:14 in
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](30)
[By Date](date.html#31)
[![Next](/images/right-icon-16x16.png)](32)

[![Previous](/images/left-icon-16x16.png)](30)
[By Thread](index.html#31)
[![Next](/images/right-icon-16x16.png)](32)

### Current thread:

* **FFmpeg 7.0+ Integer Overflow in DSCP Option Handling of FFmpeg UDP Protocol** *Ron E (Sep 08)*

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