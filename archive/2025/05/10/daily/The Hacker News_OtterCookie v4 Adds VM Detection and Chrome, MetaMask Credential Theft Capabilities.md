---
title: OtterCookie v4 Adds VM Detection and Chrome, MetaMask Credential Theft Capabilities
url: https://thehackernews.com/2025/05/ottercookie-v4-adds-vm-detection-and.html
source: The Hacker News
date: 2025-05-10
fetch_date: 2025-10-06T22:31:38.178187
---

# OtterCookie v4 Adds VM Detection and Chrome, MetaMask Credential Theft Capabilities

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

# [OtterCookie v4 Adds VM Detection and Chrome, MetaMask Credential Theft Capabilities](https://thehackernews.com/2025/05/ottercookie-v4-adds-vm-detection-and.html)

**May 09, 2025**Ravie LakshmananMalware / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFnbBFETgOTBltmYR4p4Hz9Lu_2-lzDfvaza03-i3ZqF7I4tXdjUsdb-nkKPa0W5FP-rk4a9ZHiwXRuG50WHSnQp8nxDVCIgaHmo4hWO5Fay8eNutygWhbOC_TmvXplMUZ3hk7sb3mP6DxSnmgM3thiqzoSKoN-h4R_sY4Rp8Ohhc0Huiffzpaf6t8LUAq/s790-rw-e365/browser-malware.jpg)

The North Korean threat actors behind the **Contagious Interview** campaign have been observed using updated versions of a cross-platform malware called OtterCookie with capabilities to steal credentials from web browsers and other files.

NTT Security Holdings, which [detailed](https://jp.security.ntt/tech_blog/en-waterplum-ottercookie) the new findings, said the attackers have "actively and continuously" updated the malware, introducing versions v3 and v4 in February and April 2025, respectively.

The Japanese cybersecurity company is tracking the cluster under the name **WaterPlum**, which is also known as CL-STA-0240, DeceptiveDevelopment, DEV#POPPER, Famous Chollima, PurpleBravo, and Tenacious Pungsan.

OtterCookie was [first documented](https://thehackernews.com/2024/12/north-korean-hackers-deploy-ottercookie.html) by NTT last year after having observed it in attacks since September 2024. Delivered by means of a JavaScript payload via a malicious npm package, trojanized GitHub or Bitbucket repository, or a bogus videoconferencing app, it's designed to contact an external server to execute commands on compromised hosts.

OtterCookie v3 has been found to incorporate a new upload module to send files matching a predefined set of extensions to the external server. This consists of environment variables, images, documents, spreadsheets, text files, and files containing mnemonic and recovery phrases associated with cryptocurrency wallets.

It's worth pointing out that this module was previously executed in OtterCookie v2 as a shell command received from the server.

The fourth iteration of the malware expands on its predecessor by adding two more modules to steal credentials from Google Chrome, as well as extract data from the MetaMask extension for Google Chrome, Brave browser, and iCloud Keychain.

Another new feature addition to OtterCookie v4 is the ability to detect if it's being executed in virtual machine (VM) environments pertaining to Broadcom VMware, Oracle VirtualBox, Microsoft, and QEMU.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitPb3lVlA4H6uESOvthXKg_gbwJVJs0b-gaKBjLHLH0XKaDtrCMHTJKWh-luBas9Ma2a7QjEj9DjzUodKQctBPL6LIS4-ms96WyNK_4Zug9p2AyaILKO9atbsvl5DLLBv-hJtxX8wiDQXHgNKAyZZthITDPnLeadfAW0j3aC6GOxDO27NKomHGlQnZQKEv/s790-rw-e365/checks.png)

Interestingly, it has been found that the first stealer module responsible for gathering Google Chrome credentials does so after decrypting them, whereas the second module harvests encrypted login data from browsers like Chrome and Brave.

"This difference in data processing or coding style implies that these modules were developed by different developers," researchers Masaya Motoda and Rintaro Koike said.

The disclosure comes as multiple malicious payloads related to the Contagious Interview campaign have been unearthed in recent months, indicating that the threat actors are refining their modus operandi.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This includes a Go-based information stealer that's delivered under the guise of a Realtek driver update ("WebCam.zip") that, when opened, runs a shell script responsible for downloading the stealer and launching a deceptive macOS application ("DriverMinUpdate.app") engineered to harvest the victim's macOS system password.

It's believed that the malware was distributed as part of an updated version of the activity codenamed [ClickFake Interview](https://thehackernews.com/2025/04/lazarus-group-targets-job-seekers-with.html) by Sekoia last month owing to the use of ClickFix-style lures to fix non-existent audio and video issues during an online assessment for a job interview process.

"The stealer's primary role is to establish a persistent C2 channel, profile the infected system, and exfiltrate sensitive data," MacPaw's cybersecurity division, Moonlock, [said](https://moonlock.com/realtek-macos-malware). "It achieves this through a combination of system reconnaissance, credential theft, and remote command execution."

It's assessed that the application DriverMinUpdate is part of a [larger](https://thehackernews.com/2025/02/north-korean-hackers-deploy-ferret.html) [set](https://www.kandji.io/blog/drivereasy) of [similar](https://hackernoon.com/cybercrooks-are-using-fake-job-listings-to-steal-crypto) [malicious apps](https://www.enki.co.kr/media-center/blog/analysis-of-variants-in-lazarus-s-contagious-interview-campaign) that have been uncovered by dmpdump, SentinelOne, ENKI, and Kandji such as ChromeUpdateAlert, ChromeUpdate, CameraAccess, and DriverEasy.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQ7JRkuiXn1AnuZrMu3eXjABFImdw_hyphenhyphend7D1utHLAH2DsAFpwyKNQWrf9hZlzpZoJG0H16bswCv4_dFjI5xMVcCaTj3joFymVVf_rQO52Iz7GiaKs-DcPBwyOqtBTTue-U4AgT19ebPBH-raJHB2k1lWnl3k-7VPblVDiMn5yqHWpNOqfCg499pzz6LH-8/s790-rw-e365/flow.jpg)

A second new malware family connected to the campaign is Tsunami-Framework, which is delivered as a follow-up payload to a known Python backdoor referred to as [InvisibleFerret](https://thehackernews.com/2025/04/north-korean-hackers-spread-malware-via.html). A .NET-based modular malware, it's equipped to steal a wide range of data from web browsers and cryptocurrency wallets.

It also incorporates features to log keystrokes, collect files, and even a botnet component that appears to be under early development, German security company Hi...