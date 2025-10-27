---
title: Cyberattack Group 'Awaken Likho' Targets Russian Government with Advanced Tools
url: https://thehackernews.com/2024/10/cyberattack-group-awaken-likho-targets.html
source: The Hacker News
date: 2024-10-09
fetch_date: 2025-10-06T19:10:19.362733
---

# Cyberattack Group 'Awaken Likho' Targets Russian Government with Advanced Tools

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

# [Cyberattack Group 'Awaken Likho' Targets Russian Government with Advanced Tools](https://thehackernews.com/2024/10/cyberattack-group-awaken-likho-targets.html)

**Oct 08, 2024**Ravie LakshmananCyber Threat / APT Attack

[![Russian Government with Advanced Tools](data:image/png;base64... "Russian Government with Advanced Tools")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglX-UW5Ck4vfzKKues9bXi1LUD98bO6cbV9P7QqoU5dTlYPs8FEjVKH544_eRaxDdrPf_nQo6yuX54aTMiUrv_jhCZpGNG3M7FcgIsdOEHTpKKH8HXoV0q9V-tgfpjvtmkQY-z-UlJRLKCkHkBjR3SnYeDWO-766H2bG5Ak921TaQy3c3huiO3Dut4VbpA/s790-rw-e365/russia.png)

Russian government agencies and industrial entities are the target of an ongoing activity cluster dubbed **Awaken Likho**.

"The attackers now prefer using the agent for the legitimate MeshCentral platform instead of the UltraVNC module, which they had previously used to gain remote access to systems," Kaspersky [said](https://securelist.com/awaken-likho-apt-new-implant-campaign/114101/), detailing a new campaign that began in June 2024 and continued at least until August.

The Russian cybersecurity company said the campaign primarily targeted Russian government agencies, their contractors, and industrial enterprises.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Awaken Likho, also tracked as Core Werewolf and PseudoGamaredon, was [first documented](https://bi.zone/eng/expertise/blog/core-werewolf-protiv-opk-i-kriticheskoy-infrastruktury/) by BI.ZONE in June 2023 in connection with cyber attacks directed against defense and critical infrastructure sectors. The group is believed to be active since at least August 2021.

The spear-phishing attacks involve distributing malicious executables disguised as Microsoft Word or PDF documents by assigning them double extensions like "doc.exe," ".docx.exe," or ".pdf.exe," so that only the .docx and .pdf portions of the extension show up for users.

Opening these files, however, has been found to trigger the installation of UltraVNC, thereby allowing the threat actors to gain complete control of the compromised hosts.

Other attacks mounted by Core Werewolf have also singled out a Russian military base in Armenia as well as a Russian research institute engaged in weapons development, per [findings](https://www.facct.ru/blog/core-werewolf/) from F.A.C.C.T. earlier this May.

One notable change observed in these instances concerns the use of a self-extracting archive (SFX) to facilitate the covert installation of UltraVNC while displaying an innocuous lure document to the targets.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The latest attack chain discovered by Kaspersky also relies on an SFX archive file created using 7-Zip that, when opened, triggers the execution of a file named "MicrosoftStores.exe," which then unpacks an AutoIt script to ultimately run the open-source [MeshAgent](https://thehackernews.com/2024/05/cyber-espionage-alert-lilacsquid.html) remote management tool.

"These actions allow the APT to persist in the system: the attackers create a scheduled task that runs a command file, which, in turn, launches MeshAgent to establish a connection with the MeshCentral server," Kaspersky said.

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

[APT Attack](https://thehackernews.com/search/label/APT%20Attack)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Kaspersky](https://thehackernews.com/search/label/Kaspersky)[remote access tool](https://thehackernews.com/search/label/remote%20access%20tool)[Spear-Phishing Attack](https://thehackernews.com/search/label/Spear-Phishing%20Attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on...