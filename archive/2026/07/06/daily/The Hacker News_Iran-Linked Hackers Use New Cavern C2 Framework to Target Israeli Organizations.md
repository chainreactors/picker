---
title: Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations
url: https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:04.987052
---

# Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations

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

# [Iran-Linked Hackers Use New Cavern C2 Framework to Target Israeli Organizations](https://thehackernews.com/2026/07/iran-linked-hackers-use-new-cavern-c2.html)

**Ravie Lakshmanan**Jul 06, 2026Threat intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj80nucNUGoxxOtE3SUY1SkDSu77qENrl96c2MUoLWdwAo3ZVoA4FS2QfOdM9c5bsZUJdX1ZxIsXgu7pvVfUzXz3GMZJHmblFTjv5C08dbxvLqXol72iHaD-zH950EZdXUCS-b7F2T-bn8SgqQb9nXA-uOPIaX5V0eaNNmKlQJfWHAKaPAhqsgNL0wTgJH6/s1700-e365/cavern.jpg)

An Iranian hacking group affiliated with Iran's Ministry of Intelligence and Security (MOIS) has been wielding a previously undocumented modular command-and-control (C2) framework dubbed Cavern (aka Cav3rn) targeting Israeli organizations.

The activity, which has primarily singled out IT providers and government sectors, has been attributed to a threat cluster tracked by Check Point Research under the moniker **Cavern Manticore**, which it said shares some level of tactical overlaps with [MuddyWater](https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html) and [Lyceum](https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html), the latter of which is assessed to be a subgroup within [OilRig](https://thehackernews.com/2026/03/dust-specter-targets-iraqi-officials.html).

"The framework reflects a mature and adaptable toolset built around a shared .NET foundation, while using multiple compilation formats across different components, including .NET Framework, .NET Mixed-Mode C++/CLI, and .NET [Native AOT](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/)," the cybersecurity company [said](https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/).

"The compilation format itself becomes the anti-analysis layer that forces reverse engineers into multiple toolsets and metadata-reconstruction workflows."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The components of the C2 framework are used as Cavern Agent and Cavern modules, demonstrating a clear division of responsibilities between core communication capabilities and mission-specific post-exploitation functionality. This architecture has inherent advantages as it allows the operators to tailor deployments based on the victim profile, reduce forensic visibility, and ensure persistent access through bespoke modules for reconnaissance, data theft, tunneling, and lateral movement.

The attack chain documented by Check Point Research commences with SysAid's software update feature, which is leveraged by the adversary to initiate a DLL side-loading chain that leads to the execution of a trojanized DLL ("uxtheme.dll") containing the Cavern Agent. The agent, for its part, loads a standalone communication DLL module ("n-HTCommp.dll") to contact the C2 server ("hospitalinstallation[.]com") and fetch additional post-exploitation modules on the fly over HTTPS or WebSocket.

As many as five DLL modules have been uncovered -

* **mhm.dll**, for file operations, enumeration, recursive file search, archive handling, and bidirectional file transfer
* **db.dll**, for SQL database enumeration, query, export, and manipulation
* **ode.dll**, for Active Directory reconnaissance, user/group enumeration, and LDAP brute-force attempts
* **n-ten.dll**, for network reconnaissance, port scanning, share enumeration, and SMB brute-force attempts
* **n-sws.dll**, for SOCKS5 proxy and WebSocket tunneling

A defining trait of the framework is its use of three different .NET compilation targets spanning its components: while mhm.dll, db.dll, and ode.dll are pure .NET Framework modules, n-HTCommp.dll, n-ten.dll, and n-sws.dll make use of Native AOT (Ahead-of-Time) compilation. The main agent, uxtheme.dll, combines managed .NET code with native C++ in a single portable executable.

Embedded within the agent is a unified module dispatcher that treats components whose names start with n- as native DLLs and loaded via the [LoadLibraryA](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) Windows API, while the rest is interpreted as managed .NET assemblies and loaded through a mechanism known as [AppDomain isolation](https://learn.microsoft.com/en-us/dotnet/framework/app-domains/application-domains).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWYX7NDIPCaQeZ2I0P0WjqWDXGyGRUBLBBTbxoFTQg91_jJKmX7W0zN5trpTGnzajc-M89ZHkTHRjt9TFrC914jCL5N3w12Mg3vb9oFFE7G1fZcR6XYhRVma-R4rgcZUJ3kJIevhB2qlujJ8gSbMZtCU-tntnnvZlLgpqT9_O_vG19ai_rP4Ik8S5GWQnH/s1700-e365/cp-1.png)

"The framework's anti-analysis posture relies on uncommon .NET compilation formats (Mixed-Mode C++/CLI and Native AOT) that force reverse engineers into multiple toolsets and metadata-reconstruction workflows, together with per-module AppDomain isolation as an anti-forensics measure," Check Point explained.

Attacks orchestrated by Cavern Manticore have involved the threat actor moving from an initial compromised IT provider to a second-hop provider before ultimately reaching the intended target organization, indicating their ability to weaponize [trusted relationships](https://securelist.com/trusted-relationship-attack/112731/) in the software supply chain to their advantage.

"This activity highlights the operational value of trusted service-provider relationships, particularly where Remote Monitoring and Management (RMM) solutions are deployed," the company noted.

"By abusing these tools, the actor can move laterally between victims and deliver malicious software disguised as legitimate updates. The actor also appears to leverage browser-based remote desktop technologies to access targets of interest and, in some cases, abuse built-in features such as remote printing to exfiltrate data when clipboard-based copy-paste or file-transfer capabilities are restricted."

[![Cybersecurity](htt...