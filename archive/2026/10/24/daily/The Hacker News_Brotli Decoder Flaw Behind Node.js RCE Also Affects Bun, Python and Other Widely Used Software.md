---
title: Brotli Decoder Flaw Behind Node.js RCE Also Affects Bun, Python and Other Widely Used Software
url: https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html
source: The Hacker News
date: 2026-10-24
fetch_date: 2026-10-25T07:10:52.597561
---

# Brotli Decoder Flaw Behind Node.js RCE Also Affects Bun, Python and Other Widely Used Software

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

# [Brotli Decoder Flaw Behind Node.js RCE Also Affects Bun, Python and Other Widely Used Software](https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html)

**Swati Khandelwal**Oct 24, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxIIerJT3LOMCGn3nXAnmhaHzJlJnVJCso1COluq8t3WuF4IpNARa_Asl5nEhRUDTEcR89kwzo5vGmP5IyNbj1ncdaCpkhqcHUODHAd3khanaE-7N8Vb0NyEJkmPmNkhSpJtLCLgi9srDRhZLtM5n8UDI58F797ZJaVzC7JzjPLfca4NpxZr_7tCX8RIk/s1700-nu-rw-lo-l85-e365/br-nodejs.jpg)

A memory-corruption flaw in Google's Brotli decoder sits in many programs that unpack Brotli-compressed data, among them Bun, the Python Brotli and brotlicffi packages, and Envoy proxies set up to decompress Brotli.

Tracked as **CVE-2026-111497**, the flaw allows crafted compressed data to overwrite past the end of a buffer and corrupt a program's memory, potentially causing a crash, a memory leak, or the execution of attacker-controlled code.

Imperva researchers have shown that [code can run on one unpatched Node.js build](https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html). The same has not been demonstrated on the other software, and no real-world attacks have been reported.

The flaw was [first disclosed on October 21](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html), when Node.js and Google shipped fixes, and more have followed product by product since. Because the bug is in Google's decoder and each program ships its own copy of it, every one has to update that copy on its own.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

Brotli is a compression format from Google, used across the web to shrink pages and other traffic. The bug is in the C code that unpacks a Brotli stream, so it travels into anything that reuses that code, from language runtimes to proxies to Python packages.

### Which Software Is Affected

| Product | Affected | Fixed in | Exposed when |
| --- | --- | --- | --- |
| [Google Brotli (C library)](https://github.com/google/brotli/releases) | 1.0.3 to 1.2.0 | 1.0.10, 1.1.1, 1.2.1 | code decodes untrusted Brotli |
| [Node.js](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) | 22.x, 24.x, 26.x before the fix; 20.x and older (end of life) | 22.23.4, 24.22.1, 26.12.1 | `fetch()` of a `br` response, or Express or body-parser `br` bodies |
| [Bun](https://github.com/oven-sh/bun/releases/tag/bun-v1.4.4) | 1.4.3 and earlier | 1.4.4 | `fetch()` of a `br` response, or `node:zlib` |
| [Envoy](https://github.com/envoyproxy/envoy/security/advisories/GHSA-3wvj-j6qm-62mr) | 1.39.2, 1.38.5, 1.37.7, 1.36.11 | 1.40.0, 1.39.3, 1.38.6, 1.37.8, 1.36.12 | only if the Brotli decompressor is configured |
| [Istio](https://istio.io/latest/news/security/istio-security-2026-007/) | 1.31.0 to 1.31.1, 1.30.0 to 1.30.5, 1.29.0 to 1.29.8 | 1.31.2, 1.30.6, 1.29.9 | only if Brotli decompression is enabled |
| [Python `Brotli`](https://github.com/pypa/advisory-database/blob/main/vulns/brotli/PYSEC-2026-4322.yaml) | 1.2.0 and earlier | 1.2.1 | installed, and an HTTP client decodes `br` |
| [Python `brotlicffi`](https://github.com/pypa/advisory-database/blob/main/vulns/brotlicffi/PYSEC-2026-4323.yaml) | 1.2.0.x and earlier | 1.2.1.0 | installed, and an HTTP client decodes `br` |
| [cdxgen](https://github.com/cdxgen/cdxgen/security/advisories/GHSA-5266-jm88-3grm) | standalone binaries and images, 13.4.0 and 12.8.8 and earlier | 13.5.0, 12.8.9 | standalone binary or image scanning untrusted input |

A program is exposed only if it decodes Brotli data that someone else controls. For Node.js and Bun, that happens when the built-in fetch() reads a response sent with Content-Encoding: br, or when request-body code such as Express 5 and body-parser 2 unpacks a Brotli upload. A plain Node.js HTTP server does not decode request bodies on its own.

Envoy and Istio are affected only when Brotli decompression is enabled, for example, through an Envoy filter. Where it is off, the flaw cannot be reached.

In Python, the risk comes from the Brotli or brotlicffi package being installed at all. Once either is present, HTTP clients such as requests, urllib3, httpx, and aiohttp decode Brotli responses on their own, so an application can be exposed without ever importing Brotli in its own code.

A web application firewall helps only so far. Vercel, which [added firewall rules](https://vercel.com/kb/bulletin/node-js-security-advisory) on the day of disclosure, said those rules do not cover "responses your functions fetch from other servers." For that path, only updating the runtime or library closes the hole.

How far the flaw can be pushed depends on the software. Imperva's Red Team, which calls its work Node2Shell, ran attacker-supplied code on an unmodified Node.js 24.22.0 build for Linux on ARM64, delivering it both as a fetched response and as an Express request body. The exploit took several tries, has not been released, and was not tested on other builds.

OpenAI, whose Codex Security team reported the flaw, describes it as enabling unauthenticated remote code execution in Brotli and lists Node.js, Bun, and Envoy as affected software. In its account, the flaw works both ways:

> *an unpatched server that accepts compressed input could be taken over by a malicious client, and an unpatched client that accepts compressed input (such as "curl --compressed") could be taken over by a malicious server.*

No in-the-wild exploitation has been reported. CISA's October 23 assessment recorded exploitation as "none" and automation as "no," and [Red Hat](https://access.redhat.com/security/cve/CVE-2026-111497) said there is no reliable public proof-of-concept for running code.

Severity ratings differ by who is scoring. Google, which assigned the CVE, rates it 9.2, or critical, on the CVSS 4.0 scale. Node.js calls it high, and Red Hat rates it 8.1, or important...