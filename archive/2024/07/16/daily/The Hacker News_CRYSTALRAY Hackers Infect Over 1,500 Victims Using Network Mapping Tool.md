---
title: CRYSTALRAY Hackers Infect Over 1,500 Victims Using Network Mapping Tool
url: https://thehackernews.com/2024/07/crystalray-hackers-infect-over-1500.html
source: The Hacker News
date: 2024-07-16
fetch_date: 2025-10-06T17:52:17.699366
---

# CRYSTALRAY Hackers Infect Over 1,500 Victims Using Network Mapping Tool

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

# [CRYSTALRAY Hackers Infect Over 1,500 Victims Using Network Mapping Tool](https://thehackernews.com/2024/07/crystalray-hackers-infect-over-1500.html)

**Jul 15, 2024**Ravie LakshmananSaaS Security / Vulnerability

[![Network Mapping Tool](data:image/png;base64... "Network Mapping Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhM3IekPl0FtKFBUIRU11rdAZUiarRY3pyYIOCNF3ZDSqj3xFe1XOgObSONcbvAmlou98By4iFbJh-xoPuiw5_jH1Oj7PCoyBKTW6RuUfngvdE12RHNdQMciqin0I79HCjKdCxmHDxEAxMN89iCOJyEr0CldhRbDvmWz_8Z_HN8JHJG9fUpla-4kY8woNG-/s790-rw-e365/apps.png)

A threat actor that was previously observed using an open-source network mapping tool has greatly expanded their operations to infect over 1,500 victims.

Sysdig, which is tracking the cluster under the name [CRYSTALRAY](https://sysdig.com/blog/CRYSTALRAY-rising-threat-actor-exploiting-oss-tools/), said the activities have witnessed a tenfold surge, adding it includes "mass scanning, exploiting multiple vulnerabilities, and placing backdoors using multiple [open-source software] security tools."

The primary objective of the attacks is to harvest and sell credentials, deploy cryptocurrency miners, and maintain persistence in victim environments. A majority of the infections are concentrated in the U.S., China, Singapore, Russia, France, Japan, and India, among others.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Prominent among the open-source programs used by the threat actor is [SSH-Snake](https://github.com/MegaManSec/SSH-Snake), which was first released in January 2024. It has been described as a tool to carry out automatic network traversal using SSH private keys discovered on systems.

The abuse of the software by CRYSTALRAY was [documented](https://thehackernews.com/2024/02/cybercriminals-weaponizing-open-source.html) by the cybersecurity company earlier this February, with the tool deployed for lateral movement following the exploitation of known security flaws in public-facing Apache ActiveMQ and Atlassian Confluence instances.

Joshua Rogers, the developer behind SSH-Snake, told The Hacker News at the time that the tool only automates what would have been otherwise manual steps, and called on companies to "discover the attack paths that exist – and fix them."

[![Network Mapping Tool](data:image/png;base64... "Network Mapping Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnAnjek5i0IOitkjJZB1ySK8CH3immuptzmBSikYXFMfaVNHhcmsK9ab5QeBnKjS8fSylqREFH5LiBCl_rgCco5rIDrMuHZ3kdtyU7XxgtuVIfyvrwasSQK8CtqjSITZrIWCa4a5d0_FjYfyuWIUqnUuwgpUgXI-wdTl5cCgBrk3uy_kvdElw0qRdkRY4h/s790-rw-e365/haceker.png)

Some of the other tools employed by the attackers include [asn](https://github.com/nitefood/asn), [zmap](https://github.com/zmap/zmap), [httpx](https://github.com/projectdiscovery/httpx), and [nuclei](https://github.com/projectdiscovery/nuclei) in order to check if a domain is active and launch scans for vulnerable services such as Apache ActiveMQ, Apache RocketMQ, Atlassian Confluence, Laravel, Metabase, Openfire, Oracle WebLogic Server, and Solr.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

CRYSTALRAY also weaponizes its initial foothold to conduct a wide-ranging credential discovery process that goes beyond moving between servers accessible via SSH. Persistent access to the compromised environment is accomplished by means of a legitimate command-and-control (C2) framework called [Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html) and a [reverse shell manager](https://www.archcloudlabs.com/projects/cryptojacking-adopts-termite-c2-utility/) codenamed [Platypus](https://github.com/WangYihang/Platypus).

In a further bid to derive monetary value from the infected assets, cryptocurrency miner payloads are delivered to illicitly use the victim resources for financial gain, while simultaneously taking steps to terminate competing miners that may have already been running on the machines.

"CRYSTALRAY is able to discover and extract credentials from vulnerable systems, which are then sold on black markets for thousands of dollars," Sysdig researcher Miguel Hernández said. "The credentials being sold involve a multitude of services, including Cloud Service Providers and SaaS email providers."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cryptocurrency mining](https://thehackernews.com/search/label/cryptocurrency%20mining)[Cyber threats](https://thehackernews.com/search/label/Cyber%20threats)[network security](https://thehackernews.com/search/label/network%20security)[Open-Source](https://thehackernews.com/search/label/Open-Source)[SaaS Security](https://thehackernews.com/search/label/SaaS%20Security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is...