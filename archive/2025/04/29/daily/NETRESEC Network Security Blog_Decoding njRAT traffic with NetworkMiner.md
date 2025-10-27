---
title: Decoding njRAT traffic with NetworkMiner
url: https://www.netresec.com/?page=Blog&month=2025-04&post=Decoding-njRAT-traffic-with-NetworkMiner
source: NETRESEC Network Security Blog
date: 2025-04-29
fetch_date: 2025-10-06T22:09:02.181960
---

# Decoding njRAT traffic with NetworkMiner

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

Monday, 28 April 2025 06:00:00 (UTC/GMT)

## [Decoding njRAT traffic with NetworkMiner](/?page=Blog&month=2025-04&post=Decoding-njRAT-traffic-with-NetworkMiner)

I investigate network traffic from a [Triage sandbox execution of njRAT](https://tria.ge/231027-ma78jafc79/behavioral3) in this video. The analysis is performed using [NetworkMiner in Linux](https://netresec.com/?b=2542784) ([REMnux](https://remnux.org/) to be specific).

[![

](https://media.netresec.com/images/njRAT-NetworkMiner-REMnux_1280x660.png)](https://media.netresec.com/videos/njRAT-NetworkMiner-REMnux_1280x660.mp4)

**About njRAT / Bladabindi**

njRAT is a Remote Access Trojan (RAT) that can be used to remotely control a hacked computer. It has been around since 2013, but despite being over 10 years old it still remains one of the most popular backdoors used by malicious actors.
Anti virus vendors usually refer to njRAT as Bladabindi.

**njRAT Artefacts Extracted by NetworkMiner**

NetworkMiner has a built-in parser for the njRAT Command-and-Control (C2) protocol. This njRAT parser kicks in whenever there is traffic to a well-known njRAT port, such as TCP 1177 or 5552, plus a few extra ports (like TCP 14817 that was used by the analysed sample).
You’ll need [NetworkMiner Professional](https://www.netresec.com/?page=BuyNetworkMiner) to decode njRAT traffic to other ports, since it comes with a port-independent-protocol-identification (PIPI) feature that automatically detects the protocol regardless which port the server runs on.

As demonstrated in the video, NetworkMiner can extract the following types of artefacts from njRAT network traffic:

* Screenshots of victim computer
* Transferred files
* Commands from C2 server
* Replies from bot
* Stolen credentials/passwords
* Keylog data

**Covered njRAT Commands and Plugins**

These njRAT commands and plugins are mentioned in the video:

* CAP = Screen Capture
* ret = Get Passwords
* inv = Invoke Plugin
* PLG = Plugin Delivery
* kl = Key Logger
* Ex = Execute Plugin
* Ex proc = Process List
* Ex fm = File Manager

**IOC List**

* Sample (a.exe): cca1e0b65d759f4c58ce760f94039a0a
* C2 server: 5.tcp.eu.ngrok[.]io:14817
* njRAT inv (dll): 2d65bc3bff4a5d31b59f5bdf6e6311d7
* njRAT PLG (dll): c179e212316f26ce9325a8d80d936666
* njRAT ret (dll): ac43720c43dcf90b2d57d746464ad574
* Splitter: Y262SUCZ4UJJ

Posted by Erik Hjelmvik on Monday, 28 April 2025 06:00:00 (UTC/GMT)

Tags:
#[njRAT](/?page=Blog&tag=njRAT)​
#[NetworkMiner](/?page=Blog&tag=NetworkMiner)​
#[REMnux](/?page=Blog&tag=REMnux)​
#[Video](/?page=Blog&tag=Video)​
#[videotutorial​](/?page=Blog&tag=videotutorial​)​

Short URL:
<https://netresec.com/?b=2541a39>

### Recent Posts

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

» [PureRAT = ResolverRAT = PureHVNC](/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC)

» [PureLogs Forensics](/?page=Blog&month=2025-07&post=PureLogs-Forensics)

» [CapLoader 2.0.1 Released](/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released)

» [Detecting PureLogs traffic with CapLoader](/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader)

» [CapLoader 2.0 Released](/?page=Blog&month=2025-06&post=CapLoader-2-0-Released)

» [Comparison of tools that extract files from PCAP](/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP)

### Blog Archive

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)