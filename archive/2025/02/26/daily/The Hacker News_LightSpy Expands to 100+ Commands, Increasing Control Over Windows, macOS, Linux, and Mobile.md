---
title: LightSpy Expands to 100+ Commands, Increasing Control Over Windows, macOS, Linux, and Mobile
url: https://thehackernews.com/2025/02/lightspy-expands-to-100-commands.html
source: The Hacker News
date: 2025-02-26
fetch_date: 2025-10-06T20:50:15.423506
---

# LightSpy Expands to 100+ Commands, Increasing Control Over Windows, macOS, Linux, and Mobile

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

# [LightSpy Expands to 100+ Commands, Increasing Control Over Windows, macOS, Linux, and Mobile](https://thehackernews.com/2025/02/lightspy-expands-to-100-commands.html)

**Feb 25, 2025**Ravie LakshmananMobile Security / Spyware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjGm9noFp1eI7IArSFLOgpwpoAA697U1EihVY3xgHyJtDSqAJ0RVrtRE8hyphenhyphenPrU4dxb2ESsv-B1jhfUKxlVa51jx2ck54la5PNpEHB1_if3uMHz5tc_U4AQhX1f4fRV7YHV2OcwdjIzQjeRlpyAvfgDWz9N2KnxhfDEiWXIVUGZ0tQUtplq4BJl2j5Kwm61m/s790-rw-e365/spyware.png)

Cybersecurity researchers have flagged an updated version of the LightSpy implant that comes equipped with an expanded set of data collection features to extract information from social media platforms like Facebook and Instagram.

LightSpy is the name given to a [modular spyware](https://thehackernews.com/2024/10/new-lightspy-spyware-version-targets.html) that's [capable](https://thehackernews.com/2024/06/lightspy-spywares-macos-variant-found.html) of infecting both Windows and Apple systems with an aim to harvest data. It was first documented in 2020, targeting users in Hong Kong.

This includes Wi-Fi network information, screenshots, location, iCloud Keychain, sound recordings, photos, browser history, contacts, call history, and SMS messages, and data from various apps like Files, LINE, Mail Master, Telegram, Tencent QQ, WeChat, and WhatsApp.

Late last year, ThreatFabric detailed an updated version of the malware that incorporates destructive capabilities to prevent the compromised device from booting up, alongside expanding the number of supported plugins from 12 to 28.

Previous findings have also uncovered potential overlaps between LightSpy and an Android malware named [DragonEgg](https://thehackernews.com/2023/10/researchers-link-dragonegg-android.html), highlighting the cross-platform nature of the threat.

Hunt.io's latest analysis of the malicious command-and-control (C2) infrastructure associated with the spyware has uncovered support for over 100 commands spanning Android, iOS, Windows, macOS, routers, and Linux.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The new command list shifts focus from direct data collection to broader operational control, including transmission management ('传输控制') and plugin version tracking ('上传插件版本详细信息')," the company [said](https://hunt.io/blog/lightspy-malware-targets-facebook-instagram).

"These additions suggest a more flexible and adaptable framework, allowing LightSpy operators to manage deployments more efficiently across multiple platforms."

Notable among the new commands is the ability to target Facebook and Instagram application database files for data extraction from Android devices. But in an interesting twist, the threat actors have removed iOS plugins associated with destructive actions on the victim host.

Also discovered are 15 Windows-specific plugins designed for system surveillance and data collection, with most of them geared towards keylogging, audio recording, and USB interaction.

The threat intelligence firm said it also discovered an endpoint ("/phone/phoneinfo") in the admin panel that grants logged-in users the ability to remotely control the infected mobile devices. It's currently not known if these represent new developments or previously undocumented older versions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2XLNCGEjHvHCMHofeWcNtD1ooYW8LVTQah04YTVmhIMp-1_RH8VNpeZeemYQJ59S0-6QtHBuKRwHKZvAssN9hn2Mk7nUqVsvSQ2MdXRSoaMI4KCc_SenbA1uyCSjnLRj-oTa0l8T3Up-3qp0Jl5O-mmTjy01nx7E-v4mmHg-3dxnHSHHlf37j7-m5uuy3/s790-rw-e365/code.png)

"The shift from targeting messaging applications to Facebook and Instagram expands LightSpy's ability to collect private messages, contact lists, and account metadata from widely used social platforms," Hunt.io said.

"Extracting these database files could provide attackers with stored conversations, user connections, and potentially session-related data, increasing surveillance capabilities and opportunities for further exploitation."

The disclosure comes as Cyfirma disclosed details of an Android malware dubbed SpyLend that masquerades as a financial app named Finance Simplified (APK name "com.someca.count") on the Google Play Store but engages in [predatory lending, blackmail, and extortion](https://thehackernews.com/2024/12/8-million-android-users-hit-by-spyloan.html) aimed at Indian users.

"By leveraging location-based targeting, the app displays a list of unauthorized loan apps that operate entirely within WebView, allowing attackers to bypass Play Store scrutiny," the company [said](https://www.cyfirma.com/research/spylend-the-android-app-available-on-google-play-store-enabling-financial-cyber-crime-extortion/).

"Once installed, these loan apps harvest sensitive user data, enforce exploitative lending practices, and employ blackmail tactics to extort money."

Some of the advertised loan apps are KreditPro (formerly KreditApple), MoneyAPE, StashFur, Fairbalance, and PokketMe. Users who install Finance Simplified from outside India are served a harmless WebView that lists various calculators for personal finance, accounting, and taxation, suggesting that the campaign is designed to specifically target Indian users.

The app is no longer available for download from the official Android app marketplace. According to statistics available on Sensor Tower, the application was [published](https://app.sensortower.com/overview/com.someca.count?country=IN) around mid-December 2024 and attracted over 100,000 installations.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Initially presented as a harmless finance management application, it downloads a fraud loan app from an external download URL, which once installed, gains extensive permissions to access sensitive data, including files, contacts, call logs, SMS, clipboard content, and even the camera," Cyfi...