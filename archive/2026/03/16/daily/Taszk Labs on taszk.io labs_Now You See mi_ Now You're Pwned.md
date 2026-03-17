---
title: Now You See mi: Now You're Pwned
url: https://labs.taszk.io/articles/post/nowyouseemi/
source: Taszk Labs on taszk.io labs
date: 2026-03-16
fetch_date: 2026-03-17T04:17:17.774969
---

# Now You See mi: Now You're Pwned

[![logo](https://labs.taszk.io/images/taszk_logo.png)
![logo](https://labs.taszk.io/images/taszk_logo_white.png)](https://labs.taszk.io)

* [Home](https://labs.taszk.io/)
* [Articles](https://labs.taszk.io/articles)
* [Advisories](https://labs.taszk.io/blog)
* [Get in touch](https://taszk.io/contact)

## [Now You See mi: Now You're Pwned](https://labs.taszk.io/articles/post/nowyouseemi/)

2026-03-16
 by Botond Hartmann
 [Xiaomi](/articles/tags/xiaomi) [wifi](/articles/tags/wifi) [camera](/articles/tags/camera) [smart](/articles/tags/smart)

*In this blogpost, the newest full-time member of our research team describes his internship project.*

*If you would also like to try your hand at our hacking tools and techniques, don’t hesitate to check out our training offerings! Currently available: <https://www.offensivecon.org/trainings/2026/exploiting-smartphones-through-baseband.html>*

Last summer, I had an opportunity to join TASZK Security Labs for a summer internship.
The target we selected for this 2 months project was to hack Xiaomi Security Cameras, specifically a Xiaomi C400 Smart Camera, a very popular device in our market that we also happened to already have at hand.

We defined two end goals:

* create an RCE exploit via any wireless/LAN interface
* use the exploit to create a full “cloud jailbreak”

The motivation for the latter was that we knew that these devices are heavily dependent for their operation on the Xiaomi Smartphone Application and Xiaomi Cloud Server.
Accordingly, our goal was to achieve a setup in which the camera is fully functional without any reliance on a Xiaomi account.

Given the time limit, the project was of course more real-life-CTF than an attempt at a comprehensive security review.

In the end, I identified 3 serious vulnerabilities in the implementation of Xiaomi’s proprietary device setup protocol, and was able to use them to build both the RCE exploit as well as the jailbreak that we set out to do.

![xiaomi_exploit](/images/blog/nowyouseemi/shell.gif)

The vulnerabilities we are releasing today were each reported to Xiaomi in September 2025.
The companion advisories are published [here](https://labs.taszk.io/blog/post/112_mi_hshake_bypass/), [here](https://labs.taszk.io/blog/post/113_mi_rng_predict/), and [here](https://labs.taszk.io/blog/post/114_mi_heap_bof/).

Interested parties may find more additional information about the disclosure process, and the patch status of the vulnerabilities, in the above linked advisories. We highlight here that the nature of these vulnerabilities require a physically adjacent attacker in practice, which limits their severity.

We are also releasing the full code for both the exploit and the jailbreak on our github: [rce exploit](https://github.com/TaszkSecLabs/xiaomi-c400-pwn/tree/main/xiaomi-c400-exploit), [jailbreak](https://github.com/TaszkSecLabs/xiaomi-c400-pwn/tree/main/xiaomi-c400-jailbreak).

(Note: the material released on github is provided as-is and for the sole purpose of advancing public research.
We make zero claims, we do not offer and will not provide any support, use only at your own risk, any use for any illegal activity is expressely forbidden.)

In the following, I’ll describe the research journey and the technical bits of creating the exploit and jailbreak!

# Reverse Engineering

Generally the first steps of reverse engineering such an IoT device are to obtain its software and to dissect them extracting executable binaries, config files, etc.

The firmware running on the devices may come from different sources, the most readily available is downloading the update files (OTA) from the manufacturer’s server.
Also, the flash chip of the actual device can be directly dumped by wiring it up to a flash reader hardware.
Depending on the hardening of the bootloader, the U-Boot may have been compiled with its interactive shell enabled, which makes it possible to dump the storage media much more easily.

With a dump of the system partition in hand, the static analysis part of the reverse engineering work can begin!

Most of the time static analysis is not enough, and it is desired to interact with the device as it runs on the real hardware.
For purposes like rewriting configurations or managing running services, a shell access is crucial.
The security cameras – being themselves embedded devices – usually have serial ports mainly to print application logs.
However, some also present a login shell on them!
Telnet and SSH access can also occur, probably gated behind a debug flag.

When the system-wide focus of reverse engineering narrows down to a single potentially vulnerable binary, more advanced debugging capabilities are needed.
This can be a statically compiled `gdb` server deployed to the security camera, which can be accessed over network.

## Xiaomi C400

For this research phase, shout-out to my colleague Lorant Szabo for his guidance and assistance.

The very first challenge with this camera was to physical disassemble the device: the dome section has very stiff clips holding its two parts togother.

On the PCB, around the SigmaStar ARMv7 SoC, there were some visible test pads.
By measuring them with a multimeter during the boot-up of the camera, one of them seemed like 3.3V signal.
Hooking that pin into a logical analyzer we were able to identify that it is indeed an UART-TX pin, with 115200 baudrate.
Then with trial-and-error the UART-RX pin is also found on the same set of pins.
The UART pins are connected to an FTDI USB-serial adapter, and even though a huge amount of log message is received, the device seems to ignore anything coming from RX, so no login shell was given this way.

![xiaomi_uart1](/images/blog/nowyouseemi/xiaomi1.jpg)

To obtain the actual software running on the device, we dumped the flash with the help of a SOIC-8 clip connected to a flash adapter and the flashrom tool on the PC.

![xiaomi_uart2](/images/blog/nowyouseemi/xiaomi2.jpg)

This allowed us to find the cmdline of the Linux kernel inside the u-boot envvar partition.
And by simply hooking the Linux init phase – by replacing the `init=/linuxrc` to `init=/bin/sh`, correcting the CRC of the UBOOT-ENV partition, and writing it to the flash externally – we finally got a shell on the serial port.

## OTA Firmare

For Xiaomi devices, obtaining OTAs are tricky, as there is no support page with downloadable firmware files or public file listings for the firmware files.
Xiaomi devices query the update from the Xiaomi update server, and they get served with the next possible OTA update URL.

However, there are some patterns in the URL, which contains the firmware version.
So, albeit there is no comprehensive changelog of the device, this still may allow one to brute-force it.

In our case, as described above, we already achieved a root shell at this point, so we weren’t restricted to OTA firmware images for our reverse engineering needs.

## System Partition

Further analyzing the system partition reveals multiple squashfs and JFFS2 partitions, containing the interesting service binaries on the USRFS partition.

After getting a shell, we find ourselves in a standard, [Buildroot](https://buildroot.org/)-based embedded Linux system with a busybox+uClibc userland. Inspecting the running processes, we see:

* `hostapd`, creating an open Wi-Fi network that we can connect to
* `imi_mike`, `miio_client`, `mi_daemon`: these three processes contain the actual logic of the camera
  + `imi_mike` is responsible for interfacing with hardware.
  + `miio_client` is the one that has an open UDP port. Apart from the DHCP server, this is the only network-accessible port that the device exposes.
  + `mi_daemon` loads configuration and supervises the previous two processes, restarting them should they crash.
  + These three communicate by sending JSON over unix sockets and TCP loopback connections.

As the only one directly exposed to the network, `miio_client` is the obvious attack surface. When you purchas...