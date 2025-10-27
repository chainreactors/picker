---
title: Researchers 'Accidentally’ Crash KmsdBot Cryptocurrency Mining Botnet Network
url: https://thehackernews.com/2022/12/researchers-accidentally-crashed.html
source: The Hacker News
date: 2022-12-02
fetch_date: 2025-10-04T00:20:14.494487
---

# Researchers 'Accidentally’ Crash KmsdBot Cryptocurrency Mining Botnet Network

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

# [Malware Authors 'Accidentally' Crash KmsdBot Cryptocurrency Mining Botnet](https://thehackernews.com/2022/12/researchers-accidentally-crashed.html)

**Dec 01, 2022**Ravie LakshmananThreat Intelligence / Botnet

[![Cryptocurrency Mining Botnet Network](data:image/png;base64... "Cryptocurrency Mining Botnet Network")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhETFD4ShprDJ2YtALiWL0xUrq14DlB0tDThIi_CW0U3NcTbj4C_LJ6K2KvyiAvenO8SpstKREIewnxJsF1HbXPIv5ncDSfxJYyaynkqKPImQ0oPqKIV3J0wpiGRWCxhg-5MgpbW3gSgziyPBF53QYJRQ6G6ujMmP96h0dG9ihYEHlG8qYYFaJKWJto/s790-rw-e365/botnet.png)

An ongoing analysis into an up-and-coming cryptocurrency mining botnet known as **KmsdBot** has led to it being accidentally taken down by the threat actors themselves.

KmsdBot, as christened by the Akamai Security Intelligence Response Team (SIRT), came to light mid-November 2022 for its ability to [brute-force systems](https://thehackernews.com/2022/11/new-kmsdbot-malware-hijacking-systems.html) with weak SSH credentials.

The botnet strikes both Windows and Linux devices spanning a wide range of microarchitectures with the primary goal of deploying mining software and corralling the compromised hosts into a DDoS bot.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the major targets included gaming firms, technology companies, and luxury car manufacturers.

Akamai researcher Larry W. Cashdollar, in a new update, explained how commands sent by the malware operators to carry out a DDoS attack against the bitcoin[.]com website inadvertently neutralized the malware.

[![Cryptocurrency Mining Botnet Network](data:image/png;base64... "Cryptocurrency Mining Botnet Network")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhS8cvz1uqzZR-8JFuZsTWAd8h4EXKyaVPj5kreOpnnuPKqbHSKXnR5E9yaX7cupeDe3bD3QMv261Lmgij-DbV6tDGGvX_Doian25MfuJ0LUZpSavwf6pL1fGJtCgkb67rebd1pAACdTzltW_1Xz4kjVeuNAH52gL8ZV9L5aV-l_gwJQm5hbygsiipdaA/s790-rw-e365/code.png)

"Interestingly, after one single improperly formatted command, the bot stopped sending commands," Cashdollar [said](https://www.akamai.com/blog/security-research/kmsdbot-part-two-crashing-a-botnet). "It's not every day you come across a botnet that the threat actors themselves crash their own handiwork."

This, in turn, was made possible due to the lack of an error-checking mechanism built into the source code to validate the received commands.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, an instruction issued without a space between the target website and the port number caused the entire Go binary running on the infected machine to crash and stop interacting with its command-and-control server, effectively killing the botnet.

The fact that KmsdBot doesn't have a persistence mechanism also means that the malware operator will have to re-infect the machines again and re-build the infrastructure from scratch.

"This botnet has been going after some very large luxury brands and gaming companies, and yet, with one failed command it cannot continue," Cashdollar concluded. "This is a strong example of the fickle nature of technology and how even the exploiter can be exploited by it."

*(The story has been revised to reflect the fact that the authors of KmsdBot crashed the malware themselves, and not the researchers as previously stated.)*

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

[Akamai](https://thehackernews.com/search/label/Akamai)[botnet](https://thehackernews.com/search/label/botnet)[cryptocurrency](https://thehackernews.com/search/label/cryptocurrency)[cryptocurrency mining](https://thehackernews.com/search/label/cryptocurrency%20mining)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China...