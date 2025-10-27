---
title: Russian APT28 Deploys “NotDoor” Outlook Backdoor Against Companies in NATO Countries
url: https://thehackernews.com/2025/09/russian-apt28-deploys-notdoor-outlook.html
source: The Hacker News
date: 2025-09-05
fetch_date: 2025-10-02T19:42:38.545778
---

# Russian APT28 Deploys “NotDoor” Outlook Backdoor Against Companies in NATO Countries

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

# [Russian APT28 Deploys "NotDoor" Outlook Backdoor Against Companies in NATO Countries](https://thehackernews.com/2025/09/russian-apt28-deploys-notdoor-outlook.html)

**Sep 04, 2025**Ravie LakshmananCybersecurity / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwhgINzgNirXlZNu6uMWQOzSQpkXFX5mDGt1yQPHtO2SlEBL5JhaNL2BjMrAxMYyKDMMML1L21Ke5hal5Cf_Rsc1EuNQtmmYwhdnu9Pv_J873ucjPw0MicZGydASEKUTFJHpMeffntgtwchJ3CXpFCHDPfJk8_AMbE0vgNoq5_bWFWWhqyJ_mHXXT0MJuA/s2600/email.jpg)

The Russian state-sponsored hacking group tracked as [APT28](https://thehackernews.com/2024/05/kremlin-backed-apt28-targets-polish.html) has been attributed to a new Microsoft Outlook backdoor called **NotDoor** in attacks targeting multiple companies from different sectors in NATO member countries.

NotDoor "is a VBA macro for Outlook designed to monitor incoming emails for a specific trigger word," S2 Grupo's LAB52 threat intelligence team [said](https://lab52.io/blog/analyzing-notdoor-inside-apt28s-expanding-arsenal/). "When such an email is detected, it enables an attacker to exfiltrate data, upload files, and execute commands on the victim's computer."

The artifact gets its name from the use of the word "Nothing" within the source code, the Spanish cybersecurity company added. The activity highlights the abuse of Outlook as a stealthy communication, data exfiltration, and malware delivery channel.

The exact initial access vector used to deliver the malware is currently not known, but analysis shows that it's deployed via Microsoft's OneDrive executable ("onedrive.exe") using a technique referred to as DLL side-loading.

This leads to the execution of a malicious DLL ("SSPICLI.dll"), which then installs the VBA backdoor and disables macro security protections.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Specifically, it runs Base64-encoded PowerShell commands to perform a series of actions that involve beaconing to an attacker-controlled webhook[.]site, setting up persistence through Registry modifications, enabling macro execution, and turning off Outlook-related dialogue messages to evade detection.

NotDoor is designed as an obfuscated Visual Basic for Applications (VBA) project for Outlook that makes use of the [Application.MAPILogonComplete](https://learn.microsoft.com/en-us/office/vba/api/outlook.application.mapilogoncomplete) and [Application.NewMailEx](https://learn.microsoft.com/en-us/office/vba/api/outlook.application.newmailex) events to run the payload every time Outlook is started or a new email arrives.

It then proceeds to create a folder at the path %TEMP%\Temp if it does not exist, using it as a staging folder to store TXT files created during the course of the operation and exfiltrate them to a Proton Mail address. It also parses incoming messages for a trigger string, such as "Daily Report," causing it to extract the embedded commands to be executed.

The malware supports four different commands -

* cmd, to execute commands and return the standard output as an email attachment
* cmdno, to execute commands
* dwn, to exfiltrate files from the victim's computer by sending them as email attachments
* upl, to drop files to the victim's computer

"Files exfiltrated by the malware are saved in the folder," LAB52 said. "The file contents are encoded using the malware's custom encryption, sent via email, and then deleted from the system."

The disclosure comes as Beijing-based 360 Threat Intelligence Center detailed [Gamaredon](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html)'s (aka APT-C-53) evolving tradecraft, highlighting its use of Telegram-owned Telegraph as a dead-drop resolver to point to command-and-control (C2) infrastructure.

The attacks are also notable for the abuse of Microsoft Dev Tunnels (devtunnels.ms), a service that allows developers to securely expose local web services to the internet for testing and debugging purposes, as C2 domains for added stealth.

"This technique provides twofold advantages: first, the original C2 server IP is completely masked by Microsoft's relay nodes, blocking threat intelligence tracebacks based on IP reputation," the cybersecurity company [said](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247507351&idx=1&sn=0b8c9e5b3ff9d7b6551b3a69c151f7e0&chksm=f9c1ee9eceb66788c94178eec69e10142c58dc7721874f9e4d3120d7ea952faa230221a6e2cc).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Second, by exploiting the service's ability to reset domain names on a minute-by-minute basis, the attackers can rapidly rotate infrastructure nodes, leveraging the trusted credentials and traffic scale of mainstream cloud services to maintain a nearly zero-exposure continuous threat operation."

Attack chains entail the use of bogus [Cloudflare Workers domains](https://thehackernews.com/2024/12/hackers-leveraging-cloudflare-tunnels.html) to distribute a Visual Basic Script like [PteroLNK](https://harfanglab.io/insidethelab/gamaredons-pterolnk-analysis/), which can propagate the infection to other machines by copying itself to connected USB drives, as well as download additional payloads.

"This attack chain demonstrates a high level of specialized design, employing four layers of obfuscation (registry persistence, dynamic compilation, path masquerading, cloud service abuse) to carry out a fully covert operation from initial implantation to data exfiltration," 360 Threat Intelligence Center said.

### Update

Kroll, in a separate analysis published on September 5, 2025, said it observed the NotDoor malware in a cyber espionage campaign targeting an unnamed entity. The risk advisory firm's threat intelligence team is tracking the cluster under the name KTA007 and the malware as GONEPOSTAL.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyTdJ4iojAKl5cCSpmI2Vvj1LupzFTAf1-CnhYLkGHWBTHliRuTPbGbztdKPPt0qF0c18d...