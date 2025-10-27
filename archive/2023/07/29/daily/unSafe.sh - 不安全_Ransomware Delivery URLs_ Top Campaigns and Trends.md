---
title: Ransomware Delivery URLs: Top Campaigns and Trends
url: https://buaq.net/go-173162.html
source: unSafe.sh - 不安全
date: 2023-07-29
fetch_date: 2025-10-04T11:51:07.394756
---

# Ransomware Delivery URLs: Top Campaigns and Trends

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

![](https://8aqnet.cdn.bcebos.com/e3d8781e7afc8f41408a343c1ba84269.jpg)

Ransomware Delivery URLs: Top Campaigns and Trends

This post is also available i
*2023-7-28 21:0:53
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-173162.htm)
阅读量:32
收藏*

---

![A pictorial representation of ransomware, including ransomware delivered by URLs. The Palo Alto Networks and Unit 42 logos.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/Unit42-ransomware-21-illustration_yellow.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/url-delivered-ransomware/)

## **Executive Summary**

Threat actors seeking new ways to get their creations past victims’ defenses are increasingly turning to sending ransomware through URLs. They are also using increasingly dynamic behaviors to deliver their ransomware. In addition to treading the well-worn path of using polymorphic versions of their ransomware, threat actors often rotate hostnames, paths, filenames or a combination of all three to widely distribute ransomware.

We’ll show our findings on how threat actors are distributing ransomware via URLs, as well as discussing the following aspects of this data:

* How threat actors are abusing hosting providers and top level domains
* How threat actors are abusing public hosting, social media and sharing services
* How threat actors rotate hostnames, paths or filenames in URLs using several case studies

Palo Alto Networks Next-Generation Firewall customers with [Advanced URL Filtering](https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-new-features/url-filtering-features/advanced-url-filtering) and [DNS Security](https://docs.paloaltonetworks.com/dns-security) subscriptions are protected against malicious ransomware campaigns similar to the ones described in this article. All the mentioned ransomware samples are also covered by WildFire products.

| **Related Unit 42 Topics** | [**Ransomware**](https://unit42.paloaltonetworks.com/category/ransomware/), **[Web Hosting](https://unit42.paloaltonetworks.com/tag/web-hosting/)** |
| --- | --- |

## Table of Contents

[Prevalence of Web Browsing-Delivered Ransomware](#post-129339-_53q8dgendh8g)

## **Prevalence of Web Browsing-Delivered Ransomware**

### Delivery Protocol of Ransomware

The three most popular methods of delivery for ransomware are through URLs, emails and third-party apps. People encounter ransomware delivered by URLs when they browse a site themselves, or if malware or other software surreptitiously placed on a compromised system accesses it. Ransomware delivered through email arrives as an attachment in the email itself rather than a ransomware URL included in the body of an email.

In 2021, Unit 42 published an article [discussing trends in ransomware delivery methods](https://unit42.paloaltonetworks.com/ransomware-families/). At that time, email attachments (e.g., SMTP and POP3 protocols) were the most widely-used channel for distributing ransomware. More recently, our analysis of ransomware samples from the entire year of 2022 revealed a shift in the primary entry vector for ransomware infections (as shown in Figure 1). URL or web browsing has emerged as the leading method for ransomware delivery, accounting for over 77% of cases.

Ransomware delivery through emails has decreased in prevalence to be the second most popular method, comprising almost 12% of the total.

![Image 1 is a graph of the percentage of arrival protocols used to deliver ransomware in 2022. The largest percentage is through web browsing at 76.5%. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/chart.png)

Figure 1. Arrival protocols used to deliver ransomware in 2022.

Within the URLs that are used to deliver ransomware, we observed some notable trends including ransomware hosting URLs being used in various polymorphic forms to increase the agility of attacks. For example, threat actors have been observed both rotating *different URLs* to host the *same ransomware* (e.g., hxxp://oddsium[.]com/g76dbf and hxxp://clicktoevent[.]com/g76dbf?lrebib=kvqqhaohs) and using the *same URL* to deliver *different ransomware* (e.g., rgyui[.]top/dl/build.exe). We discuss various recent tactics in detail in the ransomware campaigns and case studies section below.

### Ransomware Family Distributions

We also observed a variety of different families in the traffic we captured with our URL-based ransomware detection service. Figure 2 shows the distribution of the URLs in the top 10 ransomware families we observed in the last quarter of 2022. Lazy and Virlock ransomware, which have been in circulation for years, made up over 50% of the ransomware we observed.

![Image 2 is a graph of the top 10 ransomware families by percentage detected. The largest percentage is Lazy at almost 40%.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/chart-1.png)

Figure 2. Top 10 ransomware families detected by the URL-based ransomware detection service in 2022.

## **Web Hosting Infrastructure**

Between October and December 2022, our Advanced URL Filtering and DNS Security services detected over 27,000 unique URLs and hostnames hosting ransomware. In this section, we analyze and provide insights into the hosting infrastructure of 7,000 random samples from these ransomware hosting URLs, which consist of 3,335 domains.

### Domain Distribution

As we analyzed the hosts of ransomware URLs, we were concerned to see that (as of the end of December 2022) more than 20% of the URLs we observed were still active days or weeks after our detectors flagged them. Most of these URLs are compromised websites, and have likely gone undetected by site owners.

Figure 3 shows the most commonly abused top-level domains (TLDs), where the count shows the number of second level domains (2LDs). Aside from the expected abuse of generic top-level domains (gTLDs) (e.g., .com, .net, .org, .xyz, .top and .mobi) due to them comprising the lion’s share of the domain market, it is noteworthy to observe that attackers also abused country code top-level domains (ccTLDs) including .ru, and .cn, possibly indicating that these countries have less strict policies in place for registration of domains.

![Image 3 is a graph of the top-level domains that are most commonly abused as ransomware hosts with .com first by a large margin. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/Ransomware-URLs-F3.png)

Figure 3. Most commonly abused TLDs for hosting ransomware.

### Abuse of Public Hosting, Social Media and Sharing Services

Threat actors often abuse, take advantage of or subvert legitimate products for malicious purposes. This does not necessarily imply a flaw or malicious quality to the legitimate product being abused.

Figure 4 shows the most commonly abused public hosting, social media and sharing services. Attackers usually [create subdomains](https://unit42.paloaltonetworks.com/detecting-malicious-subdomains/) or paths under these popular services to reach a wider audience and to stay under the radar. These URLs are likely to fall through the cracks of many existing URL blocking services due to the good reputation involved with these services.

![Image 4 is a graph of the most commonly abused public hosting, social media and sharing services. The largest percentage is the first social media service at over 1500 ransomware URLs. The second is a media sharing service, and the rest of the media sharing, file sharing, and hosting services are distributed more evenly.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/07/word-image-129339-4.png)

Figure 4. Most...