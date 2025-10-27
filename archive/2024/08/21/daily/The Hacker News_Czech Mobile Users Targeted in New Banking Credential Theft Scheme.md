---
title: Czech Mobile Users Targeted in New Banking Credential Theft Scheme
url: https://thehackernews.com/2024/08/czech-mobile-users-targeted-in-new.html
source: The Hacker News
date: 2024-08-21
fetch_date: 2025-10-06T18:08:45.654775
---

# Czech Mobile Users Targeted in New Banking Credential Theft Scheme

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

# [Czech Mobile Users Targeted in New Banking Credential Theft Scheme](https://thehackernews.com/2024/08/czech-mobile-users-targeted-in-new.html)

**Aug 20, 2024**Ravie LakshmananMobile Security / Banking Fraud

[![Credential Theft Scheme](data:image/png;base64... "Credential Theft Scheme")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKB2knSk0AvxOzZB-SD1rO8OBCzisRCpgehXYtyG7yVMkQ02mW97PSJkoZgbbsDtm_btidEub1V4imaWpbQK5mz4Oys4_JJUZJO3fEBUhhaLPFPQ4fjxSO1AwixJkv1jL39ZaLib0mgGsWlMVWBcSN0j519xJ4-kyEmhE1-Sd0DMXkhUT2yI-seVCREpSr/s790-rw-e365/hacker.png)

Mobile users in the Czech Republic are the target of a novel phishing campaign that leverages a Progressive Web Application (PWA) in an attempt to sidestep security protections and steal their banking account credentials.

The attacks have targeted the Czech-based Československá obchodní banka (CSOB), as well as the Hungarian OTP Bank and a Georgian Bank, according to Slovak cybersecurity company ESET.

"The phishing websites targeting iOS instruct victims to add a Progressive Web Application ([PWA](https://web.dev/learn/pwa/progressive-web-apps/)) to their home-screens, while on Android the PWA is installed after confirming custom pop-ups in the browser," security researcher Jakub Osmani [said](https://www.welivesecurity.com/en/eset-research/be-careful-what-you-pwish-for-phishing-in-pwa-applications/).

"At this point, on both operating systems, these phishing apps are largely indistinguishable from the real banking apps that they mimic."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

What's notable about this tactic is that users are deceived into installing a PWA, or even WebAPKs in some cases on Android, from a third-party site without having to specifically allow side loading.

An analysis of the command-and-control (C2) servers used and the backend infrastructure reveals that two different threat actors are behind the campaigns.

These websites are distributed via automated voice calls, SMS messages, and social media malvertising via Facebook and Instagram. The voice calls warn users about an out-of-date banking app and ask them to select a numerical option, following which the phishing URL is sent.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjargEoXh2UizMAUbL4LEr9_FiMtp8BhwAHfVUcWitk40WyvU-APPIYJw3nHcZ8TO2zwHOEzkAknTNhHWFxfnL2YBx1uYcpz8dIHYCZ8D1FAS_7iHUMyfxfGKVxqH6eZ_JXFNkuEccMhQYWvYR0ngM1XwANFAUvF4W0dIa4d2DR2W-hk3ygPXnAgqw1mEYP/s790-rw-e365/image.png)

Users who end up clicking on the link are displayed a lookalike page that mimics the Google Play Store listing for the targeted banking app, or a copycat site for the application, ultimately leading to the "installation" of the PWA or WebAPK app under the guise of an app update.

"This crucial installation step bypasses traditional browser warnings of 'installing unknown apps': this is the default behavior of Chrome's WebAPK technology, which is abused by the attackers," Osmani explained. "Furthermore, installing a WebAPK does not produce any of the 'installation from an untrusted source' warnings."

For those who are on Apple iOS devices, instructions are provided to add the bogus PWA app to the Home Screen. The end goal of the campaign is to capture the banking credentials entered on the app and exfiltrate them to an attacker-controlled C2 server or a Telegram group chat.

ESET said it recorded the first phishing-via-PWA instance in early November 2023, with subsequent waves detected in March and May 2024. The very first instance of the technique was observed in July 2023.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as cybersecurity researchers have uncovered a new variant of the [Gigabud](https://thehackernews.com/2024/02/chinese-hackers-using-deepfakes-in.html) Android trojan that's spread via phishing websites mimicking the Google Play Store or sites impersonating various banks or governmental entities.

"The malware has various capabilities such as the collection of data about the infected device, exfiltration of banking credentials, collection of screen recordings, etc.," Broadcom-owned Symantec [said](https://www.broadcom.com/support/security-center/protection-bulletin/gigabud-mobile-malware-shows-links-to-the-golddigger-trojan).

It also follows Silent Push's [discovery](https://www.silentpush.com/blog/dukeeugene/) of 24 different control panels for a variety of Android banking trojans such as ERMAC, BlackRock, Hook, Loot, and Pegasus (not to be confused with NSO Group's spyware of the same name) that are operated by a threat actor named [DukeEugene](https://thehackernews.com/2023/09/hook-new-android-banking-trojan-that.html).

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

[Banking Fraud](https://thehackernews.com/search/label/Banking%20Fraud)[cyber attacks](https://thehackernews.com/search/label/cyber%20attacks)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data theft](https://thehackernews.com/search/label/data%20theft)[Financial Crime](https://thehackernews.com/search/label/Financial%20Crime)[Malware](https://thehac...