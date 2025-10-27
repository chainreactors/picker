---
title: The Raspberry Pi's Wi-Fi Glow-Up
url: https://www.kali.org/blog/raspberry-pi-wi-fi-glow-up/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-23
fetch_date: 2025-10-06T23:49:24.089479
---

# The Raspberry Pi's Wi-Fi Glow-Up

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

![](https://www.kali.org/blog/raspberry-pi-wi-fi-glow-up/images/banner-raspberry-pi-wi-fi-glow-up.jpg)
Tuesday, 22 July 2025

# The Raspberry Pi's Wi-Fi Glow-Up

Table of Contents

* [Where We Started](#where-we-started)
* [What’s New](#whats-new)
* [Supported Devices](#supported-devices)
* [Installing the Packages](#installing-the-packages)
* [Using Monitor Mode](#using-monitor-mode)
* [Verifying Injection](#verifying-injection)
* [Tips and Troubleshooting](#tips-and-troubleshooting)
* [Special Thanks](#special-thanks)
* [Reporting and Feedback](#reporting-and-feedback)
* [Looking Ahead](#looking-ahead)

*Thanks to Nexmon and fresh Kali packages, on-board wireless is ready for monitor mode and injection (again!).*

[Kali Linux users on Raspberry Pi](https://www.kali.org/get-kali/#kali-arm) now have an improved and more integrated way to use the on-board Wi-Fi interface for wireless assessments. While the Nexmon project has long made this technically possible, our support in Kali has recently been refined.

In [Kali 2025.1](https://www.kali.org/blog/kali-linux-2025-1-release/), with the move to a newer Raspberry Pi kernel and a chance to revisit our packaging, we have cleaned up and formalized support for Nexmon through new packages. This not only improves the setup experience and adds support for more devices, including the Raspberry Pi 5, but also makes it easier to enable other hardware supported by Nexmon within Kali.

## Where We Started

The Raspberry Pi has always been a compelling platform for portable Kali setups. But when it came to wireless assessments, things were less ideal. Raspberry Pi models use Broadcom/Cypress Wi-Fi chipsets, which don’t support monitor mode or injection by default. That left users needing an external USB adapter.

The [Nexmon](https://github.com/seemoo-lab/nexmon) project, created by [SEEMOO Lab at TU Darmstadt](https://www.seemoo.tu-darmstadt.de/), changed that by offering a firmware patching framework that extends Broadcom’s closed firmware with additional capabilities — notably, monitor mode and injection. Nexmon works by modifying the firmware binaries themselves and providing patches for the Linux driver (`brcmfmac`) to support the required modes.

Kali’s integration of Nexmon has come a long way, though it hasn’t always been smooth. We were on the 5.15 kernel series for quite some time, in part due to how we were packaging the kernel and managing patchsets. This made it difficult to support newer devices like the Raspberry Pi 5, which requires a more recent kernel. When we attempted to move to 6.6, we encountered stability issues. These were not caused by Nexmon itself, but by changes in the kernel and how they interacted with our setup. Rather than ship something unreliable, we decided to pause development until we could revisit the approach.

## What’s New

With the switch to the 6.12 kernel, we’ve taken the time to rebuild things properly. We’ve released two new packages:

* [`brcmfmac-nexmon-dkms`](https://pkg.kali.org/pkg/brcmfmac-nexmon-dkms): A DKMS-based version of the `brcmfmac` driver with Nexmon patches
* [`firmware-nexmon`](https://pkg.kali.org/pkg/firmware-nexmon): Nexmon-patched firmware for supported Broadcom chips

These packages make it possible to use the on-board Wi-Fi interface on **supported Raspberry Pi boards for monitor mode and frame injection, no USB adapter required**!

The DKMS driver rebuilds against your kernel on installation, which should help keep things working across updates.

## Supported Devices

We’ve tested the new Nexmon-enabled packages on:

* Raspberry Pi 5 (64-bit)
* Raspberry Pi 4 (64-bit and 32-bit)
* Raspberry Pi 3B (64-bit and 32-bit)
* Raspberry Pi Zero 2 W (43436s variant)
* Raspberry Pi Zero W

**If your board has a compatible Broadcom Wi-Fi chipset, it may work as well. *If it does, let us know!***

## Installing the Packages

On a Raspberry Pi Kali image:

```
$ sudo apt update
$ sudo apt full-upgrade -y
$ sudo apt install -y brcmfmac-nexmon-dkms firmware-nexmon
$ sudo reboot
```

---

Once the device is back up, you can check that the Nexmon-patched driver is in use with:

```
$ modinfo brcmfmac | grep filename
```

## Using Monitor Mode

```
$ airmon-ng start wlan0
```

---

In the command output you may see a message similar to:

```
command failed: Unknown error 524 (-524)
```

This is expected. Despite the message, monitor mode usually works. Confirm with:

```
$ iw dev
```

You should see an interface like `wlan0mon` in monitor mode.

## Verifying Injection

Test injection with:

```
$ sudo aireplay-ng --test wlan0mon
```

You should see the `Injection is working!` message. This is not always stable however, and depends on device.

## Tips and Troubleshooting

* Disable power management: `sudo iwconfig wlan0 power off`
* Stop NetworkManager if needed: `sudo systemctl stop NetworkManager`
* Confirm firmware loads: `dmesg | grep brcmfmac`
* If you need to rebuild the driver, re-run: `sudo dpkg-reconfigure brcmfmac-nexmon-dkms`

---

If upgrading on the Raspberry Pi 3B (64-bit), Wi-Fi may stop working due to the `clm_blob`. You can verify if this is the issue by running:

```
$ dmesg | grep clm_blob
```

If you see it failing to load the `clm_blob`, run `sudo rm -v /lib/firmware/brcm/brcmfmac43430-sdio.raspberrypi,3-model-b.clm_blob` and then reboot.

## Special Thanks

We want to give a couple of shout outs to our friends in the community who helped make this possible:

* [@GeneErik](https://github.com/geneerik) for discussing the pain points of working with Nexmon at a distro level, and he said it would be great if we could use DKMS with the driver. Additionally, many long nights of discussions and troubleshooting.
* [@NurseJackass](https://gitlab.com/nursejackass) contributed the initial support for supporting the 6.12 kernel.
* [The Raspberry Pi Foundation](https://www.raspberrypi.com/) for hardware donations, permissions, and assistance as needed.

## Reporting and Feedback

If:

* It works on your board (especially if unlisted), let us know!
* It doesn’t work, [report](https://bugs.kali.org/bug_report_page.php) the issue with logs and hardware details!
* You get it working on an unsup...