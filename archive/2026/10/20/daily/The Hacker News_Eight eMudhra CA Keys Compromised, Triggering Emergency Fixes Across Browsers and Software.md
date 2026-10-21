---
title: Eight eMudhra CA Keys Compromised, Triggering Emergency Fixes Across Browsers and Software
url: https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html
source: The Hacker News
date: 2026-10-20
fetch_date: 2026-10-21T06:51:11.752122
---

# Eight eMudhra CA Keys Compromised, Triggering Emergency Fixes Across Browsers and Software

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

# [Eight eMudhra CA Keys Compromised, Triggering Emergency Fixes Across Browsers and Software](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html)

**Swati Khandelwal**Oct 20, 2026Web Security / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJOWLzgriXXM626bAOaX_LEoNH97Ab_XV4oQ0GxBeY3-PqkdXdcae52-wrl8r0LipTFBsvl4R7Y5j6jFsiG_9V8ZAwHOkAlsZaRcOAswStHhAG1FYm9W6kjA4FmOz0bXgVXO6LyEs9Fv75UrRFphZEzhXodKdTlYzfPK8sqW3DpxKBnD7OFQfqJJ_ay2c/s1700-nu-rw-lo-l85-e365/ecert.jpg)

The private keys of eight eMudhra intermediate certificate authority (CA) certificates are compromised, [Mozilla](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/) and [Google's Chrome Root Program](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE/m/Kp1v6CPuAAAJ) confirms on October 20.

An intermediate CA signs the certificates that websites present, so anyone holding one of these keys could issue a certificate for any website that a browser would accept.

A researcher reported the compromise to the root programs on the evening of October 17, and Chrome and Firefox blocked the eight certificates within hours, after Chrome verified the findings.

No TLS certificate chaining to the six intermediates used for websites had been logged to [Certificate Transparency](https://googlechrome.github.io/CertificateTransparency/ct_policy.html) (CT) before Chrome's block, so none could have been trusted by default in Chrome or any other browser that requires CT logging, the Chrome Root Program said.

It is not known how the keys left eMudhra, when, or whether anyone besides the researcher holds them.

The keys are the ones Go blocked in its October 20 security releases without naming the CA, as [The Hacker News reported earlier](https://thehackernews.com/2026/10/go-issues-emergency-update-blocking.html). The eight hash values in [Go's code](https://github.com/golang/go/commit/7f86f957633ee31a1c17a1eb8452ca7a3d9bc141) match the eight certificates. Go handled the fix on its URGENT track, which its [security policy](https://go.googlesource.com/website/%2Bshow/HEAD/_content/doc/security/policy.md) reserves for threats to the ecosystem's integrity or flaws being exploited in the wild, and neither the issue nor the release notes say which applied.

### What Was Compromised

eMudhra is an Indian CA that sells certificates under the emSign brand through companies in India, the United States, and the Netherlands, and it has roots in the Mozilla, Chrome, and Apple root stores. The eight compromised certificates are:

* **TLS, domain validated:** EM DV TLS CA - G3B (eMudhra BV, Netherlands) and EM DV TLS CA - G3C (eMudhra Inc, United States)
* **TLS, organization validated:** EM OV TLS CA - G3B and EM OV TLS CA - G3C
* **TLS, extended validation:** EM EV TLS CA - G3B and EM EV TLS CA - G3C
* **Code signing:** EM OV CS CA - G3B and EM OV CS CA - G3C

The six TLS certificates were issued by emSign Root TLS CA - G3 and chain to emSign ECC Root CA - G3, a root in the Chrome and Apple stores and, until October 20, in Mozilla's.

Each of the eight also exists as a second certificate with the same public key, cross-signed by Sectigo under its AAA Certificate Services root, according to a [certificate list](https://emudhra.we-have-a-problem.com/affected-certificates.json) published by Dennis Jackson, a Mozilla cryptography engineer.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

Chrome did not need to block the two code-signing certificates, because its TLS verifier will not build a path through an intermediate restricted to code signing, the Chrome Root Program said.

### Who Is Protected, and How

The Chrome Root Program received the report at 18:05 UTC on October 17 and had a [CRLSet](https://www.chromium.org/Home/chromium-security/crlsets/) update blocking the six TLS intermediates in place by 19:45 UTC.

[Mozilla](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE) received it at 20:06 UTC and finished pushing a [OneCRL](https://blog.mozilla.org/security/2015/03/03/revoking-intermediate-certificates-introducing-onecrl/) block to Firefox installations with standard settings at 22:59 UTC. CRLSets and OneCRL are revocation lists that the two browsers fetch on their own, so neither needed an update or a restart.

Chrome's block matches the public key rather than the certificate, so it also catches the Sectigo cross-signed copies. It is the same mechanism Chrome used earlier this month against [rogue certificates for Google domains](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html).

The researcher, credited by Mozilla only as Wayne, signed the message "We have a problem here - Wayne" with each of the eight keys and sent it to the root programs that day, according to Jackson, who published the signatures and certificates on a [one-page site](https://emudhra.we-have-a-problem.com/).

eMudhra has revoked the eight certificates. Apple blocked them on October 19, Microsoft on October 20, and other trust stores were notified on October 19, according to Jackson's site.

The cross-signed copies did not widen the risk in Chrome or Firefox. Both stopped trusting Sectigo's AAA Certificate Services root for websites in [April 2025](https://www.sectigo.com/resource-library/changes-to-root-ca-hierarchies-and-trust-status), and Chrome's [root store file](https://raw.githubusercontent.com/chromium/chromium/main/net/data/ssl/chrome_root_store/root_store.textproto) does not carry it. Apple's root list for iOS 26 and macOS 26, published in December 2025, includes it.

Mozilla does not believe, for now, that the problem affects other CAs, Jackson wrote on Mozilla's policy list, and Chrome said it checked every other CA certificate in its store and "found no other instances ...