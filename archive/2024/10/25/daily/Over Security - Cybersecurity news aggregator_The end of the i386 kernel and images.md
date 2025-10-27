---
title: The end of the i386 kernel and images
url: https://www.kali.org/blog/end-of-i386-kernel-and-images/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-25
fetch_date: 2025-10-06T18:55:24.231845
---

# The end of the i386 kernel and images

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/end-of-i386-kernel-and-images/images/banner-end-of-i386.jpg)
Tuesday, 22 October 2024

# The end of the i386 kernel and images

Table of Contents

* [Some terminology first](#some-terminology-first)
* [What’s changing](#whats-changing)
* [Background and context, for the curious](#background-and-context-for-the-curious)

The `i386` architecture has long been obsolete, and from this week, support for i386 in Kali Linux is going to shrink significantly: i386 kernel and images are going away. Images and releases will no longer be created for this platform.

## Some terminology first

Let’s start with the terms used in Kali Linux to talk about CPU architectures. These terms apply more generally to any Debian-based Linux distribution.

* `amd64` refers to the [x86-64](https://en.wikipedia.org/wiki/X86-64) architecture, ie. the *64-bit version of the x86 instruction set*.
* `i386` refers to the [x86](https://en.wikipedia.org/wiki/X86) architecture, ie. the *original 32-bit x86 architecture*.

## What’s changing

First, the **Linux kernel**: starting version 6.11 (that just landed in Kali rolling), the kernel is no longer built for the i386 architecture.

Second, and as a direct consequence: the **Kali Linux images**. We will no longer build the i386 [Installer image](https://www.kali.org/get-kali/#kali-installer-images), the i386 [Live image](https://www.kali.org/get-kali/#kali-live) and the i386 [Pre-Built VM images](https://www.kali.org/get-kali/#kali-virtual-machines). This change impacts the next batch of weekly images (*2024-W44*, due next Monday) and the next Kali Linux release (*2024.4*, due before end of year).

However, *i386 packages in general are not removed from the repository*, therefore it’s still possible to run i386 programs on a 64-bit system. One can use `dpkg --add-architecture i386` in order to then install i386 packages on their system via the package manager. Running i386 binaries on a 64-bit system is a standard scenario and is very well supported. Alternatively, we also provide [i386 Docker images](https://hub.docker.com/r/kalilinux/kali-rolling/tags).

If you’re impacted by this change and need more guidance to run your i386 binaries on Kali Linux, please reach out to us via our [bug tracker](https://bugs.kali.org/), we’ll do our best to help.

## Background and context, for the curious

Kali Linux can run on a variety of CPU architectures, *amd64* being by far the most popular. It’s the architecture of choice for Intel and AMD CPUs that equip personal computers (workstations and laptops alike) and servers. In short, it’s ubiquitous for personal computing. Kali can also run on *i386* CPUs. *i386* is the ancestor of *amd64*, and it was used in personal computers, back in the days before the 64-bit x86 architecture took over and replaced it.

Note that the first *amd64* processor was released in 2003, and the first Debian release to support it was “4.0 Etch”, back in 2007. Also worth noting, the last *i386* CPU produced seem to have been some models of the Intel Pentium 4, and were discontinued in 2007. So, this is a change a long time coming.

Now that we’ve established a rough timeline for the hardware, what about software? Of course, support in software, in particular in the Linux kernel, has to last many years after the hardware is discontinued. But with times, there’s less and less i386 CPUs out there, and less and less effort is made to maintain i386-specific code, so it slowly dies.

In Linux distributions, support for i386 has declined steadily over the years. In 2017, [Arch Linux phased out 32-bit ISOs](https://archlinux.org/news/phasing-out-i686-support/). Then the big year was 2019, with [Fedora 31 dropping i386 kernel and images](https://fedoramagazine.org/in-fedora-31-32-bit-i686-is-86ed/), and [Ubuntu 19.10 doing the same](https://ubuntu.com/blog/statement-on-32-bit-i386-packages-for-ubuntu-19-10-and-20-04-lts).

By the end of 2023, Debian agreed that it would [drop i386 kernel and images](https://www.theregister.com/2023/12/19/debian_to_drop_x86_32/). It finally came into effect a few weeks ago, in September, when the Debian kernel team announced they would [stop building i386 kernel packages](https://lists.debian.org/debian-release/2024/09/msg00220.html). Then the 6.11 kernel was uploaded to Debian beginning of October, [without i386 kernel package](https://lists.debian.org/debian-release/2024/10/msg00064.html). It also means the end of i386 installer images.

Kali Linux is based on Debian, so it follows that Kali Linux also drops i386 kernel and images. This is going to be effective for weekly images starting 2024-W44, to be published on Monday 28th of October. It’s already effective for Kali rolling users.

What about packages, you may ask? i386 packages remain, as long as they can be rebuilt. Which means, as long as there are people to maintain it and fix i386-specific issues as they arise. One of the biggest area that keeps i386 alive is gaming: old games that were compiled for 32-bits x86 are still around, and enjoyed by gamers. Thanks to that, we can hope that a baseline of packages will remain for i386 for the time coming. And at the same time, we can expect other areas and ecosystems to drop i386 support as they see fit, to reduce maintenance efforts. So the overall number of i386 packages will slowly go down over the years, that’s for sure.

Table of Contents

* [Some terminology first](#some-terminology-first)
* [What’s changing](#whats-changing)
* [Background and context, for the curious](#background-and-context-for-the-curious)

LIGHT
[ ] DARK

#### Links

[Home](https://www.kali.org/)
[Download / Get Kali](https://www.kali.org/get-kali/)
[Blog](https://www.kali.org/blog/)
[OS Documentation](https://www.kali.org/docs/)
[Tool Documentation](https://www.kali.org/tools/)
[System Status](https://status.kali.org/)
[Archived Releases](https://old.kali.org/)
[Partnerships](https://www.kali.org/partnerships/)

#### Platforms

[ARM (SBC)](https://arm.kali.org/)
[NetHunter (Mobile)](https://nethunter.kali.org/)
[Amazon AWS](https://aws.amazon.com/marketplace/pp/B08LL91KKB "Amazon AWS")[Docker](https://hub.docker.com/u/kal...