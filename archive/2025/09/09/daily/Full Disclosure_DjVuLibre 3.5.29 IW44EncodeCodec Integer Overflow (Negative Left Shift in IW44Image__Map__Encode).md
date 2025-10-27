---
title: DjVuLibre 3.5.29 IW44EncodeCodec Integer Overflow (Negative Left Shift in IW44Image::Map::Encode)
url: https://seclists.org/fulldisclosure/2025/Sep/23
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:53:07.395900
---

# DjVuLibre 3.5.29 IW44EncodeCodec Integer Overflow (Negative Left Shift in IW44Image::Map::Encode)

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

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

![](/shared/images/nst-icons.svg#search)

# DjVuLibre 3.5.29 IW44EncodeCodec Integer Overflow (Negative Left Shift in IW44Image::Map::Encode)

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 6 Sep 2025 03:29:38 -0400

---

```
The DjVuLibre document compression library (tested version 3.5.29) is
vulnerable to an integer overflow caused by a left shift of a negative
signed integer in the IW44EncodeCodec.cpp component. When processing
crafted PPM input passed through the c44 utility, negative pixel values are
left-shifted in functions such as filter_fh, filter_fv, and
IW44Image::Map::Encode::create. This results in undefined behavior and
corrupted intermediate state during encoding. An attacker can trigger the
condition by supplying specially crafted image data, potentially leading to
memory corruption, application crash*, *or information disclosure depending
on compiler optimizations and runtime environment.

*Impact:*

   - Crash (DoS) confirmed with UBSan/ASan.
   - Possible memory corruption due to undefined behavior on signed shifts

*Proof of Concept:*

convert -size 500x500 gradient: bad.ppm

ASAN_OPTIONS=detect_leaks=0,abort_on_error=1 \

UBSAN_OPTIONS=print_stacktrace=1 \

./tools/c44 bad.ppm out.djvu

*Sanitizer Output:*

IW44EncodeCodec.cpp:936:30: runtime error: left shift of negative value -128

SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior
IW44EncodeCodec.cpp:936:30
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](22)
[By Date](date.html#23)
[![Next](/images/right-icon-16x16.png)](24)

[![Previous](/images/left-icon-16x16.png)](22)
[By Thread](index.html#23)
[![Next](/images/right-icon-16x16.png)](24)

### Current thread:

* **DjVuLibre 3.5.29 IW44EncodeCodec Integer Overflow (Negative Left Shift in IW44Image::Map::Encode)** *Ron E (Sep 08)*

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