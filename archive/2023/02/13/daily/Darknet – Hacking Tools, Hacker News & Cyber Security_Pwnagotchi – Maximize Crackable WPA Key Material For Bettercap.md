---
title: Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap
url: https://www.darknet.org.uk/2023/02/pwnagotchi-maximize-crackable-wpa-key-material-for-bettercap/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2023-02-13
fetch_date: 2025-10-04T06:27:03.282058
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

[Email](/cdn-cgi/l/email-protection#38074b4d5a525d5b4c05684f56595f574c5b50511d0a08151d0a08755940515551425d1d0a087b4a595b53595a545d1d0a086f68791d0a08735d411d0a0875594c5d4a5159541d0a087e574a1d0a087a5d4c4c5d4a5b59481e5a575c4105684f56595f574c5b50511d7b0a1d7908514b1d0a0859561d7b0a1d7908790a7b155a594b5d5c1d0a081d0a0a79711d0a0a1d0a08545d4e5d4a595f51565f1d7b0a1d79085a5d4c4c5d4a5b59481d7b0a1d79084c50594c1d0a08545d594a564b1d0a085e4a57551d0a08514c4b1d0a084b4d4a4a574d565c51565f1d0a086f517e511d0a085d564e514a5756555d564c1d0a084c571d0a08555940515551425d1d0a085b4a595b53595a545d1d0a086f68791d0a08535d411d0a0855594c5d4a5159541d0a08514c1d0a085b59484c4d4a5d4b1d087c1d08791d087c1d08796a5d595c1875574a5d18705d4a5d02181d0a08504c4c484b1d0b791d0a7e1d0a7e4f4f4f165c594a53565d4c16574a5f164d531d0a7e0a080a0b1d0a7e080a1d0a7e484f56595f574c5b505115555940515551425d155b4a595b53595a545d154f485915535d411555594c5d4a515954155e574a155a5d4c4c5d4a5b59481d0a7e)

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