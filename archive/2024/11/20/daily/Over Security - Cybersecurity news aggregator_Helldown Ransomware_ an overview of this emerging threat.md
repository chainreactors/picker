---
title: Helldown Ransomware: an overview of this emerging threat
url: https://blog.sekoia.io/helldown-ransomware-an-overview-of-this-emerging-threat/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-20
fetch_date: 2025-10-06T19:25:26.097416
---

# Helldown Ransomware: an overview of this emerging threat

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

# Helldown Ransomware: an overview of this emerging threat

This blogpost provide a comprehensive Analysis of Helldown: Tactics, Techniques, and Procedures (TTPs).

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion and Sekoia TDR](#molongui-disabled-link)
November 19 2024

0

17 minutes reading

*This report on Helldown was originally published for our customers on *14 November* 2024.*

## Table of contents

* [Context](#h-context)
* [Helldown Intrusion Set](#h-helldown-intrusion-set)
  + [Overview](#h-overview)
  + [Victimology](#h-victimology)
  + [Modus Operandi](#h-modus-operandi)
    - [Initial access – the Zyxel lead](#h-initial-access-the-zyxel-lead)
    - [Data stealing](#h-data-stealing)
* [Helldown ransomware – Windows](#h-helldown-ransomware-windows)
  + [Dynamic analysis](#h-dynamic-analysis)
  + [Static analysis](#h-static-analysis)
  + [Similarities](#h-similarities)
* [Helldown ransomware – Linux](#h-helldown-ransomware-linux)
  + [Code overview](#h-code-overview)
  + [Encryption](#h-encryption)
  + [ESX targeted](#h-esx-targeted)
* [Connection with the ransomware ecosystem](#h-connection-with-the-ransomware-ecosystem)
  + [Helldown vs. Hellcat](#h-helldown-vs-hellcat)
  + [Helldown vs. Darkrace or Donex](#h-helldown-vs-darkrace-or-donex)
* [Conclusion](#h-conclusion)
* [IoCs](#h-iocs)

## Context

Through our social media monitoring, Sekoia’s Threat Detection & Research (TDR) team identified a [tweet](https://x.com/TuringAlex/status/1851969443426914503) posted on 31 October 2024 mentioning a Linux variant of the **Helldown** ransomware targeting **Linux** systems.

The Helldown ransomware group is a relatively new and still largely undocumented Intrusion Set (IS), previously known to deploy ransomware exclusively on Windows systems. He employs its own custom ransomware and engages in double extortion tactics. He is particularly active, claiming **31 victims** within **three months**, including Zyxel’s European subsidiary.

This blog post provides a detailed examination of this emerging threat. Based on its pattern of targeting, we offer insights into its methods of operation. A technical analysis of both the Windows and Linux variants of this ransomware is also included.

## Helldown Intrusion Set

### Overview

Helldown is a relatively new Intrusion Set in the ransomware landscape, first documented by [Cyfirma](https://www.cyfirma.com/research/tracking-ransomware-august-2024/) in their August ransomware tracking report. Although still largely undocumented, the group is highly active, having listed 28 victims on its Data Leak Site (DLS) since 5 August 2024.

While the group’s exact methods remain unclear, both Cyfirma and [Cyberint](https://cyberint.com/blog/research/ransomware-trends-2024-report/) reports that it exploits vulnerabilities to infiltrate victims’ networks and deploy its ransomware. The IS employs a double extortion strategy, exfiltrating large volumes of data and threatening to publish it on its .onion site if the ransom is not paid.

The group’s DLS underwent changes toward the end of August. Notably, while the victims listed on the original DLS were transferred to the new one, three victims were removed. The reason for this removal is unclear, but it may indicate that a ransom was paid.

### Victimology

As of 7 November 2024, the group has allegedly compromised 31 victims, primarily small and medium-sized businesses. However, some larger companies have also been affected, including **Zyxel Europe** which provides network and cybersecurity solutions, including firewalls, routers, and access points across Europe. Most of the victims are located in the United States, with others primarily in Europe, including 3 in France.

The timeline below illustrates that the group was highly active in August and October, with a quieter period in September. This period aligns with the switch to a new DLS, suggesting that the group may have prioritised developing its tools over active ransomware operations during this time.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/11/helldown-timeline.png)

*Figure 1. Helldown victims over time as published on their DLS, as of 7 November 2024*

### Modus operandi

Like many ransomware groups, Helldown engages in double extortion. However, details about its Techniques, Tactics and Procedures remain undocumented. By analysing the profile of its victim, we can gain a clearer understanding of its intrusion and data theft techniques.

#### Initial access – the Zyxel lead

* **TDR analysis hypothesis**

On 4 November 2024, through an analysis of the attack surfaces of various victims, TDR identified that at least eight victims, including one compromised in early August, were using Zyxel firewalls as IPSec VPN access points during the time of their breach. Historical searches on the Censys engine also revealed that two of these victims replaced their Zyxel firewalls with other brands shortly after being compromised.

In an [advisory bulletin](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-multiple-vulnerabilities-in-firewalls-09-03-2024) issued on 3 September 2024, Zyxel announced security patches to address vulnerabilities in its firewalls. One of these, CVE-2024-42057, is especially critical as it allow an attacker to execute malicious code without authentication, although specific prerequisites must be met. This vulnerability was identified by nella17 (@nella17tw) of the Devcore research team. As of early/mid – November 2024, no public exploit code is available for this vulnerability or other recent vulnerabilities affecting Zyxel products.

In late September 2024, multiple users on the Zyx...