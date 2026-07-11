---
title: Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers
url: https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:37.323452
---

# Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers](https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html)

**Swati Khandelwal**Jul 10, 2026Vulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQHphr7bXE4J4-EmYSWy0cjHarUBibR2JrXpFbwDKMZnsWbiUsC9UE7g3x2r8WFDLB7BBZlH2kDJ3I9QqF8IIGLPiZda93wKUaDqJC8Nv11yrd7VPm9RmBOky0yRXGRhhcDqbwNCZvHiGTkKRb06XAwFiGl0juzUeFBn3LUDwFfxZVNlInVmXTNI4cMLI/s1700-e365/XQUIC-demo.gif)

A single wrong variable on one line in XQUIC, Alibaba's QUIC and HTTP/3 library, lets any remote client crash the server with a short burst of completely legal traffic. There is no patch.

FoxIO researcher Sébastien Féry [disclosed the flaw on July 8](https://foxio.io/blog/xring-crashing-xquic-with-spec-compliant-qpack-instructions) and nicknamed it XRING. He says it needs no login and no malformed packets: about 260 bytes of ordinary QPACK traffic takes the server process down.

XQUIC is open-source, so the risk is not Alibaba's alone: any server that embeds it and serves HTTP/3 with the default QPACK settings is exposed. That includes Tengine, Alibaba's Nginx-based web server, which FoxIO says fronts the company's cloud and CDN on sites including Taobao and Alipay.

Every release through v1.9.4, the latest, is affected. There is no fixed release and no CVE as of July 10. Until a fix ships, operators can set SETTINGS\_QPACK\_MAX\_TABLE\_CAPACITY to 0, which turns off QPACK's dynamic table, or drop HTTP/3 support entirely.

The bug lives in how HTTP/3 compresses headers. To avoid sending the same header (say, user-agent) over and over, HTTP/3 uses QPACK. It keeps a shared table that the client directs the server to build up and resize through a dedicated control channel, the encoder stream.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

XQUIC stores that table's bytes in a [ring buffer](https://github.com/alibaba/xquic/blob/main/src/common/utils/ringmem/xqc_ring_mem.c), a fixed block of memory where data wraps from the end back to the start once it fills.

When the client asks to grow the table, XQUIC allocates a bigger buffer and copies the old data across. That copy has four cases, depending on whether the data wraps in the old buffer, the new one, both, or neither. In one of them, the code sizes the leftover tail data against the new, larger buffer's capacity instead of the old one's. It overcounts badly.

Grow a 64-byte table with the write cursor near the end, and resize to 65, and XQUIC decides there are 70 tail bytes to move when there are really 6.

That wrong number flows into a memory copy. The copy length comes from subtracting the overcount from a smaller value. Because that length is an unsigned size\_t, it underflows and wraps to a near-maximum number, and the copy runs off the end of memory.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixV1_6IK3fCzhiZyzdBFm-3_r_D-Iy8F9ekwLsUvYBiZuvrN_gOs6mexzZHBPD7Cor6lupMIYWI5fINt937kxfc0NLI1vNUZr50aX-LloAEsBD8DTiyFTnnIc5vEOtfkeKppX8CSuR8URBCuyK8oVYd7DcpJK9y5uj_TvZwF92noAOyChF3H3GiIXkHi0/s1700-e365/qpack.jpg)

In FoxIO's release build on Ubuntu 26.04, glibc's \_FORTIFY\_SOURCE=2 caught the bad length and killed the process. Without that check, the copy writes out of bounds, from the old buffer past the end of the new one. Féry showed a crash but did not test whether that corruption could be exploited further.

None of the values in the attack breaks QPACK's rules. XQUIC advertises a 16 KiB dynamic-table limit by default; the payload asks for 64 bytes, then 65. The client only has to drive the table into the exact wrapped layout that hits the faulty branch. FoxIO says the mistake has been in XQUIC since its first public release in January 2022, and a proof of concept is [public](https://github.com/FoxIO-LLC/xring-poc).

XRING is the latest in a string of remote crashes in HTTP/2 and HTTP/3 stacks. Three weeks earlier, THN reported a [use-after-free in NGINX's HTTP/3 module](https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html) (CVE-2026-42530) that a remote, unauthenticated client could reach through the same QPACK encoder stream XRING abuses, a different bug class on the same attack surface.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

In June, Calif's [HTTP/2 Bomb](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html) caused remote denial of service against Nginx, Apache, IIS, and Envoy by abusing HPACK, HTTP/2's header compression, and the predecessor to QPACK.

In February, HAProxy [patched two QUIC crashes](https://www.haproxy.com/blog/cves-2026-quic-denial-of-service), one an integer underflow during token validation, the same type of bug behind XRING, though it needed a malformed packet where XRING needs none. That difference is the point: legal input, one arithmetic slip, a dead server.

FoxIO demonstrated a crash, not code execution, and reported no exploitation in the wild. It says it emailed Alibaba on April 7 through the project's security policy, which promises a reply within three working days, then followed up four more times through May 9 without an answer before going public.

The Hacker News has asked Alibaba whether a fix and a CVE are coming, and whether FoxIO's five disclosure attempts reached its security team. It has asked FoxIO whether the flaw has been exploited in the wild and whether the underlying heap write can be pushed past a crash. The story will be updated with any response.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQ...