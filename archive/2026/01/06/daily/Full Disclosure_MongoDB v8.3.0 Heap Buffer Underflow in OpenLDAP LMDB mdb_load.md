---
title: MongoDB v8.3.0 Heap Buffer Underflow in OpenLDAP LMDB mdb_load
url: https://seclists.org/fulldisclosure/2026/Jan/5
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:41.720251
---

# MongoDB v8.3.0 Heap Buffer Underflow in OpenLDAP LMDB mdb_load

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# MongoDB v8.3.0 Heap Buffer Underflow in OpenLDAP LMDB mdb\_load

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Mon, 29 Dec 2025 22:51:57 -0500

---

```
A heap buffer underflow vulnerability exists in the readline() function of
OpenLDAP's Lightning Memory-Mapped Database (LMDB) mdb_load utility. The
vulnerability is triggered through malformed input data and results in an
out-of-bounds read one byte before an allocated heap buffer. This can lead
to information disclosure through heap memory leakage.

*Root Cause:*
The vulnerability occurs in the readline() function at line 214 of
mdb_load.c. The ASAN output reveals two critical issues:
1. *Integer Underflow:* An unsigned offset addition to 0x521000000100
results in underflow to 0x5210000000ff, indicating a pointer decrement
operation that wraps below the buffer start
2. *Out-of-bounds Read: *The subsequent memory access reads 1 byte at
address 0x5210000000ff, which is located 1 byte before the 4096-byte heap
region [0x521000000100, 0x521000001100)

*Impact:*
The vulnerability allows a local attacker to trigger a heap out-of-bounds
read in mdb_load, resulting in reliable denial of service and limited
information disclosure of adjacent heap memory. While no write primitive is
present, the disclosure may expose heap metadata and contribute to exploit
mitigation bypass in multi-stage attacks.

*Evidence:*
# Execute with crash input
./mdb_load -T /tmp/lmdb_asan < [crash_input_file]

*Output:*
mdb_load.c:214:9: runtime error: addition of unsigned offset to
0x521000000100 overflowed to 0x5210000000ff
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior mdb_load.c:214:9
=================================================================
==1215390==ERROR: AddressSanitizer: heap-buffer-overflow on address
0x5210000000ff at pc 0xaaaacb6f5bf4 bp 0xffffc2d17d30 sp 0xffffc2d17d28
READ of size 1 at 0x5210000000ff thread T0
    #0 0xaaaacb6f5bf0 in readline
/root/wiredtiger/third_party/openldap_liblmdb/mdb_load.c:214:9
    #1 0xaaaacb6ed614 in main
/root/wiredtiger/third_party/openldap_liblmdb/mdb_load.c:429:9
    #2 0xffffb4662598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #3 0xffffb4662678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #4 0xaaaacb60adec in _start
(/root/wiredtiger/third_party/openldap_liblmdb/mdb_load+0xcadec) (BuildId:
54fcbfcdc4f5509b87b342e8f33cab2ab3e6d444)

0x5210000000ff is located 1 bytes before 4096-byte region
[0x521000000100,0x521000001100)
allocated by thread T0 here:
    #0 0xaaaacb6ad4e4 in malloc
(/root/wiredtiger/third_party/openldap_liblmdb/mdb_load+0x16d4e4) (BuildId:
54fcbfcdc4f5509b87b342e8f33cab2ab3e6d444)
    #1 0xaaaacb6ed068 in main
/root/wiredtiger/third_party/openldap_liblmdb/mdb_load.c:354:17
    #2 0xffffb4662598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #3 0xffffb4662678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #4 0xaaaacb60adec in _start
(/root/wiredtiger/third_party/openldap_liblmdb/mdb_load+0xcadec) (BuildId:
54fcbfcdc4f5509b87b342e8f33cab2ab3e6d444)

SUMMARY: AddressSanitizer: heap-buffer-overflow
/root/wiredtiger/third_party/openldap_liblmdb/mdb_load.c:214:9 in readline
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **MongoDB v8.3.0 Heap Buffer Underflow in OpenLDAP LMDB mdb\_load** *Ron E (Jan 05)*

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