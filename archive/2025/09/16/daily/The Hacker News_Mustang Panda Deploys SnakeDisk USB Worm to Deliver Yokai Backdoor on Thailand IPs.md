---
title: Mustang Panda Deploys SnakeDisk USB Worm to Deliver Yokai Backdoor on Thailand IPs
url: https://thehackernews.com/2025/09/mustang-panda-deploys-snakedisk-usb.html
source: The Hacker News
date: 2025-09-16
fetch_date: 2025-10-02T20:13:18.439327
---

# Mustang Panda Deploys SnakeDisk USB Worm to Deliver Yokai Backdoor on Thailand IPs

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

# [Mustang Panda Deploys SnakeDisk USB Worm to Deliver Yokai Backdoor on Thailand IPs](https://thehackernews.com/2025/09/mustang-panda-deploys-snakedisk-usb.html)

**Sep 15, 2025**Ravie LakshmananMalware / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuFHJMhcKrcm7rKKxumPi41kz_INbFE63vmSz9Z01h47HyqaoqX2NhVX3FECyM63yiZOeLoeikkQcGPdYZQdHvSUZl3LGUc8fhhz_Y_qFiYWJaunzL8jXP7of-33sZKTgvXhzwry7gVsRGnCX2zQvoEV8q8Ul7ZDsECGxH-uGeaoUQBIJ2LY2wcU3BJfzK/s790-rw-e365/usb.jpg)

The China-aligned threat actor known as **[Mustang Panda](https://thehackernews.com/2025/06/pubload-and-pubshell-malware-used-in.html)** has been observed using an updated version of a backdoor called TONESHELL and a previously undocumented USB worm called SnakeDisk.

"The worm only executes on devices with Thailand-based IP addresses and drops the [Yokai](https://thehackernews.com/2024/12/thai-officials-targeted-in-yokai.html) backdoor," IBM X-Force researchers Golo Mühr and Joshua Chung [said](https://www.ibm.com/think/x-force/hive0154-drops-updated-toneshell-backdoor) in an analysis published last week.

The tech giant's cybersecurity division is tracking the cluster under the name Hive0154, which is also broadly referred to as BASIN, Bronze President, Camaro Dragon, Earth Preta, HoneyMyte, Polaris, RedDelta, Stately Taurus, and Twill Typhoon. The state-sponsored threat actor is believed to have been active since at least 2012.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[TONESHELL](https://thehackernews.com/2025/04/mustang-panda-targets-myanmar-with.html) was first publicly documented by Trend Micro way back in November 2022 as part of cyber attacks targeting Myanmar, Australia, the Philippines, Japan, and Taiwan between May and October. Typically executed via DLL side-loading, its primary responsibility is to download next-stage payloads on the infected host.

Typical attack chains involve the use of spear-phishing emails to drop malware families like PUBLOAD or TONESHELL. PUBLOAD, which functions similarly to TONESHELL, is also capable of downloading shellcode payloads via HTTP POST requests from a command-and-control (C2) server.

The newly identified TONESHELL variants, named TONESHELL8 and TONESHELL9 by IBM X-Force, support C2 communication through locally configured proxy servers to blend in with enterprise network traffic and facilitate two active reverse shells in parallel. TONESHELL8 also incorporates junk code copied from OpenAI's ChatGPT website within the malware's functions to evade static detection and resist analysis.

Also launched using DLL side-loading is a new USB worm called SnakeDisk that shares overlaps with [TONEDISK](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan) (aka [WispRider](https://thehackernews.com/2023/07/malicious-usb-drives-targetinging.html)), another USB worm framework under the TONESHELL family. It's mainly used to detect new and existing USB devices connected to the host, using it as a means of propagation.

Specifically, it moves the existing files on the USB into a new sub-directory, effectively tricking the victim to click on the malicious payload on a new machine by either setting its name to the volume name of the USB device, or "USB.exe." Once the malware is launched, the files are copied back to their original location.

A notable aspect of the malware is that it's geofenced to execute only on public IP addresses geolocated to Thailand. SnakeDisk also serves as a conduit to drop Yokai, a backdoor that sets up a reverse shell to execute arbitrary commands. It was previously detailed by Netskope in December 2024 in intrusions targeting Thai officials.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Yokai shows overlaps with other backdoor families attributed to Hive0154, such as PUBLOAD/PUBSHELL and TONESHELL," IBM said. "Although those families are clearly separate pieces of malware, they roughly follow the same structure and use similar techniques to establish a reverse shell with their C2 server."

The use of SnakeDisk and Yokai likely points to a sub-group within Mustang Panda that's hyper-focused on Thailand, while also underscoring the continued evolution and refinement of the threat actor's arsenal.

"Hive0154 remains a highly capable threat actor with multiple active subclusters and frequent development cycles," the company concluded. "This group appears to maintain a considerably large malware ecosystem with frequent overlaps in both malicious code, techniques used during attacks, as well as targeting."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[IBM X-Force](https://thehackernews.com/search/label/IBM%20X-Force)[Malware](https://thehackernews.com/search/label/Malware)[Mustang Panda](https://thehackernews.com/search/label/Mustang%20Panda)[network security](https://thehackernews.com/search/label/network%20security)[Thailand](https://thehackernews.com/search/label/Thailand)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

...