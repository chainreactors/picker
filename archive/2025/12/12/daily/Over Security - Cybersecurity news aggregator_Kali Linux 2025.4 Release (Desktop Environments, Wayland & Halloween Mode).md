---
title: Kali Linux 2025.4 Release (Desktop Environments, Wayland & Halloween Mode)
url: https://www.kali.org/blog/kali-linux-2025-4-release/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-12
fetch_date: 2025-12-13T03:16:06.633009
---

# Kali Linux 2025.4 Release (Desktop Environments, Wayland & Halloween Mode)

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

![](https://www.kali.org/blog/kali-linux-2025-4-release/images/banner-2025.4-release.jpg)
Friday, 12 December 2025

# Kali Linux 2025.4 Release (Desktop Environments, Wayland & Halloween Mode)

Table of Contents

* [Desktop Environments](#desktop-environments)
  + [GNOME 49](#gnome-49)
  + [KDE Plasma 6.5](#kde-plasma-65)
  + [New Colors for Xfce Desktop](#new-colors-for-xfce-desktop)
* [VM Guest Utils Support For Wayland](#vm-guest-utils-support-for-wayland)
* [Kali Halloween Mode](#kali-halloween-mode)
* [Kali Live image Is Now Distributed Over BitTorrent Only](#kali-live-image-is-now-distributed-over-bittorrent-only)
* [New Tools in Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
* [Kali Documentation](#kali-documentation)
* [Community Shout-Outs](#community-shout-outs)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Miscellaneous](#miscellaneous)
* [Get Kali Linux 2025.4](#get-kali-linux-20254)

Say hello to Kali Linux 2025.4!
Expect updated tools, performance tweaks, and improved support - no fluff, just the essentials.

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2025.3 release from September](https://www.kali.org/blog/kali-linux-2025-3-release/) is:

* **[Desktop Environments](#desktop-environments)** - Changes to all! GNOME, KDE & Xfce
* **[Wayland](#vm-guest-utils-support-for-wayland)** - VM Guest Utils Support
* **[Halloween Mode](#kali-halloween-mode)** - dresses the desktop for the occasion
* **[3 New Tools](#new-tools-in-kali)** - As always, new packages added and upgraded!

---

## Desktop Environments

### GNOME 49

As with previous GNOME updates in Kali, we’ve given all our themes a fresh coat of paint - everything has been tuned to look sharp and feel smooth.

The **Totem video player has been replaced with the new Showtime app**, and the **app grid now finally organizes Kali tools into folders**, just like the menu does, making it far more intuitive to find the tool you need.

[![](images/gnome-kali-tools-app-grid.png)](https://www.kali.org/blog/kali-linux-2025-4-release/images/gnome-kali-tools-app-grid.png)

Another quality-of-life improvement is the addition of a **shortcut to quickly open a terminal** (finally!), using `Ctrl`+`Alt`+`T` or `Win`+`T` - just like in our other desktops.

One of the major changes in GNOME 49 is the removal of X11 session support. **Wayland is now the default - and only - window server**, but do not worry: the transition is seamless and, as we explain later, even VM support is excellent.

If you want to know more about the details of the new shell version, check out the official [GNOME 49 release notes](https://release.gnome.org/49/).

### KDE Plasma 6.5

KDE Plasma desktop has been bumped up to version 6.5, which brings two major releases of the desktop together. Here are some of the most relevant new features:

* More **flexible window tiling**
* **New screenshot tool**, with extra editing features
* Quick access to **pinned clipboard items** in the panel
* **Fuzzy matching support for KRunner** (Plasma’s search/launch/calculator/… tool), which means that even if you misspell an app’s name, it will still find it for you.

If you want to learn more about the new changes for this awesome DE, check out the [Plasma 6.4 announcement](https://kde.org/announcements/plasma/6/6.4.0/) and [Plasma 6.5 announcement](https://kde.org/announcements/plasma/6/6.5.0/).

[![](images/kali-plasma-6.5.png)](https://www.kali.org/blog/kali-linux-2025-4-release/images/kali-plasma-6.5.png)

### New Colors for Xfce Desktop

With this update, we wanted to bring **support for color themes to Xfce**, putting it on par with the already available settings in the other desktops (GNOME and KDE). Now you can fully customize the colors of your Kali installation with the new themes for icons, GTK 3/4 windows, Qt 5/6 windows, and Xfce’s window manager decorations.

[![](images/xfce-themes.png)](https://www.kali.org/blog/kali-linux-2025-4-release/images/xfce-themes.png)

All these settings can be changed through the “Appearance” application, except for Qt programs, which require separate themes and can be tweaked through qt5ct or qt6ct (both installed by default).

[![](images/xfce-themes-settings.png)](https://www.kali.org/blog/kali-linux-2025-4-release/images/xfce-themes-settings.png)

## VM Guest Utils Support For Wayland

[Wayland](https://www.kali.org/docs/general-use/wayland/) is a modern display protocol that serves as the successor to the older X11 system for handling graphics in Linux. It specifies how graphical applications (clients) communicate with a display server to render content and process user input. **For years, X11 has been the default system in most UNIX desktops, but the time has come for a change to more modern software** with a more efficient and secure architecture.

Now that [GNOME has moved to only supporting Wayland](#gnome-49), and KDE in Kali has already used it by default for a few years (since [Kali Linux 2023.1](https://www.kali.org/blog/kali-linux-2023-1-release/)), we wanted to ensure that the transition and experience were seamless. The only thing that we felt was missing was support for [VM guest tools](https://www.kali.org/docs/virtualization/), like clipboard sharing and window scaling, but things have been progressing, and now all the major VM software fully supports Wayland.

We have tested Kali installations with Wayland as the guest OS in [VirtualBox](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/), [VMware](https://www.kali.org/docs/virtualization/install-vmware-guest-vm/), and [QEMU](https://www.kali.org/docs/virtualization/install-qemu-guest-vm/), configured the missing parts, and we are happy to announce that **all of the VM guest additions that you expected in X11 before are now working in Wayland** without trouble.

## Kali Halloween Mode

During last Halloween season, we wanted to celebrate by launching a Kali/Hacker-themed pumpkin carving contest. We also launched a **new mode for `kali-undercover`** called **Halloween mode**, which dresses the desktop for the occasion!

[
Your browser does not support the video tag.](videos/kali-hallo...