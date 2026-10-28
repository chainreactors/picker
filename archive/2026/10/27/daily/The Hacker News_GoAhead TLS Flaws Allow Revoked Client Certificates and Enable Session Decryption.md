---
title: GoAhead TLS Flaws Allow Revoked Client Certificates and Enable Session Decryption
url: https://thehackernews.com/2026/10/goahead-tls-flaws-allow-revoked-client.html
source: The Hacker News
date: 2026-10-27
fetch_date: 2026-10-28T07:49:45.441887
---

# GoAhead TLS Flaws Allow Revoked Client Certificates and Enable Session Decryption

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

# [GoAhead TLS Flaws Allow Revoked Client Certificates and Enable Session Decryption](https://thehackernews.com/2026/10/goahead-tls-flaws-allow-revoked-client.html)

**Swati Khandelwal**Oct 27, 2026Vulnerability / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6ae8TupuVJ4B0uHZJxwQnaqstuuA42Jwt_Zh7m9RwCBp_IrCYuChUaac6fUphOhpalVEC8tfhGsYGxt1lmswBobM-r-ds6t0uEMSV9HZKT_dYcigHPxGJQo7dcJte96ymjxwSREmiGulG6xPIX4Hx3visDSuyaX2DJ3HRcctAz0Jw1T9ALkCEwZUlMsQ/s1700-nu-rw-lo-l85-e365/goahead.jpg)

The GoAhead embedded web server loaded a certificate revocation list into its default TLS backend but never turned revocation checking on, so a revoked client certificate could still pass login on affected setups.

The flaw is in builds that use the OpenSSL backend with mutual-TLS, where the server checks a client certificate and vice versa, and a revocation list is configured to block revoked certificates.

That is a setup an operator turns on deliberately; a default build does not. [GoAhead 6.1.1](https://github.com/embedthis/goahead/releases/tag/v6.1.1), released to device makers on August 2, 2026, and publicly published on October 12, fixes it.

GoAhead is a small web server that device makers build into firmware to run management pages on routers, printers, gateways and industrial controllers. Its maker, EmbedThis, says it runs in hundreds of millions of devices.

The flaw was found by Sébastien Féry of FoxIO, who described it and two other TLS problems in a [write-up](https://foxio.io/blog/choose-your-backend-three-tls-bugs-in-goahead) on October 26.

On an affected build, the server loads the revocation list file at startup and reports no error, so an operator who configured it has every reason to think revocation is working. It is not. A client whose certificate was revoked, for example a stolen or retired device, completes the handshake as if the certificate were still valid and gets whatever access that identity allows.

In FoxIO's test against GoAhead 6.1.0 with OpenSSL 3.6.2, a revoked certificate was accepted with issuer checking switched on.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

The OpenSSL advisory describes revoked client certificates as [silently accepted](https://github.com/embedthis/goahead/security/advisories/GHSA-5m75-xq69-c3c5). To be exploited, the build must use the OpenSSL backend with client certificates required, a trusted certificate authority bundle and issuer checking enabled, and a revocation list configured; the attacker must hold a certificate signed by a trusted authority and listed as revoked. Builds that use the Mbed TLS backend are unaffected; that backend checks revocation via a separate code path.

The identifier on the advisory is CVE-2026-115881, rated 9.1 by EmbedThis. As of October 27, that identifier and the others below were not yet live in the public CVE and NVD databases; EmbedThis says it has requested them. The severity ratings are the vendor's own.

Researchers cover two further problems, each tied to a specific TLS build. The versions and fixes differ, so the table below maps each by backend.

| TLS build | What goes wrong | Affected versions | Fix or interim option |
| --- | --- | --- | --- |
| OpenSSL (default) | Revocation list loaded but never enforced; revoked client certificates accepted. CVE-2026-115881, rated 9.1. | 3.4.5 through 6.1.0 | Upgrade to 6.1.1. No interim option in the advisory. |
| LibreSSL legacy verifier (3.2.x, 3.3.2–3.3.6) | A client certificate chain longer than the limit is accepted when client certificates are required but issuer checking is off. [CVE-2026-115884](https://github.com/embedthis/goahead/security/advisories/GHSA-r392-vqwx-3r4g), rated 7.4. | 6.1.0 and earlier on those LibreSSL versions | Upgrade to 6.1.1, or turn issuer checking on with a trusted CA bundle, or use OpenSSL or LibreSSL 4.x. |
| Mbed TLS | A length typo sends a 1-byte Diffie-Hellman value instead of the full 2048-bit one, so a passive observer can decrypt the session. Rated 5.9. [No CVE assigned](https://github.com/embedthis/goahead/security/advisories/GHSA-fmvx-2xfx-2gq4). | 4.0.2 through 6.1.0 | Upgrade to 6.1.1, turn off finite-field DHE suites, or use the OpenSSL backend. |

The Mbed TLS problem only reaches a session if the client accepts the broken setup. OpenSSL, current Go, current Java, and mainstream browsers refuse a value that small and fall back to a stronger key exchange, so the session never completes.

Clients without a minimum-size check, such as some embedded or custom ones, accept it, and then anyone who recorded the traffic can work out the key and read the session. TLS 1.3 and ECDHE sessions are unaffected, and Mbed TLS 4.x removed the key exchange they rely on.

The LibreSSL problem allows an attacker to present a certificate chain longer than GoAhead's 10-certificate limit and still complete the handshake as an authenticated client, without any trusted key.

It appears only on builds linked against the older LibreSSL versions listed above and only where client certificates are required with issuer checking off. OpenSSL, BoringSSL, AWS-LC and LibreSSL 4.x reject the over-long chain.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Which backend and settings a build uses are chosen when the firmware is compiled, so a device owner cannot tell from the outside which apply. That is also why the fix is slow to arrive: GoAhead 6.1.1 is a drop-in replacement that device makers rebuild and ship as a firmware update, and an owner gets it only when their manufacturer does so. Whether any manufacturer has shipped it is not known.

As of October 27, no source reported any of these problems being used in attacks. EmbedThis's policy is to end a disclosure embargo and publish early if a flaw is being exploited or disclosed by someone else, so the coordinated October 12 release is consistent with no known...