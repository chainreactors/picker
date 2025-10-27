---
title: KmsdBot Botnet Suspected of Being Used as DDoS-for-Hire Service
url: https://thehackernews.com/2022/12/kmsdbot-botnet-suspected-of-being-used.html
source: The Hacker News
date: 2022-12-21
fetch_date: 2025-10-04T02:07:36.556148
---

# KmsdBot Botnet Suspected of Being Used as DDoS-for-Hire Service

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

# [KmsdBot Botnet Suspected of Being Used as DDoS-for-Hire Service](https://thehackernews.com/2022/12/kmsdbot-botnet-suspected-of-being-used.html)

**Dec 20, 2022**Ravie LakshmananServer Security / Cyber Attacks

[![KmsdBot Botnet](data:image/png;base64... "KmsdBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbfPi6JkmeUzsg-HzFETPyLs687dzChlLgbjB4q4huWzHme8KXtY6HSJTqwSCoTeGXchK2-9F9b-3m3EMGjXs_wN8TGlwWfBjAlWNYrbKDjnzE1jTKJHBDHqL0dMlSidCIed93VVu4n1tIsIIRA_XVYRcqFyTGnVfZVY4daI3y6hxm6YG7xwI7p0zP/s790-rw-e365/ddos.png)

An ongoing analysis of the **KmsdBot** botnet has raised the possibility that it's a DDoS-for-hire service offered to other threat actors.

This is based on the different industries and geographies that were attacked, web infrastructure company Akamai said. Among the notable targets included [FiveM](https://fivem.net/) and [RedM](https://redm.net/), which are game modifications for Grand Theft Auto V and Red Dead Redemption 2, as well as luxury brands and security firms.

KmsdBot is a [Go-based malware](https://thehackernews.com/2022/11/new-kmsdbot-malware-hijacking-systems.html) that leverages SSH to infect systems and carry out activities like cryptocurrency mining and launch commands using TCP and UDP to mount distributed denial-of-service (DDoS) attacks.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

However, a lack of an error-checking mechanism in the malware source code caused the criminal operators to inadvertently [crash their own botnet](https://thehackernews.com/2022/12/researchers-accidentally-crashed.html) last month.

"Based on observed IPs and domains, the majority of the victims are located in Asia, North America, and Europe," Akamai researchers Larry W. Cashdollar and Allen West [said](https://www.akamai.com/blog/security-research/kmsdbot-part-three-examining-attack-traffic). "The presence of these commands tracks with previous observations of targeted gaming servers and offers a glimpse into the customers of this botnet for hire."

[![KmsdBot Botnet](data:image/png;base64... "KmsdBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi14a1zqAtMwZ9VKEbkMOAFOP0qEu4c6B7GBECw6LfcArq4wYCuUzg67wIcwUvSrGewCkfXP6pcgxi2eFDs8q0-z6x75UgDzyAe8AmvCLXCGWozja24WimeUlnFwFuejBvvaYzQWiZBPJP_jfSdPlcvuHnWjAlas5PgLgqlARq0e2slXOAwnwRwpmVE/s790-rw-e365/map.png)

Akamai, which examined the attack traffic, identified 18 different commands that KmsdBot accepts from a remote server, one of which, dubbed "bigdata," caters to sending junk packets containing large amounts of data to a target in an attempt to exhaust its bandwidth.

Also included are commands such as "fivem" and "redm" that are designed to target video game mod servers, alongside a "scan" instruction that "appears to target specific paths within the target environment."

Charting the infection attempts of the botnet signals minimal activity in the Russian territory and neighboring regions, potentially offering a clue as to its origins.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A further breakdown of the attack commands observed over a 30-day time period shows "bigdata" leading with a frequency of more than 70. Calls to "fivem" have occurred 45 times, while "redm" has seen less than 10 calls.

"This tells us that although gaming servers are a specific target offered, it may not be the only industry that is being hit with these attacks," the researchers said. "Support for multiple types of servers increases the overall usability of this botnet and appears to be effective in driving in customers."

The KmsdBot botnet, in its current form, doesn't seek persistence on a machine, meaning its accidental disruption requires the attackers to rebuild the botnet from scratch. However, there are indications that the botnet may be making an attempt to stage a return.

"I did see infection attempts again about 24-48 hours after the bot went down and then attack commands started coming back in again around 24 hours after that," Cashdollar told The Hacker News. "But currently, the last known C2 appears to be null routed and the bot has been quiet."

The findings come a week after Microsoft detailed a cross-platform botnet known as [MCCrash](https://thehackernews.com/2022/12/minecraft-servers-under-attack.html) that comes with capabilities to carry out DDoS attacks against private Minecraft servers.

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

[botnet](https://thehackernews.com/search/label/botnet)[Go Programming](https://thehackernews.com/search/label/Go%20Programming)[hacking news](https://thehackernews.com/search/label/hacking%20news)[KmsdBot](https://thehackernews.com/search/label/KmsdBot)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehacker...