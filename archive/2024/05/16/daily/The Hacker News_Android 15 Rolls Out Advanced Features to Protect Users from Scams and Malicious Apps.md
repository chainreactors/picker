---
title: Android 15 Rolls Out Advanced Features to Protect Users from Scams and Malicious Apps
url: https://thehackernews.com/2024/05/android-15-introduces-new-features-to.html
source: The Hacker News
date: 2024-05-16
fetch_date: 2025-10-06T17:17:58.372847
---

# Android 15 Rolls Out Advanced Features to Protect Users from Scams and Malicious Apps

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

# [Android 15 Rolls Out Advanced Features to Protect Users from Scams and Malicious Apps](https://thehackernews.com/2024/05/android-15-introduces-new-features-to.html)

**May 15, 2024**Ravie LakshmananAndroid Security / Malware

[![Android 15](data:image/png;base64... "Android 15")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjzmzJIldOiZh2c4S9W_dAr7OIpkKAYlProKSmMCr0WI30vVIfl9ynDpMLu9_Z-Fr9kIEV0rvm7TZOotA5d79_htMnvCLYW12I_enFTHhlAEfqNnk5_hAaNp6hGqGdr9dIxSX2hVKZcQVuGFb-ajdN_k1pN1VwtZ_ywDtPJnll3oM_dSdz1JXVkdk__agp/s790-rw-e365/malware.png)

Google is unveiling a set of new features in Android 15 to prevent malicious apps installed on the device from capturing sensitive data.

This constitutes an update to the [Play Integrity API](https://developer.android.com/google/play/integrity/overview) that third-party app developers can take advantage of to secure their applications against malware.

"Developers can check if there are other apps running that could be capturing the screen, creating overlays, or controlling the device," Dave Kleidermacher, vice president of engineering for Android security and privacy, [said](https://security.googleblog.com/2024/05/io-2024-whats-new-in-android-security.html).

"This is helpful for apps that want to hide sensitive information from other apps and protect users from scams."

Additionally, the Play Integrity API can be used to check if [Google Play Protect](https://support.google.com/googleplay/answer/2812853?hl=en) is active and if the user's device is free of known malware before performing sensitive actions or handling sensitive data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Google, with Android 13, introduced a feature called [restricted settings](https://support.google.com/android/answer/12623953?hl=en) that by default blocks sideloaded apps from accessing notifications and requesting accessibility services permissions.

In the latest iteration of the mobile operating system, the feature is being expanded by seeking user approval prior to enabling permissions when installing an app via sideloading from web browsers, messaging apps, and file managers.

"Developers can also opt-in to receive recent device activity to check if a device is making too many integrity checks, which could be a sign of an attack," Kleidermacher added.

The changes are squarely aimed at Android banking trojans that are [known](https://thehackernews.com/2021/04/brata-malware-poses-as-android-security.html) to [abuse](https://thehackernews.com/2022/07/over-dozen-android-apps-on-google-play.html) their permissions to the accessibility services API to perform overlay attacks and [turn off security mechanisms](https://thehackernews.com/2024/05/malicious-android-apps-pose-as-google.html) on the device to harvest valuable data.

That said, Android malware such as [Anatsa](https://thehackernews.com/2024/02/anatsa-android-trojan-bypasses-google.html) has been observed [circumventing](https://www.kaspersky.com/blog/android-restricted-settings/49991/) [restricted settings](https://thehackernews.com/2023/11/securidropper-new-android-dropper-as.html) in recent months, indicating continued efforts on the part of threat actors to devise ways to breach security guardrails.

"We're continuously working on improving and evolving our protections to stay ahead of bad actors," a Google spokesperson told The Hacker News.

"We recently began piloting enhanced fraud protection with Google Play Protect, in countries where internet-sideloaded malicious app installs are prevalent. Enhanced fraud protection will block installs from Internet-sideloaded sources (messaging apps, websites, file managers), that use permissions commonly abused for financial fraud. This pilot is live in Singapore and Thailand."

Alongside efforts to combat fraud and scams, Google is also stepping up cellular security by alerting users if their cellular network connection is unencrypted and if a bogus cellular base station or surveillance tool (e.g., [stingrays](https://thehackernews.com/2023/08/new-android-14-security-feature-it.html)) is recording their location using a device identifier.

The tech giant said it's working closely with ecosystem partners, including original equipment manufacturers (OEMs), to enable these features to users over the next couple of years.

That's not all. The company is tightening controls for screen sharing in Android 15 by automatically hiding notification content, thus preventing one-time passwords (OTPs) sent via SMS messages from being displayed during screen sharing.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"With the exception of a few types of apps, such as wearable companion apps, one-time passwords are now hidden from notifications, closing a common attack vector for fraud and spyware," Kleidermacher said.

Rounding off the new fraud and scam protection features, Google said it's diversifying Play Protect's on-device AI capabilities with live threat detection to better identify malicious apps. The approach leverages the Private Compute Core ([PCC](https://security.googleblog.com/2022/12/trust-in-transparency-private-compute.html)) infrastructure to flag anomalous patterns on the device.

"With live threat detection, Google Play Protect's on-device AI will analyze additional behavioral signals related to the use of sensitive permissions and interactions with other apps and services," Kleidermacher said.

"If suspicious behavior is discovered, Google Play Protect can send the app to Google for additional review and then warn users or disable the app if malicious behavior is confirmed."

Live threat detection also builds on a [recently added capability](https://thehackernews.com/2023/10/google-play-protect-introduces-real.html) that allows for real-time scanning at the code-level to combat novel malicious apps and help spot emerging threats.

Found this article interesting? Follow us on [Google News](https://n...