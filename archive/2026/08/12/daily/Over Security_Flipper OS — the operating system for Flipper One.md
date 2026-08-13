---
title: Flipper OS — the operating system for Flipper One
url: https://blog.flipper.net/flipper-os-the-operating-system-for-flipper-one/
source: Over Security
date: 2026-08-12
fetch_date: 2026-08-13T04:05:01.054671
---

# Flipper OS — the operating system for Flipper One

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

 Featured

# Flipper OS — the operating system for Flipper One

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)

#### [Pavel Zhovner](/author/zhovner/)

12 Aug 2026
• 9 min read

[Share](#/share)

![Flipper OS — the operating system for Flipper One](/content/images/size/w2000/2026/08/flipper_os_compressed.png)

**TL;DR:** Flipper OS is an additional layer on top of a standard Debian-based Linux system. It lets you switch between multiple preconfigured system profiles for different tasks, so you can experiment freely without worrying about breaking your setup or turning it into a mess.

Why build Flipper OS, yet another operating system, when there are already so many? Why not simply take a standard Debian-based system, as Raspberry Pi does, and customize it?

The problem is that conventional Linux distributions are designed for traditional computers/servers. They are not convenient for a multitool like Flipper One, which can be a network router, a radio lab, a desktop computer, or a TV media box all on the same device.

### **What we want to build into Flipper OS:**

**System profiles** — preconfigured operating system images for different tasks, such as a network router, radio lab, desktop computer, and TV media box. Each profile has its own settings, kernel, device tree, and set of applications.

**Unbreakable playground** — users can clone profiles and modify anything inside them, from the kernel to the system files. You can install whatever you want without worrying about breaking the device.

**Reset to default** — wow, what an innovation💀! Yet even in 2026, most Linux systems still don't let you roll back your changes and return to a clean system after breaking it.

**Atomic updates** —updating Linux today is still an unpredictable operation. No matter how badly you've broken the system, we want to guarantee that it can still update to a new version.

# Trash system problem

We all love single-board computers like Raspberry Pi. They are perfect for DIY projects when you need a tiny Linux box that is always close at hand. Today it is a home server, tomorrow you repurpose it as a servomotor controller, and the day after that as a debug probe. Each time, you completely reconfigure the operating system, kernel, and device tree.

This is what the typical workflow looks like when using an SBC in your projects:

> Install a clean system on an SD card → Install packages and configure them for one project → Rework everything for a different project → End up with a trash system → Reinstall everything from scratch.

![](https://blog.flipper.net/content/images/2026/08/IMG_7220.PNG)

If you use one OS for multiple projects at once, the system always turns into a garbage dump that's impossible to use

### Containers don't always do the job

To solve this problem, developers made containers such as Docker, along with all kinds of modern virtualization and containerization systems. They work perfectly when you need to isolate user space applications. But when you need to work close to the bare metal, patch the kernel, modify the device tree, reconfigure HDMI port or Wi-Fi drivers, or bit-bang GPIOs — containers aren't helping. In these cases, you need full access to the hardware.

### Impossible to roll back changes

Surprisingly, in 2026, most Linux distributions still don't allow you to simply roll back changes and revert the system to its default state. The only reliable method that remains is to reinstall the entire system from scratch — which requires a separate computer to write an image to an SD card.

### Multiple SD cards

![](https://blog.flipper.net/content/images/2026/08/raspberry_pi_with_multiple_sd_cards.jpg)

My personal Raspberry Pi travel kit. The easiest approach is to have several SD cards with different operating systems for different tasks

The simplest approach remains having multiple SD cards and swapping in the specific one needed for a given task. I personally used to travel with my favorite Raspberry Pi — housed in a metal case — along with several labeled SD cards, inserting the appropriate one depending on the task at hand, while backing up the SD card images to my computer before any major system experiments. That is precisely how we came up with the concept for Flipper OS.

Even though we criticize Raspberry Pi quite a bit, we genuinely love and respect the company. Its products inspired ours, and Flipper One itself is a project implementing what we miss in Raspberry Pi SBC's.

# What is Flipper OS?

Flipper OS is not exactly an operating system, but rather a higher-level toolset that enables the centralized management of snapshots for various operating systems from a single device. You can think of it as similar to Docker containers, but without virtualization — offering full access to bare metal.

![](https://blog.flipper.net/content/images/2026/08/flipper_one_multiple_os_profiles.jpg)

Flipper OS will let you create and manage multiple snapshots and profiles at once

Ultimately, we aim to create a tool that hardware hackers can easily use to build their own versatile Linux boxes for various tasks and share the resulting images with the community. We want our developments to be usable not only on Flipper One, but on other platforms, too.

### Screw containers & virtualization

Containers are amazing... for your web application. However, they are completely impractical when you need to work with bare metal — toggling GPIO pins, emulating USB devices, or handling network operations.

Imagine needing to bridge an Ethernet interface with a virtual, emulated USB-to-Ethernet adapter, then modifying the Wi-Fi driver and the adapter's firmware, and finally sniffing CEC messages on the HDMI port. Could you do this inside a Docker container? Probably, but you would spend most of your energy wrestling with container configuration and the networking subsystem — and Docker’s networking subsystem is a beast in itself. That is why containers don't work for tools like the Flipper One; we need a raw operating system and full hardware access — 100% bare metal, 100% hardcore.

## Flipper OS from a user perspective

For the user, Flipper OS should feel as familiar and intuitive as possible. In user space, it should be indistinguishable from a Debian-based operating system so that **all existing online how-to guides written for Debian or Ubuntu work on Flipper One right out of the box.** (Hello to all the fans of NixOS💀).

### Boot Menu & OS Profiles

![](https://blog.flipper.net/content/images/2026/08/flipper_os_boot_menu.png)

Boot Menu in Flipper OS allows user to choose which OS profile to boot

All the magic of Flipper OS should take place on a separate layer within the boot menu, prior to system startup. Immediately after powering on the CPU, user selects a specific boot profile and loads it:

* **Boot Menu** — this is a program that starts immediately after the CPU powers on and displays a list of OS profiles. Several standard, pre-configured system profiles come pre-installed on the device. Once a profile is selected, it begins to load. In the boot menu, the user can see the last use timestamp and perform operations on the profiles, such as resetting to default or cloning.
* **Profile** —an OS profile is an operating system image pre-configured for specific tasks. It has a name — such as 'TV Media Box' — and an icon. Several profiles come pre-installed on the device. Each profile is essentially a separate operatin...