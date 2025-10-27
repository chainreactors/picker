---
title: 2023 Breaches and Incidents: Personal Notes
url: https://buaq.net/go-169864.html
source: unSafe.sh - 不安全
date: 2023-06-23
fetch_date: 2025-10-04T11:44:28.161064
---

# 2023 Breaches and Incidents: Personal Notes

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

![](https://8aqnet.cdn.bcebos.com/b3ebabb696e5c46ab2e12c27a1173a0e.jpg)

2023 Breaches and Incidents: Personal Notes

IntroductionIn today’s digital landscape, the prevalence of cyber threats and incidents
*2023-6-22 21:34:44
Author: [marcoramilli.com(查看原文)](/jump-169864.htm)
阅读量:20
收藏*

---

#### Introduction

In today’s digital landscape, the prevalence of cyber threats and incidents has become a significant concern for individuals, organizations, and governments alike. I have had the opportunity to explore numerous vendor reports in the past months and gain insights into the evolving nature of breaches and incidents. Through my research, I have discovered a multitude of interest findings, highlighting the relentless persistence and sophistication of cybercriminals. Many things are changing and for that I’ve decided to bring you the followings takeaways.

By analyzing these reports, it becomes clear that breaches and incidents are not isolated occurrences but rather an ongoing battle in the realm of cybersecurity. The information gathered highlights the critical need for robust security measures, constant monitoring, and proactive incident response strategies to safeguard digital assets from malicious actors. As we delve further into this blog post, we will explore the specific findings and recommendations outlined in these reports, aiming to provide insights and practical advice to help individuals and organizations navigate the complex cybersecurity landscape.

#### Actors

The main threat actors involved in data breaches are **External** to the victim. Less then **20%** of actors are internal, which means they are eligible for intentional attack as well as unintentional attack (is. errors, stolen devices, weak credentials)

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2023/06/Screenshot-2023-06-12-alle-09.37.26.png?resize=661%2C356&ssl=1)

The main reason threat actors are attacking victim is by far “**money**“. They are **Financially** motivated in mostly cases which emphasize the importance of being part of a bigger and organized industry (organized crime)

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2023/06/Screenshot-2023-06-12-alle-09.35.09.png?resize=619%2C332&ssl=1)

Threat Actor Motivation in Data Breaches

While organized crime is the principal threat actor, “non-nation state or State-affiliated” threat actor is the second most common threat actors. In this category we include Noname\*, KillNet and other “war sympathetic groups”.

#### Actions

To my surprise, as someone who has become accustomed to viewing ransomware as the primary threat actor action, this year has witnessed a gradual but noteworthy shift. Ransomware is no longer at the forefront of attacker actions; instead, it has slipped into the second position. What we are observing predominantly in the current landscape is the prominence of **stolen** **credentials** as the principal action undertaken by threat actors.

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2023/06/Screenshot-2023-06-12-alle-09.30.39.png?resize=571%2C329&ssl=1)

Top Action performed by actors in data breaches

Traditionally, ransomware has garnered significant attention due to its disruptive and financially driven nature. However, recent trends suggest that threat actors are increasingly focusing on exploiting compromised credentials as their preferred method of attack. This shift can be attributed to several factors, including the rise of sophisticated phishing campaigns, data breaches resulting in massive credential leaks, and the monetization potential of stolen login information.

The implications of this shift are far-reaching and demand heightened attention from both individuals and organizations. Stolen credentials provide threat actors with an entry point to compromise sensitive systems, gain unauthorized access to valuable data, and even facilitate lateral movement within networks. Moreover, the aftermath of such breaches can be catastrophic, leading to financial losses, reputational damage, and legal ramifications.

Another intriguing observation that has emerged is the resurgence of “**Exploit** **Vulnerabilities**,” which had been somewhat overlooked until this year. The primary reason for this resurgence can be attributed to the prevalence of various remote code execution vulnerabilities, or more broadly, remote exploitable vulnerabilities. These vulnerabilities have captured significant attention in the cybersecurity landscape, ranging from **well-known instances like Log4j** (very abused during the 2022) to more recent RCE.

#### Assets

In the realm of data breaches, it is evident that a significant portion of the compromised assets primarily consists of **servers** and **general** **IT** **infrastructure**. These critical components form the backbone of organizations’ digital operations and are often targeted by threat actors seeking to gain unauthorized access or exploit vulnerabilities. The compromise of servers and IT infrastructure can have severe consequences, ranging from service disruptions to the potential exposure of sensitive information.

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2023/06/Screenshot-2023-06-12-alle-09.59.12.png?resize=598%2C533&ssl=1)

Compromised Assents in Data Breaches

However, following closely in the list of compromised assets are **personal** **information** and data pertaining to individuals. This includes a range of personally identifiable information (**PII**) such as email addresses, names, surnames, phone numbers, addresses, and user logs. The targeting of personal data highlights the value placed on this information by threat actors, who seek to exploit it for various malicious purposes, such as identity theft, phishing attacks, or even selling it on the dark web.

The inclusion of personal information in data breaches raises significant concerns regarding privacy and security. The exposure of such sensitive data not only poses risks to individuals’ personal lives but also has broader implications for organizations responsible for safeguarding this information. The fallout from these breaches can result in financial losses, reputational damage, legal consequences, and erosion of trust among stakeholders.

#### Attributes

Data breaches encompass a wide range of compromised information, and understanding the nature of the data involved is crucial in comprehending the extent of the breach’s impact. Analysis of various data breach incidents reveals that the principal category of compromised data is related to **individuals**, constituting approximately **36%** of the total. This includes personally identifiable information (**PII**) such as names, addresses, email addresses, phone numbers, and other personal details that can be exploited for identity theft, fraud, or other malicious activities.

Another significant portion, accounting for around **28%** of breached data, comprises **credential** **information**. These credentials can encompass usernames, passwords, security tokens, or any other form of authentication data that grants access to various accounts or systems. The compromise of credentials poses a severe threat, as attackers can misuse them to gain unauthorized access to sensitive information or carry out fraudulent activities, potentially causing significant harm to individuals and organizations alike.

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2023/06/Screenshot-2023-06-12-alle-10.14.04.png?resize=715%2C255&ssl=1)

Top Confidentiality data varieties in breaches

Furthermore, **internal system information** constitutes ap...