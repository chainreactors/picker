---
title: A new TrickMo saga: from Banking Trojan to Victim's Data Leak
url: https://www.cleafy.com/cleafy-labs/a-new-trickmo-saga-from-banking-trojan-to-victims-data-leak
source: Over Security - Cybersecurity news aggregator
date: 2024-09-11
fetch_date: 2025-10-06T18:33:32.686857
---

# A new TrickMo saga: from Banking Trojan to Victim's Data Leak

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

Trojan

TrickMo

# A new TrickMo saga: from banking trojan to victim's data leak

###### Published:

###### 10/9/24

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDFâ¨ guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key Points

* In June, the Cleafy Threat Intelligence team identified an unclassified Android banking Trojan. Subsequent analyses revealed that the malware was a variant of **TrickMo**, albeit with newly incorporated anti-analysis mechanisms.
* The mechanisms include using **malformed** **ZIP** files in combination with **JSONPacker**. In addition, the application is installed through a Dropper app that shares the same anti-analysis mechanisms. These features are designed to evade detection and hinder cybersecurity professionals' efforts to analyse and mitigate the malware.
* The sample analysis allowed us to trace the structure of the command-and-control (C2) server and the organisation of **exfiltrated data**, highlighting critical endpoints used to store and manage stolen information. By gaining access to these endpoints, we uncovered **sensitive files**, including credentials and pictures, exfiltrated from infected devices.
* The new findings underscore an enhancement in the Threat Actorâs capabilities. Although TrickMo retains the typical functionalities of an Android banking Trojan, the data collected from infected devices could enable the attacker to undertake additional actions, compromising the victim on multiple levels.

### Introduction

Cleafyâs Threat Intelligence team observed an interesting Android malware sample in early June, initially classified as unknown. Further analyses revealed that the malware was a variant of the banking Trojan **TrickMo**, but with newly integrated anti-analysis features that complicated its classification.

TrickMo has a well-documented history of targeting Android devices. It emerged as part of TrickBotâs evolution, enabling TAs (Threat Actors) to expand the infection to the Android environment. The introduced anti-analysis mechanisms, which consist of a combination of different techniques known as **malformed ZIP, JSONPacker**, and **dropper** apps, highlight the malware's ever-evolving nature. The malware's purpose is to evade detection and hinder the efforts of cybersecurity professionals to analyse and mitigate this threat.

Nevertheless, the sample analysis also allowed us to trace the structure of the **command-and-control (C2)** server and the management of exfiltrated data, highlighting critical endpoints used to store the stolen information. We uncovered sensitive files, including credentials and pictures, exfiltrated from infected devices by gaining access to these endpoints.

What makes this discovery particularly noteworthy is the potential impact of the compromise on a victim user. A TA's actions with the exfiltrated data extend beyond banking fraud, potentially triggering identity theft scenarios. Moreover, as highlighted in this document, the exfiltrated data could be accessible to third parties without authentication, exposing the user to multiple attackers.

Ultimately, in the following sections, we will delve deeper into how a TrickMo infection can expose the user to multiple levels of risk, including banking fraud, identity theft, and data leakage.

### Historical Overview

CERT-Bund identified TrickMo for the first time in 2019. The malware was designed to facilitate financial fraud by intercepting **one-time passwords (OTPs)** and other **two-factor authentication (2FA)** mechanisms crucial for secure banking transactions. Its primary targets were banking applications across Europe, particularly in Germany.

The malware represents an evolution of the **TrickBot** groupâs malicious activities for the mobile domain. TrickBot, originally designed to target Windows systems, quickly became famous for its ability to steal banking credentials and other sensitive information. As cybersecurity defences improved, the TrickBot group developed TrickMo to target Android devices, leveraging and adapting the sophisticated techniques that made TrickBot successful. Over time, TrickMo has continually evolved, incorporating advanced obfuscation techniques and anti-analysis mechanisms to thwart detection and analysis efforts by cybersecurity professionals.

The malwareâs key features include:**â**

1. **Interception of One-Time Passwords (OTPs)**: it can intercept OTPs sent via SMS or generated by authenticator apps, allowing cybercriminals to bypass 2FA and authorise fraudulent transactions.
2. **Screen Recording and Keylogging:** The malware can record the victim's screen and capture keystrokes, providing attackers with sensitive information such as login credentials and PINs.
3. **Remote Control Capabilities:** TrickMo enables remote control of the infected device, allowing attackers to perform various actions, including initiating transactions and modifying account settings without the user's knowledge. With these capabilities, TrickMo can enable TAs to perform the [On-Device Fraud (ODF)](https://www.cleafy.com/insights/on-device-fraud-a-rising-threat-in-online-banking-fraud) scenario, one of the most dangerous types of banking fraud.
4. **Accessibility Service Abuse:** By exploiting Android's accessibility services, TrickMo can grant itself elevated permissions, manipulate user inputs, and capture data from other apps, making it particularly effective in targeting banking applications.
5. **Advanced Obfuscation Techniques:** TrickMo continually evolves its obfuscation methods to avoid detection. It uses sophisticated code-hiding techniques to make it difficult for security researchers to analyse the malware.
6. **Anti-Analysis Mechanisms:** TrickMo incorporates sophisticated methods to evade detection, including various techniques to detect and thwart virtualised environments and analysis tools.

The recent discovery of TrickMo's new anti-analysis mechanisms highlights the malware's continuous evolution. The following sections will discuss these techniques in detail, providing deeper insights into how TrickMo operates. Moreover, the analysed sample revealed characteristics of the malware that extend beyond the typical functionalities of a banking Trojan, possibly aligning with those of an infostealer.

### Malicious App Overview

The malicious app is distributed via a dropper disguised as the **Google Chrome** browser....