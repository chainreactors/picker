---
title: Weekly Retro 2024-W26
url: https://0xda.de/blog/2024/06/weekly-retro-2024-w26/
source: Blogs  dade
date: 2024-07-01
fetch_date: 2025-10-06T17:41:00.611893
---

# Weekly Retro 2024-W26

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/06/weekly-retro-2024-w26/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

11 minutes

# [Weekly Retro 2024-W26](https://0xda.de/blog/2024/06/weekly-retro-2024-w26/)

---

* [3D Printing](#3d-printing)
* [Declarative Disk Encryption w/ NixOS](#declarative-disk-encryption-w-nixos)
* [Accidentally Discovering Disk Failures](#accidentally-discovering-disk-failures)
* [What I’m Reading](#what-im-reading)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

I bought a 3D printer, I reformatted my Framework to add disk encryption, and I discovered some drive failures that I had no warnings for and try to save the data.

## 3D Printing

I’ve wanted a 3D printer for as long as I can remember. I remember in the late 2000s, my friend and I were in a CADD class together, using Solidworks to design parts. I was… okay, at it. But my friend was very good at it, so much so that he went on to become an engineer with a focus on human-centered mechanical engineering (I think).

During our time in that class together, he also designed a lot of custom twisty puzzles (which is apparently the generic name for Rubik’s cube type puzzles), and was able to make several sales of his designs to other enthusiasts, who would typically have them printed from Shapeways. 3D printers hadn’t really saturated the mainstream at this point, but I remember some of the early prototypes he got back from Shapeways being distinctly 3D printed in that coarse granularity that came with the early technology. It was so cool to have an idea, design it on the computer, and then have it delivered to your doorstep.

Fast forward several years and I had moved to California and several folks I knew at work were into the Maker sphere, attending hackathons, spending all their spare time at Hacker Lab in Sacramento, etc. It was very clear that 3D printers were getting significantly better, and significantly more affordable. I even went to a [Hak5 Hack Across America](https://www.youtube.com/watch?v=3ux-rbR07LI&list=PLW5y1tjAOzI2mUf0qPzNHEjR6F9q4RZdu&index=20) event in 2013 at the Printrbot headquarters, where I got to meet Darren (who, little did I know at the time, would later become a friend and mentor). But I didn’t have the disposable funds, nor the mechanical inclination to deal with putting together my own 3D printers and fighting with them to get prints to work.

Well, now I’ve solved the first part of that, at least – I have the disposable funds. Still no mechanical inclination, but we’ll get there. 3D printers have also come a long way in the past 10 years, so I feel like I’ll spend less time fighting the printer and more time just printing. The 3D printing community has also come a long way, so I’m not worried about being able to get help should I struggle.

![Marketing photo of the Bambu A1 mini 3D printer, complete with 4-color printing](https://0xda.de/blog/2024/06/weekly-retro-2024-w26/img/bambu.3c1342a8913bbea327ba82089f1cb76b.png)

All this to say, I bought a [Bambu A1 mini combo](https://us.store.bambulab.com/products/a1-mini) (which is currently on sale), and it’s sitting in the box on the floor behind me as I write this. I plan to get it setup this week and hopefully have some pictures to share next week (or perhaps in a standalone post about my experience, not sure yet). I picked this printer because it seems fairly beginner friendly, the price point is affordable for a random hobby I’ll probably neglect (hello ADHD), and it has a small enough footprint that it should fit on the shelf behind my desk.

## Declarative Disk Encryption w/ NixOS

![Photo of luks passphrase prompt on my NixOS Framework 16](https://0xda.de/blog/2024/06/weekly-retro-2024-w26/img/luks-passphrase.4f7b3204717fec690173910505b0e663.jpeg)

Those of you following my RSS feed have probably seen my Framework laptop posts, in which I have been documenting my experience getting NixOS setup on it. I’ve been in pursuit of my ideal desktop operating environment – one I can easily repair, one I can make configuration changes on without (as much) fear of bricking it, and one I can wipe and get back to an ideal state as easy as possible.

I’m not going to dive too deep into the whole series of posts, but you’re welcome to check out the [#nix](https://0xda.de/tags/nix/) tag to see them all. But my [latest update](https://0xda.de/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/) is that I now have my disk partitions and filesystems declaratively managed with disko, using a lukscrypt volume with btrfs volumes. My end goal is to subscribe to the [Erase Your Darlings](https://grahamc.com/blog/erase-your-darlings/) philosophy, using something like [Impermanence](https://github.com/nix-community/impermanence).

## Accidentally Discovering Disk Failures

I’ve been a bit of a data hoarder for as long as I’ve had a computer, I think. I love having data on my device. It all began with my first brand new desktop computer. It had a 500GB hard drive in it, and no real room for expansion. After working through the summer for minimum wage, I had managed to buy a new, bigger case for it, as well as a new 1TB hard drive. This was around summer of 2011. (Note: I had several computers before this, but most were scavenged from hospital or school dumpsters, or bought secondhand).

This was my only computer, so it was also my gaming computer, and the computer I did my college homework on. It ran Windows. Over the years, I would buy another hard drive so I could continue to expand my gold pile (In this analogy, I am like a dragon, except instead of hoarding gold coins and treasures, I am hoarding installers of software that stopped working 10 years ago).

Back in 2019, I think, I replaced that computer with a new one meant purely for gaming, and the old one became purely used for running services and media. But at this point, it had 6 4TB drives in it (in pairs of 2 mirrored NTFS volumes, so I was throwing away a lot of space). It was still running windows, and I didn’t have the free hard drive space to move the data around and reinstall linux on it and use linux filesystems. So I just left it running windows. It ran qbittorrent to download linux ISOs[1](#fn:1), Plex to serve those linux ISOs[1](#fn:1) to my friends, sonarr and radarr to automatically find new linux ISOs[1](#fn:1), and occasionally it was also a Minecraft or Valheim server.

A couple years ago, I bought a Synology NAS, which currently has 4 18TB drives in it, in a RAID 5 array. Just one of these drives was more than enough to migrate the whole collection of data I had on the old machine. The old machine’s drives became purely for seeding linux ISOs[1](#fn:1). Some 1500 of them, spanning 8TB or so, and all the long term storage was moved to the NAS.

But I kept running into issues where I’d fill up a volume and then future linux ISOs[1](#fn:1) wouldn’t download correctly. So I finally had enough of it this week and decided I would move files around, break the mirrored volumes, and get into a parity configuration. When I went into the Windows Disk Management tool, I discovered that one of the drives in one array was entirely offline, and another was in an error state.

Purely by happenstance, I managed to find this issue. I had no monitoring in place, got no notifications, saw no warnings, nothing. So I started to move quickly to take the remaining drives that were in good condition, and put them into a Windo...