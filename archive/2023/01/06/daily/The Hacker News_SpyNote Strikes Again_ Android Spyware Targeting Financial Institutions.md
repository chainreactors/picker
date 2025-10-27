---
title: SpyNote Strikes Again: Android Spyware Targeting Financial Institutions
url: https://thehackernews.com/2023/01/spynote-strikes-again-android-spyware.html
source: The Hacker News
date: 2023-01-06
fetch_date: 2025-10-04T03:12:26.708835
---

# SpyNote Strikes Again: Android Spyware Targeting Financial Institutions

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

# [SpyNote Strikes Again: Android Spyware Targeting Financial Institutions](https://thehackernews.com/2023/01/spynote-strikes-again-android-spyware.html)

**Jan 05, 2023**Ravie LakshmananMobile Security / Surveillance

[![Android Spyware](data:image/png;base64... "Android Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrESTZDw6SzXCdoJhvvALTqRep486PWRORdFSl4tlo7-daMTCo0sWmAos80ZFEfbu-H9pffXG49cQ1S_RD3RrBtZvnZzzvuHy9E8oWgfEGNY3V1oeik8P4Vdwqnc75DEGY8x-a2bDkbFfbWTbnJeCSUlm77L14AhUHkWBwE6E6l4TvtrEXO69ysKB9/s790-rw-e365/ANDROID-MALWARE.png)

Financial institutions are being targeted by a new version of Android malware called **SpyNote** at least since October 2022 that combines both spyware and banking trojan characteristics.

"The reason behind this increase is that the developer of the spyware, who was previously selling it to other actors, made the source code public," ThreatFabric [said](https://www.threatfabric.com/blogs/spynote-rat-targeting-financial-institutions.html) in a report shared with The Hacker News. "This has helped other actors [in] developing and distributing the spyware, often also targeting banking institutions."

Some of the notable institutions that are impersonated by the malware include Deutsche Bank, HSBC U.K., Kotak Mahindra Bank, and Nubank.

SpyNote (aka SpyMax) is feature-rich and comes with a plethora of capabilities that allows it to install arbitrary; gather SMS messages, calls, videos, and audio recordings; track GPS locations; and even hinder efforts to uninstall the app.

It also follows the modus operandi of other [banking](https://thehackernews.com/2022/12/beware-cybercriminals-launch-new.html) [malware](https://thehackernews.com/2022/12/godfather-android-banking-trojan.html) by requesting for permissions to accessibility services to extract two-factor authentication (2FA) codes from Google Authenticator and record keystrokes to siphon banking credentials.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In addition, SpyNote packs in functionalities to plunder Facebook and Gmail passwords as well as capture screen content by leveraging Android's [MediaProjection API](https://developer.android.com/reference/android/media/projection/MediaProjection).

The Dutch security firm said that the most recent iteration of SpyNote (called SpyNote.C) is the first variant to strike banking apps as well as other well-known apps like Facebook and WhatsApp.

[![Android Spyware](data:image/png;base64... "Android Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOP5t0J6OlVWyjsEOm7loZFk9KlRu7RhBlmtmk1KHCZb4lOH52QjKM7V_8wayv4dUQh4DtoeA5DFTywtA0Meu-rrTLXLbbj2DZWMR2bvg1_ROcnlPon5iMlXj5NRsujkekSFnX4OjKj8iaQoFSv1MZkIDo3euWGaFGbVoGvBMMphxSDa0_itZywQyH/s790-rw-e365/spynote-1.png)

It's also known to masquerade as the official Google Play Store service and other generic applications spanning wallpapers, productivity, and gaming categories. A list of some of the SpyNote artifacts, which are mainly delivered through [smishing attacks](https://en.wikipedia.org/wiki/Phishing#SMS_phishing), is as follows -

* Bank of America Confirmation (yps.eton.application)
* BurlaNubank (com.appser.verapp)
* Conversations\_ (com.appser.verapp )
* Current Activity (com.willme.topactivity)
* Deutsche Bank Mobile (com.reporting.efficiency)
* HSBC UK Mobile Banking (com.employ.mb)
* Kotak Bank (splash.app.main)
* Virtual SimCard (cobi0jbpm.apvy8vjjvpser.verapchvvhbjbjq)

SpyNote.C is estimated to have been purchased by 87 different customers between August 2021 and October 2022 after it was advertised by its developer under the name CypherRat through a Telegram channel.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

However, the open source availability of CypherRat in October 2022 has led to a dramatic increase in the number of samples detected in the wild, suggesting that several criminal groups are co-opting the malware in their own campaigns.

ThreatFabric further noted that the original author has since started work on a new spyware project codenamed CraxsRat, which is set to be offered as a paid application with similar features.

"This development is not as common within the Android spyware ecosystem, but is extremely dangerous and shows the potential start of a new trend, which will see a gradual disappearance of the distinction between spyware and banking malware, due to the power that the abuse of accessibility services gives to criminals," the company said.

Users are advised to refrain from downloading apps from untrusted sources, scrutinize reviews before installing any app, and grant only those permissions that are relevant for the app's purpose.

"[Google Play Protect](https://support.google.com/googleplay/answer/2812853) checks Android devices with Google Play Services for potentially harmful apps from other sources," a Google spokesperson told The Hacker News. "Users are protected by Google Play Protect, which can warn users or block identified malicious apps on Android devices."

The findings come as a group of researchers demonstrated a novel attack against Android devices dubbed [EarSpy](https://arxiv.org/abs/2212.12151), which provides access to audio conversations, indoor locations, and touchscreen inputs by leveraging the smartphones' built-in motion sensors and ear speaker as a side-channel.

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
[**Share on Reddit](#li...