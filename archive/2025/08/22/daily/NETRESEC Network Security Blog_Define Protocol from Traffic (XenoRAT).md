---
title: Define Protocol from Traffic (XenoRAT)
url: https://www.netresec.com/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT
source: NETRESEC Network Security Blog
date: 2025-08-22
fetch_date: 2025-10-07T00:48:41.710095
---

# Define Protocol from Traffic (XenoRAT)

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

Thursday, 21 August 2025 12:50:00 (UTC/GMT)

## [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

This video shows how to define a protocol in [CapLoader](https://www.netresec.com/?page=CapLoader) just by providing examples of what the protocol looks like. CapLoader can then identify that protocol in other traffic, regardless of IP address and port number, simply by looking for traffic that behaves similar to what it was trained on. We call this [Port Independent Protocol Identification](https://netresec.com/?b=15A1776) (PIPI). You don’t need to define all protocols this way though since CapLoader can detect hundreds of different protocols out of the box using PIPI.

[![

](https://media.netresec.com/images/CapLoader_Define-Protocol-XenoRAT_1280x672.png)](https://media.netresec.com/videos/Define-Protocol_XenoRAT_1280x672.mp4)

The protocol identified in the video is the [XenoRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.xenorat) command-and-control (C2) protocol. The identification was based on a sandbox execution of [XenoRATClientScript.js on ANY.RUN](https://app.any.run/tasks/85296f64-671e-4bda-8016-59454182097d). The protocol model was then tested on a PCAP file from a [XenoRAT execution on Triage](https://tria.ge/250811-ghsvxsfr4x/behavioral1).

**IOC List**

* Url: hxxps://raw.githubusercontent[.]com/NTCHuy/hack/refs/heads/main/Client.exe
* MD5: e0b465d3bd1ec5e95aee016951d55640
* MD5: 5ab23ac79ede02166d6f5013d89738f9
* C2: Huy1612-24727.portmap[.]io:24727
* C2: 193.161.193.99:24727
* C2: 147.185.221.30:54661

Posted by Erik Hjelmvik on Thursday, 21 August 2025 12:50:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[PIPI](/?page=Blog&tag=PIPI)​
#[ANY.RUN](/?page=Blog&tag=ANY.RUN)​

Short URL:
<https://netresec.com/?b=258f641>

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