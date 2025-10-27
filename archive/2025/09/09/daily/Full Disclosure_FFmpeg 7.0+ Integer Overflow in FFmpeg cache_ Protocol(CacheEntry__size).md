---
title: FFmpeg 7.0+ Integer Overflow in FFmpeg cache: Protocol	(CacheEntry::size)
url: https://seclists.org/fulldisclosure/2025/Sep/32
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:52:56.660584
---

# FFmpeg 7.0+ Integer Overflow in FFmpeg cache: Protocol	(CacheEntry::size)

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

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

![](/shared/images/nst-icons.svg#search)

# FFmpeg 7.0+ Integer Overflow in FFmpeg cache: Protocol (CacheEntry::size)

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 7 Sep 2025 03:39:25 -0400

---

```
An integer overflow vulnerability exists in the FFmpeg cache: URL protocol
implementation. The CacheEntry structure uses a 32-bit signed integer to
store cache entry sizes (int size), but the cache layer can accumulate
cached data exceeding 2 GB. Once entry->size grows beyond INT_MAX and new
data is appended, an overflow occurs. This results in corrupted cache
metadata and can lead to logic errors, incorrect data reads, and possible
out-of-bounds access depending on downstream use. (FFmpeg 7.0-8.0)

*Impact:*

   -
   -

   Player/processing pipeline collapses with repeated write failures.
   -

   Reads/writes misaligned → corrupted output or playback.

   -

   If corrupted entry->size propagates, it can trick boundary checks
(in_block_pos
   < entry->size) into allowing invalid reads. That’s a potential
   memory-safety issue in downstream cache logic.

*Proof of Concept:*
ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 150000 big_valid.wav
ASAN_OPTIONS=abort_on_error=1 \
UBSAN_OPTIONS=print_stacktrace=1 \
./ffmpeg -read_ahead_limit -1 -i "cache:big_valid.wav" -f null -

*Output:*libavformat/cache.c:151:21: runtime error: signed integer overflow:
2147450958 + 32768 cannot be represented in type 'int'
[cache @ 0x50d000000040] write in cache failedXXx
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

### Current thread:

* **FFmpeg 7.0+ Integer Overflow in FFmpeg cache: Protocol (CacheEntry::size)** *Ron E (Sep 08)*

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