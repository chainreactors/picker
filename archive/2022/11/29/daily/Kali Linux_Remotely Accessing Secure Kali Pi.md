---
title: Remotely Accessing Secure Kali Pi
url: https://www.kali.org/blog/remotely-accessing-secure-kali-raspberry-pi/
source: Kali Linux
date: 2022-11-29
fetch_date: 2025-10-04T00:01:18.162914
---

# Remotely Accessing Secure Kali Pi

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

![](https://www.kali.org/blog/remotely-accessing-secure-kali-raspberry-pi/images/remotely-accessing-secure-kali-pi.jpg)
Monday, 28 November 2022

# Remotely Accessing Secure Kali Pi

Table of Contents

* [Ingredients](#ingredients)
* [Pre-Config Wireless 802.11](#pre-config-wireless-80211)
  + [Overview](#overview)
  + [Interface Name](#interface-name)
  + [Wi-Fi Modules](#wi-fi-modules)
  + [Wi-Fi Firmware](#wi-fi-firmware)
  + [Binaries](#binaries)
* [Change The Hostname](#change-the-hostname)
* [Wi-Fi Connection](#wi-fi-connection)
  + [Client Mode](#client-mode)
    - [Static IP](#static-ip)
  + [Access Point Mode](#access-point-mode)
* [Wired Connection](#wired-connection)
  + [Static IP](#static-ip-1)
* [VPN Tunnel](#vpn-tunnel)
* [Summary](#summary)
  + [Food for Thought](#food-for-thought)
* [Additional Resources](#additional-resources)

In [Secure Kali Pi (2022)](https://www.kali.org/blog/secure-kali-raspberry-pi/), the first blog post in the Raspberry Pi series, we set up a [Raspberry Pi 4](https://www.kali.org/docs/arm/raspberry-pi-4/) with full disk encryption. We mentioned that we can leave it somewhere as a drop box. This brought up the question, “**If it is not on my local network how do I connect to it to unlock it?**” So we will now answer this by showing a few different ways to connect to our secure Kali Pi drop box. This includes:

* [Wireless 802.11](#pre-config-wireless-80211):
  + As a [client on an existing network(s)](#client-mode) *(only if we know any details ahead of time to pre-configure)*
  + Create an [access point](#access-point-mode), to become a new network *(that we can access if we are in physical distance to the device)*
* [Wired ethernet](#wired-connection):
  + Using static network settings *(if we know the details ahead of time to pre-configure it)*
  + DHCP to automatically discover network values *(which creates noise)*

After getting internet access, we will use a **[Virtual Private Network](#vpn-tunnel)** to remotely connect back to a server of our choosing, which we can also join from anywhere online, thus getting around the requirements of having to port forward on any firewalls.

---

## Ingredients

* [ ]  Drop box - Raspberry Pi 4
  + *Pre-configured as of our [Secure Kali Pi](https://www.kali.org/blog/secure-kali-raspberry-pi/) blog post*
* [ ]  Wi-Fi - We will be using the on-board wireless adapter (to make the device as compact as possible for our drop box)
  + However if the performance is not sufficient for your needs, an external compatible wireless adapter may give greater range
* [ ]  External server - A pre-created & harden OpenVPN service
  + *Creating this is out-of-scope for this blog post*

---

## Pre-Config Wireless 802.11

### Overview

While wired networking in the initramfs does not require a lot of extras, wireless has a few more moving parts.
To enable wireless support, we need to find:

* The kernel [Wi-Fi **modules**](#wi-fi-modules) that need to be in the initramfs *(Depends on hardware)*
* The [Wi-Fi **firmware**](#wi-fi-firmware) files that need to be in the initramfs *(Depends on hardware)*
* The [Wireless **interface name**](#interface-name) *(Kali defaults to: `wlan0`)*
* [Additional packages](#binaries) to increase functionally. Either:
  + [wpa\_supplicant](https://w1.fi/wpa_supplicant/) to connect as a client to a wireless network
  + [hostapd](https://w1.fi/hostapd/) to create an access point for a new wireless network

Additionally, knowing the **[hostname](#change-the-hostname)** of your Raspberry Pi can help find it, as well as blend in, in your target environment.

---

### Interface Name

First, we need to know what our wireless interface is called.

In Kali we **disable** predictable interface names by default, so the first wireless device will be `wlan0`.

As long as there is no other hardware plugged into the Raspberry Pi at this stage, it should stand out:

```
kali@kalipi:~$ ip a
: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether dc:a6:32:b0:07:ca brd ff:ff:ff:ff:ff:ff
    inet 192.168.42.19/24 brd 192.168.42.255 scope global dynamic eth0
       valid_lft 63997sec preferred_lft 63997sec
    inet6 fe80::dea6:32ff:feb0:7ca/64 scope link
       valid_lft forever preferred_lft forever
3: wlan0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether 2a:54:d3:ee:62:95 brd ff:ff:ff:ff:ff:ff permaddr dc:a6:32:b0:07:cb
```

---

### Wi-Fi Modules

We are now going to discover what modules are needed in order for our wireless device to come up.

On most ARM systems, the wireless device is typically connected via SDIO, and unfortunately we do not have a command like [lspci](https://manpages.debian.org/testing/pciutils/lspci.8.en.html) to list any devices on the SDIO bus, but we can use [dmesg](https://manpages.debian.org/testing/util-linux/dmesg.1.en.html) and [grep](https://manpages.debian.org/testing/grep/grep.1.en.html) to look:

```
kali@kalipi:~$ dmesg | grep wlan
kali@kalipi:~$
```

Since we were returned directly to the prompt, this means that “wlan” is not found in the dmesg output. As we mention in the Kali [Raspberry Pi 4 documentation](https://www.kali.org/docs/arm/raspberry-pi-4/) we use the [nexmon](https://github.com/seemoo-lab/nexmon) firmware for the Raspberry Pi devices, so lets try searching for that instead:

```
kali@kalipi:~$ dmesg | grep nexmon
[    5.070542] brcmfmac: brcmf_c_preinit_dcmds: Firmware: BCM4345/6 wl0: Oct  3 2021 18:14:30 version 7.45.206 (nexmon.org: 2.2.2-343-ge3c8-dirty-5) FWID 01-88ee44ea
```

As we can see in the output above, `brcmfmac` is the driver that is giving us the message. There is a handy command that comes from the [kmod](https://pkg.kali.org/pkg/kmod) package, called [modinfo](https://manpages.debian.org/testing/kmod/modinfo.8.en.html) which...