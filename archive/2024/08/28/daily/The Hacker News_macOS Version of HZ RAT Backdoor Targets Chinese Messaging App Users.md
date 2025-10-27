---
title: macOS Version of HZ RAT Backdoor Targets Chinese Messaging App Users
url: https://thehackernews.com/2024/08/macos-version-of-hz-rat-backdoor.html
source: The Hacker News
date: 2024-08-28
fetch_date: 2025-10-06T18:09:23.891836
---

# macOS Version of HZ RAT Backdoor Targets Chinese Messaging App Users

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

# [macOS Version of HZ RAT Backdoor Targets Chinese Messaging App Users](https://thehackernews.com/2024/08/macos-version-of-hz-rat-backdoor.html)

**Aug 27, 2024**Ravie LakshmananCyber Espionage / Malware

[![Chinese Messaging App Users](data:image/png;base64... "Chinese Messaging App Users")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKmMX999zXB84oRNczWEK4W8VodaujsXWikVA1avU_osbjwleTfC79P6nFmxp3rUPGQk3ZKNCc93KRO_m8cO5yTfCeksQxNdWJl5__OqjppwavG_7bYX0ZgAihKpCd3nJ5SApPf490exk3_j6suXuci9htjITCz2GYWVtZz6GZgsBwIOWMYERIQ_zvB9W7/s790-rw-e365/chinese-hacker.png)

Users of Chinese instant messaging apps like DingTalk and WeChat are the target of an Apple macOS version of a backdoor named **HZ RAT**.

The artifacts "almost exactly replicate the functionality of the Windows version of the backdoor and differ only in the payload, which is received in the form of shell scripts from the attackers' server," Kaspersky researcher Sergey Puzan [said](https://securelist.com/hz-rat-attacks-wechat-and-dingtalk/113513/).

HZ RAT was [first documented](https://medium.com/%40DCSO_CyTec/hz-rat-goes-china-506854c5f2e2) by German cybersecurity company DCSO in November 2022, with the malware distributed via self-extracting zip archives or malicious RTF documents presumably built using the [Royal Road RTF weaponizer](https://thehackernews.com/2022/09/chinese-espionage-hackers-target.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack chains involving RTF documents are engineered to deploy the Windows version of the malware that's executed on the compromised host by exploiting a years-old Microsoft Office flaw in the Equation Editor ([CVE-2017-11882](https://thehackernews.com/2023/12/hackers-exploiting-old-ms-excel.html)).

The second distribution method, on the other hand, masquerades as an installer for legitimate software such as OpenVPN, PuTTYgen, or EasyConnect that, in addition to actually installing the lure program, also executes a Visual Basic Script (VBS) responsible for launching the RAT.

The capabilities of HZ RAT are fairly simple in that it connects to a command-and-control (C2) server to receive further instructions. This includes executing PowerShell commands and scripts, writing arbitrary files to the system, uploading files to the server, and sending heartbeat information.

Given the limited functionality of the tool, it's suspected that the malware is primarily used for credential harvesting and system reconnaissance activities.

Evidence shows that the first iterations of the malware have been detected in the wild as far back as June 2020. The campaign itself, per DCSO, is believed to be active since at least October 2020.

[![Chinese Messaging App Users](data:image/png;base64... "Chinese Messaging App Users")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyOraIVQWaTD-NrmfVAq_So4H8GGW4YnWSBUTNZqlWAqOVQ3WonTP9L-1iILRJwEumj5fXg1cz64roHhziYgYE_J5Kf1weWVmCUUEpac-P5bs13tC_hoZQeYJ6ri9tyIwIBzvmx1QlE7Ij-nWakhleQiZinyHyk7pHI1jBoBCLMZ_O5aTsSccNJ4aeBvn8/s790-rw-e365/code.png)

The latest sample uncovered by Kaspersky, uploaded to VirusTotal in July 2023, impersonates OpenVPN Connect ("OpenVPNConnect.pkg"), which, upon starting, establishes contact with a C2 server specified in the backdoor to run four basic commands that are similar to that of its Windows counterpart -

* Execute shell commands (e.g., system information, local IP address, list of installed apps, data from DingTalk, Google Password Manager, and WeChat)
* Write a file to disk
* Send a file to the C2 server
* Check a victim's availability

"The malware attempts to obtain the victim's WeChatID, email, and phone number from WeChat," Puzan said. "As for DingTalk, attackers are interested in more detailed victim data: Name of the organization and department where the user works, username, corporate email address, [and] phone number."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Further analysis of the attack infrastructure has revealed that almost all of the C2 servers are located in China barring two, which are based in the U.S. and the Netherlands.

On top of that, the ZIP archive containing the macOS installation package ("OpenVPNConnect.zip") is said to have been previously downloaded from a domain belonging to a Chinese video game developer named miHoYo, which is known for Genshin Impact and Honkai.

It's currently not clear how the file was uploaded to the domain in question ("vpn.mihoyo[.]com") and if the server was compromised at some point in the past. It's also undetermined how widespread the campaign is, but the fact that the backdoor is being put to use even after all these years points to some degree of success.

"The macOS version of HZ Rat we found shows that the threat actors behind the previous attacks are still active," Puzan said. "During the investigation, the malware was only collecting user data, but it could later be used to move laterally across the victim's network, as suggested by the presence of private IP addresses in some samples."

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

[apple security](https://thehackernews.com/...