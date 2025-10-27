---
title: Hackers Abuse EDRSilencer Tool to Bypass Security and Hide Malicious Activity
url: https://thehackernews.com/2024/10/hackers-abuse-edrsilencer-tool-to.html
source: The Hacker News
date: 2024-10-17
fetch_date: 2025-10-06T18:59:28.328198
---

# Hackers Abuse EDRSilencer Tool to Bypass Security and Hide Malicious Activity

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

# [Hackers Abuse EDRSilencer Tool to Bypass Security and Hide Malicious Activity](https://thehackernews.com/2024/10/hackers-abuse-edrsilencer-tool-to.html)

**Oct 16, 2024**Ravie LakshmananEndpoint Security / Malware

[![Hackers Abuse EDRSilencer Tool](data:image/png;base64... "Hackers Abuse EDRSilencer Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLYrop3Mz0QHVWdMYs0_HHvtf9HHKWYjXEmi0R1PxTxlKYT59cV2kO4hbPuLha7Sij993kI84aCOHKhjokeVS9StwxXsLXGxJ0T9UoafkQmdjnz-MI8nLhf1Wyr20HPS2ij7tQMbEg-bReXGQR3B6rE6XXha6oQEaivEvVE-ST7cJSkd-NOWFRCu_1FNHV/s790-rw-e365/hacker.png)

Threat actors are attempting to abuse the open-source EDRSilencer tool as part of efforts to tamper endpoint detection and response (EDR) solutions and hide malicious activity.

Trend Micro said it detected "threat actors attempting to integrate EDRSilencer in their attacks, repurposing it as a means of evading detection."

[EDRSilencer](https://github.com/netero1010/EDRSilencer), inspired by the [NightHawk FireBlock](https://www.mdsec.co.uk/2023/09/nighthawk-0-2-6-three-wise-monkeys/) tool from MDSec, is designed to block outbound traffic of running EDR processes using the Windows Filtering Platform ([WFP](https://learn.microsoft.com/en-us/windows/win32/fwp/windows-filtering-platform-start-page)).

It supports terminating various processes related to EDR products from Microsoft, Elastic, Trellix, Qualys, SentinelOne, Cybereason, Broadcom Carbon Black, Tanium, Palo Alto Networks, Fortinet, Cisco, ESET, HarfangLab, and Trend Micro.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

By incorporating such legitimate red teaming tools into their arsenal, the goal is to render EDR software ineffective and make it a lot more challenging to identify and remove malware.

"The WFP is a powerful framework built into Windows for creating network filtering and security applications," Trend Micro researchers [said](https://www.trendmicro.com/en_us/research/24/j/edrsilencer-disrupting-endpoint-security-solutions.html). "It provides APIs for developers to define custom rules to monitor, block, or modify network traffic based on various criteria, such as IP addresses, ports, protocols, and applications."

"WFP is used in firewalls, antivirus software, and other security solutions to protect systems and networks."

[![Hackers Abuse EDRSilencer Tool](data:image/png;base64... "Hackers Abuse EDRSilencer Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwWXP-ROQvjdXj0qAPqp4QuJviYmK5uO6vY1Ye3ByAFuR2ohJQdop-1wYmBgJRAjIx-IVG8_Atcq-TbL9Ew8Lt_dpgx-7LMlYrRCJRAEdAwxMAekJNsoWzm_tAWd0Owt2KaO6h7ga3SfRhOn6ktrUcYiUDdFxu04DW6MoczLbaummlKKe0uJgCf52C6jGX/s790-rw-e365/EDRSilencer.png)

EDRSilencer takes advantage of WFP by dynamically identifying running EDR processes and creating persistent WFP filters to block their outbound network communications on both IPv4 and IPv6, thereby preventing security software from sending telemetry to their management consoles.

The attack essentially works by scanning the system to gather a list of running processes associated with common EDR products, followed by running EDRSilencer with the argument "blockedr" (e.g., EDRSilencer.exe blockedr) to inhibit outbound traffic from those processes by configuring WFP filters.

"This allows malware or other malicious activities to remain undetected, increasing the potential for successful attacks without detection or intervention," the researchers said. "This highlights the ongoing trend of threat actors seeking more effective tools for their attacks, especially those designed to disable antivirus and EDR solutions."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as ransomware groups' use of formidable EDR-killing tools like [AuKill](https://thehackernews.com/2023/04/ransomware-hackers-using-aukill-tool-to.html) (aka AvNeutralizer), [EDRKillShifter](https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html), [TrueSightKiller, GhostDriver, and Terminator](https://thehackernews.com/2024/03/teamcity-flaw-leads-to-surge-in.html) is on the rise, with these programs weaponizing vulnerable drivers to escalate privileges and terminate security-related processes.

"EDRKillShifter enhances persistence mechanisms by employing techniques that ensure its continuous presence within the system, even after initial compromises are discovered and cleaned," Trend Micro [said](https://www.trendmicro.com/en_us/research/24/i/how-ransomhub-ransomware-uses-edrkillshifter-to-disable-edr-and-.html) in a recent analysis.

"It dynamically disrupts security processes in real-time and adapts its methods as detection capabilities evolve, staying a step ahead of traditional EDR tools."

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[EDR Solution](https://thehackernews.com/search/label/EDR%20Solution)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehacker...