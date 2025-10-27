---
title: DjVuLibre 3.5.29 ZPCodec Unsigned Integer Overflow in	Arithmetic Encoding
url: https://seclists.org/fulldisclosure/2025/Sep/24
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:53:06.255380
---

# DjVuLibre 3.5.29 ZPCodec Unsigned Integer Overflow in	Arithmetic Encoding

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

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

![](/shared/images/nst-icons.svg#search)

# DjVuLibre 3.5.29 ZPCodec Unsigned Integer Overflow in Arithmetic Encoding

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 6 Sep 2025 03:32:57 -0400

---

```
The DjVuLibre document compression library (tested version 3.5.29) contains
multiple instances of unsigned integer overflow in the ZPCodec.cpp
component. During arithmetic encoding operations (e.g., zemit, encode_lps,
encode_lps_simple, eflush), crafted input can cause arithmetic wraparound
(0-1, 1-2, or value+UINT_MAX). These operations rely on precise probability
modeling for entropy encoding, and wraparound corrupts encoder state. An
attacker can supply malicious input to c44 that triggers underflow, leading
to incorrect buffer writes, memory corruption, or crashes.

*Impact:*

   - Crash confirmed with UBSan.
   - Potential for corrupted encoded output, incorrect memory access, or
   exploitable memory corruption.
   - High risk in systems processing untrusted PPM/DjVu input.

*Proof of Concept:*

convert -size 1000x1000 gradient: overflow.ppm

ASAN_OPTIONS=detect_leaks=0,abort_on_error=1 \

UBSAN_OPTIONS=print_stacktrace=1 \

./tools/c44 overflow.ppm out.djvu

*Sanitizer Output:*

ZPCodec.cpp:1030:18: runtime error: unsigned integer overflow: 0 - 1 cannot
be represented in type 'unsigned int'

SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ZPCodec.cpp:1030:18
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](23)
[By Date](date.html#24)
[![Next](/images/right-icon-16x16.png)](25)

[![Previous](/images/left-icon-16x16.png)](23)
[By Thread](index.html#24)
[![Next](/images/right-icon-16x16.png)](25)

### Current thread:

* **DjVuLibre 3.5.29 ZPCodec Unsigned Integer Overflow in Arithmetic Encoding** *Ron E (Sep 08)*

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