---
title: Hook: a new Ermac fork with RAT capabilities
url: https://www.threatfabric.com/blogs/hook-a-new-ermac-fork-with-rat-capabilities.html
source: Over Security - Cybersecurity news aggregator
date: 2023-01-20
fetch_date: 2025-10-04T04:24:12.713806
---

# Hook: a new Ermac fork with RAT capabilities

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

## Hook: a new Ermac fork with RAT capabilities

19 January 2023

![](https://www.threatfabric.com/hubfs/Threatfabric/images/cover.png)

### Jump to

## Introduction

The joint police operation that brought down the Cabassous network infrastructure in May 2022, together with the slow but steady disappearance of Anatsa from the threat landscape, left an open space in the Android banking malware market. This space was filled initially by Hydra, and in minor part by the latest variants of ExobotCompact (also known as Octo). These two malware families stood out from the rest due to their advanced features, specifically the ability to perform **Device Take-Over (DTO)**, by being able to remotely view and interact with the screen of the infected device.

In terms of volume, ThreatFabric observed only one other family which was comparable to these two: **Ermac**. [Discovered in September 2021](https://www.threatfabric.com/blogs/ermac-another-cerberus-reborn.html) by our researchers, this malware family is a spawn from the infamous Android Banker [Cerberus](https://www.threatfabric.com/blogs/cerberus-a-new-banking-trojan-from-the-underworld.html).

Among the three, Hydra is by far the most spread, and has been the Android banker of choice for threat actors ever since the takedown of Cabassous in May 2022. However, the other two malware families have kept their numbers quite high, with ExobotCompact/Octo being slightly lower due to its distribution mechanism of choice, dropper applications on Google Play Store, which usually creates less builds, but produce more infections per malicious sample.

![stats-1](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/stats-1.png?width=1920&height=1080&name=stats-1.png)

Ermac has been publicly rented by its actor **DukeEugene** for roughly one year and a half, with multiple actors being associated with the operations we had been observing. In March 2022, the actors behind this malware family tried to sell the botnet code on different hacking forums: from this point onwards, we started observing a rise in quantity of samples from Ermac, together with the appearance of different names and actors rebranding the bot and trying to rent it.

In this sphere of Ermac forks, ThreatFabric identified botnets such as **MetaDroid** and **OWL**, created from the Ermac source code and presenting minor differences. In the case of MetaDroid for example, the author removed the Locale check which was in place to ensure that the bot would not operate on devices from CIS countries.

![forks](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/forks.png?width=1920&height=1080&name=forks.png)

In both cases, we did not observe any major difference in implementation or operations from the original Ermac samples to warrant the creation of a new malware variant.

Recently however, we encountered a new fork, which spiked our interest. This new malware variant, clearly based on Ermac, introduced the capability to manipulate files on the devices file system, as well as create a remote session able to interact with the System’s UI.

Based on the malware’s panel, we named this malware variant **Hook**. Initially, while performing our analysis and investigations, this malware looked like another fork of the original Ermac, once again spawned from the sale of the original source code.

However, on the 12th of January, the original actor of Ermac, DukeEugene, published a post advertising a brand new banking malware, called “Hook”.

![advertisement](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/advertisement.png?width=1920&height=1080&name=advertisement.png)

From this thread, we can confidently say that Hook is the latest development of Ermac, and is developed and managed by its original author, DukeEugene.

## A malware created “from scratch”

The malware is advertised as “written from scratch”. This is debatable, as the **majority of the code base remains the one from Ermac**, including some commands in Russian expressing an unnecessary angst towards the world, which in our opinion would have not made the cut if a proper revision of the code had taken place.

![scratch](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/scratch.png?width=1920&height=1080&name=scratch.png)

It is true that this malware variant introduces quite a lot of modifications compared to its predecessor, but it is fairly obvious that this is just an update and improvement of the previous versions of Ermac. It is likely that the criminals, taking an approach which is is very effective in marketing strategies, decided to start a new brand with their latest product, instead of maintaining th existing one, which was associated mostly with operations regarding cryptowallets and Personal Identifiable Information (PII) exfiltration.

In the following section we will cover the improvements added in Hook. If you want to find out the main features of Ermac, please refer to our [previous blog about this family](https://www.threatfabric.com/blogs/ermac-another-cerberus-reborn.html).

## Capabilities

![capabilities](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/capabilities.png?width=1920&height=1080&name=capabilities.png)

### WebSocket communication

Hook uses the same encryption mechanisms used by Ermac in its communication with the C2 Server. The data is encrypted using AES-256-CBC with an hardcoded key, and then encoded in Base64. One modification that was done with this new malware variant, was the introduction of **WebSocket communication** in addition to the HTTP traffic used in the previous Ermac variants. The implementation relies on **Socket.IO**, which is an implementation over HTTP and WebSocket which enables real-time, bi-directional communication between web clients and servers.

After the malware is installed and successfully setup, the bot tries to contact its C2 server using normal HTTP traffic. The request triggers a response from the C2 in the following form

```
{
    "sid": "<alphanumeric_id>",
    "upgrades": ["websocket"],
    "pingInterval": 20000,
    "pingTimeout": 60000
}
```

This response triggers an upgrade to WebSocket traffic, which is how the bot communicates with its C2. If the value of “upgrades” is instead “polling”, the communication will be over HTTP. Over this channel, the bot registers with its server, sends the list of applications installed on the device and downloads the list of targets.

![targets](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/targets.png?width=1920&height=1080&name=targets.png)

The communication protocol remains the same as it was in previous versions, with periodic requests for commands sent by the bot and updates on the latest logs collected from the malware. The server uses this channel to issue commands, still ...