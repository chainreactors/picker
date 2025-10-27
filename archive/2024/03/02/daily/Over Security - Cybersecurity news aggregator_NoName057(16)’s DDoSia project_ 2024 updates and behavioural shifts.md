---
title: NoName057(16)’s DDoSia project: 2024 updates and behavioural shifts
url: https://blog.sekoia.io/noname05716-ddosia-project-2024-updates-and-behavioural-shifts/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:12:31.394931
---

# NoName057(16)’s DDoSia project: 2024 updates and behavioural shifts

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# NoName057(16)’s DDoSia project: 2024 updates and behavioural shifts

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR, Amaury G. and Maxime A.](#molongui-disabled-link)
March 1 2024

0

11 minutes reading

## Table of contents

* [Context](#h-context)
* [System-level analysis of newly shared files by the adminstrators of DDoSia project](#h-system-level-analysis-of-newly-shared-files-by-the-adminstrators-of-ddosia-project)
* [Service instability: impact of recurring C2 changes](#h-service-instability-impact-of-recurring-c2-changes)
* [Victimology analysis: most impacted countries and sectors in early 2024 by NoName057(16)](#h-victimology-analysis-most-impacted-countries-and-sectors-in-early-2024-by-noname057-16)
  + [Impacted countries by DDoSia project](#h-impacted-countries-by-ddosia-project)
  + [Impacted economic verticals](#h-impacted-economic-verticals)
* [Conclusion](#h-conclusion)
* [DDoSia’s IoCs](#h-ddosia-s-iocs)

## Context

Since the onset of the War in Ukraine, various groups identified as “nationalist hacktivists” have emerged, particularly on the Russian side, to contribute to the confrontation between Kyiv and Moscow. Among these entities, the pro-Russian group **NoName057(16) has garnered attention through the initiation of Project DDoSia,** a collective endeavour aimed at conducting large-scale distributed denial-of-service (DDoS) attacks, targeting entities (private corporations, ministries and public institutions) belonging to countries supporting Ukraine, predominantly NATO member states.

As of 2024, Project DDoSia and the group operating it are now familiar names, **Sekoia.io continues to proactively monitor the Command and Control (C2)** infrastructure of the DDoS tool. Specifically, we implemented an automated system for real-time target collection and regular monitoring of communication channels wherein NoName057(16) claims responsibility for its attacks, as mentioned in our blog post from June 2023: [Following NoName057(16) DDoSia Project’s Targets](https://blog.sekoia.io/following-noname05716-ddosia-projects-targets). Even more recently in 2024, we discussed the monitoring of this group’s infrastructure in our annual report: [Adversary infrastructures tracked in 2023](https://blog.sekoia.io/adversary-c2-infrastructures-tracked-in-2023/).

This current report will detail **an overview of the changes made**, both from the perspective of the software shared by the group to generate DDoS attacks and the specifics of the evolution of the C2 servers, culminating in the targeting of countries and sectors for 2024.

## System-level analysis of newly shared files by the adminstrators of DDoSia project

On 11 November 2023, the administrators of the Telegram channel for Project DDoSia shared a new version. Without any prior announcement, the newly shared version now includes compatibility with more types of processor architectures. The update added compatibility for 32-bit, as well as support for the FreeBSD operating system. Of note, they already supported AMD64, ARM, and ARM64 in previous versions. As of 21 February 2024, the shared ZIP archive contains the following files:

|  |  |
| --- | --- |
| **Filename** | **Filetype** |
| d\_freebsd\_arm | ELF 32-bit LSB executable, ARM |
| d\_freebsd\_x32 | ELF 32-bit LSB executable, Intel 80386 |
| d\_freebsd\_x64 | ELF 64-bit LSB executable, x86-64 |
| d\_lin\_arm | ELF 32-bit LSB executable, ARM |
| d\_lin\_x32 | ELF 32-bit LSB executable, Intel 80386 |
| d\_lin\_x64 | ELF 64-bit LSB executable, x86-64 |
| d\_mac\_arm64 | Mach-O 64-bit arm64 executable |
| d\_mac\_x64 | Mach-O 64-bit x86\_64 executable |
| d\_win\_arm64.exe | PE32+ executable (console) Aarch64 |
| d\_win\_x32.exe | PE32 executable (console) Intel 80386 |
| d\_win\_x64.exe | PE32+ executable (console) x86-64 |

Table 1 – Contents of the ZIP archive shared by DDoSia administrators

Furthermore, it is observed that the main ZIP archive contains two folders: one named `d_eu` and the other `d_ru`, which are adapted, according to the administrators, for users wishing to execute the file based on their geographical location. When launching the executable, a warning message is displayed to the user, advising them to use a VPN if they are located in Russia, as shown in the following extract:

C:\[…]\d(27)\d\_eu>d\_win\_x64.exe
Go-Stresser версия 2.0 | PID 10912
© NoName057(16)
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

login success…
try get target list…
loaded 285 targets…
–If you work from Russia, then switch the VPN to a foreign one. You will have 1 minutes for this.
–Если вы работаете из России, то переключите vpn на зарубежный. У вас на это будет 1 минуты

Regardless of which folder the executable is launched from, this warning message will appear. The main distinction is that in the “d\_ru“ folder, all files are appended with the `_ru` suffix. On 4 December 2023, following the rollout of these new files, the administrators also shared a page on `telegra.ph` (`hxxps://telegra[.]ph/Instrukciya-dlya-uchastnikov-proekta-DDoSia-Project-12-04`), providing detailed instructions for users, along with a FAQ section. In item number 2, responding to the query “*Does the provider see my actions or law enforcement agencies see my IP?*”, the answer given is as follows:*`"If the computer is located on the territory of the Russian Federation, then even without using a VPN, it is extremely unlikely that there will be any problems with the law, since the software is designed for stress testing. At least that's what we think. If the computer is located outside the Russian Federation, it is strongly recommended to use a VPN to change the IP address. You can check the change in IP address, for example, on myip.com.
It is recommended to m...