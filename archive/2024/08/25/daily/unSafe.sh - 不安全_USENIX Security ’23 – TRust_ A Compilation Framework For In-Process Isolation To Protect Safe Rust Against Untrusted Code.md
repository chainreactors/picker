---
title: USENIX Security ’23 – TRust: A Compilation Framework For In-Process Isolation To Protect Safe Rust Against Untrusted Code
url: https://buaq.net/go-258020.html
source: unSafe.sh - 不安全
date: 2024-08-25
fetch_date: 2025-10-06T18:01:55.439645
---

# USENIX Security ’23 – TRust: A Compilation Framework For In-Process Isolation To Protect Safe Rust Against Untrusted Code

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/01c525a2447acfd4b48597ce993777bb.jpg)

USENIX Security ’23 – TRust: A Compilation Framework For In-Process Isolation To Protect Safe Rust Against Untrusted Code

Saturday, August 24, 2024 Community Chats Webinars LibraryHomeCybersecurity NewsFe
*2024-8-24 23:0:0
Author: [securityboulevard.com(查看原文)](/jump-258020.htm)
阅读量:4
收藏*

---

Saturday, August 24, 2024

[## ![Security Boulevard Logo](https://securityboulevard.com/wp-content/themes/colormag-pro/img/security-boulevard-tsg-logo.png)](https://securityboulevard.com/ "Security Boulevard")

Community Chats Webinars Library

* [Home](https://securityboulevard.com)
  + [Cybersecurity News](https://securityboulevard.com/cybersecurity-news/)
  + [Features](https://securityboulevard.com/features/)
  + [Industry Spotlight](https://securityboulevard.com/industry-spotlight/)
  + [News Releases](https://securityboulevard.com/news-releases/)
* [Security Creators Network](https://securityboulevard.com/security-creators-network/)
  + [Latest Posts](https://securityboulevard.com/security-creators-network/)
  + [Syndicate Your Blog](https://securityboulevard.com/boulevard-feed-request/)
  + [Write for Security Boulevard](https://securityboulevard.com/write-for-security-boulevard/)
* Webinars
  + [Upcoming Webinars](https://securityboulevard.com/webinars/)
  + [Calendar View](https://securityboulevard.com/webinars/month/)
  + [On-Demand Webinars](https://securityboulevard.com/on-demand-webinars/)
* Events
  + [Upcoming Events](https://www.mediaopsevents.com/virtual/upcoming)
  + [On-Demand Events](https://www.mediaopsevents.com/virtual/843942)
* [Sponsored Content](https://securityboulevard.com/category/sponsored-content/)
* [Chat](https://securityboulevard.com/chats/)
  + [Security Boulevard Chat](https://securityboulevard.com/chats/)
  + [Marketing InSecurity Podcast](https://securityboulevard.com/marketing-insecurity-podcasts/)
  + [Techstrong.tv Podcast](https://www.techstrongpodcasts.com)
  + [TechstrongTV - Twitch](https://www.twitch.tv/techstrongtv)
* [Library](https://securityboulevard.com/library/)
* Related Sites
  + [Techstrong Group](https://techstronggroup.com)
  + [Cloud Native Now](https://cloudnativenow.com/)
  + [DevOps.com](https://devops.com)
  + [Security Boulevard](https://securityboulevard.com/)
  + [Techstrong Research](https://techstrongresearch.com/)
  + [Techstrong TV](https://techstrong.tv/)
  + [Techstrong.tv Podcast](https://www.techstrongpodcasts.com)
  + [Techstrong.tv - Twitch](https://www.twitch.tv/techstrongtv)
  + [Devops Chat](https://soundcloud.com/devopschat)
  + [DevOps Dozen](https://devopsdozen.com/)
  + [DevOps TV](https://www.youtube.com/channel/UC-zcE077X98oTEDPwKkDQxQ)
* [Media Kit](https://techstronggroup.com/assets/techstrong-media-kit.pdf)
* [About](https://securityboulevard.com/about/)
* [Sponsor](https://techstronggroup.com/tellmemore/)

* [Analytics](https://securityboulevard.com/security-analytics/)
* [AppSec](https://securityboulevard.com/application-security/)
* [CISO](https://securityboulevard.com/ciso-suite)
* [Cloud](https://securityboulevard.com/cloud-security/)
* [DevOps](https://securityboulevard.com/devops/)
* [GRC](https://securityboulevard.com/governance-risk-compliance)
* [Identity](https://securityboulevard.com/identity-management)
* [Incident Response](https://securityboulevard.com/incident-response/)
* [IoT / ICS](https://securityboulevard.com/iot-ics-security/)
* [Threats / Breaches](https://securityboulevard.com/threats-breaches/)
* [More](https://securityboulevard.com)
  + [Blockchain / Digital Currencies](https://securityboulevard.com/blockchain-digital-currency-bitcoin/)
  + [Careers](https://securityboulevard.com/careers)
  + [Cyberlaw](https://securityboulevard.com/cyberlaw)
  + [Mobile](https://securityboulevard.com/mobile-security)
  + [Social Engineering](https://securityboulevard.com/social-engineering)
* [Humor](https://securityboulevard.com/humor)

Hot Topics

* [USENIX Security ’23 - TRust: A Compilation Framework For In-Process Isolation To Protect Safe Rust Against Untrusted Code](https://securityboulevard.com/2024/08/usenix-security-23-trust-a-compilation-framework-for-in-process-isolation-to-protect-safe-rust-against-untrusted-code/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "USENIX Security ’23 - TRust: A Compilation Framework For In-Process Isolation To Protect Safe Rust Against Untrusted Code")
* [Enhancing School Safety with Cloud Monitor: A Powerful Cyber Safety Protection Tool](https://securityboulevard.com/2024/08/enhancing-school-safety-with-cloud-monitor-a-powerful-cyber-safety-protection-tool/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "Enhancing School Safety with Cloud Monitor: A Powerful Cyber Safety Protection Tool")
* [Audit: FBI is Losing Track of Storage Devices Holding Sensitive Data](https://securityboulevard.com/2024/08/audit-fbi-is-losing-track-of-storage-devices-holding-sensitive-data/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "Audit: FBI is Losing Track of Storage Devices Holding Sensitive Data")
* [USENIX Security ’23 - That Person Moves Like A Car: Misclassification Attack Detection For Autonomous Systems Using Spatiotemporal Consistency](https://securityboulevard.com/2024/08/usenix-security-23-that-person-moves-like-a-car-misclassification-attack-detection-for-autonomous-systems-using-spatiotemporal-consistency/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "USENIX Security ’23 - That Person Moves Like A Car: Misclassification Attack Detection For Autonomous Systems Using Spatiotemporal Consistency")
* [Response to CISA Advisory (AA24-234A): Strengthening Defenses Through Effective Event Logging and Threat Detection](https://securityboulevard.com/2024/08/response-to-cisa-advisory-aa24-234a-strengthening-defenses-through-effective-event-logging-and-threat-detection/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "Response to CISA Advisory (AA24-234A):  Strengthening Defenses Through Effective Event Logging and Threat Detection")

[Home](https://securityboulevard.com/) » [Security Bloggers Network](https://securityboulevard.com/category/sbn/) » USENIX Security ’23 – TRust: A Compilation Framework For In-Process Isolation To Protect Safe Rust Against Untrusted Code

![SBN](https://securityboulevard.com/wp-content/uploads/2017/09/SBNIcon4_512px.png)

Authors/Presenters:Inyoung Bang and Martin Kayondo, Seoul National University; Hyungon Moon, UNIST (Ulsan National Institute of Science and Technology); Yunheung Paek, Seoul National University

Many thanks to **[USENIX](https://www.usenix.org/)** for publishing their outstanding **USENIX Security ’23 Presenter’s** content, and the organizations strong commitment to Open Access. Originating from the conference’s events situated at the **[Anaheim Marriott](https://www.marriott.com/en-us/hotels/laxah-anaheim-marriott/overview/)**; and via the organizations **[YouTube](https://www.usenix.org/conference/usenixsecurity23)** channel.

[Permalink](https://www.infosecurity.us/blog/2024/8/24/usenix-security-23-trust-a-compilation-framework-for-in-process-isolation-to-protect-safe-rust-against-untrusted-code)

[![Claroty](https://securityboulevard.com/wp-content/uploads/2024/07/OnDemand-2024.07.18-Claroty-LandingPage-1540x660-2.png)](https://webinars.techstronglearning.com/addressing-the-security-challenges-of-industrial-ot-and-iot?utm_source=Securityboulevard.com&utm_medium=Referral&utm_campaign=in-article-ad)

\*\*\* This is a Security Bloggers Network syndicated blog from [Infosecurity.US](https://www.infosec...