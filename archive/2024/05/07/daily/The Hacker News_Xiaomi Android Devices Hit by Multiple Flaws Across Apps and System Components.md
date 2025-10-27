---
title: Xiaomi Android Devices Hit by Multiple Flaws Across Apps and System Components
url: https://thehackernews.com/2024/05/xiaomi-android-devices-hit-by-multiple.html
source: The Hacker News
date: 2024-05-07
fetch_date: 2025-10-06T17:19:56.277444
---

# Xiaomi Android Devices Hit by Multiple Flaws Across Apps and System Components

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

# [Xiaomi Android Devices Hit by Multiple Flaws Across Apps and System Components](https://thehackernews.com/2024/05/xiaomi-android-devices-hit-by-multiple.html)

**May 06, 2024**Ravie LakshmananAndroid / Data Security

[![Xiaomi Android Devices](data:image/png;base64... "Xiaomi Android Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0AFmbWqUNd3G018HE8XfB9AeeuQk0WmwbIBCh6gh7Mv2scbyd4gFaB1_lvhqVzFrPyrqnAoCb8DEArPjZ7JpST1b_5q_ZYJKdHfveDjKKq8zsSo4SZTVGBIJS7BJPeNSnYX1OmC_thfu-oGo4fW9gDBZhRYo7QeXCPYtHDe4IxYxVfsRvd0BumJ6et_6y/s790-rw-e365/mi.png)

Multiple security vulnerabilities have been disclosed in various applications and system components within Xiaomi devices running Android.

"The vulnerabilities in Xiaomi led to access to arbitrary activities, receivers and services with system privileges, theft of arbitrary files with system privileges, [and] disclosure of phone, settings and Xiaomi account data," mobile security firm Oversecured [said](https://blog.oversecured.com/20-Security-Issues-Found-in-Xiaomi-Devices/) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The 20 shortcomings impact different apps and components like -

* Gallery (com.miui.gallery)
* GetApps (com.xiaomi.mipicks)
* Mi Video (com.miui.videoplayer)
* MIUI Bluetooth (com.xiaomi.bluetooth)
* Phone Services (com.android.phone)
* Print Spooler (com.android.printspooler)
* Security (com.miui.securitycenter)
* Security Core Component (com.miui.securitycore)
* Settings (com.android.settings)
* ShareMe (com.xiaomi.midrop)
* System Tracing (com.android.traceur), and
* Xiaomi Cloud (com.miui.cloudservice)

Some of the notable flaws include a shell command injection bug impacting the System Tracing app and flaws in the Settings app that could enable theft of arbitrary files as well as leak information about Bluetooth devices, connected Wi-Fi networks, and emergency contacts.

It's worth noting that while Phone Services, Print Spooler, Settings, and System Tracing are legitimate components from the Android Open Source Project ([AOSP](https://source.android.com/)), they have been modified by the Chinese handset maker to incorporate additional functionality, leading to these flaws.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also discovered is a [memory corruption flaw](https://blog.oversecured.com/Exploiting-memory-corruption-vulnerabilities-on-Android/) impacting the GetApps app, which, in turn, originates from an Android library called [LiveEventBus](https://github.com/JeremyLiao/LiveEventBus) that Oversecured said was reported to the project maintainers over a year ago and remains unpatched to date.

The Mi Video app has been found to use [implicit intents](https://developer.android.com/guide/components/intents-filters#Types) to send Xiaomi account information, such as username and email address via [broadcasts](https://developer.android.com/develop/background-work/background-tasks/broadcasts), which could be intercepted by any third-party app installed on the devices using its own broadcast receivers.

Oversecured said the issues were reported to Xiaomi within a span of five days from April 25 to April 30, 2023. Users are advised to apply the latest updates to mitigate against potential threats.

*(A previous version of the story incorrectly mentioned the disclosure timeline as April 2024. It was disclosed in April 2023.)*

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

[Android](https://thehackernews.com/search/label/Android)[data security](https://thehackernews.com/search/label/data%20security)[mobile security](https://thehackernews.com/search/label/mobile%20security)[Privacy](https://thehackernews.com/search/label/Privacy)[technology](https://thehackernews.com/search/label/technology)[Xiaomi](https://thehackernews.com/search/label/Xiaomi)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Clic...