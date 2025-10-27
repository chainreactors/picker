---
title: FFmpeg 7.0+ Integer Overflow in UDP Protocol Handler	(fifo_size option)
url: https://seclists.org/fulldisclosure/2025/Sep/30
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:52:58.863119
---

# FFmpeg 7.0+ Integer Overflow in UDP Protocol Handler	(fifo_size option)

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

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

![](/shared/images/nst-icons.svg#search)

# FFmpeg 7.0+ Integer Overflow in UDP Protocol Handler (fifo\_size option)

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 7 Sep 2025 02:43:02 -0400

---

```
A signed integer overflow exists in FFmpegâ€™s udp.c implementation when
parsing the fifo_size option from a user-supplied UDP URL. The overflow
occurs during multiplication, which is used to compute the size of the
circular receive buffer. This can result in undefined behavior, allocation
failures, or potentially memory corruption depending on compiler
optimizations and downstream usage. (FFmpeg 7.0-8.0))
*Impact:*

   -

   Denial of Service (allocation failure, runtime crash).
   -

   Heap buffer overflow if the wrapped value allocates a smaller buffer
   than required but is later written into with the intended (larger) size.
   -

   Severity depends on compiler behavior and downstream allocations.

*Proof of Concept:*./ffmpeg -i udp://127.0.0.1:1234?fifo_size=2147483647 -f
null -

*Output:*libavformat/udp.c:760:29: runtime error: signed integer overflow:
2147483647 * 188 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior
libavformat/udp.c:760:29
[in#0 @ 0x512000000040] Error opening input: Cannot allocate memory
Error opening input file udp://127.0.0.1:1234?fifo_size=2147483647.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](29)
[By Date](date.html#30)
[![Next](/images/right-icon-16x16.png)](31)

[![Previous](/images/left-icon-16x16.png)](29)
[By Thread](index.html#30)
[![Next](/images/right-icon-16x16.png)](31)

### Current thread:

* **FFmpeg 7.0+ Integer Overflow in UDP Protocol Handler (fifo\_size option)** *Ron E (Sep 08)*

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