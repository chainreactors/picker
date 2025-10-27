---
title: Kali Linux (is) Everywhere!
url: https://www.kali.org/blog/kali-linux-is-everywhere/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-12
fetch_date: 2025-10-04T03:40:39.435316
---

# Kali Linux (is) Everywhere!

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

![](https://www.kali.org/blog/kali-linux-is-everywhere/images/kali-everywhere-banner.jpg)
Wednesday, 11 January 2023

# Kali Linux (is) Everywhere!

Table of Contents

* [Platform Overview](#platform-overview)
* [What should I use?](#what-should-i-use)
* [Pros and Cons](#pros-and-cons)
* [Closing thoughts](#closing-thoughts)

One of the primary goals of Kali Linux is to put the tools you need as close to you as possible. Over the years this has resulted in a number of different ways to get Kali, but not everyone knows about all the options! In this post we are going to do an overview of different options you have for running Kali, and where you can go for more information for each option.

You should keep in mind as we review options what will be best for you, in your specific use case. What do you intend to use Kali for? Where will you be when you need access to Kali? One of the items that is unique to Kali is most instances are actually pretty short lived, and replaced often. For instance, in the penetration testing space it is considered best practice by many to wipe your install and start over with each new customer or assessment. On the other hand, there are instances of Kali that are around for a very long time; for instance, running scanning engines for enterprises.

**You won’t find a singular “right” way to interact with Kali, you have to determine what works best for you. Which is why we provide so many options**. Let’s look at an overview of all of the various ways to get Kali. Should anything seem interesting, the table contains hyperlinks directly to our documentation on a platform where available.

## Platform Overview

Please note that this is the state of Kali Linux at the time of publishing. For a consistently updated table, please check [here](https://www.kali.org/docs/introduction/kali-linux-image-overview/).

| Installations | Virtual Machines | Cloud | Containers | USB | ARM (Single Board Computer) | Mobile |
| --- | --- | --- | --- | --- | --- | --- |
| [Standard Single-boot](https://www.kali.org/docs/installation/hard-disk-install/) | [VirtualBox](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/) | [Amazon AWS](https://www.kali.org/docs/cloud/aws/) | [Docker](https://www.kali.org/docs/containers/using-kali-docker-images/) | Live boot - [Linux](https://www.kali.org/docs/usb/live-usb-install-with-linux/) / [macOS](https://www.kali.org/docs/usb/live-usb-install-with-mac/) / [Windows](https://www.kali.org/docs/usb/live-usb-install-with-windows/) | [Gateworks Newport](https://www.kali.org/docs/arm/gateworks-newport/) / [Gateworks Ventana](https://www.kali.org/docs/arm/gateworks-ventana/) | [Generic NetHunter](https://www.kali.org/docs/nethunter/installing-nethunter/) |
| macOS [Single-Boot](https://www.kali.org/docs/installation/hard-disk-install-on-mac/) / [Dual-boot](https://www.kali.org/docs/installation/dual-boot-kali-with-mac/) | [Import VirtualBox](https://www.kali.org/docs/virtualization/import-premade-virtualbox/) | [Microsoft Azure](https://www.kali.org/docs/cloud/azure/) | [LXC/LXD](https://www.kali.org/docs/containers/kalilinux-lxc-images/) | [Persistence](https://www.kali.org/docs/usb/usb-persistence/) | [Pinebook](https://www.kali.org/docs/arm/pinebook/) / [Pinebook Pro](https://www.kali.org/docs/arm/pinebook-pro/) | [Generic NetHunter Lite](https://www.kali.org/docs/nethunter/#10-nethunter-editions) |
| [Dual-booting Linux](https://www.kali.org/docs/installation/dual-boot-kali-with-linux/) | [VMware](https://www.kali.org/docs/virtualization/install-vmware-guest-vm/) | [Digital Ocean](https://www.kali.org/docs/cloud/digitalocean/) | [Podman](https://www.kali.org/docs/containers/using-kali-podman-images/) | [Encrypted Persistence](https://www.kali.org/docs/usb/usb-persistence-encryption/) | [Raspberry Pi 1 (Original)](https://www.kali.org/docs/arm/raspberry-pi/) / [2 (1.1)](https://www.kali.org/docs/arm/raspberry-pi-2/) / [3](https://www.kali.org/docs/arm/raspberry-pi-3/) / [4](https://www.kali.org/docs/arm/raspberry-pi-4/) / [400](https://www.kali.org/docs/arm/raspberry-pi-400/) | [Generic NetHunter Rootless](https://www.kali.org/docs/nethunter/nethunter-rootless/) |
| [Dual-booting Windows](https://www.kali.org/docs/installation/dual-boot-kali-with-windows/) | [Import VMware](https://www.kali.org/docs/virtualization/import-premade-vmware/) | [Linode](https://www.kali.org/docs/cloud/linode/) | [Proxmox](https://www.kali.org/docs/virtualization/install-proxmox-guest-vm/#kali-as-a-proxmox-ct-containerization) |  | [Raspberry Pi Zero](https://www.kali.org/docs/arm/raspberry-pi-zero/) / [Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w/) / [Zero 2 W](https://www.kali.org/docs/arm/raspberry-pi-zero-2-w/) |  |
| [Installing directly to USB](https://www.kali.org/docs/usb/usb-standalone-encrypted/) | [Hyper-V](https://www.kali.org/docs/virtualization/install-hyper-v-guest-vm/) |  | [WSL](https://www.kali.org/docs/wsl/wsl-preparations/) |  | [USB Armory MKII](https://www.kali.org/docs/arm/usb-armory-mkii/) | [NetHunter Pro](https://www.kali.org/get-kali/#kali-mobile) |
| [Adding BTRFS snapshots](https://www.kali.org/docs/installation/btrfs/) | [Parallels](https://www.kali.org/docs/virtualization/install-parallels-guest-vm/) |  |  |  |  |  |
| [Over a network (PXE)](https://www.kali.org/docs/installation/network-pxe/) | [Proxmox](https://www.kali.org/docs/virtualization/install-proxmox-guest-vm/) |  |  |  | For more devices, see [here](https://arm.kali.org/) | For more devices, see [here](https://nethunter.kali.org/) |
|  | [QEMU/Libvirt](https://www.kali.org/docs/virtualization/install-qemu-guest-vm/) |  |  |  |  |  |
|  | [UTM](https://www.kali.org/docs/virtualization/install-utm-guest-vm/) |  |  |  |  |  |
|  | [Vagrant](https://www.kali.org/docs/virtualization/install-vagrant-guest-vm/) |  |  |  |  |  |

As we can see, there are a lot of options. This can be quite difficult to look at initially. However, if we keep in mind our needs we can easily figure out what image we want to download or even learn about a new image:

* Are we going to be doing an on-site pentest and need to use a dedicated Kali instance?
* Are we going to want ...