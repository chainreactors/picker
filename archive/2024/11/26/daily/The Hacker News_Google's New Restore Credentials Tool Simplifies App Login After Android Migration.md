---
title: Google's New Restore Credentials Tool Simplifies App Login After Android Migration
url: https://thehackernews.com/2024/11/googles-new-restore-credentials-tool.html
source: The Hacker News
date: 2024-11-26
fetch_date: 2025-10-06T19:26:19.385791
---

# Google's New Restore Credentials Tool Simplifies App Login After Android Migration

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

# [Google's New Restore Credentials Tool Simplifies App Login After Android Migration](https://thehackernews.com/2024/11/googles-new-restore-credentials-tool.html)

**Nov 25, 2024**Ravie LakshmananMobile Security / Privacy

[![Restore Credentials Tool](data:image/png;base64... "Restore Credentials Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-uFCqNx0ZsL6LBbZog-bUN0RKNnN5OSaItuPHNia44yul-Oz0pt2aQEl104b35emljYKwOTWfCOFVd9cr8Ip-I8J4O7eWo_djlRBJTEGhEWLIS-zbHxn6gMEnsY82mkxe397g5B56Qt8uzPtgB5MK70A8iMJG7gDV0p3kG33dYwxaIW1fDutvD7StoWPe/s790-rw-e365/android.png)

Google has introduced a new feature called **Restore Credentials** to help users restore their account access to third-party apps securely after migrating to a new Android device.

Part of Android's [Credential Manager API](https://developers.google.com/identity/android-credential-manager), the feature aims to reduce the hassle of re-entering the login credentials for every app during the handset replacement.

"With Restore Credentials, apps can seamlessly onboard users to their accounts on a new device after they restore their apps and data from their previous device," Google's Neelansh Sahai [said](https://android-developers.googleblog.com/2024/11/maintain-strong-user-relationships-with-restore-credentials.html).

The tech giant said the process occurs automatically in the background when a user restores apps and data from a previous device, enabling apps to sign users back into the respective accounts without requiring any additional interaction.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This is accomplished by means of what's called a restore key, which, in reality, is a public key that's compatible with FIDO2 standards such as passkeys.

Thus when a user signs in to an app that supports this feature, their restore key is saved to the Credential Manager locally on device and in encrypted format. Optionally, the encrypted restore key can also be saved to the cloud if cloud backup is enabled.

Should they transition to a new phone and restore their apps, the restore keys are requested as part of the process, allowing them to automatically sign in to their account without having to re-enter their login information.

"If the current signed-in user is trusted, you can generate a restore key at any point after they've authenticated in your app," Google instructs app developers. "For instance, this could be immediately after login or during a routine check for an existing restore key."

App developers are also recommended to delete the associated restore key as soon as the user signs out to avoid them getting stuck in a never-ending loop of signing out intentionally and automatically getting logged back in.

[![Restore Credentials Tool](data:image/png;base64... "Restore Credentials Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0Ad-o1GrzGKG4faF2e91XgMOcy2J0AXHqftTgUfJQcxwaXSydSKRir3-NCr0iSSW8Yk2NnJz1k-9emvPhpxsZR7sQgCWv0-KEK6jhpv6ptY31jTpi1De5ePobaNbk9OfTZq4QHqBhzCpKTjlwBWgmGQNv6ATmNP86D4dGHGRNBY-5R1csDpKVAQS2Qhgu/s790-rw-e365/android.png)

It's worth noting that Apple already has a similar feature in iOS that leverages an attribute called kSecAttrAccessible to control an app's access to a specific credential stored in the iCloud Keychain.

"The kSecAttrAccessible attribute enables you to control item availability relative to the lock state of the device," Apple [notes](https://developer.apple.com/documentation/security/restricting-keychain-item-accessibility) in its documentation.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"It also lets you specify eligibility for restoration to a new device. If the attribute ends with the string ThisDeviceOnly, the item can be restored to the same device that created a backup, but it isn't migrated when restoring another device's backup data."

The development comes as Google [shipped](https://android-developers.googleblog.com/2024/11/the-first-developer-preview-android16.html) the first Developer Preview of Android 16 with the latest version of the [Privacy Sandbox on Android](https://thehackernews.com/2023/02/google-rolling-out-privacy-sandbox-beta.html) and an improved [Privacy Dashboard](https://www.android.com/safety/privacy/#safety-privacy-dashboard) that adds the ability to view which apps have accessed sensitive permissions over a seven-day period.

This also follows the [release](https://www.androidenterprise.community/t5/news-info/read-this-year-s-2024-android-security-paper/ba-p/9026) of the updated Android Security Paper, which delves into the operating system's suite of built-in security capabilities, including features like [theft protection, private space](https://thehackernews.com/2024/05/google-adds-ai-powered-theft-protection.html), [sanitizers](https://thehackernews.com/2023/12/google-using-clang-sanitizers-to.html), and lockdown mode, which aims to restrict access to a device by turning off Smart Lock, biometric unlocking, and notifications on the lock screen.

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

[Android](https://thehackernews.com/search/label/Android)[Authentication](h...