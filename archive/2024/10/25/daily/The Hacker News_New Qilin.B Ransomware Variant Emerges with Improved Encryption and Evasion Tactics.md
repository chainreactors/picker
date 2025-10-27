---
title: New Qilin.B Ransomware Variant Emerges with Improved Encryption and Evasion Tactics
url: https://thehackernews.com/2024/10/new-qilinb-ransomware-variant-emerges.html
source: The Hacker News
date: 2024-10-25
fetch_date: 2025-10-06T18:55:59.956099
---

# New Qilin.B Ransomware Variant Emerges with Improved Encryption and Evasion Tactics

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

# [New Qilin.B Ransomware Variant Emerges with Improved Encryption and Evasion Tactics](https://thehackernews.com/2024/10/new-qilinb-ransomware-variant-emerges.html)

**Oct 24, 2024**Ravie LakshmananRansomware / Cybercrime

[![Qilin.B Ransomware](data:image/png;base64... "Qilin.B Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMNGkLWSf7ypaN6B6JCMZQGgFvRZAz22FDz9m6wW3n2mjaJvKPyPvGezA4qwnbgnvl0HXzuvxkDvqMQ0powFzctfI_LTiSPTOdQo1F3mioukocYI42j3FWJWITasPEFwyzID7w-8HXIiuSv8lozNtcYbF4UP3hhTQJKGVd6ppgp5GLV-IeCNQjPsqFlbAj/s790-rw-e365/ransomware.png)

Cybersecurity researchers have discovered an advanced version of the Qilin ransomware sporting increased sophistication and tactics to evade detection.

The new variant is being tracked by cybersecurity firm Halcyon under the moniker Qilin.B.

"Notably, Qilin.B now supports AES-256-CTR encryption for systems with AESNI capabilities, while still retaining Chacha20 for systems that lack this support," the Halcyon Research Team [said](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion) in a report shared with The Hacker News.

"Additionally, RSA-4096 with OAEP padding is used to safeguard encryption keys, making file decryption without the attacker's private key or captured seed values impossible."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Qilin, also known as [Agenda](https://thehackernews.com/2023/05/inside-qilin-ransomware-affiliates-take.html), first came to the attention of the cybersecurity community in July/August 2022, with initial versions written in Golang before switching to Rust.

A May 2023 report from Group-IB revealed that the ransomware-as-a-service (RaaS) scheme allows its affiliates to anywhere between 80% to 85% of each ransom payment after it infiltrated the group and managed to strike a conversation with a Qilin recruiter.

Recent attacks [linked](https://thehackernews.com/2024/08/new-qilin-ransomware-attack-uses-vpn.html) to the ransomware operation have stolen credentials stored in Google Chrome browsers on a small set of compromised endpoints, signaling a departure of sorts from typical double extortion attacks.

Qilin.B samples analyzed by Halcyon show that it builds on older iterations with additional encryption capabilities and improved operational tactics.

This includes the use of AES-256-CTR or Chacha20 for encryption, in addition to taking steps to resist analysis and detection by terminating services associated with security tools, continuously clearing Windows Event Logs, and deleting itself.

It also packs in features to kill processes linked to backup and virtualization services like Veeam, SQL, and SAP, and delete volume shadow copies, thereby complicating recovery efforts.

"Qilin.B's combination of enhanced encryption mechanisms, effective defense evasion tactics, and persistent disruption of backup systems marks it as a particularly dangerous ransomware variant," Halcyon said.

The [pernicious and persistent nature](https://www.halcyon.ai/blog/power-rankings-ransomware-malicious-quartile-q3-2024) of the threat posed by ransomware is evidenced in the ongoing evolutionary tactics demonstrated by ransomware groups.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYno0bcSRQhGj4hRrPLzmUcT7EYlgEAojzLGOWBDC_Xz4AEnOKjzwDm90sTFf-GvQw0x1t-TKReRuKpk0riEbMzIgqB1-T9WkcCJjJFGjIFDCbUJeFILDFEfhT58UcmvMlFFE1jLiKePMt77z2RqSbpRLkqjnusHM6942p15qKkHLVZ9L73X3Dxd_pM2x5/s790-rw-e365/chart.jpg)

This is exemplified by the discovery of a new Rust-based toolset that has been used to deliver the nascent Embargo ransomware, but not before terminating endpoint detection and response (EDR) solutions installed on the host using the Bring Your Own Vulnerable Driver ([BYOVD](https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html)) technique.

Both the EDR killer, codenamed MS4Killer by ESET owing to its similarities to the open-source [s4killer](https://github.com/gavz/s4killer) tool, and the ransomware is executed by means of a malicious loader referred to as MDeployer.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"MDeployer is the main malicious loader Embargo tries to deploy onto machines in the compromised network – it facilitates the rest of the attack, resulting in ransomware execution and file encryption," researchers Jan Holman and Tomáš Zvara [said](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/). "MS4Killer is expected to run indefinitely."

"Both MDeployer and MS4Killer are written in Rust. The same is true for the ransomware payload, suggesting Rust is the go-to language for the group's developers."

According to data shared by Microsoft, 389 U.S. healthcare institutions were hit by ransomware attacks this fiscal year, costing them up to $900,000 per day due to downtime. Some of the ransomware gangs known for striking hospitals include Lace Tempest, Sangria Tempest, Cadenza Tempest, and Vanilla Tempest.

"Out of the 99 healthcare organizations that admitted to paying the ransom and disclosed the ransom paid, the median payment was $1.5 million, and the average payment was $4.4 million," the tech giant [said](https://www.microsoft.com/en-us/security/security-insider/emerging-threats/US-healthcare-at-risk-strengthening-resiliency-against-ransomware-attacks).

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
[**Sh...