---
title: Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap
url: https://buaq.net/go-149070.html
source: unSafe.sh - 不安全
date: 2023-02-13
fetch_date: 2025-10-04T06:27:22.048186
---

# Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/bcc4633867c2ca86cb1f320901864637.jpg)

Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap

Views: 51Pwnagotchi is an A2C-based “AI” leveraging bettercap that learns from its surrounding Wi
*2023-2-12 22:34:42
Author: [www.darknet.org.uk(查看原文)](/jump-149070.htm)
阅读量:37
收藏*

---

Pwnagotchi is an A2C-based “AI” leveraging [bettercap](https://www.darknet.org.uk/2016/03/bettercap-modular-portable-mitm-framework/) that learns from its surrounding WiFi environment to maximize crackable WPA key material it captures (either passively, or by performing authentication and association attacks). This material is collected as PCAP files containing any form of handshake supported by [hashcat](https://www.darknet.org.uk/2013/11/hashcat-multi-threaded-password-hash-cracking-tool/), including [PMKIDs](https://www.evilsocket.net/2019/02/13/Pwning-WiFi-networks-with-bettercap-and-the-PMKID-client-less-attack/), full and half WPA handshakes.

![](https://www.darknet.org.uk/wp-content/uploads/2023/02/Pwnagotchi-Maximize-Crackable-WPA-Material-For-Bettercap-640x314.png)

Instead of merely playing Super Mario or Atari games like most reinforcement learning-based “AI” *(yawn)*, Pwnagotchi tunes its own parameters over time to get better at pwning WiFi things in the environments you expose it to.

## How Pwnagotchi works to get Maximize Crackable WPA Key Material For Bettercap

To be more precise, Pwnagotchi is using an LSTM with MLP feature extractor as its policy network for the A2C agent. If you’re unfamiliar with A2C, here is a very good [introductory explanation](https://hackernoon.com/intuitive-rl-intro-to-advantage-actor-critic-a2c-4ff545978752) *(in comic form!)* of the basic principles behind how Pwnagotchi learns. Be sure to check out the [Usage](https://pwnagotchi.ai/usage/#training-the-ai) doc for more pragmatic details of how to help your Pwnagotchi learn as quickly as possible.

Unlike the usual reinforcement learning simulations, Pwnagotchi actually learns at a human timescale because it is interacting with a real-world environment instead of a well-defined virtual environment (like playing Super Mario). Time for a Pwnagotchi is measured in epochs; a single epoch can last anywhere from a few seconds to many minutes, depending on how many access points and client stations are visible.

Multiple units within close physical proximity can “talk” to each other, advertising their presence to each other by broadcasting custom information elements using a parasite protocol I’ve built on top of the existing dot11 standard. Over time, two or more units trained together will learn to cooperate upon detecting each other’s presence by dividing the available channels among them for optimal pwnage.

## Required Hardware

* A [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) *(see [here](https://pwnagotchi.ai/installation/#body-nbsp) for more details on alternative bodies).*
* A [microSD card](https://pwnagotchi.ai/installation/#sd-card) (8GB minimum recommended, preferably of good quality and speed).
* A decent quality micro-USB cord that allows data transfer (not just charging!)
* A portable power bank *(see [here](https://pwnagotchi.ai/installation/#battery) for benchmarks with popular portable batteries).*
* Optional: An [hardware clock](https://pwnagotchi.ai/installation/#hardware-clock) and one of the [supported displays](https://pwnagotchi.ai/installation/#display).

You can download Pwnagotchi here:

[pwnagotchi-raspbian-lite-v1.5.5.zip](https://github.com/evilsocket/pwnagotchi/releases/download/v1.5.5/pwnagotchi-raspbian-lite-v1.5.5.zip)

Or read more [here.](https://github.com/evilsocket/pwnagotchi)

文章来源: https://www.darknet.org.uk/2023/02/pwnagotchi-maximize-crackable-wpa-key-material-for-bettercap/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)