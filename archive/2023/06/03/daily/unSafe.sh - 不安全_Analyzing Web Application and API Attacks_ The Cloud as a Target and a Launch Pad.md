---
title: Analyzing Web Application and API Attacks: The Cloud as a Target and a Launch Pad
url: https://buaq.net/go-166994.html
source: unSafe.sh - 不安全
date: 2023-06-03
fetch_date: 2025-10-04T11:44:50.439547
---

# Analyzing Web Application and API Attacks: The Cloud as a Target and a Launch Pad

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

![](https://8aqnet.cdn.bcebos.com/f89efd9502f5e05330a4400a5a76ad92.jpg)

Analyzing Web Application and API Attacks: The Cloud as a Target and a Launch Pad

This post is also available i
*2023-6-2 21:0:57
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-166994.htm)
阅读量:33
收藏*

---

![A pictorial representation of web application and API attacks from the cloud](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/Cloud-21-illustration_orange.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/web-api-attacks-in-cloud/)

## **Executive Summary**

Unit 42 researchers have identified a growing trend of cyberattacks targeting web applications and application programming interfaces (APIs) hosted by cloud service providers. Based on the data from our research, 14.9% of attacks in late 2022 on web applications and APIs targeted cloud-hosted deployments.

Attackers are also operating in the cloud and using it to launch their attacks on applications and APIs, as 5.1% of the attacks originated from cloud service providers' addresses. We will discuss what web and API attacks are and why attackers are exploiting them in the cloud. We will also review possible reasons for attacks originating from the cloud, as well as the potential impact on businesses and individuals.

Palo Alto Networks customers using [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) are protected from these threats through the [WAAS](https://www.paloaltonetworks.com/prisma/cloud/web-application-API-security) module, which is designed to protect web applications and APIs in cloud environments.

| **Related Unit 42 Topics** | [**Cloud**](https://unit42.paloaltonetworks.com/category/cloud/), **[Malware](https://unit42.paloaltonetworks.com/category/malware-2/)** |
| --- | --- |

## **Table of Contents**

[Understanding Web Applications and APIs](#post-128390-_nbiz5w9g736v)

## Understanding Web Applications and APIs

[APIs](https://www.paloaltonetworks.com/cyberpedia/what-is-api-security) and [web applications](https://www.paloaltonetworks.com/cyberpedia/what-is-web-application-and-api-protection) play a pivotal role in today's digital landscape. Web applications are software programs accessed through web browsers, providing interactive and engaging user experiences. Meanwhile, APIs act as intermediaries that facilitate communication between different software applications.

By enabling seamless interaction between applications, APIs simplify complex processes and promote a more connected digital ecosystem. Generally, both web applications and APIs are served on the [HTTP](https://he.wikipedia.org/wiki/Hypertext_Transfer_Protocol) protocol.

The widespread use of web applications and APIs has made them an integral part of the modern online world. Businesses, organizations and developers are increasingly adopting them to create user-friendly interfaces and automate processes, boosting efficiency and productivity.

The growing reliance on these technologies has also led to an increased focus on ensuring their security and reliability. As a result, it is essential to keep up with [best practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) and stay informed about potential vulnerabilities to protect valuable data and to maintain users' trust.

## Web Applications and APIs on the Cloud

There has been a significant surge of organizations moving web applications and APIs to the cloud in recent years. Recognition among businesses and organizations of the numerous benefits offered by cloud solutions is driving this transformation.

Cloud applications are mainly based on [microservices architecture](https://en.wikipedia.org/wiki/Microservices), which is why the shift to the cloud is encouraging an evolution in software architecture. This difference is driving these organizations to embrace microservices architecture.

There are also many advantages of employing a microservices architecture, which is an approach to software development where an application is divided into small, independent services that communicate with each other through APIs.

A recent survey of nearly 400 organizations [by TechTarget's Enterprise Strategy Group (ESG) Research Team](https://start.paloaltonetworks.com/2023-api-security-data-in-new-report.html), published in April 2023 and co-sponsored by Palo Alto Networks, revealed that organizations plan to double down on microservices architecture for their applications and move their production workloads into cloud providers.

![Image 1 is a column graph of the percentage of public-facing web applications based on microservices for cloud native architecture. The percentage of the columns in blue is the percentage as of May 2023. The percentages in teal are what is predicted from 24 months from May 2023. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/word-image-128390-1.png)

Figure 1. Public-facing web applications based on microservices. "Today” and "from now" date from the April 2023 survey. Source: "[Securing the API Attack Surface](https://start.paloaltonetworks.com/2023-api-security-data-in-new-report.html)," ESG and Palo Alto Networks.

![Image 2 is five pie charts of the production workloads that are run on public cloud infrastructure. The percentages in blue are the percentage of production workloads run on public cloud infrastructure services today in 2023. The percentages in teal are the production workloads run on public cloud infrastructure services 24 months from May 2023. From left to right, the pie charts are: 10% to 20% of workloads, 21 to 30% of workloads, 31% to 40% of workloads, 41% to 50% of workloads, and lastly, more than 50% of workloads. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/word-image-128390-2.png)

Figure 2. Production workloads run on public cloud infrastructure. “Today” and "from now" date from the April 2023 survey. Source: "[Securing the API Attack Surface](https://start.paloaltonetworks.com/2023-api-security-data-in-new-report.html)," ESG and Palo Alto Networks.

A wide variety of organizations are increasingly deploying their web applications and APIs in the cloud due to its compelling advantages. Cloud-based infrastructure offers scalability, flexibility and cost-effectiveness, allowing businesses to adapt to changing demands quickly and only pay for the resources they use. Moreover, the cloud enables faster development and deployment cycles, promoting innovation and agility.

## Attacks on Web Applications and APIs in the Cloud

Unit 42 researchers conducted research on roughly 12 billion attacks targeting web applications and APIs to determine if attackers are targeting such instances on the cloud. Their findings revealed that attackers indeed place increased emphasis on targeting cloud-hosted web applications and APIs.

Through the analysis of this data, we discovered that 14.9% of attacks on web applications and APIs were directed at workloads hosted by the top three cloud vendors. This indicates that the cloud is not only a critical component for businesses but also an increasingly attractive target for cybercriminals.

![Image 3 is a pie chart of the destination of attacks. 85.1% are from others, and 14.9% are from the cloud. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/06/chart.png)

Figure 3. Destination of the attacks.

We believe attackers are increasingly targeting web applications and APIs in the cloud for several reasons.

* Growing adoption of cloud services:
  + As more businesses and individuals migrate their workloads to the cloud for...