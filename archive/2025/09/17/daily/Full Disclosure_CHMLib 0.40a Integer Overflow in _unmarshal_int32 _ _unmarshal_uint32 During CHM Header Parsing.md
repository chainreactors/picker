---
title: CHMLib 0.40a Integer Overflow in _unmarshal_int32 / _unmarshal_uint32 During CHM Header Parsing
url: https://seclists.org/fulldisclosure/2025/Sep/47
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:59.433065
---

# CHMLib 0.40a Integer Overflow in _unmarshal_int32 / _unmarshal_uint32 During CHM Header Parsing

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

[![Previous](/images/left-icon-16x16.png)](46)
[By Date](date.html#47)
[![Next](/images/right-icon-16x16.png)](48)

[![Previous](/images/left-icon-16x16.png)](46)
[By Thread](index.html#47)
[![Next](/images/right-icon-16x16.png)](48)

![](/shared/images/nst-icons.svg#search)

# CHMLib 0.40a Integer Overflow in \_unmarshal\_int32 / \_unmarshal\_uint32 During CHM Header Parsing

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 13 Sep 2025 14:54:32 -0400

---

```
A vulnerability exists in CHMLib (latest release 0.40) when parsing
malformed CHM (Compiled HTML Help) files. The functions _unmarshal_int32
and _unmarshal_uint32 reconstruct 32-bit values using left shifts on signed
integers without proper type casting: *dest = (*pData)[0] | (*pData)[1]<<8
| (*pData)[2]<<16 | (*pData)[3]<<24; If an attacker supplies crafted input
such that the most significant byte is 0xFF, this triggers a left shift of
255 by 24 bits on a signed int, which is undefined behavior in C. This
results in integer overflow, leading to corrupted metadata when parsing
ITSF/ITSP headers. The malformed values propagate into downstream logic,
causing incorrect length calculations, crashes, or memory mismanagement.

*Impact*

   - Application crashes when parsing malicious CHM files.
   - Invalid integer values may cause logic errors in decompression.
   - While primarily a stability issue, corrupted values may form the basis
   for further memory safety violations (depending on allocator state and
   calling context). Applications embedding CHMLib (e.g., KDEâ€™s KChmViewer,
   GNOME CHM viewers, xchm, and other tools) are affected.

*Proof of Concept:*

ASAN_OPTIONS=abort_on_error=1,allocator_may_return_null=0,detect_leaks=0 \

UBSAN_OPTIONS=print_stacktrace=1 \

./chmextract /root/CHMLib/malformed_pmgl.chm /tmp/out_malformed

*Output:*

chm_lib.c:272:73: runtime error: left shift of 255 by 24 places cannot be
represented in type 'int'

    #0 0xaaaae8f17b00 in _unmarshal_uint32 /root/CHMLib/src/chm_lib.c:272:73

    #1 0xaaaae8f02104 in _unmarshal_itsp_header
/root/CHMLib/src/chm_lib.c:458:5

    #2 0xaaaae8f02104 in chm_open /root/CHMLib/src/chm_lib.c:843:10

    #3 0xaaaae8f00a7c in main /root/CHMLib/src/extract_chmLib.c:184:9

    #4 0xffff947f2290 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16

    #5 0xffff947f2374 in __libc_start_main csu/../csu/libc-start.c:360:3

    #6 0xaaaae8e205ac in _start (/root/CHMLib/src/chmextract+0x405ac)
(BuildId: c3376fd09cabf1b5e4901002039ac179cafe58ec)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](46)
[By Date](date.html#47)
[![Next](/images/right-icon-16x16.png)](48)

[![Previous](/images/left-icon-16x16.png)](46)
[By Thread](index.html#47)
[![Next](/images/right-icon-16x16.png)](48)

### Current thread:

* **CHMLib 0.40a Integer Overflow in \_unmarshal\_int32 / \_unmarshal\_uint32 During CHM Header Parsing** *Ron E (Sep 15)*

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