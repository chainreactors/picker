---
title: Link-Layer Forensics From Ethernet II Frames to ARP Spoofing
url: https://digitalinvestigator.blogspot.com/2026/10/link-layer-forensics-from-ethernet-ii.html
source: Instapaper: Unread
date: 2026-10-20
fetch_date: 2026-10-21T06:51:10.454075
---

# Link-Layer Forensics From Ethernet II Frames to ARP Spoofing

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Network Forensics](https://digitalinvestigator.blogspot.com/search/label/Network%20Forensics)

# Link-Layer Forensics: From Ethernet II Frames to ARP Spoofing

Joseph Moronwi
October 19, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheQy26HKAMjMRV8tIJRUso7HZNUm6D5mlEmq7KTPwsIVXSnQlUf76i1Qmy1TXoy3mElljCOhdOAAe9b_oMUVpMN9jrPFt5Qp1DNDvkLBrwXyv2405Jtl0o5nuwGiTnrIGgUjuaunZLZBu26JZ5xS8Xq62y5KJ0V6G-iWEdsSaaQSTY4lMwVhKJe1HwL0Q/w656-h324/13.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheQy26HKAMjMRV8tIJRUso7HZNUm6D5mlEmq7KTPwsIVXSnQlUf76i1Qmy1TXoy3mElljCOhdOAAe9b_oMUVpMN9jrPFt5Qp1DNDvkLBrwXyv2405Jtl0o5nuwGiTnrIGgUjuaunZLZBu26JZ5xS8Xq62y5KJ0V6G-iWEdsSaaQSTY4lMwVhKJe1HwL0Q/s1366/13.png)

The link layer (also called the network access layer in the TCP/IP model) governs how data frames are transmitted between nodes over a local link. Common LAN technologies include IEEE 802.3 Ethernet and IEEE 802.11 Wi-Fi, although the link layer is not limited to the IEEE 802 family. Other data-link technologies include PPP, HDLC, Frame Relay, and ATM. Our primary concern is how a host resolves a known network-layer (IP) address into the link-layer address required to construct a frame. In IPv4, the Address Resolution Protocol (ARP) resolves an IPv4 address to a link-layer address; the older Reverse Address Resolution Protocol (RARP), which performed a different function, is now obsolete. The resolved MAC address belongs to the next hop on the local link, not necessarily the final destination. For off-subnet traffic, this is typically the default gateway, making the gateway's ARP cache entry a potential target for ARP spoofing.

In IPv6, ARP is replaced by the Neighbor Discovery Protocol (NDP), which operates over ICMPv6. Neighbor Solicitation messages use ICMPv6 type 135, while Neighbor Advertisement messages use type 136. For address resolution on multicast-capable links, a Neighbor Solicitation is sent to the target's solicited-node multicast address (`ff02::1:ffXX:XXXX`), derived from the low-order 24 bits of the target IPv6 address, rather than being broadcast to every host on the local link. Neighbor Solicitations can also be sent as unicast messages for reachability checks.

Both protocols are associated with volatile operating-system artifacts: the IPv4 ARP cache and the IPv6 neighbor cache. These caches record IP-to-link-layer address associations and can help investigators reconstruct local network activity, provided the entries are captured before they expire or are replaced. Ordinary ARP lacks authentication, making it vulnerable to ARP spoofing. NDP also faces threats such as rogue Neighbor Advertisements, although IPv6 defines validation measures and Secure Neighbor Discovery (SEND) as an additional protection mechanism. Other Layer 2 attacks, including MAC flooding and VLAN hopping, exploit different aspects of network switching and segmentation.

Because MAC addresses can be spoofed or changed, a MAC address observed in a cache, packet capture, or switch forwarding table represents an observed or claimed link-layer identity, not definitive proof of a particular physical device or actor. Investigators should corroborate such evidence with independent sources, such as DHCP records, switch-port information, endpoint logs, and other relevant network telemetry. First, however, we will examine how Ethernet framing works.

# IEEE 802.x Link Layer

The IEEE (Institute of Electrical and Electronics Engineers, commonly pronounced “I-triple-E”) develops and maintains the 802 family of LAN and MAN standards, including wireless networking standards such as 802.11. For our purposes, the most relevant member is IEEE 802.3, which specifies Ethernet. The terms “IEEE 802.3 framing” and “Ethernet II framing” are often conflated, but they describe different interpretations of the field following the source MAC address.

In Ethernet II, this 2-byte field is an EtherType identifying the encapsulated protocol, such as 0x0800 for IPv4, 0x0806 for ARP, and 0x86DD for IPv6. The resulting Ethernet II header is 14 bytes long: 6 bytes for the destination MAC address, 6 bytes for the source MAC address, and 2 bytes for the EtherType. In IEEE 802.3 length-based framing, the corresponding field specifies the length of the MAC client data, and the upper-layer protocol is identified through an IEEE 802.2 LLC header, optionally followed by a SNAP header. When LLC/SNAP encapsulation uses 8 bytes within a conventional 1500-byte Ethernet payload, up to 1492 bytes remain for the encapsulated IP packet.

Packet analyzers distinguish the two formats using the field's value: values up to and including 1500 (0x05DC) indicate a length, while values of 1536 (0x0600) and above indicate an EtherType. Values between these ranges are reserved. IEEE 802.3 revisions have accommodated EtherType-based framing, and Ethernet II is the dominant format for ordinary IP traffic on enterprise networks. LLC-based framing remains relevant in certain control protocols, including spanning-tree BPDUs. We will therefore focus on Ethernet II.

Even as workloads migrate to the cloud, Ethernet remains important in virtualized environments, where virtual switches and network interfaces provide Ethernet-like connectivity. Network-layer and higher-layer analysis remains applicable across physical and virtual environments, although Layer 2 visibility in cloud deployments depends on the provider's architecture and the telemetry it exposes, such as packet mirroring and flow logs.

Ethernet was significant in part because of its approach to sharing a communication medium. Earlier contention-based methods included ALOHA and carrier-sense multiple access (CSMA), while other networks used approaches such as time-slotted access or token passing. Robert Metcalfe’s design at Xerox PARC added collision detection (CD): Stations listened for carrier activity before transmitting, detected collisions while transmitting, sent a jam signal, and then retried after a randomized backoff using binary exponential backoff. This is CSMA/CD, which historically defined shared-medium Ethernet. On modern switched, full-duplex Ethernet links, CSMA/CD is no longer used, since each port is its own collision domain: each full-duplex link provides separate transmit and receive paths, eliminating the collisions that CSMA/CD was designed to manage.

Enterprise network monitoring commonly includes extensive wired-side visibility, while wireless monitoring addresses additional concerns such as detecting unauthorized access points and observing 802.11 management and radio activity. An ordinary wired capture on an access point's uplink generally sees traffic after it has been bridged or otherwise converted into Ethernet frames; it does not preserve the original 802.11 management frames or radio metadata.

On the wired side, the goal is to obtain the broadest practical packet visibility across relevant switches, routers, access points, and other network devices. However, a capture point sees only traffic that traverses the monitored link or is explicitly mirrored to it. Investigators must therefore plan TAP and SPAN deployments caref...