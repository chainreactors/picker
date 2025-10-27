---
title: Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap
url: https://www.darknet.org.uk/2023/02/pwnagotchi-maximize-crackable-wpa-key-material-for-bettercap/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-13
fetch_date: 2025-10-04T06:28:24.293801
---

# Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](data:image/svg+xml...)![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap

February 12, 2023

Views: 6,344

Pwnagotchi is an A2C-based “AI” leveraging [bettercap](https://www.darknet.org.uk/2016/03/bettercap-modular-portable-mitm-framework/) that learns from its surrounding WiFi environment to maximize crackable WPA key material it captures (either passively, or by performing authentication and association attacks). This material is collected as PCAP files containing any form of handshake supported by [hashcat](https://www.darknet.org.uk/2013/11/hashcat-multi-threaded-password-hash-cracking-tool/), including [PMKIDs](https://www.evilsocket.net/2019/02/13/Pwning-WiFi-networks-with-bettercap-and-the-PMKID-client-less-attack/), full and half WPA handshakes.

![](data:image/svg+xml...)![](https://www.darknet.org.uk/wp-content/uploads/2023/02/Pwnagotchi-Maximize-Crackable-WPA-Material-For-Bettercap-640x314.png)

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

## Related Posts:

* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [TREVORspray - Credential Spray Toolkit for Azure,…](https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/)
* [Privacy Implications of Web 3.0 and Darknets](https://www.darknet.org.uk/2023/03/privacy-implications-of-web-3-0-and-darknets/)
* [Emerging Threats ETOpen - Anti-malware IDS/IPS Ruleset](https://www.darknet.org.uk/2016/08/emerging-threats-etopen-anti-malware-idsips-ruleset/)
* [What You Need To Know About KRACK WPA2 Wi-Fi Attack](https://www.darknet.org.uk/2017/10/need-know-krack-wpa2-attack/)
* [airgeddon - Wireless Security Auditing Script](https://www.darknet.org.uk/2018/06/airgeddon-wireless-security-auditing-script/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2023%2F02%2Fpwnagotchi-maximize-crackable-wpa-key-material-for-bettercap%2F)

[Tweet](https://twitter.com/intent/tweet?text=Pwnagotchi+-+Maximize+Crackable+WPA+Key+Material+For+Bettercap&url=https%3A%2F%2Fwww.darknet.org.uk%2F2023%2F02%2Fpwnagotchi-maximize-crackable-wpa-key-material-for-bettercap%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2023%2F02%2Fpwnagotchi-maximize-crackable-wpa-key-material-for-bettercap%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2023%2F02%2Fpwnagotchi-maximize-crackable-wpa-key-material-for-bettercap%2F&text=Pwnagotchi+-+Maximize+Crackable+WPA+Key+Material+For+Bettercap)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2023%2F02%2Fpwnagotchi-maximize-crackable-wpa-key-material-for-bettercap%2F)

[Email](/cdn-cgi/l/email-protection#b18ec2c4d3dbd4d2c58ce1c6dfd0d6dec5d2d9d89483819c948381fcd0c9d8dcd8cbd4948381f2c3d0d2dad0d3ddd4948381e6e1f0948381fad4c8948381fcd0c5d4c3d8d0dd948381f7dec3948381f3d4c5c5d4c3d2d0c197d3ded5c88ce1c6dfd0d6dec5d2d9d894f28394f081d8c2948381d0df94f28394f081f083f29cd3d0c2d4d5948381948383f0f8948383948381ddd4c7d4c3d0d6d8dfd694f28394f081d3d4c5c5d4c3d2d0c194f28394f081c5d9d0c5948381ddd4d0c3dfc2948381d7c3dedc948381d8c5c2948381c2c4c3c3dec4dfd5d8dfd6948381e6d8f7d8948381d4dfc7d8c3dedfdcd4dfc5948381c5de948381dcd0c9d8dcd8cbd4948381d2c3d0d2dad0d3ddd4948381e6e1f0948381dad4c8948381dcd0c5d4c3d8d0dd948381d8c5948381d2d0c1c5c4c3d4c29481f59481f09481f59481f0e3d4d0d591fcdec3d491f9d4c3d48b91948381d9c5c5c1c29482f09483f79483f7c6c6c69fd5d0c3dadfd4c59fdec3d69fc4da9483f7838183829483f781839483f7c1c6dfd0d6dec5d2d9d89cdcd0c9d8dcd8cbd49cd2c3d0d2dad0d3ddd49cc6c1d09cdad4c89cdcd0c5d4c3d8d0dd9cd7dec39cd3d4c5c5d4c3d2d0c19483f7)

Filed Under: [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) Tagged With: [bettercap](https://www.darknet.org.uk/tag/bettercap/), [wifi-hacking](https://www.darknet.org.uk/tag/wifi-hacking/), [wifi-security](https://www.darknet.org.uk/tag/wifi-security/)

## Primary Sidebar

### Search Darknet

Search the site ...

* [Email](https://www.darknet.org.uk/contact-darknet/)
* [Facebook](https://www.facebook.com/darknet.org.uk/)
* [LinkedIn](https://www.linkedin.com/company/25076296/)
* [RSS](https://www.darknet.org.uk/feed/)
* [Twitter](https://x.com/THEdarknet)

**[Advertise on Darknet](https://www.darknet.org.uk/contact-darknet/advertise/)**

### Latest ...