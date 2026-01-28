---
title: China-Linked Hackers Have Used the PeckBirdy JavaScript C2 Framework Since 2023
url: https://thehackernews.com/2026/01/china-linked-hackers-have-used.html
source: The Hacker News
date: 2026-01-27
fetch_date: 2026-01-28T03:35:28.008491
---

# China-Linked Hackers Have Used the PeckBirdy JavaScript C2 Framework Since 2023

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

# [China-Linked Hackers Have Used the PeckBirdy JavaScript C2 Framework Since 2023](https://thehackernews.com/2026/01/china-linked-hackers-have-used.html)

**Ravie Lakshmanan**Jan 27, 2026Web Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy5RzwPMRj7i78zsLQinlntZrTjk6KP4CdBUnLfoumPUoYEQV_9WrqrB-5EKXD_vxcZSEDlUqb2zaHZ0tf90W9QL8lWPLCWdjZ2jhYmzIlsNSI_1HEDKiFom8VdHK_jjRz7JZWebAXTXHkVgMFto-WkrlFuCgaoU6mo871w3hP5vG0Alg3A4VmVScWjCW-/s1700-e365/chinese-hackers.jpg)

Cybersecurity researchers have discovered a [JScript](https://en.wikipedia.org/wiki/JScript)-based command-and-control (C2) framework called **PeckBirdy** that has been put to use by China-aligned APT actors since 2023 to target multiple environments.

The flexible framework has been put to use against Chinese gambling industries and malicious activities targeting Asian government entities and private organizations, according to Trend Micro.

"PeckBirdy is a script-based framework which, while possessing advanced capabilities, is implemented using JScript, an old script language," researchers Ted Lee and Joseph C Chen [said](https://www.trendmicro.com/en_us/research/26/a/peckbirdy-script-framework.html). "This is to ensure that the framework could be launched across different execution environments via LOLBins (living-off-the-land binaries)."

The cybersecurity company said it identified the PeckBirdy script framework in 2023 after it observed multiple Chinese gambling websites being injected with malicious scripts, which are designed to download and execute the primary payload in order to facilitate the remote delivery and execution of JavaScript.

The end goal of this routine is to serve fake software update web pages for Google Chrome so as to trick users into downloading and running bogus update files, thereby infecting the machines with malware in the process. This activity cluster is being tracked as SHADOW-VOID-044.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

SHADOW-VOID-044 is one of the two temporary intrusion sets detected using PeckBirdy. The second campaign, observed first in July 2024 and referred to as SHADOW-EARTH-045, involves targeting Asian government entities and private organizations -- including a Philippine educational institution -- injecting PeckBirdy links into government websites to likely serve scripts for credential harvesting on the website.

"In one case, the injection was on a login page of a government system, while in another incident, we noticed the attacker using MSHTA to execute PeckBirdy as a remote access channel for lateral movement in a private organization," Trend Micro said. "The threat actor behind the attacks also developed a .NET executable to launch PeckBirdy with ScriptControl. These findings demonstrate the versatility of PeckBirdy's design, which enables it to serve multiple purposes."

What makes PeckBirdy notable is its flexibility, allowing it to run with varying capabilities across web browsers, MSHTA, WScript, Classic ASP, Node JS, and .NET (ScriptControl). The framework's server is configured to support multiple APIs that make it possible for clients to obtain landing scripts for different environments via an HTTP(S) query.

The API paths include an "ATTACK ID" value -- a random but predefined string with 32 characters (e.g., o246jgpi6k2wjke000aaimwбe7571uh7) -- that determines the PeckBirdy script to be retrieved from the domain. Once launched, the PeckBirdy determines the current execution context and then proceeds to generate a unique victim ID and persist it for subsequent executions.

The initialization step is followed by the framework attempting to figure out what communication methods are supported in the environment. PeckBirdy uses the WebSocket protocol to communicate with the server by default. However, it can also employ Adobe Flash ActiveX objects or Comet as a fallback mechanism.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjthR6D4AkeQwGfx7QYshkl70OL0tDCX5EUZMBpRX-b1PpwU-qbriovK7vBukHIOaBjSUkERJMXFAlTFU3xrqLCzVUxhaB0yv9opsHSHzj_7sUWeVKtV-0uRadu8pKrr-BDi0zmdBRTcFnk5ej9q_eCoeqCaxyeWsKX4OwW92ZTdxeyechfH_5PaAo5nYxx/s1700-e365/tm.jpg)

After a connection has been initiated with the remote server, passing along the ATTACK ID and victim ID values, the server responds with a second-stage script, one of which is capable of stealing website cookies. One of PeckBirdy's servers associated with the SHADOW-VOID-044 campaign has been found to host additional scripts -

* An exploitation script for a Google Chrome flaw in the V8 engine ([CVE-2020-16040](https://chromereleases.googleblog.com/2020/12/stable-channel-update-for-desktop.html), CVSS score: 6.5) that was patched in December 2020
* Scripts for social engineering pop-ups that are designed to trick victims into downloading and executing malicious files
* Scripts for delivering backdoors that are executed via Electron JS
* Scripts to establish reverse shells via TCP sockets

Further infrastructure analysis has led to the identification of two backdoors dubbed HOLODONUT and MKDOOR -

* HOLODONUT, a .NET-based modular backdoor that's launched using a simple downloader named NEXLOAD and is capable of loading, running, or removing different plugins received from the server
* MKDOOR, a modular backdoor that's capable of loading, running, or uninstalling different modules received from the server

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

It's suspected that SHADOW-VOID-044 and SHADOW-EARTH-045 could be linked to different China-aligned nation-state actors. This assessment is based on the following clues -

* The presence of [GRAYRABBIT](https://www.virusbulletin.com/conference/vb2024/abstracts/down-grayrabbit-hole-exposing-unc3569-and-its-mastermind/), a backdoor previously deployed by [UNC3569](https://thehackernews.com/2024/04/researchers-identify-multiple-china.html) alongside DRAFTGRAPH and [Crosswalk](https://thehackernews.com/2024/06/chinese-cyber-espionage-group-exploits.html) following the exploitation of N-day security flaws, on a server operated by SHADOW-VOID-044
* HOLODONUT is said to share links to another backdoor, [WizardNet](https://thehackernews.com/2025/04/chinese-hackers-abuse-ipv6-slaac-for.html), ...