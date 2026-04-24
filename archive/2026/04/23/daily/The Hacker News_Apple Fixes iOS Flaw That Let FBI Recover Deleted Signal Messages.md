---
title: Apple Fixes iOS Flaw That Let FBI Recover Deleted Signal Messages
url: https://thehackernews.com/2026/04/apple-patches-ios-flaw-that-stored.html
source: The Hacker News
date: 2026-04-23
fetch_date: 2026-04-24T04:57:38.933645
---

# Apple Fixes iOS Flaw That Let FBI Recover Deleted Signal Messages

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

# [Apple Fixes iOS Flaw That Let FBI Recover Deleted Signal Messages](https://thehackernews.com/2026/04/apple-patches-ios-flaw-that-stored.html)

**Ravie Lakshmanan**Apr 23, 2026Vulnerability / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8iikjICH9h-OY06K3jZBcEcwtWEuusLcRgwG1T5SvE39V2ZfqSe7Z7N3NFXzfxgYicI_yo8bvme9f4RYazoU-5dUmoTKJMgdmW38AuWgFEWKNBTxgqQJAgpwZUOS926Ue1qCGUW7ou2wStgU-vRsle4Ky8pcp2I2mT_Sm3eyUw__JZaO-BrBZ80z3Zhvx/s1700-e365/apple-signal.jpg)

Apple has rolled out a software fix for iOS and iPadOS to address a Notification Services flaw that stored notifications marked for deletion on the device.

The vulnerability, tracked as CVE-2026-28950 (CVSS score: N/A), has been described as a logging issue that has been addressed with improved data redaction.

"Notifications marked for deletion could be unexpectedly retained on the device," Apple said in an advisory.

The shortcoming affects the following devices -

* iPhone 11 and later, iPad Pro 12.9-inch 3rd generation and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd generation and later, iPad 8th generation and later, and iPad mini 5th generation and later - Fixed in [iOS 26.4.2 and iPadOS 26.4.2](https://support.apple.com/en-us/127002)
* iPhone XR, iPhone XS, iPhone XS Max, iPhone 11 (all models), iPhone SE (2nd generation), iPhone 12 (all models), iPhone 13 (all models), iPhone SE (3rd generation), iPhone 14 (all models), iPhone 15 (all models), iPhone 16 (all models), iPhone 16e, iPad mini (5th generation - A17 Pro), iPad (7th generation - A16), iPad Air (3rd - 5th generation), iPad Air 11-inch (M2 - M3), iPad Air 13-inch (M2 - M3), iPad Pro 11-inch (1st generation - M4), iPad Pro 12.9-inch (3rd - 6th generation), and iPad Pro 13-inch (M4) - Fixed in [iOS 18.7.8 and iPadOS 18.7.8](https://support.apple.com/en-us/127003)

The update comes weeks after a report from 404 Media that the U.S. Federal Bureau of Investigation (FBI) [managed](https://thehackernews.com/2026/04/weekly-recap-fiber-optic-spying-windows.html#:~:text=FBI%20Extracts%20Signal%20Messages%20from%20iOS%20Notification%20History%20Database) to forensically extract copies of incoming Signal messages [from a defendant's iPhone](https://prairielanddefendants.com/court-notes/march-10-federal-trial-day-12/) in connection with an attack on the [Prairieland ICE detention center facility](https://www.justice.gov/opa/pr/antifa-cell-members-convicted-prairieland-ice-detention-center-shooting), even after the app was deleted, by taking advantage of the fact that copies of the content were saved in the device's push notification database.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agentic-guide-d-3)

It's not known why the notifications' content was logged in the device to begin with, but the latest update suggests it was a bug. That said, it's unclear when this issue was introduced, and if there have been prior cases where such data may have been captured by authorities using forensic tools.

While Signal already has an option to prevent the content of incoming messages from being displayed in notifications, the development highlighted how physical access to a device can facilitate the extraction of sensitive data from at-risk users.

"For most app notifications, there's no simple way to easily figure out what metadata might be gleaned from a notification, or if the notification is unencrypted or not," the Electronic Frontier Foundation (EFF) [said](https://www.eff.org/deeplinks/2026/04/how-push-notifications-can-betray-your-privacy-and-what-do-about-it). "It's also good to reconsider whether any app should be sending you notifications to begin with."

To prevent the message content from showing in notifications, users can [navigate](https://support.signal.org/hc/en-us/articles/360043273491-In-App-Notification-Options) to their profile > Notifications > Show, and select one of the following: "Name only" or "No name or message."

"Note that no action is needed for this fix to protect Signal users on iOS," Signal [said](https://x.com/signalapp/status/2047070518776356996) in a post on X. "Once you install the patch, all inadvertently-preserved notifications will be deleted, and no forthcoming notifications will be preserved for deleted applications."

"We're grateful to Apple for the quick action here, and for understanding and acting on the stakes of this kind of issue. It takes an ecosystem to preserve the fundamental human right to private communication."

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

[Apple](https://thehackernews.com/search/label/Apple), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data privacy](https://thehackernews.com/search/label/data%20privacy), [digital forensics](https://thehackernews.com/search/label/digital%20forensics), [encryption](https://thehackernews.com/search/label/encryption), [iOS](https://thehackernews.com/search/label/iOS), [iPadOS](https://thehackernews.com/search/label/iPadOS), [Signal](https://thehackernews.com/search/label/Signal), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.c...