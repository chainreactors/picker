---
title: Kali Linux 2025.2 Release (Kali Menu Refresh, BloodHound CE & CARsenal)
url: https://www.kali.org/blog/kali-linux-2025-2-release/
source: Kali Linux
date: 2025-06-14
fetch_date: 2025-10-06T23:03:45.486516
---

# Kali Linux 2025.2 Release (Kali Menu Refresh, BloodHound CE & CARsenal)

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

![](https://www.kali.org/blog/kali-linux-2025-2-release/images/banner-2025.2-release.jpg)
Friday, 13 June 2025

# Kali Linux 2025.2 Release (Kali Menu Refresh, BloodHound CE & CARsenal)

Table of Contents

* [Desktop Updates](#desktop-updates)
  + [Kali Menu Refresh](#kali-menu-refresh)
  + [GNOME 48](#gnome-48)
    - [New GNOME VPN IP Extension](#new-gnome-vpn-ip-extension)
  + [KDE Plasma 6.3](#kde-plasma-63)
  + [New Community Wallpapers](#new-community-wallpapers)
* [BloodHound Community Edition](#bloodhound-community-edition)
* [New Tools in Kali](#new-tools-in-kali)
  + [Xclip pre-installed](#xclip-pre-installed)
* [Kali NetHunter Updates](#kali-nethunter-updates)
  + [Smartwatch Wi-Fi Injection](#smartwatch-wi-fi-injection)
  + [CARsenal](#carsenal)
  + [Android Radio](#android-radio)
  + [Kali NetHunter Kernels](#kali-nethunter-kernels)
* [Kali ARM SBC Updates](#kali-arm-sbc-updates)
* [Kali Website Updates](#kali-website-updates)
  + [Kali Documentation](#kali-documentation)
  + [Kali Blog Recap](#kali-blog-recap)
* [Kali Team Updates](#kali-team-updates)
* [Community Shout-Outs](#community-shout-outs)
  + [The ROKFOSS initiative, by and for Korean users](#the-rokfoss-initiative-by-and-for-korean-users)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Miscellaneous](#miscellaneous)
* [Get Kali Linux 2025.2](#get-kali-linux-20252)

We’re almost half way through 2025 already, and we’ve got a lot to share with you in this release, **Kali 2025.2**.

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2025.1 release from March](https://www.kali.org/blog/kali-linux-2025-1-release/) is:

* **[Desktop Updates](#desktop-updates)** - Kali-Menu refresh, GNOME 48 & KDE 6.3 updates
* **[BloodHound Community Edition](#bloodhound-community-edition)** - Major upgrade with full set of ingestors
* **[Kali NetHunter Smartwatch Wi-Fi Injection](#smartwatch-wi-fi-injection)** - TicWatch Pro 3 now able to de-authenticate and capture WPA2 handshakes
* **[Kali NetHunter CARsenal](#carsenal)** - Car hacking tool set!
* **[New Tools](#new-tools-in-kali)** - 13 new shinny tools added *(and various updates)*

---

## Desktop Updates

### Kali Menu Refresh

We’ve **completely reworked the Kali Menu**! It’s now reorganized to follow the **[MITRE ATT&CK framework](https://attack.mitre.org/) structure** – which means that finding the right tool for your task should now be a lot more intuitive for red and blue teams alike.

Previously the Kali menu structure followed what was in BackTrack… which followed WHAX before it. The previous structure was an in-house item, [before MITRE was a thing](https://attack.mitre.org/resources/faq/).
When our menu was first created, there wasn’t as much design planning done, which we suffered for later. It meant that over time, scaling and adding new tools became difficult for us.
The knock on effect was that this made it harder for you, the end-users, to discover new tools as similar tools with overlapping functions were in different places or missing entries.
*Yes, seasoned professionals may not use the menu to start up items, using shortcuts such as `super key` and typing the tool name, or via a terminal window. We see the menu as a way to discover tools*.

The final nail in the coffin in the setup was the fact that it was manually managed. Yes, all those entries were previously created by-hand (which also may explain a few things).
As a result, we had stopped adding new tools to the menu… until now.

Now, we have created a new system and automated many aspects, making it easier for us to manage, and easier for you to discover items. Win win.
Over time, we hope to start to add this to [kali.org/tools/](https://www.kali.org/tools/).

Currently Kali Purple still follows [NIST CSF](https://www.nist.gov/cyberframework) (National Institute of Standards and Technology Critical Infrastructure Cybersecurity), rather than [MITRE D3FEND](https://d3fend.mitre.org/).

This is a big change, and we want your feedback! Think something should be renamed, moved, or see a tool that’s missing? Help us improve the menu by editing the structure directly — it’s all open and managed through a **[simple YAML file](https://gitlab.com/kalilinux/packages/kali-menu/-/blob/kali/master/categories.yaml)**.

[![Kali Menu Refresh in Xfce](images/kali-menu.png)](https://www.kali.org/blog/kali-linux-2025-2-release/images/kali-menu.png)

### GNOME 48

GNOME has been bumped up to version 48, and brings with it:

* **Notification Stacking**
* **Performance Improvements**
* **Dynamic triple buffering**
* **Enhanced Image Viewer**
* **Digital Wellbeing**
* **Preserve Battery Health**
* **HDR (High Dynamic Range) Support**
* **Updated Text Editor**

[![Kali GNOME 48](images/gnome-48.png)](https://www.kali.org/blog/kali-linux-2025-2-release/images/gnome-48.png)

As with previous GNOME updates in Kali, we’ve given all our themes a fresh coat of paint – everything’s been tuned to look sharp and feel smooth. The document reader evince has been replaced with the new papers app. If you’re rocking Kali with GNOME, this update is definitely worth the reboot. Want the full scoop? Check out the [official GNOME 48 release notes](https://release.gnome.org/48/).

#### New GNOME VPN IP Extension

Just like we did for Xfce back in [Kali 2024.1](https://www.kali.org/blog/kali-linux-2024-1-release/#xfce), we’ve now brought the VPN IP indicator to GNOME too!

It shows the IP address of your current VPN connection right in the panel — and with a simple click, it copies it straight to your clipboard. Handy, right?

[![Kali GNOME VPN IP](images/gnome-vpn-extension.png)](https://www.kali.org/blog/kali-linux-2025-2-release/images/gnome-vpn-extension.png)

Huge thanks to [@Sarthak Priyadarshi](https://github.com/sarthakpriyadarshi/) who not only came up with the idea, but also provided all of the coding to make it happen. Community contributions like this make Kali better for everyone!

### KDE Plasma 6.3

KDE Plasma fans, rejoice – we’ve included Plasma 6.3, and it’s packed with polish:

* **Huge overhaul of fractional scaling**
* **Accurate screen colors when using the Night Light**
* **More accurate CPU usag...