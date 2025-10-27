---
title: Microsoft Reveals Tactics Used by 4 Ransomware Families Targeting macOS
url: https://thehackernews.com/2023/01/microsoft-reveals-tactics-used-by-4.html
source: The Hacker News
date: 2023-01-07
fetch_date: 2025-10-04T03:17:48.079103
---

# Microsoft Reveals Tactics Used by 4 Ransomware Families Targeting macOS

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

# [Microsoft Reveals Tactics Used by 4 Ransomware Families Targeting macOS](https://thehackernews.com/2023/01/microsoft-reveals-tactics-used-by-4.html)

**Jan 06, 2023**Ravie LakshmananEndpoint Security / Cyber Threat

[![Ransomware Families Targeting macOS](data:image/png;base64... "Ransomware Families Targeting macOS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwzY5wYOtex7m1LscJNKZMs4dgSExc-a0kdvxoAsRZFF8dOmPHiMqZ5rz-cZZqnWPlRwiom5yJRgo20b2f_SXyrx5aN_OcJdAGNFzm6cYN5xfBdzEpLQQkSlvO5Xyl2b7JIbfglvOZRmCv-8KUru025NGvhHgPzKKIlKQtxbBiDu7SxrGyL-8cx-9H/s790-rw-e365/ransomware-macs.png)

Microsoft has shed light on four different ransomware families – [KeRanger](https://unit42.paloaltonetworks.com/new-os-x-ransomware-keranger-infected-transmission-bittorrent-client-installer/), FileCoder, MacRansom, and EvilQuest – that are known to impact Apple macOS systems.

"While these malware families are old, they exemplify the range of capabilities and malicious behavior possible on the platform," the tech giant's Security Threat Intelligence team [said](https://www.microsoft.com/en-us/security/blog/2023/01/05/unraveling-the-techniques-of-mac-ransomware/) in a Thursday report.

The initial vector for these ransomware families involves what the Windows maker calls "user-assisted methods," wherein the victim downloads and installs trojanized applications.

Alternatively, it can also arrive as a second-stage payload that's dropped by an already existing malware on the infected host or as part of a supply chain attack.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Irrespective of the modus operandi employed, the attacks proceed along similar lines, with the threat actors relying on legitimate operating system features and exploiting vulnerabilities to break into the systems and encrypt files of interest.

This includes the use of the Unix find utility as well as library functions like opendir, readdir, and closedir to enumerate files. Another method touched on by Microsoft, but not adopted by the ransomware strains, entails the [NSFileManager](https://developer.apple.com/documentation/foundation/nsfilemanager) Objective-C interface.

KeRanger, MacRansom, and EvilQuest have also been observed to utilize a combination of hardware- and software-based checks to determine if the malware is running in a virtual environment in an attempt to resist analysis and debugging attempts.

[![Ransomware Families Targeting macOS Systems](data:image/png;base64... "Ransomware Families Targeting macOS Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf_u5QSzOqQFI1Np5QS14lDRsuzmVPxS6zqkAesGs8QiLBKwU_Hovf340oWigUBB3HmhZqBE40ILW_nQ2VjiH0uLnvXa_pz9-ZgVKy_bGvNf5h5FP7Hpq0Jp93X49j0JPR3zN3XX1CT64QmCxzOnYwzPCaR7N065V0079y42cn9OqTG96uGi_9bB0d/s790-rw-e365/key.png)

KeRanger, notably, employs a technique known as delayed execution to escape detection. It achieves this by sleeping for three days upon its launch before kick-starting its malicious functions.

Persistence, which is essential to ensuring that the malware is run even after a system restart, is established by means of [launch agents](https://attack.mitre.org/techniques/T1543/001/) and [kernel queues](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/KernelQueues/KernelQueues.html), Microsoft pointed out.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

While FileCoder uses the ZIP utility to encrypt files, KeRanger uses [AES encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in cipher block chaining ([CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC))) mode to achieve its goals. Both MacRansom and EvilQuest, on the other hand, leverage a [symmetric encryption](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) algorithm.

EvilQuest, which was [first exposed](https://thehackernews.com/2020/07/macos-ransomware-attack.html) in July 2020, further goes beyond typical ransomware to incorporate other trojan-like features, such as keylogging, compromising Mach-O files by injecting arbitrary code, and disabling security software.

It also packs in capabilities to execute any file directly from memory, effectively leaving no trace of the payload on disk.

"Ransomware continues to be one of the most prevalent and impactful threats affecting organizations, with attackers constantly evolving their techniques and expanding their tradecraft to cast a wider net of potential targets," Microsoft said.

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

[Malware](https://thehackernews.com/search/label/Malware)[Microsoft](https://thehackernews.com/search/label/Microsoft)[ransomware](https://thehackernews.com/search/label/ransomware)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Fla...