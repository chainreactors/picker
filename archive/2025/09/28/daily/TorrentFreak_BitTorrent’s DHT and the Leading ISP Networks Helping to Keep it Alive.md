---
title: BitTorrent’s DHT and the Leading ISP Networks Helping to Keep it Alive
url: https://torrentfreak.com/bittorrents-dht-and-how-customers-of-major-isps-help-keep-it-vibrant-alive-250927/
source: TorrentFreak
date: 2025-09-28
fetch_date: 2025-10-02T20:49:37.533462
---

# BitTorrent’s DHT and the Leading ISP Networks Helping to Keep it Alive

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# BitTorrent’s DHT and the Leading ISP Networks Helping to Keep it Alive

September 27, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Technology](https://torrentfreak.com/category/technology/ "Go to the Technology category archives.") > [BitTorrent](https://torrentfreak.com/category/technology/bittorrent-technology/ "Go to the BitTorrent category archives.") >

Aside from the genius baked into the protocol itself, BitTorrent's success as a global network can be attributed to its Distributed Hash Table, commonly known by the initials DHT. Its existence goes unnoticed by millions of BitTorrent users, yet its absence would be felt all around the world. The DHT network is global and difficult to monitor comprehensively, but data shows that by IP address volume, customers of a relatively small number of ISPs dominate the DHT landscape.

![dht-2-s](https://torrentfreak.com/images/dht-2-s.png)
Nearly a quarter of a century after its debut, internet users stocking up on the latest multi-GB Linux distros can still do so with help from the BitTorrent protocol.

Able to download chunks of even the largest files, distributed among other users who could be anywhere on the planet, BitTorrent’s file transfer skills are two decades old yet never fail to impress.

For those yet to sample the magic of magnet links, the whole process begins with a humble .torrent file. These relatively small files contain metadata relating to the large file the user wants to download, including the location of one or more ‘trackers’, the central online servers that facilitate communication between users’ torrent clients.

Yet the real magic lies in BitTorrent’s resilience; it has a secret weapon that can find those chunks of data, wherever they may be, even when central trackers are blocked or shut down. It’s called DHT – Distributed Hash Table – and it’s one of the key reasons BitTorrent still performs so well on the global stage, even today.

## Trackers Are Useful But Disposable

A central server known as a tracker communicates with torrent clients to coordinate transfers of files between them. When a client requests a piece of a file the tracker knows is available, the tracker tells the client which other clients have it and from there, transfers take place peer-to-peer. Periodically, clients update the tracker with new information about the network, and so the cycle continues.

DHT, on the other hand, empowers torrent clients with the ability to receive and impart information directly with other clients. By creating distributed network knowledge, there’s no absolute need for a tracker, eliminating a potential central point of failure.

Peers knowledge of other peers is boosted by Peer Exchange or [PEX](https://torrentfreak.com/bittorrents-future-dht-pex-and-magnet-links-explained-091120/), a system through which a client that’s connected to another client, shares the IP addresses of peers it already knows. This increases the recipient client’s pool of connectivity opportunities and, if all goes well, speeds up downloads.

![bittorrent-network](https://torrentfreak.com/images/bittorrent-network-AI-3-5.png)
When new clients join the DHT, other torrent clients share content locations with the newcomer and, given time, the client returns the favor by passing information to other clients following similar requests.

The process is boosted locally using PEX, but the aim is the same – discovery of other clients/peers to create a more robust network with more effective file transfers.

In short, DHT makes every client a node in a vast decentralized network, with each sharing their growing knowledge of the network with other clients, that in turn have knowledge they’ll automatically share with others.

No single client knows the location of everything and even the pooled knowledge of thousands is unlikely to produce a full network map. However, most clients know enough to point out the location of at least something useful, and with PEX, they’ll provide the locations of other clients which helps to strengthen the overall network.

To many people the sharing of content is the most visible aspect of BitTorrent, but its real strength lies in the sharing of information that maintains the underlying network. The network that underlies that obviously plays a massive role too.

## Tens of Millions of Peers But Hard to Measure

In the bigger picture, the loss of few clients from public DHT is a non-event. Indeed, the sudden shut down of a major residential internet provider somewhere in the world may not be especially disruptive either, given the scale of the network. Yet putting an exact figure on the size of the network has to date proven elusive.

The lowest estimates always start in the millions of peers, with some researchers previously reporting anything from 20 to 30 million, sometimes a few million more, other times a few million less.

Researchers behind [BoonTorrent](https://github.com/gmosley/boontorrent), a now seven-year-old project to create a real-time monitoring tool for BitTorrent DHT traffic, reported that “BitTorrent traffic is abundant, but difficult to analyze. To capture enough data for significant analysis, a large distributed solution is needed.”

Their solution included a heatmap visualization of the previous two minutes of traffic, with two examples shown below.

*BoonTorrent DHT Heatmap 1*![boontorrent-eu](https://torrentfreak.com/images/boontorrent-eu-e1758892301600.png)

*BoonTorrent DHT Heatmap 2*![boontorrent-asia-rus](https://torrentfreak.com/images/boontorrent-asia-rus-e1758892361417.png)

Depending on the circumstances, we know that the number of peers can vary by at least 10 million, possibly more at times, or less.

That being said, these images suggest that Southeast Asia and Russia had quite the presence on BitTorrent’s DHT seven years ago. That’s a long time in internet years and everything is subject to change.

## Some ISPs Play Big Roles Supporting DHT Worldwide

As far as we’re aware, there are no large, recent studies on BitTorrent’s DHT so the overall numbers remain as elusive as ever. However, when using the tools available at [IPinfo.io](https://ipinfo.io/), something unexpected appeared; tracking data for BitTorrent’s DHT and some estimates based on IPinfo’s visibility of the network.

![ipinfo-dht](https://torrentfreak.com/images/ipinfo-dht.png)

The data displayed as of today concerns the number of IP addresses and their corresponding ASNs observed on the Mainline DHT in the past 30 days. The data obtained by TF from IPinfo.io just a few days ago is broadly the same.

When drilling down into the details, the data provides an overview of the ISPs with the greatest number of allocated IP addresses observed on the DHT network.

## Top ISPs With a Strong Customer DHT Presence

With 3,152,801 IP addresses observed on the DHT during the previous 30 days, Russian ISP [PJSC Rostelecom](https://ipinfo.io/AS12389) comfortably takes the top spot. Lagging two million IP addresses behind, Korea Telecom takes second place (1,143,168 IPs) with [CHINANET-BACKBONE](https://ipinfo.io/AS4134) narrowly behind with 1,131,734 observed IPs.

Positi...