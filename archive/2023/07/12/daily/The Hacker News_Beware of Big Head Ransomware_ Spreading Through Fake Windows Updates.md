---
title: Beware of Big Head Ransomware: Spreading Through Fake Windows Updates
url: https://thehackernews.com/2023/07/beware-of-big-head-ransomware-spreading.html
source: The Hacker News
date: 2023-07-12
fetch_date: 2025-10-04T11:58:22.445506
---

# Beware of Big Head Ransomware: Spreading Through Fake Windows Updates

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

# [Beware of Big Head Ransomware: Spreading Through Fake Windows Updates](https://thehackernews.com/2023/07/beware-of-big-head-ransomware-spreading.html)

**Jul 11, 2023**Ravie LakshmananRansomware / Windows Security

[![Fake Windows Updates](data:image/png;base64... "Fake Windows Updates")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAy9xl8FNZ77PjfrwZDRYOufNQrDK68wLPoKSMNZjySLmfbjDX0P2JuLgU8R5KCbG1LtRfSWNPfen6V90RaeefDtjM9scSrU9NnpdazrnWI8UsRRKqLFmZdwqH8N2fMv3D63pHQNB8RFS_QIMp9bhl7tPZTdUPjMkIrg-CYp1gDqgqKdiX63pezaCo5h-_/s790-rw-e365/windows-update.jpg)

A developing piece of ransomware called **Big Head** is being distributed as part of a malvertising campaign that takes the form of bogus Microsoft Windows updates and Word installers.

Big Head was [first documented](https://thehackernews.com/2023/06/8base-ransomware-spikes-in-activity.html) by Fortinet FortiGuard Labs last month, when it discovered multiple variants of the ransomware that are designed to encrypt files on victims' machines in exchange for a cryptocurrency payment.

"One Big Head ransomware variant displays a fake Windows Update, potentially indicating that the ransomware was also distributed as a fake Windows Update," Fortinet researchers said at the time. "One of the variants has a Microsoft Word icon and was likely distributed as counterfeit software."

A majority of the Big Head samples have been submitted so far from the U.S., Spain, France, and Turkey.

In a new analysis of the .NET-based ransomware, Trend Micro detailed its inner workings, calling out its ability to deploy three encrypted binaries: 1.exe to propagate the malware, archive.exe to facilitate communications over Telegram, and Xarch.exe to encrypt the files and display a fake Windows update.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The malware displays a fake Windows Update UI to deceive the victim into thinking that the malicious activity is a legitimate software update process, with the percentage of progress in increments of 100 seconds," the cybersecurity company [said](https://www.trendmicro.com/en_us/research/23/g/tailing-big-head-ransomware-variants-tactics-and-impact.html).

Big Head is no different from other ransomware families in that it deletes backups, terminates several processes, and performs checks to determine if it's running within a virtualized environment before proceeding to encrypt the files.

In addition, the malware disables the Task Manager to prevent users from terminating or investigating its process and aborts itself if the machine's language matches that of Russian, Belarusian, Ukrainian, Kazakh, Kyrgyz, Armenian, Georgian, Tatar, and Uzbek. It also incorporates a self-delete function to erase its presence.

[![Big Head Ransomware](data:image/png;base64... "Big Head Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWArncxYzqmdiY338MAo7kVbnYvDPyfY_dGV_fVQDkilU6Cxe6JVjYUbomvi5YsYDyTPS8GalO_Tx9Y4UZvx1Og5VkAy1vnbdwwxww7MC-EZqgAsoQIPJhQc6foDGfnvOVIWdp8AW0trCdOXEMG6pL2OCZ9cXYf6Rxq9qUjm79l_yJjvj-Cfy4atz6gyNS/s790-rw-e365/big-head-ransomware.jpg)

Trend Micro said it detected a second Big Head artifact with both ransomware and stealer behaviors, the latter of which leverages the open-source [WorldWind Stealer](https://github.com/Leecher21/WorldWind-Stealer) to harvest web browser history, directory lists, running processes, product keys, and network information.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also discovered is a third variant of Big Head that incorporates a file infector called [Neshta](https://thehackernews.com/2023/03/new-fixs-atm-malware-targeting-mexican.html), which is used to insert malicious code into executables on the infected host.

"Incorporating Neshta into the ransomware deployment can also serve as a camouflage technique for the final Big Head ransomware payload," Trend Micro researchers said.

"This technique can make the piece of malware appear as a different type of threat, such as a virus, which can divert the prioritization of security solutions that primarily focus on detecting ransomware."

The identity of the threat actor behind Big Head is currently not known, but Trend Micro said it identified a YouTube channel with the name "aplikasi premium cuma cuma," suggesting an adversary likely of Indonesian origin.

"Security teams should remain prepared given the malware's diverse functionalities," the researchers concluded. "This multifaceted nature gives the malware the potential to cause significant harm once fully operational, making it more challenging to defend systems against, as each attack vector requires separate attention."

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Malware](https://thehackernews.com/search/label/Malware)[Microsoft](https://thehackernews.com/search/label/Microsoft)[ransomware](https://thehackernews.com/search/label/ransomware)[Trend Micro](https://thehackernews.com/search/label/Trend%20Micro)

[![c](data:image/svg+xml;base64...)](ht...