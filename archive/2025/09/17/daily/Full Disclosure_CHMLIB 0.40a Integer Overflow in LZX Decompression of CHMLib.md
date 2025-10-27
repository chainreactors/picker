---
title: CHMLIB 0.40a Integer Overflow in LZX Decompression of CHMLib
url: https://seclists.org/fulldisclosure/2025/Sep/46
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:17:00.725934
---

# CHMLIB 0.40a Integer Overflow in LZX Decompression of CHMLib

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

[![Previous](/images/left-icon-16x16.png)](45)
[By Date](date.html#46)
[![Next](/images/right-icon-16x16.png)](47)

[![Previous](/images/left-icon-16x16.png)](45)
[By Thread](index.html#46)
[![Next](/images/right-icon-16x16.png)](47)

![](/shared/images/nst-icons.svg#search)

# CHMLIB 0.40a Integer Overflow in LZX Decompression of CHMLib

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 13 Sep 2025 14:47:27 -0400

---

```
An integer overflow vulnerability exists in the LZX decompression routines
of CHMLib (tested in version 0.40, latest release as of 2025). The issue
occurs within lzx.c during bitstream parsing (lzx_read_lens and
LZXdecompress), where crafted CHM files can supply values that cause
left-shift operations to exceed the representable range of 32-bit signed
integers. When processing malformed compressed blocks, operations such as:
leaf = pos >> 16; table[(next_symbol << 1)] = 0; bitbuf |=
((inpos[1]<<8)|inpos[0]) << (ULONG_BITS-16 - bitsleft); perform shifts on
large values (value << 16), triggering undefined behavior. This corrupts
the Huffman decode tables and decompression state.

*Impact:*

   - Crafted CHM files can crash applications using CHMLib by causing
   failures or illegal memory operations during decompression.
   - Although direct heap overflows were not observed in this testing, the
   corrupted decompression state (match_length, match_offset) could under
   certain inputs lead to out-of-bounds reads or writes.

*Proof of Concept:*

ASAN_OPTIONS=abort_on_error=1,allocator_may_return_null=0,detect_leaks=0 \

UBSAN_OPTIONS=print_stacktrace=1 \

./chmextract crafted_overflow_lzx.chm /tmp/out

*Observed errors:*

lzx.c:663:37: runtime error: left shift of 39074 by 16 places cannot be
represented in type 'int'

lzx.c:569:25: runtime error: left shift of 53200 by 16 places cannot be
represented in type 'int'

lzx.c:440:9: runtime error: left shift of 63471 by 16 places cannot be
represented in type 'int'
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](45)
[By Date](date.html#46)
[![Next](/images/right-icon-16x16.png)](47)

[![Previous](/images/left-icon-16x16.png)](45)
[By Thread](index.html#46)
[![Next](/images/right-icon-16x16.png)](47)

### Current thread:

* **CHMLIB 0.40a Integer Overflow in LZX Decompression of CHMLib** *Ron E (Sep 15)*

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