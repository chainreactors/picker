---
title: Mustang Panda Targets Myanmar With StarProxy, EDR Bypass, and TONESHELL Updates
url: https://thehackernews.com/2025/04/mustang-panda-targets-myanmar-with.html
source: The Hacker News
date: 2025-04-18
fetch_date: 2025-10-06T22:07:02.240056
---

# Mustang Panda Targets Myanmar With StarProxy, EDR Bypass, and TONESHELL Updates

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

# [Mustang Panda Targets Myanmar With StarProxy, EDR Bypass, and TONESHELL Updates](https://thehackernews.com/2025/04/mustang-panda-targets-myanmar-with.html)

**Apr 17, 2025**Ravie LakshmananMalware / Network Security

[![Mustang Panda Targets Myanmar](data:image/png;base64... "Mustang Panda Targets Myanmar")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPL_-wvfFUMUJJRbg4AxR6hmQzbycv8lBE34sg-DEQJk_43rgFTBsC_W7XHaf1UW3u4ryOcFMIfBiqG_oAZ5Ue2dL9vPE0CdMmnyvlbOrZ_Z-WaCmfj1rzzQ6tbcofwihODIOwwi9Pu72WW2BmMXDQ4C0_6Pe4wuIlrj-OBbuinXHmwVcPOts1dcePzEZB/s790-rw-e365/malware-attack.jpg)

The China-linked threat actor known as [Mustang Panda](https://thehackernews.com/2025/02/chinese-hackers-exploit-mavinjectexe-to.html) has been attributed to a cyber attack targeting an unspecified organization in Myanmar with previously unreported tooling, highlighting continued effort by the threat actors to increase the sophistication and effectiveness of their malware.

This includes updated versions of a known backdoor called **TONESHELL**, as well as a new lateral movement tool dubbed StarProxy, two keyloggers codenamed PAKLOG, CorKLOG, and an Endpoint Detection and Response (EDR) evasion driver referred to as **SplatCloak**.

"TONESHELL, a backdoor used by Mustang Panda, has been updated with changes to its FakeTLS command-and-control (C2) communication protocol as well as to the methods for creating and storing client identifiers," Zscaler ThreatLabz researcher Sudeep Singh said in a [two-part](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1) [analysis](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2).

Mustang Panda, also known as BASIN, Bronze President, Camaro Dragon, Earth Preta, HoneyMyte, and RedDelta, is a China-aligned state-sponsored threat actor active since at least 2012.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Known for its attacks on governments, military entities, minority groups, and non-governmental organizations (NGOs) primarily in countries located in East Asia, and to a lesser extent in Europe, the group has a history of [leveraging DLL side-loading](https://thehackernews.com/2025/01/reddelta-deploys-plugx-malware-to.html) techniques to deliver the PlugX malware.

However, since late 2022, campaigns orchestrated by Mustang Panda have begun to frequently deliver a bespoke malware family called [TONESHELL](https://thehackernews.com/2024/10/china-linked-ceranakeeper-targeting.html), which is designed to download next-stage payloads.

Zscaler said it discovered three new variants of the malware that come with varying levels of sophistication -

* **Variant 1**, which acts as a simple reverse shell
* **Variant 2**, which includes functionality to download DLLs from the C2 and execute them by injecting the DLL into legitimate processes (e.g., svchost.exe)
* **Variant 3**, which includes functionality to download files and create a sub-process to execute commands received from a remote server via a custom TCP-based protocol

A new piece of software associated with Mustang Panda is StarProxy, which is launched via DLL side-loading and is designed to take advantage of FakeTLS protocol to proxy traffic and facilitate attacker communications.

"Once active, StarProxy allows attackers to proxy traffic between infected devices and their C2 servers. StarProxy achieves this by utilizing TCP sockets to communicate with the C2 server via the FakeTLS protocol, encrypting all exchanged data with a custom XOR-based encryption algorithm," Singh said.

"Additionally, the tool uses command-line arguments to specify the IP address and port for communication, enabling attackers to relay data through compromised machines."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu2u69Biod6OQcIvJ08t1wte06CuQb6JJfVvGXPqBr6G26CPWCBNF-Xl6R3ynNCqBgnM3dnWlKnWcvHAS502xL2U-hWAXWNzakI7UIwpvp0-y7mdDOt673dMgcGBWzyVT0XJrLg9AXVKo6hu7H2pkqAjIral6mY9sWzwBTSJtHrvCnSUtJ4uhnDjXBmOJO/s790-rw-e365/xx.png) |
| StarProxy activity |

It's believed that StarProxy is deployed as a post-compromise tool to access internal workstations within a network that are not directly exposed to the internet.

Also identified are two new keyloggers, PAKLOG and CorKLOG, that are used to monitor keystrokes and clipboard data. The primary difference between the two is that the latter stores the captured data in an encrypted file using a 48-character RC4 key and implements persistence mechanisms by creating services or scheduled tasks.

Both the keyloggers lack data exfiltration capabilities of their own, meaning they solely exist to collect the keystroke data and write them to a specific location and that the threat actor uses other methods to transmit the files to their infrastructure.

Capping off the new additions to the Mustang Panda's malware arsenal is SplatCloak, a Windows kernel driver deployed by SplatDropper that's equipped to disable EDR-related routines implemented by Windows Defender and Kaspersky, thereby allowing it to fly under the radar.

"Mustang Panda demonstrates a calculated approach to achieving their objectives," Singh said. "Continuous updates, new tooling, and layered obfuscation prolongs the group's operational security and improves the efficacy of attacks."

### UNC5221 Drops New Versions of BRICKSTORM Targeting Windows

The disclosure comes as the China-nexus cyber espionage cluster named UNC5221 has been [connected](https://www.nviso.eu/blog/nviso-analyzes-brickstorm-espionage-backdoor) to use of a new version of the BRICKSTORM malware in attacks aimed at Windows environments in Europe since at least November 2022, according to Belgian cybersecurity firm NVISO.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

BRICKSTORM, [first documented](https://thehackernews.com/2024/05/china-linked-ha...