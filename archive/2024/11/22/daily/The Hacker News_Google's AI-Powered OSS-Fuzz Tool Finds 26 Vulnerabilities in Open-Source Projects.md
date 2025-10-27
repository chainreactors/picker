---
title: Google's AI-Powered OSS-Fuzz Tool Finds 26 Vulnerabilities in Open-Source Projects
url: https://thehackernews.com/2024/11/googles-ai-powered-oss-fuzz-tool-finds.html
source: The Hacker News
date: 2024-11-22
fetch_date: 2025-10-06T19:20:28.624778
---

# Google's AI-Powered OSS-Fuzz Tool Finds 26 Vulnerabilities in Open-Source Projects

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Google's AI-Powered OSS-Fuzz Tool Finds 26 Vulnerabilities in Open-Source Projects](https://thehackernews.com/2024/11/googles-ai-powered-oss-fuzz-tool-finds.html)

**Nov 21, 2024**Ravie LakshmananArtificial Intelligence / Software Security

[![Open-Source Projects](data:image/png;base64... "Open-Source Projects")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKrOnZfHrZ1tgfCsIFF02hSuNi9dScN8SMCYNBC-6HeeQYJjlQHWwwUB1vdFKG-BgXgkr4Ss9PF3qOxgONjdiUN4FUs_9MNN4NJlOXZSkmVnb7FtQnefzHJnypVl0jUYfRlKbzKkGk-3FvO7PlDaX0hyphenhyphen-9ltzFug5x-rxJcvgnp2rhbX_Y40FxYiYXdtSJ/s790-rw-e365/ai-tool.png)

Google has revealed that its AI-powered fuzzing tool, OSS-Fuzz, has been used to help identify 26 vulnerabilities in various open-source code repositories, including a medium-severity flaw in the OpenSSL cryptographic library.

"These particular vulnerabilities represent a milestone for automated vulnerability finding: each was found with AI, using AI-generated and enhanced fuzz targets," Google's open-source security team [said](https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html) in a blog post shared with The Hacker News.

The OpenSSL vulnerability in question is [CVE-2024-9143](https://www.cve.org/CVERecord?id=CVE-2024-9143) (CVSS score: 4.3), an out-of-bounds memory write bug that can result in an application crash or remote code execution. The issue has been [addressed](https://openssl-library.org/news/secadv/20241016.txt) in OpenSSL versions 3.3.3, 3.2.4, 3.1.8, 3.0.16, 1.1.1zb, and 1.0.2zl.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Google, which added the ability to [leverage](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html) large language models (LLMs) to improve fuzzing coverage in OSS-Fuzz in August 2023, said the vulnerability has likely been present in the codebase for two decades and that it "wouldn't have been discoverable with existing fuzz targets written by humans."

Furthermore, the tech giant noted that the use of AI to [generate fuzz targets](https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md) has improved code coverage across 272 C/C++ projects, adding over 370,000 lines of new code.

"One reason that such bugs could remain undiscovered for so long is that line coverage is not a guarantee that a function is free of bugs," Google said. "Code coverage as a metric isn't able to measure all possible code paths and states—different flags and configurations may trigger different behaviors, unearthing different bugs."

These AI-assisted vulnerability discoveries are also made possible by the fact that LLMs are proving to be adept at emulating a developer's fuzzing workflow, thereby allowing for more automation.

The development comes as the company [revealed](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html) earlier this month that its LLM-based framework called Big Sleep facilitated the detection of a zero-day vulnerability in the SQLite open-source database engine.

In tandem, Google has been working towards [transitioning](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html) its own codebases to [memory-safe languages](https://research.google/pubs/secure-by-design-googles-perspective-on-memory-safety/) such as Rust, while also retrofitting mechanisms to address spatial memory safety vulnerabilities – which occur when it's possible for a piece of code to access memory that's outside of its intended bounds – within existing C++ projects, including Chrome.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This includes migrating to [Safe Buffers](https://clang.llvm.org/docs/SafeBuffers.html) and enabling [hardened libc++](https://libcxx.llvm.org/Hardening.html), the latter of which adds bounds checking to standard C++ data structures in order to eliminate a significant class of spatial safety bugs. It further noted that the overhead incurred as a result of incorporating the change is minimal (i.e., an average 0.30% performance impact).

"Hardened libc++, recently added by open source contributors, introduces a set of security checks designed to catch vulnerabilities such as out-of-bounds accesses in production," Google [said](https://security.googleblog.com/2024/11/retrofitting-spatial-safety-to-hundreds.html). "While C++ will not become fully memory-safe, these improvements reduce risk [...], leading to more reliable and secure software."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cryptography](https://thehackernews.com/search/label/cryptography)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Fuzzing](https://thehackernews.com/search/label/Fuzzing)[Google](https://thehackernews.com/search/label/Google)[Open Source](https://thehackernews.com/search/label/Open%20Source)[OpenSSL](https://thehackernews.com/search/label/OpenSSL)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![...