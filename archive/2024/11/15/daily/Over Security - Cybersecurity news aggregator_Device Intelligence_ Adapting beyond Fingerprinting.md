---
title: Device Intelligence: Adapting beyond Fingerprinting
url: https://www.threatfabric.com/blogs/device-intelligence-adapting-beyond-fingerprinting
source: Over Security - Cybersecurity news aggregator
date: 2024-11-15
fetch_date: 2025-10-06T19:21:32.738078
---

# Device Intelligence: Adapting beyond Fingerprinting

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

Blog

## Device Intelligence: Adapting beyond Fingerprinting

14 November 2024

![](https://www.threatfabric.com/hubfs/TF_HyenaHologram.jpg)

### Jump to

## What is device intelligence and why is it important in today’s threat landscape?

With the rise in scams, social engineering and device takeover fraud, it is no longer enough to trust a device. Devices can be taken over by fraudsters using remote access tools and malware. “Good” users can be socially engineered to make transactions from their trusted device. Therefore, it is paramount to go beyond device identification and towards device risk analysis to understand the fraud risk of a digital banking session.

ThreatFabric defines device intelligence as: "*The real-time analysis of device attributes, such as risky software and hardware configurations, to calculate the likelihood that a device is being used as part of a fraudulent digital banking session."*

Many providers use the terms device intelligence and device fingerprinting interchangeably. As we will outline below, device fingerprinting is one of the key capabilities of any device intelligence tool, but device intelligence looks beyond device identification and considers the security posture of the device itself.

In the article below, we outline (1) what the essential ingredients of a best-in-class device intelligence tool are and (2) why device intelligence is a key tool in every financial institution’s anti-fraud technology stack

## What capabilities underpin a best-in-class device intelligence tool?

### Device fingerprinting

Device fingerprinting is the process of generating unique identifiers for individual devices based on various attributes and configurations.

First-generation device fingerprinting tools rely solely on static identifiers such as browser type, operating system, colour resolution etc. Best-in-class tools use a combination of static datapoints and dynamic datapoints, such as IP intelligence, installed apps and paired devices, to form a fingerprint that can persist app restart, device restart, app uninstall and re-install. These tools use deep learning to allow features with high uniqueness & user variance to carry more weight in fingerprint generation.

### Location intelligence

Location intelligence goes beyond gathering IP information and converts raw locational data into risk factors by considering:

* **Location familiarity:** Has the user transacted from this location before? If so, how often and when was the last session?
* **Location plausibility:** How far is the distance from the last genuine session? Could the user plausibly travel this far in the time between sessions?
* **Location reputation:** Is a VPN or TOR in use? Has this IP, ISP or ASN been used for fraud before?

Best-in-class tools have feature toggles to allow for different location data collection and data privacy strategies.

### Call intelligence

Digital banking users are rarely on live calls while making genuine transactions. ThreatFabric & industry data shows that only approximately 1% of genuine sessions contain a live call. Therefore, detecting a live call can be a powerful indicator of voice-based coaching / vishing.

First generation tools can detect the presence of a live call. Next-generation tools go further by analysing secondary level datapoints, such as call type (VOIP vs cellular) and duration, to further crystallise scam call risk and minimise false positives.

### Malware detection

ThreatFabric data shows that there has been a 94% increase in mobile malware families targeting financial apps in the past 3 years. Modern mobile malware families are equipped with sophisticated device takeover capabilities that make it very hard to detect fraud without specific malware detections.

First generation tools rely on hash-based detections that are easily circumvented by fraudsters. Next generation tools fuse together proactive threat intelligence and heuristic rules to accurately identify malicious apps without relying on hashes or behavioural biometrics alone.

### Remote access tool (RAT) detection

RATs have become a popular method fraudsters abuse as part of bank impersonation and tech support scams. After a RAT has been downloaded, a fraudster can either directly takeover the device and execute fraudulent transactions, or actively coach a genuine user into making a fraudulent transfer. In both cases, the fraud is executed from the trusted user’s device, making it difficult to detect with fingerprinting alone.

Best-in-class device intelligence tools can establish when a RAT (or screen sharing of any type) is actively being used during a banking session. Many customers with first-gen tools have noted the high false positive rate associated with RAT detection if the tool cannot differentiate between a dormant and active RAT.

### Device security posture assessment

There are various other device-related risk signals that can help anti-fraud teams establish whether a device is being used for malicious purposes.

Next generation device intelligence tools have multi-layered detections for jailbroken devices, rooted devices, emulators, bots, hooking frameworks, code injections and more. It is critical for providers to keep abreast of the latest Tactics, Techniques and Procedures (TTPs) that fraudsters and cybercriminals are using to exploit devices as static rulesets become obsolete as fraudsters evolve.

At ThreatFabric, we have a dedicated Mobile Threat Intelligence (MTI) team whose full-time role is to research, track, hunt, analyse and build detections for new and emerging fraudster tools.

## How are device intelligence signals used in anti-fraud programmes?

Risk signals and scores from ThreatFabric’s Fraud Risk Suite (FRS) SDK are ingested into in-house and third-party transaction monitoring solutions in real-time (hundreds of milliseconds) to make better informed payment risk decisioning. In contrast to device fingerprinting, device intelligence tools capture risk signals throughout the entire customer journey, allowing for continuous, dynamic risk profiling instead of point-in-time, static profiling.

Financial institutions typically use FRS signals as features in machine learning models or rulesets, as the institution will have a wider set of contextual data about the customer and transaction that is also essential for overall payment risk scoring.

Given the multiple capabilities of best-in-class device intelligence tools such as FRS, the signals can be used across multiple detection use cases, including but not limited to:

* Account Takeover (ATO)
* Vishing scams / Authorised Push Payment (APP) fraud
* Device Takeover (DTO) fraud via RAT
* Money mule identification
* Mobile malware fraud
* Application fraud
* Bot farms / bot fraud

 ![ATO - vishing](https://www.threatfabric.com/hs-fs/hubfs...