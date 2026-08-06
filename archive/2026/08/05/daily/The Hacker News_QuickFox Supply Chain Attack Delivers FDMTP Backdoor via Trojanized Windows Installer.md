---
title: QuickFox Supply Chain Attack Delivers FDMTP Backdoor via Trojanized Windows Installer
url: https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:53.387859
---

# QuickFox Supply Chain Attack Delivers FDMTP Backdoor via Trojanized Windows Installer

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

![cybersecurity](data:image/svg+xml;base64...)

# [QuickFox Supply Chain Attack Delivers FDMTP Backdoor via Trojanized Windows Installer](https://thehackernews.com/2026/08/quickfox-supply-chain-attack-delivers.html)

**Ravie Lakshmanan**Aug 05, 2026Supply Chain Attack / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFQzlCdxoVUtdNgowwmPFaISlBF7Y2HsG1BQf3b-UJDQzRbPB249_W6rwU_-TSW1NES4OI-12R1z3tXQ-QlZv8cEaagpyLJVYz48Etb9W0MtuNp9BTL_13-5Wg95kz-Ey5iZ288mTkPt_5pbsxoh7Kv2KrmHqj_Tqb0KR9NSzz-jO2DuoTLthh6Dn3FUIh/s1700-e365/quick.jpg)

Cybersecurity researchers have disclosed what has been described as a "long-standing supply chain attack" on QuickFox, a virtual private network (VPN) and network acceleration tool designed for overseas Chinese users.

According to Fortinet FortiGuard Labs, the supply chain attack has been ongoing since at least August 2025 and involves a trojanized version of the application to deliver [FDMTP](https://thehackernews.com/2024/09/mustang-panda-deploys-advanced-malware.html), a backdoor that has been put to use by a Chinese state-sponsored threat actor tracked as Mustang Panda.

"The attack is delivered via a modified Electron renderer HTML file used to download and execute a JavaScript-based loader," the FortiGuard Incident Response Team [said](https://www.fortinet.com/blog/threat-research/quickfox-supply-chain-attack-used-to-deploy-fdmtp-implant). "Upon execution, the JavaScript loader fingerprints the victim endpoint to determine if it's a valid target before downloading and installing an FDMTP implant."

Following responsible disclosure, QuickFox has removed the malicious components from their Windows installer with the release of version 3.59.6. The changes are said to have been included sometime between July 25 and August 13, 2025, with 3.0.51.0 being the earliest affected version. Evidence indicates that the campaign solely targeted Windows users.

The malicious code introduced to the installer executable involves two lines of JavaScript in a single HTML file, causing it to execute two JavaScript payloads -- "firebase-app-compat.js" and "firebase-analytics-compat.js" -- staged on "cdns3.51quickfox[.]cn," which masquerades as the official QuickFox domain ("51quickfox[.]com") to evade detection.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Of the two payloads, "firebase-analytics-compat.js" contains legitimate Google Firebase code, while "firebase-app-compat.js" is a heavily obfuscated payload that mimics the Firebase SDK, but harbors functionality to ascertain if the affected endpoint is running Windows, check with a command-and-control (C2) server to ensure the endpoint is not re-infected, and run the "[tasklist](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist)" command to obtain a list of currently running processes.

This list is then checked for specific process names, specifically Steam ("steam.exe"), and aborts execution if it is present. It also checks if there exists at least one process name that matches 26 domestic applications, cryptocurrency wallets, developer tools, and enterprise software.

This includes Xshell, MobaXterm, Tabby Terminal, Navicat, DBeaver, Git, IntelliJ IDEA, Sublime Text, Notepad++, Microsoft Visual Studio Code, Exodus Wallet, Binance, Ledger Live, Trezor Suite, Telegram, SafeW, Ai Fanyi, Haiwang Chuhai, Yi Fanyi, Kuai Fanyi, and HaiYiTong.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEaEUjzTW3iMWJuYXlCBzmRWs4QGaTXJTlOArPusUtCuYVUWZ4oGicGEqmPNriT0BUIAGZTdkmSgCsO7b81hupTR3CCs4YtCiruqnev72HqxA5NgmVZQP3d5dmEnLIjb8Hnnmll1fFrmVLQTjzbgzOj5WI16Ikordu9xy5Qsd-wasH2xgT3AXkYeNnPXsM/s1700-e365/exe.png)

Once both these conditions are met, the script proceeds to download the next stage payload, a ZIP archive from the same aforementioned domain. Two different generations of the ZIP payload have been identified -

* Generation 1 (Available from at least September 2025), which uses DLL side-loading to launch a malicious DLL embedding FDMTP ("Client.dll")
* Generation 2 (Available from May 2026), which also uses DLL side-loading to launch a malicious DLL that acts as a loader for an encrypted file ("update.bin") that contains FDMTP

FDMTP was [first highlighted](https://thehackernews.com/2024/09/mustang-panda-deploys-advanced-malware.html) by Trend Micro in September 2024 as a secondary tool distributed via a downloader known as PUBLOAD. In the latest iteration, it first attempts to obtain a C2 connection, following which the server responds with a "GetInfo" request to gather basic information from the victim's device.

The collected data contains the window title of the topmost active program, installed antivirus programs, .NET Framework runtime version, network and operating system information, current username, and details about the implant itself, such as file full path, version, process ID, and hosting process name.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Once this information is packaged and exfiltrated, the C2 server sends a request to list running processes in a further attempt to filter out certain endpoints in furtherance of the threat actor's goals. Additionally, the malware is responsible for loading plugins received from the server, allowing the operators to expand its functionality at will.

Some of the payloads, as [detailed by Darktrace](https://thehackernews.com/2026/05/weekly-recap-exchange-0-day-npm-worm.html#:~:text=Mustang%20Panda%20Delivers%20Updated%20FDMTP%20Tool) earlier this year, facilitate the management of scheduled tasks, oversee Registry persistence, and remotely fetch files or commands.

Although Fortinet has not attributed the campaign to a specific threat actor, it acknowledged tactical overlaps with Mustang Panda, a Chinese nation-state adversary known for its reliance on DLL side-loading techniques to deploy malware.

Given that QuickFox's primary user base is Chinese international students and expats, it's suspected that the campaign may have singled out Chinese citizens residing outside China.

"A competing hypothesis is that this campaign aimed to target professionals required to interact with Chinese native speakers, p...