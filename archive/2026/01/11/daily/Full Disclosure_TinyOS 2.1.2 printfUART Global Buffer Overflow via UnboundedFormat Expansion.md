---
title: TinyOS 2.1.2 printfUART Global Buffer Overflow via Unbounded	Format Expansion
url: https://seclists.org/fulldisclosure/2026/Jan/13
source: Full Disclosure
date: 2026-01-11
fetch_date: 2026-01-12T03:37:54.840127
---

# TinyOS 2.1.2 printfUART Global Buffer Overflow via Unbounded	Format Expansion

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

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

![](/shared/images/nst-icons.svg#search)

# TinyOS 2.1.2 printfUART Global Buffer Overflow via Unbounded Format Expansion

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Thu, 8 Jan 2026 10:17:43 -0500

---

```
A global buffer overflow vulnerability exists in the TinyOS printfUART
implementation used within the ZigBee / IEEE 802.15.4 networking stack. The
issue arises from an unsafe custom sprintf() routine that performs
unbounded string concatenation using strcat() into a fixed-size global
buffer. The global buffer debugbuf, defined with a size of 256 bytes, is
used as the destination for formatted output. When a %s format specifier is
supplied with a string longer than the available buffer space, the
implementation appends the string without any bounds checking, resulting in
a write beyond the end of the global buffer. This condition allows memory
corruption and can lead to denial-of-service, unintended behavior, or
information disclosure. The vulnerability is deterministic and independent
of the hardware platform.

*Root Cause:*

The vulnerability occurs in the following code path:
#define DEBUGBUF_SIZE 256
char debugbuf[DEBUGBUF_SIZE];

case 's':
    ptr = va_arg(ap, char *);
    strcat(buf, ptr);   // no bounds checking

The printfUART() macro ultimately calls the custom sprintf() implementation
with debugbuf as the destination buffer. The use of strcat() without
validating the remaining capacity of debugbuf allows attacker-controlled
strings passed via %s to overflow the buffer.

*Impact:*

   - Global memory corruption
   - Denial of service (device crash)
   - Information disclosure via UART output
   - Undefined behavior affecting adjacent global state or interrupt-driven
   execution

On typical TinyOS deployments (AVR / MSP430):

   - No memory protection
   - No stack canaries
   - No ASLR

This significantly increases the severity of memory corruption.

*Proof of Concept:*

The issue was validated using AddressSanitizer, which reported a
global-buffer-overflow during execution:

./printUART

*Output:*
=================================================================
==492203==ERROR: AddressSanitizer: global-buffer-overflow on address
0xaaaaea1774a0 at pc 0xaaaae972eee4 bp 0xfffff642d3a0 sp 0xfffff642cb90
WRITE of size 1024 at 0xaaaaea1774a0 thread T0
    #0 0xaaaae972eee0 in strcat (/root/tinyos-main/printfuart+0xbeee0)
(BuildId: b934c9b9563afd45c9ae2cf4ccdfab5bf9a33826)
    #1 0xaaaae978d024 in sprintf
/tinyos-main/tos/lib/net/zigbee/ieee802154/includes/printfUART.h:266:13
    #2 0xaaaae978e1b8 in main /root/tinyos-main/printfuart.c:47:5
    #3 0xffffac4a2598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #4 0xffffac4a2678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #5 0xaaaae96a592c in _start (/root/tinyos-main/printfuart+0x3592c)
(BuildId: b934c9b9563afd45c9ae2cf4ccdfab5bf9a33826)

0xaaaaea1774a0 is located 0 bytes after global variable 'debugbuf' defined
in '/tinyos-main/tos/lib/net/zigbee/ieee802154/includes/printfUART.h:81'
(0xaaaaea1773a0) of size 256
SUMMARY: AddressSanitizer: global-buffer-overflow
(/root/tinyos-main/printfuart+0xbeee0) (BuildId:
b934c9b9563afd45c9ae2cf4ccdfab5bf9a33826) in strcat
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](12)
[By Date](date.html#13)
[![Next](/images/right-icon-16x16.png)](14)

[![Previous](/images/left-icon-16x16.png)](12)
[By Thread](index.html#13)
[![Next](/images/right-icon-16x16.png)](14)

### Current thread:

* **TinyOS 2.1.2 printfUART Global Buffer Overflow via Unbounded Format Expansion** *Ron E (Jan 10)*

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