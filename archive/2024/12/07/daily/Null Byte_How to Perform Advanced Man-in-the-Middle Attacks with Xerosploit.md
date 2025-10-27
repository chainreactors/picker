---
title: How to Perform Advanced Man-in-the-Middle Attacks with Xerosploit
url: https://null-byte.wonderhowto.com/how-to/perform-advanced-man-middle-attacks-with-xerosploit-0384705/
source: Null Byte
date: 2024-12-07
fetch_date: 2025-10-06T19:42:50.302905
---

# How to Perform Advanced Man-in-the-Middle Attacks with Xerosploit

![Header Banner](https://assets.content.technologyadvice.com/null_byte_3840x1800_e4f3abce80.webp)

[![Null Byte Logo](https://assets.content.technologyadvice.com/Logos_Null_Byte_white_b3593aed94.webp)](https://null-byte.wonderhowto.com/)

Null Byte

[WonderHowTo](https://www.wonderhowto.com/)  [Gadget Hacks](https://www.gadgethacks.com/)  [Next Reality](https://next.reality.news/)  [Null Byte](https://null-byte.wonderhowto.com/)

[![wonderhowto.mark.png](https://assets.content.technologyadvice.com/wonderhowto_mark_facd6be46b.webp)](https://null-byte.wonderhowto.com/)

[Cyber Weapons Lab](https://null-byte.wonderhowto.com/collection/cyber-weapons-lab/)  [Forum](https://null-byte.wonderhowto.com/forum)  [Metasploit Basics](https://null-byte.wonderhowto.com/how-to/metasploit-basics/)  [Facebook Hacks](https://null-byte.wonderhowto.com/how-to/facebook-hacks/)  [Password Cracking](https://null-byte.wonderhowto.com/how-to/password-cracking/)  [Top Wi-Fi Adapters](https://null-byte.wonderhowto.com/how-to/buy-best-wireless-network-adapter-for-wi-fi-hacking-2019-0178550/)  [Wi-Fi Hacking](https://null-byte.wonderhowto.com/how-to/wi-fi-hacking/)  [Linux Basics](https://null-byte.wonderhowto.com/how-to/linux-basics/)  [Mr. Robot Hacks](https://null-byte.wonderhowto.com/how-to/mr-robot-hacks/)  [Hack Like a Pro](https://null-byte.wonderhowto.com/how-to/hack-like-a-pro/)  [Forensics](https://null-byte.wonderhowto.com/how-to/forensics/)  [Recon](https://null-byte.wonderhowto.com/how-to/recon/)  [Social Engineering](https://null-byte.wonderhowto.com/how-to/social-engineering/)  [Networking Basics](https://null-byte.wonderhowto.com/how-to/networking-basics/)  [Antivirus Evasion](https://null-byte.wonderhowto.com/how-to/evading-av-software/)  [Spy Tactics](https://null-byte.wonderhowto.com/how-to/spy-tactics/)  [MitM](https://null-byte.wonderhowto.com/how-to/mitm/)  [Advice from a Hacker](https://null-byte.wonderhowto.com/how-to/advice-from-a-hacker/)

[YouTube](https://www.youtube.com/channel/UCgTNupxATBfWmfehv21ym-g/)  [X](https://x.com/NullByte)

Follow Us

Search

  Close Search

Search    Menu

[how to](https://null-byte.wonderhowto.com/how-to/)

# How to Perform Advanced Man-in-the-Middle Attacks with Xerosploit

![](https://assets.content.technologyadvice.com/thumbnail_Logos_Null_Byte_color_light_8d3c214a02.webp)

By [Retia](https://creator.wonderhowto.com/retia/)

Jun 8, 2021, 04:39 PM

Jun 8, 2021, 04:44 PM

[Nmap](https://null-byte.wonderhowto.com/collection/nmap/)[Cyber Weapons Lab](https://null-byte.wonderhowto.com/collection/cyber-weapons-lab/)[MitM](https://null-byte.wonderhowto.com/collection/mitm/)

![Xerodeploit logo in stylized text.](https://assets.content.technologyadvice.com/637587411395252764_6cdb81b0a1.webp)

A man-in-the-middle attack, or [MitM attack](https://null-byte.wonderhowto.com/collection/mitm/), is when a hacker gets on a network and forces all nearby devices to connect to their machine directly. This lets them spy on traffic and even modify certain things. [Bettercap](https://null-byte.wonderhowto.com/how-to/hack-wi-fi-networks-with-bettercap-0194422/) is one tool that can be used for these types of MitM attacks, but Xerosploit can automate high-level functions that would normally take more configuration work in Bettercap.

Xerosploit rides on top of a few other tools, namely, Bettercap and [Nmap](https://null-byte.wonderhowto.com/collection/nmap/), automating them to the extent that you can accomplish these higher-level concepts in just a couple of commands.

However, Xerosploit can be hit or miss, so don't be surprised if some webpages can't be spoofed because the target is using HTTPS or funneling traffic through a VPN. Considering 73% of all websites use HTTPS, you'll only have success manipulating webpages on the remaining 27%, and only if no VPN is being used.

* **Don't Miss: [How to Flip Photos, Change Images & Inject Messages into Friends' Browsers on Your Wi-Fi Network](https://null-byte.wonderhowto.com/how-to/hacking-pranks-flip-photos-change-images-inject-messages-into-friends-browsers-your-wi-fi-network-0180303/)**

Some sites can still be accessed via HTTP because they aren't redirecting insecure requests to HTTPS, and some don't even have secure versions yet. Here is a small sample, but there are many more in that 27%:

* [alternativenation.net](https://alternativenation.net)
* [baidu.com](https://www.baidu.com)
* [bu.edu](https://www.bu.edu)
* [drudgereport.com](https://drudgereport.com)
* [gnu.org](https://www.gnu.org)
* [go.com](https://go.com)
* [icio.us](https://icio.us)
* [myshopify.com](https://myshopify.com)
* [washington.edu](https://www.washington.edu)
* [weevil.info](https://weevil.info)
* [wikidot.com](https://www.wikidot.com)

## What's Needed

We've only tested Xerosploit out on Ubuntu and Kali Linux, but it may work on macOS. However, you can only select between "Ubuntu / Kali Linux / Others" and "Parrot OS" during the installation process.

You'll also need the latest version of [Python](https://null-byte.wonderhowto.com/how-to/python-2-vs-python-3-important-differences-every-hacker-should-know-0302809/) installed on your computer.

## Install Xerosploit

First, install Xerosploit off [GitHub](https://github.com/LionSec/xerosploit) using **git clone**.

```
~$ git clone https://github.com/LionSec/xerosploit

Cloning into 'xerosploit' ...
remote: Enumerating objects: 306, done.
remote: Total 306 (delta 0), reused 0 (delta 0), pack-reused 306
Receiving objects: 100% (306/306), 793.28 KiB | 2.38 MiB/s, done.
Resolving deltas: 100% (68/68), done.
```

Then, change into its directory (**cd**) and start the installer using Python. It will ask you to select your operating system; if using Kali Linux, choose **1** and hit *enter*.

```
~$ cd xerosploit && sudo python install.py

ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                                                              â
â                     Xerosploit Installer                     â
â                                                              â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

[++] Please choose your operating system.

1) Ubuntu / Kali Linux / Others
2) Parrot OS

>>> 1

[++] Insatlling Xerosploit ...
Get:1 http://kali.download/kali kali-rolling inRelease [30.5 kB]
Get:2 http://kali.download/kali kali-rolling/main Sources [14.0 kB]

...

Xerosploit has been successfully installed. Execute 'xerosploit' in your termninal.
```

## Install the Dependencies

For Xerosploit to do its job correctly, you'll need all of the tools that it built its service on top of, including Nmap, hping3, build-essential, ruby-dev, libpcap-dev, and libgmp3-dev. If you're using Kali, you probably already have all of these.

```
~/xerosploit$ sudo apt install nmap hping3 build-essential ruby-dev libpcap-dev libgmp3-dev

Reading package lists ... Done
Building dependency try ... Done
Reading state information ... Done
build-essential is already the newest version (12.9).
build-essential set to manually installed.
hping3 is already the newest version (3.a2.ds2-10).
hping3 set to manually installed.
nmap is already the newest version (7.91+dfsg1-1kali1).
nmap set to manually installed.
ruby-dev is already the newest version (1:2.7+2).
ruby-dev set to manually installed.
libpcap-dev is already the newest version (1.9.1-r0).
libpcap-dev set to manually installed.
libgmp3-dev is already the newest version (2:6.0.0+dfsg-6).
libgmp3-dev set to manually installed.
```

And use Python to install tabulate and terminaltables, which will let Xerosploit display information to you in an easy-to-read way. You likely already have these tools too.

```
~/xerosploit$ su...