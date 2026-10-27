---
title: Kali Linux 2026.3 Release (Build-Scripts Refresh)
url: https://www.kali.org/blog/kali-linux-2026-3-release/
source: Kali Linux
date: 2026-10-26
fetch_date: 2026-10-27T07:05:42.671248
---

# Kali Linux 2026.3 Release (Build-Scripts Refresh)

[![](https://www.kali.org/images/kali-halloween.png "Trick or treat! 🎃")](https://www.kali.org/)

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

![](https://www.kali.org/blog/kali-linux-2026-3-release/images/banner-2026.3-release.jpg)
Monday, 26 October 2026

# Kali Linux 2026.3 Release (Build-Scripts Refresh)

Table of Contents

* [Build-Scripts Refresh](#build-scripts-refresh)
  + [Quick Example: kali-installer](#quick-example-kali-installer)
  + [What’s Next?](#whats-next)
* [Desktop Updates](#desktop-updates)
  + [KDE Plasma 6.7](#kde-plasma-67)
  + [New Icons](#new-icons)
* [New Tools in Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
  + [Wardriving On Your Wrist](#wardriving-on-your-wrist)
  + [WearHunter](#wearhunter)
  + [NFC Arsenal](#nfc-arsenal)
  + [KernelSU](#kernelsu)
  + [When Hacking Meets Tuners](#when-hacking-meets-tuners)
  + [Misc](#misc)
  + [New Kernels](#new-kernels)
* [Kali Website Updates](#kali-website-updates)
  + [Kali Documentation](#kali-documentation)
* [Community Shout-Outs](#community-shout-outs)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Get Kali Linux 2026.3](#get-kali-linux-20263)

We are back with **Kali Linux 2026.3**, the third [release](https://www.kali.org/releases/) of the year! We have been busy making it easier to build Kali, updating the desktop experience, and bringing in more tools for you.
Ready to get your hands on it? Head over to the [download page](https://www.kali.org/get-kali/), or [upgrade your existing installation](https://www.kali.org/docs/general-use/updating-kali/) to get started.

Here is what has changed since the [2026.2 release from June](https://www.kali.org/blog/kali-linux-2026-2-release/):

* **[Build-Scripts Refresh](#build-scripts-refresh)** - Building Kali has never been so easy
* **[Desktop Updates](#desktop-updates)** - KDE Plasma & New Icons
* **[New Tools](#new-tools-in-kali)** - As always, we have added various new tools

---

## Build-Scripts Refresh

*Back in [Kali 2026.2](https://www.kali.org/blog/kali-linux-2026-2-release/), we gave a sneak peek that we were working on our build-scripts. Well, here it is!*

We have **always made our [build-scripts public](https://gitlab.com/kalilinux/build-scripts)**.
These are the same scripts **we use to generate every official Kali image** available from [kali.org/get-kali](https://www.kali.org/get-kali/).
Building your own Kali image may sound *scary*, but it is not as hard as it looks *(see the [quick example](#quick-example-kali-installer) below)*.

We’ve brought **consistency** to our build-scripts across platforms.
Each one now has the **same features**, **command-line arguments**, **structure and layout** *(where possible)*, and the **same look and feel**.

Would you rather **build inside a container**? That is now supported, with both **Docker** and **Podman**!
Each refreshed build-script comes with `build-in-container.sh`, which detects which container engine you have, creates the build container, and then runs the build from within it. Previously, we had recommended building Kali on Kali, *which caused a bit of a chicken-and-egg problem*.
We have also improved the documentation for **building Kali on Debian-based systems**.

These changes are still underway.
We are sorry for any CI pipelines or workflows we have broken along the way.
Hopefully, the breakage is now behind us.

### Quick Example: kali-installer

Let’s build our own [Kali installer image](https://www.kali.org/docs/installation/), the same one you would download from us.

First, install git and clone the repository:

```
$ sudo apt install git ca-certificates
$ git clone https://gitlab.com/kalilinux/build-scripts/kali-installer.git
$ cd ./kali-installer/
```

To build straight from your machine, install the build dependencies, then run `build.sh`.
The default options will build a [Kali rolling](https://www.kali.org/docs/general-use/kali-branches/) image for the AMD64 architecture:

```
$ sudo apt install simple-cdd debian-cd cpio mtools dosfstools xorriso
$ sudo ./build.sh
┏━━(Kali Installer image)
┃  * Building a Kali Linux Installer image for amd64 architecture
┃ # System:
┃  * Build environment is host (bare metal)
┃  * Host architecture is amd64
┃ # Build:
┃  * Branch              : kali-rolling
┃  * Build mirror        : http://http.kali.org/kali/
┃  * Keep temporary files: false
┃  * Output              : /home/kali/kali-installer/output/kali-linux-rolling-installer-amd64.iso
┃  * Variant             : default
┃  * Version             : rolling
┃ # Installer:
┃  * Additional packages :
┃  * Hostname            : kali
┃ # Proxy configuration:
┃  * No apt caching proxy detected
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[...]
```

---

Rather not install the dependencies on your machine? Build from within a container instead:

```
$ sudo apt install podman
$ sudo ./build-in-container.sh
```

---

Want something other than the default? Change the hostname, add extra packages, or pick a different variant, [branch](https://www.kali.org/docs/general-use/kali-branches/) or architecture:

```
$ sudo ./build.sh --hostname haxbox --packages rustscan
$ sudo ./build.sh --branch kali-dev --variant netinst --arch arm64
```

To see every option, use `./build.sh --help`, or check out the [README](https://gitlab.com/kalilinux/build-scripts/kali-installer/-/blob/main/README.md).
Want to customize the installer even further? Have a look at [preseeding](https://www.kali.org/docs/general-use/kali-preseeding/) *(we will get to this later!)*.

### What’s Next?

We had hoped to refresh every build-script in time for this release, but we didn’t quite make it.
We are aiming to have them ready for Kali 2026.4.

This marks the first milestone of **refreshing the build-scripts**. Next, we will look at **automating builds and workflows**. Finally, we will demonstrate different **setups and customization options**. *Crawl, walk, run.*

## Desktop Updates

### KDE Plasma 6.7

KDE Plasma has been updated to **6.7**, bringing a variety of workflow and performance improvements to the Kali desktop.
One of the most interesting additions is **per-screen virtual desktops**, particularly handy for multi-monitor setups where you may want to keep te...