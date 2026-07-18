---
title: OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests
url: https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
source: The Hacker News
date: 2026-07-17
fetch_date: 2026-07-18T04:46:39.412878
---

# OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests

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

# [OpenSSL HollowByte Flaw Could Freeze Server Memory with 11-Byte TLS Requests](https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html)

**Swati Khandelwal**Jul 17, 2026Vulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk66eU1Srifu4Rdpf7MZDjg3GdNMtQK6ZW-F283kxhZ7Z0W_8nWNJynZiQ7n0ov9OLNm315P4942h3-unMI0WZ1-LH8tdQ6sv2o6q0TxKT-bVKewzkQULKKXSJOee_oANuI3YquoDgSPHsPeXEdQcFRoy8czRQimH_f0sNHJ55-5LA153sQgUPkpBBEVE/s1700-e365/openssl.jpg)

Eleven bytes will make an unpatched OpenSSL server set aside up to 131 KB of memory for a message that never arrives. On the glibc systems Okta tested, that memory is gone until the process restarts.

OpenSSL shipped the **HollowByte** fix in June with no CVE, no advisory, and no changelog entry pointing at it. Okta's Red Team, which reported the denial-of-service bug and named it, published the details on Thursday.

The fixed releases are OpenSSL [4.0.1, 3.6.3, 3.5.7, 3.4.6, and 3.0.21](https://github.com/openssl/openssl/releases), all dated June 9. Every release on those branches before the fixed ones has it. Nothing in a normal patch pipeline will point you at them: there is no identifier for a scanner to match and no advisory to read.

The flaw is that OpenSSL took the attacker's word for it. Every TLS handshake message carries a 4-byte header, three bytes of which declare how long the body will be. Older versions grew the receive buffer to that declared size the moment the header landed, before a single byte of the body showed up, and before the handshake's own checks ran.

For an inbound ClientHello the ceiling is 131 KB. Then the worker thread blocks, waiting on a body that never comes. No authentication, no session, no key exchange.

## The memory does not come back

On its own, that is a connection-exhaustion attack, and those are as old as [Slowloris](https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html). What makes HollowByte stick is glibc. When the attacker drops the connection, OpenSSL frees the buffer, but glibc holds small and medium chunks for reuse rather than returning them to the kernel.

The attack varies the claimed size on every connection, and in Okta's tests, that was enough to stop the allocator from reusing what it freed. The heap fragments, resident set size climbs, and it stays climbed long after the attacker has gone.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

In Okta's NGINX testing, a 1 GB server was OOM-killed with 547 MB of memory frozen in fragments. On a 16 GB server, HollowByte locked up 25% of system memory without ever crossing the connection ceiling, which is why the Red Team says ["standard connection-limiting defenses won't stop it"](https://sec.okta.com/articles/2026/06/openssl-hollowbtye-a-dos-hiding-in-11-bytes/).

Those figures are Okta's own, and it published no exploit code alongside them. The Hacker News found no public proof-of-concept repository on GitHub as of July 18.

## OpenSSL decided this wasn't a vulnerability

The [pull request](https://github.com/openssl/openssl/pull/30792) from Matt Caswell, who wrote the patch, puts it plainly: the security team chose to "handle this as a 'bug or hardening' only fix". OpenSSL's own [security policy](https://openssl-library.org/policies/general/security-policy/) defines four severity tiers, Critical down to Low, and "bug or hardening" is not among them.

Even a Low issue earns a CVE, a changelog note, and an entry on the vulnerabilities page. HollowByte has none of the three. The Hacker News found no mention of the fix in the [release notes](https://github.com/openssl/openssl/releases/tag/openssl-4.0.1) or in all 23 entries of OpenSSL's [4.0.1 changelog](https://github.com/openssl/openssl/blob/openssl-4.0.1/CHANGES.md).

OpenSSL has not said why. Here is the case for them: 131 KB per connection is small, every TLS server allocates memory per connection, and a bounded allocation is not a vulnerability. Okta's answer is that the memory never comes back.

The Hacker News has asked OpenSSL why HollowByte was triaged below Low, and whether the fix reached the extended-support 1.1.1 and 1.0.2 branches. It has also asked Okta whether the fragmentation survives allocators other than glibc. This story will be updated with any response.

The project's line is finer than it looks. In January, OpenSSL assigned [CVE-2025-66199](https://openssl-library.org/news/vulnerabilities-3.6/#CVE-2025-66199), rated Low, to a TLS 1.3 certificate-compression bug in which a peer-supplied length grew a heap buffer before validation, worth around 22 MiB per connection.

That one needed four things to line up: certificate compression compiled in, a compression algorithm available, the extension negotiated, and, on servers, client certificates requested. HollowByte needs none of them.

The same June 9 release assigned [CVE-2026-34183](https://openssl-library.org/news/vulnerabilities-3.6/#CVE-2026-34183), rated Moderate, to unbounded memory growth in the QUIC PATH\_CHALLENGE handler. Both are memory-exhaustion DoS. Both got numbers.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

The release also closed 18 CVEs, including a High-severity use-after-free in PKCS7\_verify(), so anyone running one of those upstream builds has the fix without being told.

Downstream is worse. Red Hat's [documented default](https://access.redhat.com/security/updates/backporting) is to backport rather than move the version, so a patched package still reports the version it was built from. What normally resolves that is the advisory and the OVAL feed, both keyed to CVE names. There...