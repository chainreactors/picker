---
title: Exposing FakeBat loader: distribution methods and adversary infrastructure
url: https://blog.sekoia.io/exposing-fakebat-loader-distribution-methods-and-adversary-infrastructure/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-03
fetch_date: 2025-10-06T17:45:19.495295
---

# Exposing FakeBat loader: distribution methods and adversary infrastructure

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

# Exposing FakeBat loader: distribution methods and adversary infrastructure

During the first semester of 2024, FakeBat (aka EugenLoader, PaykLoader) was one of the most widespread loaders using the drive-by download technique.

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue and Sekoia TDR](#molongui-disabled-link)
July 2 2024

0

23 minutes reading

## Table of contents

* [Context](#h-context)
* [Interactions on cybercrime forums](#h-interactions-on-cybercrime-forums)
  + [FakeBat loader](#h-fakebat-loader)
  + [Associated distribution service](#h-associated-distribution-service)
* [Different clusters distributing FakeBat](#h-different-clusters-distributing-fakebat)
  + [Malvertising and software impersonation](#h-malvertising-and-software-impersonation)
  + [Fake web browser updates](#h-fake-web-browser-updates)
  + [Social engineering schemes on social networks](#h-social-engineering-schemes-on-social-networks)
* [Tracking adversaries infrastructure](#h-tracking-adversaries-infrastructure)
  + [FakeBat C2 servers](#h-fakebat-c2-servers)
  + [Landing pages impersonating popular software websites](#h-landing-pages-impersonating-popular-software-websites)
* [Conclusion](#h-conclusion)
* [FakeBat IoCs & Technical details](#h-fakebat-iocs-amp-technical-details)
  + [IoCs](#h-iocs)
  + [YARA rules](#h-yara-rules)
* [External references](#h-external-references)

## Context

Over the past few years, cybercriminals have **increasingly used the drive-by download technique to distribute malware via user web browsing**. This technique mostly involves SEO-poisoning, malvertising, and code injection into compromised websites to trick users into **downloading fake software installers or browser updates**.

The drive-by download technique is commonly used by multiple intrusion sets to distribute loaders (*e.g.* FakeBat, BatLoader), botnets (*e.g.* IcedID, [PikaBot](https://blog.sekoia.io/pikabot-a-guide-to-its-deep-secrets-and-operations/)), infostealers (*e.g.* Vidar, Lumma, Redline), post-exploitation frameworks (*e.g.* [CobaltStrike](https://blog.sekoia.io/hunting-and-detecting-cobalt-strike/), Sliver) and RATs (*e.g.* NetSupport), to name but a few. From our observations, some of these attacks were conducted by Initial Access Brokers (IABs) and have led to the deployment of ransomware (BlackCat, Royal).

During the first semester of 2024, **FakeBat** (aka EugenLoader, PaykLoader) was **one of the most widespread loaders using the drive-by download technique**. FakeBat primarily aims to download and execute the next-stage payload, such as IcedID, Lumma, Redline, SmokeLoader, SectopRAT and Ursnif.

In 2024, Sekoia Threat Detection & Research (TDR) team discovered multiple FakeBat distribution campaigns. These campaigns typically leverage landing pages impersonating legitimate software and are spread via malvertising, fake web browser updates on compromised websites, and social engineering schemes on social networks. Additionally, TDR closely monitored the FakeBat C2 infrastructure to identify new C2 servers and changes in FakeBat communications.

This FLINT aims to **present the activities of the FakeBat operators** on cybercrime forums, an **analysis of previously undocumented campaigns** distributing FakeBat, **technical details on its distribution campaigns and related C2 infrastructures**. Additionally, TDR analysts share Indicators of Compromise (IoCs), YARA rules and tracking heuristics to monitor the FakeBat distribution and C2 infrastructures.

## Interactions on cybercrime forums

### FakeBat loader

#### Emergence of FakeBat

Since at least December 2022, the threat actor *Eugenfest* (aka *Payk\_34*)has sold FakeBat as Loader-as-a-Service on the Exploit forum.

As advertised by its representative FakeBat is a **loader malware in MSI format** that offers “several anti-detection features, such as bypassing the Unwanted Software Policy of Google and Windows Defender alerts and being protected from VirusTotal”.

By purchasing this service, FakeBat customers have access to an administration panel that allows them to:

* generate FakeBat builds;
* manage the distributed payloads;
* monitor the installations related to the payload distribution.

Notably, the Malware-as-a-Service (MaaS) provides build templates to trojanise legitimate software, thus luring potential victims into executing FakeBat.

The FakeBat administration panel contains information related to the infected host, including the IP address, country, OS, web browser, mimicked software, and installation status. Customers can also write comments for each bot.

#### Second wave of advertising

In September 2023, FakeBat operators launched a new advertising campaign on cybercrime forums and Telegram channels, **introducing MSIX as a new format for their malware builds**. Moreover, to bypass Microsoft SmartScreen security features, they added a digital signature to the FakeBat installer with a valid certificate. The signature is included in the MSIX format and is available as an extra in the MSI format.

![FakeBat (aka Payk Loader) advertisement on the XSS forum, published by Payk_34 on 2 September 2023](data:image/svg+xml...)![FakeBat (aka Payk Loader) advertisement on the XSS forum, published by Payk_34 on 2 September 2023](https://lh7-eu.googleusercontent.com/docsz/AD_4nXdiEsOJpsSCHXTEjxtADGg9akrpLMlCeFxzu2Sjji-prb0Fu2syX1392CPW-45GfsZhlTdUfrHLfppbFQtIVR1mThIW7pjI16p3YXxkt_2ngUMIaeepbd8RB88hL_UBHFk_5pWTUomagW51a8Z6DQyhgNZb?key=ZNnosQF9f1eRZ_KT1Fiksg)

*Figure 1. FakeBat (aka Payk Loader) advertisement on the XSS forum, published by Payk\_34 on 2 September 2023*

It is noteworthy that the threat actor started using the new handle *Payk\_34* on the XSS forum and Telegram. *Payk\_34* is allegedly the administrator of the “Payk Loader”...