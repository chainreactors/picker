---
title: Trends in Web Threats in CY Q2 2022: Malicious JavaScript Downloaders Are Evolving
url: https://buaq.net/go-132766.html
source: unSafe.sh - 不安全
date: 2022-10-27
fetch_date: 2025-10-03T20:58:26.823442
---

# Trends in Web Threats in CY Q2 2022: Malicious JavaScript Downloaders Are Evolving

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

![](https://8aqnet.cdn.bcebos.com/228661ddbd64511674b492d5cd225e7d.jpg)

Trends in Web Threats in CY Q2 2022: Malicious JavaScript Downloaders Are Evolving

Executive SummaryPalo Alto N
*2022-10-26 21:0:5
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-132766.htm)
阅读量:34
收藏*

---

![Trends conceptual image, covering web threat trends such as the evolution of a malicious JavaScript downloader.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/Trends-r3d1.png)

## Executive Summary

Palo Alto Networks Advanced URL Filtering subscription collects data regarding two types of URLs; landing URLs and host URLs. We define a malicious landing URL as one that allows a user to click a malicious link. A malicious host URL is a page containing a malicious code snippet that could abuse someone’s computing power, steal sensitive information or perform other types of attacks.

Our researchers regularly track web threats to better understand trends that develop over time. This blog will cover trends we’ve identified between April 2022 and June 2022 using our web threat detection module.

Our detection module found around 751,000 incidents of malicious landing URLs containing different kinds of web threats, 253,000 (around one third) of which are unique URLs. In addition, the detection module also detected around 1,740,000 malicious host URLs, 256,000 (almost 15%) of which are unique.

In this blog, we present our analysis and findings of these web threat trends, including the following information:

* When these web threats were more active
* Where they were hosted
* What categories they belong to
* Which malware families are the most prevalent

We will also examine a malicious downloader case study regarding a campaign that shows how malicious JavaScript downloaders are evolving to evade different kinds of detections.

Palo Alto Networks customers receive protections from the web threats discussed here, as well as many others, via the [Advanced](https://www.paloaltonetworks.com/network-security/advanced-url-filtering) [URL Filtering](https://www.paloaltonetworks.com/products/threat-detection-and-prevention/web-security), [DNS Security](https://www.paloaltonetworks.com/network-security/dns-security) and [Threat Prevention](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/threat-prevention) cloud-delivered security services.

## Table of Contents

[Web Threats Landing URLs: Detection Analysis](#landing-urls-detection-analysis)

* [Time Analysis](#time-analysis)
* [Geolocation Analysis](#geolocation-analysis)
* [Category Analysis](#category-analysis)

[Web Threats Malicious Host URLs: Detection Analysis](#host-urls-detection-analysis)

* [Time Analysis](#host-time-analysis)
* [Geolocation Analysis](#host-geolocation-analysis)
* [Malware Class Analysis](#host-malware-class-analysis)
* [Malware Family Analysis](#host-malware-family-analysis)

[Web Threats Case Study: Malicious JavaScript Downloader](#case-study)

## Web Threats Landing URLs: Detection Analysis

Between April and June 2022, we collected data from our customers with our [Advanced](https://www.paloaltonetworks.com/network-security/advanced-url-filtering) [URL Filtering](https://www.paloaltonetworks.com/products/threat-detection-and-prevention/web-security) subscription, within the web threat detection module which uses special YARA signatures. We detected 751,331 incidents of landing URLs, containing all kinds of web threats, such as web skimmers and web scams. 253,644 of these landing URLS were unique. Compared with the results from [last quarter (Q1 2022)](https://unit42.paloaltonetworks.com/web-threat-trends-web-skimmer/), which had a total of 577,275 detected landing URLs and 116,643 unique URLs, we can see the totals rose in Q2.

### Web Threats Landing URLs Detection: Time Analysis

Figure 1 shows the total number of web threat hits in Q2 of 2022, how many of those hits were unique, and how many of those hits were also observed last quarter. As we can see, the repeated unique number from Q1 is low, which suggests that attackers are always trying to target new entry points.

![Bar chart describing web threats landing URLs distribution April-June 2022. Blue bars indicate all detections, including repeated detections of the same URL, red bars indicate detection of unique URLs, and orange bars indicate a detection that was seen in 2022 Q1 but unique in 2022 Q2.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-12.png)

Figure 1. Web threats landing URLs distribution April-June 2022. (Blue bars indicate all detections, including repeated detections of the same URL, and red bars indicate detection of unique URLs. Orange bars indicate a detection that was seen in Q1 2022 but unique in Q2 2022 ).

### Web Threats Landing URLs: Geolocation Analysis

According to our analysis, the previously mentioned 253,644 unique URLs are from 34,833 unique domains. After identifying the geographical locations for these domain names, we found the majority of them seem to originate from the United States, followed by Germany and Russia, as was also the case last quarter. However, we recognize attackers are leveraging proxy servers and VPNs located in those countries to hide their actual physical locations.

The choropleth map shown in Figure 2 indicates the wide distribution of these domain names across almost every continent. Figure 3 shows the top eight countries where the owners of these domain names appear to be located.

![Choropleth map showing the geolocation distribution of landing URLs between April and June 2022](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/word-image-36.png)

Figure 2. Web threat landing URLs’ domain geolocation distribution April-June 2022.

![Pie chart showing distribution of originating country of landing URLs from April to June 2022. United States - 64.4%, Germany - 4.9%, Russia - 2.0%, France - 2.0%, Canada - 1.8%, United Kingdom - 1.7%, Netherlands - 1.7%, India - 1.3%, Others - 20.2%](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-13.png)

Figure 3. Top eight countries where web threat landing URLs’ domains originated April-June 2022.

### Web Threats Landing URLs: Category Analysis

We analyzed the landing URLs initially identified by our detection model as benign, to find the common targets for these cyberattackers and where they may be trying to fool users. These landing URLs lead to people clicking on malicious host URLs. Going forward, all these landing URLs that lead to malicious code snippets will be marked as malicious by our product.

As shown in Figure 4, the top apparently benign targets are personal sites and blogs, followed by business and economy sites, and computer and internet information sites. Compared to last quarter, computer and internet information sites take third place over shopping sites. Because attackers often try to trick users into following malicious links from seemingly benign sites, we strongly recommend users exercise caution when visiting unfamiliar websites.

![Pie chart showing the top 10 categories hosting web threats from April to June 2022. Personal sites and blogs - 14.3%, business and economy sites - 13.8%, computer and internet - 7.8%, shopping - 5.5%, health and medicine - 4.7%, society - 4.6%, entertainment and arts - 4.4%, search engines - 3.7%, parked - 3.4%, travel - 3.2%, Others - 34.7%](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/10/chart-14.png)

Figure 4. We divided landing URLs that originally appeared benign into categories. Here are the top 10 categories that hosted web threa...