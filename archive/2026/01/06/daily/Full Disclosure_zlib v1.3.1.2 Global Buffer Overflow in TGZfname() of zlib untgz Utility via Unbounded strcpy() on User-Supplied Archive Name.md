---
title: zlib v1.3.1.2 Global Buffer Overflow in TGZfname() of zlib untgz Utility via Unbounded strcpy() on User-Supplied Archive Name
url: https://seclists.org/fulldisclosure/2026/Jan/3
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:41.987851
---

# zlib v1.3.1.2 Global Buffer Overflow in TGZfname() of zlib untgz Utility via Unbounded strcpy() on User-Supplied Archive Name

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# zlib v1.3.1.2 Global Buffer Overflow in TGZfname() of zlib untgz Utility via Unbounded strcpy() on User-Supplied Archive Name

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Mon, 29 Dec 2025 22:43:46 -0500

---

```
A global buffer overflow vulnerability exists in the TGZfname() function of
the zlib untgz utility due to the use of an unbounded strcpy() call on
attacker-controlled input. The utility copies a user-supplied archive name
(argv[arg]) into a fixed-size static global buffer of 1024 bytes without
performing any length validation. Supplying an archive name longer than
1024 bytes results in an out-of-bounds write past the end of the global
buffer, leading to memory corruption.
The vulnerable code is reached prior to any archive parsing or validation,
making the flaw trivially reachable through command-line input alone.

*Root Cause*
* arcname is derived directly from argv[]
* No bounds checking is performed before copying into buffer
* buffer is a global static array, not stack-allocated
* Overflow occurs immediately on function entry

*Impact*
An attacker can trigger a global buffer overflow by invoking untgz with a
sufficiently long filename argument.
Potential impacts include:
* Denial of Service (crash)
* Memory corruption of adjacent global objects
* Undefined behavior
* Potential code execution depending on:
    * compiler
    * architecture
    * build flags
    * memory layout
Because the overflow affects global memory, corruption may persist beyond
the scope of the function and influence later program behavior.

*Evidence:*
./untgz_asan $(python3 - <<'EOF'
print("A" * 4096)
EOF)

*ASAN Output:*
=================================================================
==3141495==ERROR: AddressSanitizer: global-buffer-overflow on address
0xaaaab54d8ec0 at pc 0xaaaab4a91bec bp 0xfffffd1e5150 sp 0xfffffd1e4940
WRITE of size 2001 at 0xaaaab54d8ec0 thread T0
    #0 0xaaaab4a91be8 in strcpy
(/root/zlib/contrib/untgz/untgz_asan+0xc1be8) (BuildId:
31ab7d499b8ab40a93265dad8bfb879e63c604ab)
    #1 0xaaaab4aee508 in TGZfname /root/zlib/contrib/untgz/untgz.c:136:3
    #2 0xaaaab4af2fec in main /root/zlib/contrib/untgz/untgz.c:638:20
    #3 0xffffbaa52598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #4 0xffffbaa52678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #5 0xaaaab4a079ac in _start
(/root/zlib/contrib/untgz/untgz_asan+0x379ac) (BuildId:
31ab7d499b8ab40a93265dad8bfb879e63c604ab)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **zlib v1.3.1.2 Global Buffer Overflow in TGZfname() of zlib untgz Utility via Unbounded strcpy() on User-Supplied Archive Name** *Ron E (Jan 05)*

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