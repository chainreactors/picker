---
title: Android 17 Adds OS-Wide ECH to Hide Website Visits From Network Providers
url: https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:11.880371
---

# Android 17 Adds OS-Wide ECH to Hide Website Visits From Network Providers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Android 17 Adds OS-Wide ECH to Hide Website Visits From Network Providers](https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html)

**Ravie Lakshmanan**Aug 28, 2026Cellular Security / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHdeGqGafTZXNtGvV_-qR7K3QId_-DpEfOzetKbhVQvNdNyTMAy-6gLXVFlkMHsGDN2wKK8v1ZMeOKe9_3XVYAY5TVkqH2heesi0c_QmJzLpDX1M-XfOtI_W4Qe8OM8Yhin40QWvN0XHvU9cqDlZH3eeZY_18euIxiBdcbhWMVnXct-x84k2gvchQYSiuN/s1700-e365/1000103901.jpg)

Google on Thursday announced new network security protections in Android 17 to bolster connection privacy, address cellular vulnerabilities, and safeguard the privacy of users' home networks.

Topping the list is [support](https://developer.android.com/about/versions/17/features#ech-platform-support) for Encrypted Client Hello ([ECH](https://blog.cloudflare.com/announcing-encrypted-client-hello/)), a privacy standard that prevents networks from eavesdropping on which websites a user is visiting.

"This new privacy standard works in tandem with private DNS to obscure the domain names you visit, hiding metadata that can be used to profile you," Google's Bram Bonné and Shuaibo Huang [said](https://blog.google/security/new-Android-network-security-protections/). "By encrypting the destination website name from the very start, ECH helps ensure that, for supported websites and apps, network providers and network snoopers can no longer easily see which websites or apps you are accessing."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

In a parallel report detailing the integration, Google's Jigsaw division said ECH hides the domain name using a secret encryption key that only the destination website can decipher.

"Critically, though, not all web servers will offer ECH support," Jigsaw [said](https://medium.com/jigsaw/closing-a-critical-internet-privacy-gap-for-billions-of-users-android-17-rolls-out-ech-support-c52b49a62c04). "To avoid exposing only certain connections as ECH-protected, apps and browsers should use ECH GREASE — which sends fake, randomized ECH extensions to sites that don't support ECH — so that every connection request looks the same."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuK_DE_NtqT3_L40Exbf_lxX4p0-5DCiquVpt9uTIdK9ZoZSObrriyvQaeh01qeRWkS6PnPH6NNp7TrVFS6SXnRelrWuJhr0FmcIcgxcxN0vxw5WpLT3CjiqNokRyotmQrWy-mYFT4e_xlfiN1y21lmkwUlBF9HpgEc2uDvDMX-ucoo5o4vI5d-_3bFeNq/s1700-e365/1000103904.jpg)

With Android 17, ECH GREASE will be enabled by default. It's worth noting that ECH was integrated into Google Chrome and Mozilla Firefox with [versions 117](https://chromestatus.com/feature/6196703843581952) and [118](https://blog.mozilla.org/en/firefox/encrypted-hello/), respectively. However, with the latest update, the protection expands to the entire operating system.

Jigsaw also said OkHttp, an open-source HTTP and HTTP/2 client, has integrated ECH support into its core library, allowing third-party Android app developers to leverage the new capability.

In addition to support for ECH on Android, Google has enforced [Local Network Protection](https://developer.android.com/privacy-and-security/local-network-permission), requiring apps to ask for users' permission before they can scan or connect to other devices on their local network.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Two other privacy- and security-oriented features include enabling Certificate Transparency ([CT](https://thehackernews.com/2026/03/google-develops-merkle-tree.html)) by default, which mandates that all websites be logged in a public registry, and allowing telecom operators to turn off 2G by default for their subscribers to prevent downgrade attacks and mitigate exposure to rogue base stations or SMS blasters that can send malicious text messages or capture traffic from nearby devices.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9PcUq4QN6rBHU3lBratufnpLsijCrJEE3SZ-gqzinNTUR2GmdUzh0VlwSXBewOJ2z89M8qlVSCim6lMHZGaW6Is8cI1r5Ag6-b1Hv-bHb3VwZ9X0-svAzLEq6QOfQu0ChyphenhyphengWGKHo_RTyqAbJw3usSDZeIJyvPtnQI5nSQMEyg1NCZPPfhXGWmdWJs81ov/s1700-e365/1000103905.jpg)

Android 12 already [includes](https://thehackernews.com/2023/08/new-android-14-security-feature-it.html) a manual option that allows users to disable 2G at the hardware level. With Android 14, Google [added](https://thehackernews.com/2024/10/android-14-adds-new-security-features.html) a security feature that allowed IT administrators to turn off support for 2G cellular networks in their managed devices. The latest offering, on the other hand, is a zero-click solution.

"For participating carriers, this helps eliminate the legacy attack surface out of the box, proactively mitigating a primary method used by SMS blasters before they can target your device," Google said.

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

[Android](https://thehackernews.com/search/label/Android), [mobile security](https://thehackernews.com/search/label/mobile%20security), [network security](https://th...