---
title: Chinese Hackers Abuse IPv6 SLAAC for AitM Attacks via Spellbinder Lateral Movement Tool
url: https://thehackernews.com/2025/04/chinese-hackers-abuse-ipv6-slaac-for.html
source: The Hacker News
date: 2025-05-01
fetch_date: 2025-10-06T22:35:57.557790
---

# Chinese Hackers Abuse IPv6 SLAAC for AitM Attacks via Spellbinder Lateral Movement Tool

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

# [Chinese Hackers Abuse IPv6 SLAAC for AitM Attacks via Spellbinder Lateral Movement Tool](https://thehackernews.com/2025/04/chinese-hackers-abuse-ipv6-slaac-for.html)

**Apr 30, 2025**Ravie LakshmananMalware / DNS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjf76PFQ8Axip_h0Puv87YoqBEouMzmgLj5ZsIZMQGsRIf3lrWq2C_jJFboq0zZAXSAv96EjjUMMqH8LOkQhCVIsvWYNf9FccPBV9C7aSPzEUBjhauLnQrMq0wm6L85lPCHtf3qrLtozRglv7cwzITlhl-uCItq9Huur400iwG0RcO-_H7-1QQDPXHXiFBe/s790-rw-e365/cc-eset.jpg)

A China-aligned advanced persistent threat (APT) group called **TheWizards** has been linked to a lateral movement tool called Spellbinder that can facilitate adversary-in-the-middle (AitM) attacks.

"Spellbinder enables adversary-in-the-middle (AitM) attacks, through IPv6 stateless address autoconfiguration ([SLAAC](https://datatracker.ietf.org/doc/html/rfc4862)) [spoofing](https://www.juniper.net/documentation/us/en/software/junos/security-services/topics/topic-map/ipv6-neighbor-discovery-securing.html), to move laterally in the compromised network, intercepting packets and redirecting the traffic of legitimate Chinese software so that it downloads malicious updates from a server controlled by the attackers," ESET researcher Facundo Muñoz [said](https://www.welivesecurity.com/en/eset-research/thewizards-apt-group-slaac-spoofing-adversary-in-the-middle-attacks/) in a report shared with The Hacker News.

The attack paves the way for a malicious downloader that's delivered by hijacking the software update mechanism associated with Sogou Pinyin. The downloader then acts as a conduit to drop a modular backdoor codenamed WizardNet.

This is not the first time Chinese threat actors have abused Sogou Pinyin's software update process to deliver their own malware. In January 2024, ESET detailed a hacking group referred to as [Blackwood](https://thehackernews.com/2024/01/china-backed-hackers-hijack-software.html) that has deployed an implant named NSPX30 by taking advantage of the update mechanism of the Chinese input method software application.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Then earlier this year, the Slovak cybersecurity company revealed another threat cluster known as [PlushDaemon](https://thehackernews.com/2025/01/plushdaemon-apt-targets-south-korean.html) that leveraged the same technique to distribute a custom downloader called LittleDaemon.

TheWizards APT is known to target both individuals and the gambling sectors in Cambodia, Hong Kong, Mainland China, the Philippines, and the United Arab Emirates.

Evidence suggests that the Spellbinder IPv6 AitM tool has been put to use by the threat actor since at least 2022. While the exact initial access vector used in the attacks is unknown at this stage, successful access is followed by the delivery of a ZIP archive that contains four different files: AVGApplicationFrameHost.exe, wsc.dll, log.dat, and winpcap.exe.

The threat actors then proceed to install "winpcap.exe" and run "AVGApplicationFrameHost.exe," the latter of which is abused to sideload the DLL. The DLL file subsequently reads shellcode from "log.dat" and executes it in memory, causing Spellbinder to be launched in the process.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjW9Zd8uvzCjjbJoVHFt7_y1l4H_-4KRKZ64CHnhRy_fkWR9uBZ4PHbD8LioBFqIonVP8-6Y8s4lEj1XCRYtTp8SN9HqHWic3iYv0vKZXGNtCdfuJEO8AfKPDEsyesMvJdW6l6G2B8WEYBoTF80PKcTn_BjLNIMd_2ATBt_j-DoItXInpfXSgEQ-KOhF5nK/s790-rw-e365/icmp.png)

"Spellbinder uses the [WinPcap library](https://www.winpcap.org) to capture packets and to reply to packets when needed," Muñoz explained. "It takes advantage of IPv6's Network Discovery Protocol in which ICMPv6 Router Advertisement (RA) messages advertise that an IPv6-capable router is present in the network so that hosts that support IPv6, or are soliciting an IPv6-capable router, can adopt the advertising device as their default gateway."

In one attack case observed in 2024, the threat actors are said to have utilized this method to hijack the software update process for Tencent QQ at the DNS level to serve a trojanized version that then deploys WizardNet, a modular backdoor that's equipped to receive and run .NET payloads on the infected host.

Spellbinder pulls this off by intercepting the DNS query for the software update domain ("update.browser.qq[.]com") and issuing a DNS response with the IP address of an attacker-controlled server ("43.155.62[.]54") hosting the malicious update.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Specifically, it implements its own parser to find packets to process and if a DNS query is found, it checks whether the domain name from the query is present on a hard-coded list of subdomains. The list of targeted domains belong to several popular Chinese platforms, such as Tencent, Baidu, Xunlei, Youku, iQIYI, Kingsoft, Mango TV, Funshion, Yuodao, Xiaomi and Xioami's Miui, PPLive, Meitu, Quihoo 360, and Baofeng.

Another noteworthy tool in TheWizards' arsenal is DarkNights, which is also called DarkNimbus by Trend Micro and has been attributed to another [Chinese hacking group](https://thehackernews.com/2024/12/hackers-target-uyghurs-and-tibetans.html) tracked as [Earth Minotaur](https://thehackernews.com/2025/04/spynote-badbazaar-moonshine-malware.html). That said, both clusters are being treated as independent operators, citing differences in tooling, infrastructure, and targeting footprints.

It has since [emerged](https://www.intelligenceonline.com/surveillance--interception/2025/01/29/chinese-firm-behind-hacking-operations-against-uyghurs-and-tibetans-unveiled%2C110368855-evg) that a Chinese public security ministry contractor named Sichuan Dianke Network Security Technology Co., Ltd. (aka UPSEC) is the supplier of the DarkNimbus malware.

"While TheWizards uses a different backdoor for Windows (WizardNet), the hijacking s...