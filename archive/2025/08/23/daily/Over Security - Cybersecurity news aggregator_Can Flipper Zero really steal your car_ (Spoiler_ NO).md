---
title: Can Flipper Zero really steal your car? (Spoiler: NO)
url: https://blog.flipper.net/can-flipper-zero-steal-your-car/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-23
fetch_date: 2025-10-07T00:49:04.226478
---

# Can Flipper Zero really steal your car? (Spoiler: NO)

[![Flipper Blog](https://blog.flipper.net/content/images/2022/07/orange_text_transpar-2.png)](https://blog.flipper.net)

* [Home](https://flipperzero.one/)
* [Shop](https://shop.flipperzero.one/)
* [Docs](https://docs.flipper.net/)
* [Downloads](https://flipperzero.one/downloads)
* [Community](https://flipperzero.one/community)

Subscribe to notifications of new posts:

You're subscribed

Oops! Please try again

Subscribe

[Flipper Zero](https://blog.flipper.net/tag/zero/)

# Can Flipper Zero really steal your car? (Spoiler: NO)

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)

#### [Pavel Zhovner](/author/zhovner/)

Aug 22, 2025

![Can Flipper Zero really steal your car? (Spoiler: NO)](/content/images/size/w2000/2025/08/scam_cars.jpg)

You may have seen news reports about the “secret” Flipper Zero firmware that allegedly hacks any car, as covered by [The Verge](https://www.theverge.com/cars/763446/flipper-zero-car-theft-firmware-hack-key-fob), [Gizmodo](https://gizmodo.com/flipper-zero-cars-hacking-2000646318), [404 Media](https://www.404media.co/inside-the-underground-trade-of-flipper-zero-tech-to-break-into-cars/), and [The Drive](https://www.thedrive.com/news/this-199-hacking-device-will-probably-let-thieves-steal-your-car) have all written about it.  Let’s dive in to see whether this claim holds up (major spoiler: it doesn’t).

## What happened

Some darknet online stores have started selling so-called *“*private*”* firmware for Flipper Zero, claiming it can hack countless cars. They say new vulnerabilities have “leaked” online that make it possible to break dynamic protocols like KeeLoq.

In reality, all of these methods were published more than 10 years ago — nothing new at all. The authors of such firmware are simply recycling well-known vulnerabilities and presenting them as “new hacks.” And importantly, these vulnerabilities have nothing to do with real car theft, since they do not allow you to start the engine.

## How the KeeLoq protocol works

![](https://blog.flipper.net/content/images/2025/08/keeloq_old.jpg)

KeeLoq protocol vulnerabilities have been known since 2006

[KeeLoq](https://en.m.wikipedia.org/wiki/KeeLoq) was developed in the 1980s and used in older access systems like garage doors and early car alarms. It’s what’s called a *rolling code* or *hopping code* system. The idea is that every transmission uses a new unique signal, encrypted with a 64-bit manufacturer key. This manufacturer key is the weak spot of KeeLoq. The problem was that carmakers often used the **same key across an entire model line**. If that key leaked, an attacker could intercept signals from any remote of that brand.

The authors of these “hacker” firmwares are just redistributing old leaked manufacturer keys from various automakers. None of this is new — these vulnerabilities were thoroughly documented back in **2006**: [https://web.archive.org/web/20221206050746/https://www.cosic.esat.kuleuven.be/keeloq/](https://web.archive.org/web/20221206050746/https%3A//www.cosic.esat.kuleuven.be/keeloq/)

Since then, car manufacturers have moved on to more modern radio protocols with two-way authentication, where the car and the key exchange messages to verify authenticity.

## You can “hack” it with just a piece of cable

Because analyzing the encrypted protocol is passive, all you need for an “attack” is to record the remote’s radio signal. You don’t need Flipper Zero — even a piece of wire connected to an audio jack would do.

[![](https://img.spacergif.org/v1/1280x720/0a/spacer.png)](https://blog.flipper.net/content/media/2025/08/how_to_receive_radio_signal_with_a_piece_of_wire--1-.mp4)

0:00

/1:58

1×

[video] Demonstration on how to receive a signal from a radio remote using a piece of wire

# How car theft actually works

Intercepting a remote signal is not enough to start a car. That’s why these KeeLoq attacks have nothing to do with real-world car theft.

Today, real thieves target **keyless entry/start systems** by attacking the key fob directly. They use a combination of relays and transmitters that **proxy the signal** from the real car key, tricking the car into thinking the key is nearby.

![](https://blog.flipper.net/content/images/2024/03/car_keyless_repeater_system--1-.jpg)

Thieves trick the car into thinking the key fob is near

We covered this technique in detail in our article: [Response to Canadian Government](https://blog.flipper.net/response-to-canadian-government/)

**TL;DR**: Real car thieves don’t use Flipper Zero — they have purpose-built relay tools. Here’s a video showing how cars are actually stolen with these devices:

[![](https://img.spacergif.org/v1/1920x1080/0a/spacer.png)](https://blog.flipper.net/content/media/2025/08/car_thieves_use_keyless_repeaters_to_steal_cars_compressed.mp4)

0:00

/0:34

1×

[video] CCTV footage showing how thieves steal cars with keyless entry systems

## Conclusions

* The so-called hacker firmwares for Flipper Zero don’t add anything new — they just reuse techniques documented since 2006.
* Real car thieves use completely different, specialized tools.
* If your car could be attacked with Flipper Zero, it could just as easily be hacked with a piece of wire.

[![Firmware 1.0 Released](/content/images/size/w600/2024/09/Flipper_Zero_Firmware_1.0_main_illustration_compressed-1.jpg)](/released-firmware-1/)

[## Firmware 1.0 Released

Meet the first major release of Flipper Zero firmware — version 1.0. In this release, we have completed work on many features that have been in development for 3 years and are now stable. In this post, we’ll show you what’s new in Firmware 1.0 and the](/released-firmware-1/)

* [![Ruslan Nadyrshin](/content/images/size/w100/2024/03/007.jpg)](/author/ruslan/)
* [![Alexey Zakharov](/content/images/size/w100/2024/08/IMG_7628.jpeg)](/author/alexey/)

[Ruslan Nadyrshin](/author/ruslan/), [Alexey Zakharov](/author/alexey/)
Sep 10, 2024 • [comments](/released-firmware-1/#comments)

[![Our Response to the Canadian Government](/content/images/size/w600/2024/03/flipper_zero_against_ban_in_canada.jpg)](/response-to-canadian-government/)

[## Our Response to the Canadian Government

In just a few years, Flipper Zero has become so popular that it’s now surrounded by many myths. It’s no wonder that people in power are trying to make Flipper Zero illegal. As you might have seen in the news, the Canadian government plans to ban Flipper Zero](/response-to-canadian-government/)

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)
* [![Alexey Zakharov](/content/images/size/w100/2024/08/IMG_7628.jpeg)](/author/alexey/)
* [![Ruslan Nadyrshin](/content/images/size/w100/2024/03/007.jpg)](/author/ruslan/)

Multiple authors
Mar 19, 2024 • [comments](/response-to-canadian-government/#comments)

[![Introducing Video Game Module Powered by Raspberry Pi](/content/images/size/w600/2024/02/Video_Game_Module_powered_by_Raspberry_Pi-1.jpg)](/introducing-video-game-module-powered-by-raspberry-pi/)

[## Introducing Video Game Module Powered by Raspberry Pi

We're excited to announce the Video Game Module, our new product developed in collaboration with Raspberry Pi! The module is powered by the first chip designed by Raspberry Pi—the RP2040 microcontroller, the same as in the Raspberry Pi Pico board.
We slightly overclocked the microcontroller so it could generate](/introducing-video-game-module-powered-by-raspberry-pi/)

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)

[Pavel Zhovner](/author/zhovner/)
Feb 13, 2024 • [comments](/introducing-video-game-module-powered-by-raspberry-pi/#comments)

#### Community

[Kickstarter](https://www.kickstarter.com/projects/flipper-devices/flipper-zero-tamagochi-for-hackers)
[Habr.com](https://habr.com/ru/company/flipperdevices/)
[Discord](https://flipperzero.one/discord)
[...