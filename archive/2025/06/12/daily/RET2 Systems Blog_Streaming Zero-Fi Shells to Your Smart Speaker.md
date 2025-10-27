---
title: Streaming Zero-Fi Shells to Your Smart Speaker
url: https://blog.ret2.io/2025/06/11/pwn2own-soho-2024-sonos-exploit/
source: RET2 Systems Blog
date: 2025-06-12
fetch_date: 2025-10-06T22:51:50.466181
---

# Streaming Zero-Fi Shells to Your Smart Speaker

# [![](/assets/img/logo-full.svg)](/) ENGINEERING BLOG

[# Streaming Zero-Fi Shells to Your Smart Speaker](/2025/06/11/pwn2own-soho-2024-sonos-exploit/)

## Exploiting the Sonos Era 300 with a Malicious HLS Playlist June 11, 2025 / Jack Dates & [Markus Gaasedelen](https://twitter.com/gaasedelen)

---

In October 2024, RET2 participated in the âSmall Office / Home Officeâ (SOHO) flavor of [Pwn2Own](https://www.zerodayinitiative.com/blog/2024/7/16/announcing-pwn2own-ireland-2024), a competition which challenges top security researchers to compromise consumer-focused network devices. This includes popular smart speakers, routers, IP cameras, printers, and network-attached storage (NAS) devices.

One of the two devices we targeted this year was the [Sonos Era 300](https://www.sonos.com/en-us/shop/era-300), a high-end smart speaker which retails for around $500 USD. The Sonos layers several security technologies to establish a chain of trust rooted in hardware, protect device specific secrets (ARM Trustzone, eFuses), and harden its primary runtime service against active exploitation. For a category of devices historically derided as â[junk hacking](https://web.archive.org/web/20141010194433/https%3A//lists.immunityinc.com/pipermail/dailydave/2014-September/000746.html),â things have certainly changed.

In this post, weâll touch on how past research was adapted to obtain a foothold on the device, providing us the necessary introspection to discover and exploit a powerful [memory corruption](https://wargames.ret2.systems/) vulnerability ([CVE-2025-1050](https://www.sonos.com/en-us/security-advisory-2024-0002)) in remotely accessible, unauthenticated attack surface, netting our exploit $60,000 USD from the competition.

[![](/assets/img/pwn2own_soho24_sonos_title_card.jpg)](/assets/img/pwn2own_soho24_sonos_title_card.jpg)

Jack Dates (far-right) of RET2 Systems attacking a Sonos Era 300 with a zero-day exploit at Pwn2Own 2024

## Device Reconnaissance

Going into any Pwn2Own, we weigh several factors deciding which devices we want to attack. This can range from how personally interesting the device seems to us, the prize money assigned to it, how many other competitors we think will poke at it, and how much time we expect the research to take.

We picked the Sonos smart speaker primarily because there was some amount of recent public research against the product family that seemed like useful context for getting started. While there wasnât any explicit research against the Sonos Era 300, we purchased it assuming there could be new functionality worth probing for vulnerabilities.

Previous Pwn2Own Sonos entries were also memory-corruption vulnerabilities, meaning remote attack surface involved native code, which aligned with our skills and experience.

[![](/assets/img/pwn2own_soho24_smart_speakers_zdi.jpg)](/assets/img/pwn2own_soho24_smart_speakers_zdi.jpg)

The list of smart speaker devices from ZDI and their respective prizes for Pwn2Own 2024

We made careful note of the following works and reviewed them while waiting for our device to arrive:

* [Shooting Yourself in the .flags â Jailbreaking the Sonos Era 100](https://www.nccgroup.com/us/research-blog/shooting-yourself-in-the-flags-jailbreaking-the-sonos-era-100/)
* [A 3-Year Tale of Hacking a Pwn2Own Target](https://www.youtube.com/watch?v=uGofhlB1vZU)
* [A Journey To Pwn And Own The Sonosâ¯One Speaker](https://www.synacktiv.com/sites/default/files/2022-11/sonos.pdf)
* [Dumping the Amlogic A113X Bootrom](https://haxx.in/posts/dumping-the-amlogic-a113x-bootrom/)
* [Smart Speaker Shenanigans: Making The SONOS One Sing](https://www.youtube.com/watch?v=Wqcbp9wFO7o)
* [Exploiting the Sonos One Speaker Three Different Ways: A Pwn2Own Toronto Highlight](https://www.zerodayinitiative.com/blog/2023/5/24/exploiting-the-sonos-one-speaker-three-different-ways-a-pwn2own-toronto-highlight)
* â¦

While itâs clear that Sonos products have received some real attention from high quality researchers in the past, being able to work off of prior research doesnât necessarily mean itâs going to be an easy target to take on.

For example, Synacktiv described how Sonos was sure to enable all major compiler-based mitigations (Cookies, PIE, RELRO) following their 2021 entry, while Orange Tsai [speculated](https://youtu.be/uGofhlB1vZU?t=2318) that Sonos was aggressively monitoring and patching crashes produced by researchers in 2022. NCC also [burned](https://www.nccgroup.com/us/research-blog/shooting-yourself-in-the-flags-jailbreaking-the-sonos-era-100/) several important bootloader bugs in 2023 which seemed like they would have been really useful for establishing a foothold on the Sonos Era 300.

## Device Teardown

Tearing down the Sonos Era 300 is a little tricky, but everything we care about is confined to one main logic board. The âPSUâ is integrated directly onto the main board rather than being a separate or modular unit which is a little unusual, and makes working with the logic side a bit more precarious with high voltage elements openly exposed on the bench.

The fit and finish on the unit is so precise that we basically wrote off ever re-assembling the device, too.

[![](/assets/img/pwn2own_soho24_sonos_motherboard.jpg)](/assets/img/pwn2own_soho24_sonos_motherboard.jpg)

The main Sonos Era 300, logic board + PSU combo

Removing the shielding, the top side of the board has two real chips of interest: a Mediatek MT7921 (wifi/bluetooth) and an 8GB Kingston EMMC / flash chip. We did not end up conducting any hardware or software research into the Mediatek chipset for Pwn2Own so we will not be discussing it further.

[![](/assets/img/pwn2own_soho24_sonos_flash_mtk.jpg)](/assets/img/pwn2own_soho24_sonos_flash_mtk.jpg)

A Mediatek MT7921 radio and Kingston EMMC on the top side of the Sonos Era 300 main logic board

On the bottom side of the board, we find the main CPU marked âS767eâ and some RAM chips under more shielding.

[![](/assets/img/pwn2own_soho24_sonos_cpu.jpg)](/assets/img/pwn2own_soho24_sonos_cpu.jpg)

CPU + RAM chips on the bottom of the Sonos Era 300 main logic board

Based on some googling and the work of previous researchers, the CPU appears to be an Amlogic chip, presumably the S905X3 or something pretty close to it. Even if we cannot find the exact chip, having a datasheet within the same family of chips / vendor can provide quite a bit of insight.

## Reading / Writing EMMC Flash

The first priority is for us to get a dump of the 8GB EMMC straight from the factory. This is useful for a number of reasons, as it could be an older firmware that may be hard or impossible to find online or elsewhere. It also provides a clean known-good backup in-case we accidentally update the device or brick it.

To do this, we need to locate some of the signal pins on the board.
We take a few pictures of the PCB and begin overlaying them with ball diagrams from the datasheet (stretched, skewed, and scaled) to fit approximately where the chip footprint should be. This gives us a rough map of where signals may be popping out on the other side of the board.

[![](/assets/img/pwn2own_soho24_sonos_ff_small.gif)](/assets/img/pwn2own_soho24_sonos_ff_small.gif)

Marking up the top/bottom of the board using photoshop to map out EMMC signals traveling to the CPU

This often works quite well, with a bit of reasoning on both where traces emerge from the EMMC and how they route into the CPU based on its ball placements we can predict almost all of them before even probing the board.

While the EMMC chip has all eight data lines routed to the CPU, when âhardware hackingâ it is common to wire up only one data line plus the CMD and CLK signals. This is sufficient for communicating with the EMMC chip in 1-bit / SD Mode to read or write its entire contents (albeit, slowly).

[![](/assets/img/pwn2own_soho24_sonos_emmc.jpg)](/assets/img/pwn2own_soho24_sonos_emmc.jpg)

30awg enameled copper wire connected to CLK ...