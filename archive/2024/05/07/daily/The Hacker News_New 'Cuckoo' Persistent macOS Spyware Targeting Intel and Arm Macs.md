---
title: New 'Cuckoo' Persistent macOS Spyware Targeting Intel and Arm Macs
url: https://thehackernews.com/2024/05/new-cuckoo-persistent-macos-spyware.html
source: The Hacker News
date: 2024-05-07
fetch_date: 2025-10-06T17:19:57.116512
---

# New 'Cuckoo' Persistent macOS Spyware Targeting Intel and Arm Macs

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

# [New 'Cuckoo' Persistent macOS Spyware Targeting Intel and Arm Macs](https://thehackernews.com/2024/05/new-cuckoo-persistent-macos-spyware.html)

**May 06, 2024**Ravie LakshmananSpyware / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_F1KzJ-rXXDfpfsaOUDosDvEa2Iwig46Nm0LlpvTguCzmNRDH1jUtpku3ElPR4QkVdU9ZULPOYYtstxSDYnLyXV6sUZ4FZliYlJEdfnlwwW4MLtlcpW0JfYqfly_O861Gbam37tqnvNNXzShHY1mIT1IIvqyWFhDP3_etN0NJjNu0g0lrPk47lMpHY9j1/s790-rw-e365/macos.png)

Cybersecurity researchers have discovered a new information stealer targeting Apple macOS systems that's designed to set up persistence on the infected hosts and act as a spyware.

Dubbed **Cuckoo** by Kandji, the malware is a universal Mach-O binary that's capable of running on both Intel- and Arm-based Macs.

The exact distribution vector is currently unclear, although there are indications that the binary is hosted on sites like dumpmedia[.]com, tunesolo[.]com, fonedog[.]com, tunesfun[.]com, and tunefab[.]com that claim to offer free and paid versions of applications dedicated to ripping music from streaming services and converting it into the MP3 format.

The disk image file downloaded from the websites is responsible for spawning a bash shell to gather host information and ensuring that the compromised machine is not located in Armenia, Belarus, Kazakhstan, Russia, Ukraine. The malicious binary is executed only if the locale check is successful.

It also establishes persistence by means of a LaunchAgent, a technique previously adopted by different malware families like [RustBucket](https://thehackernews.com/2023/07/beware-new-rustbucket-malware-variant.html), [XLoader](https://thehackernews.com/2023/08/new-variant-of-xloader-macos-malware.html), [JaskaGO](https://thehackernews.com/2023/12/new-go-based-jaskago-malware-targeting.html), and a [macOS backdoor](https://thehackernews.com/2024/01/experts-warn-of-macos-backdoor-hidden.html) that shares overlaps with ZuRu.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Cuckoo, like the [MacStealer macOS stealer malware](https://thehackernews.com/2023/03/new-macstealer-macos-malware-steals.html), also leverages osascript to display a fake password prompt to trick users into entering their system passwords for privilege escalation.

"This malware queries for specific files associated with specific applications, in an attempt to gather as much information as possible from the system," researchers Adam Kohler and Christopher Lopez [said](https://blog.kandji.io/malware-cuckoo-infostealer-spyware).

It's equipped to run a series of commands to extract hardware information, capture currently running processes, query for installed apps, take screenshots, and harvest data from iCloud Keychain, Apple Notes, web browsers, crypto wallets, and apps like Discord, FileZilla, Steam, and Telegram.

"Each malicious application contains another application bundle within the resource directory," the researchers said. "All of those bundles (except those hosted on fonedog[.]com) are signed and have a valid Developer ID of Yian Technology Shenzhen Co., Ltd (VRBJ4VRP)."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm3noaOGB8broLvcEwrm9P8ak-jGg5hF3PGGyCqpMvkCL-DnBG9WSZk8W4xEMVyZSAUMvj_WkrYG6P0bFOEmHEH3YDajmCZ8xh4fxRdN_4Z1aNmUB5SA_J0fe3QVGhZs_2IPqwtLx98yqwKryX2Z9ZKQu01U1gupGFq3Njhezuxrgng8Vxn5ThsaNVltHK/s790-rw-e365/map.png)

"The website fonedog[.]com hosted an Android recovery tool among other things; the additional application bundle in this one has a developer ID of FoneDog Technology Limited (CUAU2GTG98)."

The disclosure comes nearly a month after the Apple device management company also exposed another stealer malware codenamed [CloudChat](https://blog.kandji.io/cloudchat-infostealer) that masquerades as a privacy-oriented messaging app and is capable of compromising macOS users whose IP addresses do not geolocate to China.

The malware works by grabbing crypto private keys copied to the clipboard and data associated with wallet extensions installed on Google Chrome.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It also follows the discovery of a new variant of the notorious [AdLoad malware](https://thehackernews.com/2023/08/this-malware-turned-thousands-of-hacked.html) written in Go called Rload (aka Lador) that's engineered to evade the Apple XProtect malware signature list and is compiled solely for Intel x86\_64 architecture.

"The binaries function as initial droppers for the next stage payload," SentinelOne security researcher Phil Stokes [said](https://www.sentinelone.com/blog/macos-adload-prolific-adware-pivots-just-days-after-apples-xprotect-clampdown/) in a report last week, adding the specific distribution methods remain presently obscure.

That having said, these droppers have been observed typically embedded in cracked or trojanized apps distributed by malicious websites.

AdLoad, a widespread adware campaign afflicting macOS since at least 2017, is known for hijacking search engine results and injecting advertisements into web pages for monetary gain by means of an adversary-in-the-middle web proxy to redirect user's web traffic through the attacker's own infrastructure.

### Update: More Cuckoo Artifacts Spotted

Cybersecurity firm SentinelOne, in a new analysis, said it has observed a spike in Cuckoo samples and trojanized applications delivering the C++-based malware since its emergence late last month.

"The trojanized apps are various kinds of 'potentially unwanted programs' offering dubious services such as PDF or music converters, cleaners, and uninstallers," security researcher Phil Stokes [said](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/). "The latest version of XProtect, version 2194, does not block execution of Cuckoo Stealer malware."

The malware's theft of macOS ...