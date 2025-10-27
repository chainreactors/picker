---
title: CapraRAT Spyware Disguised as Popular Apps Threatens Android Users
url: https://thehackernews.com/2024/07/caprarat-spyware-disguised-as-popular.html
source: The Hacker News
date: 2024-07-02
fetch_date: 2025-10-06T17:46:57.891925
---

# CapraRAT Spyware Disguised as Popular Apps Threatens Android Users

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

# [CapraRAT Spyware Disguised as Popular Apps Threatens Android Users](https://thehackernews.com/2024/07/caprarat-spyware-disguised-as-popular.html)

**Jul 01, 2024**Ravie LakshmananMobile Security / Spyware

[![CapraRAT Spyware](data:image/png;base64... "CapraRAT Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgU4ISPkb4I9mBvScSZZXu5z-uFde93jyAL5gTjvqAZYQnBQAPUb8ycK_aMDThGoFkduhSpJJB_c7DUeL9ID-u6-ZCAhWywL2rQyKDoson93LLeg89RVTCBP-wUWoKec2_ivs-z38EpFiGymQENVz55Kb8I2xKUGv0GoglhfQQDvSjOtDyNJLhTrL-k6u4w/s790-rw-e365/android-spyware.png)

The threat actor known as [Transparent Tribe](https://thehackernews.com/2024/06/pakistani-hackers-use-disgomoji-malware.html) has continued to unleash malware-laced Android apps as part of a social engineering campaign to target individuals of interest.

"These APKs continue the group's trend of embedding spyware into curated video browsing applications, with a new expansion targeting mobile gamers, weapons enthusiasts, and TikTok fans," SentinelOne security researcher Alex Delamotte [said](https://www.sentinelone.com/labs/capratube-remix-transparent-tribes-android-spyware-targeting-gamers-weapons-enthusiasts/) in a new report shared with The Hacker News.

The campaign, dubbed CapraTube, was [first outlined](https://thehackernews.com/2023/09/transparent-tribe-uses-fake-youtube.html) by the cybersecurity company in September 2023, with the hacking crew employing weaponized Android apps impersonating legitimate apps like YouTube to deliver a spyware called CapraRAT, a modified version of AndroRAT with capabilities to capture a wide range of sensitive data.

Transparent Tribe, suspected to be of Pakistan origin, has leveraged [CapraRAT](https://thehackernews.com/2022/02/new-caprarat-android-malware-targets.html) for over two years in attacks targeting the Indian government and military personnel. The group has a history of leaning into spear-phishing and watering hole attacks to deliver a variety of Windows and Android spyware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The activity highlighted in this report shows the continuation of this technique with updates to the social engineering pretexts as well as efforts to maximize the spyware's compatibility with older versions of the Android operating system while expanding the attack surface to include modern versions of Android," Delamotte explained.

The list of new malicious APK files identified by SentinelOne is as follows -

* Crazy Game (com.maeps.crygms.tktols)
* Sexy Videos (com.nobra.crygms.tktols)
* TikToks (com.maeps.vdosa.tktols)
* Weapons (com.maeps.vdosa.tktols)

CapraRAT uses WebView to launch a URL to either YouTube or a mobile gaming site named CrazyGames[.]com, while, in the background, it abuses its permissions to access locations, SMS messages, contacts, and call logs; make phone calls; take screenshots; or record audio and video.

A notable change to the malware is that permissions such as READ\_INSTALL\_SESSIONS, GET\_ACCOUNTS, AUTHENTICATE\_ACCOUNTS, and REQUEST\_INSTALL\_PACKAGES are no longer requested, suggesting that the threat actors are aiming to use it as a surveillance tool than a backdoor.

"The updates to the CapraRAT code between the September 2023 campaign and the current campaign are minimal, but suggest the developers are focused on making the tool more reliable and stable," Delamotte said.

"The decision to move to newer versions of the Android OS are logical, and likely align with the group's sustained targeting of individuals in the Indian government or military space, who are unlikely to use devices running older versions of Android, such as Lollipop which was released 8 years ago."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Promon revealed a novel type of Android banking malware called Snowblind that, in ways similar to [FjordPhantom](https://thehackernews.com/2023/12/new-fjordphantom-android-malware.html), attempts to bypass detection methods and make use of the operating system's accessibility services API in a surreptitious manner.

By using the seccomp functionality to intercept and manipulate system calls, it not only allows the malware to undermine security checks and fly under the radar, but also steal credentials, export data, and disable features like two-factor authentication (2FA) or biometric verification.

"Snowblind [...] performs a normal repackaging attack but uses a lesser-known technique based on [seccomp](https://en.wikipedia.org/wiki/Seccomp) that is capable of bypassing many anti-tampering mechanisms," the company [said](https://promon.co/app-threat-reports/snowblind).

"Interestingly, FjordPhantom and Snowblind target apps from Southeast Asia and leverage powerful new attack techniques. That seems to indicate that malware authors in that region have become extremely sophisticated."

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

[Android](https://thehackernews.com/search/label/Android)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://t...