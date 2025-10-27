---
title: Recent Trends in Internet Threats: Common Industries Impersonated in Phishing Attacks, Web Skimmer Analysis and More
url: https://buaq.net/go-161014.html
source: unSafe.sh - 不安全
date: 2023-04-29
fetch_date: 2025-10-04T11:32:46.695125
---

# Recent Trends in Internet Threats: Common Industries Impersonated in Phishing Attacks, Web Skimmer Analysis and More

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

![](https://8aqnet.cdn.bcebos.com/a2f00d8c360291c1c92d8d8643a5ec7d.jpg)

Recent Trends in Internet Threats: Common Industries Impersonated in Phishing Attacks, Web Skimmer Analysis and More

Executive SummaryFrom July-D
*2023-4-28 21:0:16
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-161014.htm)
阅读量:37
收藏*

---

![A pictorial representation of internet threat trends in the last half of 2022](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/Trends-r3d1.png)

## **Executive Summary**

From July-December 2022, Unit 42 researchers have observed and analyzed over 67 million unique malicious URLs, domains and IPs, which we use to block associated malicious network traffic. We will cover the trends we have observed during the second half of 2022 based on our detections of malicious URLs, domains and IPs.

We present our analysis and findings of these internet threat trends, including the following information:

* A view of the internet threat landscape
  + This includes malicious URL distribution, geolocation, category analysis and statistics describing attempted malware attacks that we observe
* A spotlight on internet threats of particular interest
  + This includes industry sectors being targeted for spoofing in phishing pages, as well as downloaded malware statistics, injected JavaScript (JS) malware analysis and malicious DNS analysis
* A case study of a classic web skimmer that infected a Tranco top 1 million-rated website

Palo Alto Networks customers receive protections from the web and DNS threats discussed here via the Advanced URL Filtering, DNS Security and Advanced Threat Prevention Cloud-Delivered Security Services.

| **Related Unit 42 Topics** | **[Web threats](https://unit42.paloaltonetworks.com/tag/web-threats/),** [**Phishing**](https://unit42.paloaltonetworks.com/tag/phishing/), [**Cryptomining**](https://unit42.paloaltonetworks.com/tag/cryptomining/) |
| --- | --- |

[Internet Threat Landscape](#post-127920-_eo047sk27ry1)

## **Internet Threat Landscape**

During the second half of 2022 (H2), we amassed over 67 million malicious domains and URLs, an increase of over 52% over the first half of 2022 (H1). These malicious domains and URLs have a broad impact on their victims. We observed over 12 million HTTP requests to some of these malicious URLs and over 60 million DNS requests to these domains every day. These malicious URLs are collected from third-party feeds as well as our own internal analyzers. These analyzers include a variety of types including web crawlers, malware traffic analyzers and deep learning models.

Looking more closely at malicious JavaScript samples as an example, during the second half of 2022, we detected over 4 million malicious JS samples hosted on 4.8 million malicious URLs and 1.6 million hostnames. Compared to the first half of the year, the total number of URLs containing malicious JavaScripts increased by 99.3%.

![Image 1 is a column graph, showing the percentage of URLs compared to host names, in millions, for the first half to the second half of 2022. There is a much larger number of unique URLs in the second half of 2022 compared to the first half. In the second half of 2022, the first half and second half measurements are more equal.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/word-image-127920-1.png)

Figure 1. The number of malicious JS and their hosting URLs and hostnames.

### Malicious URL and Domain Distribution

Figure 2 shows the number of newly observed malicious URLs each quarter. Compared to H1 2022, the number of malicious URLs in H2 increased by 52%. For the grayware and command-and-control (C2) categories, even though the number of observed URLs dropped in Q4, the total increase in H2 is still 80% and 165%, respectively, when compared to H1.

![Image 2 is a column chart showing the amount (in log scale) of newly observed malicious URLs from quarter 1 to quarter 4 in 2022. It compares malware, phishing, grayware, and command and control over these four quarters. The largest numbers are malware and the smallest are C2.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/word-image-127920-2.png)

Figure 2. Number of newly observed malicious URLs from Q1 to Q4 2022.

Figure 3 shows the number of new malicious domains in each month from July-December 2022. Note that for the monthly numbers for the grayware and C2 categories, the number of detections are distributed less evenly than the other categories, mainly because they are more related to specific attack campaigns.

For example, one of the main sources of URLs in the grayware category is from detected clusters of malicious domains belonging to the same campaign at their registration time. More details of this detection logic are presented in [Detecting and Preventing Malicious Domains Proactively with DNS Security](https://unit42.paloaltonetworks.com/proactive-detector/).

![Image 3 is a column chart comparing the number of malicious domains observed from July to December 2022. Like figure 2, the largest percentage is malware, and the smallest is C2.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/word-image-127920-3.png)

Figure 3. The number of malicious domains observed from July-December 2022.

### Geolocation Analysis of Malicious URLs

By looking at passive DNS data and an IP to location database, we can retrieve the IPs where the domains hosting the malicious URLs are located. Figures 4 and 5 below show the geolocation distribution of the domains hosting malicious URLs worldwide. Note: Figure 4 is an interactive map. To see distribution, hover your mouse over the map for data by country. The meter will indicate where it falls between 0 and 7.5.

*Figure 4. Geolocation distribution of domains (in millions) hosting malicious URLs during July-December 2022.*

Although malicious websites are hosted in more than 150 countries and regions, over 85% are hosted in the top eight countries, as shown in Figure 5.

Similar to what we observed in [Q1 2022](https://unit42.paloaltonetworks.com/web-threat-trends-web-skimmer/) and [Q2 2022](https://unit42.paloaltonetworks.com/web-threats-malicious-javascript-downloader/), the majority of all malicious URLs and domains continue to be hosted in the United States. During the second half of 2022, the next most common hosting locations were Brazil and China.

![Image 5 is a pie chart of the top eight countries for malicious URLs hosted during July to December 2022. The largest percentage is the United States at 51.8%, followed by Brazil, China, and Germany.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/04/word-image-127920-5.png)

Figure 5. Top eight countries hosting malicious URLs during July-December 2022.

### Category Analysis

We also analyzed the distribution of the original content categories of the malicious URLs and domains we amassed. In other words, we determined what they were intended for before they were used for malicious purposes or were otherwise detected as malicious. This analysis aims to find the common targets for these cyberattacks and how they might be trying to fool people.

Figure 6 shows the distribution of the original categories for the malicious URLs in Advanced URL Filtering. Unsurprisingly, URLs with the original categories Insufficient Content and Newly Registered Domains make up over 30% of all malicious URLs. We classify a URL as Insufficient Content when it does not host enough content for classification. In both cases, this result makes sense as, after an attacker registers a domain, it will likely fall into these two categories before the U...