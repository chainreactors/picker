---
title: New P2PInfect Worm Targets Redis Servers with Undocumented Breach Methods
url: https://thehackernews.com/2023/07/new-p2pinfect-worm-targets-redis.html
source: The Hacker News
date: 2023-08-01
fetch_date: 2025-10-06T17:04:41.416101
---

# New P2PInfect Worm Targets Redis Servers with Undocumented Breach Methods

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

# [New P2PInfect Worm Targets Redis Servers with Undocumented Breach Methods](https://thehackernews.com/2023/07/new-p2pinfect-worm-targets-redis.html)

**Jul 31, 2023**Ravie LakshmananCyber Threat / Botnet

[![P2PInfect Worm](data:image/png;base64... "P2PInfect Worm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmsu6laBK5j5fAZScT_-J1VmR0aHNztUr5Leb7jt5T8uVfLKiRqylRA6kVMbAh54Q0oKGXzLCmKs6vEmRt0e36xBbNbsneOa8uU_WOJh9U5FHnweMYefIwCSO0yJqiZOL5r-6UBPopfD8s5wXuJBS-4mdAK0T3cNY42a8tmrr9AnWcKunN4HrqDCAIvW6o/s790-rw-e365/worm.jpg)

The P2PInfect peer-to-peer (P2) worm has been observed employing previously undocumented initial access methods to breach susceptible Redis servers and rope them into a botnet.

"The malware compromises exposed instances of the Redis data store by exploiting the replication feature," Cado Security researchers Nate Bill and Matt Muir [said](https://www.cadosecurity.com/redis-p2pinfect/) in a report shared with The Hacker News.

"A common attack pattern against Redis in cloud environments is to exploit this feature using a malicious instance to enable replication. This is achieved via connecting to an exposed Redis instance and issuing the SLAVEOF command."

The Rust-based malware was [first documented](https://thehackernews.com/2023/07/new-p2pinfect-worm-targeting-redis.html) by Palo Alto Networks Unit 42, calling out the malware's ability to exploit a critical Lua sandbox escape vulnerability ([CVE-2022-0543](https://nvd.nist.gov/vuln/detail/CVE-2022-0543), CVSS score: 10.0) to obtain a foothold into Redis instances. The campaign is believed to have commenced on or after June 29, 2023.

However, the latest discovery suggests that the threat actors behind the campaign are leveraging multiple exploits for initial access.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This is not the first time the [SLAVEOF command](https://medium.com/%40knownsec404team/rce-exploits-of-redis-based-on-master-slave-replication-ef7a664ce1d0) has been abused in the wild. Previously, threat actors associated with malware families such as [H2Miner](https://www.alibabacloud.com/blog/new-outbreak-of-h2miner-worms-exploiting-redis-rce-detected_595743) and [HeadCrab](https://thehackernews.com/2023/02/new-threat-stealthy-headcrab-malware.html) have abused the attack technique to [illicitly mine cryptocurrency](https://www.microsoft.com/en-us/security/blog/2023/07/25/cryptojacking-understanding-and-defending-against-cloud-compute-resource-abuse/) on compromised hosts.

In doing so, the goal is to replicate a malicious instance and load a malicious module to activate the infection.

Another initial access vector entails the registration of a malicious cron job on the Redis host to download the malware from a remote server upon execution, a method previously observed in attacks mounted by the [WatchDog cryptojacking group](https://thehackernews.com/2023/03/new-cryptojacking-campaign-leverages.html).

A successful breach is followed by the distribution of next-stage payloads that allow the malware to alter [iptables firewall rules](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands) at will, upgrade itself, and potentially deploy cryptocurrency miners at a later date once the botnet has grown to a specific size.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The P2Pinfect malware makes use of a peer-to-peer botnet," the researchers said. "Each infected server is treated as a node, which then connects to other infected servers. This allows the entire botnet to gossip with each other without using a centralized C2 server."

A notable trait of the botnet is its worming behavior, enabling it to expand its reach by using a list of passwords to brute-force SSH servers and attempting to exploit the Lua sandbox escape vulnerability or use the SLAVEOF command in the case of Redis servers.

The identity of the threat actors behind the campaign is currently unknown and the purpose of P2PInfect remains unclear, with Unit 42 previously noting that the indicators don't overlap with any of the known cryptojacking groups.

"P2Pinfect is well-designed and utilizes sophisticated techniques for replication and C2," the researchers concluded. "The choice of using Rust also allows for easier portability of code across platforms (with the Windows and Linux binaries sharing a lot of the same code), while also making static analysis of the code significantly harder."

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

[botnet](https://thehackernews.com/search/label/botnet)[Cado Security](https://thehackernews.com/search/label/Cado%20Security)[Malware](https://thehackernews.com/search/label/Malware)[Peer-to-Peer](https://thehackernews.com/search/label/Peer-to-Peer)[Redis](https://thehackernews.com/search/label/Redis)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the ...