---
title: CapLoader 2.0.1 Released
url: https://www.netresec.com/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released
source: NETRESEC Network Security Blog
date: 2025-07-02
fetch_date: 2025-10-06T23:54:28.424983
---

# CapLoader 2.0.1 Released

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

Tuesday, 01 July 2025 13:48:00 (UTC/GMT)

## [CapLoader 2.0.1 Released](/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released)

This update resolves several minor bugs, but also brings better protocol identification and a new IP lookup alert to [CapLoader](https://www.netresec.com/?page=CapLoader).

![CapLoader showing Info-level alert for IP lookup using ip-api.com](https://media.netresec.com/images/CapLoader_2-0-1_IP-lookup-domain_522x465.webp)

*Alert for IP lookup using ip-api.com in [PCAP from tria.ge](https://tria.ge/250629-hy4sssv1f1/behavioral1)*
![Transcript of ip-api.com IP lookup traffic](https://media.netresec.com/images/CapLoader_transcript_ip-api_522x523.webp)

*Transcript of ip-api.com IP lookup traffic*

IP lookup services, like ip-api, checkip.amazonaws.com and ident.me, aren’t malicious, but malware often use such services to find out what the public IP address is of an infected machine. As [Tony Robinson](https://infosec.exchange/%40da_667) points out, in his recent [External IP Lookup Rules](https://community.emergingthreats.net/t/external-ip-lookup-rules/2838) post, malware does so to check for internet connectivity and determine the country of the infected PC. But I’ve also observed a third reason, which is when the threat actor resolves the victim’s public IP to then query a [DNSBL service](https://en.wikipedia.org/wiki/Domain_Name_System_blocklist) and check the IP’s reputation. I believe the DNSBL lookup is performed to evaluate the success rate of sending spam, such as emails with malicious attachments or links, from the victim PC.

![TrickBot performing a DNSBL lookup of client’s public IP](https://media.netresec.com/images/CapLoader_transcript_zen-spamhaus-org_515x315.webp)

*TrickBot performing a DNSBL lookup of client’s public IP*

If you want to learn more about how TrickBot used DNSBL then read GoSecure’s [TrickBot […] and Spamhaus](https://gosecure.ai/blog/2021/12/03/trickbot-leverages-zoom-work-from-home-interview-malspam-heavens-gate-and-spamhaus/) blog post or sign up for one of my [network forensics training sessions](https://www.netresec.com/?page=Training).

**Improved Protocol Detection**

The precision of CapLoaders built-in [port independent protocol identification](https://netresec.com/?b=15A1776) has been improved and a few additional protocols can now be detected, including
[Interlock RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.interlock).

**Bug Fixes**

The following bugs fixes and feature updates are included in this release:

* Better handling of corrupt PCAP files
* Fixed [periodicity measurement](https://netresec.com/?b=165bf7d) inconsistency for services with more than 100 flows
* Fixed parsing bug for duplicate QUIC packets
* Improved speed and reliability of auto-extract PCAP from selection
* ThreatFox API updated to use abuse.ch Auth-Key

Posted by Erik Hjelmvik on Tuesday, 01 July 2025 13:48:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[TrickBot](/?page=Blog&tag=TrickBot)​
#[DNSBL](/?page=Blog&tag=DNSBL)​

Short URL:
<https://netresec.com/?b=2571527>

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