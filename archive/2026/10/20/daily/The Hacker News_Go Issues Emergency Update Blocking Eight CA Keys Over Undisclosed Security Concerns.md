---
title: Go Issues Emergency Update Blocking Eight CA Keys Over Undisclosed Security Concerns
url: https://thehackernews.com/2026/10/go-issues-emergency-update-blocking.html
source: The Hacker News
date: 2026-10-20
fetch_date: 2026-10-21T06:51:12.701164
---

# Go Issues Emergency Update Blocking Eight CA Keys Over Undisclosed Security Concerns

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

# [Go Issues Emergency Update Blocking Eight CA Keys Over Undisclosed Security Concerns](https://thehackernews.com/2026/10/go-issues-emergency-update-blocking.html)

**Swati Khandelwal**Oct 20, 2026Encryption / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh12Jum-ReZMOyqaMubiLlMwx4-uDVxEJkD6-CJabWhHfCKV-Csw7P4MoeRX85Ag-3rxZMftHE6KGcdh059DoOPvF1Mirv05BQsflmg8RroWBt_t00BGTHsdhqkmVWVuRHKAs56AhNfdsq_YH0QWrMJ1z4dFT3I3xOK7Dwqu7aPp_P7tFSxQ-bzqyz8e4/s1700-nu-rw-lo-l85-e365/go-certs.jpg)

Go 1.27.3 and Go 1.26.10, [released](https://groups.google.com/g/golang-announce/c/66pojueaQek) on October 20, make Go's certificate verifier reject any certificate chain that passes through one of [eight intermediate](https://github.com/golang/go/commit/7f86f957633ee31a1c17a1eb8452ca7a3d9bc141) certificate authority keys.

Programs built on the new release will refuse connections to sites and services whose certificates were issued under those keys. The Go team says the keys belong to one certificate authority it has not named, and that it is blocking them because of "specific security concerns around their operation."

It handled the fix on its [URGENT track](https://go.dev/doc/security/policy), the one reserved for its most serious issues, and recommends upgrading immediately.

Two days earlier, on October 17, Mozilla added six intermediate certificates issued by eMudhra's emSign Root TLS CA - G3 to [OneCRL](https://firefox.settings.services.mozilla.com/v1/buckets/security-state/collections/onecrl/records), the list Firefox uses to block certificates. The Mozilla bug behind those entries is [closed to the public](https://bugzilla.mozilla.org/show_bug.cgi?id=2083382), and neither Mozilla nor Go has said what prompted its action. Whether Chrome, Apple, or Microsoft have taken similar action is not established.

Go's change lists only the SHA-256 hashes of the eight keys. [A commenter on the Go issue](https://github.com/golang/go/issues/82345) matched all eight to eMudhra intermediates by looking the hashes up in certificate records.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

By that matching, six are TLS intermediates issued under the same emSign Root TLS CA - G3 that Mozilla's entries name, and two are code-signing intermediates under emSign Root CS CA - G3:

* **TLS, domain validated:** EM DV TLS CA - G3B (eMudhra BV, Netherlands) and EM DV TLS CA - G3C (eMudhra Inc, U.S.)
* **TLS, organization validated:** EM OV TLS CA - G3B and EM OV TLS CA - G3C
* **TLS, extended validation:** EM EV TLS CA - G3B and EM EV TLS CA - G3C
* **Code signing:** EM OV CS CA - G3B and EM OV CS CA - G3C

The Hacker News has not independently checked the hashes against the certificates. Mozilla's six entries carry the same issuing root, but Mozilla's records do not name the six certificates.

The filter runs whenever a Go program verifies a certificate chain. It hashes each certificate's public key rather than the certificate itself, so a cross-signed copy of one of the eight keys, the same key signed by a different root, is caught as well.

It is applied in Go's own verifier and in the macOS and Windows code paths that hand verification to the operating system. A rejected chain returns the error x509: no valid chains built.

The change contains no setting to turn the filter off. Given the structure of the code, it also applies when a program supplies its own set of trusted roots, so a private deployment that intentionally trusts one of the eight keys will fail too. The Go team has not said whether that is intended.

Go's verifier "doesn't do any revocation checking," as [its documentation warns](https://pkg.go.dev/crypto/x509). It also does not read the block lists browsers use, such as the [CRLSets Chrome used](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html) against rogue Google certificates this month.

Blocking a key therefore means shipping it in a release, and programs keep the old behavior until they are rebuilt. Projects including Bluesky's indigo were rebuilt on the new releases on October 20.

What happened at the certificate authority is not public. Go's announcement gives one sentence about security concerns, and the release came without the pre-announcement Go sent before its October 8 security releases.

Go's security policy defines URGENT track issues as "a threat to the Go ecosystem's integrity" or flaws being actively exploited with severe damage, and says there are no recent examples. Go has not said which of those applied.

On the issue, one user asked for the committed patch to explain "who and what they correspond to." The Go team had not replied as of October 20.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

eMudhra is an Indian certificate authority that sells certificates under the emSign brand. Its roots emSign Root CA - G1 and emSign ECC Root CA - G3 are in the [Chrome](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md), [Apple](https://support.apple.com/en-us/126047) , and Mozilla root stores. The company [told Mozilla](https://bugzilla.mozilla.org/show_bug.cgi?id=2018979) earlier this year that its newer TLS root is cross-signed by emSign Root CA - G1, which is how certificates under the newer root chain to a trusted root.

In September, a six-week [public discussion](https://mail-archive.com/public%40ccadb.org/msg00586.html) of eMudhra's request to add ten new roots to the root programs run by browser and operating-system makers, including emSign Root TLS CA - G3, closed with no objections.

Certificates logged for eMudhra's own domains, including emsign.com and emudhra.com, chain through other eMudhra intermediates, according to certificate transparency records The Hacker News checked on October 20. The company's repository contained no notice ...