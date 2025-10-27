---
title: Sky’s Enhanced High Court Pirate IPTV Blocking Order Closes Loopholes
url: https://torrentfreak.com/skys-enhanced-high-court-pirate-iptv-blocking-order-could-change-the-game-241221/
source: TorrentFreak
date: 2024-12-22
fetch_date: 2025-10-06T19:38:11.066924
---

# Sky’s Enhanced High Court Pirate IPTV Blocking Order Closes Loopholes

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

# Sky’s Enhanced High Court Pirate IPTV Blocking Order Closes Loopholes

December 21, 2024 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Sixteen well-known suppliers active in the UK pirate IPTV market have been selected by broadcaster Sky to star in a new phase of the company's ISP blocking program. A new order obtained at the High Court is technically an extension of an existing order won last year. However, with significant tweaks, upgrades and an extremely determined opponent, pirates may be about to face their toughest challenge yet.

![sky-1](https://torrentfreak.com/images/sky-1.png)
As a TV broadcaster, Sky has an exceptional view of the legal subscription TV market and how the illegal IPTV market encroaches on that.

As an ISP that supplies 20% of the market, Sky’s view of its own customers using Sky Broadband to pirate Sky’s pay TV content is a persistent irritant that comes with the territory.

Sky’s involvement in ISP blocking orders has traditionally meant complying with injunctions obtained by groups including the MPA and RIAA. Along with its main ISP rivals including market leader BT (28%), roughly on-par competitor Virgin Media (20%), and TalkTalk (12.5%), over the years Sky has blocked thousands of domains to protect content owned by others.

## Sky Tests Blocking to Protect Its Own Content

In the summer of 2023, [Sky obtained a blocking injunction](https://torrentfreak.com/sky-obtains-novel-injunction-to-prevent-piracy-of-live-sports-house-dragon-230731/) at the High Court to protect content it broadcasts on its own TV channels. Sky’s targets included *BunnyStream, Enigma Streams, GenIPTV, CatIPTV, GoTVMix, and IPTVMain*, none of which warmed to the idea of being blocked. Sky’s blocking measures faced pirate countermeasures, most visibly through the use of endless subdomains generated at will, which Sky also went on to [block on an unprecedented scale](https://torrentfreak.com/skys-industrial-scale-pirate-iptv-blocking-becomes-a-war-of-attrition-240118/), with a predictable response each time.

On November 12, 2024, Sky obtained an extension to its original order, the second since the summer of 2023. With BT, EE, Plusnet, TalkTalk, and Virgin Media listed once again, there was no change among the respondents. The list of targets, which includes static promotional/sales websites and underlying pirate IPTV services, reads as follows:

*BunnyStream; CatIPTV; EnigmaStreams; GenIPTV; GoTVMix; IPTVMAIN; FastIP.tv; IP-TV.uk; IPTV-King.co.uk; IPTVSubscribe.uk; IPTV-UK.digital; KemoIPTV.tv; UKChannels.co.uk; UKIPTVMedia.co; TheSkyIPTV.shop; and Calmahub.live*

All of Sky’s initial targets appear to have survived unprecedented levels of ISP blocking so are now appearing once again. Why that’s the case isn’t mentioned in the High Court order, and the same applies to other confidential aspects of the case to prevent circumvention. Fortunately, not everything is shrouded in darkness.

## Dynamic and Static Blocking

The order allows Sky to conduct *Dynamic Blocking* of IP addresses associated with the IPTV platforms’ servers. Once Sky becomes aware of a server it needs to block, IP address information can be sent to the respondent ISPs for blocking in real-time.

Blocking takes place during specific *Blocking Windows* based on detection of unauthorized broadcasts of Sky Channels (table below), or various conditions listed in a confidential schedule.

The IP addresses are unblocked at the conclusion of each *Blocking Window*, the durations of which are confidential.

Non-Exclusive List of ‘Trigger’ Channels

![sky-channel-list](https://torrentfreak.com/images/sky-channel-list.png)

Under the order, *Static Blocking* of URLs and Fully Qualified Domain Names (FQDNs) associated with the IPTV services’ websites is permanent.

Sky is authorized to detect and instantly notify the ISPs of IP addresses for *Dynamic Blocking* and URLs/FQDNs for *Static Blocking* if certain conditions are met. They include use of an IP address to broadcast public linear audiovisual footage of any Sky Channel during an unspecified *Monitoring Period*, or use that meets one or more detection conditions specified in a confidential schedule.

The order allows Sky to notify the ISPs of any URL or FQDN for *Static Blocking* if its “sole or predominant purpose is to enable or facilitate access to a Target Website.” Due to the confidentiality aspects of this and previous orders, specific examples aren’t provided.

However, this could be a measure to limit the usefulness of generating thousands of new subdomains to circumvent blocking. Previously the IPTV providers appeared to utilize wildcard certificates to generate FQDNs such as those shown below.

[![sky-iptv-dga](https://torrentfreak.com/images/sky-iptv-dga.png)](https://torrentfreak.com/images/sky-iptv-dga.png)

It may have been the case that if infringing activity only ever took place on subdomains, only those subdomains could be legally blocked. With an infinite supply of subdomains available at zero cost, generating more subdomains wasn’t a problem.

Here, however, a main domain would qualify as having the “sole or predominant purpose” of facilitating access to a pirate service. That means domains and subdomains could be blocked permanently, forcing the purchase of a whole new domain that when deployed would ultimately fare no better.

## IP Blocking, URL Blocking, DNS Blocking, Deep Packet Inspection

Each ISP is required to implement blocking based on the type requested and the availability of existing specialist tools.

**British Telecommunications (BT)**

The section of the order detailing how blocking should be carried out is more complicated than one might expect, largely due to the unique position of British Telecommunications Plc and companies operating within the BT Group. These include the ISP most people know as BT, telecoms brand EE, and the ISP Plusnet, both of which are listed as separate respondents in the blocking order.

BT Group subsidiary Openreach Limited operates the Openreach digital network through which the ISP BT supplies internet connectivity to customers. The Openreach network is also used by over 680 other companies selling broadband and telecoms services, including Plusnet and EE. The blocking order lacks clarity, but it appears that BT’s residential-type customers are handled using BT’s *[Cleanfeed](https://wiki.openrightsgroup.org/wiki/Cleanfeed)* filtering/blocking system, while ‘wholesale’ customers have access to a lesser-known BT blocking/filtering system called *RedCard*.

When *Dynamic Blocking* is required by the order, ISP BT must block by IP address. Customers to which the *RedCard* system applies must also block by IP address. When applying *Static Blocking*, BT must apply *Cleanfeed* for customers using its fixed-line and mobile networks, using technical means including;

● IP address blocking and IP address re-routing at the core netw...