---
title: USENIX NSDI ’24 – Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices
url: https://buaq.net/go-263292.html
source: unSafe.sh - 不安全
date: 2024-09-22
fetch_date: 2025-10-06T18:20:05.490408
---

# USENIX NSDI ’24 – Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices

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

![](https://8aqnet.cdn.bcebos.com/38a00690c77666a2f1f7b4c7ed312624.jpg)

USENIX NSDI ’24 – Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices

Saturday, September 21, 2024 Community Chats Webinars LibraryHomeCybersecurity New
*2024-9-21 23:0:0
Author: [securityboulevard.com(查看原文)](/jump-263292.htm)
阅读量:8
收藏*

---

Saturday, September 21, 2024

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

* [USENIX NSDI '24 - Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices](https://securityboulevard.com/2024/09/usenix-nsdi-24-autothrottle-a-practical-bi-level-approach-to-resource-management-for-slo-targeted-microservices/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "USENIX NSDI '24 - Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices")
* [Customer Story | Lanett City Schools Works Smarter With The Help Of Cloud Monitor](https://securityboulevard.com/2024/09/customer-story-lanett-city-schools-works-smarter-with-the-help-of-cloud-monitor/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "Customer Story | Lanett City Schools Works Smarter With The Help Of Cloud Monitor")
* [Building a RAG System on Databricks With Your Unstructured Data Using Tonic Textual](https://securityboulevard.com/2024/09/building-a-rag-system-on-databricks-with-your-unstructured-data-using-tonic-textual/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "Building a RAG System on Databricks With Your Unstructured Data Using Tonic Textual")
* [USENIX NSDI '24 - Revisiting Congestion Control for Lossless Ethernet](https://securityboulevard.com/2024/09/usenix-nsdi-24-revisiting-congestion-control-for-lossless-ethernet/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "USENIX NSDI '24 - Revisiting Congestion Control for Lossless Ethernet")
* [How Asset Discovery Tools Work](https://securityboulevard.com/2024/09/how-asset-discovery-tools-work/?utm_source=sbwebsite&utm_medium=marquee&utm_campaign=marquee "How Asset Discovery Tools Work")

[Home](https://securityboulevard.com/) » [Security Bloggers Network](https://securityboulevard.com/category/sbn/) » USENIX NSDI ’24 – Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices

![SBN](https://securityboulevard.com/wp-content/uploads/2017/09/SBNIcon4_512px.png)

Authors/Presenters:Zibo Wang, Pinghe Li, Chieh-Jan Mike Liang, Feng Wu, Francis Y. Yan
Awarded Outstanding Paper!

Our sincere thanks to **[USENIX](https://www.usenix.org/)**, and the Presenters & Authors for publishing their superb **21st USENIX Symposium on Networked Systems Design and Implementation (NSDI ’24)** content, placing the organizations enduring commitment to Open Access front and center. Originating from the conference’s events situated at the **[Hyatt Regency Santa Clara](https://www.hyatt.com/hyatt-regency/en-US/clara-hyatt-regency-santa-clara)**; and via the organizations **[YouTube](https://www.youtube.com/playlist?list=PLbRoZ5Rrl5ldyIkhu7rzerLnR6HOZTlP9)** channel.

[![Claroty](https://securityboulevard.com/wp-content/uploads/2024/07/OnDemand-2024.07.18-Claroty-LandingPage-1540x660-2.png)](https://webinars.techstronglearning.com/addressing-the-security-challenges-of-industrial-ot-and-iot?utm_source=Securityboulevard.com&utm_medium=Referral&utm_campaign=in-article-ad)

[Permalink](https://www.infosecurity.us/blog/2024/9/21/usenix-nsdi-24-autothrottle-a-practical-bi-level-approach-to-resource-management-for-slo-targeted-microservices)

\*\*\* This is a Security Bloggers Network syndicated blog from [Infosecurity.US](https://www.infosecurity.us/) authored by [Marc Handelman](https://securityboulevard.com/author/0/ "Read other posts by Marc Handelman"). Read the original post at: <https://www.youtube-nocookie.com/embed/FQXVrRYsW5M?si=ILNPmufBBigK1i9h>

* [← Customer Story | Lanett City Schools Works Smarter With The Help Of Cloud Monitor](https://securityboulevard.com/2024/09/customer-story-lanett-city-schools-works-smarter-with-the-h...