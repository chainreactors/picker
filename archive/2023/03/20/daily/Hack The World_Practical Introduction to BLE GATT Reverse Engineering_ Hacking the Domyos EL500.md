---
title: Practical Introduction to BLE GATT Reverse Engineering: Hacking the Domyos EL500
url: https://jcjc-dev.com/2023/03/19/reversing-domyos-el500-elliptical/
source: Hack The World
date: 2023-03-20
fetch_date: 2025-10-04T10:05:23.720354
---

# Practical Introduction to BLE GATT Reverse Engineering: Hacking the Domyos EL500

# [Hack The World](https://jcjc-dev.com)

Projects and learnt lessons on Systems Security, Embedded Development, IoT and anything worth writing about

[Archive](/archive/)
[Consulting](/consulting/)
[Juan Carlos Jimenez](https://uk.linkedin.com/in/juan-carlos-jim%C3%A9nez-bba49033/en)
[Twitter](https://twitter.com/Palantir555)
[GitHub](https://github.com/Palantir555)
e-mail

# Practical Introduction to BLE GATT Reverse Engineering: Hacking the Domyos EL500

19 Mar 2023

My goal for this project was quite specific, leaving many details unexplored (for now).
This post aims to be a quick reference for my future self, and to hopefully help
anyone else who might be interested in doing something similar.

No security is bypassed, no exciting exploits are used, and no dangerous
backdoors are found. We will simply connect to the device and determine how it
works using straightforward methodologies.

Some decisions were made for the sake of my own learning, and might be simplified
by using different tools and approaches. Consider following this guide if you
are more interested in learning about BLE GATT than in discovering the fastest
and most efficient tools.

## The Target: Domyos EL500

[The EL500](https://www.decathlon.com/products/el500-smart-connect-elliptical-exercise-machine-331582),
is a cheap(ish) Bluetooth-enabled elliptical trainer sold by Decathlon. There’s
no need to delve into too much detail; it’s an affordable machine with multiple
resistance settings, a heart rate monitor, and Bluetooth connectivity.

![el500-drawing](/assets/domyos-el500/domyos-target-compressed.jpg)

A mobile app called `eConnected` is provided to monitor the exercise session from your
smartphone, and save it for future reference as an image of a graph. The active
sessions look like this, and are saved as an image of that same graph:

![econnected session](/assets/domyos-el500/econnected-quick-session.jpg)

I was interested in building a very specific user interface, and logging the data
in much more detail, so I decided to reverse engineer the BLE comms, and build my
own interface in Python. As one does…

First, we need to understand the basics of BLE, and the tools we’ll be using.

## The Protocol: BLE GATT

BLE (Bluetooth Low Energy) is a wireless communication technology for short-range
comms between devices. BLE supports multiple profiles with different degrees
of flexibility, data throughput, energy usage, etc.

The BLE protocol we are interested in is GATT (Generic Attribute Profile); it is
-AFAIK- the most commonly used on wireless devices to exchange arbitrary data.
It is highly specified to facilitate interoperability, which plays to our advantage
in the reverse engineering process.

Grossly oversimplifying things, a profile is a predefined collection of services,
and each service contains a group of characteristics. Characteristics can have
associated descriptors that provide metadata or connection-specific config
options for their characteristic.

Here’s a diagram to illustrate the very basics:

![GATT diagram](/assets/domyos-el500/gatt-basics.jpg)

We can easily start the device, discover it using some bluetooth
tool, confirm that it is indeed running GATT, connect to it, and discover how the
GATT properties are set up.

![nRF Connect screenshot](/assets/domyos-el500/nrf-scanner.jpg)

Even though this device -as so many others- does not seem to use any of the
security mechanisms supported by BLE, they are still worth mentioning:

* [Pairing](http://lpccs-docs.renesas.com/Tutorial-DA145x-BLE-Security/pairing_and_bonding.html#pairing):
  The client and server go through a “secure” connection process to
  authenticate each other and share the keys used for further communication.
  The pairing process supports 4 different association models, each with its own
  set of security properties and suitable differently abled devices:
  + **Just Works**: Unauthenticated pairing process, common in devices without a screen or other
    means of presenting a pairing code. Since BLE 4.2’s “Secure Connections” (an upgrade
    to the older Secure Simple Pairing), the key exchange is performed with P-256
    Elliptic Curve Diffie-Hellman (ECDH), which protects the process against passive
    eavesdropping, but not so much against Man-in-the-Middle attacks.
  + **Numeric Comparison**: The devices go through the ECDH key exchange, then share
    a secret and use it along with their respective private keys to compute the same
    pairing code. Each device displays the code to the user, who must confirm that
    the codes match on both devices.
  + **Passkey**: One device displays a pairing code for the user to enter on the other device.
    Or, less commonly, the user enters the same code on both devices.
    The pairing code is used along the ECDH-derived shared secret to compute the
    encryption keys.
  + **Out of Band**: The devices may or may not use ECDH to exchange keys, but they
    will use communication channels outside bluetooth to share some secure element(s).
    e.g. Tap the devices to kickstart an NFC-based key exchange, or have the device
    display a QR code for the user to scan from a mobile app, etc.
* [Bonding](http://lpccs-docs.renesas.com/Tutorial-DA145x-BLE-Security/pairing_and_bonding.html#bonding):
  Akin to a website’s “remember me”. The paired devices exchange and
  store the necessary information to reconnect in the future without having to go
  through the pairing process again.
* [Message Signatures](http://lpccs-docs.renesas.com/Tutorial-DA145x-BLE-Security/access_and_signing.html#authentication-and-data-signing):
  BLE devices can generate and use a dedicated signing key (CSRK) to digitally sign
  messages for authentication, integrity and non-repudiation purposes
* [Authorization](http://lpccs-docs.renesas.com/Tutorial-DA145x-BLE-Security/access_and_signing.html?highlight=authorization):
  The BLE spec accounts for the possibility of allowing different levels of access for
  connected clients. Given the nature of the feature, GATT can simply report if
  a given attribute requires authorization, but the product implications of that are
  left to the application layer

For more/better info, you should check out the BLE
specifications published by the [Bluetooth SIG](https://www.bluetooth.com/specifications/).
Or at least one of the
[countless](https://learn.adafruit.com/introduction-to-bluetooth-low-energy?view=all)
[BLE](https://www.arduino.cc/reference/en/libraries/arduinoble/)
[intros](https://devzone.nordicsemi.com/guides/short-range-guides/b/bluetooth-low-energy/posts/ble-characteristics-a-beginners-tutorial)
[available](http://lpccs-docs.renesas.com/Tutorial-DA145x-BLE-Security/pairing_and_bonding.html)
[online](https://iotexpert.com/ble-write-request-write-command-signed-write-command-prepare-write/).

## The Tools: bluetoothctl, nRF Connect, Android, BlueZ, gattacker…

Given the popularity of BLE in modern devices, there are plenty of tools to work
with it. Some are for developers, others for users, or security researchers…

I’d classify them in 3 categories:

* Offensive tools: Made specifically to run attacks or offensive recon against BLE targets
  + `gattacker`, `ubertooth`, etc.
* System tools: Made to integrate and manage BLE on an OS
  + Linux: `bluetoothctl`, `hcitool`, `bluez`, `gatttool`, etc.
* Developer tools: Made to help developers create and debug their systems
  + Android apps: `nRF Connect`
  + Android: `Bluetooth HCI snoop log` developer mode option
  + BLE/GATT libraries: `bluepy`, `pygatt`, `gatt`, embedded SDKs, Arduino libs, etc.

I tried sniffing the traffic using `ubertooth`, if just to make sure there
was no funny business going on. But it is not worth the effort for a project like this.

Other than that, I decided against using any of the many offensive tools out there.
I couldn’t be bothered to find a dongle that would support MAC vendor spoofing,
worked well with my setup, etc.

Since this shouldn’t be a high ef...