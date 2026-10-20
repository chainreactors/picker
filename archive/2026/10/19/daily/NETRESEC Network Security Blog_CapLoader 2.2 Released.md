---
title: CapLoader 2.2 Released
url: https://www.netresec.com/?page=Blog&month=2026-10&post=CapLoader-2-2-Released
source: NETRESEC Network Security Blog
date: 2026-10-19
fetch_date: 2026-10-20T06:53:37.407349
---

# CapLoader 2.2 Released

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

Monday, 19 October 2026 08:48:00 (UTC/GMT)

## [CapLoader 2.2 Released](/?page=Blog&month=2026-10&post=CapLoader-2-2-Released)

![CapLoader 2.2](https://media.netresec.com/images/CL_2-2_770x770.webp)

[CapLoader](https://www.netresec.com/?page=CapLoader) 2.2 adds new alerts for services and infrastructure that may be abused, makes flow transcripts easier to navigate and improves alert-based coloring. It also includes more helpful BPF filter feedback and several bug fixes.

**More alerts**

CapLoader’s alerting has been expanded with built-in detections for online services and infrastructure that are commonly abused, along with support for external blocklists from [IFIN](https://lists.ifin.network/about.html), [GAYINT](https://intel.gayint.org/blocklists) and [Spamhaus](https://www.spamhaus.org/resource-hub/dnsbl/the-return-of-the-asn-drop/).

New alert types include:

* [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System) services and gateways
* Port forwarding services
* Abused web hosting and cloud storage services
* VPN, proxy and tunnel protocols
* [Blockchain RPC nodes](https://lists.ifin.network/lists/rpc-nodes/index.html)
* [Paste bin domains](https://lists.ifin.network/lists/paste-bins---code/index.html)
* Bulletproof, scanner and VPN ASNs

Many of these alerts are informational, while others are low severity.

**Transcript navigation and row coloring**

You can now move between flow transcripts using the arrow keys. To make moving to the next transcript quicker, CapLoader anticipates the next Flow Index and pre-fetches its frames.

Thanks to André for suggesting the transcript navigation feature during one of my [trainings](https://www.netresec.com/?page=Training)!

[

](https://media.netresec.com/videos/CapLoader-flow-transcript_short_1056x516.mp4)

*Video: Transcript of flows in Johannes Weber’s [Ultimate PCAP](https://weberblog.net/the-ultimate-pcap/)*

CapLoader 2.2 also adds the **AlertSeverity** row color scheme. It colors each flow, service and host according to the highest-severity alert associated with it.

Here’s CapLoader with the traditional Wireshark style color scheme:

![CapLoader with Wireshark style colors](https://media.netresec.com/images/CapLoader_Wireshark-colors_540x548.webp)

This is what the same traffic looks like with the new AlertSeverity color scheme:

![CapLoader with AlertSeverity style colors](https://media.netresec.com/images/CapLoader_AlertSeverity-colors_540x548.webp)

Both screenshots show the same capture file, which contains traffic from an [XMRig sample on Triage](https://tria.ge/261019-jv1seagy9x/behavioral2).

BPF filter boxes now provide better error checking, with colors and tooltips to warn about possible syntax mistakes. You can also press Enter to open the transcript for a selected flow from any tab, not just the Flows tab. If you select multiple flows, Enter opens multiple transcripts.

**Bug fixes**

This release fixes an issue that could prevent the “About CapLoader” window from opening, as well as a crash that could occur when reading very large frames. It also fixes JA4 fingerprints when TLS Signature Algorithms contain GREASE values.

Posted by Erik Hjelmvik on Monday, 19 October 2026 08:48:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[transcript](/?page=Blog&tag=transcript)​

Short URL:
<https://netresec.com/?b=26A4762>

### Recent Posts

» [CapLoader 2.2 Released](/?page=Blog&month=2026-10&post=CapLoader-2-2-Released)

» [Detecting AtlasRAT C2](/?page=Blog&month=2026-10&post=Detecting-AtlasRAT-C2)

» [NetworkMiner 3.2 Released](/?page=Blog&month=2026-10&post=NetworkMiner-3-2-Released)

» [Stop Feeding the SOC Garbage](/?page=Blog&month=2026-10&post=Stop-Feeding-the-SOC-Garbage)

» [Unmasking Malware Families](/?page=Blog&month=2026-09&post=Unmasking-Malware-Families)

» [PolarProxy 2.0.2 Released](/?page=Blog&month=2026-09&post=PolarProxy-2-0-2-Released)

» [OT Networks Still Need Monitoring](/?page=Blog&month=2026-08&post=OT-Networks-Still-Need-Monitoring)

» [CNCMachineRMS C2 Protocol](/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol)

### Blog Archive

» [2026 Blog Posts](?page=Blog&year=2026)

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