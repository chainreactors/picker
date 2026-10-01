---
title: OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted
url: https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html
source: The Hacker News
date: 2026-09-30
fetch_date: 2026-10-01T07:59:26.165721
---

# OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [OpenSSL Fixes High-Severity DTLS Flaw That Can Leak Heap Memory Unencrypted](https://thehackernews.com/2026/09/openssl-fixes-high-severity-dtls-flaw.html)

**Swati Khandelwal**Sep 30, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0Po53IuyRAhsYzbs5KKPp_UBpklONBiOzoLWgXrklvrgDn5xnpjuRjU8UYoyLuImSmiPtOHQK3ExgQk5zhxlqsAcUmTLRFowkQXzan2RD955Gw-sumsvmwzLBTViUBRhyphenhyphenHCnETV23Qbt01RwaovTe1ogMeMYDSGxmF5n84NKZOB3EiWz6VAHUlfDm5YE/s1700-nu-rw-lo-l85-e365/openssl-memory.jpg)

A High-severity OpenSSL flaw can leak heap memory to the other side of a DTLS connection or crash the program, [OpenSSL said](https://openssl-library.org/news/secadv/20260929.txt) on September 29 as it released fixes.

[DTLS](https://www.rfc-editor.org/rfc/rfc9147.html), the TLS variant used for UDP traffic, resends a handshake message if no reply arrives before the timer expires. The leak or crash can happen when such a resend starts while a larger handshake message is stuck part-way through being sent.

The flaw, tracked as CVE-2026-84782, is fixed in [OpenSSL 4.0.3, 3.6.5, 3.5.9 and 3.4.8](https://openssl-library.org/source/). Fixed versions for the older 3.0, 1.1.1 and 1.0.2 branches go only to customers who pay for OpenSSL's premium support. OpenSSL 3.0 [stopped getting public security fixes](https://openssl-library.org/post/2026-09-16-eol30/) on September 7.

OpenSSL has not said whether an attacker can cause a resend while a message is stuck, nor has it reported any attacks exploiting the flaw.

DTLS is used, for example, to protect WebRTC data channels and to set up encryption keys for internet calls. Software is exposed to this flaw only if it uses OpenSSL for DTLS.

DTLS splits a large handshake message into fragments that each fit in one UDP datagram. If the connection cannot accept more data for the moment, sending can pause part-way through a message and continue later. While sending is paused, the resend timer can still fire and send an earlier message again.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Before the fix, the resend used the paused message's position in the buffer instead of going back to the start of the message being resent. The resent message went out with the wrong label. Its body was leftover bytes from the larger message, and reading it could overrun the buffer.

The wrongly labeled message can carry heap memory to the other side as unencrypted handshake data, according to OpenSSL. If the read reaches unmapped memory, the program crashes.

OpenSSL does not limit the flaw to DTLS clients or servers, and its fix was tested in both roles.

Laurent Gaffie of Secorizon reported the flaw on August 17, and Ryan Hooper developed [the fix](https://github.com/openssl/openssl/commit/d951e02ede8f6a6ff8150546db44b34f0518192c).

OpenSSL rates the flaw High, one level below Critical in its severity scale. The project's [security policy](https://openssl-library.org/policies/general/security-policy/) advises installing updates with High fixes as soon as possible.

CISA gave the flaw a [CVSS score of 8.2](https://github.com/cisagov/vulnrichment/blob/develop/2026/84xxx/CVE-2026-84782.json) out of 10 on September 29, rating its impact on confidentiality Low and on availability High. CISA's record listed exploitation as "none" at that time. OpenSSL does not use CVSS to set its severity ratings and says scores from outside parties can differ greatly from them.

[Ubuntu's security notice](https://ubuntu.com/security/notices/USN-8847-1) says an attacker could possibly use the flaw to cause "incorrect handshake behavior or a denial of service." It does not mention leaked memory.

### Which Versions Fix the Flaw

The flaw affects OpenSSL 4.0, 3.6, 3.5, 3.4, 3.0, 1.1.1, and 1.0.2, in every release before the fixed version shown below.

| Branch | Fixed version | Who can get it | Support status |
| --- | --- | --- | --- |
| 4.0 | 4.0.3 | Public download | Supported until May 14, 2027 |
| 3.6 | 3.6.5 | Public download | Supported until November 1, 2026 |
| 3.5 | 3.5.9 | Public download | Long-term support release, supported until April 8, 2030 |
| 3.4 | 3.4.8 | Public download | Supported until October 22, 2026 |
| 3.0 | 3.0.23 | Premium support customers only | Public support ended September 7, 2026 |
| 1.1.1 | 1.1.1zj | Premium support customers only | No public support |
| 1.0.2 | 1.0.2zs | Premium support customers only | No public support |
| 3.1, 3.2, 3.3 | None listed | Not applicable | No public support. OpenSSL did not check whether these branches are affected. |

OpenSSL lists no workaround for users who cannot update yet. Ubuntu fixed the flaw on September 29 in its own packages, which keep older OpenSSL version numbers:

* Ubuntu 26.04 LTS: libssl3t64 3.5.5-1ubuntu3.6
* Ubuntu 24.04 LTS: libssl3t64 3.0.13-0ubuntu3.16
* Ubuntu 22.04 LTS: libssl3 3.0.2-0ubuntu1.30

Ubuntu users need to reboot after the update for all the changes to take effect.

Debian fixed the flaw in Debian 13 with version 3.5.7-1~deb13u3 of its openssl package, released as [DSA-6531-1](https://security-tracker.debian.org/tracker/DSA-6531-1). Its [security tracker](https://security-tracker.debian.org/tracker/source-package/openssl) still listed Debian 12 as vulnerable as of 07:36 UTC on September 30.

### What OpenSSL 3.0 Users Can Do

The last public 3.0 release was [3.0.22](https://github.com/openssl/openssl/releases/tag/openssl-3.0.22), on August 25. Version 3.0.23 is the first 3.0 security release that OpenSSL has not made public. It fixes 6 of the 14 flaws disclosed on September 29, including CVE-2026-84782.

For Ubuntu 22.04 and 24.04, which use OpenSSL 3.0, the fix is already available in the packages listed above. Anyone who builds OpenSSL 3.0 or ships a copy inside their own software has no public fix from OpenSSL.

[![Cybersecurity](data:image/png;base64...)](https://th...