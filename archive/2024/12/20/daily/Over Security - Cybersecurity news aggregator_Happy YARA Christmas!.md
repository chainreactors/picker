---
title: Happy YARA Christmas!
url: https://blog.sekoia.io/happy-yara-christmas/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-20
fetch_date: 2025-10-06T19:42:00.789547
---

# Happy YARA Christmas!

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

# Happy YARA Christmas!

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR](#molongui-disabled-link)
December 19 2024

0

11 minutes reading

![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/Bonnet_de_noel.png)

## Table of contents

* [What is YARA?](#h-what-is-yara)
* [YARA rules at Sekoia.io](#h-yara-rules-at-sekoia-io)
* [Rule creation process](#h-rule-creation-process)
* [Custom tooling](#h-custom-tooling)

In the ever-evolving landscape of cybersecurity, effective threat detection is paramount. Since its creation, YARA stands out as a powerful tool created to identify and classify malware. Originally developed by Victor Alvarez of VirusTotal, **YARA has become a vital tool for security professionals seeking to streamline their threat-hunting processes**.

The Sekoia.io Threat Detection and Research (TDR) team incorporates YARA into its threat hunting workflow addressing various needs such as **identifying threats**, **tracking the evolution of malware families**, **infection chains**, and **uncovering suspicious files from unknown threats**. This article outlines the daily use of YARA at TDR and the tools that we use. More than making YARA rules our own, **we are sharing most of the created rules with our customers and partners via our platform**, it helps them in their investigations, triage process and DFIR engagements.

This blog post on our use of YARA rules is also an opportunity for us to announce **[the release of hundreds of our YARA rules on GitHub](https://github.com/SEKOIA-IO/Community/tree/main/yara_rules)**, which are now **directly integrated into VirusTotal for detection**. The community has contributed many ideas for detection rules, so it’s our turn to share a part of our own rules.

## What is YARA?

YARA is a **pattern-matching engine** designed to help security analysts in the identification and classification of malware samples. “YARA” stands for “Yet Another Recursive Acronym”. It uses a flexible and powerful rules-based approach to match patterns in files and processes, allowing for the detection and **identification of malware quickly in large data sets**.

This technology allows users to create rules that describe the characteristics of any file, literally ANY file. These rules can include strings, binary and regex patterns. The matching condition in YARA rules is highly customisable and can include logical operators and modifiers, making it possible to create precise and complex detection criteria.

By writing signatures that capture the unique attributes of a file, any malware researcher can detect known threats in files, volatile memory, network packets and even logs (yes…) !

Of course, **using YARA alone from the command line is not so fancy and customisable**. It reveals its full potential integrated with other security tools and frameworks, enhancing its utility in comprehensive malware analysis and incident response workflows. Several programming and scripting languages offer a library for dealing with YARA rules. This enables them to be integrated into SIEM, IDS/IPS or EDR systems, for example.

## YARA rules at Sekoia.io

The Threat Research and Detection team uses YARA rules to achieve one of its main objectives: track threats actively. The main goal behind this mission is to get new Indicators of Compromise (IoCs) related to infection vectors, malware, tools and threat actor’s infrastructure to feed our XDR and Threat Intelligence customers.

The YARA rules that we are using to track threats are shared with our customers but also used on other third party services to notify us when a rule is triggered. Among the wildly available services that we use: **[VirusTotal](https://virustotal.com)**, **[Triage](https://tria.ge/)**, or the **[YARAify](https://yaraify.abuse.ch/)** project from Abuse.ch. These services allow users to submit a file to identify whether it can be trusted. This file is scanned by security products and by detection rules submitted by analysts.

When a rule is triggered by a file, the file attributes are received and processed in-house, enriching the matched file with a context, for example, linking it in STIX to a known intrusion set, campaign, malware and/or tool. Some files can be retrieved and stored in our malware zoo by using **[AssemblyLine](https://cybercentrecanada.github.io/assemblyline4_docs/)** for further analysis, such as extracting their configuration. Some parts of the extracted configurations such as C2s, file paths, mutexes etc. can then be transformed into STIX new indicators for detection.

More than feeding [**Sekoia.io’s threat intelligence**](https://www.sekoia.io/en/product/cti/) with IoCs, TDR’s analysts often use YARA for hunting purposes. In fact, **YARA also serves to discover anomalies in files**, which can lead to discovery of new malware, exploits, or parts of infection chains, such as decoy documents, malicious archives, emails etc.

**Being creative to draft hunting rules is the most challenging part of YARA** rule creation. However, it’s also the most interesting as this shows you **the limitless of YARA capabilities when it comes to match any kind of file**.

#### Would you like to learn more about how we investigate code using YARA?

Charles Meslay presented this year at **[SSTIC’24](https://www.sstic.org/2025/news/)** how pivots can be made between codes by using YARA. This talk, in French, shows the philosophy and the methodology that we use at TDR to sign malicious binaries. You can watch it below.

[](https://static.sstic.org/videos2024/540p/la_retro-ingnierie_de_code_malveillant_dans_la_cti_-_analyse_de_levolution_dune_chaine_dinfection.mp4)

## Rule creation process

In our day-to-day work as CTI analysts, we enrich and capitalise in STIX 2.1 format all the relevant reports published in...