---
title: Hello Sprout
url: https://daniel.haxx.se/blog/2025/07/28/hello-sprout/
source: daniel.haxx.se
date: 2025-07-29
fetch_date: 2025-10-06T23:54:04.105794
---

# Hello Sprout

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/framwork-top.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Development](https://daniel.haxx.se/blog/category/development/)

# Hello Sprout

[July 28, 2025](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [10 Comments](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/#comments)

Sprout is the name of my new machine that just arrived. The [crowd-funded laptop](https://daniel.haxx.se/blog/2025/07/12/sponsor-my-laptop/). Since this beauty is graciously sponsored by a large crowd of people I felt I should share a little bit of its journey and entry into my life.

First I needed a name for it, and since it is small and is meant to grow with me a bit, I think Sprout feels apt.

## The crowd-funding

Starting the initiative on a Saturday afternoon might not have been the most clever thing to get widest possible reach, but it seems it did not matter. We reached the goal of 3,500 USD within 90 minutes and people have kept on donating even after that and the counter is now at 7,000 USD. Amazing.

As mentioned: all surplus ends up in the general curl fund and will be used solely and exclusively to cover expenses that benefit and favor curl and its development. That is a promise. The [curl fund](https://opencollective.com/curl) is also completely open and transparent so everyone who wants to can in fact monitor our finances to verify this.

## Specs

I decided to go with a Framework laptop because I like and want to support their concept of modular and upgradable laptops. After the overwhelming funding round, I decided to go with the top of the line AMD CPU alternative they offer, 96GB of RAM and 4TB of storage. This should make the laptop last a while I think.

* CPU: AMD Ryzen AI 9 HX 370. Up to 5.1 GHz. 12 cores, 24 threads.
* Graphics (integrated): AMD Radeon 890M. Up to 2.9GHz. 16 Graphics Cores
* Wifi: AMD RZ717 Wi-Fi 7
* Display: 13.5″ 2880×1920 120Hz matte display (3:2 ratio)
* Memory: DDR5-5600 – 96GB (2 x 48GB)
* Storage: WD\_BLACK SN850X NVMe – M.2 2280 – 4TB
* Laptop Bezel: Framework Laptop 13 Bezel – Black
* Keyboard: Swedish/Finnish (2nd Gen)
* Dimensions: 15.85mm x 296.63mm x 228.98mm
* Weight: 1.3 Kg

## Outputs

The laptop has four slots available for ports. I have USB-C, USB-A, HDMI and external Ethernet modules. I bought a few more than four, because I don’t know which exact setup I will prefer and they are interchangeable so I can change them according to the situation I’m in.

## Dimensions compared to the old

My old laptop was a Lenovo T470S 14″.

Dimensions: 18.8 mm x 331 mm x 226.8 mm
Weight 1.32 kg

So the new one is 3 mm thinner, 3 cm narrower and pretty much the same depth (+2mm) and pretty much the same weight.

## Assembling

Ordered without Windows installed (of course), this thing arrived like an IKEA flat-pack and there was some assembly required. The necessary screwdriver comes included and I could complete the task in under ten minutes. Not at all complicated.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/sprout-internals.jpg)

The Framework 13 as shipped: without memory, storage, keyboard, bezel etc.

## Linux

I noticed two different Linux distributions offered as “easy installs” with guides from Framework, but as none of them were Debian I opted to take the more complicated route.

## Debian

I downloaded a DVD iso image for Debian testing, copied it onto a USB stick and booted up Sprout with it. The installation went like a breeze and it detected the Wifi networking just fine.

Once the system came up for real without the USB stick, I edited the necessary files and took it up to current Debian Unstable over wifi with no problems.

## Initial glitches

I experienced some glitches (X or the keyboard or something would stop accepting input after 5-15 minutes of use), which I first thought was due to an older Linux kernel as I had friends tell me that I might need 6.15+ for proper hibernation support and Debian unstable only has a 6.12 one just now. I switched to the Debian experimental kernel (6.16-rc7) but the issue remained. Hm?

I then remembered I hadn’t upgraded the laptop BIOS to its latest version yet, and after having invoked

```
fwupdmgr refresh --force
```

```
fwupdmgr get-updates
```

```
fwupdmgr update
```

and done a reboot, it first seemed to have fixed the problems but I was wrong. Is it X11 related? I have now switched my desktop to Plasma/Wayland to see if it fixes the problem. I might switch around a little bit more if I see it again because it is clearly a software glitch and not a hardware problem. Hardly Framework’s fault but instead more of a thing that happens occasionally when you run bleeding edge stuff. I’ll sort it out.

## Console

Having a small but high DPI screen and trying to use the console with its default (tiny) font is next to impossible, at least with my aging eyes, so I spent a few minutes to figure out how to use *setfont* and then to invoke `dpkg-reconfigure console-setup`.

I find it a little curious that the Debian installer doesn’t have any easy provided option to do this already at install time.

## A message

A few days after I had received my laptop I received a package via FedEx, and as I opened it I found this lovely note and some presents from Framework!

I know some of my followers tagged and mentioned Framework during the crowdfunding campaign but I of course didn’t expect anything from that.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/framework-note.jpg)

A note from the Framework founder

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/framework-gifts.jpg)

Gifts from Framework

The thing that looks like a CD-R among the gifts is actually a mouse mat, slightly larger than a CD. The small packages are USB-C modules for the laptop.

This little message still holds and shows more appreciation than what I have received from most companies that ever used my Open Source. It’s not a high bar. I truly appreciate it – said entirely without sarcasm.

## Impressions and Performance

Just to give you a small idea of the performance difference, I decided to compare a simple but common operation I do. Build curl. It basically requires three command lines:

### autoreconf -fi

This invokes a series of tools to setup the build.

Sprout: 4.8 seconds

Old: 9.3 seconds

**Diff: 1.9 times faster**

### configure –with-openssl

A long series of single-threaded tests of the environment. Lots of invokes of gcc to check for features, functions etc.

Sprout: 10.4 seconds

Old: 11.1 seconds

**Diff: 1.1 times faster**

### make -sj

This invokes gcc and forks off lots of new processes. The old machine’s 4 threads vs the new 24 threads probably plays a role here.

Sprout: 8.9 seconds

Old: 60.6 seconds

**Diff: 6.8 times faster**

(My [desktop PC](https://daniel.haxx.se/blog/2023/02/20/my-2023-dev-machine/) does the same in under 4 seconds.)

## Keyboard

This is not a full-time development machine for me and I have never been fully productive on a laptop and I don’t expect to be on this new one either. I don’t think a laptop keyboard exists that can satisfy me the way a proper one can.

The Framework one does not have dedicated page up/down keys for example. The keys still feel decently fine to press and I think I will adjust to the layout over time.

## Stickers

I offered everyone who donated 200 USD or more for the laptop sticker space on my cover, but so far not a single one has reached out to make this reality. To h...