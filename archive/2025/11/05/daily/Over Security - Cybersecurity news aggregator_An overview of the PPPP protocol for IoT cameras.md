---
title: An overview of the PPPP protocol for IoT cameras
url: https://palant.info/2025/11/05/an-overview-of-the-pppp-protocol-for-iot-cameras/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-05
fetch_date: 2025-11-06T03:15:41.806260
---

# An overview of the PPPP protocol for IoT cameras

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More ГӮВ»

[ ]

# An overview of the PPPP protocol for IoT cameras

2025-11-05
 [Security](/categories/security/)/[IoT](/categories/iot/)
 21 mins
 [0 comments](/2025/11/05/an-overview-of-the-pppp-protocol-for-iot-cameras/#comments)

My [previous article on IoT ГўВҖВңP2PГўВҖВқ cameras](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/) couldnГўВҖВҷt go into much detail on the PPPP protocol. However, there is already lots of security research on and around that protocol, and I have a feeling that there is way more to come. There are pieces of information on the protocol scattered throughout the web, yet every one approaching from a very specific narrow angle. This is my attempt at creating an overview so that other people donГўВҖВҷt need to start from scratch.

While the protocol can in principle be used by any kind of device, so far IГўВҖВҷve only seen network-connected cameras. It isnГўВҖВҷt really peer-to-peer as advertised but rather relies on central servers, yet the protocol allows to transfer the bulk of data via a direct connection between the client and the device. ItГўВҖВҷs hard to tell how many users there are but there are *lots* of apps, IГўВҖВҷm sure that I havenГўВҖВҷt found all of them.

There are other protocols with similar approaches being used for the same goal. One is used by ThroughTekГўВҖВҷs Kalay Platform which [has the interesting string ГўВҖВңCharlie is the designer of P2P!!ГўВҖВқ in its codebase](https://www.thirtythreeforty.net/posts/2020/05/hacking-reolink-cameras-for-fun-and-profit/#the-charlie-scrambler) (32 bytes long, seems to be used as ГўВҖВңencryptionГўВҖВқ key for some non-critical functionality). I recognize both the name and the ГўВҖВңhandwriting,ГўВҖВқ it looks like PPPP protocol designer found a new home here. Yet PPPP seems to be still more popular than the competition, thanks to it being the protocol of choice for cheap low-end cameras.

*Disclaimer*: Most of the information below has been acquired by analyzing public information as well as reverse engineering applications and firmware, not by observing live systems. Consequently, there can be misinterpretations.

#### Contents

* [The general design](#the-general-design)
* [The network ports](#the-network-ports)
* [The device IDs](#the-device-ids)
* [The protocol variants](#the-protocol-variants)
  + [CS2 Network](#cs2-network)
  + [Yi Technology](#yi-technology)
  + [iLnk](#ilnk)
  + [HLP2P](#hlp2p)
* [ГўВҖВңEncryptionГўВҖВқ](#encryption)
* [ГўВҖВңSecretГўВҖВқ messages](#secret-messages)
* [Applications](#applications)

## The general design

The protocolГўВҖВҷs goal is to serve as a drop-in replacement for TCP. Rather than establish a connection to a known IP address (or a name to be resolved via DNS), clients connect to a device identifier. The abstraction is supposed to hide away how the device is located (via a server that keeps track of its IP address), how a direct communication channel is established (via [UDP hole punching](https://en.wikipedia.org/wiki/UDP_hole_punching)) or when one of multiple possible fallback scenarios is being used because direct communication is not possible.

The protocol is meant to be resilient, so there are usually three redundant servers handling each network. When a device or client needs to contact a server, it sends the same message to all of them and doesnГўВҖВҷt care which one will reply. *Note*: In this article ГўВҖВңnetworkГўВҖВқ generally means a PPPP network, i.e. a set of servers and the devices connecting to them. While client applications typically support multiple networks, devices are always associated with a specific one determined by [their device prefix](#the-device-ids).

For what is meant to be a [transport layer protocol](https://en.wikipedia.org/wiki/Transport_layer), PPPP has some serious complexity issues. It encompasses device discovery on the LAN via UDP broadcasts, UDP communication between device/client and the server and a number of (not exactly trivial) fallback solutions. It also features multiple ГўВҖВңencryptionГўВҖВқ algorithms which are more correctly described as obfuscators and network management functionality.

Paul MarrapeseГўВҖВҷs [Wireshark Dissector](https://github.com/pmarrapese/iot/tree/master/p2p/dissector) provides an overview of the messages used by the protocol. While it isnГўВҖВҷt quite complete, a look into the `pppp.fdesc` file shows roughly 70 different message types. ItГўВҖВҷs hard to tell how all these messages play together as the protocol has not been designed as a state machine. The protocol implementation uses its previous actions as context to interpret incoming messages, but it has little indication as to which messages are expected when. Observing a running system is essential to understanding this protocol.

The complicated message exchange required to establish a connection between a device and a client has been [described by Elastic Security Labs](https://www.elastic.co/security-labs/storm-on-the-horizon#building-a-p2p-client). They also provide the code of their client which implements that secret handshake.

I havenГўВҖВҷt seen any descriptions of how the fallback approaches work when a direct connection cannot be established. Neither could I observe these fallbacks in action, presumably because the network I observed didnГўВҖВҷt enable them. There are at least three such fallbacks: UDP traffic can be relayed by a network-provided server, it can be relayed by a ГўВҖВңsupernodeГўВҖВқ which is a device that agreed to be used as a relay, and it can be wrapped in a TCP connection to the server. The two centralized solutions incur significant costs for the network owners, rendering them unpopular. And I can imagine the ГўВҖВңsupernodeГўВҖВқ approach to be less than reliable with low-end devices like these cameras (itГўВҖВҷs also a privacy hazard but this clearly isnГўВҖВҷt a consideration).

I recommend going though the [CS2 sales presentation](https://prezi.com/5cztk-98izyc/cs2-network-p2p/) to get an idea of how the protocol is *meant* to work. Needless to say that it doesnГўВҖВҷt always work as intended.

## The network ports

I could identify the following network ports being used:

* UDP 32108: broadcast to discover local devices
* UDP 32100: device/client communication to the server
* TCP 443: client communication to the server as fallback

Note that while port 443 is normally associated with HTTPS, here it was apparently only chosen to fool firewalls. The traffic is merely obfuscated, not really encrypted.

The direct communication between the client and the device uses a random UDP port. In my understanding the ports are also randomized when this communication is relayed by a server or supernode.

## The device IDs

The canonical representation of a device ID looks like this: `ABC-123456-VWXYZ`. Here `ABC` is a device prefix. While a PPPP network will often handle more than one device prefix, mapping a device prefix to a set of servers is supposed to be unambiguous. This rule isnГўВҖВҷt enforced across different [protocol variants](#the-protocol-variants) however, e.g. the device prefix `EEEE` is assigned differently by CS2 and iLnk.

The six digit number following the device prefix allows distinguishing different devices within a prefix. It seems that vendors can choose these numbers freely ГўВҖВ“ some will assign them to devices sequentially, others go by some more complicated rules. [A comment on my previous article](/2025/09/08/a-look-at-a-p2p-camera-lookcam-app/#c000003) even claims that they will sometimes reassign existing device IDs to new devices.

The final part is the verification code, meant to prevent enumeration of devices. It is generated by some secret algorithm and allows distinguishing valid device IDs from invalid ones. At least one such algorithm got leaked in the past.

Depending on the application a device ID will no...