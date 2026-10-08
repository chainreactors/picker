---
title: NetworkMiner 3.2 Released
url: https://www.netresec.com/?page=Blog&month=2026-10&post=NetworkMiner-3-2-Released
source: NETRESEC Network Security Blog
date: 2026-10-07
fetch_date: 2026-10-08T08:08:09.900989
---

# NetworkMiner 3.2 Released

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

Wednesday, 07 October 2026 11:30:00 (UTC/GMT)

## [NetworkMiner 3.2 Released](/?page=Blog&month=2026-10&post=NetworkMiner-3-2-Released)

![NetworkMiner 3.2](https://media.netresec.com/images/NetworkMiner_3-2_707x707.webp)

NetworkMiner 3.2 parses RADIUS authentication data and extracts more details from the OT/ICS protocols UMAS and IEC-104. The release also improves several existing protocol parsers and fixes file-reassembly issues, helping analysts extract more information from captured network traffic.

**OT Protocol Support**

NetworkMiner parses many OT/SCADA/ICS communication protocols, such as [CIP](https://netresec.com/?b=254caa9), [COTP](https://netresec.com/?b=245092b), [EtherNet/IP](https://netresec.com/?b=254caa9), [IEC 60870-5-104](https://netresec.com/?b=224e357), [Modbus/TCP](https://netresec.com/?b=245092b) and [UMAS](https://netresec.com/?b=254caa9). The parsers for UMAS and IEC-104 have been updated in this release.

The parser for Schneider Electric’s proprietary UMAS protocol in NetworkMiner has been improved. NetworkMiner can now extract data from UMAS commands “Read Physical Address” and “Write Physical Address”. This addition enables analysts to determine not only if data stored in memory of a Schneider Modicon PLC has been modified, but also what changed. This visibility is particularly valuable when performing forensic analysis of OT network traffic after an incident.

![UMAS write in NetworkMiner 3.2](https://media.netresec.com/images/NetworkMiner _3-2_UMAS_write_539x412.png)

*Image: Data 0x43 written to address 0x0001FF4E on a Modicon M221 PLC*

NetworkMiner can parse most commands defined by the IEC 60870-5-104 protocol, which is used for monitoring and controlling systems in European and Asian power grids.

In this release we’ve added support for IEC-104 command ID 60 (C\_RC\_TA\_1) “Regulating step command with time tag CP56Time2a”, which is used to increase or decrease a data-point by one.

![IEC-104 DOWN command extracted by NetworkMiner 3.2](https://media.netresec.com/images/NetworkMiner_3-2_IEC-104_DOWN_539x260.webp)

*Image: Data-point at IOA 16 decremented using IEC-104 command ID 60*

**RADIUS**

NetworkMiner now includes a parser for the authentication and authorization protocol RADIUS. The parser extracts usernames, passwords (encrypted or hashed), IP addresses, messages and various RADIUS-specific identifiers.

![RADIUS credentials extracted with NetworkMiner 3.2](https://media.netresec.com/images/NetworkMiner_3-2_Credentials_RADIUS_539x511.webp)

*Image: Usernames and password related attributes extracted from RADIUS traffic*

![RADIUS parameters extracted with NetworkMiner 3.2](https://media.netresec.com/images/NetworkMiner_3-2_Parameters_RADIUS_539x759.webp)

*Image: Parameters extracted from RADIUS packets*

RADIUS traffic for the screenshots above comes from Wireshark’s [Sample Captures](https://wiki.wireshark.org/SampleCaptures) (radius\_localhost.pcap) and Johannes Weber’s [Ultimate PCAP](https://weberblog.net/the-ultimate-pcap/).

**JA4 Download in NetworkMiner Professional**

Many users of NetworkMiner Professional have received an error message saying “JA4 database download failed”.

![JA4 database download failed error](https://media.netresec.com/images/JA4-database-download-failed_199x133.png)

This error message is displayed when NetworkMiner Professional tries to download a JA4 database from FoxIO’s website ja4db.com. After consulting FoxIO in 2024, we implemented a solution that automatically retrieved the JA4 database and checked for updates every 30 days.

FoxIO no longer provides this database for download, which is why users saw “JA4 database download failed” messages. We apologize for any inconvenience this may have caused.

Version 3.2 no longer attempts to download this database.

**Bug Fixes and Other Improvements**

NetworkMiner 3.2 includes fixes for several bugs reported by Jeliazko Zlatev, which relate to how files are extracted from PCAP data (thank you Jeliazko!). We have also improved parsers for protocols like HTTP, SIP and DNS to extract even more data from the analyzed network traffic to the various tabs on the user interface.

**Upgrading to Version 3.2**

Users who have purchased NetworkMiner Professional can download version 3.2 from our [customer portal](https://www.netresec.com/portal/), or use the “Check for Updates” feature from NetworkMiner’s Help menu. Users who prefer to use the free and open source version can grab the latest release of NetworkMiner from the official [NetworkMiner page](https://www.netresec.com/?page=NetworkMiner).

Posted by Erik Hjelmvik on Wednesday, 07 October 2026 11:30:00 (UTC/GMT)

Tags:
#[NetworkMiner](/?page=Blog&tag=NetworkMiner)​
#[UMAS](/?page=Blog&tag=UMAS)​
#[IEC-104](/?page=Blog&tag=IEC-104)​
#[ICS](/?page=Blog&tag=ICS)​
#[JA4](/?page=Blog&tag=JA4)​

Short URL:
<https://netresec.com/?b=26Aa0d3>

### Recent Posts

» [NetworkMiner 3.2 Released](/?page=Blog&month=2026-10&post=NetworkMiner-3-2-Released)

» [Stop Feeding the SOC Garbage](/?page=Blog&month=2026-10&post=Stop-Feeding-the-SOC-Garbage)

» [Unmasking Malware Families](/?page=Blog&month=2026-09&post=Unmasking-Malware-Families)

» [PolarProxy 2.0.2 Released](/?page=Blog&month=2026-09&post=PolarProxy-2-0-2-Released)

» [OT Networks Still Need Monitoring](/?page=Blog&month=2026-08&post=OT-Networks-Still-Need-Monitoring)

» [CNCMachineRMS C2 Protocol](/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol)

» [PureLogs, PureRAT and misleading zgRAT](/?page=Blog&month=2026-07&post=PureLogs-PureRAT-and-misleading-zgRAT)

» [Ping32 RMM and ValleyRAT](/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT)

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