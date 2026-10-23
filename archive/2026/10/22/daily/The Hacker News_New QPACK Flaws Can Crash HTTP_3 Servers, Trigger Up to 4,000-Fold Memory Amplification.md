---
title: New QPACK Flaws Can Crash HTTP/3 Servers, Trigger Up to 4,000-Fold Memory Amplification
url: https://thehackernews.com/2026/10/new-qpack-flaws-can-crash-http3-servers.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:44.090801
---

# New QPACK Flaws Can Crash HTTP/3 Servers, Trigger Up to 4,000-Fold Memory Amplification

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [New QPACK Flaws Can Crash HTTP/3 Servers, Trigger Up to 4,000-Fold Memory Amplification](https://thehackernews.com/2026/10/new-qpack-flaws-can-crash-http3-servers.html)

**Swati Khandelwal**Oct 22, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidksxeLP_h5vpqmr62J_72yOAmQIRsZDLE6bpclFaHY1yQX6Dv-omiTvu_j49FuvXUOwxQT8levg89_AGRMiPNidANkEn1PSGSaNFoCVnY_VQ2Ny9D7FhLwtd9VDboOjxPi6Ssg78CdLFUzShhEt8oK6x0obKcHCZbbIMWBylnQCVCbQGUqjfbBJAKCew/s1700-nu-rw-lo-l85-e365/http3.jpg)

A remote attacker who has not logged in can crash many HTTP/3 web servers with a single connection, security firm FoxIO [disclosed](https://foxio.io/blog/header-accordions-qpack-amplification-attacks-against-http-3-servers), releasing working proof-of-concept code.

By sending a small batch of compressed HTTP headers that expands in memory to a much larger set, the attacker can force the server to use thousands of times more memory than it received, enough to run a default server out of memory.

The flaws cause only denial-of-service attacks, with no evidence of data theft or code execution and no public reports of attacks in the wild. Fixes are out for quic-go, Cloudflare quiche, lsquic and Wireshark, but Bun, the h3 Rust library and aioquic were still unpatched at disclosure.

FoxIO found the same class of flaw in seven of ten HTTP/3 stacks it tested. The common cause is in QPACK, the scheme HTTP/3 uses to compress request headers so repeated fields travel as a short code instead of the full text.

A server is supposed to cap the size of the headers after it unpacks them. The affected stacks cap the compressed batch that arrives on the wire, but not the unpacked result, or they apply the cap too late, so a single request can expand into hundreds of thousands of header entries that the server holds in memory.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The reach is wide because these stacks sit under common software. quic-go is the Go library behind Caddy, Traefik and cloudflared; lsquic is LiteSpeed's library, used in LiteSpeed Web Server and OpenLiteSpeed; and Bun's HTTP/3 server runs on lsquic.

The attacker needs no account or special access, and since HTTP/3 runs over UDP, the request reaches the server before much of the usual filtering applies.

Which stacks are fixed and which are still exposed, as of October 22, 2026:

| Stack | Status | Fixed version | Identifier |
| --- | --- | --- | --- |
| quic-go | Fixed | 0.57.0 | [CVE-2025-64702](https://github.com/quic-go/quic-go/security/advisories/GHSA-g754-hx8w-x2g6) |
| Cloudflare quiche | Fixed | 0.29.3 | [CVE-2026-12523](https://github.com/cloudflare/quiche/security/advisories/GHSA-4fgf-9xrr-88gf) |
| lsquic | Fixed | 4.9.0 | no CVE |
| Wireshark | Fixed | 4.6.2 / 4.4.12 | [CVE-2025-13945](https://www.wireshark.org/security/wnpa-sec-2025-07.html) |
| Bun | Unpatched | — | no CVE |
| h3 (hyperium) | Unpatched | — | no CVE |
| aioquic / mitmproxy | Unpatched | — | no CVE |

FoxIO lists IIS, Envoy, ngtcp2/nghttp3, and Google's quiche as not affected, each because it caps the unpacked headers while decoding rather than after.

The amplification varies by stack, in FoxIO's own tests against default settings. On quic-go, a 1 MB compressed batch unpacked into about 160,000 header fields and left roughly 15 MB held in the request, about 17 times the bytes sent; quic-go's own advisory puts the possible expansion at around 50 times.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLtdobSM9_4CXj9ccjvTJLTPECd0riq7WjDzrE_2gLFW_XsawO-SNEaAICxo2CI7Ae03sUT59om0mnLtoGf0r7XUtDAaHqYEz0ZWkPDe5W6XCAS7a9AXrBmXVj0zfqiF65Wt3tj0eNYb0NGfVn_g_adXyFoY47S04feyyVTq5nzpk26QR8sSKvCL5glCw/s1700-nu-rw-lo-l85-e365/demo.gif)

A second method drives the ratio much higher: the attacker stores one roughly 4 KB header entry, then points at it thousands of times using one-byte references, and the server rebuilds the full entry on each reference. FoxIO measured about 4,000 times on Bun and between 600 and 1,800 times on lsquic.

Bun carries a worst-case. Its HTTP/3 server, which Bun's documentation [calls experimental](https://bun.sh/docs/runtime/http), uses lsquic but replaces the part that caps header memory with its own code, which checks each header but never the running total. FoxIO found that once the unpacked headers pass 2 GB, a size counter in that code overflows to zero and the server enters a loop it never leaves.

A single stream carrying about 516 KB on the wire, FoxIO reported, leaves the server stuck at 100 percent CPU with no recovery, blocking new requests. The missing running total is what lets the overflow be reached; lsquic's own 64 KB cap prevents it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Wireshark is a different case from the server flaws. Its issue crashes the HTTP/3 dissector, the part that reads HTTP/3 out of a capture, when Wireshark decrypts traffic using a key-log file or opens a capture file that holds decryption secrets. It is not a server an attacker reaches over the network. Wireshark [said](https://www.wireshark.org/security/wnpa-sec-2025-07.html) it is "unaware of any exploits for this issue."

Operators should upgrade to the fixed releases above. For the stacks with no fix, FoxIO gives interim steps: on Bun, do not expose an HTTP/3 server; on mitmproxy, turn off HTTP/3 by passing --set http3=false; and for the h3 Rust library, set a sensible limit with max\_field\_section\_size.

The [lsquic fix](https://github.com/litespeedtech/lsquic/releases), released July 16, 2026, caps how many unpacked header sets a server holds per stream, defaulting to one. FoxIO said the work began after Gal Bar Nahum's research into ["MadeYouReset," a denial-of-service technique against HTTP/2](https://thehackernews.com/2025/08/new-http2-madeyoureset-vulnerability.html), whic...