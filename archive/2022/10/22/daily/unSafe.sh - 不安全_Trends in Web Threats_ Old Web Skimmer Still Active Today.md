---
title: Trends in Web Threats: Old Web Skimmer Still Active Today
url: https://buaq.net/go-132041.html
source: unSafe.sh - 不安全
date: 2022-10-22
fetch_date: 2025-10-03T20:34:53.423634
---

# Trends in Web Threats: Old Web Skimmer Still Active Today

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

![](https://8aqnet.cdn.bcebos.com/22d8ad8274ce38ef886e9003a9272a0a.jpg)

Trends in Web Threats: Old Web Skimmer Still Active Today

Executive SummaryPalo Alto N
*2022-10-21 21:0:38
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-132041.htm)
阅读量:30
收藏*

---

![Web Threat Trends conceptual image](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/Trends-r3d3.png)

## Executive Summary

Palo Alto Networks Advanced URL Filtering subscription collects data regarding two types of URLs; landing URLs and host URLs. We define a malicious landing URL as one that provides an opportunity for a user to click a malicious link. A malicious host URL is a web page that contains a malicious code snippet that could abuse someone’s computing power, steal sensitive information or perform other types of attacks.

Between January 2022 and March 2022, Palo Alto Networks detected over 577,000 instances of landing URLs, of which 20% were unique URLs. We also detected over two million host URLs, of which about 9% were unique URLs. This analysis was done using our web threat detection modules, which is used in our cloud-delivered security services such as Advanced URL Filtering.

In this blog, we present our analysis and findings around the latest trends of web threats like host and landing URLs including; where they are hosted, what categories they belong to, and which malware families are more likely to pose a threat. We also take a look at other threats such as skimmer attacks, downloaders and cryptominers.

With the help of Palo Alto Networks [Advanced URL Filtering](https://www.paloaltonetworks.com/network-security/advanced-url-filtering) and [Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention) [cloud-delivered security services](https://www.paloaltonetworks.com/network-security/security-subscriptions), customers are protected from the threats discussed in this blog. Our web protection engine, Advanced URL Filtering, helps detect malicious URLs such as landing and host URLs. Our intrusion prevention system, Advanced Threat Prevention, applies added protection and helps prevent web threats like cryptomining and JavaScript downloading.

## Table of Contents

[Web Threats Landing URLs: Detection Analysis](#landing-urls-detection-analysis)

* [Time Analysis](#time-analysis-landing)
* [Geolocation Analysis](#geolocation-analysis-landing)
* [Category Analysis](#category-analysis-landing)

[Web Threats Malicious Host URLs: Detection Analysis](#host-urls-detection-analysis)

* [Time Analysis](#time-analysis-host)
* [Geolocation Analysis](#geolocation-analysis-host)
* [Malware Class Analysis](#malware-class-analysis-host)
* [Malware Family Analysis](#malware-family-analysis-host)

[Web Threats Case Study](#web-threats-case-study)

## Web Threats Landing URLs: Detection Analysis

Palo Alto Networks crawls and analyzes millions of URLs from different sources every day, including newly seen URLs in customer traffic and email links. We collected web threat related data from customers with our [Advanced](https://www.paloaltonetworks.com/network-security/advanced-url-filtering) [URL Filtering](https://www.paloaltonetworks.com/products/threat-detection-and-prevention/web-security) subscription, using special YARA signatures.

Between January 2022 and March 2022, we detected 577,275 incidents involving landing URLs containing all kinds of web threats, 116,643 of which were unique URLs. We discovered, when compared to the previous quarter, the total number of incidents involving landing URLs increased while the number of unique URLs decreased.

### Web Threats Landing URLs Detection: Time Analysis

As shown in Figure 1 and also mentioned in our blog, “[Web Threats: Malicious Host URLs, Landing URLs and Trends](https://unit42.paloaltonetworks.com/web-threats-malicious-host-urls/)”, we saw an increase in landing URLs in November 2021, and then began to see this number decline beginning in January through March 2022.

![Bar chart showing web threat trends. January-March 2022 on the X-axis, and 0-250,000 on the Y-axis. Key indicates blue bars are all hits, and red bars are unique hits. January 2022 = 216,621 total hits: 46,534 unique hits. February 2022 = 212,643 total hits: 31,825 unique hits. March 2022 = 148,011 total hits: 38,284 unique hits.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-4.png)

Figure 1. Web threats landing URLs distribution January-March 2022. (Blue bars indicate all detections, including repeated detections of the same URL, and red bars indicate detection of unique URLs).

### Web Threats Landing URLs: Geolocation Analysis

According to our analysis, the previously mentioned 116,643 malicious unique landing URLs came from 22,279 unique domains. After identifying the geographical locations of these domains, we found that the majority of them seem to originate from the United States, followed by Germany and Russia, which was also the case in the previous quarter. However, we recognized that attackers are leveraging proxy servers and VPNs located in those countries to hide their actual physical locations.

The choropleth map shown in Figure 2 shows the wide distribution of these domains across almost every continent, including Africa and Australia. Figure 3 shows the top eight countries where the owners of these domain names appeared to be located.

![Choropleth map showing the geolocation distribution of landing URLs from January-March 2022](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-23.png)

Figure 2. Web threats landing URLs’ domain geolocation distribution January-March 2022.

![Pie chart showing distribution of originating country of landing URLs from January-March 2022. United States - 62.2%, Germany - 3.9%, Russia - 3.0%, France - 1.6%, United Kingdom, Brazil, Netherlands - 1.3%, Canada - 1.1%, Others - 24.3%](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-5.png)

Figure 3. Top eight countries where web threat landing URLs’ domains originated from, between January 2022 and March 2022.

### Web Threats Landing URLs: Category Analysis

We analyzed landing URLs that were originally identified by our detection module as benign, to find common targets for cyberattackers, and where they might be trying to fool users. These landing URLs can potentially lead to people clicking on a malicious host URL. Going forward, all these landing URLs that lead to malicious code snippets will be marked as malicious by our Advanced URL FIltering service.

As shown in Figure 4, the top apparently benign targets are business and economy sites, followed by personal sites and blogs, and then shopping sites. Compared to last quarter, the top two categories flipped. Because attackers often try to trick users into clicking malicious links from seemingly benign sites, we strongly recommend that users exercise caution when visiting an unfamiliar website.

![Pie chart showing the top 10 categories hosting web threats from January-March 2022. Business and economy sites - 14.9%, personal sites and blogs - 9.1%, shopping - 7.8%, computer and internet - 7.5%, health and medicine - 5.5%, society - 4.8%, entertainment - 4.3%, web hosting - 3.6%, travel - 3.3%, parked - 2.9%, Others - 36.3%](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-6.png)

Figure 4. We divided landing URLs that originally appeared benign into categories. Here are the top 10 categories that hosted web threats January-March 2022.

## Web Threats Malicious Host URLs: Detection Analysis

With [Advanced](https://www.paloaltonetworks.co...