---
title: NetworkMiner 3.1 Released
url: https://www.netresec.com/?page=Blog&month=2025-12&post=NetworkMiner-3-1-Released
source: NETRESEC Network Security Blog
date: 2025-12-01
fetch_date: 2025-12-02T03:18:39.627896
---

# NetworkMiner 3.1 Released

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

Monday, 01 December 2025 08:20:00 (UTC/GMT)

## [NetworkMiner 3.1 Released](/?page=Blog&month=2025-12&post=NetworkMiner-3-1-Released)

![NetworkMiner 3.1 Logo](https://media.netresec.com/images/NetworkMiner_3-1_707x707.webp)

This [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) release brings improved extraction of artifacts like usernames, passwords and hostnames from network traffic. We have also made some updates to the user interface and continued our effort to extract even more details from malware C2 traffic.

**More Artifacts Extracted**

Usernames and passwords are now extracted from [Proxy-Authenticate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Proxy-Authenticate) headers. NetworkMiner’s username extraction support for SMTP [AUTH LOGIN](https://www.ietf.org/archive/id/draft-murchison-sasl-login-00.txt) requests has also been improved.

![Username and password extracted from Proxy-Authenticate HTTP request](https://media.netresec.com/images/NetworkMinerProfessional_Credentials_Proxy-Authenticate_526x285.webp)

*Image: Username and password extracted from HTTP Proxy-Authenticate header*

NetworkMiner has several methods for passively identifying host names of clients and servers. We’ve added a few additional hostname sources to this release, such as client hostnames from SMTP EHLO requests and TLS [SNI fields](https://www.rfc-editor.org/rfc/rfc3546#section-3.1) from [RDP](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol) traffic.

**User Interface Improvements**

The most significant user interface update in the 3.1 release is probably the new “Not in” keyword filter mode. I received this feature request when teaching a [network forensics class](https://www.netresec.com/?page=Training) (thanks for the great idea Lukas!). This filter mode is the opposite to the default “Exact Phrase” setting.

![NetworkMiner Professional with filter Not in HTTP](https://media.netresec.com/images/NetworkMinerProfessional_3-1_Parameters_HTTP_Not-in_521x479.webp)

*Image: Parameters extracted from anything but HTTP traffic in Johannes Weber's [Ultimate PCAP](https://weberblog.net/the-ultimate-pcap/)*

The “Not in” filter mode comes in very handy when the information you’re interested in is drowning in a sea of non-relevant, but easily identifiable, data.

**Malware C2 Traffic**

NetworkMiner can extract information from various malware Command-and-Control (C2) protocols like [IcedID BackConnect](https://netresec.com/?b=23A4de6), [Meterpreter](https://netresec.com/?b=22479d5), [njRAT](https://netresec.com/?b=2541a39), [Redline Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.redline_stealer), [Remcos](https://malpedia.caad.fkie.fraunhofer.de/details/win.remcos), [RMS](https://malpedia.caad.fkie.fraunhofer.de/details/win.rms) and [StealC](https://netresec.com/?b=245092b). The free version of NetworkMiner can extract information, such as commands or transferred files, from these malware protocols as long as the C2 server listens on a “standard” port number. But if the C2 server runs on some other port (which often is the case), then [NetworkMiner Professional](https://www.netresec.com/?page=BuyNetworkMiner)’s Port Independent Protocol Identification (PIPI) feature is required to identify the correct parser for the network traffic.

Implementing malware C2 protocol parsers is sometimes a thankless task because these protocols tend to get replaced at a much higher rate compared to legitimate network protocols. But it is an important task nevertheless.

**njRAT**

A popular malware for which the C2 protocol hasn’t changed much during the past decade is njRAT. In fact, new [njRAT samples](https://bazaar.abuse.ch/browse/signature/njRAT/) are discovered by security researchers pretty much every day despite it being a 13 years old trojan. NetworkMiner’s njRAT support has therefore been improved in this release. NetworkMiner can extract files that are uploaded or downloaded to/from a PC infected with njRAT. This file extraction feature also includes the ability to extract plugins for specific tasks, such as to run a reverse shell, see camera images or steal passwords. njRAT C2 servers transmit these plugins as gzip compressed DLL files to victim computers when needed.

![Files extracted from njRAT traffic by NetworkMiner](https://media.netresec.com/images/NetworkMinerProfessional_Linux_Files_njRAT_519x368.webp)

*Image: Files extracted from njRAT in PCAP from our [network forensics class](https://www.netresec.com/?page=Training)*

NetworkMiner extracts these gz compressed plugin DLL files to disk. A new feature in the 3.1 release is that it then decompresses the gz data and calculates an MD5 hash of the file contents, but without saving the decompressed data to disk. The MD5 hash of the transferred files are instead displayed on the Parameters tab as seen in this screenshot:

![MD5 hashes of njRAT plugin DLLs](https://media.netresec.com/images/NetworkMinerProfessional_Linux_Parameters_njRAT-MD5_519x368.webp)

*Image: MD5 hashes of njRAT plugin DLLs*

The following njRAT plugin MD5 hashes can be seen in this screenshot:

* [cef141d894400bc2e0096d1ed0c8f95b](https://www.virustotal.com/gui/file/9648ffd2eb53744c5f78dc8442a8bcbbe9831db1e198be370a62cbf9f51cd896/details) (aka inf.dll)
* [a73edb60b80a2dfa86735d821bea7b19](https://www.virustotal.com/gui/file/7a4977b024d048b71bcc8f1cc65fb06e4353821323f852dc6740b79b9ab75c98/details) (aka cam.dll)
* [a93349ba5e621cfb7a46dc9f401fd998](https://www.virustotal.com/gui/file/25d1969fb395caef8d9122f9befd597d0cb93a687d7703a42f06119d92520cc4/details) (aka plg.dll)
* [11375fb0cee4c06b5cefa2031ee2ed6d](https://www.virustotal.com/gui/file/9e0ccd6be2a8d6eb045363c44af34e7b1482856e64b4b9cfc3deae465e3cdccd/details) (aka pw.dll)
* [19967e886edcd2f22f8d4a58c8ea3773](https://www.virustotal.com/gui/file/3e5141c75b7746c0eb2b332082a165deacb943cef26bd84668e6b79b47bdfd93/details) (aka sc2.dll)

See our video [Decoding njRAT traffic with NetworkMiner](https://netresec.com/?b=2541a39) for a more in-depth demonstration of NetworkMiner’s njRAT parsing features.

**Redline Stealer**

Another common malware is [Redline Stealer](https://malpedia.caad.fkie.fraunhofer.de/details/win.redline_stealer). It uses a legitimate protocol called [MC-NMF](https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-nmf/) to send instructions and exfiltrate data from victim computers. Basic support for the MC-NMF protocol has therefore been added to NetworkMiner 3.1. MC-NMF is also used by legitimate services like Microsoft’s [Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview), so as a bonus you can now analyze such traffic with NetworkMiner as well. The MC-NMF protocol has a compression routine called [MC-NBFSE](https://learn.microsoft.com/en-us/openspecs/windows_protocols/mc-nbfse/3caf1ffa-6333-4c5f-8aa7-c06db4748c1b), which is utilized by Redline Stealer. NetworkMiner can’t decompress this format, so files are extracted to disk in compressed form.

![Files extracted by NetworkMiner from Redline Stealer traffic](https://media.netresec.com/images/NetworkMinerProfessional_Files_Redline-Stealer_511x401.webp)

Image: Files extracted from [Redline execution on Joe Sandbox](https://www.joesandbox.com/analysis/1815055)

You can probably spot some interesting details in the extracted data even when viewing the NBFSE compressed contents though.

![Contents of files extracted by NetworkMiner from Redline Stealer traffic](https://media.netresec.com/images/NetworkMiner_File-Details_Redline-NBFSE_801x804.webp...