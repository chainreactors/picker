---
title: Three Lazarus RATs coming for your cheese
url: https://blog.fox-it.com/2025/09/01/three-lazarus-rats-coming-for-your-cheese/
source: Fox-IT International blog
date: 2025-09-02
fetch_date: 2025-10-02T19:30:36.284031
---

# Three Lazarus RATs coming for your cheese

[Skip to content](#content)

[![Fox-IT International blog](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/06/Fox-logo-for-wordpress-blog-2.png?fit=180%2C49&ssl=1)](https://blog.fox-it.com/)

[Fox-IT International blog](https://blog.fox-it.com/)

News and opinions from Fox-IT

Menu

* [Home](http://blog.fox-it.com/)
* [Archive](https://blog.fox-it.com/archive/)
* [Back to Fox-IT](http://www.fox-it.com)

# Three Lazarus RATs coming for your cheese

[Fox-SRT](https://blog.fox-it.com/author/foxsrt/ "Posts by Fox-SRT")

[Threat Intelligence](https://blog.fox-it.com/category/threat-intelligence/)

September 1, 2025September 21, 2025
22 Minutes

**Authors:** Yun Zheng Hu and Mick Koomen

[![A Telegram from Pyongyang](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/09/telegram-pyongyang2.jpg?resize=800%2C534&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/09/telegram-pyongyang2.jpg?ssl=1)

# Introduction

In the past few years, Fox-IT and NCC Group have conducted multiple incident response cases involving a Lazarus subgroup that specifically targets organizations in the financial and cryptocurrency sector. This Lazarus subgroup overlaps with activity linked to AppleJeus[1](#c9cc8db3-b181-4f57-81f9-cde8a0eee97f), Citrine Sleet[2](#8f87a1f0-2bb4-4101-adcf-d36158b7c8d6), UNC4736[3](#3f04ffb1-c7ee-4001-b560-a5de67325da7), and Gleaming Pisces[4](#211f8321-260b-4945-a21e-18e15a6c7786). This actor uses different remote access trojans (RATs) in their operations, known as PondRAT[5](#7ad29534-c69c-41ce-ae8e-99c32f0d11b3), ThemeForestRAT and RemotePE. In this article, we analyse and discuss these three.

First, we describe an incident response case from 2024, where we observed the three RATs. This gives insights into the tactics, techniques, and procedures (TTPs) of this actor. Then, we discuss PondRAT, ThemeForestRAT and RemotePE, respectively.

PondRAT received quite some attention last year, we give a brief overview of the malware and document other similarities between PondRAT and POOLRAT (also known as SimpleTea) that have not yet been publicly documented. Secondly, we discuss ThemeForestRAT, a RAT that has been in use for at least six years now, but has not yet been discussed publicly. These two malware families were used in conjunction, where PondRAT was on disk and ThemeForestRAT seemed to only run in memory.

Lastly, we briefly describe RemotePE, a more advanced RAT of this group. We found evidence that the actor cleaned up PondRAT and ThemeForestRAT artifacts and subsequently installed RemotePE, potentially signifying a next stage in the attack. We cannot directly link RemotePE to any public malware family at the time of this writing.

In all cases, the actor used social engineering as an initial access vector. In one case, we suspect a zero-day might have been used to achieve code execution on one of the victim’s machines. We think this highlights their advanced capabilities, and with their history of activity, also shows their determination.

# A Telegram from Pyongyang

In 2024, Fox-IT investigated an incident at an organisation in decentralized finance (DeFi). There, an employee’s machine was compromised through social engineering. From there, the actor performed discovery from inside the network using different RATs in combination with other tools, for example, to harvest credentials or proxy connections. Afterwards, the actor moved to a stealthier RAT, likely signifying a next stage in the attack.

In Figure 1, we provide an overview of the attack chain, where we highlight four phases of the attack:

1. **Social engineering:** the actor impersonates an existing employee of a trading company on Telegram and sets up a meeting with the victim, using fake meeting websites.
2. **Exploitation:** the victim machine gets compromised and shortly afterwards PondRAT is deployed. We are uncertain how the compromise was achieved, though we suspect a Chrome zero-day vulnerability was used.
3. **Discovery:** the actor uses various tooling to explore the victim network and observe daily activities.
4. **Next phase:** after three months, the actor removes PerfhLoader, PondRAT and ThemeForestRAT and deploys a more advanced RAT, which we named RemotePE.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/07/attack-overview.png?resize=800%2C751&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/07/attack-overview.png?ssl=1)

*Figure 1: Overview of the attack chain from a 2024 incident response case involving a Lazarus subgroup*

## Social Engineering

We found traces matching a social engineering technique previously described by SlowMist[6](#ddaabe0e-9972-4329-84fb-3533d5f5dbb6). This social engineering campaign targets employees of companies active in the cryptocurrency sector by posing as employees of investment institutions on Telegram.

This Lazarus subgroup uses fake Calendly and Picktime websites, including fake websites of the organisations they impersonate. We found traces of two impersonated employees of two different companies. We did not observe any domains linked to the “Access Restricted” trick as described by SlowMist. In Figure 2, you can see a Telegram message from the actor, impersonating an existing employee of a trading company. Looking up the impersonated person, showed that the person indeed worked at the trading company.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/07/image-1.png?resize=603%2C330&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/07/image-1.png?ssl=1)

*Figure 2: Lazarus subgroup impersonating an employee at a trading company interested in the cryptocurrency sector*

From the forensic data, we could not establish a clear initial access vector. We suspect a Chrome zero-day exploit was used. Although, we have no actual forensic data to back up this claim, we did notice changes in endpoint logging behaviour. Around the time of compromise, we noted a sudden decrease in the logging of the endpoint detection agent that was running on the machine. Later, Microsoft published a blogpost[7](#db20a81f-b3df-431b-96c6-045e9018a938), describing Citrine Sleet using a zero-day Chrome exploit to launch an evasive rootkit called FudModule[8](#710dfe8b-23d9-418f-9f87-b99a6a8730f7), which could explain this behaviour.

## Persistence with PerfhLoader

The actor leveraged the `SessionEnv` service for persistence. This existing Windows service is vulnerable to phantom DLL loading[9](#7381a5cf-a6fd-4457-a73f-7f4b4451ca1d). A custom `TSVIPSrv.dll` can be placed inside the `%SystemRoot%\System32\` directory, which `SessionEnv` will load upon startup. The actor placed its own loader in this directory, which we refer to as PerfhLoader. Persistence was ensured by making the service start automatically at reboot using the following command:

```
sc config sessionenv start=auto
```

The actor also modified the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SessionEnv\RequiredPrivileges` registry key by adding `SeDebugPrivilege` and `SeLoadDriverPrivilege` privileges. These elevated privileges enable loading kernel drivers, which can bypass or disable Endpoint Detection and Response (EDR) tools on the compromised system.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/07/sessionenv-perfhloader-overview.png?resize=800%2C221&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2025/07/sessionenv-perfhloader-overview.png?ssl=1)

*Figure 3: PerfhLoader loaded through SessionEnv service via Phantom DLL Loading which in turn loads PondRAT or POOLRAT*

In a case from 2020[10](#e0a93a5c-8e4c-44dd-8c3d-c34a30ce280a), this actor used the `IKEEXT` service for phantom DLL loading, writing PerfhLoader to the path `%SystemRoot%\System32\wlbsctrl.dll`. The vulnerable `VIAGLT64.SYS` kernel driver (CVE-2017-16237) was also used to gain `SYSTEM` privileges.

PerfhLoader is a simple loader that reads a file with a hardcoded filename (`perfh011.dat`) f...