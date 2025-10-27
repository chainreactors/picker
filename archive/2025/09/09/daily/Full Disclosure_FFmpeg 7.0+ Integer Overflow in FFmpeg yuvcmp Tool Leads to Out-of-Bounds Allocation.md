---
title: FFmpeg 7.0+ Integer Overflow in FFmpeg yuvcmp Tool Leads to Out-of-Bounds Allocation
url: https://seclists.org/fulldisclosure/2025/Sep/26
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:53:03.989265
---

# FFmpeg 7.0+ Integer Overflow in FFmpeg yuvcmp Tool Leads to Out-of-Bounds Allocation

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# FFmpeg 7.0+ Integer Overflow in FFmpeg yuvcmp Tool Leads to Out-of-Bounds Allocation

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 7 Sep 2025 01:35:50 -0400

---

```
The FFmpeg tools/yuvcmp utility is vulnerable to an integer overflow when
large width and height parameters are supplied. The overflow occurs during
buffer size calculations (width * height) leading to incorrect allocation
sizes and subsequent memory corruption. An attacker controlling input
dimensions can trigger large or invalid memory allocations, leading to
denial of service (DoS), memory exhaustion, or potential heap corruption.
(FFmpeg 7.0-8.0)

*Impact:*

   -

   DoS via crash on allocation failure.
   -

   Potential heap overflow / OOM condition if overflow results in
   undersized allocations followed by large reads.

*Proof of Concept:*
./yuvcmp file1.yuv file2.yuv 70000 70000 pixelcmp

*Output:*yuvcmp.c:37:22: runtime error: signed integer overflow: 70000 *
70000 cannot be represented in type 'int'
==ERROR: AddressSanitizer: requested allocation size ... exceeds maximum
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **FFmpeg 7.0+ Integer Overflow in FFmpeg yuvcmp Tool Leads to Out-of-Bounds Allocation** *Ron E (Sep 08)*

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