---
title: 14 Trojanized npm Packages Drop RedC2 4.0 Linux Backdoor With AI-Assisted C2
url: https://thehackernews.com/2026/08/14-trojanized-npm-packages-drop-redc2.html
source: The Hacker News
date: 2026-08-21
fetch_date: 2026-08-22T02:52:36.134056
---

# 14 Trojanized npm Packages Drop RedC2 4.0 Linux Backdoor With AI-Assisted C2

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [14 Trojanized npm Packages Drop RedC2 4.0 Linux Backdoor With AI-Assisted C2](https://thehackernews.com/2026/08/14-trojanized-npm-packages-drop-redc2.html)

**Ravie Lakshmanan**Aug 21, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvZpEOpS6_M3zQlIDwvD1wMhESnRAMTCz1nW2JFP__pGSVWOw28REaDTZ5lI7sdwvcRKSSUHI4sm1CUuWs6_gvOXE1c5BbvKnR75iyBl9Er1SckweDAxBEotnOlSikBeOE5WEBIIGlS74w4b85pvznpr3c4mj88LzLt-3pGr1HHXHQDg5v7T9FxdBSWSlK/s1700-e365/linux-npm.jpg)

Cybersecurity researchers have discovered a set of trojanized npm packages that masquerade as working calendar and streak utilities but are engineered to stealthily deliver an artificial intelligence (AI)-powered Linux implant dubbed RedC2 4.0.

"When the module loads, it locates the bundled binary, marks it executable, and launches it as a detached background process," TrendAI, Trend Micro's enterprise cybersecurity business, [said](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant) in a report published Thursday. "No install hook function call is needed; a single import anywhere in the dependency graph, even a transitive one, is enough to execute the payload."

The list of identified packages is below -

* streak-metrics-math@1.0.0,1.0.1
* kit-map-vim@1.0.0
* streak-map-cache@1.0.0
* streak-map-kit@1.0.0
* map-streak-kit@1.0.0
* streak-cache-map@1.0.0
* streak-calc-metrics@1.0.0
* streak-calc-math@1.0.0
* streak-math-abz@1.0.0
* streak-metricsaz@1.0.0
* streak-math-metrics@1.0.0
* streak-metricazbd@1.0.0
* streak-metricsazb@1.0.0
* streak-kit-map@1.0.0

What's notable about these packages is that they are functional and offer the promised functionality. But beneath that garb of date utilities is code designed to drop a Linux backdoor by framing it as a native math accelerator. The name of the file varies across the packages: math-core.bin, math-calc.bin, calc-math.dat, calc-cache.bin, calc.bin, calc-mapping.bin.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

It's located either directly within the "dist/" or under "dist/internal/,", but what it contains is the same: the RedShell Linux beacon for RedC2 4.0 that communicates with a remote Windows or Linux server to facilitate post-exploitation activities on the compromised host.

"Delivery is handled by the package entry file, dist/index.mjs, which acts as a trojan loader," security researcher Aliakbar Zahravi said. "It re-exports the date helpers and launches the bundled implant as soon as the module loads, with no install hook and no exported function required."

RedC2 4.0, marketed on cybercrime forums as a cross-platform toolkit for Windows, macOS, and Linux, offers surveillance, credential theft, payload loading, and mass-operation capabilities. The version was advertised by a threat actor named "MarlboroMan" on Hack Forums in early June 2026, describing it as a command-and-control (C2 or C&C) framework "built for evasion."

Version 3.0 of RedC2 was sold earlier this January, while version 2.0 was released in August 2025, indicating the framework has been under active development for at least a year. The RedShell Linux beacon was introduced in version 4.0.

The C2 framework is also feature-rich, supporting terminal access, file transfer, staged payload delivery, data collection, multi-beacon operation, network visualization, host-to-host tunneling, and in-memory execution of Beacon Object Files (BOFs), .NET assemblies, and shellcode.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlHCLJlXhU8AcLg7JSdDErd_fLrMesEfNfedrzh1Lz4G3BBdG010Z-_HCGWEVVwUPgTsOBPvYEQLzdJC18Kwe10a-KKAngzQjsnnW6RiBJ_gyvus9IoXpAcERDcwfmPIjP3Hz9WXY8o8P5Ee58uocwewQ6_ZO91UJpLcBjzXhyaDTKc7BhbabCKrOitnJT/s1700-e365/endpoint.png) |
| RedShell Linux execution flow |

The Linux variant of the beacon, once deployed, provides an interactive shell through "/bin/sh" and exposes Linux-specific commands to enable system discovery, file operations, data collection (e.g., SSH keys and browser credentials), execution, persistence, in-memory ELF execution, SOCKS5 proxying, and network pivoting.

It also establishes communication with a C2 server and registers the infected system by gathering basic system information and transmitting it in the form of a "check-in message," after which it enters a command-processing loop to process incoming instructions from the operator, execute them via "/bin/sh," and send the results back.

The Windows and macOS counterparts cover a similar ground, allowing file operations, host and network reconnaissance, user enumeration, and data harvesting. The Windows beacon also incorporates User Account Control (UAC) bypass, antivirus and endpoint detection, antivirus tampering, in-memory execution, and lateral movement that the macOS version lacks.

On a clearnet website branded Red Offsec, the threat actor claims, "Red C2 is a multi-language, multi-OS command and control framework designed for Windows, Linux, and macOS. The entire framework was built with evasion as a core principle, utilizing the latest developments and techniques in the offensive security field." It's available for purchase for $99.99.

Red Offsec's Terms of Service expressly prohibit its customers from using the tool for "unauthorized computer access," "hacking without explicit permission," and "abuse, exploitation, or damage of systems you do not own or are not authorized to test."

"Red Offsec provides tools intended for red team professionals and users who understand external offensive security tooling within legal and ethical boundaries," the terms read.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

RedC2 extends its control layer with a command-line extension referred to as RedC2 EXT as well as a large language model (LLM)-driven component called Red Agent, the latter of ...