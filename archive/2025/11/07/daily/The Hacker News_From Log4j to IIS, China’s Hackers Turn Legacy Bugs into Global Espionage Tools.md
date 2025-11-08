---
title: From Log4j to IIS, China’s Hackers Turn Legacy Bugs into Global Espionage Tools
url: https://thehackernews.com/2025/11/from-log4j-to-iis-chinas-hackers-turn.html
source: The Hacker News
date: 2025-11-07
fetch_date: 2025-11-08T03:06:25.001349
---

# From Log4j to IIS, China’s Hackers Turn Legacy Bugs into Global Espionage Tools

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

# [From Log4j to IIS, China's Hackers Turn Legacy Bugs into Global Espionage Tools](https://thehackernews.com/2025/11/from-log4j-to-iis-chinas-hackers-turn.html)

**Nov 07, 2025**Ravie LakshmananCyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghZqCg2FCyFs0KtendNTgM4kewxtAD-fYM5tkn2HDgCT7zqWB-FhYCeJWfm7eeYgQ0ip9aM7jsB1Ix3uGJqIeuJ8R96V4N7fGEOmKsPADGI_yBY5t-PdMm_troy6kaZ6NHtF4fQobzpxaMu9FqSPBvQGeZoVADWx54U9zHT5JvFHQUWdxkY73A2bEPhHg/s790-rw-e365/1000031591.jpg)

A China-linked threat actor has been attributed to a cyber attack targeting an U.S. non-profit organization with an aim to establish long-term persistence, as part of broader activity aimed at U.S. entities that are linked to or involved in policy issues.

The organization, according to a [report](https://www.security.com/threat-intelligence/china-apt-us-policy) from Broadcom's Symantec and Carbon Black teams, is "active in attempting to influence U.S. government policy on international issues." The attackers managed to gain access to the network for several weeks in April 2025.

The first sign of activity occurred on April 5, 2025, when mass scanning efforts were detected against a server by leveraging various well-known exploits, including [CVE-2022-26134](https://nvd.nist.gov/vuln/detail/cve-2022-26134) (Atlassian), [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/cve-2021-44228) (Apache Log4j), [CVE-2017-9805](https://nvd.nist.gov/vuln/detail/cve-2017-9805) (Apache Struts), and [CVE-2017-17562](https://nvd.nist.gov/vuln/detail/cve-2017-17562) (GoAhead Web Server).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

No further actions were recorded until April 16, when the attacks executed several curl commands to test internet connectivity, after which the Windows command-line tool netstat was executed to collect network configuration information. This was followed by setting up persistence on the host by means of a scheduled task.

The task was designed to execute a legitimate Microsoft binary "msbuild.exe" to run an unknown payload, as well as create another scheduled task that's configured to run every 60 minutes as a high-privileged SYSTEM user.

This new task, Symantec and Carbon Black said, was capable of loading and injecting unknown code into "csc.exe" that ultimately established communications with a command-and-control (C2) server ("38.180.83[.]166"). Subsequently, the attackers were observed executing a custom loader to unpack and run an unspecified payload, likely a remote access trojan (RAT) in memory.

Also observed was the execution of the legitimate Vipre AV component ("vetysafe.exe") to sideload a DLL loader ("sbamres.dll"). This component is also said to have been used for DLL side-loading in connection with [Deed RAT](https://thehackernews.com/2025/10/hackers-used-snappybee-malware-and.html) (aka [Snappybee](https://thehackernews.com/2024/11/chinese-hackers-use-ghostspider-malware.html)) in prior activity attributed to Salt Typhoon (aka Earth Estries), and in attacks attributed to [Earth Longzhi](https://thehackernews.com/2024/06/chinese-state-backed-cyber-espionage.html), a sub-cluster of [APT41](https://thehackernews.com/2025/09/china-linked-apt41-hackers-target-us.html).

"A copy of this malicious DLL was previously used in attacks linked to the China-based threat actors known as [Space Pirates](https://thehackernews.com/2023/08/researchers-expose-space-pirate-cyber.html)," Broadcom said. "A variant of this component, with a different filename, was also used by that Chinese APT group Kelp (aka Salt Typhoon) in a separate incident."

Some of the other tools observed in the targeted network included Dcsync and Imjpuexc. It's not clear how successful the attackers were in their efforts. No additional activity was registered after April 16, 2025.

"It is clear from the activity on this victim that the attackers were aiming to establish a persistent and stealthy presence on the network, and they were also very interested in targeting domain controllers, which could potentially allow them to spread to many machines on the network," Symantec and Carbon Black said.

"The sharing of tools among groups has been a long-standing trend among Chinese threat actors, making it difficult to say which specific group is behind a set of activities."

The disclosure comes as a security researcher who goes by the online moniker BartBlaze [disclosed](https://bartblaze.blogspot.com/2025/10/earth-estries-alive-and-kicking.html) Salt Typhoon's exploitation of a security flaw in WinRAR (CVE-2025-8088) to initiate an attack chain that [sideloads a DLL](https://www.virustotal.com/gui/file/5e062fee5b8ff41b7dd0824f0b93467359ad849ecf47312e62c9501b4096ccda/community) responsible for running shellcode on the compromised host. The final payload is designed to establish contact with a remote server ("mimosa.gleeze[.]com").

### Activity from Other Chinese Hacking Groups

According to a report from ESET, China-aligned groups have [continued](https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html) to remain active, striking entities across Asia, Europe, Latin America, and the U.S. to serve Beijing's geopolitical priorities. Some of the notable campaigns include -

* The targeting of the energy sector in Central Asia by a threat actor codenamed Speccom in July 2025 via phishing emails to deliver a variant of [BLOODALCHEMY](https://thehackernews.com/2024/05/japanese-experts-warn-of-bloodalchemy.html) and custom backdoors such as kidsRAT and RustVoralix.
* The targeting of European organizations by a threat actor codenamed [DigitalRecyclers](https://thehackernews.com/2025/05/chinese-hackers-deploy-marssnake.html) in July 2025, using an unusual persistence technique that involved the use of the [Magnifier accessibility tool](https://oddvar.moe/2018/07/23/another-way-to-get-to-a-system-shell/) to gain SYSTEM privileges.
* The targeting of governmental entities in Latin Americ...