---
title: CapLoader 2.1.0 Released
url: https://www.netresec.com/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released
source: NETRESEC Network Security Blog
date: 2026-05-27
fetch_date: 2026-05-28T06:02:38.497849
---

# CapLoader 2.1.0 Released

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

Wednesday, 27 May 2026 09:15:00 (UTC/GMT)

## [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

![CapLoader 2.1.0](https://media.netresec.com/images/CL_2-1-0_770x770.webp)

[CapLoader](https://www.netresec.com/?page=CapLoader) has been updated to version 2.1.0. The new release comes with better JA3/JA4 extraction and integration of additional threat-intel and OSINT services. We have also added support for more encapsulation protocols.

**TLS Client Hello Reassembly**

TLS handshakes no longer reliably fit in a single packet. Modern TLS features, like [post-quantum key exchanges](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/) and [Encrypted Client Hello](https://datatracker.ietf.org/doc/html/rfc9849) (ECH), often expand handshake sizes across multiple TCP segments. The same trend appears in QUIC traffic, where TLS handshakes now often are too large to fit in a single UDP packet.

As a result, packet‑analysis tools that parse live traffic or PCAP files (like CapLoader) must cache partial TLS handshakes and reassemble them to recover the complete TLS ClientHello messages. [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) and [FlowCarp](https://flowcarp.com/) already perform TLS handshake reassembly; CapLoader now supports it as well. This enables CapLoader to extract metadata from large TLS handshakes, including SNI hostnames, JA3 hashes and JA4 fingerprints.

![TLS and QUIC sessions in CapLoader 2.1.0.0](https://media.netresec.com/images/CapLoader_2-1-0-0_TLS-and-QUIC_1050x926.png)

The screenshot above shows CapLoader displaying information extracted from PCAP files that contain TLS and QUIC traffic with multi‑segment TLS 1.3 handshakes. The visible JA4 fingerprints for the client handshakes are:

* q13d0311h3\_55b375c5d22e\_5a1f323ef56d − HTTP/3 w/ ECH
* t13d1516h2\_8daaf6152771\_02713d6af862 − HTTP/2 w/ ECH
* t13d1517h2\_8daaf6152771\_b0da82dd1658 − HTTP/2 w/ ECH
* t13d1515h2\_8daaf6152771\_f37e75b10bcc − HTTP/2
* t13d1516h2\_8daaf6152771\_9b887d9acb53 − HTTP/2

All these handshakes support post-quantum key agreements with a 1216 byte X25519MLKEM768 key. The first three listed JA4 fingerprints also use ECH.

![JA4 fingerprint t13i010400_0f2cb44170f4_5c4c70b73fa0_518x136](https://www.netresec.com/images/JA4_t13i010400_0f2cb44170f4_5c4c70b73fa0_518x136.webp)

**Threat Intel and OSINT**

[CapLoader](https://www.netresec.com/?page=CapLoader) now matches network traffic against indicators of compromise (IOCs) from [Johannes Bader](https://infosec.exchange/%40viql)'s open source threat intelligence platform [Rösti](https://rosti.dev/). An alert is raised whenever the analysed traffic matches any of the following IOC types on Rösti:

* domain
* domain:port
* IP
* IP:port

When a match occurs, CapLoader raises an alert on the flow/service and includes the matching IOC type and value.
Rösti aggregates IOCs from public feeds, researchers, and threat‑intel providers (including IOCs published on this blog).

We have also extended the OSINT lookup shortcuts in CapLoader to include the following websites:

* [BGP.Tools](https://bgp.tools) (IP lookup)
* [IPinfo](https://ipinfo.io) (IP lookup)
* [Netify](https://www.netify.ai) (IP lookup)
* [ScanMalware](https://scanmalware.com) (domain, IP and ASN lookups)

Right-click a flow/service/host/alert in [CapLoader](https://www.netresec.com/?page=CapLoader) and select "Lookup [domain/IP/ASN] at...", which opens the chosen OSINT site in a browser tab with info about the domain/IP/ASN.

**Encapsulated Protocols**

CapLoader already decapsulates [GRE](https://datatracker.ietf.org/doc/html/rfc2784), [VXLAN](https://datatracker.ietf.org/doc/html/rfc7348), [CapWap](https://datatracker.ietf.org/doc/html/rfc5415), [Teredo](https://www.rfc-editor.org/rfc/rfc4380.html), [GTP-U](https://en.wikipedia.org/wiki/GPRS_Tunnelling_Protocol#GTP-U_-_GTP_user_data_tunneling), [TZSP](https://wiki.mikrotik.com/wiki/Manual%3ATools/Packet_Sniffer) as well as [IP-in-IP](https://datatracker.ietf.org/doc/html/rfc1853).

![Decapsulate all the things](https://media.netresec.com/images/Decapsulate_all-the-things_1336x1000.webp)

With this release we add support for extracting traffic from the following encapsulation protocols:

* Aruba GRE encapsulated WiFi
* Geneve ([RFC 8926](https://datatracker.ietf.org/doc/html/rfc8926))
* GRE in UDP ([RFC 8086](https://datatracker.ietf.org/doc/html/rfc8086)) to ports 4754 and 4755

**Improved Protocol Detection**

The precision of [CapLoader](https://www.netresec.com/?page=CapLoader)'s built-in port independent protocol identification has been improved and several additional protocols can now be detected, including [GSocket](https://www.gsocket.io/), Hioles, [Mirai](https://malpedia.caad.fkie.fraunhofer.de/details/elf.mirai), [Pulsar RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.pulsar_rat), [PureRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.pure_rat), [SVCStealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.svcstealer) and [XenoRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.xenorat).

Posted by Erik Hjelmvik on Wednesday, 27 May 2026 09:15:00 (UTC/GMT)

Tags:
#[CapLoader](/?page=Blog&tag=CapLoader)​
#[JA3](/?page=Blog&tag=JA3)​
#[JA4](/?page=Blog&tag=JA4)​
#[TLS](/?page=Blog&tag=TLS)​
#[QUIC](/?page=Blog&tag=QUIC)​
#[OSINT](/?page=Blog&tag=OSINT)​
#[encapsulation](/?page=Blog&tag=encapsulation)​
#[decapsulation](/?page=Blog&tag=decapsulation)​
#[GRE](/?page=Blog&tag=GRE)​

Short URL:
<https://netresec.com/?b=265c041>

### Recent Posts

» [CapLoader 2.1.0 Released](/?page=Blog&month=2026-05&post=CapLoader-2-1-0-Released)

» [PolarProxy 2.0 Released](/?page=Blog&month=2026-05&post=PolarProxy-2-0-Released)

» [Remcos Alerts from FlowCarp in EveBox](/?page=Blog&month=2026-05&post=Remcos-Alerts-from-FlowCarp-in-EveBox)

» [FlowCarp Identifies Protocols](/?page=Blog&month=2026-05&post=FlowCarp-Identifies-Protocols)

» [CISA mixup of IOC domains](/?page=Blog&month=2026-02&post=CISA-mixup-of-IOC-domains)

» [njRAT runs MassLogger](/?page=Blog&month=2026-02&post=njRAT-runs-MassLogger)

» [Decoding malware C2 with CyberChef](/?page=Blog&month=2026-01&post=Decoding-malware-C2-with-CyberChef)

» [Latrodectus BackConnect](/?page=Blog&month=2025-12&post=Latrodectus-BackConnect)

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
[Privac...