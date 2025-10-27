---
title: CapLoader 1.9.7 Released
url: https://www.netresec.com/?page=Blog&month=2024-09&post=CapLoader-1-9-7-Released
source: NETRESEC Network Security Blog
date: 2024-09-07
fetch_date: 2025-10-06T18:29:20.606715
---

# CapLoader 1.9.7 Released

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

Friday, 06 September 2024 09:45:00 (UTC/GMT)

## [CapLoader 1.9.7 Released](/?page=Blog&month=2024-09&post=CapLoader-1-9-7-Released)

![CapLoader 1.9.7](https://media.netresec.com/images/CL_1-9-7_770x770.png)

A new release of [CapLoader](https://www.netresec.com/?page=CapLoader) has been published! Some of the changes can be seen directly in the user interface, such as Community ID values for flows and a few other new columns in the Flows and Services tabs. Other improvements are more subtle, like improved detection of remote management protocols and malicious C2 protocols.

**User Interface Improvements**

The most important user interface update is probably the addition of a Community\_ID column in the Flows tab, which shows a unique [Community ID](https://github.com/corelight/community-id-spec) string for each flow. The community ID is a common flow identifier that can be used to correlate traffic in CapLoader with alerts or events from tools like Zeek, Suricata, MISP or Arkime.

![CapLoader 1.9.4 with Retransmissions and Community ID](https://media.netresec.com/images/CapLoader_1-9-4_Flows_with-Retransmissions-Community_ID_520x525.png)

CapLoader now has a column named Retransmissions in both Flows and Services tab, which shows an estimate of how many percent of the packets in each flow or service that are retransmissions. This value can be used to quickly diagnose a network issue without having to inspect network traffic on a packet-by-packet level.

We have also added a column named Client\_IP\_TTL to CapLoader’s Flows tab, which can be used to differentiate between NAT’ed clients that share a single public IP address – provided that they run operating systems with different IP TTL of course! There is also a new column in the Services tab called First\_Seen, which shows when each service was first observed in the analyzed network traffic.

The Severity and Severity\_Label columns in the Alerts tab are now colored according to severity level, where red means High, orange is Medium, yellow is Low and blue is Info (the exact color codes were borrowed from the [US Homeland Security Advisory System scale](https://en.wikipedia.org/wiki/Homeland_Security_Advisory_System)).

![Alerts in CapLoader 1.9.4](https://media.netresec.com/images/CapLoader_1-9-4_Alerts_520x573.png)

We have also included a handy little feature that allows you to append additional PCAP files to an existing analysis session simply by holding down Ctrl while drag-and-dropping another capture file onto CapLoader. The “Append File(s)” option is also available under CapLoader’s File menu.

**Even More Protocols Identified**

CapLoader’s unique ability to identify protocols regardless of port has been improved and we’ve also added detections for several new protocols. For this release we’ve focused adding detection for remote monitoring and management (RMM) protocols, such as ConnectWise (formerly ScreenConnect), AnyDesk, NetSupport (including [NetSupport RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.netsupportmanager_rat)), TeamViewer (including [TVRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.teamspy)) and [RMS](https://malpedia.caad.fkie.fraunhofer.de/details/win.rms) (Remote Utilities). This enables CapLoader to alert whenever an RMM protocol is detected.

We’ve also added detection of several new malware protocols, including [Matanbuchus](https://malpedia.caad.fkie.fraunhofer.de/details/win.matanbuchus), [Meduza Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.meduza), [SectopRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.sectop_rat), [STRRAT](https://malpedia.caad.fkie.fraunhofer.de/details/jar.strrat) and [zgRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.zgrat).

**Even More Protocols Decapsulated**

![DECAPSULATE ALL THE THINGS](https://media.netresec.com/images/Decapsulate_all-the-things_800x599.webp)

CapLoader already decapsulates flows inside of [GRE](https://datatracker.ietf.org/doc/html/rfc2784), [VXLAN](https://datatracker.ietf.org/doc/html/rfc7348) and [CapWap](https://datatracker.ietf.org/doc/html/rfc5415). With this release we add support for decapsulation of [Teredo](https://www.rfc-editor.org/rfc/rfc4380.html), [GTP-U](https://en.wikipedia.org/wiki/GPRS_Tunnelling_Protocol#GTP-U_-_GTP_user_data_tunneling), [TZSP](https://wiki.mikrotik.com/wiki/Manual%3ATools/Packet_Sniffer) as well as [IP-in-IP](https://datatracker.ietf.org/doc/html/rfc1853) traffic, so that tunneled traffic can be analyzed without any additional effort.

**Credits**

I would like to thank [Jarmo Lahtiranta](https://infosec.exchange/%40naranek) for the TZSP idea and [Lenny Hansson](https://networkforensic.dk/contact/) for pointing out the need for improved protocol detection. I would also like to thank [Christian Kreibich](https://mastodon.coffee/%40ckreibich) and his fellow Corelight devs for creating and open sourcing the [Community ID project](https://github.com/corelight/community-id-spec).

**Updating to the Latest Release**

﻿Users who have already purchased a license for CapLoader can download a free update to version 1.9.7 from our [customer portal](https://www.netresec.com/portal/) or by clicking “Check for Updates” in CapLoader’s Help menu.

Posted by Erik Hjelmvik on Friday, 06 September 2024 09:45:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[TZSP](/?page=Blog&tag=TZSP)​
#[TTL](/?page=Blog&tag=TTL)​

Short URL:
<https://netresec.com/?b=2499359>

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
[Blue...