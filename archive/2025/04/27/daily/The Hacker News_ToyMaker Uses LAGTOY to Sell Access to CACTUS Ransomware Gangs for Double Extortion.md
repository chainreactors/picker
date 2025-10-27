---
title: ToyMaker Uses LAGTOY to Sell Access to CACTUS Ransomware Gangs for Double Extortion
url: https://thehackernews.com/2025/04/toymaker-uses-lagtoy-to-sell-access-to.html
source: The Hacker News
date: 2025-04-27
fetch_date: 2025-10-06T22:04:15.765961
---

# ToyMaker Uses LAGTOY to Sell Access to CACTUS Ransomware Gangs for Double Extortion

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

# [ToyMaker Uses LAGTOY to Sell Access to CACTUS Ransomware Gangs for Double Extortion](https://thehackernews.com/2025/04/toymaker-uses-lagtoy-to-sell-access-to.html)

**Apr 26, 2025**Ravie LakshmananMalware / Vulnerability

[![CACTUS Ransomware](data:image/png;base64... "CACTUS Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh54Ourbq0zwfMhEZX9sf4vQJs2M2fFY4gwxptBvJZMvHyv4PmtBsfgC42z9pRGWLLvlVVkdDhmVe3gWkhSmVj2Shf709LV92TPN-OQ2xwvauNY42DPJ0f964MdhZKx5fyM0MzkECmNsq-u319RORNmGA7xR1_JNHC0pRGE4gDDCy8HIxPEgM76zZhXBTQH/s790-rw-e365/hacker-iab.jpg)

Cybersecurity researchers have detailed the activities of an initial access broker (IAB) dubbed **ToyMaker** that has been observed [handing over access](https://thehackernews.com/2024/11/new-ymir-ransomware-exploits-memory-for.html) to double extortion ransomware gangs like [CACTUS](https://thehackernews.com/2025/03/researchers-link-cactus-ransomware.html).

The IAB has been assessed with medium confidence to be a financially motivated threat actor, scanning for vulnerable systems and deploying a custom malware called LAGTOY (aka HOLERUN).

"LAGTOY can be used to create reverse shells and execute commands on infected endpoints," Cisco Talos researchers Joey Chen, Asheer Malhotra, Ashley Shen, Vitor Ventura, and Brandon White [said](https://blog.talosintelligence.com/introducing-toymaker-an-initial-access-broker/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware was first documented by Google-owned Mandiant in late March 2023, attributing its use to a threat actor it tracks as [UNC961](https://thehackernews.com/2023/09/cyber-group-gold-melody-selling.html). The activity cluster is also known by other names such as Gold Melody and Prophet Spider.

The threat actor has been observed leveraging a huge arsenal of known security flaws in internet-facing applications to obtain initial access, followed by conducting reconnaissance, credential harvesting, and LAGTOY deployment within a span of a week.

The attackers also open SSH connections to a remote host to download a forensics tool called Magnet RAM Capture to obtain a memory dump of the machine in a likely attempt to gather the victim's credentials.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZLAC3hBRUDTT4cBo5F4RMXHh12jfEVqHyhrHPE6X80HGXc3yXUdw4cmQqC8VWL0aG4Lq5IV1r7PGTKTdT3Lr-lCnksuw02V9N5bLBhyhOMS_xZLz062bISs2QPauNVOKwyGi929FxPl3HHob_Vdw8vKs5-GWZ5IQod_hCupnB38XtwR_eRuJz5Rv9KFpG/s790-rw-e365/malware.jpg)

LAGTOY is [designed](https://cloud.google.com/blog/topics/threat-intelligence/unc961-multiverse-financially-motivated) to contact a hard-coded command-and-control (C2) server to retrieve commands for subsequent execution on the endpoint. It can be used to create processes and run commands under specified users with corresponding privileges, per Mandiant.

The malware is also equipped to process three commands from the C2 server with a Sleep interval of 11000 milliseconds between them.

"After a lull in activity of approximately three weeks, we observed the CACTUS ransomware group make its way into the victim enterprise using credentials stolen by ToyMaker," Talos said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Based on the relatively short dwell time, the lack of data theft and the subsequent handover to CACTUS, it is unlikely that ToyMaker had any espionage-motivated ambitions or goals."

In the incident analyzed by Talos, the CACTUS ransomware affiliates are said to have conducted reconnaissance and persistence activities of their own prior to data exfiltration and encryption. Also observed are multiple methods to set up long-term access using OpenSSH, AnyDesk, and eHorus Agent.

"ToyMaker is a financially-motivated initial access broker (IAB) who acquires access to high-value organizations and then transfers that access to secondary threat actors who usually monetize the access via double extortion and ransomware deployment," the company said.

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

[Cisco Talos](https://thehackernews.com/search/label/Cisco%20Talos)[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Initial Access Broker](https://thehackernews.com/search/label/Initial%20Access%20Broker)[Malware](https://thehackernews.com/search/label/Malware)[Mandiant](https://thehackernews.com/search/label/Mandiant)[Memory Dump](https://thehackernews.com/search/label/Memory%20Dump)[ransomware](https://thehackernews.com/search/label/ransomware)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI S...