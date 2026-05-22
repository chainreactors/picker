---
title: Flipper One — we need your help
url: https://blog.flipper.net/flipper-one-we-need-your-help/
source: Over Security
date: 2026-05-21
fetch_date: 2026-05-22T06:08:16.666352
---

# Flipper One — we need your help

[![Flipper Blog](https://blog.flipper.net/content/images/2022/07/orange_text_transpar-2.png)](https://blog.flipper.net)

* [Home](https://flipper.net/)
* [Products](https://flipper.net/collections)
* [Docs](https://docs.flipper.net/)
* [Downloads](https://flipper.net/pages/downloads)
* [Community](https://flipper.net/pages/community)

Subscribe to notifications of new posts:

You're subscribed

Oops! Please try again

Subscribe

[Flipper One](/tag/flipper-one/)

# Flipper One — we need your help

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)

#### [Pavel Zhovner](/author/zhovner/)

21 May 2026
• 18 min read

[Share](#/share)

![Flipper One — we need your help](/content/images/size/w2000/2026/05/Flipper-One-we-need-your-help-main-v2.jpg)

We're finally ready to talk about Flipper One — a project we've been grinding on for years and have rebuilt from scratch several times. It's an incredibly hard project, both financially and technically. So today we're going public not with a big shiny announcement, but to tell the whole story straight. Honestly? We're genuinely terrified, and we need your help.

**TL;DR** With Flipper One, we're reimagining what a Linux cyberdeck can be — it's a huge project. We're opening up the development process and asking the community for help.

**With Flipper One, we’ve set ourselves a list of ambitious goals:**

* Build the most open and best-documented ARM computer in the world, with full mainline Linux kernel support.
* Push vendors to open up their existing closed-source code and ditch binary blobs entirely.
* Build an unconventional hardware platform based on a co-processor architecture that pairs a microcontroller with a CPU, and port tons of low-level MCU code.
* Rethink how people use Linux and develop our own GUI framework with wrappers around existing CLI utilities.

Many of these goals come with a lot of uncertainty, which is scary. But we believe this is the only way to make a truly meaningful contribution to the open-source community and to education.

# What is Flipper One?

![](https://blog.flipper.net/content/images/2026/05/What-is-Flipper-One-new.jpg)

Flipper One isn't an upgrade to Flipper Zero — it's a completely different project with its own goals. Flipper One is an open Linux platform you can build almost anything on: from a 5G-enabled IP network analyzer to an SDR-powered radio signal analyzer with local AI. We focused a lot on the hardware expansion system. You can connect high-speed modules to Flipper One over PCI Express, USB 3.0, and SATA interfaces. Add an SDR, a fast SSD, or a cellular modem — just plug in the right module.

Flipper One comes with several network interfaces: 2x Gigabit Ethernet, USB Ethernet (5 Gbps), and Wi-Fi 6E (2.4/5/6 GHz). You can add 5G connectivity by plugging in an M.2 modem. That means you can use Flipper One as a router, a VPN gateway, or a bridge between wired and wireless networks.

# Zero vs One

Flipper Zero and Flipper One are completely different projects built for different tasks. The easiest way to think about it is in terms of networking layers:

* **Layer 0** — Offline point-to-point access-control protocols: NFC, low-frequency RFID, Sub-1 GHz radio, Infrared, wired protocols like iButton, UART, SPI, I²C. Based on a low-power microcontroller.
* **Layer 1 —** Everything that's IP-connected: Wi-Fi, Ethernet, 5G, and satellite. It's all about networking, data transfer, and high-performance computing. Running on powerful hardware and an open Linux toolkit — enough computing power to handle SDR and local AI.

![](https://blog.flipper.net/content/images/2026/05/Zero-vs-One-comparison-new.png)

Flipper Zero and Flipper One operate at different protocol layers and are not meant to replace each other

So they're not "newer" and "older" generations of the same product. Flipper One doesn't replace Flipper Zero — they're different categories of devices.

# Truly Open Linux platform

We want to build a truly open Linux hardware platform — the best-documented ARM computer, one that works out of the box on any recent upstream kernel. It will never go stale because it'll keep getting the latest updates. Our goals:

* Full mainline Linux kernel support
* No binary blobs, closed drivers, or proprietary firmware
* No vendor-locked BSP (board support package)

![](https://blog.flipper.net/content/images/2026/05/Flipper-One-Linux-UI-rotated.jpg)

We say "truly open" because the current state of ARM Linux is depressing. Every vendor bolts on their own custom mess: closed boot blobs, vendor-specific patches, "board support packages" that nobody outside the chip maker can really understand. You can no longer just read the specs and understand how computers work — you can only learn the workarounds for one specific chip with one specific BSP. We're sick of this ourselves, and we don't want to be part of the problem by shipping yet another product that just adds to the mess.

To pull this off, we've partnered with the **Collabora** team to push full support for the Rockchip RK3576 SoC into the mainline Linux kernel. Practically, this means you can download the kernel directly from [kernel.org](https://kernel.org/), with zero vendor patches, and run it on your Flipper One.

👩‍👩‍👧‍👦

****Flipper + Collabora — Making things open together****
We've partnered with Collabora to bring the RK3576 SoC into the mainline kernel and give Flipper One full upstream support.
Read more: [Collabora blog post](https://www.collabora.com/news-and-blog/news-and-events/collabora-flipper-opening-up-the-rk3576.html)

Current RK3576 mainline support is in pretty good shape, and all the major components are working. But there's still one last binary blob in the boot chain — the **DDR trainer**, which initializes RAM during early boot.

We're asking the community to help us polish RK3576 support so we can build a truly open platform together. We'd be glad for any kind of contribution, not just code. For example, maybe you can find a way to convince Rockchip to open up that last blob.

Right now, we're focused on power management and USB DP Alt-mode support. There are also drivers and accelerators that aren't fully upstream yet — the NPU, hardware video decoding, and other accelerators. Collabora maintains a public list of what's already working in mainline and what isn't, and we'd love help closing those gaps.

![](https://blog.flipper.net/content/images/2026/05/rk3576-current-support-2.jpg)

Current status of RK3576 support in BSP kernel and mainline Linux kernel

* [RK3576 open source roadmap](https://docs.flipper.net/one/cpu-software/rk3576-mainlining) — what we plan to do and how you can contribute
* [Open tasks](https://docs.flipper.net/one/open-tasks) — where you can help us
* [RK3576 mainline status](https://gitlab.collabora.com/hardware-enablement/rockchip-3588/notes-for-rockchip-3576/-/blob/main/mainline-status.md) from Collabora

# Developer Portal – let's build together

![Flipper One developers portal](https://cdn.flipper.net/flipper-one-developer-portal-splash-cropped.jpg)

Openness has always been our thing. With Flipper One, we want to go further — not just open-source code, but an **open development process**. We're publishing our task trackers, internal discussions, half-finished docs, and architectural debates. All the messy stuff companies usually keep behind closed doors.

### Introducing → [**Flipper One Developer Portal**](https://docs.flipper.net/one)

###

This is uncomfortable. We've never been this open before, and there's a real instinct to hide the unfinished work, the wrong turns, and the arguments. But we believe the educational value of building openly is worth more than the polish of pretending it was easy.

## What is the Developer Portal?

Flipper One Developer Portal is a public wiki with all the development documentation for Flipper One, and anyone can edit it. The portal describes the project's structure...