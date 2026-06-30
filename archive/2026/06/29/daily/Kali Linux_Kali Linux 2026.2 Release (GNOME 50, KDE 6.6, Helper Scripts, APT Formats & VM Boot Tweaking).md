---
title: Kali Linux 2026.2 Release (GNOME 50, KDE 6.6, Helper Scripts, APT Formats & VM Boot Tweaking)
url: https://www.kali.org/blog/kali-linux-2026-2-release/
source: Kali Linux
date: 2026-06-29
fetch_date: 2026-06-30T06:10:06.219451
---

# Kali Linux 2026.2 Release (GNOME 50, KDE 6.6, Helper Scripts, APT Formats & VM Boot Tweaking)

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

![](https://www.kali.org/blog/kali-linux-2026-2-release/images/banner-2026.2-release.jpg)
Monday, 29 June 2026

# Kali Linux 2026.2 Release (GNOME 50, KDE 6.6, Helper Scripts, APT Formats & VM Boot Tweaking)

Table of Contents

* [Desktop Environments Updates](#desktop-environments-updates)
  + [GNOME 50](#gnome-50)
  + [KDE Plasma 6.6](#kde-plasma-66)
* [Improved Consistency For Services Helper Scripts](#improved-consistency-for-services-helper-scripts)
* [APT Gets A New Sources Format](#apt-gets-a-new-sources-format)
* [No More Graphics Firmware Pre-installed For VM Use-cases](#no-more-graphics-firmware-pre-installed-for-vm-use-cases)
* [Disruptive Package Updates](#disruptive-package-updates)
* [Linux Kernel For This Release: 6.19](#linux-kernel-for-this-release-619)
* [A Sneak Peek: Build Scripts](#a-sneak-peek-build-scripts)
* [New Tools in Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
  + [The Qcacld3.0 Injection Story](#the-qcacld30-injection-story)
  + [Wifite On TV](#wifite-on-tv)
  + [Magisk Standalone Kernel Installer](#magisk-standalone-kernel-installer)
  + [New Kernels](#new-kernels)
  + [[NetHunter Pro](https://www.kali.org/docs/nethunter-pro/)](#nethunter-prodocsnethunter-pro)
  + [NetHunter Podcast Episode 3](#nethunter-podcast-episode-3)
* [Kali Website Updates](#kali-website-updates)
  + [Kali Documentation](#kali-documentation)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Get Kali Linux 2026.2](#get-kali-linux-20262)

It’s the final week of Q2, and Kali Linux 2026.2 is here - right on schedule ;) We have been heads down since our last release, and we are ready to share what we have been working on. This release is a mix of desktop refreshes, infrastructure improvements, and quality-of-life changes that we think you will appreciate.

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2026.1 release from March](https://www.kali.org/blog/kali-linux-2026-1-release/) is:

* **[Desktop Environments](#desktop-environments-updates)** - Bump to GNOME 50 and KDE Plasma 6.6
* **[Helper Scripts Consistency](#improved-consistency-for-services-helper-scripts)** - Consistency to our little launches at starting services
* **[APT Format](#apt-gets-a-new-sources-format)** - Goodbye `sources.list`, hello `sources.list.d/kali.source`
* **[VM Boot Optimisation](#no-more-graphics-firmware-pre-installed-for-vm-use-cases)** - Smaller initrd + faster boot times = happy virtual machine users
* **[Reboot Warning](#disruptive-package-updates)** - Heads-up, `polkit` and `xrdp` upgrades require a system reboot
* **[Kali Kernel Incoming](#linux-kernel-for-this-release-619)** - Staying with 6.19 for now, how to get 7.0 early
* **[Build Scripts Incoming](#a-sneak-peek-build-scripts)** - Heads-up with some changing on the way
* **[New Tools](#new-tools-in-kali)** - As always, various new shiny packages have been added *(9!)*

---

## Desktop Environments Updates

As we do roughly every six months, every other Kali release, our [desktop environments](https://www.kali.org/docs/general-use/switching-desktop-environments/) get a major update. This time it’s for: [GNOME](#gnome-50) and [KDE Plasma](#kde-plasma-6-6). Neither brings sweeping changes, but both have put real effort into **refining performance and usability** across the whole ecosystem.

### GNOME 50

GNOME 50 brings usability and performance improvements across the desktop. The **file manager received significant optimizations**, resulting in faster thumbnail and icon loading, improved responsiveness, and reduced memory usage. The desktop also received new accessibility enhancements through a brand-new preferences window, tweaks to the screen reader, and automatic language switching.

Another addition is **support for document annotations** in the Document Viewer app, making it easier to add text notes and highlights directly to documents.

Here you can read more about all the changes with this new GNOME release: [GNOME 50 release announcement](https://release.gnome.org/50/).

[![Kali + GNOME 50](images/gnome-50.png)](https://www.kali.org/blog/kali-linux-2026-2-release/images/gnome-50.png)

### KDE Plasma 6.6

KDE Plasma 6.6 focuses on improving usability and accessibility while introducing several new features, including a **new on-screen keyboard**, providing a better experience particularly for touch-enabled devices.

The **Spectacle screenshot utility can now recognize and extract text** directly from screenshots, making OCR functionality available from the desktop. Accessibility has also been enhanced with new color-vision support options, improvements to Zoom and Magnifier, support for Slow Keys on Wayland, and adoption of the standardized Reduced Motion setting.

Here you can read more about all the changes with this new Plasma release: [KDE Plasma 6.6 release announcement](https://kde.org/announcements/plasma/6/6.6.0/).

[![Kali + KDE Plasma 6.6](images/kde-6.6.png)](https://www.kali.org/blog/kali-linux-2026-2-release/images/kde-6.6.png)

## Improved Consistency For Services Helper Scripts

To improve consistency across tools that depend on a service, we have updated our helper scripts. Previously, a tool that required a service might only let you start it (with no way to stop) - and the information displayed back was inconsistent (mixture of service status, how to access, default credentials or nothing at all). With this change, multiple packages have been updated to use these new scripts, which now handle the following tasks:

* Manage the service - **start/stop**
* **Check if the service is already running** - avoiding starting it twice
* Show the **service status**
* Show any **[default credentials](https://www.kali.org/docs/introduction/default-credentials/)**
* Show **how to access it** - such as if it’s a web UI, the URL *(and bonus, **automatically open it in the browser**!)*

We also make sure that any Kali packages which include a service use **`<tool>-start`**/**`<tool>-stop`** for their command names.

*Hopefully this makes the little things a little easier.*

[![Kali Services Helper Scripts](images/kali-services.png)](https://www.kali.org/blog/kali-linux-20...