---
title: Malicious npm Packages Mimicking 'noblox.js' Compromise Roblox Developers’ Systems
url: https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html
source: The Hacker News
date: 2024-09-03
fetch_date: 2025-10-06T18:28:32.649123
---

# Malicious npm Packages Mimicking 'noblox.js' Compromise Roblox Developers’ Systems

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

# [Malicious npm Packages Mimicking 'noblox.js' Compromise Roblox Developers' Systems](https://thehackernews.com/2024/09/malicious-npm-packages-mimicking.html)

**Sep 02, 2024**Ravie LakshmananSoftware Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoNL7P8eg35tWbTCI5IO41nMzh2rBeeUFuLfnjoTZTi77WW_1BtKRbHIV5tNV6jpILMQ_8cdOTkWxAXkAiSNn9YHFHI4SFbO2lpiTLFeMmtNhrUyoKE5rg2psPHmfM6PdAhjXTUCBHjFnOnnywA-pW7kJy_RXOIGRkeI2mo2Wj8ekxb2B7pKyhPwFIKhvz/s790-rw-e365/software.jpg)

Roblox developers are the target of a persistent campaign that seeks to compromise systems through bogus npm packages, once again underscoring how threat actors continue to exploit the trust in the open-source ecosystem to deliver malware.

"By mimicking the popular 'noblox.js' library, attackers have published dozens of packages designed to steal sensitive data and compromise systems," Checkmarx researcher Yehuda Gelb [said](https://checkmarx.com/blog/year-long-campaign-of-malicious-npm-packages-targeting-roblox-users/) in a technical report.

Roblox is an online game platform and game creation system with nearly [80 million daily active users](https://corp.roblox.com), and thus makes for an attractive target for threat actors. It was launched in September 2006 for Windows, before debuting in other platforms, including iOS, Android, Xbox One, Meta Quest, and PlayStation 4.

Details about the activity were [first documented](https://thehackernews.com/2023/08/over-dozen-malicious-npm-packages.html) by ReversingLabs in August 2023 as part of a [campaign](https://devforum.roblox.com/t/malicious-packages-targeting-roblox-api-users/2559934) that delivered a stealer called Luna Token Grabber, which it said was a "replay of an attack uncovered two years ago" in October 2021.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Since the start of the year, two other packages called [noblox.js-proxy-server](https://socket.dev/npm/package/noblox.js-proxy-server) and [noblox-ts](https://stacklok.com/blog/destroyloneliness-npm-starjacking-attack-on-roblox-nodejs-library-delivers-quasarrat/) were identified as malicious and impersonating the popular Node.js library to deliver stealer malware and a remote access trojan named Quasar RAT.

"The attackers of this campaign have employed techniques including brandjacking, combosquatting, and starjacking to create a convincing illusion of legitimacy for their malicious packages," Gelb said,

To that end, the packages are given a veneer of legitimacy by naming them noblox.js-async, noblox.js-thread, noblox.js-threads, and noblox.js-api, giving the impression to unsuspecting developers that these libraries are related to the legitimate "noblox.js" package.

The package download stats are listed below -

* [noblox.js-async](https://npm-stat.com/charts.html?package=noblox.js-async) (74 downloads)
* [noblox.js-thread](https://npm-stat.com/charts.html?package=noblox.js-thread) (117 downloads)
* [noblox.js-threads](https://npm-stat.com/charts.html?package=noblox.js-threads) (64 downloads)
* [noblox.js-api](https://npm-stat.com/charts.html?package=noblox.js-api) (64 downloads)

Another technique employed is starjacking, in which the phony packages list the source repository as that of the actual noblox.js library to make it seem more reputable.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0NeIzyBPUPIIuQPL8eai_-9dXRh-uTfurLtag5peSbXILtGsK0XTbATPiXSyB3D-Be_6QP8SAL43wDEH5EPt5wY2wxtp5D3DqVmkWVo9-syZdhbtA8yrYMGWaytWVxHxpi5PNI96ZltUoWcnDssX1kf8PAz1Y0IDTnZuBi7YWzPZW690IHpIw2d48MwGw/s790-rw-e365/flow.jpg)

The malicious code embedded in the latest iteration acts as a gateway for serving additional payloads [hosted on a GitHub repository](https://github.com/aspdasdksa2/), while simultaneously stealing Discord tokens, updating the Microsoft Defender Antivirus exclusion list to evade detection, and setting up persistence by means of a Windows Registry change.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Central to the malware's effectiveness is its approach to persistence, leveraging the Windows Settings app to ensure sustained access," Gelb noted. "As a result, whenever a user attempts to open the Windows Settings app, the system inadvertently executes the malware instead."

The end goal of the attack chain is the deployment of Quasar RAT, granting the attacker remote control over the infected system. The harvested information is exfiltrated to the attacker's command-and-control (C2) server using a Discord webhook.

The findings are an indication a steady stream of new packages continue to be published despite takedown efforts, making it essential that developers stay vigilant against the ongoing threat.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Developer Security](https://thehackernews.com/search/label/Developer%20Security)[Malware](https://thehackernews.com/search/label/Malware)[npm Security](https://thehackernews.com/search/label/npm%20Security)[Open Source](https://thehackernews...