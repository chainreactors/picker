---
title: libwmf v0.2.13 Integer Overflow in libwmf Left-Shift Operations (wmf.c, fig.c, svg.c)
url: https://seclists.org/fulldisclosure/2025/Sep/48
source: Full Disclosure
date: 2025-09-17
fetch_date: 2025-10-02T20:16:58.129564
---

# libwmf v0.2.13 Integer Overflow in libwmf Left-Shift Operations (wmf.c, fig.c, svg.c)

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

# libwmf v0.2.13 Integer Overflow in libwmf Left-Shift Operations (wmf.c, fig.c, svg.c)

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 13 Sep 2025 14:59:58 -0400

---

```
libwmf is vulnerable to an integer overflow / undefined behavior condition
in multiple code paths. The affected source files (wmf.c, fig.c, svg.c) use
left-shift operations on signed integers that shift into the sign bit
(e.g., 1 << 31). According to the C standard, shifting a signed integer
into the sign bit is undefined behavior and may lead to incorrect values or
unexpected execution paths. When a crafted WMF file is processed with tools
such as wmf2fig or wmf2svg, the integer overflow is triggered during API
initialization (wmf_api_create) and rendering setup (wmf_fig_function,
wmf_svg_function). Depending on compiler optimizations and platform, this
can result in miscalculated flags, denial of service, or other
unpredictable behavior.

*Impact:*

   - Application aborts due to invalid state.
   - Miscomputed flags could lead to corrupted rendering or bypassing
   internal safety checks.
   - While no controlled memory corruption was observed, compilers may
   optimize UB in dangerous ways.

*Proof of Concept:*

ASAN_OPTIONS=abort_on_error=1,allocator_may_return_null=0,detect_leaks=0
UBSAN_OPTIONS=print_stacktrace=1 ./src/convert/wmf2fig AAAAAA....AAAA.wmf

*Output:*

wmf.c:110:11: runtime error: left shift of 1 by 31 places cannot be
represented in type 'int'

    #0 0xaaaac5564d74 in wmf_api_create /root/libwmf/src/wmf.c:110:11

    #1 0xaaaac554c874 in wmf2fig_draw
/root/libwmf/src/convert/wmf2fig.c:118:8

    #2 0xaaaac555b4a0 in wmf2fig_file
/root/libwmf/src/convert/wmf2fig.c:479:11

    #3 0xaaaac555bd3c in main /root/libwmf/src/convert/wmf2fig.c:498:33

    #4 0xffff9afc2290 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16

    #5 0xffff9afc2374 in __libc_start_main csu/../csu/libc-start.c:360:3

    #6 0xaaaac546d2ac in _start (/root/libwmf/src/convert/wmf2fig+0xdd2ac)
(BuildId: a39ad033766fcd9a1723b20e5eb94936b2d83e67)
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

* **libwmf v0.2.13 Integer Overflow in libwmf Left-Shift Operations (wmf.c, fig.c, svg.c)** *Ron E (Sep 15)*

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