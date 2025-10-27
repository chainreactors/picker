---
title: Noisy Bear Targets Kazakhstan Energy Sector With BarrelFire Phishing Campaign
url: https://thehackernews.com/2025/09/noisy-bear-targets-kazakhstan-energy.html
source: The Hacker News
date: 2025-09-07
fetch_date: 2025-10-02T19:47:53.548334
---

# Noisy Bear Targets Kazakhstan Energy Sector With BarrelFire Phishing Campaign

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

# [Noisy Bear Campaign Targeting Kazakhstan Energy Sector Outed as a Planned Phishing Test](https://thehackernews.com/2025/09/noisy-bear-targets-kazakhstan-energy.html)

**Sep 06, 2025**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJwP01hvXlLBWyWmZQ3T2ETpY2oqabj5DKEs-OfHlaotHz6BrQvUnkgc8zQSHk_XdMHhveYv9X2WajcLSZn6SWlnjRrgj1y_VNx4uIDXz03X9d5qgNbDBcoGuu03EbZnAOo8lwdxMphLKQTT5Az8TDJKg18XmZn01xGunYmW8-kibWWGxGqdxPLkpimA8n/s790-rw-e365/phish-malware.jpg)

A threat actor possibly of Russian origin has been attributed to a new set of attacks targeting the energy sector in Kazakhstan.

The activity, codenamed Operation BarrelFire, is tied to a new threat group tracked by Seqrite Labs as Noisy Bear. The threat actor has been active since at least April 2025.

"The campaign is targeted towards employees of KazMunaiGas or KMG where the threat entity delivered a fake document related to the KMG IT department, mimicking official internal communication and leveraging themes such as policy updates, internal certification procedures, and salary adjustments," security researcher Subhajeet Singha [said](https://www.seqrite.com/blog/operation-barrelfire-noisybear-kazakhstan-oil-gas-sector/).

The infection chain begins with a phishing email containing a ZIP attachment, which includes a Windows shortcut (LNK) downloader, a decoy document related to KazMunaiGas, and a README.txt file with instructions written in both Russian and Kazakh to run a program named "KazMunayGaz\_Viewer."

The email, per the cybersecurity company, was sent from a compromised email address of an individual working in the finance department of KazMunaiGas and targeted other employees of the firm in May 2025.

The LNK file payload is designed to drop additional payloads, including a malicious batch script that paves the way for a PowerShell loader dubbed DOWNSHELL. The attacks culminate with the deployment of a DLL-based implant, a 64-bit binary that can run shellcode to launch a reverse shell.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Further analysis of the threat actor's infrastructure has revealed that it's hosted on the Russia-based bulletproof hosting (BPH) service provider [Aeza Group](https://thehackernews.com/2025/07/us-sanctions-russian-bulletproof.html), which was sanctioned by the U.S. in July 2025 for enabling malicious activities.

The development comes as HarfangLab linked a Belarus-aligned threat actor known as [Ghostwriter](https://thehackernews.com/2025/02/belarus-linked-ghostwriter-uses.html) (aka FrostyNeighbor or UNC1151) to campaigns targeting Ukraine and Poland since April 2025 with rogue ZIP and RAR archives that are aimed at collecting information about compromised systems and deploying implants for further exploitation.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs8y1sxf2e2IM74j5BBF_uzndxomFkZPR_NG0rX7jmND23kiF-U8cWfDlomcnByFlKwcldaDPTqdNMIrdp3eUnijI-HgG4JNH2UOSjBuL1Cqssaj1InA3wAWmH7cHWoMUsnBeWCHClurHlVsyW3-S5rpzvBXkxdygivrWX0_tn9xI3nkQ7hQas0uhiTi3P/s2600/attack.jpg)

"These archives contain XLS spreadsheets with a VBA macro that drops and loads a DLL," the French cybersecurity company [said](https://harfanglab.io/insidethelab/uac-0057-pressure-ukraine-poland/). "The latter is responsible for collecting information about the compromised system and retrieving next-stage malware from a command-and-control (C2) server."

Subsequent iterations of the campaign have been found to write a Microsoft Cabinet (CAB) file along with the LNK shortcut to extract and run the DLL from the archive. The DLL then proceeds to conduct initial reconnaissance before dropping the next-stage malware from the external server.

The attacks targeting Poland, on the other hand, tweak the attack chain to use Slack as a beaconing mechanism and data exfiltration channel, downloading in return a second-stage payload that establishes contact with the domain pesthacks[.]icu.

At least in one instance, the DLL dropped through the macro-laced Excel spreadsheet is used to load a Cobalt Strike Beacon to facilitate further post-exploitation activity.

"These minor changes suggest that UAC-0057 may be exploring alternatives, in a likely attempt to work around detection, but prioritizes the continuity or development of its operations over stealthiness and sophistication," HarfangLab said.

### Cyber Attacks Reported Against Russia

The findings come amid [OldGremlin's](https://thehackernews.com/2022/10/oldgremlin-ransomware-targeted-over.html) renewed extortion attacks on Russian companies in the first half of 2025, targeting as many as eight large domestic industrial enterprises using phishing email campaigns.

The intrusions, per [Kaspersky](https://www.kaspersky.ru/about/press-releases/vozvrashenie-oldgremlin-kibergruppa-vymogatelej-vozobnovila-ataki-na-rossijskie-kompanii), involved the use of the bring your own vulnerable driver (BYOVD) technique to disable security solutions on victims' computers and the legitimate Node.js interpreter to execute malicious scripts.

Phishing attacks aimed at Russia have also [delivered](https://www.f6.ru/blog/phantom-stealer/) a new information stealer called Phantom Stealer, which is based on an open-source stealer codenamed [Stealerium](https://github.com/Stealerium/Stealerium), to collect a wide range of sensitive information using email baits related to adult content and payments. It also shares overlaps with another Stealerium offshoot known as [Warp Stealer](https://www.seqrite.com/blog/new-warp-malware-drops-modified-stealerium-infostealer/).

According to F6, Phantom Stealer also inherits Stealerium's "PornDetector" module that captures webcam screenshots when users visit pornographic websites by keeping tabs on the active browser window and whether the title includes a configurable list of terms like porn, and sex, among others.

[![CIS Build Kits](data...