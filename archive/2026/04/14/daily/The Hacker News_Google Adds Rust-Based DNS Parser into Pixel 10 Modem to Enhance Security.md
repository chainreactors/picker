---
title: Google Adds Rust-Based DNS Parser into Pixel 10 Modem to Enhance Security
url: https://thehackernews.com/2026/04/google-adds-rust-based-dns-parser-into.html
source: The Hacker News
date: 2026-04-14
fetch_date: 2026-04-15T04:44:12.125299
---

# Google Adds Rust-Based DNS Parser into Pixel 10 Modem to Enhance Security

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

# [Google Adds Rust-Based DNS Parser into Pixel 10 Modem to Enhance Security](https://thehackernews.com/2026/04/google-adds-rust-based-dns-parser-into.html)

**Ravie Lakshmanan**Apr 14, 2026Mobile Security / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjblrgfLU8m4awyQDEqyzwguow-RuCp4UH1k5DBkrUrP87A7tsEQPPaLD_D9M4VXF5mSNrmp1eurx_QW-nVjM1nNnkyEIFyFiry3nxE0Wq3xrT0L06S6B11rEHcWzB7q78RRQySSxwLAVIncgqO5qhtY6b0A_LzYF8wtvH94G_TLQEn8UIivqrJNkH88Nf7/s1700-e365/android-rust.jpg)

Google has announced the integration of a Rust-based Domain Name System (DNS) parser into the modem firmware as part of its ongoing efforts to beef up the security of Pixel devices and push memory-safe code at a more foundational level.

"The new Rust-based DNS parser significantly reduces our security risk by mitigating an entire class of vulnerabilities in a risky area, while also laying the foundation for broader adoption of memory-safe code in other areas," Jiacheng Lu, a software engineer part of the Google Pixel Team, [said](https://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html).

The security boost via Rust integration is available for Pixel 10 devices, making it the first Pixel device to integrate a memory-safe language into its modem.

The move builds upon a series of initiatives the tech giant has taken to harden the cellular baseband modem against exploitation. In late 2023, it [highlighted](https://thehackernews.com/2023/12/google-using-clang-sanitizers-to.html) the role played by Clang sanitizers like Overflow Sanitizer (IntSan) and BoundsSanitizer (BoundSan) to catch undefined behavior during program execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

A year later, it also [detailed](https://thehackernews.com/2024/10/android-14-adds-new-security-features.html) the various security measures built into the modem firmware to combat 2G exploits and baseband attacks that exploit memory-safety vulnerabilities like buffer overflows to achieve remote code execution.

These security advances have been complemented by Google's steady adoption of Rust into [Android](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html) and [low-level firmware](https://security.googleblog.com/2024/09/deploying-rust-in-existing-firmware.html). In November 2025, the company [revealed](https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html) that the number of memory safety vulnerabilities fell below 20% of total vulnerabilities discovered in the mobile operating system last year.

Google said it opted for the DNS protocol for its Rust implementation owing to the fact that it underpins modern cellular communications and that vulnerabilities in the system can expose users to malicious attacks when designed in a memory-unsafe language, resulting in out-of-bound memory accesses, as in the case of [CVE-2024-27227](https://nvd.nist.gov/vuln/detail/cve-2024-27227).

"With the evolution of cellular technology, modern cellular communications have migrated to digital data networks; consequently, even basic operations such as call forwarding rely on DNS services," it added. "Implementing the DNS parser in Rust offers value by decreasing the attack surfaces associated with memory unsafety."

To that end, Google has chosen the "[hickory-proto](https://crates.io/crates/hickory-proto)" crate, a [Rust-based DNS client, server, and resolver](https://github.com/hickory-dns/hickory-dns), to implement the protocol, while modifying it to support bare metal and embedded environments. Another important component of this change is the use of a custom tool called "[cargo-gnaw](https://fuchsia.googlesource.com/fuchsia/%2B/master/tools/cargo-gnaw/)" to easily resolve and maintain more than 30 dependencies introduced by the crate.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

The internet company also noted that the DNS Rust crate is not optimized for use in memory-constrained systems, and that one possible code size optimization could be achieved by adding extra feature flags to ensure modularity and selectively compile only required functionality.

"For the DNS parser, we declared the DNS response parsing API in C and then implemented the same API in Rust," Google said. "The Rust function returns an integer standing for the error code. The received DNS answers in the DNS response are required tobe updated to in-memory data structures that are coupled with the original C implementation;therefore, we use existing C functions to do it. The existing C functions are dispatched from the Rust implementation."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Android](https://thehackernews.com/search/label/Android), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DNS](https://thehackernews.com/search/label/DNS), [Firmware Security](https://thehackernews.com/search/label/Firmware%20Security), [Google](https://thehackernews.com/search/label/Google), [mobile security](https://thehackernews.com/search/label/mobile%20security), [network security](https://thehackernews.com/search/label/network%20security), [Rust Programming](https://thehackernews.com/search/label/Rust%20Programming), [secure coding](https://thehackernews.com/search/label/secure%20coding), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Microso...