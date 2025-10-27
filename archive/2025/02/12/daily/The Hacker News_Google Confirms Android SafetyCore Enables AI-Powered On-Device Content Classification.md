---
title: Google Confirms Android SafetyCore Enables AI-Powered On-Device Content Classification
url: https://thehackernews.com/2025/02/google-confirms-android-safetycore.html
source: The Hacker News
date: 2025-02-12
fetch_date: 2025-10-06T20:50:47.719674
---

# Google Confirms Android SafetyCore Enables AI-Powered On-Device Content Classification

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

# [Google Confirms Android SafetyCore Enables AI-Powered On-Device Content Classification](https://thehackernews.com/2025/02/google-confirms-android-safetycore.html)

**Feb 11, 2025**Ravie LakshmananMobile Security / Machine Learning

[![Android SafetyCore](data:image/png;base64... "Android SafetyCore")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjWF0W0H7ZIWXsOxmyUHdjEpDPBk6rsNSPbxjkxxYxdlh9GbMYRLI3LUOkVktBxC0p-GctBtoFqJ_YTNdkNB0VjivL06_YGX6cnIVUx-2VhoDCzvOdlQLVKAjbW2A-OZXfj1ckvO1YBk13QkEEqQuI0eTbzfvCE6CSX257AFDOTKFMeoojoiFL-NNLcTiZ/s790-rw-e365/android.png)

Google has stepped in to clarify that a newly introduced Android System SafetyCore app does not perform any [client-side scanning](https://thehackernews.com/2024/06/signal-foundation-warns-against-eus.html) of content.

"Android provides many on-device protections that safeguard users against threats like malware, messaging spam and abuse protections, and phone scam protections, while preserving user privacy and keeping users in control of their data," a spokesperson for the company told The Hacker News when reached for comment.

"SafetyCore is a new Google system service for Android 9+ devices that provides the on-device infrastructure for securely and privately performing classification to help users detect unwanted content. Users are in control over SafetyCore and SafetyCore only classifies specific content when an app requests it through an optionally enabled feature."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

SafetyCore (package name "com.google.android.safetycore") was [first introduced](https://thehackernews.com/2024/11/new-phishing-kit-xiu-gou-targets-users.html) by Google in October 2024, as part of a [set of security measures](https://developers.google.com/android/binary_transparency/google1p/overview) designed to combat scams and other content deemed sensitive on the Google Messages app for Android.

The feature, which requires 2GB of RAM, is rolling out to all Android devices, running Android version 9 and later, as well as those running Android Go, a lightweight version of the operating system for entry-level smartphones.

Client-side scanning (CSS), on the other hand, is seen as an alternative approach to enable on-device analysis of data as opposed to weakening encryption or adding backdoors to existing systems. However, the method has raised serious privacy concerns, as it's ripe for abuse by forcing the service provider to search for material beyond the initially agreed-upon scope.

In some ways, Google's Sensitive Content Warnings for the Messages app is a lot similar to Apple's [Communication Safety feature](https://support.apple.com/en-us/105069) in iMessage, which employs on-device machine learning to analyze photo and video attachments and determine if a photo or video appears to contain nudity.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The maintainers of the GrapheneOS operating system, in a [post](https://x.com/GrapheneOS/status/1888280836426084502?mx=2) shared on X, reiterated that SafetyCore doesn't provide client-side scanning, and is mainly designed to offer on-device machine-learning models that can be used by other applications to classify content as spam, scam, or malware.

"Classifying things like this is not the same as trying to detect illegal content and reporting it to a service," GrapheneOS said. "That would greatly violate people's privacy in multiple ways and false positives would still exist. It's not what this is and it's not usable for it."

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

[AI](https://thehackernews.com/search/label/AI)[Android](https://thehackernews.com/search/label/Android)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Google](https://thehackernews.com/search/label/Google)[machine learning](https://thehackernews.com/search/label/machine%20learning)[Messaging](https://thehackernews.com/search/label/Messaging)[mobile](https://thehackernews.com/search/label/mobile)[Privacy](https://thehackernews.com/search/label/Privacy)[security](https://thehackernews.com/search/label/security)[technology](https://thehackernews.com/search/label/technology)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found St...