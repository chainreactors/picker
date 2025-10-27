---
title: Remote Sniffing from Mikrotik Routers
url: https://www.netresec.com/?page=Blog&month=2024-05&post=Remote-Sniffing-from-Mikrotik-Routers
source: NETRESEC Network Security Blog
date: 2024-05-31
fetch_date: 2025-10-06T16:51:14.784842
---

# Remote Sniffing from Mikrotik Routers

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

Thursday, 30 May 2024 13:05:00 (UTC/GMT)

## [Remote Sniffing from Mikrotik Routers](/?page=Blog&month=2024-05&post=Remote-Sniffing-from-Mikrotik-Routers)

One of the new features in [NetworkMiner 2.9](https://netresec.com/?b=245092b) is a [TZSP](https://wiki.mikrotik.com/wiki/Manual%3ATools/Packet_Sniffer) streaming server. It is designed to read a real-time stream of sniffed packets from Mikrotik routers. This method for remote sniffing can be used to capture packets regardless if NetworkMiner is running in Windows or [Linux](https://netresec.com/?b=2542784).

![Sniff Packets with Mikrotik TZSP to NetworkMiner](https://media.netresec.com/images/Mikrotik-TZSP-NetworkMiner_512x256.png)

**How to Sniff Packets with TZSP**

Open a [console](https://help.mikrotik.com/docs/display/ROS/Command%2BLine%2BInterface) or terminal on the Mikrotik router and run “/tool sniffer print” to see the current settings.
Then run the following commands to configure the sniffer:

* /tool sniffer
* set streaming-enabled=yes
* set streaming-server=10.1.2.3:37008
* set filter-stream=yes

Replace 10.1.2.3 with the IP address of the computer running NetworkMiner

It is also possible to activate the sniffer from the RouterOS [WebFig](https://help.mikrotik.com/docs/display/ROS/WebFig) interface.

* Expand the “Tools” section
* Click “Packet Sniffer”
* Check “Streaming Enabled”
* Enter IP of computer running NetworkMiner in **Server**
* Enter 37008 as **Port**
* Check “Filter Stream”
* Click the “Apply” button at the top

![Mikrotik WebFig Packet Sniffer settings](https://media.netresec.com/images/Mikrotik-WebFig-Filter_513x205.png)

The “filter-stream” setting prevents the sniffer from capturing packets that are sent to the streaming-server (i.e. NetworkMiner). This setting must be enabled to avoid a snowball effect, where copies of previously captured packets get sniffed and re-transmitted to the streaming-server.

The next step is to open the TZSP window in NetworkMiner, which you’ll find under “File, Receive TZSP Stream”.

![NetworkMiner TZSP Sniffer](https://media.netresec.com/images/NetworkMiner_2-9_TZSP-Sniffer_517x260.png)

Click “Start” in NetworkMiner’s TZSP window, so that it listens for an incoming TZSP stream on UDP port 57008. Go back to the Mikrotik router, where you start the sniffer with “/tool sniffer start” or by clicking the “Start” button in the WebFig. You should now see the Frames counter increasing in NetworkMiner's TZSP window. You’ll probably also notice that artifacts get added to the main NetworkMiner window in the background as more packets are received.

Close the sniffer by running “/tool sniffer stop” or clicking the “Stop” button in WebFig, then click “Stop” in NetworkMiner. You can now close NetworkMiner’s TZSP window to view the artifacts that NeworkMiner has extracted from the captured traffic.

Posted by Erik Hjelmvik on Thursday, 30 May 2024 13:05:00 (UTC/GMT)

Tags:
#[TZSP](/?page=Blog&tag=TZSP)​
#[NetworkMiner](/?page=Blog&tag=NetworkMiner)​
#[sniffer](/?page=Blog&tag=sniffer)​

Short URL:
<https://netresec.com/?b=2459ed5>

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