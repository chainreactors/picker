---
title: Community Showcase: Raspberry Pi Zero W P4wnP1 A.L.O.A.
url: https://www.kali.org/blog/community-showcase-using-kali-pi-p4wnp1-aloa/
source: Kali Linux
date: 2022-10-14
fetch_date: 2025-10-03T19:52:56.667606
---

# Community Showcase: Raspberry Pi Zero W P4wnP1 A.L.O.A.

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

![](https://www.kali.org/blog/community-showcase-using-kali-pi-p4wnp1-aloa/images/kali-p4wnp1-banner.jpg)
Thursday, 13 October 2022

# Community Showcase: Raspberry Pi Zero W P4wnP1 A.L.O.A.

Table of Contents

* [Shopping List](#shopping-list)
* [Setting Up To Get Down To Business](#setting-up-to-get-down-to-business)
* [Using the P4wnP1 A.L.O.A.](#using-the-p4wnp1-aloa)
  + - [USB Settings](#usb-settings)
    - [Wi-Fi Settings](#wi-fi-settings)
    - [Bluetooth](#bluetooth)
    - [Network Settings](#network-settings)
    - [Trigger Actions](#trigger-actions)
    - [HIDScript](#hidscript)
    - [Event Log](#event-log)
    - [Generic Settings](#generic-settings)
* [Creating our own Trigger](#creating-our-own-trigger)
* [Installing A Package When Connected over SSH](#installing-a-package-when-connected-over-ssh)
* [Credits](#credits)
* [Reminder](#reminder)
* [Other Resources](#other-resources)

The Kali community has been hard at work (as always!), and we want to showcase what we think is a very cool project of Kali Linux on a [Raspberry Pi Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w/), the “**[P4wnP1 A.L.O.A.](https://www.kali.org/docs/arm/raspberry-pi-zero-w-p4wnp1-aloa/)** (**A** **L**ittle **O**ffensive **A**pplication)”.

It takes the standard Kali Linux image and adds custom software and some extra firmware designed for the Raspberry Pi Zero W to turn it into a **Swiss Army knife of attacks and exfiltration**.

This blog post will be a [brief overview](#using-the-p4wnp1-aloa) of how to get started using the web interface, [setting up a trigger](#creating-our-own-trigger) as well as [installing additional packages](#installing-a-package-when-connected-over-ssh) found in Kali Linux.
There is a lot more to P4wnP1 than this blog post goes over, which is why we have included [additional reading material](#other-resources) from the community which cover additional attack scenarios as well as more payloads that people have written if you want to go deeper!

If you have a Raspberry Pi Zero W, we highly recommend giving this image a try.
We see this as a great tool in any tester’s toolkit!

## Shopping List

* [Raspberry Pi Zero W](https://www.kali.org/docs/arm/raspberry-pi-zero-w/) *(**not** Zero 2 W)*
* Raspberry Pi Zero W [USB-A Add-on Board](https://www.makerfocus.com/products/usb-type-a-adapter-board-for-raspberry-pi-zero-w) (optional but recommended)
* MicroUSB to USB-A cable (required if you are not using the above add-on board)
* MicroSD card (32GB or larger)
* [Kali Linux Raspberry Pi Zero W P4wnP1 A.L.O.A.](https://www.kali.org/get-kali/) image

## Setting Up To Get Down To Business

First thing, download the [Kali P4wnP1 A.L.O.A. image](https://www.kali.org/get-kali/#kali-arm).
*At the time of writing, the current version is 2022.3:*

```
kali@kali:~/Downloads$ ls
kali-linux-2022.3-raspberry-pi-zero-w-p4wnp1-aloa-armel.img.xz
```

---

We will verify the download as well, by going back to the download page and clicking on the `sum` link on the **Raspberry Pi Zero W (P4wnP1 A.L.O.A)** line to get the SHA256 checksum:

```
kali@kali:~/Downloads$ echo "210635bb3dc7876b638a7035cd4dc60e0b134b19a6aec42a75f5995036b45840 kali-linux-2022.3-raspberry-pi-zero-w-p4wnp1-aloa-armel.img.xz" | sha256sum -c
kali-linux-2022.3-raspberry-pi-zero-w-p4wnp1-aloa-armel.img.xz: OK
```

---

Now that we have verified that we have downloaded the file and it matches, we write it to the microSD card, which on **our system** is `/dev/sdb` - on **your system this may be different**, **do NOT just copy and paste** what we have put here, because you **WILL** overwrite whatever you have on your system’s `/dev/sdb` if you do.

The `xzcat` command will open the compressed image file and pipe it to the `dd` command, which will do the actual writing to the microSD card. The use of `xzcat` is a quick trick, as it removes having to actually uncompress the image first:

```
kali@kali:~/Downloads$ xzcat kali-linux-2022.3-raspberry-pi-zero-w-p4wnp1-aloa-armel.img.xz | sudo dd of=/dev/sdb bs=1M status=progress
[sudo] password for kali:
6421807104 bytes (6.4 GB, 6.0 GiB) copied, 101 s, 63.6 MB/s
0+577993 records in
0+577993 records out
6442450944 bytes (6.4 GB, 6.0 GiB) copied, 162.961 s, 39.5 MB/s
```

The speeds above are on our system, these will differ based on your system and the speed of the microSD card that you are using.

---

Now that this is done, we can unplug the microSD card from the machine, and plug it in to our Raspberry Pi Zero W.
If you are using a USB-A adapter similar to what we linked to in the “[shopping list](#shopping-list)” section, you can plug it in to your computer to power it on, otherwise power the Raspberry Pi Zero W via the micro port as usual.

Since the first boot of Kali Linux will do things like resize the filesystem, and set up the [default credentials](https://www.kali.org/docs/introduction/default-credentials/) (user: `kali`, password: `kali`) the timing will vary based on microSD card speed.

## Using the P4wnP1 A.L.O.A.

Once it is booted, you will know everything is **ready to go, when you see the default wireless network**: `💥🖥💥 Ⓟ➃ⓌⓃ🅟❶`.
*Handy if you do not have an HDMI monitor plugged in!*

Select the above SSID, and then we login with the **password**: `MaMe82-P4wnP1`.

[![](images/select-network-1.png)](https://www.kali.org/blog/community-showcase-using-kali-pi-p4wnp1-aloa/images/select-network-1.png)

---

Now that we are connected, we should see our wireless device is connected and has an IP address in the `172.24.0.xxx/24` range:

```
kali@kali:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 4096
    link/ether 00:03:7f:12:1f:ae brd ff:ff:ff:ff:ff:ff
    inet 172.24.0.12/24 brd 172.24.0.255 scope global dynamic noprefixroute wlan0
       valid_lft 297sec preferred_lft 297sec
```

We can see that the IP addr...