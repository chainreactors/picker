---
title: New HttpTroy Backdoor Poses as VPN Invoice in Targeted Cyberattack on South Korea
url: https://thehackernews.com/2025/11/new-httptroy-backdoor-poses-as-vpn.html
source: The Hacker News
date: 2025-11-03
fetch_date: 2025-11-04T03:11:35.370701
---

# New HttpTroy Backdoor Poses as VPN Invoice in Targeted Cyberattack on South Korea

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [New HttpTroy Backdoor Poses as VPN Invoice in Targeted Cyberattack on South Korea](https://thehackernews.com/2025/11/new-httptroy-backdoor-poses-as-vpn.html)

**Nov 03, 2025**Ravie LakshmananCybersecurity / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuEYAYmymffrJslyjZDJpRu1vE-IbqbiurB5-rldIfgwDRWEeV8EpVqbWpZrVsKjw-LBAbl_b6Ao-TviGJigU85u3F8JI5kARLR9Vt4TL2QpJZolmnhl_v5KEKyJBzWqvGC9hVEla_UrX3YZblzOV3Ty1J4hCn3ULFJSxO3pszRKpflfwECdsSGs7Grzld/s790-rw-e365/vpn-invoice.jpg)

The North Korea-linked threat actor known as [Kimsuky](https://thehackernews.com/2025/07/north-korean-hackers-target-web3-with.html#kimsuky-s-use-of-clickfix-continues) has distributed a previously undocumented backdoor codenamed HttpTroy as part of a likely spear-phishing attack targeting a single victim in South Korea.

Gen Digital, which [disclosed details](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis) of the activity, did not reveal any details on when the incident occurred, but noted that the phishing email contained a ZIP file ("250908\_A\_HK이노션\_SecuwaySSL VPN Manager U100S 100user\_견적서.zip"), which masqueraded as a VPN invoice to distribute malware capable of file transfer, capturing screenshots, and executing arbitrary commands.

"The chain has three steps: a small dropper, a loader called MemLoad, and the final backdoor, named 'HttpTroy,'" security researcher Alexandru-Cristian Bardaș said.

Present within the ZIP archive is a SCR file of the same name, opening which triggered the execution chain, starting with a Golang binary containing three embedded files, including a decoy PDF document that's displayed to the victim to avoid raising any suspicion.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Also launched simultaneously in the background is MemLoad, which is responsible for setting up persistence on the host by means of a scheduled task named "AhnlabUpdate," an attempt to impersonate AhnLab, a South Korean cybersecurity company, and decrypt and execute the DLL backdoor ("HttpTroy").

The implant allows the attackers to gain complete control over the compromised system, enabling file upload/download, screenshot capture, command execution with elevated privileges, in-memory loading of executables, reverse shell, process termination, and trace removal. It communicates with the command-and-control (C2) server ("load.auraria[.]org") over HTTP POST requests.

"HttpTroy employs multiple layers of obfuscation to hinder analysis and detection," Bardaș explained. "API calls are concealed using custom hashing techniques, while strings are obfuscated through a combination of XOR operations and SIMD instructions. Notably, the backdoor avoids reusing API hashes and strings. Instead, it dynamically reconstructs them during runtime using varied combinations of arithmetic and logical operations, further complicating static analysis."

The findings come as the cybersecurity vendor also detailed a [Lazarus Group](https://thehackernews.com/2025/10/north-korean-hackers-lure-defense.html) attack that led to the deployment of [Comebacker](https://thehackernews.com/2024/05/microsoft-uncovers-moonstone-sleet-new.html) and an upgraded version of its [BLINDINGCAN](https://thehackernews.com/2025/04/north-korean-hackers-deploy-beavertail.html) (aka AIRDRY or ZetaNile) remote access trojan. The attack targeted two victims in Canada and was detected in the "middle of the attack chain," it added.

While the exact initial access vector used in the attack is not known, it's assessed to be a phishing email based on the absence of any known security vulnerabilities that could have been exploited to gain a foothold.

Two different variants of Comebacker – one as a DLL and another as an EXE – have been put to use, with the former launched via a Windows service and the latter through "cmd.exe." Irrespective of the method used to execute them, the end goal of the malware is the same: to decrypt an embedded payload (i.e., BLINDINGCAN) and deploy it as a service.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

BLINDINGCAN is designed to establish a connection with a remote C2 server ("tronracing[.]com") and await further instructions that allow it to -

* Upload/download files
* Delete files
* Alter a file's attributes to mimic another file
* Recursively enumerate all files and sub-directories for a specified path
* Gather data about files across the entire file system
* Collect system metadata
* List running processes
* Run a command-line using [CreateProcessW](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw)
* Execute binaries directly in memory
* Execute commands using "cmd.exe"
* Terminate a specific process by passing a process ID as input
* Take screenshots
* Take pictures from the available video capture devices
* Update configuration
* Change current working directory
* Delete itself and remove all traces of malicious activity

"Kimsuky and Lazarus continue to sharpen their tools, showing that DPRK-linked actors aren't just maintaining their arsenals, they're reinventing them," Gen Digital said. "These campaigns demonstrate a well-structured and multi-stage infection chain, leveraging obfuscated payloads and stealthy persistence mechanisms."

"From the initial stages to the final backdoors, each component is designed to evade detection, maintain access and provide extensive control over the compromised system. The use of custom encryption, dynamic API resolution and COM-based task registration/services exploitation highlights the groups' continued evolution and technical sophistication."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackerne...