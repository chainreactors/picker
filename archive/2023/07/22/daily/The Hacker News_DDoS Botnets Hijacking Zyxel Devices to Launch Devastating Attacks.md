---
title: DDoS Botnets Hijacking Zyxel Devices to Launch Devastating Attacks
url: https://thehackernews.com/2023/07/ddos-botnets-hijacking-zyxel-devices-to.html
source: The Hacker News
date: 2023-07-22
fetch_date: 2025-10-04T11:58:03.314363
---

# DDoS Botnets Hijacking Zyxel Devices to Launch Devastating Attacks

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

# [DDoS Botnets Hijacking Zyxel Devices to Launch Devastating Attacks](https://thehackernews.com/2023/07/ddos-botnets-hijacking-zyxel-devices-to.html)

**Jul 21, 2023**Ravie LakshmananVulnerability / Botnet

[![distributed denial-of-service (DDoS)](data:image/png;base64... "distributed denial-of-service (DDoS)")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiR1VswotL6o8mAJg7uvzsqtADj2GeQapKknMMih_emF3SEeJaeDmZZrKItYQeygTBEN96yYTIHOjs6uoKfTwO3yYB8dmgz2vu6NZikHQu7WeDpihjqwGV2mYtacRjtuDOfEatjEgrqLF2jBXmRDrLUqV_NPATcCwuRyu1FXGq9iw5p34jwBvqk5hSJFNpm/s790-rw-e365/ddos-attack.jpg)

Several distributed denial-of-service (DDoS) botnets have been observed exploiting a critical flaw in Zyxel devices that came to light in April 2023 to gain remote control of vulnerable systems.

"Through the capture of exploit traffic, the attacker's IP address was identified, and it was determined that the attacks were occurring in multiple regions, including Central America, North America, East Asia, and South Asia," Fortinet FortiGuard Labs researcher Cara Lin [said](https://www.fortinet.com/blog/threat-research/ddos-botnets-target-zyxel-vulnerability-cve-2023-28771).

The flaw, tracked as CVE-2023-28771 (CVSS score: 9.8), is a command injection bug affecting multiple firewall models that could potentially allow an unauthorized actor to execute arbitrary code by sending a specifically crafted packet to the targeted appliance.

Last month, the Shadowserver Foundation [warned](https://thehackernews.com/2023/06/active-mirai-botnet-variant-exploiting.html) that the flaw was being "actively exploited to build a Mirai-like botnet" at least since May 26, 2023, an indication of how abuse of [servers running unpatched software](https://thehackernews.com/2022/03/hackers-abuse-mitel-devices-to-amplify.html) is on the rise.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The latest findings from Fortinet suggest that the shortcoming is being opportunistically leveraged by multiple actors to breach susceptible hosts and corral them into a botnet capable of launching DDoS attacks against other targets.

This comprises [Mirai botnet](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/) variants such as Dark.IoT and another botnet that has been dubbed Katana by its author, which comes with capabilities to mount DDoS attacks using TCP and UDP protocols.

"It appears that this campaign utilized multiple servers to launch attacks and updated itself within a few days to maximize the compromise of Zyxel devices," Lin said.

The disclosure comes as Cloudflare [reported](https://blog.cloudflare.com/ddos-threat-report-2023-q2/) an "alarming escalation in the sophistication of DDoS attacks" in the second quarter of 2023, with threat actors devising novel ways to evade detection by "adeptly imitating browser behavior" and keeping their attack rates-per-second relatively low.

[![DDoS Botnets](data:image/png;base64... "DDoS Botnets")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikYTFZCTev_AhXnCNPGuMvYQ-QND4wFYpMXwmi3AgSxlZH3nvh4LXkMGnFKlonFdiu0FFdZJQEoCP27yk5O10bfkhs52CxBlajqz92cucwPsZolNz4BxaZ3kV2iqnDrB4DWbiRfF6WOx-lgAHZoYDhWgSdrd-BK-il8Emcyiz5XC0JrjWmPO-53CXQT9d3/s790-rw-e365/ddos-attack.png)

Adding to the complexity is the use of DNS laundering attacks to conceal malicious traffic via reputable recursive DNS resolvers and virtual machine botnets to orchestrate hyper-volumetric DDoS attacks.

"In a DNS Laundering attack, the threat actor will query subdomains of a domain that is managed by the victim's DNS server," Cloudflare explained. "The prefix that defines the subdomain is randomized and is never used more than once or twice in such an attack."

"Due to the randomization element, recursive DNS servers will never have a cached response and will need to forward the query to the victim's authoritative DNS server. The authoritative DNS server is then bombarded by so many queries until it cannot serve legitimate queries or even crashes all together."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another noteworthy factor contributing to the increase in DDoS offensives is the emergence of [pro-Russian hacktivist groups](https://thehackernews.com/2023/07/ddosia-attack-tool-evolves-with.html) such as KillNet, REvil, and Anonymous Sudan (aka Storm-1359) that have overwhelmingly focused on targets in the U.S. and Europe. There is no evidence to connect REvil to the widely known [ransomware group](https://thehackernews.com/2022/05/new-revil-samples-indicate-ransomware.html).

KillNet's "regular creation and absorption of new groups is at least partially an attempt to continue to garner attention from Western media and to enhance the influence component of its operations," Mandiant [said](https://www.mandiant.com/resources/blog/killnet-new-capabilities-older-tactics) in a new analysis, adding the group's targeting has "consistently aligned with established and emerging Russian geopolitical priorities."

"KillNet's structure, leadership, and capabilities have undergone several observable shifts over the course of the last 18 months, progressing toward a model that includes new, higher profile affiliate groups intended to garner attention for their individual brands in addition to the broader KillNet brand," it further added.

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
[**Share on Hacker N...