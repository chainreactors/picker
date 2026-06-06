---
title: PolarProxy 2.0.1 Released
url: https://www.netresec.com/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released
source: NETRESEC Network Security Blog
date: 2026-06-05
fetch_date: 2026-06-06T05:51:06.582734
---

# PolarProxy 2.0.1 Released

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

Friday, 05 June 2026 06:45:00 (UTC/GMT)

## [PolarProxy 2.0.1 Released](/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released)

![PolarProxy 2.0.1](https://media.netresec.com/images/PolarProxy_2-0-1_2000x2000.webp)

Our TLS inspection proxy [PolarProxy](https://www.netresec.com/?page=PolarProxy) has been updated with bug fixes, improved performance and more reliable PCAP output.

The recent [PolarProxy 2.0 release](https://netresec.com/?b=2658a26) added musl/Alpine compatibility and support for unencrypted HTTP proxy requests. But there were a few small, yet very important, updates that unfortunately didn’t make it into that release. The new PolarProxy 2.0.1 release takes care of this.

**Bug Fixes**

The PolarProxy 2.0.1 release fixes three bugs affecting non-TLS traffic: two that could block non-TLS connections under certain conditions, and one that could corrupt packets in output PCAP data.

**Improved Performance**

Memory overhead has been reduced as part of a major overhaul of PolarProxy’s data-flow logic. PolarProxy now caches less data, reducing CPU and memory use while supporting more simultaneous sessions.

![PCAP vs. throughput](https://media.netresec.com/images/pcap-vs-throughput_1000x679.webp)

**PCAP vs Throughput**

[PolarProxy](https://www.netresec.com/?page=PolarProxy) now prioritizes accurate PCAP output over raw proxy throughput. If the consumer of a real-time [PCAP-over-IP](https://en.wikipedia.org/wiki/PCAP-over-IP) stream (for example [Arkime](https://arkime.com/settings#reader-poi) or [Zeek](https://github.com/emnahum/zeek-pcapovertcp-plugin)) cannot process encrypted traffic fast enough, PolarProxy may rate-limit proxied traffic to avoid dropping packets in the PCAP output. This preserves every decrypted packet for forensic analysis, unlike many TLS-inspection products that sacrifice decrypted packets to maximize throughput.

A single dropped packet can cause major problems, particularly in forensic investigations. To ensure analysts see every decrypted packet, [PolarProxy](https://www.netresec.com/?page=PolarProxy) avoids dropping packets when possible.

Posted by Erik Hjelmvik on Friday, 05 June 2026 06:45:00 (UTC/GMT)

Tags:
#[PolarProxy](/?page=Blog&tag=PolarProxy)​
#[PCAP](/?page=Blog&tag=PCAP)​
#[TLS](/?page=Blog&tag=TLS)​
#[proxy](/?page=Blog&tag=proxy)​

Short URL:
<https://netresec.com/?b=266dc11>

### Recent Posts

» [PolarProxy 2.0.1 Released](/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released)

» [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

» [PolarProxy 2.0 Released](/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released)

» [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

» [FlowCarp Identifies Protocols](/?page=Blog&month=2026-05&post=FlowCarp-Identifies-Protocols)

» [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

» [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

» [Decoding malware C2 with CyberChef](/?page=Blog&month=2026-01&post=Decoding-malware-C2-with-CyberChef)

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