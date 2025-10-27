---
title: If the Person Who Finds a Web3 Hardware Wallet is a Hacker
url: https://www.darknavy.org/blog/if_the_person_who_finds_a_web3_hardware_wallet_is_a_hacker/
source: Instapaper: Unread
date: 2025-05-04
fetch_date: 2025-10-06T22:29:34.777364
---

# If the Person Who Finds a Web3 Hardware Wallet is a Hacker

[![](https://www.darknavy.org/images/darknavy_shenlan_dot.png)](https://www.darknavy.org/ "  (Alt + H)")

* |
* [Zh](https://www.darknavy.org/zh/ "Chinese")

* [Home](https://www.darknavy.org/ "Home")
* [Blog](https://www.darknavy.org/blog/ "Blog")
* [Insight](https://www.darknavy.org/darknavy_insight/ "Insight")
* [About](https://www.darknavy.org/about/ "About")

[Home](https://www.darknavy.org/) » [Blog](https://www.darknavy.org/blog/)

# If the Person Who Finds a Web3 Hardware Wallet is a Hacker

March 30, 2025 · 1437 words · DARKNAVY

Table of Contents

* [Attack Surface Overview](#attack-surface-overview)
* [USB Attack Surface](#usb-attack-surface)
* [NFC Attack Surface](#nfc-attack-surface)
* [Conclusion](#conclusion)
* [Reference](#reference)

In 2024, Web3 security incidents caused by private key leaks have surged, resulting in estimated financial losses exceeding $855 million.

Private keys function as the sole credentials for blockchain accounts, controlling access to all associated on-chain assets like cryptocurrencies and NFTs. Due to the decentralized nature of blockchain, losing the private key means permanently losing account control, while leakage typically results in asset theft. **Hardware wallets**, utilizing techniques like offline private key storage and secure chips, have become the primary choice for asset protection.

But does the moment a hacker’s fingertip touches the metal casing of a hardware wallet, the Pandora’s box of the digital abyss truly open?

In this brief overview of attack and defense, we outline DARKNAVY’s research on Web3 hardware wallets from an adversarial perspective.

![Exploiting Cypherock X1 Vault Vulnerability to display “Hacked by DARKNAVY” on screen](/blog/if_the_person_who_finds_a_web3_hardware_wallet_is_a_hacker/attachments/7040d7d5-4672-4806-a6e3-ef920e3515da.png)

## Attack Surface Overview[#](#attack-surface-overview)

Mainstream hardware wallets available on the market, despite variations in form factor, are typically marketed with assertions of robust security designs. However, the efficacy of these proclaimed security features may not consistently meet expectations, and in some cases, might even introduce vulnerabilities. Although hardware wallets effectively reduce numerous attack surfaces through mechanisms like offline signing and simplified functionalities, **this does not guarantee that the security of the remaining attack surfaces.**

Due to their offline nature, hardware wallets require external devices (e.g., browsers, mobile apps) to transmit transaction data for signing and to subsequently broadcast signed results to the blockchain. Certain wallets with small or absent displays provide configuration settings exclusively via an associated application, which in turn transmits the necessary configuration parameters to the wallet.

Based on analysis of mainstream hardware wallets, We classify the typical connection methods between the hardware wallet and external entities and access the associated security risks.

Firstly, three duplex communication interfaces have been identified: USB, NFC, and Bluetooth.

These three methods may harbor vulnerabilities in their data communication protocols and data processing, potentially leading to issues like memory corruption or sensitive information leakage. **When an attacker has physical access to the device, these communication interfaces may further introduce security risks:**

* **USB:** Some wallets can emulate a USB flash drive,thereby increasing the attack surface; Additionally, certain devices support bootloader mode, granting access to lower-level functions via USB.
* **NFC:** Although physical proximity limits its exploitation, NFC communication remains susceptible to Man-in-the-Middle (MitM) attacks, which may allow an attacker to intercept and parse sensitive data.
* **Bluetooth:** Bluetooth communication itself has multiple risk points, such as pairing hijacking, MitM attacks, and data sniffing, and its range limit is much less restrictive than NFC’s.

![USB connection of Hardware Wallets](/blog/if_the_person_who_finds_a_web3_hardware_wallet_is_a_hacker/attachments/223ade8e-09ea-490c-9c6e-ecdc00e5c99d.png)

These communication methods connect the offline wallet to networked devices, raising concerns among users: What data is actually being transferred between the external device and the wallet? If the device is compromised, is the wallet still safe? Or, could the wallet and its accompanying app have built-in backdoors that surreptitiously upload wallet data after establishing a connection?

To address these concerns, hardware wallet manufacturers have introduced the concept of “Air Gapped,” physically isolating the wallet from network-connected devices. Two primary transmission methods adhere to this principle, both requiring user intervention to execute a one-way data transfer. The specific operation processes and risks are as follows:

* **QR Code:** The client first converts the data requiring a signature into a static or dynamic QR code. The hardware wallet, equipped with a camera, scans the QR code to retrieve the data and confirm the signature, and finally, the client scans the QR code displayed on the hardware wallet. Memory corruption issues might arise during the processes of image parsing and QR code recognition.
* **SD Card:** The client and the hardware wallet exchange signature request and signature result files in a specific format using a single SD card. Memory corruption issues may occur when parsing the file format.

![Using QR Code to obtain transaction information](/blog/if_the_person_who_finds_a_web3_hardware_wallet_is_a_hacker/attachments/f45f7110-e4c3-447c-9aef-fc31aa74121c.jpeg " =385x482")

Besides attack surfaces exposed during communication, some hardware wallets also provide firmware update interfaces (commonly via USB, Bluetooth, or SD card mode). The update process typically involves hash calculations, signature verifications to ensure firmware integrity and authenticity, and version checks to prevent rollbacks. If the update process is poorly implemented, an attacker might be able to flash malicious firmware or an older, vulnerable firmware version.

![Firmware update process](/blog/if_the_person_who_finds_a_web3_hardware_wallet_is_a_hacker/attachments/f046cacb-ba9f-45b3-b2d2-3ff65fa7096b.jpeg " =214x300")

Furthermore, although most hardware wallets employ secure chips for private key storage, they remain vulnerable to physical attacks such as side-channel analysis and hardware fault injection.

The following sections will analyze the **USB and NFC attack surfaces** from an adversary’s perspective.

## USB Attack Surface[#](#usb-attack-surface)

Many hardware wallets communicate with computers or mobile devices via USB. Based on the underlying USB HID protocol, each hardware wallet implements its own proprietary application-layer protocol that defines specific commands and response formats. Using the Cypherock X1 wallet as a case study, we outline the attack surface associated with USB connectivity.

The X1 runs a **real-time embedded system** that processes incoming USB requests. A complete USB command cycle begins with **the desktop application cySync**, which serializes the request via an SDK and transmits it to the X1 wallet over USB. The wallet processes the request and returns a data packet, repeating this circle until the command is fully executed.

![USB communication with the X1 wallet via CLI](/blog/if_the_person_who_finds_a_web3_hardware_wallet_is_a_hacker/attachments/f911a6a2-3747-4a68-a800-c14beb2f9f91.png " =910x778")

The X1 wallet contains multiple applets. After reading the `applet_id` from the request via a USB event callback, the X1 invokes the corresponding applet for further processing.

From an attacker’s perspective, the logic related to the device’s communication with the outside world is of greater interest: the device responds to requests via event callbacks, parsing protobuf d...