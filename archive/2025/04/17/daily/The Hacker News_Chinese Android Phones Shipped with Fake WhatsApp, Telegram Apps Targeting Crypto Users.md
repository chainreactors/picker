---
title: Chinese Android Phones Shipped with Fake WhatsApp, Telegram Apps Targeting Crypto Users
url: https://thehackernews.com/2025/04/chinese-android-phones-shipped-with.html
source: The Hacker News
date: 2025-04-17
fetch_date: 2025-10-06T22:09:31.318170
---

# Chinese Android Phones Shipped with Fake WhatsApp, Telegram Apps Targeting Crypto Users

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

# [Chinese Android Phones Shipped with Fake WhatsApp, Telegram Apps Targeting Crypto Users](https://thehackernews.com/2025/04/chinese-android-phones-shipped-with.html)

**Apr 16, 2025**Ravie LakshmananMobile Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtNuuZYXAvYPgIecCXIp1qr9xMXs237jxdN3YwEI7A183PGKbbwxqgZClGptneLRJy_k5n8XDW0B2uvnoGsU3wKGdJPCHv5pJSTZqN93W-GzjwRk9u03Nh5fn4NaNi2lC5jfDyePnbGwON7sXm-0i8zG0VBKUFVZaFnJiP1sjtS7jeDZR21-sf5xFrHq9t/s790-rw-e365/malware-android.jpg)

Cheap Android smartphones manufactured by Chinese companies have been observed pre-installed with trojanized apps masquerading as WhatsApp and Telegram that contain cryptocurrency [clipper functionality](https://thehackernews.com/2024/09/binance-warns-of-rising-clipper-malware.html) as part of a campaign since June 2024.

While using malware-laced apps to steal financial information is not a new phenomenon, the new findings from Russian antivirus vendor Doctor Web point to significant escalation where threat actors are directly [targeting the supply chain](https://thehackernews.com/2025/04/triada-malware-preloaded-on-counterfeit.html) of various Chinese manufacturers to preload brand new devices with malicious apps.

"Fraudulent applications were detected directly in the software pre-installed on the phone," the company [said](https://news.drweb.com/show/?lng=en&i=15002&c=5). "In this case, the malicious code was added to the WhatsApp messenger."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A majority of the compromised devices are said to be low-end phones that mimic well-known premium models from Samsung and Huawei with names like S23 Ultra, S24 Ultra, Note 13 Pro, and P70 Ultra. At least four of the affected models are manufactured under the **SHOWJI** brand.

The attackers are said to have used an application to spoof the technical specification displayed on the About Device page, as well as hardware and software information utilities like AIDA64 and CPU-Z, giving users a false impression that the phones are running Android 14 and have improved hardware.

The malicious Android apps are created using an open-source project called [LSPatch](https://github.com/LSPosed/LSPatch) that allows the trojan, dubbed Shibai, to be injected into otherwise legitimate software. In total, about 40 different applications, like messengers and QR code scanners, are estimated to have been modified in this manner.

In the artifacts analyzed by Doctor Web, the application hijacks the app update process to retrieve an APK file from a server under the attacker's control and searches for strings in chat conversations that match cryptocurrency wallet address patterns associated with Ethereum or Tron. If found, they are replaced with the adversary's addresses to reroute transactions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFk_O8uNsMl5nHBB1jvbML-KI2tw0ZAiBT6UxaH_ONimpqJUVNAh8dyEbTGuHLePBEOQz48PThlU5mpx6pOJM-gtB5l0W93MYfaP5gGASGRBJMZc14fghZEF3Q_Au1djO0RzUJEJz8G2ILvI3QnbXykOOhFpyknU5ZdmQ-2hL2s7NvKGf_NiUy8IMOBGFR/s790-rw-e365/phones.jpg)

"In the case of an outgoing message, the compromised device displays the correct address of the victim's own wallet, while the recipient of the message is shown the address of the fraudsters' wallet," Doctor Web said.

"And when an incoming message is received, the sender sees the address of their own wallet; meanwhile, on the victim's device, the incoming address is replaced with the address of the hackers' wallet."

Besides changing the wallet addresses, the malware is also fitted with capabilities to harvest device information, all WhatsApp messages, and .jpg, .png, and .jpeg images from DCIM, Pictures, Alarms, Downloads, Documents, and Screenshots folders to the attacker's server.

The intention behind this step is to scan the stored images for wallet recovery (aka mnemonic) phrases, allowing the threat actors to gain unauthorized access to victims' wallets and drain the assets.

It's not clear who is behind the campaign, although the attackers have been found to leverage about 30 domains to distribute the malicious applications and employ more than 60 command-and-control (C2) servers to manage the operation.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Further analysis of the nearly two dozen cryptocurrency wallets used by the threat actors has revealed that they have received more than $1.6 million over the last two years, indicating that the supply chain compromise has paid off in a big way.

The development comes as Swiss cybersecurity company PRODAFT uncovered a new Android malware family dubbed Gorilla that's designed to collect sensitive information (e.g., device model, phone numbers, Android version, SIM card details, and installed apps), main persistent access to infected devices, and receive commands from a remote server.

"Written in Kotlin, it primarily focuses on SMS interception and persistent communication with its command-and-control (C2) server," the company [said](https://catalyst.prodaft.com/public/report/gorilla/overview) in an analysis. "Unlike many advanced malware strains, Gorilla does not yet employ obfuscation techniques, indicating that it may still be under active development."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMsiquKcn1V4MDeJp4p4Zod6PDkVTboew6PwgYopxHsFg90Bxd-UQ52UxPD6FgUZHnexZcv_9ekhiIlh5KEKvfB-GUB5KLZO89hajPmPllCTm61zn1ioXBW4YNAnPnq6oXCN6f0lSrBC4KwK4PvyZ9KsSFNa0ZsAE9GlUMg0X3xJ3jQzO0ZpBFZCQ_1CsB/s790-rw-e365/go.png)

In recent months, Android apps embedding the [FakeApp](https://thehackernews.com/2023/11/malicious-apps-disguised-as-banks-and.html) [trojan](https://www.broadcom.com/support/security-center/protection-bulletin/fakeapp-campaign-south-korea-s-financial-institutions-mobile-users-targeted) propagated via Google Play Store have also bee...