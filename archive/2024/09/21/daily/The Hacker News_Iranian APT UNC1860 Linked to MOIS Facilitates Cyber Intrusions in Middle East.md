---
title: Iranian APT UNC1860 Linked to MOIS Facilitates Cyber Intrusions in Middle East
url: https://thehackernews.com/2024/09/iranian-apt-unc1860-linked-to-mois.html
source: The Hacker News
date: 2024-09-21
fetch_date: 2025-10-06T18:32:12.061647
---

# Iranian APT UNC1860 Linked to MOIS Facilitates Cyber Intrusions in Middle East

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Iranian APT UNC1860 Linked to MOIS Facilitates Cyber Intrusions in Middle East](https://thehackernews.com/2024/09/iranian-apt-unc1860-linked-to-mois.html)

**Sep 20, 2024**Ravie LakshmananMalware / Cyber Threat

[![Iranian APT UNC1860](data:image/png;base64... "Iranian APT UNC1860")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwq3ADvdE9FnCsinHydEesuesu7cOi5yllg4Pmzi00lOON5UP-49K7M5SJ8ZFobT6g5FkCgu-itJYe2v7Usy6uk1cmrMiqGPZdekj7_AwPfs8Bpn1kK-9_Bx3E-GAzne98Dcb29q3suuEg3SAPGKNONWPbpfiZb-a0-3n1nn8URX4WK2y6Bp7dy9yUbaz9/s790-rw-e365/iran-hackers.png)

An Iranian advanced persistent threat (APT) threat actor likely affiliated with the Ministry of Intelligence and Security (MOIS) is now acting as an initial access facilitator that provides remote access to target networks.

Google-owned Mandiant is tracking the activity cluster under the moniker **UNC1860**, which it said shares similarities with intrusion sets tracked by Microsoft, Cisco Talos, and Check Point as [Storm-0861](https://thehackernews.com/2022/09/us-imposes-new-sanctions-on-iran-over.html) (formerly DEV-0861), [ShroudedSnooper](https://thehackernews.com/2023/09/shroudedsnoopers-httpsnoop-backdoor.html), and [Scarred Manticore](https://thehackernews.com/2023/11/iranian-cyber-espionage-group-targets.html), respectively.

"A key feature of UNC1860 is its collection of specialized tooling and passive backdoors that [...] supports several objectives, including its role as a probable initial access provider and its ability to gain persistent access to high-priority networks, such as those in the government and telecommunications space throughout the Middle East," the company [said](https://cloud.google.com/blog/topics/threat-intelligence/unc1860-iran-middle-eastern-networks/).

The group first came to light in July 2022 in [connection](https://thehackernews.com/2022/08/iranian-hackers-likely-behind.html) with destructive cyber attacks targeting Albania with a ransomware strain called ROADSWEEP, the CHIMNEYSWEEP backdoor, and a ZEROCLEAR wiper variant (aka Cl Wiper), with [subsequent intrusions](https://thehackernews.com/2024/05/iranian-mois-linked-hackers-behind.html) in Albania and Israel leveraging new wipers dubbed No-Justice and BiBi (aka BABYWIPER).

Mandiant described UNC1860 as a "formidable threat actor" that maintains an arsenal of passive backdoors that are designed to obtain footholds into victim networks and set up long-term access without attracting attention.

Among these tools includes two GUI-operated malware controllers tracked as TEMPLEPLAY and VIROGREEN, which are said to provide other MOIS-associated threat actors with remote access to victim environments using remote desktop protocol (RDP).

Specifically, these controllers are designed to provide third-party operators an interface that offers instructions on the ways custom payloads could be deployed and post-exploitation activities such as internal scanning could be carried out within the target network.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Mandiant said it identified overlaps between UNC1860 and APT34 (aka Hazel Sandstorm, Helix Kitten, and OilRig) in that organizations compromised by the latter in 2019 and 2020 were previously infiltrated by UNC1860, and vice versa. Furthermore, both the clusters have been observed pivoting to Iraq-based targets, as recently [highlighted](https://thehackernews.com/2024/09/iranian-cyber-group-oilrig-targets.html) by Check Point.

The attack chains involve leveraging initial access gained by opportunistic exploitation of vulnerable internet-facing servers to drop web shells and droppers like STAYSHANTE and SASHEYAWAY, with the latter leading to the execution of implants, such as TEMPLEDOOR, FACEFACE, and SPARKLOAD, that are embedded within it.

"VIROGREEN is a custom framework used to exploit vulnerable SharePoint servers with [CVE-2019-0604](https://nvd.nist.gov/vuln/detail/cve-2019-0604)," the researchers said, adding that it controls STAYSHANTE, along with a backdoor referred to as BASEWALK.

"The framework provides post-exploitation capabilities including [...] controlling post-exploitation payloads, backdoors (including the STAYSHANTE web shell and the BASEWALK backdoor) and tasking; controlling a compatible agent regardless of how the agent has been implanted; and executing commands and uploading/downloading files.

TEMPLEPLAY (internally named Client Http), for its part, serves as the .NET-based controller for TEMPLEDOOR. It supports backdoor instructions for executing commands via cmd.exe, upload/download files from and to the infected host, and proxy connection to a target server.

[![Iranian APT UNC1860](data:image/png;base64... "Iranian APT UNC1860")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjv8GKuOUf5NGZxR3Hw_x5saUtBxahGOeGb9edCjbfmrijcQ5LDYIMyJwjs1b4avqkSg05TdwNBfglu0PpFdx7GGygZ-MAAWhUp7vP-AkdUby9EfMe1YlcrZrnP8BPH366UX6TFq-1kbv_Bn-EWXCRdlDsTAOFJ3fcmo5rINc29opLi5R3yXakyERVFuPNj/s790-rw-e365/tool.png)

It's believed that the adversary has in its possession a diverse collection of passive tools and main-stage backdoors that align with its initial access, lateral movement, and information gathering goals.

Some of the other tools of note documented by Mandiant are listed below -

* OATBOAT, a loader that loads and executes shellcode payloads
* TOFUDRV, a malicious Windows driver that overlaps with [WINTAPIX](https://thehackernews.com/2023/05/new-wintapixsys-malware-engages-in.html)
* TOFULOAD, a passive implant that employs undocumented Input/Output Control (IOCTL) commands for communication
* TEMPLEDROP, a repurposed version of an Iranian antivirus software Windows file system filter driver named Sheed AV that's used to protect the files it deploys from modification
* TEMPLELOCK, a .NET defense evasion utility that's capable of killing the Windows Event Log service
* TUNNELBOI, a network controller capable of establishing a connection with a remote host and managing ...