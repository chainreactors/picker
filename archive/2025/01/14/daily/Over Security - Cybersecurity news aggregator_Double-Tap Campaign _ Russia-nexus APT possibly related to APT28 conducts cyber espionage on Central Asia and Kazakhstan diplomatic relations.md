---
title: Double-Tap Campaign : Russia-nexus APT possibly related to APT28 conducts cyber espionage on Central Asia and Kazakhstan diplomatic relations
url: https://blog.sekoia.io/double-tap-campaign-russia-nexus-apt-possibly-related-to-apt28-conducts-cyber-espionage-on-central-asia-and-kazakhstan-diplomatic-relations/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-14
fetch_date: 2025-10-06T20:13:10.716179
---

# Double-Tap Campaign : Russia-nexus APT possibly related to APT28 conducts cyber espionage on Central Asia and Kazakhstan diplomatic relations

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Double-Tap Campaign: Russia-nexus APT possibly related to APT28 conducts cyber espionage on Central Asia and Kazakhstan diplomatic relations

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/01/TDR-badge.png)](#molongui-disabled-link)

[Amaury G., Maxime A., Erwan Chevalier, Felix Aimé and Sekoia TDR](#molongui-disabled-link)
January 13 2025

0

20 minutes reading

*This report was originally published for our customers on 12 *December* 2024.*

## Table of contents

* [Introduction](#h-introduction)
* [I. UAC-0063 background](#h-i-uac-0063-background)
* [II. Initial findings](#h-ii-initial-findings)
* [III. HATVIBE and CHERRYSPY infection chain](#h-iii-hatvibe-and-cherryspy-infection-chain)
  + [Double-Tap infection chain leading to HATVIBE execution](#h-double-tap-infection-chain-leading-to-hatvibe-execution)
  + [Focus on HATVIBE](#h-focus-on-hatvibe)
  + [A potential overlap with APT28-related Zebrocy campaigns](#h-a-potential-overlap-with-apt28-related-zebrocy-campaigns)
* [IV. From Kazakhstan to Central Asia: a focus on a broader strategic espionage](#h-iv-from-kazakhstan-to-central-asia-a-focus-on-a-broader-strategic-espionage)
  + [Kazakhstan geopolitical context](#h-kazakhstan-geopolitical-context)
  + [Kazakhstan targeting for broader intelligence gathering](#h-kazakhstan-targeting-for-broader-intelligence-gathering)
* [V. Detection opportunities](#h-v-detection-opportunities)
  + [Registry change](#h-registry-change)
  + [Scheduled task](#h-scheduled-task)
* [Conclusion](#h-conclusion)
* [Appendix](#h-appendix)
  + [C2](#h-c2)
  + [Weaponized documents](#h-weaponized-documents)
  + [Deobfuscated HATVIBE VBA code](#h-deobfuscated-hatvibe-vba-code)
  + [YARAs](#h-yaras)

## Introduction

On Wednesday, 27 November 2024, Russian President Putin was on a 2-day state visit in Kazakhstan to discuss with local representatives the implementation of energy projects and to counter Chinese and Western influence. Putin said he was visiting his “true ally”, yet Sekoia investigated an ongoing cyber espionage campaign using legitimate Office documents assessed to originate from the Ministry of Foreign Affairs of the Republic of Kazakhstan, that were further weaponized and likely used to collect strategic intelligence in Central Asia, including Kazakhstan and its diplomatic and economic relations with Asian and Western countries. We assess it is possible that this campaign was conducted by a Russia-nexus intrusion set, UAC-0063, sharing overlaps with APT28.

## I. UAC-0063 background

**UAC-0063** is an intrusion set active since at least 2021 that was first [exposed](https://cert.gov.ua/article/4697016) by **CERT-UA** in April 2023 for conducting a cyber espionage campaign targeting several countries such as Ukraine, Israel and India, including multiple central Asian countries (Kazakhstan, Kyrgyzstan and Tajikistan). CERT-UA analysts identified spearphishing lure Word documents with malicious macros sent by a compromised official mailbox of the Embassy of Tajikistan in Ukraine.

UAC-0063 targeting suggests a focus on **intelligence collection** in sectors such as government, including diplomacy, NGOs, academia, energy, and defence, with a geographic focus on **Ukraine**, **Central Asia**, and **Eastern Europe**.

Later, in July 2024, CERT-UA published another report exposing UAC-0063 activities targeting Ukrainian scientific research institutions with new malware (dubbed HATVIBE and CHERRYSPY). The report associates the intrusion set UAC-0063 with **APT28 with medium confidence**.

As a reminder, APT28 is a well-studied intrusion set active since at least 2004, attributed by multiple governments and cybersecurity experts to **Russia’s General Staff Main Intelligence Directorate** (**GRU**) Military Unit 26165. This intrusion set is especially known for its hybrid operations on the sidelines of armed conflicts (Ukraine 2015, 2017, 2022), election manipulation (2016 US and 2017 French Presidential Election), and diplomatic crises related to Russia (TV5 Monde 2015).
Our colleagues from **Recorded Future** are tracking UAC-0063 under the alias TAG-110, [assessing](https://go.recordedfuture.com/hubfs/reports/CTA-RU-2024-1121.pdf) that its activities overlap with APT28’s strategic interests, yet without confirming the CERT-UA’s medium confidence association with APT28 based on technical elements.

## II. Initial findings

In late July 2024, our attention was drawn to an [article published by CERT-UA](https://cert.gov.ua/article/6280129) detailing the activities of the UAC-0063 intrusion set, leveraging HATVIBE and CHERRYSPY malware to conduct cyber espionage operations against government institutions. We conducted further research to identify a pattern for future Command and Control (C2) servers and to further track it through our [Sekoia C2 Trackers](https://blog.sekoia.io/adversary-c2-infrastructures-tracked-in-2023/) project. We also created a set of YARA rules to detect the infection chain and the deployed malware.

On 16 October 2024, one of our YARA rules that detects malicious macros caught a malicious file uploaded to VirusTotal. The Office document titled *Rev5\_Joint Declaration C5+GER\_clean version.doc* seemed to be a draft version of a diplomatic join statement containing a malicious macro that prompts the user for permission for execution and lead to the compromise of the host.

Within a function in the macro, we observed the removal of the document’s protection using a highly unique password. By pivoting on this password, we were able to identify **10 additional Word documents that had not yet been publicly disclosed**.

Our investigation led us to find 18 DOCX files with embedded macros, including seven blank documents that are part of the same infection chain. **Almost all documents likely originally belong to the Ministry of Foreign Affairs of the Repub...