---
title: What is a PCAP file?
url: https://www.netresec.com/?page=Blog&month=2022-10&post=What-is-a-PCAP-file
source: NETRESEC Network Security Blog
date: 2022-10-28
fetch_date: 2025-10-03T21:09:39.062083
---

# What is a PCAP file?

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

Thursday, 27 October 2022 06:50:00 (UTC/GMT)

## [What is a PCAP file?](/?page=Blog&month=2022-10&post=What-is-a-PCAP-file)

A PCAP file is a container for packets captured on a computer network, such as a WiFi or Ethernet network. Each packet in a PCAP file is tagged with a timestamp indicating when it was captured.

The term PCAP is short for Packet CAPture. Other common names are capture file, trace file, packet trace, packet dump, dumpfile and pcap savefile.
The PCAP file format was created by [Van Jacobson](https://en.wikipedia.org/wiki/Van_Jacobson), [Craig Leres](https://crd.lbl.gov/divisions/scidata/about-scidata/office-of-the-director/craig-leres/) and [Steven McCanne](https://twitter.com/SteveMcCanne) around 1987 as part of the work they did on tcpdump and libpcap at the Lawrence Berkeley Laboratory.

File endings: .pcap .cap .dmp .trc
Media type: application/vnd.tcpdump.pcap

**PCAP File Header Format**

A PCAP file always starts with a 24 byte header,
referred to as [pcap\_file\_header](https://github.com/the-tcpdump-group/libpcap/blob/22813e20e8f1f1a1c1a4cd95cc06cd1e422a9dc0/pcap/pcap.h#L207) in the libpcap source code,
which contains the following fields:

* Magic Number (4 bytes) = d4 c3 b2 a1
* Version Major (2 bytes) = 02 00
* Version Minor (2 bytes) = 04 00
* Timezone (4 bytes) = 00 00 00 00
* Timestamp Accuracy (4 bytes) = 00 00 00 00
* Snap Length (4 bytes)
* Link-Layer Type (4 bytes)

As shown above, the first 16 bytes in the PCAP header have fixed values. There is one common exception though, which is when the field values are encoded as big endian rather than little endian.
A big endian capture file typically starts with these 8 bytes:

* Magic Number (4 bytes) = a1 b2 c3 d4
* Version Major (2 bytes) = 00 02
* Version Minor (2 bytes) = 00 04

There are a few additional magic number variants, such as “4d 3c b2 a1” used to indicate nanosecond timestamps and FRITZ!Box’s “34 cd b2 a1”, as well as big endian versions of those magic numbers.

The timezone and accuracy fields aren’t used in practice, they should therefore be all zeroes.

The snap length value is a 32 bit number indicating the maximum packet size that can be stored in the PCAP without truncating the packet data. This value is often “00 00 04 00” (256 kB) or “ff ff 00 00” (65535 bytes), but can in theory be any value except zero.

The link layer type defines which type of packets the capture file contains.
As an example, if the link-layer field is “01 00 00 00” in a little endian PCAP file,
then all packets in that file should be parsed as Ethernet packets.

Some of the most common link-layer type values are:

* 01 00 00 00 = [IEEE 802.3 Ethernet](https://en.wikipedia.org/wiki/IEEE_802.3)
* 65 00 00 00 = Raw IP packets (no layer 2 header)
* 69 00 00 00 = IEEE 802.11 (WiFi)
* 71 00 00 00 = SLL ([Linux "cooked" capture encapsulation](https://www.tcpdump.org/linktypes/LINKTYPE_LINUX_SLL.html))
* 77 00 00 00 = Prism header + IEEE 802.11 (WiFi)
* 7f 00 00 00 = Radiotap header + IEEE 802.11 (WiFi)
* c3 00 00 00 = IEEE 802.15.4 (Zigbee)
* c5 00 00 00 = [Endace ERF](https://netresec.com/?b=12B3A4A)
* e4 00 00 00 = Raw IPv4 (no layer 2 header)

A list of all link layer type values is [available](https://www.tcpdump.org/linktypes.html) on the tcpdump website.

**Packet Header Format**

Each captured packet in a PCAP file is prefixed by a 16 byte header,
referred to as [pcap\_sf\_pkthdr](https://github.com/the-tcpdump-group/libpcap/blob/7b955929deb75804ec74dffc2934cbef7c1196c6/pcap-int.h#L422) in the libpcap source code,
which contains the following fields:

* Timestamp Seconds (4 bytes)
* Timestamp Microseconds (4 bytes)
* Captured Length (4 bytes)
* Original Length (4 bytes)

The “timestamp seconds” field is a standard epoch or Unix time field, indicating the number of seconds that have elapsed since 1 January 1970. As you’ve probably guessed, the microsecond field indicates the microsecond fractions of the packet timestamp. However, PCAP files with the magic number “4d 3c b2 a1” in the file header use this field to represent nanosecond fractions instead. The nanosecond variant makes a lot of sense, since only 20 bits of this 32 bit field are used when representing microsecond fractions, but 30 bits are needed to represent nanosecond fractions.

The captured length field indicates the number of bytes of packet data that follows after the 16 byte packet header. This value should never be larger than the snap length value in the PCAP file header.

The original length field indicates the size of the actual packet on the network. This value is typically the same as the captured length, provided that a large enough snap length was used when capturing packets.

**Packet Data**

Following right after each packet header is the actual packet data that was being transferred over the network. This data is written to the PCAP file exactly as it was received, without caring about endianness or correctness of the data.

Now that I’ve covered all the different parts of a PCAP file, let’s have a look at the contents of an actual PCAP file.

![Hex view of PCAP file](https://www.netresec.com/images/PCAP-header-hex_520x260.png)

The data in the illustration above was cut off after the second packet header, but you get the idea. A PCAP file can contain an unlimited number of packet headers and packets, but there can only be one PCAP file header per file.

I’d also like to stress the fact that the endianness defined in the PCAP file header doesn’t affect how the packet data gets stored in the packet data. Most network protocols use big endian encoding, but most PCAP files — including the one in the illustration above — use little endian. That’s why the TCP destination port 80 is encoded as “00 50” in the packet data, even though the little endian “d4 c3 b2 a1” magic number is specified in the PCAP file header.

**Other Packet Capture Formats**

The PCAP file format is by far the most widely used one for storing packet data, but it's not the only one.
Common alternative packet capture formats are [PcapNG](https://pcapng.com), [ETL](https://netresec.com/?b=21B0d0e) and [Endace ERF](https://netresec.com/?b=12B3A4A).

Posted by Erik Hjelmvik on Thursday, 27 October 2022 06:50:00 (UTC/GMT)

Tags:
#[pcap](/?page=Blog&tag=pcap)​
#[tcpdump](/?page=Blog&tag=tcpdump)​
#[libpcap](/?page=Blog&tag=libpcap)​

Short URL:
<https://netresec.com/?b=22A1c18>

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

» [20...