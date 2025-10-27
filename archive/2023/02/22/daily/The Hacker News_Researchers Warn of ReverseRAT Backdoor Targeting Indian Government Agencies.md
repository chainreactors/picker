---
title: Researchers Warn of ReverseRAT Backdoor Targeting Indian Government Agencies
url: https://thehackernews.com/2023/02/researchers-warn-of-reverserat-backdoor.html
source: The Hacker News
date: 2023-02-22
fetch_date: 2025-10-04T07:48:13.301746
---

# Researchers Warn of ReverseRAT Backdoor Targeting Indian Government Agencies

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

# [Researchers Warn of ReverseRAT Backdoor Targeting Indian Government Agencies](https://thehackernews.com/2023/02/researchers-warn-of-reverserat-backdoor.html)

**Feb 21, 2023**Ravie LakshmananCyber Threat / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgCCfHSIzoDTc6xFjFRi_e6UJchPjWfF1XiN5ghEE_ZWupVSF0UxOOgSMFCWUS6pEIF5s2SR7RwWCQdrYErIlq-PoU6CBIyH-HE_LpJvFWnjvFN-g8tUC95mQqqX9RwzZ5ntf6Q0nl4GMCQ66R8ri3fFedynpHmQl8vKbLSftEK5AVDrlKtGEFUjsS/s790-rw-e365/india.png)

A spear-phishing campaign targeting Indian government entities aims to deploy an updated version of a backdoor called **ReverseRAT**.

Cybersecurity firm ThreatMon [attributed](https://threatmon.io/apt-sidecopy-targeting-indian-government-entities/) the activity to a threat actor tracked as **SideCopy**.

SideCopy is a threat group of Pakistani origin that shares overlaps with another actor called [Transparent Tribe](https://thehackernews.com/2022/11/researchers-detail-new-malware-campaign.html). It is so named for mimicking the infection chains associated with [SideWinder](https://thehackernews.com/2023/02/researchers-link-sidewinder-group-to.html) to deliver its own malware.

The adversarial crew was first observed delivering ReverseRAT in 2021, when Lumen's Black Lotus Labs [detailed](https://thehackernews.com/2021/06/pakistan-linked-hackers-targeted-indian.html) a set of attacks targeting victims aligned with the government and power utility verticals in India and Afghanistan.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Recent attack campaigns associated with SideCopy have primarily [set their sights](https://thehackernews.com/2022/12/researchers-warn-of-kavach-2fa-phishing.html) on a two-factor authentication solution known as Kavach (meaning "armor" in Hindi) that's used by Indian government officials.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHrsB9ahlvfoC0BK98nqa5wVx3c8zesB29o3y_rTYuwCGzJMNeq8cB6DvJak0BVW2X_NScaD782zTI8AnSIiK-dKYVm40u2aEOn9LR7CE_7j0UCSNLyWTlePo9iovWpS9pJ_oTArWvP5QvN7qkkPOh4OY6a2Z_vgJoa6_xImOllKn6QW4Wpl2bQPy1/s790-rw-e365/a.png)

The infection journey documented by ThreatMon commences with a phishing email containing a macro-enabled Word document ("Cyber Advisory 2023.docm").

The file masquerades as a fake advisory from India's Ministry of Communications about "Android Threats and Preventions." That said, most of the content has been [copied verbatim](https://dot.gov.in/sites/default/files/2020_07_09%20Cybersec%20SA.pdf) from an actual alert published by the department in July 2020 about best cybersecurity practices.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Once the file is opened and macros are enabled, it triggers the execution of malicious code that leads to the deployment of ReverseRAT on the compromised system.

"Once ReverseRAT gains persistence, it enumerates the victim's device, collects data, encrypts it using RC4, and sends it to the command-and-control (C2) server," the company said in a report published last week.

"It waits for commands to execute on the target machine, and some of its functions include taking screenshots, downloading and executing files, and uploading files to the C2 server."

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Pakistani Hackers](https://thehackernews.com/search/label/Pakistani%20Hackers)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehac...