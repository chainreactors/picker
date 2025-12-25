---
title: God Mode On how we attacked a vehicle’s head unit modem
url: https://ics-cert.kaspersky.com/publications/reports/2025/11/20/god-mode-on-researchers-run-doom-on-a-vehicles-head-unit-after-remotely-attacking-its-modem/
source: Instapaper: Unread
date: 2025-12-24
fetch_date: 2025-12-25T03:27:04.391409
---

# God Mode On how we attacked a vehicle’s head unit modem

[![](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/logo-ics.svg)](https://ics-cert.kaspersky.com)

* [Publications](https://ics-cert.kaspersky.com/publications/)
* [Services](https://ics-cert.kaspersky.com/services/)
* [Advisories](https://ics-cert.kaspersky.com/advisories/)
* [Statistics](https://ics-cert.kaspersky.com/statistics/)

English
English
Русский

[![](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/logo-ics.svg)](https://ics-cert.kaspersky.com)

* [Publications](https://ics-cert.kaspersky.com/publications/)
* [Services](https://ics-cert.kaspersky.com/services/)
* [Advisories](https://ics-cert.kaspersky.com/advisories/)
* [Statistics](https://ics-cert.kaspersky.com/statistics/)

English
English
Русский

Contents:

* [Main](https://ics-cert.kaspersky.com)
* [Publications](https://ics-cert.kaspersky.com/publications)
* [Reports](https://ics-cert.kaspersky.com/publications/reports/)
* God Mode On: Researchers run Doom on a vehicle’s head unit after remotely attacking its modem
* God Mode On: Researchers run Doom on a vehicle’s head unit after remotely attacking its modem

20 November 2025

# God Mode On: Researchers run Doom on a vehicle’s head unit after remotely attacking its modem

* ![](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/icons/telegram-black.svg)
* ![](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/icons/x-black.svg)
* ![](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/icons/linkedin-black.svg)
* ![](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/icons/email-black.svg)

[Download PDF](https://ics-cert.kaspersky.com/media/Kaspersky-ICS-CERT-Doom-on-the-cars-head-unit-En.pdf)

Subscribe to newsletter

![close](https://ics-cert.kaspersky.com/wp-content/themes/new_ics_cert/assests/img/icons/close.svg)

Related tags

[vulnerabilities](https://ics-cert.kaspersky.com/publications/reports/?t=vulnerabilities)

Related tags

Show all

[vulnerabilities](https://ics-cert.kaspersky.com/publications/reports/?t=vulnerabilities)

![](https://ics-cert.kaspersky.com/wp-content/uploads/sites/27/2025/11/kaspersky-ics-cert_doom-on-head-unit-1024x585.jpg)

**Exploiting a vulnerability identified in a modem installed in the head units of some vehicles enabled Kaspersky ICS CERT experts to gain complete control of the system.**

## **Introduction**

Imagine you are a driver speeding down the highway in your brand-new electric car. All of a sudden, the entire massive multimedia display is filled with Doom, the iconic 3D shooter game, replacing the navigation map or the controls menu, and you realize someone is playing it right now by remotely controlling the character. This is not a dream or an overactive imagination, but a realistic scenario in today’s world, as vividly demonstrated by Kaspersky ICS CERT experts.

We know that the Internet of Things plays a significant role in the modern world, where not only smartphones and laptops, but also factories, cars, trains, and even airplanes are connected to the network. Most of the time, connectivity is provided via 3G/4G/5G mobile data networks using modems installed in these vehicles and devices. Increasingly, these modems are integrated into a System-on-Chip (SoC), which can simultaneously perform multiple functions using a Communication Processor (CP) and an Application Processor (AP). A general-purpose operating system such as Android can run on the AP, while the CP, which handles communication with the mobile network, typically runs on a dedicated OS. The interaction between the AP, CP, and RAM within the SoC at the microarchitecture level is a “black box” known only to the manufacturer – even though the security of the entire SoC depends on it.

It is generally believed that bypassing 3G/LTE security mechanisms is purely an academic challenge, because a secure communication channel is established when a user device (User Equipment, UE) connects to a cellular base station (Evolved Node B, eNB). Even if someone can bypass these mechanisms, discover a vulnerability in the modem, and execute their own code on it, this is unlikely to compromise the device’s business logic. This logic (for example, user applications, browser history, calls, and SMS on a smartphone) resides on the AP and is presumably not accessible from the modem. Or is it?

To find out, we conducted a security assessment of a modern SoC, Unisoc UIS7862A, which features an integrated 2G/3G/4G modem. This SoC can be found in various mobile devices by multiple vendors or, more interestingly, in the head units of modern Chinese vehicles, which are becoming increasingly common on the roads. The head unit is one of a car’s key components, and a breach of its information security poses a threat to road safety, as well as the confidentiality of user data.

During our research, we identified several critical vulnerabilities at various levels of the Unisoc UIS7862A modem’s cellular protocol stack. This article discusses a stack-based buffer overflow vulnerability in the 3G RLC protocol implementation ([CVE-2024-39432](https://ics-cert.kaspersky.com/away?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2024-39432&hs=e45ee7ce7e88149af8dd32b27f9512ce)). The vulnerability can be exploited to achieve remote code execution at the early stages of connection, before any protection mechanisms are activated.

Importantly, gaining the ability to execute code on the modem is only the entry point for a complete remote compromise of the entire SoC. Our subsequent efforts were focused on gaining access to the AP. We discovered several ways to do so, including leveraging a hardware vulnerability in the form of a hidden peripheral Direct Memory Access (DMA) device to perform lateral movement within the SoC. This enabled us to install our own patch into the running Android kernel and execute arbitrary code on the AP with the highest privileges. Details are provided in the relevant sections.

## **Acquiring the modem firmware**

The modem at the center of our research was found on the circuit board of the head unit in a Chinese car.

![](https://ics-cert.kaspersky.com/wp-content/uploads/sites/27/2025/11/doom-on-the-cars-head-unit-11.png)

| Number in the board photo | Component |
| --- | --- |
| 1 | Realtek RTL8761ATV 802.11b/g/n 2.4G controller with wireless LAN (WLAN) and USB interfaces (USB 1.0/1.1/2.0 standards) |
| 2 | SPRD UMW2652 BGA WiFi chip |
| 3 | 55966 TYADZ 21086 chip |
| 4 | SPRD SR3595D (Unisoc) radio frequency transceiver |
| 5 | Techpoint TP9950 video decoder |
| 6 | UNISOC UIS7862A |
| 7 | BIWIN BWSRGX32H2A-48G-X internal storage, Package200-FBGA, ROM Type – Discrete, ROM Size – LPDDR4X, 48G |
| 8 | SCY E128CYNT2ABE00 EMMC 128G/JEDEC memory card |
| 9 | SPREADTRUM UMP510G5 power controller |
| 10 | FEI.1s LE330315 USB2.0 shunt chip |
| 11 | SCT2432STER synchronous step-down DC-DC converter with internal compensation |

**Table. Description of the circuit board components**

Using information about the modem’s hardware, we desoldered and read the embedded multimedia memory card, which contained a complete image of its operating system. We then analyzed the image obtained.

## **Remote access to the modem (CVE-2024-39431)**

The modem under investigation, like any modern modem, implements several protocol stacks: 2G, 3G, and LTE. Clearly, the more protocols a device supports, the more potential entry points (attack vectors) it has. Moreover, the lower in the OSI network model stack a vulnerability sits, the more severe the consequences of its exploitation can be. Therefore, we decided to analyze the data packet fragmentation mechanisms at the data link layer (RLC protocol).

We focused on this protocol because it is used to establish a secure encrypted data transmission channel between the base station and the modem, and, in particular, it is used to transmit NAS (Non-Access Stratum) ...