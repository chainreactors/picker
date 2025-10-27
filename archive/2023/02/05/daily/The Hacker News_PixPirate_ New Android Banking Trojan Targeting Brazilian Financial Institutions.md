---
title: PixPirate: New Android Banking Trojan Targeting Brazilian Financial Institutions
url: https://thehackernews.com/2023/02/pixpirate-new-android-banking-trojan.html
source: The Hacker News
date: 2023-02-05
fetch_date: 2025-10-04T05:46:29.951987
---

# PixPirate: New Android Banking Trojan Targeting Brazilian Financial Institutions

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

# [PixPirate: New Android Banking Trojan Targeting Brazilian Financial Institutions](https://thehackernews.com/2023/02/pixpirate-new-android-banking-trojan.html)

**Feb 04, 2023**Ravie LakshmananMobile Security / Malware

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_JG18prqhBeNCMKDPprIDbtCWW78AfFkj0z81cW7BNQClIPsmtU_jPjXTbIruLJKrzXAJoW6xoqnlxZexsBLP75SlcOzLr6TI0JQRu5VCMR0jWjZKwdVS_YDlNMKEheyHLJQzrzzBtBxgm7XEP-JxHQdibXtmXs01MWfMF6NjUSu2rbRgwpkQMKcd/s790-rw-e365/android-malware.png)

A new Android banking trojan has set its eyes on Brazilian financial institutions to commit fraud by leveraging the PIX payments platform.

Italian cybersecurity company Cleafy, which discovered the malware between the end of 2022 and the beginning of 2023, is tracking it under the name PixPirate.

"PixPirate belongs to the newest generation of Android banking trojan, as it can perform [ATS](https://www.cleafy.com/documents/how-ats-attacks-work-infographic) ([Automatic Transfer System](https://www.malwaretech.com/2016/08/automatic-transfer-systems-ats-for-beginners.html)), enabling attackers to automate the insertion of a malicious money transfer over the instant payment platform PIX, adopted by multiple Brazilian banks," researchers Francesco Iubatti and Alessandro Strino [said](https://www.cleafy.com/cleafy-labs/pixpirate-a-new-brazilian-banking-trojan).

It is also the latest addition in a long list of Android banking malware to abuse the operating system's accessibility services API to carry out its nefarious functions, including disabling Google Play Protect, intercepting SMS messages, preventing uninstallation, and serving rogue ads via push notifications.

Besides stealing passwords entered by users on banking apps, the threat actors behind the operation have leveraged code obfuscation and encryption using a framework known as Auto.js to resist reverse engineering efforts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The dropper apps used to deliver PixPirate come under the garb of authenticator apps. There are no indications that the apps were published to the official Google Play Store.

The findings come more than a month after ThreatFabric disclosed details of another malware called [BrasDex](https://thehackernews.com/2022/12/beware-cybercriminals-launch-new.html) that also comes with ATS capabilities, in addition to abusing PIX to make fraudulent fund transfers.

"The introduction of ATS capabilities paired with frameworks that will help the development of mobile applications, using flexible and more widespread languages (lowering the learning curve and development time), could lead to more sophisticated malware that, in the future, could be compared with their workstation counterparts," the researchers said.

The development also comes as Cyble shed light on a new Android remote access trojan codenamed Gigabud RAT targeting users in Thailand, Peru, and the Philippines since at least July 2022 by masquerading as bank and government apps.

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXzzbKWA4wlaXQqrgY8aBQIaQNf0rBWI8lelY_RTNJ1JeUkvp2qOXapvEiagjYzlan5EjS5e4wSk6_HLtMGcJP3aakqOS5vOhw3edPUoc91ZBo__W2zRfU7C73Z_6K7NkCRhurnQuvHqAhdEjhFlD-X4Uhu0VsGps7XT0iGyw6vlB3OSZkI3oBr2l9/s790-rw-e365/malware.png)

"The RAT has advanced features such as screen recording and abusing the accessibility services to steal banking credentials," the researchers [said](https://blog.cyble.com/2023/01/19/gigabud-rat-new-android-rat-masquerading-as-government-agencies/), noting its use of phishing sites as a distribution vector.

The cybersecurity firm further [revealed](https://blog.cyble.com/2023/01/31/inthebox-web-injects-targeting-android-banking-applications-worldwide/) that the threat actors behind the [InTheBox darknet marketplace](https://thehackernews.com/2022/12/darknets-largest-mobile-malware.html) are advertising a catalog of 1,894 web injects that are compatible with various Android banking malware such as Alien, Cerberus, ERMAC, Hydra, and Octo.

The web inject modules, mainly used for harvesting credentials and sensitive data, are designed to single out banking, mobile payment services, cryptocurrency exchanges, and mobile e-commerce applications spanning Asia, Europe, Middle East, and the Americas.

But in a more concerning twist, fraudulent apps have found a way to bypass defenses in Apple App Store and Google Play to perpetrate what's called a pig butchering scam known as [CryptoRom](https://thehackernews.com/2022/03/cryptorom-crypto-scam-abusing-iphone.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The technique entails employing social engineering methods such as approaching victims through dating apps like Tinder to entice them into downloading fraudulent investment apps with the goal of stealing their money.

The malicious iOS apps in question are Ace Pro and MBM\_BitScan, both of which have since been removed by Apple. An Android version of MBM\_BitScan has also been taken down by Google.

Cybersecurity firm Sophos, which made the discovery, said the iOS apps featured a "review evasion technique" that enabled the malware authors to get past the vetting process.

"Both the apps we found used remote content to provide their malicious functionality -- content that was likely concealed until after the App Store review was complete," Sophos researcher Jagadeesh Chandraiah [said](https://news.sophos.com/en-us/2023/02/01/fraudulent-cryptorom-trading-apps-sneak-into-apple-and-google-app-stores/).

Pig butchering scams had their beginnings in China and Taiwan, and has since expanded globally in recent years, with a [huge chunk of operations](https://www.vice.com/en/article/n7zb5d/pig-butchering-scam-cambodia-trafficking) carried out from special economic zones in Laos, ...