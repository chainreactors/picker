---
title: New EAGERBEE Variant Targets ISPs and Governments with Advanced Backdoor Capabilities
url: https://thehackernews.com/2025/01/new-eagerbee-variant-targets-isps-and.html
source: The Hacker News
date: 2025-01-08
fetch_date: 2025-10-06T20:15:09.962957
---

# New EAGERBEE Variant Targets ISPs and Governments with Advanced Backdoor Capabilities

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

# [New EAGERBEE Variant Targets ISPs and Governments with Advanced Backdoor Capabilities](https://thehackernews.com/2025/01/new-eagerbee-variant-targets-isps-and.html)

**Jan 07, 2025**Ravie LakshmananCyber Attack / Hacking

[![Advanced Backdoor Capabilities](data:image/png;base64... "Advanced Backdoor Capabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfQa9xZi5U744tJL51LdFlQUwuEK5b73bZYEYAClqyAe8n0rgwOuPr-D8qBdmIOlQRVj0a2NrIAXVpr4CxqPVclvr9axir0QnNHAhfKOaHLwEqd_1UrtGR-Utfr54wVQntt7fggepMFJTErcHtJ2XhXkwXJn9iXx3DGELK2nRcgIAy-y3neP5yxlHxPTpx/s790-rw-e365/map.png)

Internet service providers (ISPs) and governmental entities in the Middle East have been targeted using an updated variant of the EAGERBEE malware framework.

The new variant of EAGERBEE (aka [Thumtais](https://www.lac.co.jp/lacwatch/report/20240605_004019.html)) comes fitted with various components that allow the backdoor to deploy additional payloads, enumerate file systems, and execute commands shells, demonstrating a significant evolution.

"The key plugins can be categorized in terms of their functionality into the following groups: Plugin Orchestrator, File System Manipulation, Remote Access Manager, Process Exploration, Network Connection Listing, and Service Management," Kaspersky researchers Saurabh Sharma and Vasily Berdnikov [said](https://securelist.com/eagerbee-backdoor/115175/) in an analysis.

The backdoor has been assessed by the Russian cybersecurity company with medium confidence to a threat group called CoughingDown.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

EAGERBEE was [first documented](https://thehackernews.com/2023/11/chinese-hackers-launch-covert-espionage.html) by the Elastic Security Labs, attributing it to a state-sponsored and espionage-focused intrusion set dubbed REF5961. A "technically straightforward backdoor" with forward and reverse command-and-control and SSL encryption capabilities, it's designed to conduct basic system enumeration and deliver subsequent executables for post-exploitation.

Subsequently, a variant of the malware was observed in attacks by a Chinese state-aligned threat cluster tracked as Cluster Alpha as part of a broader cyber espionage operation codenamed [Crimson Palace](https://thehackernews.com/2024/06/chinese-state-backed-cyber-espionage.html) with an aim to steal sensitive military and political secrets from a high-profile government organization in Southeast Asia.

Cluster Alpha, per Sophos, overlaps with threat groups tracked as BackdoorDiplomacy, REF5961, Worok, and TA428. BackdoorDiplomacy, for its part, is known to exhibit tactical similarities with another Chinese-speaking group codenamed [CloudComputating](https://thehackernews.com/2021/06/new-cyber-espionage-group-targeting.html) (aka Faking Dragon), which has been attributed to a multi-plugin malware framework referred to as QSC in attacks targeting the telecom industry in South Asia.

"QSC is a modular framework, of which only the initial loader remains on disk while the core and network modules are always in memory," Kaspersky [noted](https://securelist.com/cloudcomputating-qsc-framework/114438/) back in November 2024. "Using a plugin-based architecture gives attackers the ability to control which plugin (module) to load in memory on demand depending on the target of interest."

In the latest set of attacks involving EAGERBEE, an injector DLL is designed to launch the backdoor module, which is then used to collect system information and exfiltrate the details to a remote server to which a connection is established via a TCP socket. However, the exact initial entry point used in these intrusions remains unknown at this stage.

The server subsequently responds with a Plugin Orchestrator that, in addition to reporting system-related information to the server (e.g., NetBIOS name of the domain; physical and virtual memory usage; and system locale and time zone settings), harvests details about running processes and awaits further instructions -

* Receive and inject plugins into memory
* Unload a specific plugin from memory, remove the plugin from the list
* Remove all plugins from the list
* Check if the plugin is loaded or not

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"All the plugins are responsible for receiving and executing commands from the orchestrator," the researchers said, adding they perform file operations, manage processes, maintain remote connections, manage system services, and list network connections.

Kaspersky said it also observed EAGERBEE being deployed in several organizations in East Asia, with two of them breached using the ProxyLogon vulnerability (CVE-2021-26855) to drop web shells that were then used to execute commands on the servers, ultimately leading to the backdoor deployment.

EAGERBEE is "a malware framework primarily designed to operate in memory," the researchers pointed out. "This memory-resident architecture enhances its stealth capabilities, helping it evade detection by traditional endpoint security solutions."

"EAGERBEE also obscures its command shell activities by injecting malicious code into legitimate processes. These tactics allow the malware to seamlessly integrate with normal system operations, making it significantly more challenging to identify and analyze."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on H...