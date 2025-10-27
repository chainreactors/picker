---
title: Iranian Hackers Set Up New Network to Target U.S. Political Campaigns
url: https://thehackernews.com/2024/08/iranian-hackers-set-up-new-network-to.html
source: The Hacker News
date: 2024-08-31
fetch_date: 2025-10-06T18:12:52.033638
---

# Iranian Hackers Set Up New Network to Target U.S. Political Campaigns

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

# [Iranian Hackers Set Up New Network to Target U.S. Political Campaigns](https://thehackernews.com/2024/08/iranian-hackers-set-up-new-network-to.html)

**Aug 30, 2024**Ravie LakshmananCyber Threat / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvkDJKVf4Rgrv1AF3icXmTkauTUUnJoGXCsA7YlZdIUAJvEfSRHY8cDMAm65kULJsZR8MVVo2zMnS3DCMvBnMcVvgz4ra_jSWXwGQ69HMnU7DcYEjVi71Ayb3LxSqYOvtvqfvPpP3dMSbANp2Ddl1uf7Zy_OpY78AldwT7vcASgdOygX7ZXm-QJs0GpcD3/s790-rw-e365/Iranianhackers.jpg)

Cybersecurity researchers have unearthed new network infrastructure set up by Iranian threat actors to support activities linked to the recent targeting of U.S. political campaigns.

Recorded Future's Insikt Group has linked the infrastructure to a hacking group it tracks as GreenCharlie, an Iran-nexus cyber threat group that [overlaps](https://thehackernews.com/2024/08/meta-exposes-iranian-hacker-group.html) with APT42, Charming Kitten, Damselfly, Mint Sandstorm (formerly Phosphorus), TA453, and Yellow Garuda.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The group's infrastructure is meticulously crafted, utilizing dynamic DNS (DDNS) providers like Dynu, DNSEXIT, and Vitalwerks to register domains used in phishing attacks," the cybersecurity company [said](https://www.recordedfuture.com/research/greencharlie-infrastructure-linked-us-political-campaign-targeting).

"These domains often employ deceptive themes related to cloud services, file sharing, and document visualization to lure targets into revealing sensitive information or downloading malicious files."

Examples include terms like "cloud," "uptimezone," "doceditor," "joincloud," and "pageviewer," among others. A majority of the domains were registered using the .info top-level domain (TLD), a shift from the previously observed .xyz, .icu, .network, .online, and .site TLDs.

The adversary has a track record of staging highly-targeted phishing attacks that leverage extensive social engineering techniques to infect users with malware like POWERSTAR (aka CharmPower and GorjolEcho) and [GORBLE](https://thehackernews.com/2024/08/openai-blocks-iranian-influence.html), which was recently identified by Google-owned Mandiant as used in campaigns against Israel and U.S.

GORBLE, [TAMECAT](https://thehackernews.com/2024/05/apt42-hackers-pose-as-journalists-to.html), and POWERSTAR are assessed to be variants of the same malware, a series of ever-evolving PowerShell implants deployed by GreenCharlie over the years. It's worth noting that Proofpoint detailed another POWERSTAR successor dubbed [BlackSmith](https://thehackernews.com/2024/08/iranian-cyber-group-ta453-targets.html) that was used in a spear-phishing campaign targeting a prominent Jewish figure in late July 2024.

The infection process is often a multi-stage one, which involves gaining initial access through phishing, followed by establishing communication with command-and-control (C2) servers, and ultimately exfiltrating data or delivering additional payloads.

Recorded Future's findings show that the threat actor registered a large number of DDNS domains since May 2024, with the company also identifying communications between Iran-based IP addresses (38.180.146[.]194 and 38.180.146[.]174) and GreenCharlie infrastructure between July and August 2024.

Furthermore, a direct link has been unearthed between GreenCharlie clusters and C2 servers used by GORBLE. It's believed that the operations are facilitated by means of Proton VPN or Proton Mail to obfuscate their activity.

"GreenCharlie's phishing operations are highly targeted, often employing social engineering techniques that exploit current events and political tensions," Recorded Future said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The group has registered numerous domains since May 2024, many of which are likely used for phishing activities. These domains are linked to DDNS providers, which allow for rapid changes in IP addresses, making it difficult to track the group's activities."

The disclosure comes amid a [ramping up of Iranian malicious cyber activity](https://thehackernews.com/2024/08/us-agencies-warn-of-iranian-hacking.html) against the U.S. and other foreign targets. Earlier this week, Microsoft revealed that multiple sectors in the U.S. and the U.A.E. are the target of an Iranian threat actor codenamed Peach Sandstorm (aka Refined Kitten).

Additionally, U.S. government agencies said yet another Iranian state-backed hacking crew, Pioneer Kitten, has moonlighted as an initial access broker (IAB) for facilitating ransomware attacks against education, finance, healthcare, defense, and government sectors in the U.S. in collaboration with NoEscape, RansomHouse, and BlackCat crews.

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Cyber threats](https://thehackernews.com/search/label/Cyber%20threats)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DNS](https://thehackernews.com/search/label/DNS)[Malware](https://thehackernews.com/search/label/...