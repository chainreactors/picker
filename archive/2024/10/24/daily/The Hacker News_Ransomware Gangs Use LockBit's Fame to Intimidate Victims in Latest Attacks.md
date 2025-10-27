---
title: Ransomware Gangs Use LockBit's Fame to Intimidate Victims in Latest Attacks
url: https://thehackernews.com/2024/10/ransomware-gangs-use-lockbits-fame-to.html
source: The Hacker News
date: 2024-10-24
fetch_date: 2025-10-06T18:56:31.681242
---

# Ransomware Gangs Use LockBit's Fame to Intimidate Victims in Latest Attacks

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

# [Ransomware Gangs Use LockBit's Fame to Intimidate Victims in Latest Attacks](https://thehackernews.com/2024/10/ransomware-gangs-use-lockbits-fame-to.html)

**Oct 23, 2024**Ravie LakshmananRansomware / Cloud Security

[![Ransomware](data:image/png;base64... "Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_Ey1czMFb35WoYB85WsmA7xip2VvLVsQn6wyJqiyhMCBvrlBxDA4ZGYSs4CXrU2z_thKyboYx1rb0Ebrmy2gwM8A2Edt6J4_-4M4sprfEOh_EXaOKfFT8H-NSXYfwl9Nz2lElMQu2OOXmuYxWSzf0XeJt5LPaB2rUMXfsOhu9RnggkrARnFUbIvQT1Hpr/s790-rw-e365/lockbit.png)

Threat actors have been observed abusing Amazon S3 (Simple Storage Service) Transfer Acceleration feature as part of ransomware attacks designed to exfiltrate victim data and upload them to S3 buckets under their control.

"Attempts were made to disguise the Golang ransomware as the notorious LockBit ransomware," Trend Micro researchers Jaromir Horejsi and Nitesh Surana [said](https://www.trendmicro.com/en_us/research/24/j/fake-lockbit-real-damage-ransomware-samples-abuse-aws-s3-to-stea.html). "However, such is not the case, and the attacker only seems to be capitalizing on LockBit's notoriety to further tighten the noose on their victims."

The ransomware artifacts have been found to embed hard-coded Amazon Web Services (AWS) credentials to facilitate data exfiltration to the cloud, a sign that adversaries are increasingly weaponizing popular cloud service providers for malicious schemes.

The AWS account used in the campaign is presumed to be either their own or compromised. Following responsible disclosure to the AWS security team, the identified AWS access keys and accounts have been suspended.

Trend Micro said it detected more than 30 samples with the AWS Access Key IDs and the Secret Access Keys embedded, signaling active development. The ransomware is capable of targeting both Windows and macOS systems. Cybersecurity firm SentinelOne has given it the name [NotLockBit](https://www.sentinelone.com/blog/macos-notlockbit-evolving-ransomware-samples-suggest-a-threat-actor-sharpening-its-tools/).

It's not exactly known how the cross-platform ransomware is delivered to a target host, but once it's executed, it obtains the machine's universal unique identifier (UUID) and carries out a series of steps to generate the master key required for encrypting the files.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The initialization step is followed by the attacker enumerating the root directories and encrypting files matching a specified list of extensions, but not before exfiltrating them to AWS via S3 Transfer Acceleration ([S3TA](https://aws.amazon.com/s3/transfer-acceleration/)) for faster data transfer.

"After the encryption, the file is renamed according to the following format: <original file name>.<initialization vector>.abcd," the researchers said. "For instance, the file text.txt was renamed to text.txt.e5c331611dd7462f42a5e9776d2281d3.abcd."

In the final stage, the ransomware changes the device's wallpaper to display an image that mentions LockBit 2.0 in a likely attempt to compel victims into paying up.

"Threat actors might also disguise their ransomware sample as another more publicly known variant, and it is not difficult to see why: the infamy of high-profile ransomware attacks further pressures victims into doing the attacker's bidding," the researchers said.

The development comes as Gen Digital released a decryptor for a [Mallox](https://thehackernews.com/2024/05/ongoing-campaign-bombarded-enterprises.html) ransomware variant that was spotted in the wild from January 2023 through February 2024 by taking advantage of a flaw in the cryptographic schema.

[![Ransomware](data:image/png;base64... "Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYuQpbxkos8VdRZuiu0goYEZanXzAqV3SzFDAM6IzdP_aS1v2Lfm7SnBf101sINxLl61w5aP970xGaHBM1x9LDAyFALgj1KxWchURwpnEWZQJb1x5fuKSvx6mintpvSWS6Bv7fP7buDGWgbc5bUCVdZdwZXQPo-6kiCeZAkqIpyMnUKHvjXEP5Q0GV57M5/s790-rw-e365/golang-01.png)

"Victims of the ransomware may be able to restore their files for free if they were attacked by this particular Mallox variant," researcher Ladislav Zezula [said](https://www.gendigital.com/blog/news/innovation/decrypted-mallox-ransomware). "The crypto-flaw was fixed around March 2024, so it is no longer possible to decrypt data encrypted by the later versions of Mallox ransomware."

It should be mentioned that an affiliate of the Mallox operation, also known as TargetCompany, has been discovered using a slightly modified version of the Kryptina ransomware – codenamed Mallox v1.0 – to breach Linux systems.

"The Kryptina-derived variants of Mallox are affiliate-specific and separate from other Linux variants of Mallox that have since emerged, an indication of how the ransomware landscape has evolved into a complex menagerie of cross-pollinated toolsets and non-linear codebases," SentinelOne researcher Jim Walter [noted](https://www.sentinelone.com/labs/kryptina-raas-from-unsellable-cast-off-to-enterprise-ransomware/) late last month.

Ransomware [continues](https://www.security.com/threat-intelligence/ransomware-threat-level-remains-high) to be a major threat, with 1,255 attacks claimed in the third quarter of 2024, down from 1,325 in the previous quarter, according to Symantec's analysis of data pulled from ransomware leak sites.

Microsoft, in its Digital Defense Report for the one-year period from June 2023 to June 2024, [said](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2024) it observed a 2.75x increase year-over-year in human-operated ransomware-linked encounters, while the percentage of attacks reaching the actual encryption phase has decreased over the past two years by threefold.

Some of the major beneficiaries of LockBit's decline following an [international law enforcement operation](https://thehackernews.com/2024/10/lockbit-ransomware-and-evil-corp.html) targeting ...