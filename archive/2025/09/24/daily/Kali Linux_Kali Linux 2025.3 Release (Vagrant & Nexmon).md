---
title: Kali Linux 2025.3 Release (Vagrant & Nexmon)
url: https://www.kali.org/blog/kali-linux-2025-3-release/
source: Kali Linux
date: 2025-09-24
fetch_date: 2025-10-02T20:36:55.597184
---

# Kali Linux 2025.3 Release (Vagrant & Nexmon)

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

![](https://www.kali.org/blog/kali-linux-2025-3-release/images/banner-2025.3-release.jpg)
Tuesday, 23 September 2025

# Kali Linux 2025.3 Release (Vagrant & Nexmon)

Table of Contents

* [HashiCorp: Packer & Vagrant](#hashicorp-packer--vagrant)
* [Nexmon Support](#nexmon-support)
* [Dropping ARMel](#dropping-armel)
* [Configurable VPN IP panel plugin (Xfce)](#configurable-vpn-ip-panel-plugin-xfce)
* [New Tools in Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
  + [Wireless Injection](#wireless-injection)
  + [CARsenal Update](#carsenal-update)
  + [Modules in Magisk](#modules-in-magisk)
  + [Bugfixes & Improvements](#bugfixes--improvements)
  + [Playground](#playground)
* [Kali ARM SBC Updates](#kali-arm-sbc-updates)
* [Miscellaneous](#miscellaneous)
* [Kali Documentation](#kali-documentation)
* [Kali Blog Recap](#kali-blog-recap)
* [Community Shout-Outs](#community-shout-outs)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Get Kali Linux 2025.3](#get-kali-linux-20253)

Another quarter, another drop - Kali 2025.3 is now here! Bringing you another round of updates, new features and introducing some new tools - pushing Kali further.
The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2025.2 release from June](https://www.kali.org/blog/kali-linux-2025-2-release/) is:

* **[Packer & Vagrant](#hashicorp-packer--vagrant)** - *HashiCorp’s products have had a refresh*
* **[Nexmon Support](#nexmon-support)** - *Monitor mode and injection for Raspberry Pi’s in-built Wi-Fi*
* **[10 New Tools](#new-tools-in-kali)** - *As always, various new packages added (as well as updates)*

---

## HashiCorp: Packer & Vagrant

Kali has been using two HashiCorp products, which go hand-in-hand with each other:

* [**Packer**](https://developer.hashicorp.com/packer) - ***Creating VMs** for multiple platforms from a single source configuration*
* [**Vagrant**](https://developer.hashicorp.com/vagrant) - ***Building and managing** VM environments*

Until now, we have been using our Packer build-script to generate our Vagrant VMs. This has been working well for us.
We wanted to streamline our platform building process more, which prompted us to revisit how we generate Vagrant VMs.
Whilst it is possible to automate Packer, it was not ideal for our infrastructure setup and workflow *(e.g. trying to build Hyper-V images on Linux)*.

This caused us to refresh a few items:

* [Kali **pre-seed examples**](https://gitlab.com/kalilinux/recipes/kali-preseed-examples) - Packer uses pre-seed to automate the Kali installer - we made sure they are **all consistent**.
* [Kali **Packer build-scripts**](https://gitlab.com/kalilinux/build-scripts/kali-packer/-/tree/main) - We were using v1 of the standards. **We upgraded to v2**.
* [Kali **VM build-scripts**](https://gitlab.com/kalilinux/build-scripts/kali-vm) - Vagrant images are VMs which a few tweaks done to them. **We added these modification to our existing VM build-scripts**.

For more information, please keep reading our blog post: [Kali Vagrant Rebuilt: Out With Packer, In With DebOS](https://www.kali.org/blog/kali-vagrant-rebuilt/)

## Nexmon Support

Nexmon is a “patched” firmware, for certain wireless chips, to extend their functionally to allow:

* **Monitor mode** - *able to **sniff packets***
* **Injection mode** - *frame injection allows for **custom raw packets** to be sent, outside of the “standard” stack ordering*

Both are really useful when it comes to information security!
*For the record, it is possible to-do both of the features above without Nexmon, as it depends on the device’s chipset and drivers.*

Now, Nexmon supported wireless chips are Broadcom & Cypress, which are in a various devices, including the Raspberry Pi’s in-built Wi-Fi!
In [Kali 2025.1](https://www.kali.org/blog/kali-linux-2025-1-release/), we changed how we package our Raspberry Pi kernel, as well as bump to a new major version. Now Nexmon support is back as well as supporting Raspberry Pi 5!
***Other devices can also use Nexmon, its not limited to Raspberry Pis.***

To find out more, please see our previous blog post: [The Raspberry Pi’s Wi-Fi Glow-Up](https://www.kali.org/blog/raspberry-pi-wi-fi-glow-up/)

## Dropping ARMel

We are announcing that we too are **dropping support for ARMel** (Acorn RISC Machine, Little-Endian). We are [following Debian’s footsteps in this decision](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1113680): Debian “trixie” 13 is the [last release with ARMel support](https://www.debian.org/releases/trixie/release-notes/issues.en.html#armel-last-release), and Debian testing (which Kali is based on) doesn’t provide ARMel packages anymore.

Luckily, the **[amount of devices](https://arm.kali.org/images.html) which use this architecture is very limited**:

* Raspberry Pi 1 (Original)
* Raspberry Pi Zero W
* *ODROID-W, which already is End-Of-Life*.

We cannot justify the amount of resources, both human power as well as hardware, required to support such a limited amount of legacy hardware. *We would much rather put the time into RISC-V…*

## Configurable VPN IP panel plugin (Xfce)

In [Kali 2024.1](https://www.kali.org/blog/kali-linux-2024-1-release/), we introduced a new Xfce panel plugin that allows users to quickly check and copy the current IP address of their VPN connection. Until now, it was only possible to view the IP of the first VPN, but if you were using multiple connections or wanted to check a different interface, there was no way to switch it. To improve the usability of this plugin, **we have now added the option to choose which network interface the plugin monitors**.

[![](images/xfce-vpn-ip-plugin.png)](https://www.kali.org/blog/kali-linux-2025-3-release/images/xfce-vpn-ip-plugin.png)

To configure it, right-click the VPN-IP plugin and open the preferences dialog, where you can set the new interface at the end of the **“Command”** parameter. If you don’t see the VPN-IP plugin, you can find it in the panel preferences by searching for the **“Generic Monitor”** plugin in the **“Items”** tab.

## New Tools in Kali

It would not be a Kali release if there were not any new tools added! A quic...