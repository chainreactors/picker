---
title: New Agenda Ransomware Variant, Written in Rust, Aiming at Critical Infrastructure
url: https://thehackernews.com/2022/12/new-agenda-ransomware-variant-written.html
source: The Hacker News
date: 2022-12-20
fetch_date: 2025-10-04T02:01:23.259666
---

# New Agenda Ransomware Variant, Written in Rust, Aiming at Critical Infrastructure

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

# [New Agenda Ransomware Variant, Written in Rust, Aiming at Critical Infrastructure](https://thehackernews.com/2022/12/new-agenda-ransomware-variant-written.html)

**Dec 19, 2022**Ravie LakshmananData Security / Endpoint Security

[![agenda ransomware](data:image/png;base64... "agenda ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5KeDEDBr-aAoyF9pL9SP19MlpLNmSz1Rs9FJOF0TEk-oBXGljqcNYtZrTfTDMAedjc890dZe9zEOWnLAo_vyhl9pzViO0HcTJB72bxc0-dVe-O_UWQ77Vg-FJekx4NN3AELExQ4D_uznaWr3KoVmVYPyUoZbWK7leQdRcmQtSm1Ma9GVNL84lmk_j/s790-rw-e365/ransomware.png)

A Rust variant of a ransomware strain known as **Agenda** has been observed in the wild, making it the latest malware to adopt the cross-platform programming language after [BlackCat, Hive, Luna, and RansomExx](https://thehackernews.com/2022/11/new-ransomexx-ransomware-variant.html).

[Agenda](https://thehackernews.com/2022/08/new-golang-based-agenda-ransomware-can.html), attributed to an operator named Qilin, is a ransomware-as-a-service (RaaS) group that has been linked to a spate of attacks primarily targeting manufacturing and IT industries across different countries.

A previous version of the ransomware, written in Go and customized for each victim, singled out healthcare and education sectors in countries like Indonesia, Saudi Arabia, South Africa, and Thailand.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Agenda, like [Royal ransomware](https://thehackernews.com/2022/12/royal-ransomware-threat-takes-aim-at-us.html), expands on the idea of partial encryption (aka intermittent encryption) by configuring parameters that are used to determine the percentage of file content to be encrypted.

[![agenda ransomware](data:image/png;base64... "agenda ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikeMr50rkSulpKuvQEksnWaN9dcK1zOYaZPM0en9OKnR9GkxvCCPNKfffLyc1v4xX6oDuiuk7tSQwcHRSNjLoXLKFrDjX-a7q8uehH66-Plgn7YNhCl9LyaEtcRkHiVtJcm90RJUxaaRgMMuBhY4TgwfO6bRWzjUyywXWyBzmiyOV1F4XbEeunu5NL/s790-rw-e365/ilin.png)

"This tactic is becoming more popular among ransomware actors as it lets them encrypt faster and avoid detections that heavily rely on read/write file operations," a group of researchers from Trend Micro [said](https://www.trendmicro.com/en_us/research/22/l/agenda-ransomware-uses-rust-to-target-more-vital-industries.html) in a report last week.

An analysis of the ransomware binary reveals that encrypted files are given the extension "MmXReVIxLV," before proceeding to drop the ransom note in every directory.

In addition, the Rust version of Agenda is capable of terminating the Windows AppInfo process and disabling User Account Control (UAC), the latter of which helps mitigate the impact of malware by requiring administrative access to launch a program or task.

"At present, its threat actors appear to be migrating their ransomware code to Rust as recent samples still lack some features seen in the original binaries written in the Golang variant of the ransomware," the researchers noted.

"Rust language is becoming more popular among threat actors as it is more difficult to analyze and has a lower detection rate by antivirus engines."

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

[Malware](https://thehackernews.com/search/label/Malware)[ransomware](https://thehackernews.com/search/label/ransomware)[Rust Programming Language](https://thehackernews.com/search/label/Rust%20Programming%20Language)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "...