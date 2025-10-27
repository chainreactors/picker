---
title: Weekly Retro 2025-W03
url: https://0xda.de/blog/2025/01/weekly-retro-2025-w03/
source: Blogs  dade
date: 2025-01-20
fetch_date: 2025-10-06T20:08:18.774561
---

# Weekly Retro 2025-W03

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/01/weekly-retro-2025-w03/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

7 minutes

# [Weekly Retro 2025-W03](https://0xda.de/blog/2025/01/weekly-retro-2025-w03/)

---

* [Natlas Changes](#natlas-changes)
* [ICANN & CZDS](#icann--czds)
* [Conference Work](#conference-work)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

This week was a busy one, with a ton of Natlas changes, an update on my acquisition of TLD zones, and a lot of work for a conference that we don’t advertise.

## Natlas Changes

This past week saw many huge changes for the [Natlas](https://github.com/natlas/natlas) project. Most importantly, in an effort to make it easier to scale this service going forward, as well as provide the best possible experience for both users and developers, I’ve decided to no longer support SQLite or MySQL, and instead will only support Postgres as the database backend. This allows me to build features that rely on Postgres data types and capabilities without worrying about cross-compatibility.

In addition to the Postgres change, I’ve also changed it so that the only supported way to store screenshots that the project takes is via S3-compatible storage. This, combined with the postgres change, eliminates the need to do volume mounts into the container, which means that running multiple server containers becomes more feasible, and based on prior experience, it becomes very necessary at a certain scale.

In the same spirit as these changes, I went through and found places where I was doing convoluted things and simplified them. Namely, 5 years ago I was apparently afraid to make very simple queries to the database if I didn’t need to, so I found ways to cache the database data in memory. This was… fine, but if you ever had more than one process or more than one container, states would quickly become out of sync. So I embraced the one or two extra queries (which are just gets on a primary key lol) and allowed the server to further reduce its own state. This simplified app startup as well as a bunch of administrative interfaces for configuration, and I’m no longer just attaching objects all willy nilly to the Flask app instance.

Finally, I switched the natlas project to use [uv](https://docs.astral.sh/uv/) instead of [Pipenv](https://pipenv.pypa.io/en/latest/). I’ve long been a fan of Pipenv, but only because it was the best tool available to handle the development experience and dependency pinning in a way that didn’t suck (in my opinion). But the thing it really did suck at was resolving dependency trees and installing packages. It was capable, don’t get me wrong, but it was slow. Like xkcd-chair-jousting levels of slow. UV, however, is blazing fast and handles basically all the same things that Pipenv did.

I did a [few other things here and there](https://github.com/natlas/natlas/commits/main/?since=2025-01-14&until=2025-01-19) if you’d like to take a deeper look, but that about captures the most of it. My next projects in the works for natlas are going to be rebuilding the UI to use [tailwind](https://tailwindcss.com/) (I have a love/hate relationship with tailwind, but it’s better than what I’ve got now), and rewriting the elasticsearch interface layer to use [elasticsearch-dsl-py](https://github.com/elastic/elasticsearch-dsl-py).

## ICANN & CZDS

I used to have access to ICANN’s [CZDS](https://czds.icann.org/home) service many many years ago, like, almost 10. But it was in an account with my employer’s email, which did help me justify the requests, but also means I lost access to it like 7 years ago.

I applied again as part of my independent company, Room 641A, and was approved for over 800 TLDs, with more coming in pretty much every work day. I was also rejected for a few, ones asking for FTP IP addresses, or wanting to know my physical address, things like that. I’m going to just leave those ones alone for now and focus on the ones accessible through CZDS directly.

My plan with access to this data is to start monitoring newly registered domains, as well as domains of particular interest, and start to build up a data set that I can use to improve the value of the Natlas project. I have big visions in mind, but some of those visions rely on starting to collect the data as soon as I can. And yes, I do know there are other commercial services out there that offer this data. Part of the fun is in building it myself.

Huge shout out to Ian Foster ([lanrat](https://github.com/lanrat/)) for helping me get a better understanding of what this sort of data pipeline can look like, as well as his [CZDS golang utility](https://github.com/lanrat/czds).

## Conference Work

I’m involved with an annual invitation-only conference and through some happenstance I’ve found myself even more involved this year. We’re attempting to shift the way the conference runs this year, so I’ve been busy coordinating that. But since it’s an invitation only conference, I’m also helping to make sure that we extend invites to eligible parties, and tracking the invites. I’m also coordinating a social event that I’m hosting after the conference, which I’ve never hosted before. So there’s a lot of stuff going on, and I don’t really talk about it, but thought it deserved a small callout since it *has* been something I’m focusing on and working on.

If you happen to be reading this and know the conference I’m talking about and are going to be attending said conference, come say hi, I might have a special secret gift.

## Interesting Links

* [Atproto and ownership of identity](https://anirudh.fi/blog/identity/) - An interesting short piece about how atproto approaches the ownership of identity. This is interesting to me because I was already thinking about running my own [PDS](https://atproto.com/guides/self-hosting) soon, now that I know they are available to run. You can also find me on bluesky at [@0xda.de](https://bsky.app/profile/0xda.de).
* [So You Want To Build Your Own Data Center (Part 1)](https://blog.railway.com/p/data-center-build-part-one) - An interesting post from Railway about building their own datacenter. I don’t want to build my own data center (or maybe I do?) but I do want to get my own IPv4 space and a rack to start hosting my projects in.
* [JetKVM](https://www.kickstarter.com/projects/jetkvm/jetkvm) - I’m a bit late to this one and so don’t currently have one, but I am excited about small form factor remote KVM options. I’d like one for each cluster in my NUC, purely so that I can remotely manage them without having to remove it from the rack and put it on my desk and hook up a mouse/keyboard.
* [Jellyfin gets support for RKMPP](https://jellyfin.org/docs/general/administration/hardware-acceleration/rockchip/) - Jellyfin (which I don’t currently use) added support for Rockchip VPU, which allows hardware acelerated transcoding on Rockchip devices, which are super low power and quite efficient, it seems. I don’t want to switch away from Plex yet, but I do like to support Jellyfin.
* [A 5.8MB png with a 1032:1 compression ratio](https://www.bamsoftware.com/hacks/deflate.html) - I don’t remember who I saw post about this, but I saved the link and its super cool. It’s basically a zip bomb but for png files. It’s 420 bytes of bzip2 and 50.625 Gigapixels. I bet this thing would crash many a website.
* [Homomorphic Encryption in iOS 18](https://boehs.org/node/homomorphic-encryption) - Evan has a lot of great post...