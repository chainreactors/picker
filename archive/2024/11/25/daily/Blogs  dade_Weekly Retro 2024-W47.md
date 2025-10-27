---
title: Weekly Retro 2024-W47
url: https://0xda.de/blog/2024/11/weekly-retro-2024-w47/
source: Blogs  dade
date: 2024-11-25
fetch_date: 2025-10-06T19:14:47.577781
---

# Weekly Retro 2024-W47

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/11/weekly-retro-2024-w47/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Weekly Retro 2024-W47](https://0xda.de/blog/2024/11/weekly-retro-2024-w47/)

---

* [First Vacation… ever?](#first-vacation-ever)
* [Meshtastic](#meshtastic)
* [New Home Server](#new-home-server)
* [Micro Projects](#micro-projects)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

Holy cow it’s been a minute. We went to Japan for a couple weeks and when I came back, I was feeling super chill. So chill that I didn’t want to get back into the swing of writing. It’s not just my retros that suffered, but all of my notes. My Obsidian Vault has cobwebs growing.

But if I just keep not writing, it’ll be a year before I write here again, and I really don’t want that to happen. So here I am, writing a… 6 week retro.

## First Vacation… ever?

I’ve been working full time for just about 10 years now. During that time, I’ve traveled a lot for work, I’ve traveled a lot for conferences, and I’ve traveled a lot to see loved ones. But I never really traveled internationally, and I recently changed that.

Sienna and I spent 16 days in Japan, mostly in Tokyo. It was my first time there and I had a great time. It was wild that I could just go out walking around at like 11pm and things were safe and clean. We explored Akihabara, Ginza, Shibuya, Shinjuku, and Ikebukuro, and maybe one or two other areas I’m forgetting.

A lot of people have asked me my favorite part of the trip, and I’d be lying if I said anything other than the transit system. Trains in Japan are incredible. Missed your train? Don’t worry, another will be there in 5 minutes or less. Meanwhile if I miss Bart in the morning I might be waiting 20 minutes or more. We also took the Tokaido Shinkansen over to Kyoto and Osaka, and that was a super cool experience. I have heard a lot of people talk about how America should invest in high speed rail over the years, but now that I’ve experienced it first hand… damn.

## Meshtastic

I’ve been getting more into the Meshtastic scene, but my little Heltec radio has been a bit of a nightmare. While it was super cool to get and start experimenting with, I basically constantly have issues receiving or sending messages to the default LongFast channel. I will sometimes not get any messages for hours, then get many hours of messages all at once. My messages also often hit maximum retries without being delivered, despite being in an area with several other radios fairly close.

But even with the difficulties I’ve been having, I’m still super interested and I recently printed a [little MOLLE holster](https://www.printables.com/model/936466-pager-style-holster-for-the-muziworks-h1-heltec-v3/files) for it, which was a super smooth print and fits wonderfully. I am considering getting a little solar outdoor node like this [Atlavox S4](https://atlavox.com/products/atlavox-s4-solar-meshtastic%E2%84%A2-node). I’m sure I could make something for a cheaper price, but I feel like getting started it would be nice to just have something pre-fab.

## New Home Server

I’ve finally decided to pull the trigger and I ordered an [HL15 from 45 Home Lab](https://store.45homelab.com/configure/hl15). I’m going with the X11SPH-nCTF SuperMicro board, a Xeon Silver 4210 processor, and 64GB of memory.

This will be replacing my current media server, which is running Windows 10 on my old i7-3770K that used to be my state of the art gaming server. That machine is so old that it’s also not running an NVMe SSD, it’s running an engineering sample drive I got while I worked at Intel. I might bring the drive over to the new system, though. It’s getting pretty close to 1PB total bytes written, and I really want to see how far it goes. It has also only been powered off for less than 3 hours since it’s release date, which is very satisfying.

I’ve been pretty hesitant - I’ve been thinking about buying this for months, but it’s a pretty hefty expense, and technically my media server still works fine now. But overall I’m looking at this and thinking “If this lasts 10 years like my current one, the amortized price isn’t so big.” I have a lot of opportunity to fix some mistakes I made while building my current server over time, get to use some newer technology, and consolidate down so that I can combine my media server, my NAS, and the few random services I have running on pis and nucs aroudn the house. I think I’m also giving up on my home k3s cluster. That thing feels like pulling teeth whenever I want to work on it.

So I’m thinking TrueNAS Scale. I’d love to hear your opinions, though. I want something that is out of the way when I just want it to work, but that lets me tinker and customize when I want to.

## Micro Projects

I have a few microprojects that I am starting to develop. I’ve thought, for a long time, that I wanted to have my own services like my own image sharing service, my own pastebin, my own link shortener, etc. I know that all of these options have self-hosted options that are easy to install. But the usage model I’d like to consider is that only I can publish things to these services, but anyone can see them.

I built a link shortener on my laptop in about an hour the other night, and I think a personal-use link shortener might be the perfect first web development project for new developers. It’s easy to scope it pretty narrowly, and also easy to see new features that you might want. For example, at the base, you just need to submit the URL and return a short ID, and have a route that redirects the short ID to the URL. But then you can add some basic stats, like tracking each visit over time so you can see how popular it is on any given day. And you could do all this with just a json file, if you wanted, or a simple sqlite database once you want to improve it even more.

Anyways, I’m going to start recommending link shorteners as projects when someone wants to get started with development. Meanwhile I’m going to keep building my own little single-purpose tools.

## Interesting Links

* [Western Digital Recycling Program](https://www.westerndigital.com/company/programs/easy-recycle) - Free hard drive disposal, and you can get a discount code on future orders. They recycle devices from any manufacturer, which is awesome.
* [FCC Open Data on Pirate Radio Enforcement Actions](https://opendata.fcc.gov/stories/s/Pirate-Radio-Broadcasting-Database/wgq8-eb5c/) - I didn’t know this was published data, and I thought it was pretty cool and wanted to share.
* [PiAware ADS-B Ground Station](https://www.flightaware.com/adsb/piaware/build/) - FlightAware provides instructions on how to build an ADS-B receiver, and if you contribute data you can get free access to their data set.
* [Doctorow’s Opinion on Bluesky](https://pluralistic.net/2024/11/02/ulysses-pact/#tie-yourself-to-a-federated-mast) - While I like Bluesky as a Twitter alternative, Cory brings up some pretty valid points about lock in. Bluesky isn’t actually decentralized right now, and it kind of sucks to build up an audience on a platform that can terminate you at any time. I mean, in the ActivityPub universe you can get defederated from various servers, but it still feels… more robust.

## Upcoming Projects

* N/A

---

Share this page

`https://0xda.de/blog/2024/11/weekly-retro-2024-w47/`

[weekly retro](https://0xda.de/tags/weekly-retro)

1164 Words

Date Published

2024-11-24 17:44 +0000

218a617 ...