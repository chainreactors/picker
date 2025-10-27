---
title: SuperCard X: exposing a Chinese-speaker MaaS for NFC Relay fraud operation | Cleafy
url: https://www.cleafy.com/cleafy-labs/supercardx-exposing-chinese-speaker-maas-for-nfc-relay-fraud-operation
source: Over Security - Cybersecurity news aggregator
date: 2025-04-19
fetch_date: 2025-10-06T22:07:26.046547
---

# SuperCard X: exposing a Chinese-speaker MaaS for NFC Relay fraud operation | Cleafy

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

Malware

Android

NFC

# SuperCard X: exposing a Chinese-speaker MaaS for NFC Relay fraud operation

###### Published:

###### 18/4/25

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDFâ¨ guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key points

This report details a newly identified and active fraud campaign, highlighting the emergence of sophisticated mobile malware leveraging innovative techniques:

* **SuperCard X Malware**: A novel Android malware offered through a Malware-as-a-Service (MaaS) model, enabling NFC relay attacks for fraudulent cash-outs.
* **Evolving Threat Landscape**: Demonstrates the continuous advancement of mobile malware in the financial sector, with NFC relay representing a significant new capability.
* **Combined Attack Vectors**: Employs a multi-stage approach combining social engineering (via smishing and phone calls), malicious application installation, and NFC data interception for highly effective fraud.
* **Low Detection Rate**: SuperCard X currently exhibits a low detection rate among antivirus solutions due to its focused functionality and minimalistic permission model.**â**
* **Broad Target Scope**: The fraud scheme targets customers of banking institutions and card issuers, aiming to compromise payment card data.

### Executive Summary

The Cleafy Threat Intelligence team has identified a new and sophisticated Android malware campaign, dubbed **'SuperCard Xâ**. This campaign employs a novel NFC-relay technique, enabling Threat Actors (TAs) to fraudulently authorize **Point-of-Sale (POS)** payments and **Automated Teller Machine (ATM)** withdrawals by intercepting and relaying NFC communications from compromised devices. The malware is distributed through Social Engineering tactics, deceiving victims into installing the malicious application and subsequently âtappingâ their payment cards on their infected phones.Â

Preliminary analysis suggests that TAs are leveraging a **Chinese-speaking Malware-as-a-Service (MaaS)** platform promoted as SuperCard X. This malware exhibits significant code overlap with the previously documented NGate malware discovered by ESET in 2024.Â

**This novel campaign introduces a significant financial risk** that extends beyond the conventional targets of banking institutions to affect payment providers and credit card issuers directly. The innovative combination of malware and NFC relay empowers attackers to perform fraudulent cash-outs with debit and credit cards. This method demonstrates high efficacy, especially when targeting contactless ATM withdrawals.

### Introduction

The mobile threat landscape, particularly within the **financial** **sector**, is marked by a relentless evolution towards greater sophistication and scalability. As established attack vectors mature, novel trends emerge, introducing advanced functionalities that redefine the threat paradigm. A significant new trend challenging traditional banking institutions, payment institutions, and card issuers is the abuse of **Near-Field Communication (NFC) technology**. TAs increasingly exploit NFC capabilities to capture and relay sensitive data exchanged via this protocol. This emerging threat is not confined to a single region; recent reports, including those covered by [KrebsOnSecurity](https://krebsonsecurity.com/2025/03/arrests-in-tap-to-pay-scheme-powered-by-phishing/), detail similar NFC-enabled fraud schemes in the US, leading to arrests linked to **Chinese actors**.

This article delves into a particularly active fraud campaign targeting **Italy**, which we assess to be associated with a previously undocumented Android malware offered through a Malware-as-a-Service (MaaS) model promoted as **'SuperCard X'**. The nature of MaaS enables multiple affiliates to operate locally within their own regions or areas of specific interest. Consequently, we cannot exclude the possibility of similar or related campaigns being active in other regions globally.Â

Our analysis will provide a comprehensive breakdown of the group's techniques, encompassing both **sophisticated social engineering tactics** and the deployment of this novel Android malware. We will detail the entire fraud lifecycle, from the initial phishing campaigns designed to deliver SuperCard X to the eventual cash-out operations exploiting the relayed NFC data. Given the potential for widespread impact due to the **MaaS distribution model**, we strongly recommend that banking institutions and card issuers maintain heightened vigilance regarding these emerging attack scenarios.

### Dissecting the Fraud Scenario

The execution of this sophisticated fraud campaign unfolds through a series of well-orchestrated steps initiated by a targeted social engineering strategy. The attack typically starts with deceptive messages, often delivered via **SMS or WhatsApp**, designed to instil a sense of urgency or alarm in the recipient. These messages commonly impersonate bank security alerts, notifying users of a suspicious outgoing payment. The message prompts potential victims to call a specific number to dispute the transaction. This initial contact establishes a **Telephone-Oriented Attack Delivery (TOAD) scenario**, where TAs leverage direct phone conversations to manipulate their targets.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/680107938cc6819a194db4a0_fig.1.png)

Figure 1: Example of SMS messages

During the ensuing phone call, the TAs employ persuasive social engineering tactics to guide victims through actions that ultimately compromise their payment card details. This multi-stage manipulation involves:

* **PIN Elicitation**: Exploiting the victim's potential anxiety regarding the fraudulent transaction, the TAs convince them to "reset" or "verify" their card. Since victims often do not recall their PIN immediately, the attackers guide them through their mobile banking application to retrieve this sensitive information.
* **Card Limit Removal**: Once they have gained the victim's trust and potentially their banking app access (through verbal guidance), the TAs instruct the victim to navigate to the card settings within their banking app and remove any existing spending limits on their debit or credit card. This crucial step maximizes the potential for fraudulent cash-out.**â**
* **Malicious Application Installation**: Subsequently, the TAs persuade the victim to install a seemingly in...