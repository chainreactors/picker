---
title: Google’s AI ‘Big Sleep’ Finds 5 New Vulnerabilities in Apple’s Safari WebKit
url: https://thehackernews.com/2025/11/googles-ai-big-sleep-finds-5-new.html
source: The Hacker News
date: 2025-11-04
fetch_date: 2025-11-05T03:12:48.032795
---

# Google’s AI ‘Big Sleep’ Finds 5 New Vulnerabilities in Apple’s Safari WebKit

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

# [Google's AI 'Big Sleep' Finds 5 New Vulnerabilities in Apple's Safari WebKit](https://thehackernews.com/2025/11/googles-ai-big-sleep-finds-5-new.html)

**Nov 04, 2025**Ravie LakshmananArtificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO90ZGqS1o8oXuQSYe44zmCBkNPE4eZDZy-NJhnRyFZ_ePcN4Tv-OOIuBKoi5Dnp0bN_HpCcxpAgMNYs6t0rCntWspx1JNRJSBbMsvzxDnSXewOvLDls6VU47KVeRxxDO4fHBO7_Ow6P9T3crzMpcwQxBofwQLcX0WKBIQYsHY64MDoazdGW_9ehXK7sXv/s790-rw-e365/safari-flaw-ai.jpg)

Google's artificial intelligence (AI)-powered cybersecurity agent called **Big Sleep** has been credited by Apple for discovering as many as five different security flaws in the WebKit component used in its Safari web browser that, if successfully exploited, could result in a browser crash or memory corruption.

The list of vulnerabilities is as follows -

* **CVE-2025-43429** - A buffer overflow vulnerability that may lead to an unexpected process crash when processing maliciously crafted web content (addressed through improved bounds checking)
* **CVE-2025-43430** - An unspecified vulnerability that could result in an unexpected process crash when processing maliciously crafted web content (addressed through improved state management)
* **CVE-2025-43431 & CVE-2025-43433** - Two unspecified vulnerabilities that may lead to memory corruption when processing maliciously crafted web content (addressed through improved memory handling)
* **CVE-2025-43434** - A use-after-free vulnerability that may lead to an unexpected Safari crash when processing maliciously crafted web content (addressed through improved state management)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Patches for the shortcomings were released by Apple on Monday as part of iOS 26.1, iPadOS 26.1, macOS Tahoe 26.1, tvOS 26.1, watchOS 26.1, visionOS 26.1, and Safari 26.1. The updates are available for the following devices and operating systems -

* **[iOS 26.1 and iPadOS 26.1](https://support.apple.com/en-us/125632)** - iPhone 11 and later, iPad Pro 12.9-inch 3rd generation and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd generation and later, iPad 8th generation and later, and iPad mini 5th generation and later
* **[macOS Tahoe 26.1](https://support.apple.com/en-us/125634)** - Macs running macOS Tahoe
* **[tvOS 26.1](https://support.apple.com/en-us/125637)** - Apple TV 4K (2nd generation and later)
* **[visionOS 26.1](https://support.apple.com/en-us/125638)** - Apple Vision Pro (all models)
* **[watchOS 26.1](https://support.apple.com/en-us/125639)** - Apple Watch Series 6 and later
* **[Safari 26.1](https://support.apple.com/en-us/125640)** - Macs running macOS Sonoma and macOS Sequoia

Big Sleep, formerly called Project Naptime, is an AI agent [launched](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html) by Google last year as part of a collaboration between DeepMind and Google Project Zero to enable automated vulnerability discovery.

Earlier this year, Google [said](https://thehackernews.com/2025/07/google-ai-big-sleep-stops-exploitation.html) the large language model (LLM)-assisted framework identified a security flaw in SQLite (CVE-2025-6965, CVSS score: 7.2) that it said was at "risk of being exploited" by malicious actors.

While none of the vulnerabilities listed in Monday's security bulletins have been flagged as exploited in the wild, it's always a good practice to keep devices updated to the latest version for optimal protection.

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

[Apple](https://thehackernews.com/search/label/Apple)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[browser security](https://thehackernews.com/search/label/browser%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Google](https://thehackernews.com/search/label/Google)[MacOS](https://thehackernews.com/search/label/MacOS)[Safari](https://thehackernews.com/search/label/Safari)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[WebKit](https://thehackernews.com/search/label/WebKit)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](https://thehackernews.com/2025/10/weekly-recap-wsus-exploited-lockbit-50.html)

[![ThreatsDay Bulletin: $176M Crypto Fine, Hacking Formula 1, Chromium Vulns, AI Hijack and More](data:image/svg+xml;base64... "ThreatsDay Bulletin: $176M Crypto Fine, Hacking Formula 1, Chromium Vulns, AI Hijack and More")

ThreatsDay Bulletin: $176M Crypto Fine, Hacking Formula 1, Chromium Vulns, AI Hijack and More](https://thehackernews.com/2025/10/threatsday-bulletin-176m-crypto-fine.html)

[![New TEE.Fail Side-Channel Attack Extracts Secrets from Intel and AMD DDR5 Secure Enclaves](data:image/svg+xml;base64... "New TEE.Fail Side-...