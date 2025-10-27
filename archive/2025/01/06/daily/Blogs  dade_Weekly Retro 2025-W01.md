---
title: Weekly Retro 2025-W01
url: https://0xda.de/blog/2025/01/weekly-retro-2025-w01/
source: Blogs  dade
date: 2025-01-06
fetch_date: 2025-10-06T20:07:29.557551
---

# Weekly Retro 2025-W01

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/01/weekly-retro-2025-w01/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

7 minutes

# [Weekly Retro 2025-W01](https://0xda.de/blog/2025/01/weekly-retro-2025-w01/)

---

* [Obsidian Plugins](#obsidian-plugins)
* [Reviving Natlas](#reviving-natlas)
* [How do I even release this package?](#how-do-i-even-release-this-package)
* [Oh wow I almost forgot about my new server](#oh-wow-i-almost-forgot-about-my-new-server)
* [A new video series?](#a-new-video-series)
* [Interesting Links](#interesting-links)

---

Alright Alright Alright. I took a few weeks off again, for the holidays this time. That doesn’t mean I didn’t get anything done, but I also didn’t want to feel the pressure to come up with something to write about each week. Realistically I watched a lot of TV and played a lot of games, and managed to sneak a few more productive things in from time to time.

## Obsidian Plugins

I had never written an obsidian plugin before, but I can confidently say that is no longer true. I cannot confidently say that I have interest in doing it again, but it is cool to get an idea for how they work, at least.

I saw a [post from Kelly Shortridge](https://bsky.app/profile/shortridge.bsky.social/post/3ldqzct27ns2e) about [deciduous.app](https://deciduous.app), a tool for decision tree threat modeling. The post actually highlights a new VS Code extension that brings the same capabilities into the IDE. This got me thinking, I do most of my note taking in Obsidian these days, and this seemed to operate pretty similarly to mermaid, which is just a markdown processor in Obsidian.

So anyways, I spent an afternoon hacking together the [Deciduous Obsidian Plugin](https://github.com/0xdade/deciduous-obsidian-plugin). You can render your decision trees directly into your notes using triple tick code block notation. E.g.  ```` ```deciduous ````.

I don’t really plan to maintain this plugin, and haven’t submitted it to the community plugin repository. But it was a fun experience.

## Reviving Natlas

Some of you may remember back in 2018-2020, I was all in on a project called [Natlas](https://github.com/natlas/natlas). I was live streaming development, and I was pushing changes quite frequently.

At a certain point, around the same time that I started my current job, I started to get overwhelmed with working on Natlas. There are so many things I wanted to do, but the developer experience was pretty terrible (untyped python sucks), and I had written things in such a spaghetti fashion that to make improvements, it almost felt like I was going to have to rebuild entire chunks of it from scratch.

I also found myself making decisions by committee, listening to too many people about what to do, which resulted in many things being sort of half-functional or half-supported. It also meant that making new changes was harder, because I was trying to appease too many people. Too many supported deployment strategies. Too many supported database backends. Uncertainty around whether I wanted the project to just be a community “Hey come scan with us, we’ll make a leaderboard for most port scans” or if I wanted it to be something where an individual or a team could work together for things like scanning corporate networks (internal or external).

I think in hindsight, the answer was always the latter – there were multiple active users in the corporate security space, using this for red team purposes, but also using it to help defense teams augment their lack of visibility into what is on the network. In an ideal world you know every device you have on the network and you know exactly what ports and services are running on each device. This quickly loses feasibility as the network gets bigger, though. So Natlas was great at helping those teams have a decent idea of what was on their network. Especially in incident response scenarios, where some service is vulnerable and you need to know if it’s on your network. For some reason your expensive Cisco router doesn’t have a Crowdstrike agent telling you what is running on it, but nmap never lies.

So anyways, I’ve found some inspiration to get back into it and I’ve started modernizing the code base. There have been 40 commits in the past week. Once I get things into shape the way I would like them, I’m going to start looking for opportunities to commercialize (while keeping the project open source, always). Managed deployments, consulting on deployments for companies, support contracts, custom feature development, etc. If your company could benefit from being able to query “what ports are open on my network” or “What versions of ssh are running” or “where are those pesky IIS servers” or anything else, please reach out via [Room 641A](https://room641a.com/).

## How do I even release this package?

As I revisit software that I mostly haven’t touched in several years, I am learning (1) how bad a developer I used to be, and (2) how much better I’ve gotten since then.

One area that I’ve been a bit annoyed with is that I wanted to go release a new version of [CyclicPRNG](https://github.com/natlas/cyclicprng) to fix some issues with class variables and mutable defaults (a common theme among my old code, I didn’t know better), but I had not left myself any instructions on how to do that. Thankfully the package itself is one dependency and one file, so it wasn’t a particularly difficult thing to build. But I figured I may as well update the process so that I never really have to worry about it again.

Now I have a [publish.yaml workflow](https://github.com/natlas/cyclicprng/blob/main/.github/workflows/publish.yaml) that uses PyPI Trusted Publisher to build and push a release to PyPI whenever I push a tag for a new version. Trust Publisher is a super cool OIDC workflow that allows setting up trusted workflows that publish packages, eliminating the need for PyPI credentials in your github workflows. Highly recommend, I’m going to set it up with my other packages as well.

## Oh wow I almost forgot about my new server

![TrueNAS SCALE dashboard](https://0xda.de/blog/2025/01/weekly-retro-2025-w01/truenas.54a879c7b163dd969b1c575388dd9049.png)

I have a new server! It’s a 45HomeLab HL-15 running TrueNAS SCALE. It’s my first experience with TrueNAS and my first experience with ZFS. But I do have lots of hard drive and SSD space, and lots of room to grow. I can finally retire my old plex server, which used to be my gaming computer about 10 years ago, is running on Windows with a bunch of jank old 4TB drives (and a few 2TB drives), on a desktop processor from the Sandy Bridge days. That’s a 13 year old processor. It’s been doing okay, but I’m very eager to get the services moved over to the TrueNAS box and let that old machine retire.

I just need to figure out how to do ingress proxying to the TrueNAS apps/docker containers so that I can set up DNS names and trusted certs for everything. But then again, I don’t have that setup on my current server, so maybe I should just move over and deal with figuring that out later.

## A new video series?

I’ve been toying with an idea for an educational video series for over a year now, but I haven’t gotten around to making it a reality. I think I let the pressure of producing to a certain quality standard get in my way, and so now it’s been like 15 months since I had the idea, and I still haven’t published a single video.

I’m going to try to make an effort to get videos written, recorded, edited, and pub...