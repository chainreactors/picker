---
title: New Cryptojacking Campaign Leverages Misconfigured Redis Database Servers
url: https://thehackernews.com/2023/03/new-cryptojacking-campaign-leverages.html
source: The Hacker News
date: 2023-03-03
fetch_date: 2025-10-04T08:33:38.595619
---

# New Cryptojacking Campaign Leverages Misconfigured Redis Database Servers

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

# [New Cryptojacking Campaign Leverages Misconfigured Redis Database Servers](https://thehackernews.com/2023/03/new-cryptojacking-campaign-leverages.html)

**Mar 02, 2023**Ravie LakshmananData Security / Cryptojacking

[![Cryptojacking](data:image/png;base64... "Cryptojacking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuI3j8HG3_G4EANm4h34ocUQZFAa01h981bdDsW9Kdc4ZJg21HOmdyBJHxUohyzMoNG8KXo4JXio4q0Fjw-9fmS0IrSRDdrHNKKjxbQRwtBt5zB4Vl4_-s3a0J4Fr6d5Z-z1__d_Y-HQY3GhhJb8mr4ZNtQqLSU9jzRGJj49PvxOhIUDdzIwCv_h62/s790-rw-e365/redis.png)

Misconfigured Redis database servers are the target of a novel cryptojacking campaign that leverages a legitimate and open source command-line file transfer service to implement its attack.

"Underpinning this campaign was the use of transfer[.]sh," Cado Security [said](https://www.cadosecurity.com/redis-miner-leverages-command-line-file-hosting-service/) in a report shared with The Hacker News. "It's possible that it's an attempt at evading detections based on other common code hosting domains (such as pastebin[.]com)."

The cloud cybersecurity firm said the command line interactivity associated with transfer[.]sh has made it an ideal tool for hosting and delivering malicious payloads.

The attack chain commences with targeting insecure Redis deployments, followed by registering a [cron job](https://en.wikipedia.org/wiki/Cron) that leads to arbitrary code execution when parsed by the scheduler. The job is designed to retrieve a payload hosted at transfer[.]sh.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's worth noting that [similar](https://unit42.paloaltonetworks.com/teamtnt-cryptojacking-watchdog-operations/) [attack mechanisms](https://www.cadosecurity.com/tales-from-the-honeypot-watchdog-evolves-with-a-new-multi-stage-cryptojacking-attack/) have been employed by other threat actors like TeamTNT and [WatchDog](https://www.cadosecurity.com/watchdog-continues-to-target-east-asian-csps/) in their cryptojacking operations.

The payload is a script that paves the way for an XMRig cryptocurrency miner, but not before taking preparatory steps to free up memory, terminate competing miners, and install a network scanner utility called pnscan to find vulnerable Redis servers and propagate the infection.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj3eM9I9TWMvu2reqQUtOpNPRZxS19Ov8izEXRBhlaILtTFZRnto0jRLL2n5LA0Hepd1EIvhfrOg2aOOXoYoM4u3n0275XmrpK7jMTHwEsPRfdbIaStAv-BN77iooOfGu0H22v-tVGBB9WE-xpU-4DCPRcde2FyW9xVio1JFdn31s4pG2M4afTk5lxd/s790-rw-e365/server.png)

"Although it is clear that the objective of this campaign is to hijack system resources for mining cryptocurrency, infection by this malware could have unintended effects," the company said. "Reckless configuration of Linux memory management systems could quite easily result in corruption of data or the loss of system availability."

The development makes it the latest threat to strike Redis servers after [Redigo](https://thehackernews.com/2022/12/hackers-exploiting-redis-vulnerability.html) and [HeadCrab](https://thehackernews.com/2023/02/new-threat-stealthy-headcrab-malware.html) in recent months.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings also come as Avertium [disclosed](https://www.avertium.com/resources/threat-reports/ssh-scanning-and-xorddos-propagation) a new set of attacks in which SSH servers are brute-forced to deploy the [XorDdos botnet](https://thehackernews.com/2022/05/microsoft-warns-rise-in-xorddos-malware.html) malware on compromised servers with the goal of launching distributed denial-of-service (DDoS) attacks against targets located in China and the U.S.

The cybersecurity company said it observed 1.2 million unauthorized SSH connection attempts across 18 honeypots between October 6, 2022, and December 7, 2022. It attributed the activity to a threat actor based in China.

42% of those attempts originated from 49 IP addresses assigned to ChinaNet Jiangsu Province Network, with the rest emanating from 8,000 IP addresses scattered all over the world.

"It was found that once the scanning identified an open port, it would be subject to a brute-force attack against the 'root' account using a list of approximately 17,000 passwords," Avertium said. "Once the brute-force attack was successful, a XorDDoS bot was installed."

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

[Cado Security](https://thehackernews.com/search/label/Cado%20Security)[cryptojacking](https://thehackernews.com/search/label/cryptojacking)[database security](https://thehackernews.com/search/label/database%20security)[Redis](https://thehackernews.com/search/label/Redis)[Server Securiy](https://thehackernews.com/search/label/Server%20Securiy)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Exec...