---
title: Klopatra: exposing a new Android banking trojan operation with roots in Turkey | Cleafy LABS
url: https://www.cleafy.com/cleafy-labs/klopatra-exposing-a-new-android-banking-trojan-operation-with-roots-in-turkey
source: Over Security - Cybersecurity news aggregator
date: 2025-10-27
fetch_date: 2025-10-28T03:00:25.275108
---

# Klopatra: exposing a new Android banking trojan operation with roots in Turkey | Cleafy LABS

[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Discover Cleafy's Copilot

The first AI cyber-fraud agent

Read more

d](http://www.cleafy.com/eura)[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Discover Cleafy's Copilot

The first AI cyber-fraud agent

Read more

d](http://www.cleafy.com/eura)[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Discover Cleafy's Copilot

The first AI cyber-fraud agent

Read more

d](http://www.cleafy.com/eura)

[![Cleafy Logo](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/6031121f255fb120fa9d4d05_Cleafy-logo.svg)](/)

* [Platform](/platform)
* [Who it's for](/industries)
* [LABS](/threat-intelligence)
* Resources

  g

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS Reports](/labs)[Webinars](/webinars)[Events](/events)

  Resources

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS Reports](/labs)[Webinars](/webinars)[Events](/events)
* Company

  g

  [About us](/about-us)[Careers](/careers)[Partners](/partners)[Press](/press)[News](/news)

  Company

  [About us](/about-us)[Careers](/careers)[Partners](/partners)[Press](/press)[News](/news)
* [Support](https://support.cleafy.com/)
* [Get in touch](/get-in-touch)

[Support](https://support.cleafy.com/)[Get in touch](/get-in-touch)

Trojan

Android

Malware

# Klopatra: exposing a new Android banking trojan operation with roots in Turkey

###### Published:

###### 30/9/25

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDFâ¨ guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key points

* **New Sophisticated Threat Emerges:** In late August 2025, the Cleafy team discovered and analyzed **Klopatra**, a new Android Remote Access Trojan (RAT) that was previously unknown and had no apparent connections to known malware families.
* **Next-Generation Evasion:** Klopatra represents a significant evolution in mobile malware sophistication. It combines extensive use of **native libraries** with the integration of **Virbox**, a commercial-grade code protection suite, making it exceptionally difficult to detect and analyze.
* **Powerful Banking Trojan Capabilities:** At its core, Klopatra is a modern banking trojan that executes fraud through a powerful combination of **Hidden VNC** for complete remote device control and dynamic **Overlay attacks** for credential theft.
* **Active Campaigns in Europe:** At the time of analysis, two main botnets were identified, actively compromising **over 3,000 devices**, with campaigns heavily focused on financial targets in **Spain and Italy**.
* **Turkish-Speaking Threat Actor:** Extensive evidence from malware artifacts, C2 infrastructure data, and direct operator notes strongly indicates that Klopatra is developed and operated by a **Turkish-speaking criminal group**.
* **Agile Development and Private Operation:** Tracking over 40 distinct builds since March 2025 suggests a rapid development cycle. It's plausible that Klopatra is operating as a private botnet with limited affiliates and no public Malware-as-a-Service (MaaS) offering.

### Executive Summary

In late August 2025, Cleafy's Threat Intelligence team discovered **Klopatra**, a new, highly sophisticated Android malware currently used in active campaigns against financial institutions and their customers. The analysis identified two major botnets targeting users primarily in **Spain and Italy**, with the number of compromised devices already exceeding 3,000. Klopatra operates as a powerful banking trojan and Remote Access Trojan (RAT), allowing its operators to gain complete control over infected devices, steal sensitive credentials, and execute fraudulent transactions.

What elevates Klopatra above the typical mobile threat is its advanced architecture, built for stealth and resilience. The malware authors have integrated **Virbox**, a commercial-grade code protection tool rarely seen in the Android threat landscape. This, combined with a strategic shift of core functionalities from Java to **native libraries**, creates a formidable defensive layer. This design choice drastically reduces its visibility to traditional analysis frameworks and security solutions, applying extensive code obfuscation, anti-debugging mechanisms, and runtime integrity checks to hinder analysis.

This technical sophistication provides a clear footprint of the Threat Actor (TAs). Linguistic clues within the malware's code and intelligence gathered from the Command and Control (C2) infrastructure point decisively to a **Turkish-speaking origin**. This assessment is corroborated by operational notes left by the attackers themselves, revealing a cohesive and disciplined group managing the entire attack lifecycle, from development to monetization. Klopatra marks a significant step in the professionalization of mobile malware, demonstrating a clear trend of TAs adopting commercial-grade protections to maximize the lifespan and profitability of their operations.

### Introduction: The Rise of Klopatra

The mobile threat landscape is constantly evolving, with Android banking trojans becoming increasingly bold and technically advanced. However, most of these threats tend to follow recognizable patterns, reusing known code or techniques. Occasionally, a threat emerges that **deviates from the norm**, signaling a shift in adversary tactics and capabilities.

Klopatra is one such threat. Initially discovered by **Cleafy's automated detection systems** due to behavioral anomalies indicative of sophisticated activity, it quickly stood out as a previously undocumented malware. The analysis revealed no connections to existing malware families, prompting the team to classify it as a new family. The name "Klopatra" was derived from the name of a certificate embedded in one of the first analyzed samples (March 2025), an artifact left by the developers that provided the first clue to its identity.Â Â

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/68d54af1a63e147bc919e643_21694bf0.png)

Figure 1 - Certificate details

This report provides a comprehensive technical analysis of Klopatra. It explores its unique, **evasion-focused architecture**, its powerful capabilities as a financial fraud tool, the operational infrastructure supporting active campaigns, and the evidence that conclusively links the operation to a Turkish-speaking group. Through this analysis, Klopatra emerges as an **immediate threat to financial institutions** and a harbinger of **a new wave of mobile malware** adopting professional-grade obfuscation techniques to evade defenses, which has already been seen on other modern Android banking trojans.

### Anatomy of an Attack: From Lure to Full Control

Klopatra's effectiveness lies in a carefully orchestrated **infection chain**, which begins with social engineering and culminates in the complete takeover of the victim's device. Each stage is designed to overcome the defenses of the user and the Android operating system.

### The Dropper: A Trojan Horse Disguised as IPTV

The initial phase of the attack relies on a dropper application, a lure designed to appear legitimate and desirable. In this case, the dropper masquerades as an IPTV application called "Mobdro Pro IP TV + VPN," promising access to **high-quality television channels**. This choice is not accidental; pirated streaming applications are very popular, and users are often willing to install them from unofficial sources, bypassing the protections of the Google Play Store.

â

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/68d54af2a63e147bc919e660_15dfc449.png)

Figure 2 - Installation process

Once installed, the dropper application has a single purpose: to convince the user to g...