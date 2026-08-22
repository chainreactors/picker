---
title: CNCMachineRMS C2 Protocol
url: https://www.netresec.com/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol
source: NETRESEC Network Security Blog
date: 2026-08-21
fetch_date: 2026-08-22T02:52:33.966897
---

# CNCMachineRMS C2 Protocol

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

Friday, 21 August 2026 14:45:00 (UTC/GMT)

## [CNCMachineRMS C2 Protocol](/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol)

![CNCMachineRMS](https://media.netresec.com/images/CNCMachineRMS_2000x2005.webp)

This post describes the binary command-and-control (C2) protocol used by CNCMachineRMS, a recently identified remote access trojan (RAT). We cover how the protocol was discovered, how its infrastructure was identified, and how network defenders can detect it.

**Background**

We have been tracking a previously unknown malware C2 protocol for several months. It first came to our attention back in April through packet captures from two [sandbox](https://www.malware-traffic-analysis.net/2026/04/06/index.html) [executions](https://www.malware-traffic-analysis.net/2026/04/23/index.html) created by [Brad Duncan](https://infosec.exchange/%40malware_traffic).

The captures showed ClickFix attacks in which a fake CAPTCHA was used to deliver a previously unknown remote access trojan. The RAT communicated with 89.110.110.119 over TCP port 443. Although the traffic used port 443, it was not protected by TLS and did not resemble any previously known C2 protocol.

We later added a detection model for the protocol to [FlowCarp](https://flowcarp.com/). At that point, the protocol was labeled "Unknown\_16". Using FlowCarp, we identified additional C2 servers using the same protocol. All of them exposed the C2 service on TCP port 443:

* 85.158.110.78
* 89.110.110.119
* 89.124.79.98
* 144.124.242.171

Brad Duncan’s malware captures were instrumental in identifying this infrastructure. We then used the IP addresses and hashes from Brad’s executions to find additional samples and executions of the same malware family on ANY.RUN, Joe Sandbox, and Triage.

**CNCMachineRMS**

I only recently read Rodel Mendrez’s excellent writeup [CNCMachineRMS: The Undocumented RAT At the End of a BabaDeda Chain](https://www.levelblue.com/blogs/spiderlabs-blog/cncmachinerms-the-undocumented-rat-at-the-end-of-a-babadeda-chain). The report confirmed that the malware Rodel had reverse engineered was the same malware we had observed communicating in Brad Duncan’s PCAP files. In particular, the report mentions the IP address 85.158.110.78 and the domain notepadreleased[.]com.

One notable feature is the malware’s use of DNS over HTTPS (DoH). Rather than sending the C2 domain lookup to the system’s usual DNS resolver, CNCMachineRMS sends the query over HTTPS to an external DoH provider. Rodel also mentioned this in his report:

> The payload resolves its C2 domain over DNS over HTTPS, using dns.google, cloudflare-dns.com and dns.quad9.net. Local DNS logs will not show the lookup.

![notepadreleased domain resolved using DoH](https://media.netresec.com/images/ANY-RUN_notepadreleased_1322x422.webp)

*Image: Decrypted DoH query for notepadreleased[.]com from [ANY.RUN](https://app.any.run/tasks/537425cf-d112-4500-9189-ed3ec8f982ba)*

Even without extracting crypto keys from memory or using a TLS inspection tool like [PolarProxy](https://www.netresec.com/?page=PolarProxy), you can still see a TLS encrypted connection to a DoH provider such as dns.google. This usually happens just seconds before CNCMachineRMS connects to its C2 server.

**Network Detection**

FlowCarp uses a statistical model of the CNCMachineRMS binary protocol to detect similar traffic. This made it possible to add support for the CNCMachineRMS C2 protocol by providing FlowCarp with some example C2 sessions.

To our knowledge, no IDS signatures currently exist for this protocol. However, the traffic appears relatively straightforward to identify. Several fields contain consecutive 0x00 or 0xff bytes at fixed offsets, creating a distinctive pattern across the protocol’s messages.

![CapLoader flow transcript of CNCMachineRMS traffic](https://media.netresec.com/images/CNCMachineRMS_C2_markup_1200x726.png)

*Image: CapLoader flow transcript of CNCMachineRMS traffic*

Note: Yellow 0xff fields contain 0x00 in some connections.

You can test a PCAP file for CNCMachineRMS traffic by submitting it to the free [FlowCarp](https://flowcarp.com/) demo server:

curl --data-binary @suspicious.pcap https://demo.flowcarp.com

If the file contains CNCMachineRMS traffic, the response includes a JSON alert similar to the following:

![JSON alert for CNCMachineRMS from FlowCarp](https://media.netresec.com/images/FlowCarp-CNCMachineRMS_1094x833.webp)

**IOC List**

| Indicator | Details |
| --- | --- |
| 89.110.110.119:443 | first seen 2026-04-06 last seen 2026-05-27 |
| 85.158.110.78:443 | first seen 2026-06-30 last seen 2026-08-02 |
| 89.124.79.98:443 | first seen 2026-06-30 last seen 2026-07-31 |
| 144.124.242.171:443 | first seen 2026-08-12 last seen 2026-08-12 |
| notepadreleased[.]com | registered 2026-04-02 |
| triotmelon[.]com | registered 2026-08-04 |
| b0bc47a7308bd39a5b638781874a3d8e | JSONSchema.zip |
| ca88a6c055a96e1a6fa47e2586d41d2a | python.zip |
| e421ad53b169282b04e50e1b9d1faa9e | 403404323857317050-pdf.zip |
| eba2bbd380b6949a249aba5c3ed13245 | 81241123044010750.pdf |

Posted by Erik Hjelmvik on Friday, 21 August 2026 14:45:00 (UTC/GMT)

Tags:
#[FlowCarp](/?page=Blog&tag=FlowCarp)​
#[malware-traffic-analysis.net](/?page=Blog&tag=malware-traffic-analysis.net)​
#[ANY.RUN](/?page=Blog&tag=ANY.RUN)​
#[DoH](/?page=Blog&tag=DoH)​

Short URL:
<https://netresec.com/?b=268ee19>

### Recent Posts

» [CNCMachineRMS C2 Protocol](/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol)

» [PureLogs, PureRAT and misleading zgRAT](/?page=Blog&month=2026-07&post=PureLogs-PureRAT-and-misleading-zgRAT)

» [Ping32 RMM and ValleyRAT](/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT)

» [Maximizing IOC Impact](/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact)

» [PolarProxy 2.0.1 Released](/?page=Blog&month=2026-06&post=PolarProxy-2-0-1-Released)

» [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

» [PolarProxy 2.0 Released](/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released)

» [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

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
[RSS](http...