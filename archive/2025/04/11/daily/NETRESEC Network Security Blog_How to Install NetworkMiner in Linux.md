---
title: How to Install NetworkMiner in Linux
url: https://www.netresec.com/?page=Blog&month=2025-04&post=How-to-Install-NetworkMiner-in-Linux
source: NETRESEC Network Security Blog
date: 2025-04-11
fetch_date: 2025-10-06T22:05:49.972361
---

# How to Install NetworkMiner in Linux

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Thursday, 10 April 2025 07:30:00 (UTC/GMT)

## [How to Install NetworkMiner in Linux](/?page=Blog&month=2025-04&post=How-to-Install-NetworkMiner-in-Linux)

This guide shows how to install the latest version of [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) in Linux. To install an older NetworkMiner release, prior to version 3.0, please see our [legacy NetworkMiner in Linux guide](https://netresec.com/?b=142AA47).

![NetworkMiner + Linux](https://media.netresec.com/images/NM-Linux_1464x786.webp)

**STEP 1: Install Mono and GTK2**

[Mono](https://www.mono-project.com/) is an open source cross-platform implementation of the .NET framework, it is needed to run NetworkMiner non-Windows machines. GTK2 is not required, but it provides a more consistent look to the user interface.

Ubuntu / Linux Mint / Kali Linux / Raspberry Pi OS:

sudo apt install mono-devel
sudo apt install libgtk2.0-common

Fedora:

sudo yum install mono-devel gtk2

AlmaLinux / RHEL:

sudo dnf install epel-release
sudo dnf install mono-devel gtk2

Arch Linux:

sudo pacman -S mono gtk2

**STEP 2: Install NetworkMiner**

curl -o /tmp/nm.zip https://www.netresec.com/?download=NetworkMiner

sudo unzip /tmp/nm.zip -d /opt/

sudo chmod +x /opt/NetworkMiner\_\*/NetworkMiner.exe

**STEP 3: Run NetworkMiner**

mono /opt/NetworkMiner\_\*/NetworkMiner.exe --noupdatecheck

![NetworkMiner running in Linux](https://media.netresec.com/images/NetworkMiner_3-0_Linux_519x412.webp)

*Image: NetworkMiner running in Linux*

Follow these steps to analyze live network traffic:

* Click File, Receive PCAP over IP [Ctrl+R]
* Click Start Receiving and note the listen TCP port (default is 57012)

Then run this command to sniff network traffic and send a real-time stream of captured packets to NetworkMiner:

sudo tcpdump -U -w - not tcp port 57012 | nc localhost 57012

*Change 57012 in the command above if NetworkMiner is listening on a different TCP port.*

This [PCAP-over-IP](https://netresec.com/?b=228fddf) technique can also be used to read a real-time packet stream from a remote device.
It is also possible to [sniff packets from Mikrotik routers](https://netresec.com/?b=2459ed5) by clicking File, Receive TZSP Stream.

**STEP 4 (optional): Create Shortcut Command**

sudo bash -c 'cat > /usr/local/bin/networkminer' << EOF

#!/usr/bin/env bash

mono $(which /opt/NetworkMiner\*/NetworkMiner.exe | sort -V | tail -1) --noupdatecheck \$@

EOF

sudo chmod +x /usr/local/bin/networkminer

NetworkMiner can now be started like this:

networkminer ~/Downloads/\*.pcap

**Linux Distros with NetworkMiner**

NetworkMiner comes pre-packaged on some Linux distributions, such as [REMnux](https://remnux.org/), [Security Onion Desktop](https://docs.securityonion.net/en/2.4/desktop.html), [CSI Linux](https://csilinux.com/) and [BlackArch](https://www.blackarch.org/).

![NetworkMiner running in REMnux](https://media.netresec.com/images/NetworkMiner-in-REMnux_506x392.webp)

*Image: NetworkMiner running in REMnux*

**Static Download Link**

The https://www.netresec.com/?download=NetworkMiner download link always delivers the latest release of NetworkMiner.
If you prefer a static link, that points to a specific version of NetworkMiner, then please use this one:
https://download.netresec.com/networkminer/NetworkMiner\_3-0.zip

Posted by Erik Hjelmvik on Thursday, 10 April 2025 07:30:00 (UTC/GMT)

Tags:
#[NetworkMiner](/?page=Blog&tag=NetworkMiner)​
#[Linux](/?page=Blog&tag=Linux)​
#[Ubuntu](/?page=Blog&tag=Ubuntu)​
#[Kali](/?page=Blog&tag=Kali)​

Short URL:
<https://netresec.com/?b=2542784>

### Recent Posts

» [Gh0stKCP Protocol](/?page=Blog&month=2025-09&post=Gh0stKCP-Protocol)

» [Define Protocol from Traffic (XenoRAT)](/?page=Blog&month=2025-08&post=Define-Protocol-from-Traffic-XenoRAT)

» [PureRAT = ResolverRAT = PureHVNC](/?page=Blog&month=2025-08&post=PureRAT-ResolverRAT-PureHVNC)

» [PureLogs Forensics](/?page=Blog&month=2025-07&post=PureLogs-Forensics)

» [CapLoader 2.0.1 Released](/?page=Blog&month=2025-07&post=CapLoader-2-0-1-Released)

» [Detecting PureLogs traffic with CapLoader](/?page=Blog&month=2025-06&post=Detecting-PureLogs-traffic-with-CapLoader)

» [CapLoader 2.0 Released](/?page=Blog&month=2025-06&post=CapLoader-2-0-Released)

» [Comparison of tools that extract files from PCAP](/?page=Blog&month=2025-05&post=Comparison-of-tools-that-extract-files-from-PCAP)

### Blog Archive

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)