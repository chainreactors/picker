---
title: Kali Linux 2024.4 Release (Python 3.12, Goodbye i386, Raspberry Pi Imager & Kali NetHunter)
url: https://www.kali.org/blog/kali-linux-2024-4-release/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-17
fetch_date: 2025-10-06T19:41:10.992190
---

# Kali Linux 2024.4 Release (Python 3.12, Goodbye i386, Raspberry Pi Imager & Kali NetHunter)

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

![](https://www.kali.org/blog/kali-linux-2024-4-release/images/banner-2024.4-release.jpg)
Monday, 16 December 2024

# Kali Linux 2024.4 Release (Python 3.12, Goodbye i386, Raspberry Pi Imager & Kali NetHunter)

Table of Contents

* [A New Python Version: 3.12](#a-new-python-version-312)
* [The End Of The i386 Kernel And Images](#the-end-of-the-i386-kernel-and-images)
* [Deprecations In The SSH Client: DSA keys](#deprecations-in-the-ssh-client-dsa-keys)
* [Raspberry Pi Imager Customizations Support](#raspberry-pi-imager-customizations-support)
  + [How Does It Work?](#how-does-it-work)
  + [Default Settings For Non-Customized Images](#default-settings-for-non-customized-images)
* [GNOME 47](#gnome-47)
* [Kali Forums Refresh](#kali-forums-refresh)
* [New Tools In Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
  + [App](#app)
  + [Store](#store)
  + [Installer](#installer)
  + [Website](#website)
  + [Kernel/Device](#kerneldevice)
  + [Package](#package)
* [Kali NetHunter Pro Updates](#kali-nethunter-pro-updates)
* [Kali ARM SBC Updates](#kali-arm-sbc-updates)
* [Kali Website Updates](#kali-website-updates)
  + [Kali Documentation](#kali-documentation)
  + [Kali Blog Recap](#kali-blog-recap)
* [Community Shout-Outs](#community-shout-outs)
* [Miscellaneous](#miscellaneous)
* [Get Kali Linux 2024.4](#get-kali-linux-20244)

Just before the year starts to wrap up, we are getting the final 2024 release out! This contains a wide range of updates and changes, which are in already in effect, ready for immediate [download](https://www.kali.org/get-kali/), or [updating](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2024.3 release from September](https://www.kali.org/blog/kali-linux-2024-3-release/) is:

* **[Python 3.12](#a-new-python-version-312)** - New default Python version *(Au revoir `pip`, hello [pipx](https://pipx.pypa.io/stable/))*
* **[The End Of The i386 Kernel and Images](#the-end-of-the-i386-kernel-and-images)** - Farewell x86 *(images)*, but not goodbye *(packages)*
* **[Deprecations in the SSH Client: DSA keys](#deprecations-in-the-ssh-client-dsa-keys)** - Reminder about using `ssh1` if required
* **[Raspberry Pi Imager Customizations Support](#raspberry-pi-imager-customizations-support)** - Able to alter settings at write time
* **[GNOME 47](#gnome-47)** - Now able to synchronize your favorite colors
* **[Kali Forums Refresh](#kali-forums-refresh)** - New heart of the community home
* **[Kali NetHunter](#kali-nethunter-updates)** - Updates to the app, kernels, installer, store and website!
* **[New Tools](#new-tools-in-kali)** - 14 new shiny toys added *(and countless updated!)*

---

## A New Python Version: 3.12

**Python 3.12 is now the default Python interpreter**. While it was [released upstream](https://docs.python.org/3/whatsnew/3.12.html) a year ago, it took a bit of time to become the [default in Debian](https://tracker.debian.org/news/1542739/python3-defaults-3122-1-migrated-to-testing/), and then even more time to [make it to Kali Linux](https://pkg.kali.org/news/601805/python3-defaults-3125-1-imported-into-kali-rolling/), but finally it’s here. Every new version of Python brings along some deprecations or subtle changes of behavior, which in turn breaks some Python packages, and we have to investigate and fix all the issues reported by our QA system. Hence the delay.

There is a major change with this new Python version: **installing third-party Python packages via `pip` is now strongly discouraged and disallowed by default**. This change has been coming for a long time, [we wrote about it 18 months ago already](https://www.kali.org/blog/python-externally-managed/), been given little reminders in each release blog post since and we gave another push about it in the [2024.3 release blog post](https://www.kali.org/blog/kali-linux-2024-3-release/). Now it’s finally effective.

`pip` users, fear not! It’s not the end of the world: **there is [pipx](https://pipx.pypa.io/) as a replacement**. On the surface, it provides a similar user experience, but under the hood it overcomes the one outstanding issue with pip: the lack of environment isolation.

**For more details, please check our dedicated documentation page: [Installing Python Applications via pipx](https://www.kali.org/docs/general-use/python3-external-packages/)**. If you still have a hard time running a third-party Python application in Kali, please reach out to us via our [bug tracker](https://bugs.kali.org/).

## The End Of The i386 Kernel And Images

*…but not packages.*

History lesson: `i386` is a 32-bit CPU architecture, maybe more widely known by the name *x86*. It was the CPU architecture of the first generations of Intel Pentium, AMD K6, and Athlon. In short, it was ubiquitous in personal computers back in the 90s. Starting in 2003, a 64-bit version of the x86 architecture appeared, usually named *x86-64* (or `amd64` in Debian-based Linux distributions). It marked the end of the 32-bit x86 CPUs.

Despite being long obsolete, this architecture remained supported in software for years. 2019 was the year when major Linux distributions ([Fedora 31](https://fedoraproject.org/wiki/Changes/Stop_Building_i686_Kernels) & [Ubuntu](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes)) started to drop it. Finally, in [October 2024](https://lists.debian.org/debian-release/2024/10/msg00064.html), Debian stopped building a `i386` kernel (and OS images, as a consequence). Kali Linux, being based on Debian, [follow suit](https://www.kali.org/blog/end-of-i386-kernel-and-images/): **images and releases will no longer be created for this platform**.

It’s important to note that this is not an instant death for i386 though. This is not how architectures die. The i386 kernel and images are gone, however ***i386 packages in general are not removed** from the repository*. It means that it’s **still possible to run i386 programs on a 64-bit system**. Either directly via the package manager (APT supports installation of i386 packages on a amd64 system), or via [i386 Docker images](https://hub.docker.com/r/kalilinu...