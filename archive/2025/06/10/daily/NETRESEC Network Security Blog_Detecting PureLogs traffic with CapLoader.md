---
title: Detecting PureLogs traffic with CapLoader
url: https://www.netresec.com/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader
source: NETRESEC Network Security Blog
date: 2025-06-10
fetch_date: 2025-10-06T22:57:16.225060
---

# Detecting PureLogs traffic with CapLoader

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

Monday, 09 June 2025 14:26:00 (UTC/GMT)

## [Detecting PureLogs traffic with CapLoader](/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader)

[CapLoader](https://www.netresec.com/?page=CapLoader) includes a feature for [Port Independent Protocol Identification](https://netresec.com/?b=15A1776) (PIPI), which can detect which protocol is being used inside of TCP and UDP sessions without relying on the port number. In this video CapLoader identifies the C2 protocol used by the [PureLogs Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.purelogs) malware.

The PureLogs protocol detection was added to CapLoader in the recent [2.0 release](https://netresec.com/?b=256dbbc).

[![

](https://media.netresec.com/images/PureLogs-CapLoader_poster_1280x672.png)](https://media.netresec.com/videos/PureLogs-CapLoader-1280x762.mp4)

The PCAP file analyzed in the video is from [Brad Duncan](https://infosec.exchange/%40malware_traffic)’s fantastic [malware-traffic-analysis.net](https://malware-traffic-analysis.net/2025/05/12/index.html) website.

Indicators of Compromize (IOC):

* mxcnss.dns04.com:7702
* 176.65.144.169:7702

Posted by Erik Hjelmvik on Monday, 09 June 2025 14:26:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[PureLogs](/?page=Blog&tag=PureLogs)​
#[malware-traffic-analysis.net](/?page=Blog&tag=malware-traffic-analysis.net)​
#[PIPI](/?page=Blog&tag=PIPI)​

Short URL:
<https://netresec.com/?b=256a8c4>

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