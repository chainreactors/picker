---
title: Apple iOS and macOS Flaw Could've Let Apps Eavesdrop on Your Conversations with Siri
url: https://thehackernews.com/2022/10/apple-ios-and-macos-flaw-couldve-let.html
source: The Hacker News
date: 2022-10-28
fetch_date: 2025-10-03T21:10:23.776445
---

# Apple iOS and macOS Flaw Could've Let Apps Eavesdrop on Your Conversations with Siri

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

# [Apple iOS and macOS Flaw Could've Let Apps Eavesdrop on Your Conversations with Siri](https://thehackernews.com/2022/10/apple-ios-and-macos-flaw-couldve-let.html)

**Oct 27, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhynr4fbFbRXPW16mAg1DscRgqTrt8mbDwdM66FICpylozUNf2anDFhLY0zot2uSs6oX1pTvARriucHuaNMj_ExUiBRWIx80ijqOjyLL9BjOHfcxtTRrOfImbZtKsPpj9oXQJO0nYkGgEZ7eIG7pFCw_ScWMMfdv_NFpHL64n9EjFuZdiMZ4GIFesdw/s790-rw-e365/siri.jpg)

A now-patched security flaw in Apple's iOS and macOS operating systems could have potentially enabled apps with Bluetooth access to eavesdrop on conversations with Siri.

Apple said "an app may be able to record audio using a pair of connected AirPods," adding it addressed the Core Bluetooth issue in iOS 16.1 with improved entitlements.

Credited with discovering and reporting the bug in August 2022 is app developer Guilherme Rambo. The bug, dubbed **SiriSpy**, has been assigned the identifier CVE-2022-32946.

"Any app with access to Bluetooth could record your conversations with Siri and audio from the iOS keyboard dictation feature when using AirPods or Beats headsets," Rambo [said](https://rambo.codes/posts/2022-10-25-sirispy-ios-bug-allowed-apps-to-eavesdrop) in a write-up.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This would happen without the app requesting microphone access permission and without the app leaving any trace that it was listening to the microphone."

The vulnerability, according to Rambo, relates to a service called DoAP that's included in AirPods for Siri and Dictation support, thereby enabling a malicious actor to craft an app that could be connected to the AirPods via Bluetooth and record the audio in the background.

This is compounded by the fact that "there's no request to access the microphone, and the indication in Control Center only lists 'Siri & Dictation,' not the app that was bypassing the microphone permission by talking directly to the AirPods over Bluetooth LE."

[![Apple iOS and macOS](data:image/png;base64... "Apple iOS and macOS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgmZmuAs8DqrkDmCJ70zuN_CGtp7UVBTDrbk3rvKMQ5IeBUOPDy3JQ9XapVGO86H07N6wNQoAoG3Py_nad1fuE1TvAsEe0KOuft9JG8N7mTtAaML4QuY5l0BStHt1PK07e_EsGYmVSwnp0YQislwNAvMnVIwNuZl2WHaxJGtLJ-oDBWVn2qYG9FB81t/s790-rw-e365/code.jpg)

While the attack requires that the app has access to Bluetooth, this restriction can be trivially bypassed as users granting Bluetooth access to the app are unlikely to expect that it could also open the door to accessing their conversations with Siri and audio from dictation.

On macOS, however, the exploit could be abused to achieve a total bypass of the Transparency, Consent and Control ([TCC](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/)) security framework, meaning any app can record conversations with Siri without requesting for any permissions in the first place.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Rambo said the reason for this behavior is owing to the lack of entitlement checks for BTLEServerAgent, the daemon service responsible for handling DoAP audio.

A [software patch](https://support.apple.com/en-us/HT213489) remediating this flaw is available for iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th generation and later, and iPad mini 5th generation and later. It has also been resolved in all [supported versions](https://support.apple.com/en-us/HT201222) of macOS.

The iOS 16.1 update, which was released on October 24, 2022, comes with fixes for a total of 20 flaws, including a [Kernel vulnerability](https://thehackernews.com/2022/10/apple-releases-patch-for-new-actively.html) (CVE-2022-42827) that Apple disclosed as being actively exploited in the wild.

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

[AirPod](https://thehackernews.com/search/label/AirPod)[Apple](https://thehackernews.com/search/label/Apple)[Apple Siri](https://thehackernews.com/search/label/Apple%20Siri)[Bluetooth](https://thehackernews.com/search/label/Bluetooth)[iOS](https://thehackernews.com/search/label/iOS)[MacOS](https://thehackernews.com/search/label/MacOS)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc ...