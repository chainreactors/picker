---
title: BingoMod: The new android RAT that steals money and wipes data
url: https://www.cleafy.com/cleafy-labs/bingomod-the-new-android-rat-that-steals-money-and-wipes-data
source: Over Security - Cybersecurity news aggregator
date: 2024-08-01
fetch_date: 2025-10-06T18:07:54.776236
---

# BingoMod: The new android RAT that steals money and wipes data

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

Android

On-Device

BingoMod

# BingoMod: The new android RAT that steals money and wipes data

###### Published:

###### 31/7/24

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDFâ¨ guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key Points

* At the end of May 2024, the Cleafy TIR team discovered and analysed a new Android RAT. Since we didn't find references to any known families, we decided to dub this new family **BingoMod**.
* The main goal of **BingoMod** is to initiate money transfers from the compromised devices via **Account Takeover** (ATO) using a well-known technique, called **On Device Fraud** (ODF). It aims to bypass bank countermeasures used to enforce usersâ identity verification and authentication, combined with behavioural detection techniques applied by banks to identify suspicious money transfers.
* After installation on the victimâs device, BingoMod leverages various permissions, including **Accessibility Services**, Â to quietly steal sensitive information, including credentials, SMS messages, and current account balances. In addition, the malware is equipped with active features that allow it to conduct overlay attacks and remotely access the compromised device using VNC-like functionality.
* After a successful fraudulent transfer, the **infected device is typically wiped**, removing any traces of BingoMod activity to hinder forensic investigations.
  Another interesting element that emerged during the BingoMod investigation is related to target devices, which include three languages: **English, Romanian**, and **Italian**.
* At the time of writing, BingoMod is in a development phase, where developers are experimenting with obfuscation techniques to **lower its detection rate** against AV solutions. From the whole sample collected, what has emerged is the will to try multiple anti-analysis configurations rather than making the malware more complex in terms of functionalities.
* According to the comments identified within the malware code, developers may be **Romanian** speakers.

### Executive Summary

At the end of May 2024, a new Android RAT appeared in Cleafyâs telemetries.
Due to the lack of information and the absence of a proper nomenclature for this malware family, we decided to dub it **BingoMod** to track it inside our Threat Intelligence taxonomy. This nomenclature is based on the malware's core component, known at an early stage as âChrUpdateâ but later renamed â**BingoMod**â.

â**BingoMod** belongs to the modern RAT generation of mobile malware, as its remote access capabilities allow Threat Actors (TAs) to conduct **Account Takeover** (ATO) directly from the infected device, thus exploiting the **On Device Fraud** (ODF) technique. This consolidation of this technique has already been seen recently by other banking trojans, such as [Medusa](https://www.cleafy.com/cleafy-labs/medusa-reborn-a-new-compact-variant-discovered), [Copybara](https://www.cleafy.com/cleafy-labs/on-device-fraud-on-the-rise-exposing-a-recent-copybara-fraud-campaign), and [Teabot](https://www.cleafy.com/cleafy-labs/teabot).

These techniques have several advantages: they require less skilled developers, expand the malware's target base to any bank, and bypass various behavioural detection countermeasures put in place by multiple banks and financial services. However, this advantage does not come for free, one of the drawbacks of this technique relies on a live operator that is required to insert and authorise a money transfer, which implicitly means lowering its scale factor.

BingoMod is similar to the [Brata](https://www.cleafy.com/cleafy-labs/how-brata-is-monitoring-your-bank-account)'s operation model in using device wiping after a successful fraudulent transfer. This self-destruction mechanism is designed to eradicate any trace of BingoMod's activity on the infected device, effectively hindering forensic analysis and making it more challenging for researchers to identify and attribute incidents. This tactic is relatively rare in the Android landscape, suggesting that the developers of BingoMod could be aware of Brata's methods and have incorporated them into their methodology.

Moreover, it's also worth mentioning that this sample is in its early stage of development, and it's still hard to predict which direction will be taken. However, the developersâ commitment to attempting obfuscation techniques underlines their intention to pursue a more opportunistic approach than a tailored one already seen in malware like [SharkBot](https://www.cleafy.com/cleafy-labs/sharkbot-a-new-generation-of-android-trojan-is-targeting-banks-in-europe) or Gustuff.

The following table represents a summary of the TTP behind BingoMod campaigns:

| First Evidence | May 2024 |
| --- | --- |
| State | Active (July 2024) |
| Affected Entities | Retail banking |
| Target OSs | Android Devices |
| Target Countries | IT |
| Infected Chain | Social Engineering (smishing) -> Side-loading |
| Fraud Scenario | On-Device Fraud (ODF) |
| Preferred Cash-Out | Instant/SEPA transfer |
| Amount handled (per transfer) | Up to 15K EUR |

â

All detected samples provided in the Appendix are **disguised** as legitimate **security** **tools** **to protect the device**.

![Figure 1 - Common decoy used by BingoMod](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/66a8c8ada7ecac8afebca4c7_66a8c6abb6d80a8a4e9184a3_F1.png)

Figure 1 - Common decoy used by BingoMod

### Technical Analysis

As previously mentioned, the malicious app is distributed via smishing and often masquerades as a legitimate antivirus application. Â After installation on the victim's device, BingoMod prompts the user to activate **Accessibility Service**s, disguising the request as necessary for the app to function correctly. If the user grants the requested permissions, the APK begins to **unpack** itself, executing its malicious payload. Once the operation is completed, the apps still lock out the user from the main screen to collect device information and set up the C2 communication channel.

![Figure 2 - Starting phase of BingoMod](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/66a8c8ada7ecac8afebca494_66a8c6eb66bcfea88f7e9f81_f2u%25CC%2580.png)

Figure 2 - Starting phase of BingoMod

After activation, BingoMod's **background** functions act, aiming to provide sensitive data to the actors behind the malware. In detail, two...