---
title: libheif v1.21.0 Integer Overflow in Y4M Loader leading to Uncontrolled Memory Allocation
url: https://seclists.org/fulldisclosure/2025/Sep/22
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:53:08.360617
---

# libheif v1.21.0 Integer Overflow in Y4M Loader leading to Uncontrolled Memory Allocation

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# libheif v1.21.0 Integer Overflow in Y4M Loader leading to Uncontrolled Memory Allocation

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 23 Aug 2025 11:51:27 -0400

---

```
An integer overflow vulnerability exists in the Y4M input loader (loadY4M
in decoder_y4m.cc) of libheif. The loader fails to properly validate the
width and height values declared in the Y4M file header. Supplying a
crafted .y4m file with extremely large dimensions (e.g., W2147483647
H2147483647) causes integer overflow during buffer size calculations. This
results in uncontrolled memory allocation requests that exceed supported
limits. Depending on the build and allocator behavior, this may cause a
denial of service (application crash or out-of-memory) or heap buffer
overflow leading to potential memory corruption.

*Impact*

   -

   *Denial of Service (DoS):* Application crash or OOM when parsing
   malicious Y4M.
   -

   *Potential Memory Corruption:* If allocation wraps around to a smaller
   buffer, subsequent writes may overrun heap memory, possibly leading to
   arbitrary code execution under certain conditions.

*Proof of Concept:*Run through a libheif build with Y4M enabled (e.g.,
heif-enc or a harness linked against decoder_y4m.cc), AddressSanitizer
reports:

ERROR: AddressSanitizer: requested allocation size 0x400000000000000f ...
SUMMARY: AddressSanitizer: allocation-size-too-big in
HeifPixelImage::ImagePlane::alloc
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **libheif v1.21.0 Integer Overflow in Y4M Loader leading to Uncontrolled Memory Allocation** *Ron E (Sep 08)*

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