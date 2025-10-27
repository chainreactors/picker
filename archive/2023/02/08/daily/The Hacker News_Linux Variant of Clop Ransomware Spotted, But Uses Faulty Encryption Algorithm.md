---
title: Linux Variant of Clop Ransomware Spotted, But Uses Faulty Encryption Algorithm
url: https://thehackernews.com/2023/02/linux-variant-of-clop-ransomware.html
source: The Hacker News
date: 2023-02-08
fetch_date: 2025-10-04T06:03:19.466482
---

# Linux Variant of Clop Ransomware Spotted, But Uses Faulty Encryption Algorithm

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

# [Linux Variant of Clop Ransomware Spotted, But Uses Faulty Encryption Algorithm](https://thehackernews.com/2023/02/linux-variant-of-clop-ransomware.html)

**Feb 07, 2023**Ravie LakshmananEncryption / Linux

[![Linux Variant of Clop Ransomware](data:image/png;base64... "Linux Variant of Clop Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjh_SPFb2U7bYGXJeouO5K_nZG92gGEACrMl2Nu2p9hC-dtYxh4tYUFLZUR3zYWJYbZUOuYO9perqYMK4XIUHJFKR39alOyHUJizu3sKCVm5Z2HPz80HSkrJ6ThUKTyzi0zSc4sAE3-bCBfxgMnrirE6NHLf-pN84kF3DfRlPjbXuS-suYuRVJQvp2U/s790-rw-e365/lock.jpg)

The first-ever Linux variant of the Clop ransomware has been detected in the wild, but with a faulty encryption algorithm that has made it possible to reverse engineer the process.

"The ELF executable contains a flawed encryption algorithm making it possible to decrypt locked files without paying the ransom," SentinelOne researcher Antonis Terefos [said](https://s1.ai/Clop-ELF) in a report shared with The Hacker News.

The cybersecurity firm, which has [made available a decryptor](https://github.com/SentineLabs/Cl0p-ELF-Decryptor), said it observed the ELF version on December 26, 2022, while also noting its similarities to the Windows flavor when it comes using the same encryption method.

The detected sample is said to be part of a larger attack targeting educational institutions in Colombia, including La Salle University, around the same time. The university was added to the criminal group's leak site in early January 2023, per [FalconFeedsio](https://twitter.com/FalconFeedsio/status/1610873583844339712).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Known to have been active since 2019, the Clop (stylized as Cl0p) ransomware operation [suffered a major blow](https://thehackernews.com/2021/06/clop-gang-members-laundered-500-million.html) in June 2021 when six individuals affiliated with the gang were arrested following an international law enforcement exercise codenamed Operation Cyclone.

But the cybercrime group staged an "[explosive and unexpected](https://newsroom.nccgroup.com/news/ncc-group-monthly-threat-pulse-april-2022-448500)" comeback in early 2022, claiming dozens of victims spanning industrial and tech verticals.

SentinelOne characterized the Linux version as an early-stage version owing to the fact that some functions that are present in its Windows counterpart are missing.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguGrtvo88YC4RqkMwmZ4l7jbD_ktMt1JU19m3k3mgdc7OQGW_w32ghMrqGag5q_0C7272RW6umbuxmGNv5o5-PjxTlcME7hubP9TtvCNpYDY9tuLU0v_3o41CyVnhGRr4E7Z2UPottoZ7NimpO08QdPOFITsPPJEla-xYe7ETD99Fm6038doJZTRv0/s790-rw-e365/ransomware.png)

This lack of feature parity is also explained by the fact that the malware authors have opted to build a custom Linux payload rather than simply porting over the Windows version, suggesting that future variants of Clop could close those gaps.

"A reason for this could be that the threat actor has not needed to dedicate time and resources to improve obfuscation or evasiveness due to the fact that it is currently undetected by all 64 security engines on VirusTotal," Terefos explained.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Linux version is designed to single out specific folders and file types for encryption, with the ransomware containing a hard-coded master key that can be utilized to recover the original files without making a payment to the threat actors.

If anything, the development points to a growing trend of threat actors increasingly venturing beyond Windows to target other platforms.

"While the Linux-flavored variation of Cl0p is, at this time, in its infancy, its development and the almost ubiquitous use of Linux in servers and cloud workloads suggests that defenders should expect to see more Linux-targeted ransomware campaigns going forward," Terefos said.

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

[Clop Ransomware](https://thehackernews.com/search/label/Clop%20Ransomware)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hac...