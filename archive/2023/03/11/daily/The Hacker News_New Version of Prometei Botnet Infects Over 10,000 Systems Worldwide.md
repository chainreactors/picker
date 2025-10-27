---
title: New Version of Prometei Botnet Infects Over 10,000 Systems Worldwide
url: https://thehackernews.com/2023/03/new-version-of-prometei-botnet-infects.html
source: The Hacker News
date: 2023-03-11
fetch_date: 2025-10-04T09:18:37.590203
---

# New Version of Prometei Botnet Infects Over 10,000 Systems Worldwide

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

# [New Version of Prometei Botnet Infects Over 10,000 Systems Worldwide](https://thehackernews.com/2023/03/new-version-of-prometei-botnet-infects.html)

**Mar 10, 2023**Ravie LakshmananEndpoint Security / Hacking

[![Prometei Botnet](data:image/png;base64... "Prometei Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqv961TEQDaqfU4ifnpZv9CcwRCvLOH0_JOvDrWW_ivOwYKq0IDcG7YKApmxg8OEqRZOJ1UW2LTilDm7Lpg0JF3zMAIDOPiHv_qslnbd3Uqj0EKztLcZIyLlUuosi7Q1kCbAAGFGmy2bPrYHgxlrf1Ivjq2GIwdU0gCizeleuudOXgUZBWbKqBHIz3/s790-rw-e365/botnet.png)

An updated version of a botnet malware called **Prometei** has infected more than 10,000 systems worldwide since November 2022.

The infections are both geographically indiscriminate and opportunistic, with a majority of the victims reported in Brazil, Indonesia, and Turkey.

Prometei, first observed in 2016, is a modular botnet that features a large repertoire of components and several proliferation methods, some of which also include the [exploitation](https://thehackernews.com/2021/04/prometei-botnet-exploiting-unpatched.html) of ProxyLogon Microsoft Exchange Server flaws.

It's also notable for avoiding striking Russia, suggesting that the threat actors behind the operation are likely based in the country.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cross-platform botnet's motivations are financial, primarily leveraging its pool of infected hosts to mine cryptocurrency and harvest credentials.

The latest variant of Prometei (called v3) improves upon its existing features to challenge forensic analysis and further burrow its access on victim machines, Cisco Talos [said](https://blog.talosintelligence.com/prometei-botnet-improves/) in a report shared with The Hacker News.

[![Prometei Botnet](data:image/png;base64... "Prometei Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMiD0XqwyM82fZJszQ4o_BMHMjAcIIOrLgfes5NH_15WrkjmQj2S52uuNTIiIH6USVF5crSabTSTxpADQsTAOgEA1uoCvXBi4NQh1c7enZhj_7HqabfVE8wshI8vlVGUpXJQCCZXsywLxSkgUrXTjpXJQnNPzeb67eeF1S5kXzw0DxEW-1R2HUbbNf/s790-rw-e365/map.png)

The attack sequence proceeds thus: Upon gaining a successful foothold, a PowerShell command is executed to download the botnet malware from a remote server. Prometei's main module is then used to retrieve the actual crypto-mining payload and other auxiliary components on the system.

Some of these support modules function as spreader programs designed to propagate the malware through Remote Desktop Protocol ([RDP](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol)), Secure Shell ([SSH](https://en.wikipedia.org/wiki/Secure_Shell)), and Server Message Block ([SMB](https://en.wikipedia.org/wiki/Server_Message_Block)).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Prometei v3 is also noteworthy for using a domain generation algorithm ([DGA](https://en.wikipedia.org/wiki/Domain_generation_algorithm)) to build out its command-and-control (C2) infrastructure. It further packs in a self-update mechanism and an expanded set of commands to harvest sensitive data and commandeer the host.

Last but not least, the malware deploys an Apache web server that's bundled with a PHP-based web shell, which is capable of executing Base64-encoded commands and carrying out file uploads.

"This recent addition of new capabilities aligns with threat researchers' previous assertions that the Prometei operators are continuously updating the botnet and adding functionality," Talos said.

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

[botnet](https://thehackernews.com/search/label/botnet)[Microsoft](https://thehackernews.com/search/label/Microsoft)[Prometei](https://thehackernews.com/search/label/Prometei)[ProxyLogon](https://thehackernews.com/search/label/ProxyLogon)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX an...