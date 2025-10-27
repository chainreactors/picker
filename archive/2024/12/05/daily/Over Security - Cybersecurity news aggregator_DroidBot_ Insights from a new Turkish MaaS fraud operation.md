---
title: DroidBot: Insights from a new Turkish MaaS fraud operation
url: https://www.cleafy.com/cleafy-labs/droidbot-insights-from-a-new-turkish-maas-fraud-operation
source: Over Security - Cybersecurity news aggregator
date: 2024-12-05
fetch_date: 2025-10-06T19:41:10.347805
---

# DroidBot: Insights from a new Turkish MaaS fraud operation

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

On-Device

Trojan

DroidBot

# DroidBot: Insights from a new Turkish MaaS fraud operation

###### Published:

###### 4/12/24

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDFâ¨ guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key Points

* In late October 2024, the Cleafy TIR team discovered and analysed a new Android Remote Access Trojan (RAT). Upon investigation, traces of this threat were found dating back to June 2024. However, as of this writing, no connections to any known malware families have been identified. Consequently, the team has classified this new threat under the name **DroidBot**, based on a domain name leveraged by this malware.
* DroidBot is a modern RAT that combines hidden VNC and overlay attack techniques with spyware-like capabilities, such as keylogging and user interface monitoring. Moreover, it leverages dual-channel communication, transmitting outbound data through MQTT and receiving inbound commands via HTTPS, providing enhanced operation flexibility and resilience.
* At the time of writing, DroidBot **targets 77 distinct entities**, including banking institutions, cryptocurrency exchanges, and national organisations. Active campaigns have been observed in countries such as the **United Kingdom**, **Italy**, **France**, **Spain**, and **Portugal**, indicating a potential expansion into **Latin** **America**.
  Inconsistencies observed across multiple samples indicate that this malware is still under active development. These inconsistencies include placeholder functions, such as root checks, different levels of obfuscation, and multi-stage unpacking. Such variations suggest ongoing efforts to enhance the malwareâs effectiveness and tailor it to specific environments.
* The information retrieved within malware samples (e.g., debug strings, configuration files, etc.) makes us assume that most of its developers are Turkish speakers. This observation reflects, at least partially, the efforts to adapt tactics for broader geographical impact.

### Executive Summary

DroidBot is an advanced Android Remote Access Trojan (RAT) that combines classic hidden VNC and overlay capabilities with features often associated with spyware. It includes a keylogger and monitoring routines that enable the interception of user interactions, making it a powerful tool for surveillance and credential theft. A distinctive characteristic of DroidBot is its dual-channel communication mechanism: outbound data from infected devices is transmitted using the MQTT protocol, while inbound commands, such as overlay target specifications, are received over HTTPS. This separation enhances its operational flexibility and resilience.
At the time of analysis, **77 distinct targets** have been identified, including banking institutions, cryptocurrency exchanges, and national organisations, underscoring its potential for widespread impact. Notably, the threat actor behind DroidBot has been linked to Turkey, reflecting a broader trend of adapting tactics and geographical focus.

Analysis of DroidBot samples has also revealed its **Malware-as-a-Service (MaaS)** infrastructure, with **17 distinct affiliate groups** identified, each assigned unique identifiers. Interestingly, multiple affiliates were found to be communicating over the same MQTT server, suggesting that some groups may collaborate or participate in demonstration sessions showcasing the malwareâs capabilities.

Moreover, DroidBot appears to be under active development. Some functions, such as root checks, exist as placeholders and are not yet properly implemented, while other features vary between samples (e.g., obfuscation, emulator checks, multi-stage unpacking). These inconsistencies suggest ongoing refinement to enhance functionality or adapt to specific environments. Despite these developmental signs, the malware has already demonstrated its potential, successfully targeting users in the **United** **Kingdom**, **Italy**, **France**, **Spain**, and **Portugal**, with indications of expansion into linguistically similar Latin American regions.
The combination of advanced surveillance features, dual-channel communication, a diverse target list, and an active MaaS infrastructure highlights DroidBotâs sophistication and adaptability. As it evolves, this malware poses an escalating threat to financial institutions, government entities, and other high-value targets across multiple regions.

The following table represents a summary of the TTP behind DroidBot campaigns:

| First Evidence | Mid-2024 |
| --- | --- |
| State | Active |
| Affected Entities | Retail banking |
| Target OSs | Android |
| Target Countries | DE, FR, IT, TK, UK, ES, PT |
| Infected Chain | Side-loading via Social Engineering |
| Fraud Scenario | On-Device Fraud (ODF) |
| Preferred Cash-Out | Data not available |
| Amount handled (per transfer) | Data not available |

### Technical Analysis

### Malicious App Overview

To lure victims into downloading and installing DroidBot, the TAs leverage common decoys frequently observed in banking malware distribution campaigns. In this case, the malware is disguised as generic security applications, Google services, or popular banking apps.

![Figure 1 - Common decoy used in DroidBot campaigns](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/674ef2ec9c5dda0b347b3dac_674ef140838377589424cbae_f1.png)

Figure 1 - Common decoy used in DroidBot campaigns

Like most modern Android banking malware, DroidBot relies heavily on abusing Accessibility Services to carry out its malicious functions. These services are typically requested during the initial stages of installation, as shown in the Figure above. DroidBot appears to have been developed using the B4A framework, a popular framework for native Android applications. Itâs important to note that B4A Â is widely used in malware developed by Brazilian TAs, such as the [Brata](https://www.cleafy.com/cleafy-labs/brata-is-evolving-into-an-advanced-persistent-threat) family and its known variant [CopyBara](https://www.cleafy.com/cleafy-labs/on-device-fraud-on-the-rise-exposing-a-recent-copybara-fraud-campaign).

DroidBot offers a range of functionalities commonly found in modern Android banking malware, including:

* **SMS Interception**: The malware monitors incoming SMS messages, often used by financial institutions to deliver transaction authentication numbers (TANs), allowing attackers t...