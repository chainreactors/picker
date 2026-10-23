---
title: Node.js Brotli Decoder Bug Could Allow Remote Code Execution in All Supported Versions
url: https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:43.952529
---

# Node.js Brotli Decoder Bug Could Allow Remote Code Execution in All Supported Versions

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

# [Node.js Brotli Decoder Bug Could Allow Remote Code Execution in All Supported Versions](https://thehackernews.com/2026/10/nodejs-brotli-decoder-bug-could-allow.html)

**Swati Khandelwal**Oct 22, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFwR_FE94PTthun36oXfrSIiYx7N-Hb3Ww1w2gFs6x6qs0mML2v_TmYZmgqYKxB6VlMBzmIQksNdHldgX-UxykDBNwnszmBuB7IZWyWJhxei65NJlOImUWde5tYzB7D94dmieFBGhFNVAt3bL4qlhXkl4o3uw362QKgJpk37xutyRmM5bB3sHR8XMC3bc/s1700-nu-rw-lo-l85-e365/nodejs-rce.jpg)

Node.js released [security updates](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) on October 21 for its three supported release lines, 22.x, 24.x and 26.x, fixing 10 flaws. The most serious is a bug in the Brotli decompression code that Node.js bundles, which the project says can allow remote code execution, meaning an attacker could run code of their choosing on the affected system.

Each supported line has one fixed version: [22.23.4](https://nodejs.org/en/blog/release/v22.23.4/) and [24.22.1](https://nodejs.org/en/blog/release/v24.22.1/) on the long-term support lines, and [26.12.1](https://nodejs.org/en/blog/release/v26.12.1/) on the current line. Node.js 20.x and earlier have [reached end of life](https://github.com/nodejs/Release#release-schedule) and will not receive the fix, so they should be moved to a supported line.

The Brotli flaw is in code Node.js bundles, not in a user's own program. Node.js runs that code whenever it decompresses Brotli data, either directly through the [node:zlib](https://nodejs.org/api/zlib.html) module or automatically when code calls fetch() on a response sent with Brotli compression.

An application is exposed where it decompresses Brotli data an attacker controls, such as a request body or a response fetched from another server.

### The Brotli Flaw

The flaw is an out-of-bounds write in the Brotli decoder, set off by malformed compressed input. The fix is an upstream patch from the Brotli project that Node.js copied in, and it makes the decoder catch invalid input and stop earlier rather than writing past the buffer.

Brotli is Google's compression library, and Node.js ships its own copy. The same fix shipped in [Brotli 1.2.1, 1.1.1, and 1.0.10](https://github.com/google/brotli/blob/v1.2.1/CHANGELOG.md) on October 21, so other software that bundles Brotli may need the same update. The change was first made in Brotli's source in February 2026 and shipped as a security release only in October.

"Remote code execution" is the project's description of what the flaw could allow, and the flaw is rated high rather than critical. How far that has been shown in practice is narrower.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

A public proof-of-concept published on October 22 reached code execution only against a deliberately weakened test build. On a standard Node.js build, its author reported a crash and a limited read of process memory, not code execution, and said a working attack on a normal build was not achieved.

Patched Node.js rejects the malformed input the proof-of-concept uses, and no exploitation of the flaw in the wild has been reported as of October 22.

### The Other Flaws

Three of the other fixes are also rated high. Two are TLS certificate checks an attacker could bypass by writing a server's IP address in an unusual form, so a certificate matches a host it should not (CVE-2026-106069 and CVE-2026-105483). The third stops dns.resolve from cutting a hostname short at an embedded null byte (CVE-2026-105482).

Node.js rates CVE-2026-105483 high, though the commit that fixed it calls the bug low-severity and hard to exploit.

The rest are medium and low severity. One medium flaw makes crypto.randomUUID() and crypto.randomInt() hand back the same values in every process when an application is built as a startup snapshot or a single-executable application (CVE-2026-106074), which undermines anything that relies on those values being unpredictable.

The full set, and the lines each one affects:

| CVE | What it is | Severity | Affected lines |
| --- | --- | --- | --- |
| CVE-2026-111497 | Out-of-bounds write in the Brotli decoder; remote code execution, per the project | High | 22.x, 24.x, 26.x |
| CVE-2026-106069 | TLS hostname-check bypass when a host resolves to an IP address in non-canonical form | High | 22.x, 24.x, 26.x |
| CVE-2026-105483 | TLS hostname-check bypass when an IP is written in fullwidth digits | High | 24.x, 26.x |
| CVE-2026-105482 | dns.resolve truncates names that contain a null byte | High | 22.x, 24.x, 26.x |
| CVE-2026-105481 | Keep-alive socket can process a response written before the request was sent | Medium | 22.x, 24.x, 26.x |
| CVE-2026-106072 | Certificate validation for non-canonical IPv4 lets DNS names authenticate IP endpoints | Medium | 22.x, 24.x, 26.x |
| CVE-2026-106074 | randomUUID() and randomInt() caches reused in startup snapshots and single-executable apps | Medium | 22.x, 24.x, 26.x |
| CVE-2026-106070 | ZipFile returns attacker-controlled bytes after a failed header check | Low | 26.x |
| CVE-2026-106071 | Permission Model over-grants file access through a wildcard lookup | Low | 26.x |
| CVE-2026-106073 | Permission Model bypass with fs.realpathSync | Low | 22.x, 24.x, 26.x |

### The eMudhra Certificate Block

The same updates also stop Node.js from trusting eight intermediate certificate authority keys from the Indian provider eMudhra that were [reported compromised](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html) days earlier.

Node.js uses the Mozilla root certificate list but does not perform revocation checks by default, so before this update, a certificate chain built on one of the compromised keys still passed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The releases add a [built-in block](https://...