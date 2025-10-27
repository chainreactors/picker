---
title: New Ransomware-as-a-Service 'Eldorado' Targets Windows and Linux Systems
url: https://thehackernews.com/2024/07/new-ransomware-as-service-eldorado.html
source: The Hacker News
date: 2024-07-09
fetch_date: 2025-10-06T17:47:29.684433
---

# New Ransomware-as-a-Service 'Eldorado' Targets Windows and Linux Systems

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

# [New Ransomware-as-a-Service 'Eldorado' Targets Windows and Linux Systems](https://thehackernews.com/2024/07/new-ransomware-as-service-eldorado.html)

**Jul 08, 2024**Ravie LakshmananRansomware / Encryption

[![Ransomware-as-a-Service](data:image/png;base64... "Ransomware-as-a-Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqaqt6f7Up8mPDo9tUp-usTlDng9cVeNXKLiHEpcHyMZUiZvREWQ-OjdYH_atv4FRmCnGSJJQTeDH_4_NgDQ2Hr-AnaY_Q2VotL7dKIT2BgjqpquzKzbH4OYRAkuLfqjYZKvi4q0mSp46W5EnL81K4nAHC_DVJU4N3WgT6gy1cgphBbr6p3PSLQsNiwDS8/s790-rw-e365/ransomware.png)

An emerging ransomware-as-a-service (RaaS) operation called Eldorado comes with locker variants to encrypt files on Windows and Linux systems.

Eldorado first appeared on March 16, 2024, when an advertisement for the affiliate program was posted on the ransomware forum RAMP, Singapore-headquartered Group-IB said.

The cybersecurity firm, which infiltrated the ransomware group, noted that its representative is a Russian speaker and that the malware does not overlap with previously leaked strains such as LockBit or Babuk.

"The Eldorado ransomware uses Golang for cross-platform capabilities, employing Chacha20 for file encryption and Rivest Shamir Adleman-Optimal Asymmetric Encryption Padding (RSA-OAEP) for key encryption," researchers Nikolay Kichatov and Sharmine Low [said](https://www.group-ib.com/blog/eldorado-ransomware/). "It can encrypt files on shared networks using Server Message Block (SMB) protocol."

The encryptor for Eldorado comes in four formats, namely esxi, esxi\_64, win, and win\_64, with its data leak site already listing 16 victims of June 2024. Thirteen of the targets are located in the U.S., two in Italy, and one in Croatia.

These companies span various industry verticals such as real estate, education, professional services, healthcare, and manufacturing, among others.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Further analysis of the Windows version of artifacts has revealed the use of a PowerShell command to overwrite the locker with random bytes before deleting the file in an attempt to clean up the traces.

Eldorado is the latest in the list of new double-extortion ransomware players that have sprung up in recent times, including [Arcus Media](https://ransomwareattacks.halcyon.ai/news/emerging-ransomware-threat-actors-arcus-media-apt73-dan0n-space-bears), [AzzaSec](https://www.broadcom.com/support/security-center/protection-bulletin/azzasec-ransomware), [Brain Cipher](https://socradar.io/dark-web-profile-brain-cipher/), [dan0n](https://ransomwareattacks.halcyon.ai/news/emerging-ransomware-threat-actors-arcus-media-apt73-dan0n-space-bears), [Limpopo](https://www.fortinet.com/blog/threat-research/ransomware-roundup-shinra-and-limpopo-ransomware) (aka SOCOTRA, FORMOSA, SEXi), [LukaLocker](https://www.halcyon.ai/blog/halcyon-identifies-new-ransomware-operator-volcano-demon-serving-up-lukalocker), [Shinra](https://www.fortinet.com/blog/threat-research/ransomware-roundup-shinra-and-limpopo-ransomware), and [Space Bears](https://ransomwareattacks.halcyon.ai/news/emerging-ransomware-threat-actors-arcus-media-apt73-dan0n-space-bears), once again highlighting the enduring and persistent nature of the threat.

[![Ransomware-as-a-Service](data:image/png;base64... "Ransomware-as-a-Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk4Qz-4Sj-98oxAUiN6chtm3vBOw0A5rWou1DTFeeHPQzZMFORL95JQR7_6TfNaKjtJK4DCafST0mP8kWWhtrTwUmBpBCTc1olTKV6wnufZK-wwdsHq_ubR7w-qpCGLtQBhXfzilNjdvMlxnSzNBLtlTxF3Hdu5p1yiy-Cdr3d1ol_Z4ZMWpKuNf-GNpju/s790-rw-e365/ib.png)

LukaLocker, linked to an operator dubbed Volcano Demon by Halcyon, is notable for the fact that it does not make use of a data leak site and instead calls the victim over the phone to extort and negotiate payment after encrypting Windows workstations and servers.

The development coincides with the discovery of new Linux variants of [Mallox](https://thehackernews.com/2024/05/ongoing-campaign-bombarded-enterprises.html) (aka Fargo, TargetCompany, and Mawahelper) ransomware as well as decryptors associated with seven different builds.

[![Ransomware-as-a-Service](data:image/png;base64... "Ransomware-as-a-Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgw-AV1l9N2CDuo_fhV4RmWFFCY3mVHDqurNkGhx0cGKsx7iSlhK5BrUIUOeXb7eKxDMlOMOYL4I7MSquFgS42YMVgzyrFMnwVOMMXInTY1U3i7SwX-AKJq3soK2iwZwKH-j5kU4SJ8T_QUW6L57SVLPddZ3MJwyqxRKRTCnKkpNfcuWOblHRfP6WMb_fIY/s790-rw-e365/ransomware.png)

Mallox is known to be propagated by brute-forcing Microsoft SQL servers and phishing emails to target Windows systems, with recent intrusions also making use of a .NET-based loader named PureCrypter.

"The attackers are using custom python scripts for the purpose of payload delivery and victim's information exfiltration," Uptycs researchers Tejaswini Sandapolla and Shilpesh Trivedi [said](https://www.uptycs.com/blog/mallox-ransomware-linux-variant-decryptor-discovered). "The malware encrypts user data and appends .locked extension to the encrypted files."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A decryptor has also been made available for [DoNex](https://thehackernews.com/2024/03/teamcity-flaw-leads-to-surge-in.html) and its predecessors (Muse, fake LockBit 3.0, and DarkRace) by Avast by taking advantage of a flaw in the cryptographic scheme. The Czech cybersecurity company [said](https://decoded.avast.io/threatresearch/decrypted-donex-ransomware-and-its-predecessors/) it has been "silently providing the decryptor" to victims since March 2024 in partnership with law enforcement organizations.

"Despite law enforcement efforts and increased security measures, ransomware groups continue to adapt and thrive," Group-IB said.

Data shared by [Malwarebytes](https://www.threatdown.com/blog/ransomware-review-june-2024-a-year-high-470-attacks-recorded/) and [NCC Group](https://www.nccgroup.com/us/newsroom/ncc-group-month...