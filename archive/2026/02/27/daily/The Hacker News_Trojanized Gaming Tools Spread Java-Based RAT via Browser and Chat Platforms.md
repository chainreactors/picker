---
title: Trojanized Gaming Tools Spread Java-Based RAT via Browser and Chat Platforms
url: https://thehackernews.com/2026/02/trojanized-gaming-tools-spread-java.html
source: The Hacker News
date: 2026-02-27
fetch_date: 2026-02-28T04:01:40.735463
---

# Trojanized Gaming Tools Spread Java-Based RAT via Browser and Chat Platforms

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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Trojanized Gaming Tools Spread Java-Based RAT via Browser and Chat Platforms](https://thehackernews.com/2026/02/trojanized-gaming-tools-spread-java.html)

**Ravie Lakshmanan**Feb 27, 2026Endpoint Security / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEillKgTghwZEhxrFFKb47xsniaaZYeDlISTMJYxMDr_82YETlHvM5M0XWXjizlkv1MgSAzkIEDbOcvfPsjsOaxRHvzl4-7LWTmKR6awOPB_FidaOgq0xhHslZbEJ7zh0Hq6CV0NJ8LUY-SDyA-nF6SeQ6Zzu-qrlWWMFsVg2n3yDRj0hcIPYEPLw6eAmadL/s1700-e365/remote.jpg)

Threat actors are luring unsuspecting users into running trojanized gaming utilities that are distributed via browsers and chat platforms to distribute a remote access trojan (RAT).

"A malicious downloader staged a portable Java runtime and executed a malicious Java archive (JAR) file named jd-gui.jar," the Microsoft Threat Intelligence team [said](https://x.com/MsftSecIntel/status/2027070355487997998) in a post on X. "This downloader used PowerShell and living-off-the-land binaries (LOLBins) like cmstp.exe for stealthy execution."

The attack chain is also designed to evade detection by deleting the initial downloader and by configuring Microsoft Defender exclusions for the RAT components.

Persistence is achieved by means of a scheduled task and Windows startup script named "world.vbs," before the final payload is deployed on the compromised host. The malware, per Microsoft, is a "multi-purpose malware" that acts as a loader, runner, downloader, and RAT.

Once launched, it connects to an external server at "79.110.49[.]15" for command-and-control (C2) communications, allowing it to exfiltrate data and deploy additional payloads.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

As ways to defend against the threat, users are advised to audit Microsoft Defender exclusions and scheduled tasks, remove malicious tasks and startup scripts, isolate affected endpoints, and reset credentials for users active on compromised hosts.

The disclosure comes as BlackFog disclosed details of a new Windows RAT malware family called Steaelite that was first advertised on criminal forums in November 2025 as a "best Windows RAT" with "fully undetectable" (FUD) capabilities. It's compatible with both Windows 10 and 11.

Unlike other off-the-shelf RATs sold to criminal actors, Steaelite bundles together data theft and ransomware, packaging them into one web panel, with an Android ransomware module on the way. The panel also incorporates various developer tools to facilitate keylogging, client-to-victim chat, file searching, USB spreading, wallpaper modification, UAC bypass, and [clipper functionality](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html).

Other notable features include removing competing malware, disabling Microsoft Defender, or configuring exclusions, and installing persistence methods.

As for its main capabilities, Steaelite RAT supports remote code execution, file management, live streaming, webcam and microphone access, process management, clipboard monitoring, password theft, installed program enumeration, location tracking, arbitrary file execution, URL opening, DDoS attacks, and VB.NET payload compilation.

"The tool gives operators browser-based control over infected Windows machines, covering remote code execution, credential theft, live surveillance, file exfiltration, and ransomware deployment from a single dashboard," security researcher Wendy McCague [said](https://www.blackfog.com/steaelite-rat-double-extortion-from-single-panel/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"A single threat actor can browse files, exfiltrate documents, harvest credentials, and deploy ransomware from the same dashboard. This enables complete double extortion from one tool."

In recent weeks, threat hunters have also discovered two new RAT families tracked as [DesckVB RAT](https://github.com/ShadowOpCode/DesckVB-RAT) and [KazakRAT](https://ctrlaltintel.com/threat%20research/KazakRAT/) that enable comprehensive remote control over infected hosts and even selectively deploy capabilities post-compromise. According to Ctrl Alt Intel, KazakRAT is suspected to be the work of a suspected state-affiliated cluster targeting Kazakh and Afghan entities as part of a persistent campaign ongoing since at least August 2022.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft Defender](https://thehackernews.com/search/label/Microsoft%20Defender), [ransomware](https://thehackernews.com/search/label/ransomware), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [windows security](https://thehackernews.com/search/label/windows%20security)

Trending News

[![Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](data...