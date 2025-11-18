---
title: Rust Adoption Drives Android Memory Safety Bugs Below 20% for First Time
url: https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html
source: The Hacker News
date: 2025-11-17
fetch_date: 2025-11-18T03:15:22.221252
---

# Rust Adoption Drives Android Memory Safety Bugs Below 20% for First Time

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Rust Adoption Drives Android Memory Safety Bugs Below 20% for First Time](https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html)

**Nov 17, 2025**Ravie LakshmananVulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_qGZvQDuR4AG6uEiMhGDHMsSkL1TLRNfW1kBylVrG6oiDRdisUMsnMb2vjfad2_IywwPHoJsNNX4kuhs_1UPn07KCLnt_z7C0AdmNTfDNKApwOAKnjDtuNuPR84jCFyw6deU-N6D3Jj8kR-BcV9sKidAEvdTxKFZA71P8OmCpvVgekFZCTwmMzoXS9qc2/s790-rw-e365/android-rust.jpg)

Google has disclosed that the company's continued adoption of the Rust programming language in Android has resulted in the number of memory safety vulnerabilities falling below 20% of total vulnerabilities for the first time.

"We adopted Rust for its security and are seeing a 1000x reduction in memory safety vulnerability density compared to Android's C and C++ code. But the biggest surprise was Rust's impact on software delivery," Google's Jeff Vander Stoep [said](https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html). "With Rust changes having a 4x lower rollback rate and spending 25% less time in code review, the safer path is now also the faster one."

The development comes a little over a year after the tech giant [disclosed](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html) that its transition to Rust led to a decline in memory safety vulnerabilities from 223 in 2019 to less than 50 in 2024.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

The company pointed out that Rust code requires fewer revisions, necessitating about 20% fewer revisions than their C++ counterparts, and has contributed to a decreased rollback rate, thereby improving overall development throughput.

Google also said it's planning to expand Rust's "security and productivity advantages" to other parts of the Android ecosystem, including [kernel](https://source.android.com/docs/core/architecture/kernel/release-notes), firmware, and critical first-party apps like [Nearby Presence](https://developers.google.com/nearby), Message Layer Security ([MLS](https://thehackernews.com/2023/07/google-messages-getting-cross-platform.html)), and Chromium, which has had its parsers for PNG, JSON, and web fonts replaced with memory-safe implementations in Rust.

Furthermore, it has emphasized the need for a defense-in-depth approach, stating that the programming language's built-in memory safety features are just one part of a comprehensive memory safety strategy.

As an example, Google highlighted its discovery of a memory safety vulnerability ([CVE-2025-48530](https://www.cve.org/CVERecord?id=CVE-2025-48530), CVSS score: 8.1) in CrabbyAVIF, an AVIF (AV1 Image File) parser/decoder implementation in [unsafe Rust](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html), that could have resulted in remote code execution. While the linear buffer overflow flaw never made it into a public release, it was [patched](https://thehackernews.com/2025/08/google-fixes-3-android-vulnerabilities.html) by Google as part of its Android security update for August 2025.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Further analysis of the "near-miss" vulnerability found that it was rendered non-exploitable by [Scudo](https://source.android.com/docs/security/test/scudo), a dynamic user-mode memory allocator in Android that's designed to combat heap-related vulnerabilities, such as buffer overflow, use after free, and double free, without sacrificing performance.

Emphasizing that unsafe Rust is "already really quite safe," Google said the vulnerability density is significantly lower as opposed to C and C++, adding that the incorporation of an ["unsafe" code block in Rust](https://rustfoundation.org/media/unsafe-rust-in-the-wild-notes-on-the-current-state-of-unsafe-rust/) doesn't automatically disable the programming language's safety checks.

"While C and C++ will persist, and both software and hardware safety mechanisms remain critical for layered defense, the transition to Rust is a different approach where the more secure path is also demonstrably more efficient," it said.

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

[Android](https://thehackernews.com/search/label/Android)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Google](https://thehackernews.com/search/label/Google)[mobile security](https://thehackernews.com/search/label/mobile%20security)[programming](https://thehackernews.com/search/label/programming)[Rust](https://thehackernews.com/search/label/Rust)[secure coding](https://thehackernews.com/search/label/secure%20coding)[software development](https://thehackernews.com/search/label/software%20development)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-aws-ai-security)

Trending News

[![⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Hyper-V Malware, Malicious AI Bots, RDP Exploits, WhatsApp Lockdown and More")

⚡ We...