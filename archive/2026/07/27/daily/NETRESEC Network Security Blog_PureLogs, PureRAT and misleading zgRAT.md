---
title: PureLogs, PureRAT and misleading zgRAT
url: https://www.netresec.com/?page=Blog&month=2026-07&post=PureLogs-PureRAT-and-misleading-zgRAT
source: NETRESEC Network Security Blog
date: 2026-07-27
fetch_date: 2026-07-28T04:59:56.466842
---

# PureLogs, PureRAT and misleading zgRAT

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

Monday, 27 July 2026 16:00:00 (UTC/GMT)

## [PureLogs, PureRAT and misleading zgRAT](/?page=Blog&month=2026-07&post=PureLogs-PureRAT-and-misleading-zgRAT)

![No to zgRAT](https://media.netresec.com/images/zgRAT-refusal_1200x1200.webp)

Please stop classifying malware as zgRAT. That malware label is confusing. As far as I know, there isn’t a proper definition of what zgRAT actually is. Some claim that zgRAT is the same malware family as PureLogs, while others argue that zgRAT should be mapped to PureRAT. There is also a [blog post](https://any.run/cybersecurity-blog/pure-malware-family-analysis/) by malware analysts khr0x and Jane where they clearly state that PureLogs is not the same thing as zgRAT.

Despite the similar names PureLogs and PureRAT are not the same type of malware. PureLogs is an infostealer, while PureRAT is a Remote Access Trojan (RAT). Both are, however, built using .NET and are developed by PureCoder.

We previously helped [clear up](https://netresec.com/?b=2589522) confusion around labels like ResolverRAT and PureHVNC, which were used in the past to refer to PureRAT malware samples. I hope this post helps reduce misunderstandings caused by the use of zgRAT.

**Naming malware and threat actors**

Malware labels and threat-actor labels serve different purposes. Publicly attributing an attack to a real-world organization might cause political turmoil, which can be avoided by using a threat-actor alias instead. Threat-actor aliases also often reflect each organization’s access to evidence and internal clustering process. As a result, multiple aliases for the same actor can coexist.

Malware-family labels, on the other hand, are usually more deterministic. Given a hash of a malware sample, researchers generally know they’re looking at the exact same artifact. For that reason, the most useful practice is to use the same name as the malware developers or the earliest widely adopted naming and use “unknown” or “unidentified” when classification is unclear. This reduces label fragmentation and downstream confusion when the same label is reused for different malware families.

**Why zgRAT causes confusion**

Many zgRAT signatures consistently match PureLogs, while others match PureRAT. There’s also a fairly popular YARA rule called “MALWARE\_Win\_zgRAT” that matches pretty much [any binary protected with .NET Reactor](https://blog.washi.dev/posts/misconceptions-about-dotnet). Taken together, this creates a solid foundation for false positives and misunderstandings stemming from the zgRAT label. And without a proper definition of what zgRAT actually is, such as a consistent mapping to a single malware family, false positives and misclassifications involving the zgRAT label are much harder to spot and weed out.

**PureLogs**

![info stealer](https://media.netresec.com/images/stealer_800x889.webp)

[PureLogs](https://malpedia.caad.fkie.fraunhofer.de/details/win.purelogs) is an infostealer that automatically collects and exfiltrates credentials and sensitive data from infected hosts, including browser-stored logins, credit card numbers, cookies, crypto-wallet data, VPN credentials and credentials for various chat/messaging platforms.

PureLogs uses a custom binary protocol to exfiltrate stolen data. As of PureLogs v5.0 the network traffic is often wrapped in TLS, thereby making it harder to detect on the network.

Default ports:

* TCP 7702 (non-TLS)
* TCP 8443 (TLS)

*Server ports are configurable, but the default ports are often used.*

Suricata signatures for non-TLS PureLogs traffic:

* 2048901 ET MALWARE [ANY.RUN] zgRAT / PureLogs Stealer C2 Connection M2
* 2061601 ET MALWARE zgRAT / PureLogs Stealer GZIP Exfiltration Outbound
* 2061633 ET MALWARE PureLogs Backdoor Server GZIP C2 Traffic
* 2061634 ET MALWARE PureLogs Backdoor Client GZIP C2 Traffic
* 2063215 ET MALWARE zgRAT / PureLogs Stealer C2 Server Connection M3

Selected suricata signatures (not exhaustive) for TLS encrypted PureLogs traffic:

* 903209570 SSLBL: Malicious SSL certificate detected (PureHVNC C&C)
* 903209620 SSLBL: Malicious SSL certificate detected (PureHVNC C&C)
* 903209854 SSLBL: Malicious SSL certificate detected (PureLogsStealer C&C)
* 903210180 SSLBL: Malicious SSL certificate detected (PureLogsStealer C&C)

FlowCarp protocol names:

* PureLogs
* TLS, PureLogs

Recent PureLogs examples:

* [404f0d36fcbe5c4643e821403a4827eb](https://bazaar.abuse.ch/sample/0cb54132e0a6c763044968293effe0794ae787435ca616a626245d23e2291b11/) 204.44.93.88:8449
* [7e49bac468548a0e83133f0d5b02544b](https://bazaar.abuse.ch/sample/1cd9e489da7d5a543a219458d60fae774c3c7771a2d60bbe3a6217bbf8fbe626/) 5.101.84.75:4242
* [3c9852c53cb45221886b34ed6bc7d674](https://bazaar.abuse.ch/sample/f273dfb134166251f00456f8fcff32a827afa03781794f8071281dcadc37b444/) 46.151.182.159:776

**PureRAT**

![Trojan Horse](https://media.netresec.com/images/trojan-horse_800x834.webp)

[PureRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.pure_rat) is a Remote Access Trojan (RAT) with many built-in features for live interaction with infected hosts, such as:

* Hidden VNC (HVNC) and remote desktop with mouse and keyboard control
* Viewing the webcam
* Listening to the microphone
* Real-time keylogging
* Remote command prompt
* Reverse proxy (HTTP and SOCKS5)
* Code injection

PureRAT previously used [a flawed TLS implementation](https://netresec.com/?b=2589522) that could be easily detected on the network. The current TLS implementation is much more difficult to spot.

Default C2 ports:

* TCP 56001
* TCP 56002
* TCP 56003

*Server ports are configurable, but the default ports are often used.*

Selected suricata signatures (not exhaustive) for PureRAT traffic:

* 2035595 ET MALWARE Generic AsyncRAT/zgRAT Style SSL Cert
* 2070181 ET MALWARE PureRAT TLS Certificate Observed (PureRAT Agent)
* 903208736 SSLBL: Malicious SSL certificate detected (PureHVNC C&C)
* 903209136 SSLBL: Malicious SSL certificate detected (PureLogsStealer C&C)
* 903209139 SSLBL: Malicious SSL certificate detected (PureLogsStealer C&C)
* 903209682 SSLBL: Malicious SSL certificate detected (ResolverRAT C&C)
* 906200096 SSLBL: Malicious JA3 SSL-Client Fingerprint detected (AsyncRAT)

FlowCarp protocol names:

* PureRAT
* TLS, PureRAT

PureRAT sample examples:

* [323fed78fc8aaa86c3d35aa85313645d](https://bazaar.abuse.ch/sample/e937e353759cb981feb958f6fc54cc4922169260a9eaa8f1d7266c14b53fe7ce/) 85.239.149.178:56001
* [b4400998cf293b0767455fb37526b18e](https://bazaar.abuse.ch/sample/5a3938aa0350f3bf94c8f12cab8b9b0555648c20176fe9166a91240c4b27fa18/) 196.251.107.6:56001
* [010301d23beacee631006245ed09a2f7](https://bazaar.abuse.ch/sample/794331fd4fd48600ebee0c579517f3a7122a87a2bf8e2da18dfc8d5d57c0da93/) 45.192.211.59:56001

**Detection notes**

As you can see, both PureLogs and PureRAT traffic can trigger Suricata alerts with signatures labeled as “zgRAT”. There are also still signatures using outdated names like “PureHVNC” and “ResolverRAT”. Luckily, analysts know that the alert label often doesn’t map to the correct malware family. The alert labels merely reflect how the rule author named the suspected malware at creation time. Nevertheless, the fact that the “zgRAT“ label is used for PureLogs as well as PureRAT signatures contributes to the confusion regarding what zgRAT actually is.

I use [FlowCarp](https://flowcarp.com/) to identify PureLogs and PureRAT traffic and to tell them apart. FlowCarp uses statistical methods for identifying the C2 protocol, which allows it to identify PureLogs as well as PureRAT traffic without having to track every new X.509 certificate that the C2 se...