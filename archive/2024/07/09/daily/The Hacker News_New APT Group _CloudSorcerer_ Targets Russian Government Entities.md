---
title: New APT Group "CloudSorcerer" Targets Russian Government Entities
url: https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html
source: The Hacker News
date: 2024-07-09
fetch_date: 2025-10-06T17:47:27.032623
---

# New APT Group "CloudSorcerer" Targets Russian Government Entities

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

# [New APT Group "CloudSorcerer" Targets Russian Government Entities](https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html)

**Jul 08, 2024**Ravie LakshmananCyber Espionage / Cloud Security

[![Russian Government Entities](data:image/png;base64... "Russian Government Entities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbAWQ-mtrY8ID2PfS3d6laTVCrqGO5KPEXP0I6Zn_Ijl76kDozhyphenhypheng-neYy5PClMssA0vxCyOkw_w8WvMhOr29sCrZukN52ce15RGV_w2-MGcv3L1G7FpK4loyjE8m8McObAOrvipgRolYhb6lYmLU2b1znUXT_aqo0QEZjjuOVNM6YVwsQm8ppRMWntv4i/s790-rw-e365/hackers.png)

A previously undocumented advanced persistent threat (APT) group dubbed **CloudSorcerer** has been observed targeting Russian government entities by leveraging cloud services for command-and-control (C2) and data exfiltration.

Cybersecurity firm Kaspersky, which discovered the activity in May 2024, said the tradecraft adopted by the threat actor bears similarities with that of [CloudWizard](https://thehackernews.com/2023/05/bad-magics-extended-reign-in-cyber.html), but pointed out the differences in the malware source code. The attacks wield an innovative data-gathering program and a slew of evasion tactics for covering its tracks.

"It's a sophisticated cyber espionage tool used for stealth monitoring, data collection, and exfiltration via Microsoft Graph, Yandex Cloud, and Dropbox cloud infrastructure," the Russian security vendor [said](https://securelist.com/cloudsorcerer-new-apt-cloud-actor/113056/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The malware leverages cloud resources as its command and control (C2) servers, accessing them through APIs using authentication tokens. Additionally, CloudSorcerer uses GitHub as its initial C2 server."

The exact method used to infiltrate targets is currently unknown, but the initial access is exploited to drop a C-based portable executable binary that's used as a backdoor, initiate C2 communications, or inject shellcode into other legitimate processes based on the process in which it is executed – namely mspaint.exe, msiexec.exe, or contains the string "browser."

"The malware's ability to dynamically adapt its behavior based on the process it is running in, coupled with its use of complex inter-process communication through Windows pipes, further highlights its sophistication," Kaspersky noted.

The backdoor component is designed to collect information about the victim machine and retrieve instructions to enumerate files and folders, execute shell commands, perform file operations, and run additional payloads.

The C2 module, for its part, connects to a GitHub page that acts as a [dead drop resolver](https://attack.mitre.org/techniques/T1102/001/) to fetch an encoded hex string pointing to the actual server hosted on Microsoft Graph or Yandex Cloud.

"Alternatively, instead of connecting to GitHub, CloudSorcerer also tries to get the same data from hxxps://my.mail[.]ru/, which is a Russian cloud-based photo hosting server," Kaspersky said. "The name of the photo album contains the same hex string."

"The CloudSorcerer malware represents a sophisticated toolset targeting Russian government entities. Its use of cloud services such as Microsoft Graph, Yandex Cloud, and Dropbox for C2 infrastructure, along with GitHub for initial C2 communications, demonstrates a well-planned approach to cyber espionage."

### Update

Enterprise security firm Proofpoint said it detected a cyber campaign targeting an unnamed U.S.-based organization mirroring the tactics of CloudSorcerer. It's tracking the activity under the moniker UNK\_ArbitraryAcrobat.

The attack, observed in late May 2024, is said to have used a freemail account impersonating a well-known U.S. think tank and leveraged a fake event invitation as a lure to trick recipients into downloading a ZIP archive file hosted on acrobat-inst[.]com.

"If the ZIP file is downloaded and opened, a user is presented with a folder and three LNK files, all of which can be used to start the chain of malicious activity," the company [said](https://x.com/threatinsight/status/1810363156029649142).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The LNKs will launch either the PDF or Word Document embedded in the folder, then rename various components in the folder to new names, and then launch an embedded executable file, cache.tmp."

The loaded process subsequently reaches out to GitHub or TechNet profiles to fetch a hex-style blob that starts and ends with the same byte pattern "CDOY," matching observations made by Kaspersky.

Proofpoint threat researcher Greg Lesnewich told The Hacker News that the latest findings indicate the threat actor is employing spear-phishing techniques to infiltrate networks, although the possibility of other delivery methods cannot be ruled out. There is currently no evidence to suggest that the adversary is "targeting anything besides Windows operating systems."

*(The story was updated after publication to include additional comments from Proofpoint.)*

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

[Advanced Persistent Threat](https://thehackernews...