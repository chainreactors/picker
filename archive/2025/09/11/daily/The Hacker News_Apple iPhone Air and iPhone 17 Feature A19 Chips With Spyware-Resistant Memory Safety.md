---
title: Apple iPhone Air and iPhone 17 Feature A19 Chips With Spyware-Resistant Memory Safety
url: https://thehackernews.com/2025/09/apple-iphone-air-and-iphone-17-feature.html
source: The Hacker News
date: 2025-09-11
fetch_date: 2025-10-02T20:00:51.474408
---

# Apple iPhone Air and iPhone 17 Feature A19 Chips With Spyware-Resistant Memory Safety

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

# [Apple iPhone Air and iPhone 17 Feature A19 Chips With Spyware-Resistant Memory Safety](https://thehackernews.com/2025/09/apple-iphone-air-and-iphone-17-feature.html)

**Sep 10, 2025**Ravie LakshmananSpyware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIc1QgZZdOOu9jQtxubJBFHmvw4qLx40ihiXPLh2OxNaah10hDEBugyyYCv1sjQKw8k-VKw6wGRWPZhclMXqjT2WDKUghP8iKJqAmjM2ytlLCPgtWSDONfGR8SFPPubQGwfBIH37pc2db46JzDHvJo_H6yH8KywjBPNNOidUwtJPc2urPlb61QyI8agqb2/s790-rw-e365/apple.jpg)

Apple on Tuesday revealed a new security feature called **Memory Integrity Enforcement** (MIE) that's built into its newly introduced iPhone models, including iPhone 17 and iPhone Air.

MIE, per the tech giant, offers "always-on memory safety protection" across critical attack surfaces such as the kernel and over 70 userland processes without sacrificing device performance by designing its A19 and A19 Pro chips keeping this aspect in mind.

"Memory Integrity Enforcement is built on the robust foundation provided by our secure memory allocators, coupled with Enhanced Memory Tagging Extension (EMTE) in synchronous mode, and supported by extensive Tag Confidentiality Enforcement policies," the company [noted](https://security.apple.com/blog/memory-integrity-enforcement/).

The effort is an aim to improve [memory safety](https://thehackernews.com/2024/09/googles-shift-to-rust-programming-cuts.html) and prevent bad actors, specifically those leveraging [mercenary spyware](https://thehackernews.com/2025/08/whatsapp-issues-emergency-update-for.html), from weaponizing such flaws in the first place to break into devices as part of highly-targeted attacks.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The technology that underpins MIE is EMTE, an improved version of the Memory Tagging Extension ([MTE](https://developer.arm.com/documentation/108035/0100/Introduction-to-the-Memory-Tagging-Extension)) specification released by chipmaker Arm in 2019 to flag memory corruption bugs either synchronously or asynchronously. EMTE was released by Arm in 2022 following a collaboration with Apple.

It's worth noting that Google's Pixel devices already have [support](https://developer.android.com/ndk/guides/arm-mte) for [MTE](https://source.android.com/docs/security/test/memory-safety/arm-mte) as a developer option starting with Android 13. Similar [memory integrity features](https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity?tabs=security) have also been introduced by Microsoft in Windows 11.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEXLULazhS1HqcscpINLblaEOovBcwt_oLeRXypuRQ3zXv-Av_hg6urj0A2XkYoLCqkRuyxnuG3rStBsbuH1sBAjnD5FPPQhHVqryYTYk1ocDIhxgT3iznL4KTLAZUQ4GrovKXCIpGKvh0WtltZbh9LMvI-C3GLy7K-WpOzmVRbn4jsSvO_BhVpeGNJEMZ/s790-rw-e365/apple-1.png) |
| How MIE blocks use-after-free access |

"The ability of MTE to detect memory corruption exploitation at the first dangerous access is a significant improvement in diagnostic and potential security effectiveness," Google Project Zero researcher Mark Brand [said](https://googleprojectzero.blogspot.com/2023/11/first-handset-with-mte-on-market.html) in October 2023, coinciding with the release of Pixel 8 and Pixel 8 Pro.

"The availability of MTE on a production handset for the first time is a big step forward, and I think there's real potential to use this technology to make 0-day harder."

Apple said MIE transforms MTE from a "helpful debugging tool" into a groundbreaking new security feature, offering security protection against two common vulnerability classes – buffer overflows and use-after-free bugs – that could result in memory corruption.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUPz593dsiIF2cC6JcZRfmKlj50anZuwf7ZoEtIHW6gN9_567xlkjTg5IZQr_Sw5Sd6IeA5NCAbjbrm73c19sldk72c3dfUd_RihPDIfMcK6NTGbR_kr3_YNtrvQ3xZQmuGUj8GIf0gukuW86hpCac4zM7O4jGCp6oyvF6ayQu7-9zcdqCc7JiNaNEtyWG/s790-rw-e365/apple-2.png) |
| How MIE blocks buffer overflows |

This essentially involves blocking out-of-bounds requests to access adjacent memory that has a different tag, and retagging memory as it gets reused for other purposes after it has been freed and reallocated by the system. As a result, requests to access retagged memory with an older tag (indicating use-after-free scenarios) also get blocked.

"A key weakness of the original MTE specification is that access to non-tagged memory, such as global variables, is not checked by the hardware," Apple explained. "This means attackers don't have to face as many defensive constraints when attempting to control core application configuration and state."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"With Enhanced MTE, we instead specify that accessing non-tagged memory from a tagged memory region requires knowing that region's tag, making it significantly harder for attackers to turn out-of-bounds bugs in dynamic tagged memory into a way to sidestep EMTE by directly modifying non-tagged allocations."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwW5qctiPHNfZXcoPe-ONVeSxZYa5UPZulEov5WtW9nLEtmv5YaF5pSRLn1_rGhhDEM_ZdSz5isrW6PsoEkI_IoDs5pH1_7vgluZjsdgBVwJGBkjPV3PBph9tRZhz1AfVVN2_IH_FjLMrO0_OV-Go3NUspxoPlKfolYpBerKIAdbOUUUeXatJwvRIijXxS/s2600/crash.jpg) |
| Enabling MTE on Google Pixel |

Cupertino said it has also developed what it calls Tag Confidentiality Enforcement (TCE) to secure the implementation of memory allocators against side-channel and [speculative execution attacks](https://thehackernews.com/2022/06/mit-researchers-discover-new-flaw-in.html) like [TikTag](https://thehackernews.com/2024/07/new-intel-cpu-vulnerability-indirector.html) that MTE was found susceptible to last year, resulting in th...