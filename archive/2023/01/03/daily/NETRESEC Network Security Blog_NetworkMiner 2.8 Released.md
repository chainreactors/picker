---
title: NetworkMiner 2.8 Released
url: https://www.netresec.com/?page=Blog&month=2023-01&post=NetworkMiner-2-8-Released
source: NETRESEC Network Security Blog
date: 2023-01-03
fetch_date: 2025-10-04T02:55:52.645405
---

# NetworkMiner 2.8 Released

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

Monday, 02 January 2023 08:00:00 (UTC/GMT)

## [NetworkMiner 2.8 Released](/?page=Blog&month=2023-01&post=NetworkMiner-2-8-Released)

![NetworkMiner 2.8](https://www.netresec.com/images/NetworkMiner_2-8_200x200.png)

I am happy to announce the release of NetworkMiner 2.8 today! This new version comes with an improved user interface, better parsing of IEC-104 traffic and decapsulation of CAPWAP traffic. The professional edition of NetworkMiner additionally adds port-independent detection of SMTP and SOCKS traffic, which enables extraction of emails and tunneled traffic even when non-standard ports are used.

**User Interface Improvements**

The first thing you see when starting [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) is the Hosts tab, which now has been updated to include a filter text box. This text box can be used to filter the displayed hosts based on the property fields they contain. By entering “Android” into the filter box NetworkMiner will show only the hosts having a property containing the string “Android”, for example in the OS classification or User-Agent string. Other properties you might find useful to filter on are hostname, JA3 hash and MAC address.
If you’re running NetworkMiner Professional then you’ll also be able to filter on Country thanks to the offline IP-to-Country database included in the Pro edition.

![NetworkMiner with Hosts filter Android](https://www.netresec.com/images/NetworkMiner_2-8_Hosts_Filter-Android_520x829.png)

It’s now also possible to copy text from most tabs in NetworkMiner with Ctrl+C or by right-clicking and selecting “Copy selected rows”. A maximum of 10 rows can be copied at a time using the free version of NetworkMiner, while the [Professional version](https://www.netresec.com/?page=BuyNetworkMiner) allows all rows to be copied in one go.

The content based file type identification introduced in [NetworkMiner 2.7](https://netresec.com/?b=21644b7) has been improved to also differentiate between EXE and DLL files as of version 2.8.

![Matanbuchus malware download in NetworkMiner](https://www.netresec.com/images/NetworkMiner_2-8_FileDetails_d733d96a25fd14f4494f6d76f9ff9892_Matanbuchus-DLL_506x407.png)

* Matanbuchus malware DLL disguised as PNG
* MD5: d733d96a25fd14f4494f6d76f9ff9892
* Source: [2022-06-17-Matanbuchus-with-Cobalt-Strike.pcap](https://www.malware-traffic-analysis.net/2022/06/17/index.html)

![Malicious AutoIt binary extracted from network traffic by NetworkMiner](https://www.netresec.com/images/NetworkMiner_2-8_FileDetails_c56b5f0201a3b3de53e561fe76912bfd_AutoIt_EXE_506x407.png)

* AutoIt EXE disguised as ZIP file
* MD5: c56b5f0201a3b3de53e561fe76912bfd
* Source: [2022-08-19-Astaroth-Guildma-infection-traffic.pcap](https://www.malware-traffic-analysis.net/2022/08/19/index.html)

**IEC 60870-5-104**

NetworkMiner’s parser for the SCADA protocol [IEC 60870-5-104](https://en.wikipedia.org/wiki/IEC_60870-5#IEC_60870-5-104) (IEC-104) has been significantly improved in version 2.8. NetworkMiner now supports more IEC-104 commands and the commands are presented on the Parameters tab in a clearer way than before.

![IEC-104 traffic in NetworkMiner](https://www.netresec.com/images/NetworkMiner_2-8_Parameters_IEC-104_520x347.png)

*Image: IEC-104 commands sent by the [Industroyer2](https://netresec.com/?b=224e357) malware*

I’m also proud to announce that NetworkMiner 2.8 now extracts files transferred over the IEC-104 protocol. More details about that particular feature is available in our [IEC-104 File Transfer Extraction](https://netresec.com/?b=231efae) blog post.

**CAPWAP Decapsulation**

NetworkMiner 2.8 can read IEEE 802.11 packets inside CAPWAP tunnels between WLAN Controllers and Access Points. This feature allows WiFi traffic to be analyzed without having to capture packets in the air.

**Reading PCAP from a Named Pipe**

NetworkMiner previously allowed packets to be read from [PacketCache](https://www.netresec.com/?page=PacketCache) over a named pipe. This feature has been upgraded to allow a PCAP stream to be read from any named pipe, not just from PacketCache.
Here’s an example showing how to capture packets from localhost for 10 seconds with [RawCap](https://www.netresec.com/?page=RawCap) and make those packets available via a named pipe called “RawCap”:

RawCap.exe -s 10 127.0.0.1 \\.\pipe\RawCap

RawCap will start capturing packets once a PCAP reader connects to the “RawCap” named pipe, which now can be done with NetworkMiner by clicking “Read from Named Pipe” on the File menu.

![Read PCAP from Named Pipe](https://www.netresec.com/images/NetworkMiner_2-8_ReadPCAPfromNamedPipe_396x215.png)

**Bug Fixes**

NetworkMiner previously produced incorrect JA3S signatures for TLS servers if they sent Session ID values in Server Hello messages or listed only one supported TLS version using the Supported Versions extension. These bugs have now been fixed in NetworkMiner 2.8.

NetworkMiner’s live sniffing feature has been improved to better handle huge packets caused by [Large Send Offload](https://en.wikipedia.org/wiki/TCP_offload_engine#Large_send_offload) (LSO). NetworkMiner previously crashed with an error message saying that the received packet was “larger than the internal message buffer” when attempting to capture a too large packet.

TCP sessions occasionally didn’t show up in NetworkMiner’s Sessions tab previously if the application layer protocol was unknown. This bug has now been fixed in version 2.8.

**New Features in NetworkMiner Professional**

NetworkMiner Professional includes a feature for port independent protocol detection of protocols like FTP, HTTP, IRC, Meterpreter, SSH and TLS, which enables extraction of artifacts from those protocols even though the service is running on a non-standard port. This new release adds two additional protocols to the collection of identified protocols, namely SMTP and SOCKS. This allows analysts to extract emails from spam runs sent to ports other than 25 or 587, as well as to see what goes on inside covert SOCKS tunnels running on non-standard ports.

![SMTP usernames and passwords extracted from SMTP traffic](https://www.netresec.com/images/NetworkMinerProfessional_2-8_Credentials_SMTP_censored_520x247.png)

*Image: SMTP credentials extracted from spam run to non-standard SMTP port*

In addition to allowing hosts to be filtered using string and regex matching, NetworkMiner Professional also allows the discovered hosts to be filtered on IP address using [CIDR notation](https://www.shellhacks.com/cidr-notation-explained-examples/), such as “192.168.1.0/24” or “10.0.0.0/8”.

![NetworkMiner with CIDR filter 192.168.88.0/24](https://www.netresec.com/images/NetworkMinerProfessional_2-8_Hosts_CIDR_520x284.png)

*Image: NetworkMiner Professional with CIDR filter 192.168.88.0/24*

Here are some IPv4 and IPv6 CIDR filters that you might find useful:

* 224.0.0.0/4 = IPv4 multicast (224/4 is also supported)
* 127.0.0.0/8 = IPv4 loopback (127/8 is also supported)
* fe80::/10 = IPv6 link-local addresses
* ff00::/8 = IPv6 multicast
* 0.0.0.0/0 = IPv4 hosts (0/0 is also supported)
* 0::/0 = IPv6 hosts

**Credits**

We’d like to thank René Perraux, Matt Smith and Anand Kumar Singh for reporting bugs that have been fixed in this new release.

**Upgrading to Version 2.8**

Users who have purchased NetworkMiner Professional can download a free update to version 2.8 from our [customer portal](https://www.netresec.com/portal/), or use the “Check for Updates” feature from NetworkMiner's Help menu. Those who instead prefer to use the free and open source version can grab the late...