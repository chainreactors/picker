---
title: Researchers Shed Light on APT31's Advanced Backdoors and Data Exfiltration Tactics
url: https://thehackernews.com/2023/08/researchers-shed-light-on-apt31s.html
source: The Hacker News
date: 2023-08-12
fetch_date: 2025-10-04T12:03:43.817237
---

# Researchers Shed Light on APT31's Advanced Backdoors and Data Exfiltration Tactics

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

# [Researchers Shed Light on APT31's Advanced Backdoors and Data Exfiltration Tactics](https://thehackernews.com/2023/08/researchers-shed-light-on-apt31s.html)

**Aug 11, 2023**Ravie LakshmananMalware / Cyber Attack

[![Backdoors and Data Exfiltration Tactics](data:image/png;base64... "Backdoors and Data Exfiltration Tactics")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiuGNa8T5VV5rml1Id-qDRzQ4ixrtVVVZ3rDXSzA2f7YgUrdkEJwo00dxSSZSTJv3SCCFAEorU5LfAMpvsLQjF5JzeI-Z9W_sKRTTqDpigxBfwTQVvx0wmoTz4zceIKZRkn45IUhuYq59GW7_nKFBneqwe51RMSoh6_2B4u41KahKoCa-HNPX2ojyG6YA30/s790-rw-e365/code.jpg)

The Chinese threat actor known as APT31 (aka Bronze Vinewood, Judgement Panda, or Violet Typhoon) has been linked to a set of advanced backdoors that are capable of exfiltrating harvested sensitive information to Dropbox.

The malware is part of a broader collection of [more than 15 implants](https://thehackernews.com/2023/08/chinas-apt31-suspected-in-attacks-on.html) that have been put to use by the adversary in attacks targeting industrial organizations in Eastern Europe in 2022.

"The attackers aimed to establish a permanent channel for data exfiltration, including data stored on air-gapped systems," Kaspersky [said](https://ics-cert.kaspersky.com/publications/reports/2023/08/10/common-ttps-of-attacks-against-industrial-organizations-implants-for-uploading-data/) in an analysis spotlighting APT31's previously undocumented tradecraft.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The intrusions employ a three-stage malware stack, each focused on disparate aspects of the attack chain: setting up persistence, gathering sensitive data, and transmitting the information to a remote server under the threat actor's control.

Some variants of the second-stage backdoors also come with features designed to look up file names in the Microsoft Outlook folder, execute remote commands, and employ the third-phase component to complete the data exfiltration step in the form of RAR archive files.

"The first step is used for persistence, the deployment and startup of the second-step malware module, which is responsible for uploading the files collected to the server by calling the third-step implant and cleaning up," the Russian cybersecurity firm said.

In what's a novel twist, APT31 is said to have used a command-and-control (C2) inside the corporate perimeter and leveraged it as a proxy to siphon data from systems that lacked direct access to the internet, indicating clear attempts to single out air-gapped hosts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Kaspersky said it also spotted additional tools used by the attacker to manually upload the data to Yandex Disk and other temporary file-sharing services such as extraimage, imgbb, imgshare, schollz, and zippyimage, among others. A third similar implant is configured to send the data via the Yandex email service.

The findings highlight the meticulous planning and the ability of the threat actor to adapt and spin up new capabilities in their cyber espionage pursuits.

"Abusing popular cloud-based data storages may allow the threat actor(s) to evade security measures," the company said. "At the same time, it opens up the possibility for stolen data to be leaked a second time in the event that a third party gets access to a storage used by the threat actor(s)."

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

[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Kaspersky](https://thehackernews.com/search/label/Kaspersky)[Microsoft Outlook](https://thehackernews.com/search/label/Microsoft%20Outlook)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networ...