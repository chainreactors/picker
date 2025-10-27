---
title: How to Identify IcedID Network Traffic
url: https://www.netresec.com/?page=Blog&month=2023-02&post=How-to-Identify-IcedID-Network-Traffic
source: NETRESEC Network Security Blog
date: 2023-02-16
fetch_date: 2025-10-04T06:48:07.979965
---

# How to Identify IcedID Network Traffic

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

Wednesday, 15 February 2023 10:52:00 (UTC/GMT)

## [How to Identify IcedID Network Traffic](/?page=Blog&month=2023-02&post=How-to-Identify-IcedID-Network-Traffic)

Brad Duncan published [IcedID (Bokbot) from fake Microsoft Teams page](https://malware-traffic-analysis.net/2023/02/13/index.html) earlier this week. In this video I take a closer look at the PCAP file in that blog post.

[![

The video cannot be played in your browser.
](https://www.netresec.com/images/identify-icedid-traffic_poster_512x288.png)](https://media.netresec.com/videos/identify-icedid-traffic_1280x720.webm)
> *Note: This video was recorded in a [Windows Sandbox](https://netresec.com/?b=215d5b5) to minimize the risk of infecting the host PC in case of accidental execution of a malicious payload from the network traffic.*

As I have [previously pointed out](https://netresec.com/?b=214d7ff), IcedID sends beacons to the C2 server with a 5 minute interval. According to Kai Lu’s blog post [A Deep Dive Into IcedID Malware: Part 2](https://www.fortinet.com/blog/threat-research/icedid-malware-analysis-part-two), this 5 minute interval is caused by a call to [WaitForSingleObject](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject) with a millisecond timeout parameter of 0x493e0 (300,000), which is exactly 5 minutes.

***UPDATE 2023-03-22***

*In the research paper
[Thawing the permafrost of ICEDID](https://www.elastic.co/pdf/elastic-security-labs-thawing-the-permafrost-of-icedid.pdf)
Elastic Security Labs confirm that IcedID's default polling interval is 5 minutes. They also mention that this interval is configurable:
> Once initialized, ICEDID starts its C2 polling thread for retrieving new commands to execute
> from one of its C2 domains.
> The polling loop checks for a new command every N seconds as defined by the
> g\_c2\_polling\_interval\_seconds global variable. By default this interval is 5 minutes, but one of
> the C2 commands can modify this variable.*

The IcedID trojan uses a custom BackConnect protocol in order to interact with victim computers through VNC, a file manager or by establishing a reverse shell.
There was no IcedID BackConnect traffic in this particular PCAP file though, but
[several](https://www.malware-traffic-analysis.net/2022/06/28/index.html) [other](https://www.malware-traffic-analysis.net/2022/10/31/index.html) IcedID capture files published on malware-traffic-analysis.net do contain IcedID BackConnect traffic.
For more information on this proprietary protocol, please see our blog post [IcedID BackConnect Protocol](https://netresec.com/?b=22A38f9).

**IOC List**

Fake Microsoft Teams download page

* URL: hxxp://microsofteamsus[.]top/en-us/teams/download-app/
* MD5: 5dae65273bf39f866a97684e8b4b1cd3
* SHA256: e365acb47c98a7761ad3012e793b6bcdea83317e9baabf225d51894cc8d9e800
* More info: [urlscan.io](https://urlscan.io/result/3a0995a2-7994-4a91-a82e-fa037118aee5/)

IcedID GzipLoader

* Filename: Setup\_Win\_13-02-2023\_16-33-14.exe
* MD5: 7327fb493431fa390203c6003bd0512f
* SHA256: 68fcd0ef08f5710071023f45dfcbbd2f03fe02295156b4cbe711e26b38e21c00
* More info: [Triage](https://tria.ge/230214-mdys9sbh9y)

IcedID payload disguised as fake gzip file

* URL: hxxp://alishabrindeader[.]com/
* MD5: 8e1e70f15a76c15cc9a5a7f37c283d11
* SHA256: 7eb6e8fdd19fc6b852713c19a879fe5d17e01dc0fec62fa9dec54a6bed1060e7
* More info: [IcedID GZIPLOADER Analysis](https://www.binarydefense.com/icedid-gziploader-analysis/) by Binary Defense

IcedID C2 communication

* IP and port: 192.3.76.227:443
* DNS: treylercompandium[.]com
* DNS: qonavlecher[.]com
* X.509 certificate SHA1: b523e3d33e7795de49268ce7744d7414aa37d1db
* X.509 certificate SHA256: f0416cff86ae1ecc1570cccb212f3eb0ac8068bcf9c0e3054883cbf71e0ab2fb
* JA3: a0e9f5d64349fb13191bc781f81f42e1
* JA3S: ec74a5c51106f0419184d0dd08fb05bc
* Beacon interval: 5 minutes
* More info: [ThreatFox](https://threatfox.abuse.ch/ioc/1078315/)

**Network Forensics Training**

Check out our upcoming [live network forensics classes](https://www.netresec.com/?page=Training) for more hands-on network forensic analysis. Our current class material doesn’t include any IcedID traffic though, instead you’ll get to investigate C2 traffic from Cobalt Strike, TrickBot, njRAT, Meterpreter and a few others.

Posted by Erik Hjelmvik on Wednesday, 15 February 2023 10:52:00 (UTC/GMT)

Tags:
#[IcedID](/?page=Blog&tag=IcedID)​
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[Video](/?page=Blog&tag=Video)​
#[Periodicity](/?page=Blog&tag=Periodicity)​
#[GzipLoader](/?page=Blog&tag=GzipLoader)​
#[a0e9f5d64349fb13191bc781f81f42e1](/?page=Blog&tag=a0e9f5d64349fb13191bc781f81f42e1)​
#[ec74a5c51106f0419184d0dd08fb05bc](/?page=Blog&tag=ec74a5c51106f0419184d0dd08fb05bc)​

Short URL:
<https://netresec.com/?b=23242ad>

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