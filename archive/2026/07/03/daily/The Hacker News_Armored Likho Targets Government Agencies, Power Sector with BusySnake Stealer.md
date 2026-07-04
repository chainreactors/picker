---
title: Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer
url: https://thehackernews.com/2026/07/armored-likho-targets-government.html
source: The Hacker News
date: 2026-07-03
fetch_date: 2026-07-04T05:49:52.613320
---

# Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Armored Likho Targets Government Agencies, Power Sector with BusySnake Stealer](https://thehackernews.com/2026/07/armored-likho-targets-government.html)

**Ravie Lakshmanan**Jul 03, 2026Infostealer / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTOYmjevwtg2njZKRnBeTtT1fSpmOD45a_apqSQWJJQH8N0HtftQ_Tj3mCC6dfysokuddsTPVCKKM4hd4Trjs6dPn1tvUNi4gWvj_OQevLSDqNfuGOK87WNAQSRVZSEOOLoo0Ip4IQQTa14eqh7J7rPo-8edHwoNORqqrcgtFAT-LySviPfbahvJDMDk_T/s1700-e365/power.jpg)

A previously undocumented threat actor known as **Armored Likho** has been attributed to cyber attacks targeting government agencies and the electric power sector across Russia, Brazil, and Kazakhstan.

"Armored Likho blends financially motivated campaigns targeting private individuals with targeted cyber espionage aimed at organizations," Kaspersky [said](https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/) in a technical analysis published today. "Their toolkit features obfuscated, modular RATs and infostealers specifically engineered to bypass dynamic analysis."

The attacks are also characterized by the use of tools like Go2Tunnel for remote access and network tunneling. The wide variety of tools in its arsenal allows the threat actor to maintain persistent access to compromised hosts, steal credentials and sensitive data, and dynamically deliver modules tailored to the victim's profile.

The Russian cybersecurity vendor said Armored Likho shares possible overlaps with a threat cluster tracked by BI.ZONE under the moniker Eagle Werewolf, which has been active since May 2023. The hacking group has a track record of targeting government and defense organizations, specifically those involved in UAV development and manufacturing, using droppers, remote access trojans (RATs), and utilities for establishing SSH tunnels.

"Threat actors may use compromised Telegram channels to distribute the malware," BI.ZONE [notes](https://gti.bi.zone/) in its description of the threat actor. "While the group's primary motivation is cyber espionage, campaigns aimed at stealing funds from victims have also been recorded."

Back in February 2026, Eagle Werewolf was [observed](https://thehackernews.com/2026/04/phantomcore-exploits-trueconf.html) compromising a drone‑focused Telegram channel to distribute AquilaRAT via a Rust dropper that masquerades as a checklist for Starlink device activation. Also put to use in its attacks is a tool referred to as Go2Tunnel to establish a reverse SSH tunnel to a command-and-control (C2) server using a private key.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The latest findings show that the threat actor has also employed a previously unreported Python-based information stealer named BusySnake Stealer targeting Windows systems, one version of which includes a module for stealing cookies from web browsers. The exact origins of Armored Likho remain unknown.

The starting point of the attack chain is a spear-phishing email that uses lures related to official government notices or social programs to distribute a RAR archive containing EXE binaries that serve as droppers for additional payloads retrieved from a GitHub repository, including the stealer payload.

The dropper malware also creates two Visual Basic Script (VBScript) files that are responsible for erasing traces of the initial execution as well as launching the stealer by means of a scheduled task.

Alternate chains utilize Windows shortcuts (LNK) instead of EXE payloads that weaponize a now-patched vulnerability related to how Windows handles such files, resulting in remote code execution. The flaw, tracked as [CVE-2025-9491](https://thehackernews.com/2025/12/microsoft-silently-patches-windows-lnk.html) (aka ZDI-CAN-25373), was addressed by Microsoft as part of its Patch Tuesday updates for November 2025. Evidence unearthed by Trend Micro last year revealed that the shortcoming had been weaponized by a dozen hacking groups since 2017.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjajcEszVn2a3upcLHhbQGEtTdSdJvSA_2ugcB4KzpeMjp3-Pz2t7QFTPd-mpHE80MLU0XRKe5lMYsLG2e4Tp7AndNCm1xZh1kHufn9TT-2l1ams39eKHYWxn8orLDQHGjx8M-42L5Wi3NF-CM8m00CCw_TCSt3V3kKPWcqI4H52zg-AmI3gf_7ChR-Gf70/s1700-e365/headers.png)

In the attack chain documented by Kaspersky, the shortcut vulnerability is abused to trigger the execution of an obfuscated PowerShell command that launches a loader responsible for displaying a decoy document, while preparing the environment for the execution of the Python stealer. The malware then establishes persistence through a combination of a VBScript file and a scheduled task, as before.

The stealer, called BusySnake, implements multiple evasion techniques to complicate static analysis and sidestep detection. Its primary goal is to establish communication with a C2 server and then await incoming instructions. It also supports the following functionality -

* Steal data from the system clipboard.
* Enumerate files across the system and log their metadata in a local database.
* Upload user documents to the C2 server.
* Capture screenshots and stage them in a local directory.
* Archive captured screenshots and remove previously created archives from the disk.
* Prevent multiple instances of the stealer from running concurrently on the infected host.
* Ensure persistence by checking if the scheduled task exists, and if not, drop a VBScript to register a new scheduled task.

Furthermore, the commands issued by the C2 server allow it to take screenshots at a designated interval, log keystroke data, gather cryptocurrency wallet files with a JSON extension, collect Telegram session and credential data, establish a reverse SSH tunnel using Go2Tunnel, install RustDesk, and extract cookies from Mozilla Firefox and Chromium-based browsers, along with passwords.

If RustDesk is already installed on the machine...