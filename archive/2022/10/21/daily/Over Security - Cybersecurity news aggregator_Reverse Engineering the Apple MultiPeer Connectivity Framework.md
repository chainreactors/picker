---
title: Reverse Engineering the Apple MultiPeer Connectivity Framework
url: https://www.evilsocket.net/2022/10/20/Reverse-Engineering-the-Apple-MultiPeer-Connectivity-Framework/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-21
fetch_date: 2025-10-03T20:31:16.904105
---

# Reverse Engineering the Apple MultiPeer Connectivity Framework

* [~/](/)
* [rss](/atom.xml)

Previous post
Next post
Back to top
Share post

1. [1. MultipeerConnectivity Framework](#MultipeerConnectivity-Framework)
2. [2. Discovery Phase: Multicast DNS](#Discovery-Phase-Multicast-DNS)
3. [3. How a PeerID is made](#How-a-PeerID-is-made)
4. [4. Handshake Phase: Hellos and Acks](#Handshake-Phase-Hellos-and-Acks)
5. [5. Authorization Phase: Spoofable Invites and BPlist inside BPlist inside TCP](#Authorization-Phase-Spoofable-Invites-and-BPlist-inside-BPlist-inside-TCP)
6. [6. Data Exchange Phase](#Data-Exchange-Phase)
7. [7. STUN a la Facetime](#STUN-a-la-Facetime)
8. [8. Brief note on OSPF](#Brief-note-on-OSPF)
9. [9. Conclusion](#Conclusion)

# Reverse Engineering the Apple MultiPeer Connectivity Framework

2022-10-20

[apple](/tags/apple/), [facetime](/tags/facetime/), [framework](/tags/framework/), [ice](/tags/ice/), [mcpeer](/tags/mcpeer/), [mcpeerid](/tags/mcpeerid/), [mdns](/tags/mdns/), [mpc framework](/tags/mpc-framework/), [multipeer](/tags/multipeer/), [multipeerconnectivity](/tags/multipeerconnectivity/), [network](/tags/network/), [network packets](/tags/network-packets/), [network protocol](/tags/network-protocol/), [ospf](/tags/ospf/), [re](/tags/re/), [reverse engineering](/tags/reverse-engineering/), [stun](/tags/stun/), [tcp](/tags/tcp/), [wireshark](/tags/wireshark/)

Some time ago I was using [Logic Pro](https://www.apple.com/it/logic-pro/) to record some of my music and I needed a way to start and stop the recording from an iPhone, so I found about [Logic Remote](https://apps.apple.com/it/app/logic-remote/id638394624) and was quite happy with it.
After the session, the hacker in me became curious about how the tools were communicating with each other, so I quickly started Wireshark while establishing a connection and saw something that tickled my curiosity even more: some of the data, such as the client and server names, were transmitted in cleartext on what it seemed a custom (and as typical of Apple, undocumented) TCP protocol (**“stevie”** being the hostname of my Mac):

![cleartext packets](/images/2022/cleartext.png)

Using [lsof](https://ss64.com/osx/lsof.html) confirmed that this was indeed the communication between the client phone and Logic listening on port 56076:

![lsof](/images/2022/lsof.png)

Initially I tought this was just some Logic Pro specific protocol and very lazily started looking into it, without much success mostly due to lack of motivation given the very limited scope of the research. After a while I [tweeted](https://twitter.com/evilsocket/status/1568310905640722433) asking if anyone had ever seen anything like it. [@isComputerOn pointed out](https://twitter.com/isComputerOn/status/1568344165175508992) that this looked a lot like a protocol that has been partially reversed and presented by [Alban Diquet](https://twitter.com/nabla_c0d3) back in 2014. Unfortunately, however brilliant, this research covers the protocol at a very high level and doesn’t really document the packets, their fields and how to establish a connection from anything but a client using the Apple framework. However, this helped me a lot in two ways: first it helped me realize this was not just Logic Pro specific, but that it was part of the [Multipeer Connectivity Framework](https://developer.apple.com/documentation/multipeerconnectivity), and gave me a few hints about the general logic of the protocol itself.

With renewed curiosity and motivation then I jumped into this rabbit hole and managed to reverse engineer all network packets. This allowed me to write a [Python proof of concept client](https://github.com/evilsocket/mpcfw) that automatically discovers any MPC servers, initializes the connection and succesfully exchanges application specific data packets.

Moreover, while sending crafted packets and attempting all sorts of things, **I’ve discovered several vulnerabilities in the Apple custom made parsers**. I will **not** discuss them here (exception made for the session spoofing) but at the same time I’m not interested in reporting them to Apple, I’ve heard way too many negative stories about their disclosure program and in general how they mistreat researchers.

![crash](/images/2022/crash.png)

Let’s see how this whole thing works! :)

### MultipeerConnectivity Framework

Apple’s [documentation](https://developer.apple.com/documentation/multipeerconnectivity) describes the framework like so:

> The Multipeer Connectivity framework supports the discovery of services provided by nearby devices and supports communicating with those services through message-based data, streaming data, and resources (such as files). In iOS, the framework uses infrastructure Wi-Fi networks, peer-to-peer Wi-Fi, and Bluetooth personal area networks for the underlying transport. In macOS and tvOS, it uses infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Ethernet.

The document mostly describes how they abstracted the protocol in several classes while being extremely vague about how the thing actually works at the packet level. In reality they mostly reused existing protocols such as MDNS and a customized STUN implementation (in Logic Pro specific case, this doesn’t always apply to apps using this framework), plus a custom TCP based protocol for which they heavily relied on custom (and extremely badly) written parsers.

### Discovery Phase: Multicast DNS

The very first thing that I’ve noticed was that, despite the server port being randomized at each application startup, the client application never asked me for the server ip address nor tcp port. This was a strong indicator that something else was happening on the network before the TCP session was being established, as if the server (and possibly the client as well) broadcasted this information in such a way to be automatically discoverable, as also hinted by the wording used in the documentation.

My informed guess was [multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS) as I’ve seen this protocol being (ab)used a lot from Apple ([Bonjour](https://developer.apple.com/bonjour/) for instance), and Wireshark confirmed my guess. Both the server and the client are broadcasting their hostnames and peer identifiers (more on this later) on the network so that they can find each other without user interaction.

Here’s how the server advertisement looks like on [Spycast](https://github.com/evilsocket/spycast):

![mdns server](/images/2022/mdns_server.png)

We can see which TCP port is being used (57219), some application specific information in the text record and a weird string “1tvdkfvihbru6”, the [PeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid).

At the same time, the client is broadcasting some information such as its hostname:

![mdns client](/images/2022/mdns_client.png)

Keep in mind that all this data is visible by **anyone** on the same network, this is an important detail as we’ll see shortly when I’ll describe how the spoofing works.

### How a PeerID is made

Before proceeding to the next part, let’s stop for a moment to see how a peer is identified in this protocol and what that “1tvdkfvihbru6” string is.

Upon startup, each peer is represented by a [MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid) object. Long story short, a random 64bit integer is generated and converted to base36.

So that 1tvdkfvihbru6 in base36 is 8670129607084362000 in base 10. This number is used to uniquely identify the host during the session, regardless of the hostname itself and it’s present in various forms in most of the packets we’re about to see.

### Handshake Phase: Hellos and Acks

After the client discovers the server peer via MDNS the connection is initiated to the TCP port indicated in the advertisement. This is when things started being complicated as the protocol is entirely custom and undocumented.

I needed to work my way from something like this:

![hex data](/images/2022/hexdata.png)

To somet...