---
title: TIDRONE Espionage Group Targets Taiwan Drone Makers in Cyber Campaign
url: https://thehackernews.com/2024/09/tidrone-espionage-group-targets-taiwan.html
source: The Hacker News
date: 2024-09-10
fetch_date: 2025-10-06T18:31:58.288663
---

# TIDRONE Espionage Group Targets Taiwan Drone Makers in Cyber Campaign

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

# [TIDRONE Espionage Group Targets Taiwan Drone Makers in Cyber Campaign](https://thehackernews.com/2024/09/tidrone-espionage-group-targets-taiwan.html)

**Sep 09, 2024**Ravie LakshmananCyber Attack / Threat Intelligence

[![Espionage Group](data:image/png;base64... "Espionage Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYQY5sOh6LMF8vawGqS-tDTJZyA9Qh875JVIS2Jzv4q1QSaFbUGRZTjjEEqXsN_CHgflyMLeRuIGJVidpC5omB1JehRuPJJDiO3yeSGObKB2fDNzsqtx5TOLILvj9N5UcyNLAWC962Y607IV2ZhI6IXFO226_W-Uz8Rjpg4_wa0G6fz40VmntCyWaaYuSK/s790-rw-e365/drone.png)

A previously undocumented threat actor with likely ties to Chinese-speaking groups has predominantly singled out drone manufacturers in Taiwan as part of a cyber attack campaign that commenced in 2024.

Trend Micro is [tracking](https://www.trendmicro.com/en_us/research/24/i/tidrone-targets-military-and-satellite-industries-in-taiwan.html) the adversary under the moniker **TIDRONE**, stating the activity is espionage-driven given the focus on military-related industry chains.

The exact initial access vector used to breach targets is presently unknown, with Trend Micro's analysis uncovering the deployment of custom malware such as CXCLNT and CLNTEND using remote desktop tools like UltraVNC.

An interesting commonality observed across different victims is the presence of the same enterprise resource planning (ERP) software, raising the possibility of a supply chain attack.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The attack chains subsequently go through three different stages that are designed to facilitate privilege escalation by means of a User Account Control ([UAC](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/)) bypass, credential dumping, and defense evasion by disabling antivirus products installed on the hosts.

[![Drone Makers](data:image/png;base64... "Drone Makers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUmvMIw40eccFgT_8aqw6fS2-1o9mQO_zAmMZxE6sjRg1gBdbiMTWHj7JdAJg6IZWO1Rqvj2ej1BGbx7yD0JJ6h1lIiGb4U3BNUwTnE-iTSHtymhUc0rtC9lnkeEN0CDLe2LAXvqpl4hY5x4GHFiaoaMcmBHzzHmSVADzJfLwNAKADIAB4XjgLrQ0IMdmO/s790-rw-e365/hack.png)

Both the backdoors are initiated by sideloading a rogue DLL via the Microsoft Word application, allowing the threat actors to harvest a wide range of sensitive information,

CXCLNT comes equipped with basic upload and download file capabilities, as well as features for clearing traces, collecting victim information such as file listings and computer names, and downloading next-stage portable executable (PE) and DLL files for execution.

CLNTEND, first detected in April 2024, is a discovered remote access tool (RAT) that supports a wider range of network protocols for communication, including TCP, HTTP, HTTPS, TLS, and SMB (port 445).

"The consistency in file compilation times and the threat actor's operation time with other Chinese espionage-related activities supports the assessment that this campaign is likely being carried out by an as-yet unidentified Chinese-speaking threat group," security researchers Pierre Lee and Vickie Su said.

### Update

Cybersecurity firm Acronis has published its own findings into the campaign, which it has dubbed **Operation WordDrone**, stating it observed the attacks between April and July 2024.

The intrusions are also characterized by the use of a technique called [Blindside](https://thehackernews.com/2022/12/guloader-malware-utilizing-new.html) to evade detection by endpoint detection and response (EDR) software prior to deploying CLNTEND (aka ClientEndPoint).

Acronis further revealed that the malicious artifacts were detected inside the folder of a Taiwanese ERP software called Digiwin, alluding to the possibility of either a supply chain attack or the exploitation of a security flaw in the product to gain initial access.

[![TIDRONE Espionage](data:image/png;base64... "TIDRONE Espionage")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh65DyUuhEps6lzo_T4jeZ00s-D2XiP4_D0WzEJBySJdKEwG3xabaDeN2WiVcCTO9KwuuL1wWyZOilgrwthS9IvqaXda1NEMqNJgt8SG1aQXmZiJoSt1Ien3D0MtTdAQp36qY9_PYEZonBP3XJyKrux1AY-6NYF9z3B7zd6-cL_C-4Gx96M4J8UGRjpM-rQ/s790-rw-e365/disk.png)

"There are about a dozen companies in Taiwan participating in drone manufacturing — often for OEM purposes — and even more if we look at their global aerospace industry," the Singapore-based company [said](https://www.acronis.com/en-us/cyber-protection-center/posts/operation-worddrone-drone-manufacturers-are-being-targeted-in-taiwan/).

"The country has always been a U.S. ally, and that, coupled with Taiwan's strong technological background, makes them a prime target for adversaries interested in military espionage or supply chain attacks."

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

[china](https://thehackernews.com/search/label/china)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[Military Technology](https://thehackernews.com/search/label/Military%20Technology)[remote...