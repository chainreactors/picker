---
title: China-Aligned Bronze Sandcastle Abuses Sandboxie DLL Sideloading to Deploy Backdoors
url: https://thehackernews.com/2026/10/china-aligned-bronze-sandcastle-abuses.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:43.364322
---

# China-Aligned Bronze Sandcastle Abuses Sandboxie DLL Sideloading to Deploy Backdoors

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [China-Aligned Bronze Sandcastle Abuses Sandboxie DLL Sideloading to Deploy Backdoors](https://thehackernews.com/2026/10/china-aligned-bronze-sandcastle-abuses.html)

**Ravie Lakshmanan**Oct 21, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgq2iUs3zJHHrrskI-icX8x-nBeJxjr_O9uRE2lvcLQkaOhVUHFjTQYLItaZPVskt39VgI2ZYoMDuIhqkAAqEl1bYHLv5ctEfQvPe9UmLyzVEo46YS4xOEz7HcoYKSiNtT_g2bqfKLPFis98BVTTjSR9gafpKRceKKcj0rUf3pb89zBXVt_PequHoA-ta3t/s1700-nu-rw-lo-l85-e365/sandboxie.png)

Cybersecurity researchers have disclosed details of a previously undocumented China-aligned threat cluster known as **[Bronze Sandcastle](https://www.sophos.com/en-us/threat-profiles/bronze-sandcastle)** that has been observed targeting organizations in Asia and Africa since mid-2025.

"The most distinctive technical marker for Bronze Sandcastle is its consistent use of Sandboxie DLL sideloading," Sophos security researcher Gabor Szappanos [said](https://www.sophos.com/en-us/blog/bronze-sandcastle-deploys-modified-meterpreter-shells) in a post published Tuesday.

Between August 2025 and August 2026, attacks mounted by the threat actor have resulted in victims in the Philippines, Taiwan, Afghanistan, Namibia, and likely South Korea. Evidence indicates that Bronze Sandcastle is most active in the UTC+8 time zone.

DLL sideloading is a [popular adversarial technique](https://attack.mitre.org/techniques/T1574/001/) that exploits the way Windows loads DLL files, allowing an attacker to [trick a legitimate program](https://techzone.bitdefender.com/en/tech-explainers/what-is-dll-sideloading.html) into [loading a malicious DLL](https://cloud.google.com/blog/topics/threat-intelligence/abusing-dll-misconfigurations).

When an application is launched, it needs to load various DLLs in order to function correctly. If the application does not provide the full path to a required DLL, the operating system looks for it in a predetermined sequence of directories.

An attacker can take advantage of this behavior by planting a malicious DLL with the same name as a legitimate one in a location that Windows searches before the folder that contains the actual DLL. Thus, when the legitimate application starts, it proceeds to load and run the malicious DLL, giving the attacker a way in to the system.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

"Because the malicious code is executed by a trusted and often digitally signed application, it is less likely to be flagged by antivirus software and other security solutions," Zscaler [noted](https://www.zscaler.com/blogs/product-insights/uncover-dll-sideloading-attack-endpoint-context) in an analysis last week.

"If the legitimate application runs with elevated privileges, the malicious DLL will inherit those same permissions, allowing the attacker to perform more sensitive actions on the system."

What's more, the technique enables persistence if the compromised application is configured to automatically run every time a system is rebooted, thereby allowing the attacker's code to execute on the infected host.

Sophos said it observed legitimate Sandboxie executables placed in multiple victim environments, along with a malicious "sbiedll.dll" file, which, in turn, causes the trusted application ("SandboxieWUAU.exe") to load attacker-controlled code during runtime.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieaLMW_coXIRw7T_yg4m3a5y1hP4F8LaZKYq6JPx-Rzjd0nGLfAqbngiBeH3B4tMvoV6EWuBmklC6z_nGkQwXb-RG9J08qyOrE_2nhYbFZ14lNB5rohyyKYbGxqqebD1nTsmfp-id_z87EMDB6nYJvSfnrwI51f_v15YVqjHnMynTxJ_pVTEk5p8P0imbg/s1700-nu-rw-lo-l85-e365/sophos.png)

Besides Sandboxie, Bronze Sandcastle has been leveraged in seven other DLL sideloading combinations -

* javaw.exe (Java application) - jli.dll
* Krita.exe (Krita digital painting) - Krita.dll
* NvdaHelper.exe (NVDA NonVisual Desktop Access) - NvdaHelperRemote.dll
* Jcef\_helper.exe (Java Chromium Embedded Framework Helper) - Libcef.dll
* Vmmap.exe (Sysinternals process memory analyzer) - version.dll
* LineAppMgr.exe (LINE messaging application) - msvcp140.dll
* bginfo64.exe (Sysinternals utility that displays system information) - snmpapi.dll

"The sideloaded DLLs typically read and execute payloads stored in encrypted config.ini files," Sophos said. "This design minimizes static detection and allows operators to adjust behavior without replacing DLL binaries. Renamed legitimate executables are frequently used to blend into victims' environments, with execution resulting in in-memory shellcode activity rather than additional disk artifacts."

The DLL is designed to load and execute an encrypted payload ("config.ini"), which functions as a backdoor designed to enumerate local network and user accounts, as well as collect system metadata, running processes, keystrokes, and screenshots. Two different versions of the payload have been identified to date: 1.1.5 and 1.1.7.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The payload has also been found to communicate with external sites (e.g., file[.]io, gofile[.]io, ably[.]net, and ably[.]io), likely in an attempt to receive additional tasking from its operators. In addition, version 1.1.5 has been observed using dc.cathaypacifice[.]com and net.dpworldto[.]com for command-and-control (C2).

Version 1.1.7 payloads, on the other hand, have been observed communicating with GitHub repositories ("github[.]com/LatonyCharnleyaW") via the API to download encrypted config files. The GitHub account is no longer accessible.

This is [not the first time](https://www.sophos.com/en-us/blog/family-tree-dll-sideloading-cases-may-be-related) Chinese [hacking groups](https://thehackernews.com/2023/08/china-linked-bronze-starlight-group.html) have [relied](https://www.darktrace.com/blog/chinese-apt-target-royal-thai-police-in-malware-campaign) o...