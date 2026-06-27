---
title: Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks
url: https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html
source: The Hacker News
date: 2026-06-26
fetch_date: 2026-06-27T05:52:31.673312
---

# Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Google Details Turla's New STOCKSTAY Backdoor Used in Ukraine Espionage Attacks](https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html)

**Ravie Lakshmanan**Jun 26, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9SthtlfUvEkaX0iZanYdYTAOV5hgm44yCwHu_3GCaoa11rO-GkO9oc0_qN9JGw2n86dsEsN_sdaYt2ra_4I_dQ57ja0kiUeYtkg1eY8ZJtu45oKtN-TqWLdKudnJPFQQFGPReCfu1xcfHGgfqgtLe8zyFlEoMnO2AwnsEsosf9LCZS9gJHq58Q8OcPlWP/s1700-e365/STOCKSTAY.jpg)

The Russian state-sponsored threat actor known as Turla has been attributed to a previously undocumented .NET backdoor called **STOCKSTAY** that has been deployed against government and military organizations in Ukraine, and entities that have an interest in Italian foreign policy.

Describing the Windows backdoor as continually developed by the hacking group, Google Threat Intelligence Group (GTIG) said the cyber espionage tool shares significant code and functional overlaps with [Kazuar](https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html), a staple implant put to use by the adversary since 2017. Suspected development activity of malware dates back to December 2022.

"STOCKSTAY is a multi-component backdoor written in .NET, using the Windows Forms framework, which communicates with its command-and-control (C2) via a secure WebSocket connection, utilizing the open-source [websocket-sharp](https://github.com/sta/websocket-sharp) library," GTIG [said](https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering).

"STOCKSTAY consists of several distinct components that communicate with one another via an inter-process communication (IPC) channel, based on the exchange of [WM\_COPYDATA](https://learn.microsoft.com/en-us/windows/win32/dataxchg/wm-copydata) messages."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Evidence indicates that the implant was originally designed to mimic a stock market data viewing tool, before being adapted to masquerade as other harmless programs like PDF viewers and calculator utilities. The starting point is a downloader component codenamed STOCKSTAY.MARKETMAKER that installs and executes three additional modules -

* **STOCKSTAY.STOCKBROKER**, a proxy-aware tunneler that facilitates network communication capabilities to the wider STOCKSTAY suite by establishing a secure WebSocket connection to a specified remote server.
* **STOCKSTAY.STOCKTRADER**, the main backdoor that enables information gathering.
* **STOCKSTAY.STOCKMARKET**, an orchestrator or controller that parses the backdoor's configuration to set several options regarding the malware's execution, such as the WebSocket server, time interval, and the days it's not supposed to work. It also communicates with STOCKSTAY.STOCKBROKER to provide the server details and receive messages via the established WebSocket connection, as well as STOCKSTAY.STOCKTRADER to issue commands to be run on the compromised host.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2jpA4sC2nD22pzqW5RYgZr8eP95jIASVMGntCgzA1J1W3uFIZeUYWX7JP68Ef4xDlda3G-lg0yNhvq8Vqr1iFFZ-xA6BLs_RXL_mrkLgw9MTwsRdr4HMLXMfJqjpe3nJNL5ZjNFzmRO1kaV8LZ6RRhWkLaDb7D_WK4rNveN6pJu4v9VkbBugxZ1FD1iIj/s1700-e365/google-1.png) |
| STOCKSTAY malware architecture |

Some of the support commands of STOCKSTAY.STOCKTRADER is listed below -

* Del, to delete the specified files
* Dir, to enumerate the specified directories
* Get, to fetch one or more specified files matching certain extensions
* MkDir, to make one or more directories
* RmDir, to delete the specified directories
* Image, to perform a screen capture of the device's screen
* MultyTask, to run a semi-colon-separated list of tasks at once
* Put, to upload a file to the device
* RegRead, to read a Windows Registry value
* RegDelete, to delete a Windows Registry value
* RegWrite, to set a Windows Registry value
* Run, to execute a new process
* Sysinfo, to gather system information
* UnpackArchive, to extract the specified ZIP file to its current directory

Google said it identified a publicly accessible GitHub repository ("[ChikenFresh/google-ai-labs-it](https://github.com/ChikenFresh/google-ai-labs-it)") containing a Python implementation of the victim-facing STOCKSTAY WebSocket server controller that's responsible for handling inbound messages from a connected client and logging its IP address.

"The inability for the server to decrypt inbound messages prevents introspection by platform operators, and further obfuscates the location of the threat actor’s dedicated infrastructure," GTIG noted. "This architecture somewhat resembles Turla's multi-hop Kazuar C2 infrastructure."

Attacks distributing STOCKSTAY have consistently leveraged academic- or diplomatic-themed lures to target government and military organizations within Ukraine, with early versions of the backdoor used in attacks aimed at entities in Italy, the Netherlands, Poland, and Germany. That said, it's unknown which European entities were singled out in these attacks.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifds_fej3eLUylgsnZl0yK1HqzWd2sw00zhDctxmW5P77HJ2Zk4tuIsFRYZwOyZjDyWlywyFWgl13KHGN3jwR9twSn4FQRmEycAwZ7kEPB_H8ZB84VJ9eVY3kSYE3iCuud73ci2qT0lu52RuuiKhGSlKxDLNUYh9vDQYHy24ux778wdhyphenhyphen5F2bxfZOgZdjV/s1700-e365/google-2.png) |
| Timeline of STOCKSTAY observations |

In at least one instance observed in early 2025, the Turla actors are said to have employed a phishing email containing a malicious RDP file attachment that, when opened, sets up a connection between the victim's device and actor-controlled infrastructure, through which additional payloads, including STOCKSTAY, can be deployed.

As recently as November 2025, an email phishing wave targeting Ukraine was found to deliver the implant via RAR archives that exploit ...