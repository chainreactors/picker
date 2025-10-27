---
title: Comparison of tools that extract files from PCAP
url: https://www.netresec.com/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP
source: NETRESEC Network Security Blog
date: 2025-05-06
fetch_date: 2025-10-06T22:30:46.767973
---

# Comparison of tools that extract files from PCAP

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

Monday, 05 May 2025 16:05:00 (UTC/GMT)

## [Comparison of tools that extract files from PCAP](/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP)

One of the premier features in [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) is the ability to extract files from captured network traffic in [PCAP files](https://netresec.com/?b=22A1c18). NetworkMiner reassembles the file contents by parsing protocols that are used to transfer files across a network.

But there are other tools that also can extract files from PCAP files, such as [Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html) and [Zeek](https://docs.zeek.org/en/lts/scripts/policy/frameworks/files/extract-all-files.zeek.html). The file extraction support in these alternative solutions sometimes complement and sometimes overlap with that of NetworkMiner. Either way it is good that there are multiple tools that are designed to perform the same task. This allows us to compare the output from the different implementations, for example if the results from one tool seems strange or is suspected to be incorrect or incomplete.

![comparing apple to orange](https://media.netresec.com/images/compare-apple-orange_purple_2000x1000.webp)

Tools that can reassemble and extract files from network traffic or PCAP files:

* [Chaosreader](https://github.com/brendangregg/Chaosreader) (hasn't been updated since 2014)
* [NetworkMiner](https://www.netresec.com/?page=NetworkMiner)
* [Suricata](https://docs.suricata.io/en/suricata-7.0.4/file-extraction/file-extraction.html)
* [tcpflow](https://github.com/simsong/tcpflow) (-e all)
* Wireshark's [Export Objects](https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html)
* Zeek's [extract-all-files.zeek](https://docs.zeek.org/en/lts/scripts/policy/frameworks/files/extract-all-files.zeek.html)

All of these tools can extract files from HTTP and FTP, but when it comes to other protocols the support varies. The following table summarizes which protocols each tool supports:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Chaos​reader | Network​Miner | Suri​cata | tcp​flow | Wire​shark | Zeek |
| FTP | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HTTP/2 |  | ✅ | ❓ |  | ✅ |  |
| IEC-104 |  | [✅](https://netresec.com/?b=231efae) |  |  |  |  |
| IMAP |  | ✅ |  |  | ✅ |  |
| LPR |  | ✅ |  |  |  |  |
| NFS |  |  | ✅ |  |  |  |
| njRAT |  | [✅](https://netresec.com/?b=2541a39) |  |  |  |  |
| POP3 |  | ✅ |  |  | ✅ | ✅ |
| SMB |  | ✅ | ✅ |  | ✅ | ✅ |
| SMB2/3 |  | ✅ | ✅ |  | ✅ | ✅ |
| SMTP | ✅ | ✅ | ✅ |  | ✅ | ✅ |
| TFTP |  | ✅ |  |  | ✅ |  || TLS certs |  | ✅ |  |  |  | ✅ |

I’ve been quite forgiving when compiling the table above. Tools are listed as supporting a protocol even if they only work under very specific conditions. I don’t want to name-and-shame any tool, but I strongly recommend that you verify the tools you’re using by comparing what they extract to one or two alternative tools. As an example, some tools only support a few specific commands for the protocol they claim to support. Additionally, some tools only support file extraction in one direction for protocols like HTTP or FTP, even though these protocols are regularly used to download as well as upload files.

Posted by Erik Hjelmvik on Monday, 05 May 2025 16:05:00 (UTC/GMT)

Tags:
#[Extract](/?page=Blog&tag=Extract)​
#[PCAP](/?page=Blog&tag=PCAP)​
#[NetworkMiner](/?page=Blog&tag=NetworkMiner)​
#[Suricata](/?page=Blog&tag=Suricata)​
#[tcpflow](/?page=Blog&tag=tcpflow)​
#[Wireshark](/?page=Blog&tag=Wireshark)​
#[Zeek](/?page=Blog&tag=Zeek)​
#[FTP](/?page=Blog&tag=FTP)​
#[HTTP](/?page=Blog&tag=HTTP)​
#[IEC-104](/?page=Blog&tag=IEC-104)​
#[IMAP](/?page=Blog&tag=IMAP)​
#[LPD](/?page=Blog&tag=LPD)​
#[LPR](/?page=Blog&tag=LPR)​
#[njRAT](/?page=Blog&tag=njRAT)​
#[POP3](/?page=Blog&tag=POP3)​
#[SMB](/?page=Blog&tag=SMB)​
#[SMB2](/?page=Blog&tag=SMB2)​
#[SMTP](/?page=Blog&tag=SMTP)​

Short URL:
<https://netresec.com/?b=255329f>

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