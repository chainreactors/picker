---
title: Kali Linux 2026.1 Release (2026 Theme & BackTrack Mode)
url: https://www.kali.org/blog/kali-linux-2026-1-release/
source: Kali Linux
date: 2026-03-24
fetch_date: 2026-03-25T04:17:36.689718
---

# Kali Linux 2026.1 Release (2026 Theme & BackTrack Mode)

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

![](https://www.kali.org/blog/kali-linux-2026-1-release/images/banner-2026.1-release.jpg)
Tuesday, 24 March 2026

# Kali Linux 2026.1 Release (2026 Theme & BackTrack Mode)

Table of Contents

* [2026 Theme Refresh](#2026-theme-refresh)
* [BackTrack Mode For Kali-Undercover](#backtrack-mode-for-kali-undercover)
* [Kali’s 13th Birthday Event](#kalis-13th-birthday-event)
* [New Tools in Kali](#new-tools-in-kali)
* [Known Issues](#known-issues)
* [Kali NetHunter Updates](#kali-nethunter-updates)
  + [Kali Blog Recap](#kali-blog-recap)
* [Community Shout-Outs](#community-shout-outs)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Get Kali Linux 2026.1](#get-kali-linux-20261)

New year, new release - Kali 2026.1 is here! There is everything from a fresh coat of paint to a nod to our roots, with normal ongoing improvements.
Building on from [December’s 2025.4](https://www.kali.org/blog/kali-linux-2025-4-release/), the summary of the [changelog](https://bugs.kali.org/changelog_page.php):

* **[2026 Theme Refresh](#2026-theme-refresh)** - Our yearly theme refresh
* **[BackTrack Mode For Kali-Undercover](#backtrack-mode-for-kali-undercover)** - New mode celebrating BackTrack’s 20th anniversary
* **[Kali’s 13th Birthday Event](#kalis-13th-birthday-event)** - A little community event
* **[New Tools](#new-tools-in-kali)** - 8 new programs

---

## 2026 Theme Refresh

As with previous 20xx.1 releases, this major update brings our **annual theme refresh**, a long-standing tradition that keeps the Kali Linux interface as modern and innovative. This year’s release unveils a brand-new theme from the moment you boot. Everything from the **boot menu, installer to the login display, and a fresh set of [desktop wallpapers](https://www.kali.org/wallpapers/)**.

**Boot Animation**

The changes to the boot animation are subtle, but now the **animation is fixed for live images**, where it used to get stuck at the beginning, showing only the tail. It will also restart the loop in case the boot process takes longer, making it look smoother.

[
Your browser does not support the video tag.](videos/kali-boot-splash-animation.mp4)

---

**Boot Menu**

[![Kali 2026 Default Grub Boot Menu](images/kali-grub.png)](https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-grub.png)

---

**Graphical Installer**

[![Kali 2026 Graphical Installer](images/kali-installer.png)](https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-installer.png)

---

**Login**

[![Kali 2026 Default Login](images/kali-login.png)](https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-login.png)

---

**Desktop**

[![Kali 2026 Default Desktop](images/kali-desktop.png)](https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-desktop.png)

---

**Kali Purple Desktop**

[![Kali Purple 2026 Default Desktop](images/kali-desktop-purple.png)](https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-desktop-purple.png)

---

**New Wallpapers**

[![New Kali Wallpapers For 2026](images/kali-wallpapers.jpg)](https://www.kali.org/blog/kali-linux-2026-1-release/images/kali-wallpapers.jpg)

---

## BackTrack Mode For Kali-Undercover

2026 marks **the 20th anniversary of [BackTrack Linux](https://www.backtrack-linux.org/)**, the [predecessor to Kali](https://www.kali.org/docs/introduction/kali-linux-history/). To celebrate this milestone, we wanted to bring back some nostalgia for longtime users of this legendary cybersecurity distribution by adding a “BackTrack mode” to `kali-undercover`. This mode transforms the desktop to recreate the look and feel of BackTrack 5, with the same wallpaper, colors, and window themes.

You can run it directly from the menu or by running `kali-undercover --backtrack` in the terminal. You can switch back to the default Kali desktop (or not) by running it again.

[
Your browser does not support the video tag.](videos/kali-backtrack-mode.mp4)

---

Here is a screenshot of BackTrack 5, so you can compare it with our theme:

[![BackTrack Linux 5r3](images/backtrack5-screenshot.png)](https://www.kali.org/blog/kali-linux-2026-1-release/images/backtrack5-screenshot.png)

## Kali’s 13th Birthday Event

Kali recently had our 13th birthday. To celebrate this, [our discord](https://discord.kali.org/) had a little event and prize give away to mark the occasion.
Shout-out to the people who managed to solve it already:

* @AI Program
* @Arszilla
* @UltraStrawberryDream

Even though the top 3 places and prizes have been claimed, we will keep it open for a little longer.
To help you get started, Kali is always getting [new tools](#new-tools-in-kali), it can take some patience to learn about each of them.

> The Quieter You Become, The More You Are Able To Hear

*Thanks to @BeamOfOldLight and @cr4mb0 from the DAFreqs for creating the puzzles!*

## New Tools in Kali

It would not be a Kali release without some new tools!
Here is a quick rundown of the 8 new tools which have been added *(to the network repositories)*:

* [AdaptixC2](https://www.kali.org/tools/adaptixc2/) - Extensible post-exploitation and adversarial emulation framework
* [Atomic-Operator](https://www.kali.org/tools/atomic-operator/) - Execute Atomic Red Team tests across multiple operating system environments
* [Fluxion](https://www.kali.org/tools/fluxion/) - Security auditing and social-engineering research tool
* [GEF](https://www.kali.org/tools/gef/) - Modern experience for GDB with advanced debugging capabilities
* [MetasploitMCP](https://www.kali.org/tools/metasploitmcp/) - MCP server for Metasploit
* [SSTImap](https://www.kali.org/tools/sstimap/) - Automatic SSTI detection tool with interactive interface
* [WPProbe](https://www.kali.org/tools/wpprobe/) - Fast WordPress plugin enumeration tool
* [XSStrike](https://www.kali.org/tools/xsstrike/) - Advanced XSS scanner

*There have been a total of 25 new packages, 9 removed, and 183 updates. On top of that, we also bump the Kali kernel to 6.18.*

## Known Issues

Bad news for users of the `kali-tools-sdr` metapackage (aka. Software Defined Radio): the GNU Radio ecosystem is not in great shape in this release. Tools like `gr-air-modes` or `gqrx-sdr` are known to be broken. Maybe other relate...