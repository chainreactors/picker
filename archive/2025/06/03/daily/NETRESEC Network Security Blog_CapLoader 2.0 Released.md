---
title: CapLoader 2.0 Released
url: https://www.netresec.com/?page=Blog&month=2025-06&post=CapLoader-2-0-Released
source: NETRESEC Network Security Blog
date: 2025-06-03
fetch_date: 2025-10-06T22:56:28.454898
---

# CapLoader 2.0 Released

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

Monday, 02 June 2025 13:47:00 (UTC/GMT)

## [CapLoader 2.0 Released](/?page=Blog&month=2025-06&post=CapLoader-2-0-Released)

![CapLoader 2.0](https://media.netresec.com/images/CapLoader_2-0_Logo_770x770.webp)

I am thrilled to announce the release of [CapLoader](https://www.netresec.com/?page=CapLoader) 2.0 today!

This major update includes a lot of new features, such as a QUIC parser, alerts for threat hunting and a feature that allow users to define their own protocol detections based on example network traffic.

**User Defined Protocols**

CapLoader's [Port Independent Protocol Identification](https://netresec.com/?b=15A1776) feature can currently detect over 250 different protocols without having to rely on port numbers. This feature can be used to alert on rogue services like SSH, FTP, VPN and web servers that have been set up on non-standard ports to go unnoticed. But what if you want to detect traffic that isn’t using any of the 250 protocols that CapLoader identifies? CapLoader 2.0 includes a fantastic solution that solves this problem! Simply right-click a flow containing the traffic you want to identify and select “Define protocol from flow”. This creates a custom local protocol detection model based on the selected traffic.

CapLoader’s protocol identification feature may seem like magic, but it actually relies on several different statistical measurements of the traffic in order to build a model of how the protocol behaves. It's possible to define a protocol model from just a single flow, but doing so may lead to poor detection results, which is why we recommend defining protocols from at least 10 different flows. You can do this either by selecting multiple flows or services before clicking “Define protocol from” or by adding additional flows or services to a protocol model at a later point by clicking “Add flow to protocol definition”.

**More Malware Protocols Detected**

There are several malware C2 protocols among CapLoader’s built-in models for protocol identification. The 2.0 release has been extended to detect even more malware protocols out of the box, such as
[Aurotun Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.aurotun_stealer), [PrivateLoader](https://malpedia.caad.fkie.fraunhofer.de/details/win.privateloader), [PureLogs](https://malpedia.caad.fkie.fraunhofer.de/details/win.purelogs), [RedTail](https://malpedia.caad.fkie.fraunhofer.de/details/elf.redtail), [ResolverRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.resolver_rat), [SpyMAX](https://malpedia.caad.fkie.fraunhofer.de/details/apk.spymax), [SpyNote](https://malpedia.caad.fkie.fraunhofer.de/details/apk.spynote) and [ValleyRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.valley_rat).

These protocols can now be detected using CapLoader regardless which IP address or port number the server runs on.

**QUIC Parser**

CapLoader now parses the QUIC protocol, which typically runs on UDP port 443 and transports TLS encrypted HTTP/3 traffic. CapLoader doesn’t decrypt the TLS encrypted HTTP/3 traffic though, it only parses the initial QUIC packets containing the client’s TLS handshake to extract the target domain name from the [SNI extension](https://en.wikipedia.org/wiki/Server_Name_Indication) and generates JA3 hashes and [JA4 fingerprints](https://github.com/FoxIO-LLC/ja4) of the client’s TLS handshake.

![QUIC network traffic from Active Countermeasures shown in CapLoader's services tab](https://media.netresec.com/images/CapLoader_Services_QUIC_ActiveCountermeasures_520x505.png)

*Image: QUIC traffic from [Active Countermeasures](https://www.activecountermeasures.com/category/malware-of-the-day/)*

* Merlin C2 JA3: 203c2306834e5bf5ace01fb74ad1badf
* Merlin C2 JA4: q13i0311h3\_55b375c5d22e\_c183556c78e2

**More Alerts**

There’s a fantastic service called [ThreatFox](https://threatfox.abuse.ch), to which security researchers, incident responders and others share indicators of compromise (IOC). Many of the shared IOCs are domain names and IP addresses used by malware for payload delivery, command-and-control (C2) or data exfiltration. Various IOC lists can be [downloaded from ThreatFox](https://threatfox.abuse.ch/export/), so that they can be used by a [DNS firewall](https://dnsrpz.info/) or a [TLS firewall](https://tlsfirewall.com) to block malware traffic. But the IOCs can also be used for alerting and threat hunting. CapLoader downloads two IOC lists from ThreatFox when the tool is started (the data is then cached for 24 hours, so that no new download is needed until the next day). Analyzed network traffic is then matched against these downloaded offline databases to provide alerts whenever there is traffic to a domain name or IP address that has been reported to be associated with malware.

![CapLoader alerts for Lumma and Remcos traffic to servers listed on ThreatFox](https://media.netresec.com/images/CapLoader_Alerts_ThreatFox_Lumma_Remcos_521x451.png)

*Image: Alerts for traffic to [Lumma Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.lumma) and [Remcos](https://malpedia.caad.fkie.fraunhofer.de/details/win.remcos) servers listed on ThreatFox*

We’ve also added two additional alert types in this release, one for anomalous TLS handshakes, and one for connections to suspicious domains. Both these alerts are designed primarily for threat hunting, since there’s a considerable risk that they will alert on legitimate traffic. The anomalous TLS handshake alert tries to detect odd TLS connections that are not originating from the user’s web browser or the operating system. The alert is triggered when such odd connections are made to domain names that are not well-known. This alert logic is designed to generically detect any TLS encrypted malware traffic, where the malware is using a custom TLS library instead of relying on operating system API calls for establishing encrypted connections. But this logic might also lead to false positive alerts, for example when legitimate applications use custom TLS libraries to perform tasks like checking a license or looking for software updates. The suspicious domain alert looks for connections to domain names like devtunnels.ms, ngrok.io and mocky.io, which are often [used by APTs](https://infosec.exchange/%40netresec/114552524778145250) as well as crime groups.

**Metrics for VPN Detection**

CapLoader 2.0 displays the TCP [MSS](https://en.wikipedia.org/wiki/Maximum_segment_size) values on the Hosts tab. This value can help with determining if a host is behind a VPN. An MSS value below 1400 indicates that the host’s traffic might pass through some form of overlay network, such as a tunnel or VPN. Other indicators that can help identify VPN and tunnelled traffic is IP [TTL](https://en.wikipedia.org/wiki/Time_to_live) and latency, which CapLoader also displays in the hosts tab.

![Client traffic coming out of VPN concentrator with low MSS value](https://media.netresec.com/images/CapLoader_Hosts_TCP-MSS-1355-VPN-markup_520x504.webp)

**Improved User Experience**

A lot of effort has been put into improving the user interface and general user experience for this new CapLoader release. One very important user experience factor is the responsiveness of the user interface, which has been significantly improved. Actions like sorting and filtering flows, services or alerts in CapLoader now complete around 10 times faster than before, which is very noticeable when working with multi-gigabyte capture files. Another improvement related to working with large capture files is that CapLoader now uses significantly less memory.

The trans...