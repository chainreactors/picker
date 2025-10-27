---
title: I Know Which Device You Used Last Summer Fingerprinting WhatsApp Users’ Devices
url: https://medium.com/@TalBeerySec/i-know-which-device-you-used-last-summer-fingerprinting-whatsapp-users-devices-71b21ac8dc70
source: Instapaper: Unread
date: 2024-10-19
fetch_date: 2025-10-06T18:56:27.459082
---

# I Know Which Device You Used Last Summer Fingerprinting WhatsApp Users’ Devices

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F71b21ac8dc70&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40TalBeerySec%2Fi-know-which-device-you-used-last-summer-fingerprinting-whatsapp-users-devices-71b21ac8dc70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40TalBeerySec%2Fi-know-which-device-you-used-last-summer-fingerprinting-whatsapp-users-devices-71b21ac8dc70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# I Know Which Device You Used Last Summer: Fingerprinting WhatsApp Users’ Devices

[![Tal Be'ery](https://miro.medium.com/v2/resize:fill:64:64/0*xv5INqVj65wt8lER.jpeg)](/%40TalBeerySec?source=post_page---byline--71b21ac8dc70---------------------------------------)

[Tal Be'ery](/%40TalBeerySec?source=post_page---byline--71b21ac8dc70---------------------------------------)

9 min read

·

Oct 15, 2024

--

Listen

Share

**TL;DR: As part of our ongoing security research on Meta’s WhatsApp privacy issues, we found out these issues are worse than previously realized:**

**Not only that WhatsApp leaks user device setup information (number of devices, mobile or not), it leaks additional information about their Operating Systems (Android, iPhone / iOS, Windows, Mac). Such information may allow potential attackers to gather actionable intelligence about their victims.**

Meta’s WhatsApp is the most popular messaging app in the world, with over [five billion downloads](https://www.businessofapps.com/data/messaging-app-market/) and [2.4 billion active users](https://explodingtopics.com/blog/messaging-apps-stats). WhatsApp’s End-to-End Encryption (E2EE) protocol is the cornerstone of protecting its users’ messages’ confidentiality. However, we discovered and published earlier this year that WhatsApp E2EE protocol design suffers from some privacy issues in the Multi Device setting and reveals information on the user devices. Today we show these issue is worse than previously realized and the leaked information may include the devices’ operating system, which can greatly enhance attackers’ reconnaissance phase.

## Reminder: WhatsApp protocol reveals device information

Our inspection of WhatsApp’s End-to-End Encryption (E2EE) protocol for the Multi Device setting, [Signal’s Sesame protocol](https://signal.org/docs/specifications/sesame/) earlier this year, showed it leaks some private information about the users’ device setup.

[## Hi Meta, WhatsApp with privacy?

### TL;DR: Meta’s WhatsApp suffers from a privacy issue that leaks victim devices’ setup information (mobile device + up to…

medium.com](/%40TalBeerySec/hi-meta-whatsapp-with-privacy-6d646c5aa3bc?source=post_page-----71b21ac8dc70---------------------------------------)

The crux of these privacy issues is that the Sesame protocol made a design **choice** to extend E2EE from the Single Device setting to the Multi Device setting, by establishing a dedicated session between sender’s device and **each of** recipient’s devices. For example, if Alice wants to send Bob a WhatsApp message and Bob has 5 devices, then Alice’s device needs to establish an E2EE session with each of Bob’s device. As a result, senders (and even potential senders) are aware of the devices setup of their (potential) recipients and some long term identity of the devices, due to the persistence of their cryptographic material (keys). In addition, recipients know which protocol message originated from which sender device.

To sum up: WhatsApp exposes, **by design**, some information about the devices used by its users to any user of the platform and does not provide any controls or settings or configuration to allow users to control this exposure (even blocking a user does not solve it) .

Specifically, we found out that attackers can learn about:

* **Number of user device**s: WhatsApp user must have 1 mobile ***primary*** device, and up to 4 ***companion*** non-mobile (desktop app, Web) devices.
* **Devices’ long term identifiers**: Each devices is assigned with a unique and unchanging WhatsApp ID which is exposed to potential senders. It enables continued monitoring and identification of the active device.
* **Crude device type identification**: Whether the device is the mobile ***primary*** device, or one of the 4 ***companion*** non-mobile (desktop app, Web) devices.

These information leaks, may allow attackers to gain some needed information about their victims, such as the number of devices, changes to the setup by monitoring this data over time and which message was sent by which device (including acknowledges and read receipts)

While these information leaks by themselves are bad enough, we wanted to know if attackers can refine the crude device identification and find out more specific information about their victims’ devices.

## Fingerprinting WhatsApp Operating Systems take 1: View Once Media

[firewalls.com](https://www.firewalls.com/blog/security-terms/os-fingerprinting/) defines Operating System (OS) Fingerprinting as

> ..the process of analyzing data packets which originate from a network in an attempt to glean intelligence to be used in later attacks. By detecting which operating system a network operates on, hackers have an easier time targeting known vulnerabilities.

Press enter or click to view image in full size

![]()

Our first candidate for OS Fingerprinting, was the “View once media” feature that behaves differently by design on different Operating Systems: For example, web clients should not display “View once media”.

Surprisingly, we found out that this feature is actually privacy theater: All types of clients behave virtually the same, with the addition of a skin deep display prevention layer in Web clients. While this is a serious problem per se, as Web extensions can easily remove this display prevention layer to re-enable users to view and redistribute such media, it does not advance us in fingerprinting the OS.

[## Once and Forever: WhatsApp’s View Once Functionality is Broken

### Meta’s WhatsApp suggests using “View once” media for privacy. We discovered attackers can and actually do bypass this…

medium.com](/%40TalBeerySec/once-and-forever-whatsapps-view-once-functionality-is-broken-302a508390b0?source=post_page-----71b21ac8dc70---------------------------------------)

## Fingerprinting WhatsApp Operating Systems take 2: Message IDs

The failed “View Once Media” attempt did help us in an unexpected manner. While looking into “View once media” exploiting extensions, we found the excellent [WhatsApp-Web-Plus](https://github.com/Schwartzblat/WhatsApp-Web-Plus) open source Chrome Web extension

[## GitHub — Schwartzblat/WhatsApp-Web-Plus: A WhatsApp-Web extension that extends the client…

### A WhatsApp-Web extension that extends the client capabilities and does some very cool stuff. …

github.com](https://github.com/Schwartzblat/WhatsApp-Web-Plus?source=post_page-----71b21ac8dc70---------------------------------------)

On top of this Web extension “View once” capabilities, it also contains this code to identify the senders’ Operating System, based on the message ID. Later on

Message ID is generated by the sending devic...