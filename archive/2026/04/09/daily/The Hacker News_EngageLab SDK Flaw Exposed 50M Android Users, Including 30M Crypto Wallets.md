---
title: EngageLab SDK Flaw Exposed 50M Android Users, Including 30M Crypto Wallets
url: https://thehackernews.com/2026/04/engagelab-sdk-flaw-exposed-50m-android.html
source: The Hacker News
date: 2026-04-09
fetch_date: 2026-04-10T04:47:46.307102
---

# EngageLab SDK Flaw Exposed 50M Android Users, Including 30M Crypto Wallets

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

# [EngageLab SDK Flaw Exposed 50M Android Users, Including 30M Crypto Wallets](https://thehackernews.com/2026/04/engagelab-sdk-flaw-exposed-50m-android.html)

**Ravie Lakshmanan**Apr 09, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigi73Eo-lmEoLh8BcTJmWW5GrmLrm49pUkkl8zyxIg1YTEncbgCaY-wXarkWZuipJhJEubcJx-VEiHOv_NrMtPw1BoEU3Ni8gXNcKcbWX4TqBU8pikOAkRdCl-r_XvLz4oXmQ2IpY25bWzLFkXh_hezhx0jgUYiuRvrYVxhW-6x5J7m84HH_VeRtRzTGbW/s1700-e365/vul-app.jpg)

Details have emerged about a now-patched security vulnerability in a widely used third-party Android software development kit (SDK) called [EngageLab SDK](https://www.engagelab.com/docs/essentials/developer-guide/client-sdk/android-sdk) that could have put millions of cryptocurrency wallet users at risk.

"This flaw allows apps on the same device to bypass Android security sandbox and gain unauthorized access to private data," the Microsoft Defender Security Research Team [said](https://www.microsoft.com/en-us/security/blog/2026/04/09/intent-redirection-vulnerability-third-party-sdk-android/) in a report published today.

EngageLab SDK offers a [push notification service](https://www.engagelab.com/app-push), which, according to its website, is designed to deliver "timely notifications" based on user behavior already tracked by developers. Once integrated into an app, the SDK offers a way to send personalized notifications and drive real-time engagement.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

The tech giant said a significant number of apps using the SDK are part of the cryptocurrency and digital wallet ecosystem, and that the affected wallet apps accounted for more than 30 million installations. When non‑wallet apps built on the same SDK are included, the installation count surpasses 50 million.

Microsoft did not reveal the names of the apps, but noted that all those detected apps using vulnerable versions of the SDK have been removed from the Google Play Store. Following responsible disclosure in April 2025, EngageLab released [version 5.2.1](https://mvnrepository.com/artifact/com.engagelab/engagelab/5.2.1) in November 2025 to address the vulnerability.

The issue, identified in version 4.5.4, has been described as an intent redirection vulnerability. Intents in Android refer to [messaging objects](https://developer.android.com/guide/components/intents-filters) that are used to request an action from another app component.

Intent redirection occurs when the contents of an intent that a vulnerable app sends are manipulated by taking advantage of its trusted context (i.e., permissions) to gain unauthorized access to protected components, expose sensitive data, or escalate privileges within the Android environment.

An attacker could exploit this vulnerability by means of a malicious app installed on the device through some other means to access internal directories associated with an app that has the SDK integrated, resulting in unauthorized access to sensitive data.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

There is no evidence that the vulnerability was ever exploited in a malicious context. That said, developers who integrate the SDK are recommended to update to the latest version as soon as possible, especially given that even trivial flaws in upstream libraries can have cascading impacts and impact millions of devices.

"This case shows how weaknesses in third‑party SDKs can have large‑scale security implications, especially in high‑value sectors like digital asset management," Microsoft said. "Apps increasingly rely on third‑party SDKs, creating large and often opaque supply‑chain dependencies. These risks increase when integrations expose exported components or rely on trust assumptions that aren’t validated across app boundaries."

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

[Android](https://thehackernews.com/search/label/Android), [cryptocurrency](https://thehackernews.com/search/label/cryptocurrency), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data protection](https://thehackernews.com/search/label/data%20protection), [Google Play](https://thehackernews.com/search/label/Google%20Play), [Microsoft](https://thehackernews.com/search/label/Microsoft), [mobile security](https://thehackernews.com/search/label/mobile%20security), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](data:image/svg+xml;base64... "Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass")

Microsoft Warns of WhatsApp-Delivered VBS Malware Hijacking Windows via UAC Bypass](https://thehackernews.com/2026/04/microsoft-warns-of-whatsapp-delivered.html)

[![New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](data:image/svg+xml;base64... "New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released")

New Chrome Zero-Day CVE-2026-5281 Under Active Exploitation — Patch Released](https://thehackernews.com/2026/04/new-chrome-zero-day-cve-2026-5281-under.html)

[![Apple Expands iOS 18.7.7 Update to More Devices to Block DarkSword Exploit](data:image/svg+xml;base64... "Apple Expands iOS 18.7.7 Update to ...