---
title: Ghost Tap: New cash-out tactic with NFC Relay
url: https://www.threatfabric.com/blogs/ghost-tap-new-cash-out-tactic-with-nfc-relay
source: Over Security - Cybersecurity news aggregator
date: 2024-11-21
fetch_date: 2025-10-06T19:20:04.892359
---

# Ghost Tap: New cash-out tactic with NFC Relay

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

## Ghost Tap: New cash-out tactic with NFC Relay

20 November 2024

![](https://www.threatfabric.com/hubfs/TF_GhostTap_LOGO.jpg)

### Jump to

## Threat actors are scaling the cash-outs

Cash-out tactics of fraudsters are of particular interest for financial institutions for obvious reasons – the ability to detect anomaly in the flow of the customer assets that is matching the known cash-out tactic allows to protect unsuspecting customer’s assets as well as detect money laundering schemes as a part of anti-fraud compliance.

Knowing that, fraudsters are always on the lookout for the new ways to cash-out the stolen funds, both to avoid detection based on the transactions monitoring as well as to ensure the stability and scalability of the cash-out process, staying anonymous while easily finding new mules.

During our recent investigations, ThreatFabric analysts came across a new cash-out tactic being actively used by the threat actors as well as promoted on underground forums. This report is dedicated to explaining this new tactic we called "Ghost Tap" used by threat actors to cash-out money having stolen credit card details linked to mobile payment services like Google Pay or Apple Pay and involving relaying of NFC traffic.

## New tactic in cash-out: Relaying NFC traffic

During the investigation, ThreatFabric analysts came across a post on one of the underground forums where a user was stating that they are able to “send my apple pay /google pay card from my phone to your phone for NFC operation”. Another user was mentioning that “There are also other people who offer a similar method, … transactions are made using the phone's built-in NFC reader”.

![image-png-Nov-12-2024-10-27-58-2276-AM](https://www.threatfabric.com/hs-fs/hubfs/image-png-Nov-12-2024-10-27-58-2276-AM.png?width=726&height=86&name=image-png-Nov-12-2024-10-27-58-2276-AM.png)

*A post on underground forum*

In these cases, the actors were referring to some way to cash-out money from stolen cards that were linked to mobile payment systems like Apple Pay or Google Pay. To link the card to a new device with Apple Pay or Google Pay, the cybercriminals would need to obtain OTP from the bank (likely sent via SMS). The most plausible scenarios for that are:

1. Victim has a mobile banking malware installed on the device. Credit card details are stolen with the help of overlay attack or keylogging capabilities. OTP code can be further intercepted by the malware (from SMS or push-notification) and sent to attackers successfully confirming the link of the card to mobile payment system.
2. Victim submits the credentials of the card on the phishing website, which further requests OTP (thus, again giving the attackers all the necessary details).

At this point the cybercriminals have the stolen card linked to their device, which they can further use and spend rather significant amounts at offline retailers.

However, it obviously poses significant risk for the actors – if they use the device with the stolen card directly, law enforcement can further identify them during the investigation after the report of the owner of the card. Moreover, if the actors are to “process” significant number of cards, they are unable to do it quickly, meanwhile increasing the risk of the cards being blocked by the issuer. This raises a challenge in front of the actors to scale the cash-out as well as remain anonymous during this final stage of the fraud execution.

As a result, threat actors adopted the tactic that we reported in the private report for customers about **NFSkate** in April 2024 (also reported in August by [ESET as NGate](https://www.welivesecurity.com/en/eset-research/ngate-android-malware-relays-nfc-traffic-to-steal-cash/)): using publicly available tool NFCGate they relay the NFC traffic from one cybercriminal (attacker) to another (mule) and do it on a scalable manner, effectively cashing out money.

### Ghost Tap Concept

Cybercriminals are increasingly leveraging legitimate research tools for malicious purposes. A prime example is NFCGate, developed at TU Darmstadt, which was originally designed for research purposes but has been weaponized by threat actors. Notably, the NFSkate malware family is also based on this project, highlighting the growing trend of malicious actors exploiting academic research for illicit gains.

This time cybercriminals found another application of this tool: cashing-out the money. Cybercriminals can establish a relay between a device with stolen card and POS terminal at a retailer, staying anonymous and performing cash-outs on a larger scale. The cybercriminal with stolen card can be far away from the location (even different country) where the card will be used as well as use the same card in multiple locations within short period of time.

In the following explanation we use “**Attacker**” referring to the cybercriminal possessing the stolen card details and the device with enrolled stolen card and “**Mule**” as a person that interacts with POS and buys goods at offline retailers.

The prerequisites for the tactic to be executed are rather simple: a mobile device with NFC with stolen card linked to mobile payment system (could be iOS or Android device), two devices with NFCGate installed and a server that is setup to relay the traffic.

The list **does not include any expensive or closed proprietary resources**, everything can be easily obtained by the cybercriminals acting as attackers and, more importantly, easily obtained by the criminals acting as mules as no specific knowledge/skills are needed.

This approach allows the cybercriminals having the ability to link cards to mobile payment services to:

* Buy goods (i.e. gift cards) at offline retailers while staying anonymous and **being far away from the location** of the store.
* Scale the fraud execution by enabling **multiple mules** at different locations to buy goods **within short period of time.**

The following picture shows the scheme of interactions:

![MTI_NFC_relay_flow](https://www.threatfabric.com/hs-fs/hubfs/MTI_NFC_relay_flow.png?width=2560&height=1440&name=MTI_NFC_relay_flow.png)

### NFC-based attacks become popular

As it was mentioned previously in the blog, cybercriminals pay more and more attention to NFC-based attacks. Mobile malware like NFSkate, attacks with NFCGate-based tools on physical cards, relaying NFC traffic between device with linked stolen card and “mule” at POS – all these are recent examples of rising interest of cybercriminals to such attacks.

We suspect that the evolution of networks with increasing speed of communication together with a lack of proper time-based detection on ATM/POS terminals made these attacks possible, where the actual devices with cards are physically located far away from the place where transaction is performe...