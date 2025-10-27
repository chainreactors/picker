---
title: SpyNote: Spyware with RAT capabilities targeting Financial Institutions
url: https://www.threatfabric.com/blogs/spynote-rat-targeting-financial-institutions.html
source: ThreatFabric
date: 2023-01-06
fetch_date: 2025-10-04T03:11:56.619292
---

# SpyNote: Spyware with RAT capabilities targeting Financial Institutions

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## SpyNote: Spyware with RAT capabilities targeting Financial Institutions

05 January 2023

![](https://www.threatfabric.com/hubfs/Threatfabric/images/spyware.png)

### Jump to

## Uncovering the Latest Developments in SpyNote

Android Spyware is one of the most common kinds of malware used by attackers to gain access to personal data and carry out fraud operations. Due to its capability to track a user’s location, examine web browsing behavioral patterns, and even steal sensitive information, such as passwords and credit card numbers, the threat level that Android Spyware poses to banking institutions and banking customers alike is comparable to Android Banking malware.

Spyware also has the potential to record phone calls, remotely manage the device, intercept SMS messages, and perform other tasks by using legitimate APIs and permissions that are intended to aid people.

In the last quarter of 2022, ThreatFabric researchers observed a large increase in volume for samples belonging to the SpyNote Malware family. This family, which is also known as **SpyMax**, is an unique and effective Spyware designed to secretly observe user activity on an Android device. The SpyNote malware can monitor, manage, and modify the device’s resources and features along with Remote access capabilities.

This spyware family has evolved over time, with the adoption of cutting-edge methods and technologies. SpyNote has several distinct variants: the most recent one, **SpyNote.C**, is routinely traced and tracked in day-to-day operations, and makes up for the majority of spyware samples ThreatFabric observed from October 2022.

One of the main differences between the first variants, **SpyNote.A** and **SpyNote.B**, and the latest one, **SpyNote.C**, is the campaign objective. SpyNote.C has been the first variant to openly target banking applications, impersonating a large number of reputable financial institutions like HSBC, Deutsche Bank, Kotak Bank, BurlaNubank, as well as others to well-known applications like WhatsApp, Facebook, and Google Play.

![spyNote-Bank-Impersonation](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/spyNote-Bank-Impersonation.png?width=1920&height=1080&name=spyNote-Bank-Impersonation.png)

In addition, we also observed that the attackers utilize more generic application masquerades, such as wallpaper apps, productivity apps, or gaming apps.

ThreatFabric researchers have identified that some of the **SpyNote.C** classified apps are being developed by lone actors and promoted as **CypherRat**. In this article we will discuss how developments on this actor’s project, which is advertised as both spyware and banking malware, are likely behind the surge in numbers that we observed in the last few months.

Other SpyNote.C campaigns were discovered while analyzing this Spyware family, impersonating System Notifications, Google Play Store. These campaigns ran together with the previously mentioned ones, with the one shown below sharing the same hosts used as C2.

![spyNote-discovered-campaign](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/spyNote-discovered-campaign.png?width=1920&height=1080&name=spyNote-discovered-campaign.png)

## SpyNote Alias CypherRat

The latest variant of this malware family, **SpyNote.C**, was further developed and sold to individual actors via Telegram channel by its developer, under the name **CypherRat**.

The threat actor offered CypherRat for sale utilizing the Sellix payment system, which uses Cryptocurrencies to prevent tracking. These sales ran from August 2021 until October 2022, accumulating more than 80 separate customers.

![TF_SpyNote_Sales](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/TF_SpyNote_Sales.png?width=1920&height=1080&name=TF_SpyNote_Sales.png)

In October 2022, the source code was made available as open-source via GitHub, after a leak and a few scamming incidents in hacking forums, where actors would impersonate the original threat actor to steal money from other criminals.

![cypherRat-Released-free](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/cypherRat-Released-free.png?width=1920&height=1080&name=cypherRat-Released-free.png)

Following the release of the source code, the number of samples counts have increase significantly, as we can observe in the statistical view using our ThreatFabric Intelligence data.

![TF-SpyNote-Statistical](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/TF-SpyNote-Statistical.png?width=1920&height=1080&name=TF-SpyNote-Statistical.png)

As you can see, the numbers are following a clear upward trend, which allowed ThreatFabric to collect more than 1100 **SpyNote/CypherRat** samples from October 2022; this number equals the amount of samples that we saw from the first test version of this variant collected in 2020.

During the course of our investigation, we discovered that the original creator had switched his focus to a new spyware project, **CraxsRat**, as a paid application with similar capabilities as the original project.

## Outstanding Capabilities means Exceptional Abilities

We were interested in the unique spyware skills that the **SpyNote.C** malware variant can do, which were identified in malicious financial apps with RAT capabilities around 2022. We have highlighted a few of these features, which can be used to **exfiltrate and utilize PII from online banking customers**.

Using the privileges requested in the screenshot below, This SpyNote variant can be used to track SMS messages, calls, videos, and audio recordings in addition to updating its version and even installing new applications.

![TF-SpyNote-accessibility](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/TF-SpyNote-accessibility.png?width=1920&height=1080&name=TF-SpyNote-accessibility.png)

The most recent versions of SpyNote are not only extremely powerful, but they also include a variety of security features, from simple string obfuscation to the use of commercial packers. This makes it much more difficult to analyze, making it a potent tool for threat actors.

![spynote-capabilities](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/spynote-capabilities.png?width=1920&height=1080&name=spynote-capabilities.png)

Below is a list of some of the SpyNote’s standout features:

* Ability to use the **Camera API** to record and send videos from the device’s camera to the Command and Control(C&C) center
* GPS and network location tracking information
* Stealing social media credentials (Facebook and Google).
* Uses **Accessibility (A11y)** to extract codes from **Google Authenticator**.
* Uses **Keylogging** powered by Accessibility services, to **steal banking credentials**.

### Accessibility Service

SpyNote uses Accessibility Services to make it difficult for users ...