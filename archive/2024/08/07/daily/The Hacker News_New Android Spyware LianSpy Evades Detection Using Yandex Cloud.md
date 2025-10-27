---
title: New Android Spyware LianSpy Evades Detection Using Yandex Cloud
url: https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html
source: The Hacker News
date: 2024-08-07
fetch_date: 2025-10-06T18:06:14.942121
---

# New Android Spyware LianSpy Evades Detection Using Yandex Cloud

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

# [New Android Spyware LianSpy Evades Detection Using Yandex Cloud](https://thehackernews.com/2024/08/new-android-spyware-lianspy-evades.html)

**Aug 06, 2024**Ravie LakshmananAndroid / Malware

[![Android Spyware](data:image/png;base64... "Android Spyware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivOqCZOxV7LD9U-qFXevwZcGiUAzFK63iSc_9yzpBpNXE0ys12j3LLQNQddhGoLsLB-oQevIijfOuO9w489l7FFp3LIwDqkZlhXVnG47E02Ki2LJJpoMNV9kqNXfj7ABWqNh3-u9kT4gkD0jZPr8ZUOgpLhzPQ9JdMVv7z8Un0o9xbZLD65WAX8yus-2cT/s790-rw-e365/russian-android-spuware.png)

Users in Russia have been the target of a previously undocumented Android post-compromise spyware called **LianSpy** since at least 2021.

Cybersecurity vendor Kaspersky, which discovered the malware in March 2024, noted its use of Yandex Cloud, a Russian cloud service, for command-and-control (C2) communications as a way to avoid having a dedicated infrastructure and evade detection.

"This threat is equipped to capture screencasts, exfiltrate user files, and harvest call logs and app lists," security researcher Dmitry Kalinin [said](https://securelist.com/lianspy-android-spyware/113253/) in a new technical report published Monday.

It's currently not clear how the spyware is distributed, but the Russian company said it's likely deployed through either an unknown security flaw or direct physical access to the target phone. The malware-laced apps are disguised as Alipay or an Android system service.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

LianSpy, once activated, determines if it's running as a system app to operate in the background using administrator privileges, or else requests a wide range of permissions that allow it to access contacts, call logs, and notifications, and draw overlays atop the screen.

It also checks if it's executing in a debugging environment to set up a configuration that persists across reboots, followed by hiding its icon from the launcher and trigger activities such as taking screenshots, exfiltrating data, and updating its configuration to specify what kinds of information needs to be captured.

In some variants, this has been found to include options to gather data from instant messaging apps popular in Russia as well as allow or prohibit running the malware only if it's either connected to Wi-Fi or a mobile network, among others.

"To update the spyware configuration, LianSpy searches for a file matching the regular expression "^frame\_.+\\.png$" on a threat actor's Yandex Disk every 30 seconds," Kalinin said. "If found, the file is downloaded to the application's internal data directory."

The harvested data is stored in encrypted form in an SQL database table, specifying the type of record and its SHA-256 hash, such that only a threat actor in possession of the corresponding private RSA key can decrypt the stolen information.

Where LianSpy showcases its stealth is in its ability to bypass the [privacy indicators](https://source.android.com/docs/core/permissions/privacy-indicators) feature introduced by Google in Android 12, which requires apps requesting for microphone and camera permissions to display a status bar icon.

"LianSpy developers have managed to bypass this protection by appending a cast value to the Android secure setting parameter icon\_blacklist, which prevents notification icons from appearing in the status bar," Kalinin pointed out.

"LianSpy hides notifications from background services it calls by leveraging the NotificationListenerService that processes status bar notifications and is able to suppress them."

Another sophisticated aspect of the malware entails the use of the [su binary](https://github.com/jpacg/su-binary) with a modified name "mu" to gain root access, raising the possibility that it's likely delivered through a previously unknown exploit or physical device access.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

LianSpy's emphasis on flying under the radar is also evidenced in the fact that C2 communications are unidirectional, with the malware not receiving any incoming commands. The Yandex Disk service is used for both transmitting stolen data and storing configuration commands.

Credentials for Yandex Disk are updated from a hard-coded Pastebin URL, which varies across malware variants. The use of legitimate services adds a layer of obfuscation, effectively clouding attribution.

LianSpy is the latest addition to a growing list of spyware tools, which are often delivered to target mobile devices – be it Android or iOS – by leveraging zero-day flaws.

"Beyond standard espionage tactics like harvesting call logs and app lists, it leverages root privileges for covert screen recording and evasion," Kalinin said. "Its reliance on a renamed su binary strongly suggests secondary infection following an initial compromise."

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

[Android](https://thehackernews.com/search/label/Android)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label...