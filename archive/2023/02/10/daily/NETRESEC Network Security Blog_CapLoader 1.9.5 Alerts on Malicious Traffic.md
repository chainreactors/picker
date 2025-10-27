---
title: CapLoader 1.9.5 Alerts on Malicious Traffic
url: https://www.netresec.com/?page=Blog&month=2023-02&post=CapLoader-1-9-5-Alerts-on-Malicious-Traffic
source: NETRESEC Network Security Blog
date: 2023-02-10
fetch_date: 2025-10-04T06:16:05.967549
---

# CapLoader 1.9.5 Alerts on Malicious Traffic

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

Thursday, 09 February 2023 14:30:00 (UTC/GMT)

## [CapLoader 1.9.5 Alerts on Malicious Traffic](/?page=Blog&month=2023-02&post=CapLoader-1-9-5-Alerts-on-Malicious-Traffic)

[CapLoader](https://www.netresec.com/?page=CapLoader) 1.9.5 was released today!

The most important addition in the 1.9.5 release is the new Alerts tab, in which CapLoader warns about malicious network traffic such as command-and-control protocols. The alerts tab also shows information about network anomalies that often are related to malicious traffic, such as periodic connections to a particular service or long running sessions.

Other additions in this new version are:

* BPF support for “vlan” keyword, for example “vlan”, “not vlan” or “vlan 121”
* Support for nanosecond PCAP files (magic 0xa1b23c4d)
* Support for FRITZ!Box PCAP files (magic 0xa1b2cd34)
* Decapsulation of CAPWAP protocol, so that flows inside CAPWAP can be viewed and filtered on
* Domain names extracted from TLS SNI extensions

**Alerts for Malicious Network Traffic**

As you can see in the video at the end of this blog post, the Alert tab is a fantastic addition for everyone who wants to detect malicious activity in network traffic. Not only can it alert on over 30 different malicious command-and-control (C2) protocols — including
[Cerber](https://malpedia.caad.fkie.fraunhofer.de/details/win.cerber),
[Gozi ISFB](https://malpedia.caad.fkie.fraunhofer.de/details/win.isfb),
[IcedID](https://netresec.com/?b=214d7ff), [RedLine Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.redline_stealer),
[njRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.njrat) and [QakBot](https://malpedia.caad.fkie.fraunhofer.de/details/win.qakbot) — it also alerts on generic behavior that is typically seen in malware traffic.
Examples of such generic behavior are periodic connections to a C2 server or long running TCP connections. This type of behavioral analysis can be used to detect C2 and backdoor traffic even when the protocol is unknown. There are also signatures that detect “normal” protocols, such as HTTP, TLS or SSH running on non-standard ports as well as the reverse, where a standard port like TCP 443 is carrying a protocol that isn’t TLS.

Many of CapLoader’s alert signatures are modeled after threat hunting techniques, which can be used to detect malicious activities that traditional alerting mechanisms like antivirus, EDR’s and IDS’s might have missed. By converting the logic involved in such threat hunting tasks into signatures a great deal of the analysts’ time can be saved. In this sense part of CapLoader’s alerting mechanism is a form of automated threat hunting, which saves several steps in the process of finding malicious network traffic in a packet haystack.

Watch my [Hunting for C2 Traffic video](https://netresec.com/?b=2296553) for a demonstration on the steps required to perform manual network based threat hunting without CapLoader's alerts tab. In that video I identify TLS traffic to a non-TLS port (TCP 2222) as well as non-TLS traffic to TCP port 443. As of version 1.9.5 CapLoader automatically generates alerts for that type of traffic. More specifically, the alert types will be **Protocol-port mismatch** (TLS on TCP 2222) and **Port-protocol mismatch** (non-TLS on TCP 443).
Below is a screenshot of CapLoader’s new Alerts tab after having loaded the capture files analyzed in the [Hunting for C2 Traffic video](https://netresec.com/?b=2296553).

![Alerts produced by CapLoader 1.9.5 after loading the three PCAP files from malware-traffic-analysis.net](https://www.netresec.com/images/CapLoader_1-9-5_Alerts_malware-traffic-analysis_220627-220628_520x395.png)

*Image: Alerts for malicious traffic in CapLoader 1.9.5.*

**Video Demonstration of CapLoader's Alerts Tab**

The best way to explain the power of [CapLoader](https://www.netresec.com/?page=CapLoader)’s Alerts tab is probably by showing it in action. I have therefore recorded the following video demonstration.

[![

The video cannot be played in your browser.
](https://www.netresec.com/images/caploader_1-9-5_alerts_lp_512x288.png)](https://media.netresec.com/videos/caploader_1-9-5_alerts_lp_1280x720.webm)

The PCAP file analyzed in the video can be downloaded from here:
<https://media.netresec.com/pcap/McDB_150724-18-22_FpF90.pcap>

This capture file is a small snippet of the network traffic analyzed in one of my old network forensics classes. It contains malicious traffic from njRAT and Kovter mixed with a great deal of legitimate web traffic.

Posted by Erik Hjelmvik on Thursday, 09 February 2023 14:30:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[Video](/?page=Blog&tag=Video)​
#[njRAT](/?page=Blog&tag=njRAT)​
#[Threat Hunting](/?page=Blog&tag=Threat Hunting)​

Short URL:
<https://netresec.com/?b=232e498>

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