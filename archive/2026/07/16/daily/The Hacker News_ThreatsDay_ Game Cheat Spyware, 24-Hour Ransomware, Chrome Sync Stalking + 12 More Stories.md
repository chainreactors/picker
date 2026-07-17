---
title: ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories
url: https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:23.661861
---

# ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories

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

# [ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories](https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html)

**Ravie Lakshmanan**Jul 16, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioBa_Q-TYfQvhOH0gqZxwAzgn_QnC9YSD6GYI3-z53LVjJSL1MDl4Af_DSeuIA33luHnEkGIGe9eXbCGvyWZ2zfOELZLhLAJtAcCTzIrpEPPU2f-7hvztkeHhA89Fb3aTq7b-0HHHVSPUsmUKXOPbX17rwMGjB75yG_r4-9vyarYK77pmdgzy3YeIn46M4/s1700-e365/threatsday-recap.jpg)

A lot of this week’s trouble starts with something that looks close enough.

A familiar repo. A useful installer. A harmless sync setting. Then the handoff goes bad, the box starts talking to someone else, and the damage moves faster than the explanation.

Old bugs are back, weak defaults are earning their keep, and some attack paths are so plain they barely feel like research. Here’s the mess.

1. Game cheats drop spyware

   [11 Malicious NuGet Tools Masquerade as Game Cheats to Drop Windows Surveillance Payload](https://socket.dev/blog/11-malicious-nuget-tools-pose-as-game-cheats)

   Cybersecurity researchers 11 malicious NuGet packages published as .NET command-line tools that present themselves as game utilities, bots, and "panels," each of which act as a first-stage downloader responsible for fetching and executing a second-stage Python payload named "pepesoft.exe" from GitHub Releases and Hugging Face paths under the username "pepegit666," along with a dormant BitTorrent fallback mechanism built into it. "The recovered payloads use downloader-supplied AWS-style key material to retrieve remote configuration, authenticate to Google Sheets, bind activations to hardware, and honor a remote HWID/UUID ban-list," Socket [said](https://socket.dev/blog/11-malicious-nuget-tools-pose-as-game-cheats). "In the three direct-bytecode payloads, the larger game-automation application also exposes Telegram bot commands that can send screenshots back to the configured chat."
2. Fake installers deploy RATs

   [UAT-11795 Deploys Starland RAT and Bespoke WLDR C2 Implant](https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/)

   UAT-11795, a sophisticated, Russian-speaking, financially motivated adversary, has been observed conducting a malicious campaign targeting users in the U.S. and Europe since at least June 2025. The activity delivers a Python-based remote access tool (RAT) dubbed Starland RAT and a command-and-control (C2) memory implant known as WLDR agent using trojanized installer lures for software like developer tooling, IT administration utilities, enterprise collaboration platforms, and consumer gaming applications (e.g., MobaXterm, WebEx, Zoom, DBeaver, and FaceIT). "The WLDR agent is a sophisticated PowerShell-based C2 memory implant that features encrypted beaconing, task queuing, and a Runspace execution engine for executing additional payloads," Cisco Talos [said](https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/). Alternatively, UAT-11795 has been linked to the deployment of [CastleStealer](https://thehackernews.com/2026/06/new-oxloader-loader-uses-malicious.html) and Remcos RAT. The malware is designed to target victims' credentials and cryptocurrency wallet assets, harvest Active Directory information, and establish a persistent connection to the victims' machines from the C2 server, likely with an aim to deliver and execute further payloads. The majority of the infections are in the U.S., with fewer potential impacts recorded in Germany, Romania, and Venezuela. The attack chain makes use of ClickFix lures to distribute HTA scripts, which then download and run trojanized installers to deliver Starland RAT, which then uses "curl.exe" to execute a PowerShell stager for decrypting and running WLDR agent. In recent weeks, ClickFix has also served as a conduit for [TELEPUZ](https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html), a modular malware, and [ClickLock Stealer](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/), a macOS-focused information and cryptocurrency wallet stealer targeting users in Europe, North America, and MEA. "ClickLock Stealer targets data from 8 browsers, 31 crypto wallet browser extensions, 7 password manager extensions, 8 desktop wallet applications, extracts blockchain addresses across 6 chains, macOS Keychain, shell history, and FTP credentials," Group-IB said.
3. Network encrypted within hours

   [New Spirals Ransomware Encrypts Victim Network Within 24 Hours](https://www.security.com/threat-intelligence/ransomware-spirals-extortion)

   An IT services company in South Asia was targeted by a previously undocumented ransomware family called Spirals in June 2026. "The Rust-based payload is either a new ransomware threat or one purpose-built for this attack," Broadcom's Symantec and Carbon Black Threat Hunter Team [said](https://www.security.com/threat-intelligence/ransomware-spirals-extortion). "Less than 24 hours after the initial breach, the ransomware payload was being pushed to machines on the network." The attacker is said to have obtained initial access by compromising an internet-facing IIS web server and uploading an ASP.NET web shell. Over the next three hours, they established persistent access, conducted reconnaissance, uninstalled endpoint security software, dumped the Security Account Manager (SAM) hive, and set up covert remote access prior to deploying the payload across the network using PsExec. The ransom note seeks to apply pressure by threatening to publish stolen data after six days if a ransom is not paid and directs victims to a Tor portal for negotiations. The actor behind the attack remains unknown.
4. Actively exploited flaws

   [CISA Adds Oracle and KNX Association KNX Protocol Flaws to KEV Catalog...