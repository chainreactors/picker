---
title: Latrodectus BackConnect
url: https://www.netresec.com/?page=Blog&month=2025-12&post=Latrodectus-BackConnect
source: NETRESEC Network Security Blog
date: 2025-12-10
fetch_date: 2025-12-11T03:24:56.301334
---

# Latrodectus BackConnect

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Wednesday, 10 December 2025 13:00:00 (UTC/GMT)

## [Latrodectus BackConnect](/?page=Blog&month=2025-12&post=Latrodectus-BackConnect)

![Latrodectus BackConnect spider](https://media.netresec.com/images/Latrodectus-BackConnect_2000x2338.webp)

I recently learned that the great folks from [The DFIR Report](https://thedfirreport.com) have done a writeup covering the Latrodectus backdoor. Their report is titled [From a Single Click: How Lunar Spider Enabled a Near Two-Month Intrusion](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/).

I found it particularly interesting that the threat actors used [Latrodectus](https://malpedia.caad.fkie.fraunhofer.de/details/win.latrodectus) to drop a BackConnect RAT to the victim PC. I have verified that this RAT’s Command and Control (C2) traffic is using the exact same [BackConnect C2 protocol](https://netresec.com/?b=22A38f9) as what would previously be seen in [IcedID](https://malpedia.caad.fkie.fraunhofer.de/details/win.icedid) and [QakBot](https://malpedia.caad.fkie.fraunhofer.de/details/win.qakbot) infections.

This BackConnect RAT supports features such as:

* Reverse VNC ([Keyhole](https://malpedia.caad.fkie.fraunhofer.de/details/win.keyhole))
* Reverse SOCKS
* Reverse shell (cmd.exe or powershell)
* File manager

**NetworkMiner**

I immediately recognized the [BackConnect protocol](https://netresec.com/?b=22A38f9) because I spent many hours reverse engineering that protocol back in 2022. I later spent even more time building a parser for it in 2023. This BackConnect parser was eventually published as part of the [NetworkMiner 2.8.1 release](https://netresec.com/?b=23A41e6).

I was happy to see that NetworkMiner could parse the BackConnect traffic in The DFIR Report’s [Latrodectus case](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/) (#TB28761).

![Images extracted from BackConnect traffic by NetworkMiner Professional 3.1](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Images_BackConnect_523x655.webp)

The only caveat was that I had to use [NetworkMiner Professional](https://www.netresec.com/?page=BuyNetworkMiner), because it has a built-in protocol detection feature that detects the BackConnect traffic and applies the correct parser. That feature isn’t included in the free version of NetworkMiner, which is why it doesn’t know what to do with this strange looking TCP traffic to port 443.

Below are some screenshots extracted with NetworkMiner Professional from the BackConnect reverse VNC traffic.

![Keyhole reverse VNC session](https://media.netresec.com/images/VNC_58D23BBC_240513142808.jpg)

*Image: Keyhole reverse VNC session*

![Attacker fails to inspect the file ad_users.txt](https://media.netresec.com/images/VNC_58D222F7_240513125919_REDACTED.webp)

*Image: Attacker fails to inspect ad\_users.txt*

![Attacker launches additional malware with rundll](https://media.netresec.com/images/VNC_58D23D61_240514162001_REDACTED.webp)

*Image: Attacker launches additional malware with rundll*

![Task Manager in BackConnect VNC session](https://media.netresec.com/images/VNC_58D23755_240514163635.jpg)

The reverse VNC activity spanned a period of over two weeks, which is very impressive for this type of intrusion data set. The threat actors used the BackConnect reverse VNC service to access the machine several times during this period, for example to steal credentials and install additional malware.

A histogram of interactive BackConnect events, including reverse shell, VNC and file manager sessions, show that the majority of the work was carried out around 12pm UTC.

![BackConnect working hours histogram](https://media.netresec.com/images/BackConnect-working-hours_943x530.webp)

**Keylog of the Attacker**

Not only does the BackConnect network traffic from the intrusion allow us to extract screenshots from the VNC traffic. NetworkMiner also extracts the attacker’s hands-on keyboard activity.

![Keys pressed by attacker in BackConnect VNC session](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Parameters_BackConnect_Key-pressed_REDACTED_524x675.webp)

The keylog shows that the attacker accidentally typed “cd //” instead of “cd ..” at one point. Here’s the screenshot that NetworkMiner extracted from the reverse VNC traffic after the attacker had corrected the typo.

![Command shell in VNC session](https://media.netresec.com/images/VNC_58D23D61_240514161620.jpg)

This typo might seem a bit odd, but if you compare the US keyboard layout with the Russian Cyrillic one, then you’ll see that the dot key on the Cyrillic keyboard is at the same place as slash on the US keyboard.

![Russian windows keyboard layout aka JCUKEN for Russian with dot character marked](https://media.netresec.com/images/KB_Russian_1280x427.webp)

*Image: Russian Windows keyboard layout [from Wikipedia](https://en.wikipedia.org/wiki/File%3AKB_Russian.svg)*

This reminds me of another BackConnect infection, captured by [Brad Duncan](https://infosec.exchange/%40malware_traffic), which he named [IcedID (BokBot) infection with Keyhole VNC and Cobalt Strike](https://malware-traffic-analysis.net/2023/09/28/index.html). Here’s a screenshot that NetworkMiner extracted from the PCAP file shared by Brad:

![Attacker types фьфящт instead of amazon in BackConnect VNC session](https://media.netresec.com/images/VNC_C40394EC_230928155157.jpg)

The attacker can be seen typing “фьфящт” into the browser’s address bar in that VNC session. Фьфящт doesn’t mean anything in Russian, but the individual positions on the Russian keyboard corresponds to “amazon” on a standard Latin keyboard layout.

**Reverse Shell**

NetworkMiner also extracts commands from BackConnect reverse shell sessions.

![Shell commands from BackConnect session displayed in NetworkMiner Professional](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Parameters_BackConnect_Shell-command_REDACTED2_524x526.webp)

This screenshot shows that the attacker sent the following command to the reverse shell:

rundll32 C:\ProgramData\sys.dll,StartUp471

This command launched a [Cobalt Strike](https://malpedia.caad.fkie.fraunhofer.de/details/win.cobalt_strike) implant that connected to avtechupdate[.]com. Analysis of the Cobalt Strike C2 traffic is not in the scope for this blog post though, but the [original writeup](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/) for this lab contains additional details on the Cobalt Strike infection.

The attacker later issued another rundll command to launch another red-team/penetration testing tool, namely [Brute Ratel C4](https://malpedia.caad.fkie.fraunhofer.de/details/win.brute_ratel_c4).

rundll32 wscadminui.dll, wsca

This Brute Ratel backdoor connected to C2 servers on erbolsan[.]com and a few other domains (see IOC list). The DFIR Report’s [writeup](https://thedfirreport.com/2025/09/29/from-a-single-click-how-lunar-spider-enabled-a-near-two-month-intrusion/) contains additional information about that payload as well.

**About The DFIR Report**

The DFIR Report provide analysis of cyber intrusions, detailing the tactics, techniques, and procedures used by attackers. They share insights into various attacks, from initial access to execution, and offer private threat briefs and reports for organizations.

A lab containing Elastic or Splunk data from this infection can be purchased from [The DFIR Report’s store](https://dfirlabs.thedfirreport.com/store). Look for the lab titled “...