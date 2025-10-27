---
title: Major Private Torrent Sites Have a Security Disaster to Fix Right Now
url: https://torrentfreak.com/major-private-torrent-sites-have-a-security-disaster-to-fix-right-now-230103/
source: TorrentFreak
date: 2023-01-04
fetch_date: 2025-10-04T03:02:06.550616
---

# Major Private Torrent Sites Have a Security Disaster to Fix Right Now

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

# Major Private Torrent Sites Have a Security Disaster to Fix Right Now

January 3, 2023 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy](https://torrentfreak.com/category/piracy/ "Go to the Piracy category archives.") >

At least three major torrent sites are currently exposing intimate details of their operations to anyone with a web browser. TorrentFreak understands that the sites use a piece of software that grabs brand-new content from other sites before automatically uploading it to their own. A security researcher tried to raise the alarm but nobody will listen.

[![Pirate Fire](https://torrentfreak.com/images/pirate-fire-burn.jpg)](https://torrentfreak.com/images/pirate-fire-burn.jpg)Private torrent sites, or private trackers as they’re commonly known, are designed to be difficult to access.

In many cases, prospective members will need an invitation from someone who is already a member, although some sites will open their front doors when people open their wallets. This presents a challenge for people who want to give them valuable, urgent information but must pay to do so.

## Background and Dilemma

Just a few hours ago, TorrentFreak received a rather detailed tip from a security researcher who prefers to remain anonymous. The information relates to three major/well-known private trackers and their users directly, but from the evidence presented, the security debacle exposes other sites too.

The researcher came to us with the story because, after trying to get the attention of the sites’ operators, even through other sites that might forward the message, nothing has been done. Surprising, given the scale of the problem.

The researcher’s goal is to protect the sites’ users but if we publicly name the sites here, that will not buy enough time for the admins to hear about the news and plug the gaps. Instead, we’ll provide enough information for the sites’ operators to recognize their own site from the inside and then one minute later, the problem should be fixed.

## The Security Issue

To get their hands on the latest releases as quickly as possible, trackers often rely on outside sources that have access to so-called 0-Day content, i.e, content released today. The three affected sites seem to have little difficulty obtaining some of their content within minutes. At least in part, that’s achieved via automation.

When outside suppliers of content are other torrent sites, a piece of software called Torrent Auto Uploader steps in. It can automatically download torrents, descriptions, and associated NFO files from one site and upload them to another, complete with a new .torrent file containing the tracker’s announce URL.

[![taud-1](https://torrentfreak.com/images/taud-1.png)](https://torrentfreak.com/images/taud-1.png)

The management page above has been heavily redacted because the content has the potential to identify at least one of the sites. It’s a web interface, one that has no password protection and is readily accessible by anyone with a web browser. The same problem affects at least three different servers operated by the three sites in question.

## Web Interface For Torrent Clients

Torrent Auto Uploader relies on torrent clients to transfer content. The three sites in question all use rTorrent clients with a ruTorrent Web UI. We know this because the researcher sent over a whole bunch of screenshots and supporting information which confirms access to the torrent clients as well as the Torrent Auto Uploader software.

[![rutorrent-gui](https://torrentfreak.com/images/rutorrent-gui.png)](https://torrentfreak.com/images/rutorrent-gui.png)

The image above shows redactions on the tracker tab for good reason. In a regular setup, torrent users can see the names of the trackers coordinating their downloads. This setup is no different except that these URLs reference three different trackers supplying the content to one of the three compromised sites.

## Can it Get Any Worse?

Rather than publish a sequence of completely redacted screenshots, we’ll try to explain what they contain. One begins with a GET request to another tracker, which responds with a torrent file. It’s then uploaded to the requesting site which updates its SQL database accordingly.

From there the script starts checking for any new entries on a specific RSS feed which is hidden away on another site that has nothing to do with torrents. The feed is protected with a passkey but that’s only useful when nobody knows what it is.

The same security hole also grants direct access to one of the sites tracker ‘bots’ through the panel that controls it.

[![torrents-clientru](https://torrentfreak.com/images/torrents-clientru.png)](https://torrentfreak.com/images/torrents-clientru.png)

Then there’s access to ‘Staff Tools’ on the same page which connect to other pages allowing username changes, uploader application reviews, and a list of misbehaving users that need to be monitored. That’s on top of user profiles, the number of torrents they have active, and everything else one could imagine.

Another screenshot featuring a torrent related to a 2022 movie reveals the URL of yet another third-party supplier tracker. Some basic queries on that URL lead to even more torrent sites. And from there, more, and more, and more – revealing torrent passkeys for every single one on the way.

Security holes need to be fixed sooner rather than later but getting hold of operators in this niche is difficult by design. Users of all sites might want to make a bit of noise in the hope that the three that matter actually do something.

**Update:** Two shut down, one to go

* [![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-left.svg)Next Post](https://torrentfreak.com/riaa-wants-250000-in-attorneys-fees-from-yout-without-delay-230104/)
* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/soccerstreams-throws-the-towel-following-u-s-domain-seizures-230103/)

### Tagged In:

* [bittorrent](https://torrentfreak.com/tag/bittorrent/)
* [private-trackers](https://torrentfreak.com/tag/private-trackers/)
* [torrent sites](https://torrentfreak.com/tag/torrent-sites/)

### You Might Also Like:

[![](https://torrentfreak.com/images/dht-2-f-500x210.png)

Technology

### BitTorrent’s DHT and the Leading ISP Networks Helping to Keep it Alive

* September 27, 2025, 13:10 by Andy Maxwell](https://torrentfreak.com/bittorrents-dht-and-how-customers-of-major-isps-help-keep-it-vibrant-alive-250927/)

[![](https://torrentfreak.com/images/musical-daybreak-f-500x210.png)

Lawsuits

### Record Labels Target 20 ISPs in Pursuit of BitTorrent Pirates and Damages

* February 14, 2025, 08:42 by Andy Maxwell](https://torrentfreak.com/record-labels-target-20-isps-in-pursuit-of-bittorrent-pirates-and-damages-250214/)

[![](https://torrentfreak.com/images/featuredlarge-500x210.jpg)

Piracy

### Top 10 Most Popular Torrent Sites 2025

* January 3, 2025, 08:26 by Staff](https://torrentfreak.com/top-torrent-sites/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/comment....