---
title: Kelvin Security and Spectre, investigating possible relationships
url: https://labs.yarix.com/2024/05/__trashed/
source: Over Security - Cybersecurity news aggregator
date: 2024-05-11
fetch_date: 2025-10-06T17:18:54.288256
---

# Kelvin Security and Spectre, investigating possible relationships

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Kelvin Security and Spectre, investigating possible relationships

* [Home](https://labs.yarix.com "Go to Home Page")
* Kelvin Security and Spectre, investigating possible relationships

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2024/12/featured_image-1024x445.jpg)

10May10/05/2024

## Kelvin Security and Spectre, investigating possible relationships

[cti](https://labs.yarix.com/author/cti/ "Posts by cti")2024-05-10T10:00:38+02:00

By
[cti](https://labs.yarix.com/author/cti/ "Posts by cti")

Reading Time:   17 minutes

# **Kelvin Security and Spectre, investigating possible relationships**

## Introduction

The **Yarix Cyber Threat Intelligence Team (YCTI)** has conducted an investigation that has discovered a possible relationship between the threat actor **Kelvin Security** with another threat actor called **Spectre**. This relations was identified through the discovery and analysis of an indicator found within an Italian governmental leak that was shared by a malicious actor. The following analysis attempts to identify links between both threat actors by reconstructing the last months of public activity of the Kelvin Security group.

## Brief introduction of the KelvinSecurity group and Spectre

**Kelvin Security** is a threat actor (TA) who is believed to be active since 2013. The group has been targeting critical infrastructure, governmental targets as well as private companies. It is believed that Kelvin is composed of many members and the original funders might come from South America.[[1]](#_ftn1) The group exploits web pages and vulnerabilities in exposed services as well as make use of stolen corporate credentials to extract large sets of internal data and selling them on Dark Web forums.[[2]](#_ftn2) Only in the last three years, the group has attacked more than 300 organizations in more than 90 countries around the world. Notorious recent leaks and corporate credential selling released by Kelvin Security are BMW (2020), Walmart (2022), the Italian Ministry of Transport (2022) Vodafone Italia (2022), the German Institute of Global and Area Studies – GIGA – (2023).

**Spectre** is the owner of a data leak site called **Intel Repository**. The threat actor is specialized in sharing classified leaks related to governments and armed forces. It is believed that the threat actor has been active since 2020. Spectre describes itself as a data broker. One of the most famous leaks shared by **Spectre** is a set of files released in 2020 of a defense manufacturer called Havelsan containing NATO and Turkish military documents.[[3]](#_ftn3) According to open source information, there is no evidence that the Threat Actor exploits vulnerabilities to obtain data, rather, the TA search for, buys and shares leaks. Currently, Spectre is the owner of the data leak site called **Intel Repository**and the **Intel Exchange** Telegram channel. In July 2023, Spectre acquired the Telegram channels originally used by the group Kelvin Security as a result of the group’s alleged retirement.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x46.jpg)

*The official Telegram logos of Kelvin Security (on the left) and Intel Exchange (on the right)*

## The Italian Federal Police leak

The YCTI Team collaborates with national law enforcement organs by informing when relevant data leaks and indicators of compromise are identified in the cyber underground.

In this case, the investigation started at the end of April 2023, when evidence of a compromised Italian State Police e-mail account was circulating in specific Telegram channels. The selling of the access has been advertised through the Telegram channel called **Classified documents sale by AIG**. In the sample provided, the threat actor shared screens of a webmail inbox showing the account that has been allegedly compromised.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x147.jpg)

*The sample from the Telegram channel Classified document sale by AIG.*

Initially, the YCTI team found it suspicious that some of the images contained elements and words translated into Spanish. This aspect contributed to the idea that the images could have been somehow fabricated by a distracted non-Italian-speaking threat actor which might have misled Italian and Spanish words.

However, the proofs seemed to be legitimate as the e-mail contents describe official high-level institutional meetings between Italian and foreign leaders which actually took place during April 2023.[[4]](#_ftn1)

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x39.jpg)

*The sample shared by the threat actor – e-mail describing the Visit of the Prime Minister of Ukraine April 26, 2023.*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x44.jpg)

*Official Statement of the Prime Minister of Ukraine visit to Italy (source: Ukraine government portal).*

Unfortunately, further direct contact with the threat actor did not bring any useful indicator that would have clarified the context and legitimacy of the data provided. A few days later, the post was removed from the Telegram channel.

Later on, similar announcements announcing the sale of Italian Federal Police documents circulated within two different Telegram channels, the first one called **Intel Repository** and the second called **Intel Exchange**. While the first post published in June was deleted after two days and did not contain any useful indicators, the second message published in July contained a URL address leading to a set of proofs matching the ones already shared back in April 2023.

As it will become clearer later in the article, both June and July posts were published by the same Threat Actor called **Spectre**. While the first message was published on the official **Intel Repository** Telegram channel, the second was published on the former **Kelvin Security** channel which was acquired by **Spectre** in July 2023 and rebranded as **Intel Exchange**.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x18.jpg)

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x144.jpg)

*Evidences from the Telegram channel Spectre’s Intel Repository.*

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x29.jpg)

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x42.jpg)

*Evidences from the channel Intel Exchange (former Kelvin Security Telegram channel).*

As a result of direct contact with **Spectre**, the administrator of the **Intel Exchange** Telegram channel, the YCTI Team was able to retrieve a noticeable amount of data which have been shared through a drive folder by the threat actor.

The shared folder contained an archive which was including a dump of around 600 megabytes of e-mails and attachments related to the Italian Federal Police account.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x35.jpg)

*The screen of the drive folders containing the archive of the Italian Police e-mail dump*

At this point, the YCTI Team shared the findings with the national law enforcement point of contact and continued the investigation using the available elements to gain more knowledge about the threat actor who shared the samples.

The analysis of the source of the page of the shared folder allowed the identification of an exposed e-mail address **kelvin\*\*@gmail[.]com**.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x11.jpg)

*Ind...