---
title: Pwnagotchi – Maximize Crackable WPA Key Material For Bettercap
url: https://www.darknet.org.uk/2023/02/pwnagotchi-maximize-crackable-wpa-key-material-for-bettercap/
source: Instapaper: Unread
date: 2023-02-14
fetch_date: 2025-10-04T06:34:34.298834
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

[Email](/cdn-cgi/l/email-protection#2c135f594e46494f58117c5b424d4b43584f4445091e1c01091e1c614d544541455649091e1c6f5e4d4f474d4e4049091e1c7b7c6d091e1c674955091e1c614d58495e454d40091e1c6a435e091e1c6e495858495e4f4d5c0a4e434855117c5b424d4b43584f4445096f1e096d1c455f091e1c4d42096f1e096d1c6d1e6f014e4d5f4948091e1c091e1e6d65091e1e091e1c40495a495e4d4b45424b096f1e096d1c4e495858495e4f4d5c096f1e096d1c58444d58091e1c40494d5e425f091e1c4a5e4341091e1c45585f091e1c5f595e5e4359424845424b091e1c7b456a45091e1c49425a455e434241494258091e1c5843091e1c414d544541455649091e1c4f5e4d4f474d4e4049091e1c7b7c6d091e1c474955091e1c414d58495e454d40091e1c4558091e1c4f4d5c58595e495f091c68091c6d091c68091c6d7e494d480c61435e490c64495e49160c091e1c4458585c5f091f6d091e6a091e6a5b5b5b02484d5e4742495802435e4b025947091e6a1e1c1e1f091e6a1c1e091e6a5c5b424d4b43584f444501414d544541455649014f5e4d4f474d4e4049015b5c4d0147495501414d58495e454d40014a435e014e495858495e4f4d5c091e6a)

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