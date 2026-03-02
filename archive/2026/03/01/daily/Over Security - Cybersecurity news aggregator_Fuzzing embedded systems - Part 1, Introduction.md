---
title: Fuzzing embedded systems - Part 1, Introduction
url: https://blog.sparrrgh.me//fuzzing/embedded/2024/06/05/fuzzing-embedded-systems-1.html
source: Over Security - Cybersecurity news aggregator
date: 2026-03-01
fetch_date: 2026-03-02T04:07:02.621323
---

# Fuzzing embedded systems - Part 1, Introduction

[Sparrrgh's blog](/)

[ ]

[About](/about/)

[About](/about/)

# Fuzzing embedded systems - Part 1, Introduction

Jun 5, 2024

## Intro

This will be the start of a series of blog posts based on my bachelor’s degree thesis, developed during an internship at Secure Network srl[1](#fn:1). The objective of the internship was to analyze an embedded device, and develop tools to test its security.

As a result I developed a **fuzzer** to search for vulnerabilities in CGI binaries and a **Binary Ninja plugin** to search for ROP chains in MIPS binaries, as well as an exploit for one of the crashes triaged.

Today will be really introductory and we will briefly explore the basics of how to obtain and analyze a device’s firmware, and the process to choose a target binary for the fuzzer. In the next part we will explore how to write a binary-only fuzzer in LibAFL and finally in the third part how to exploit the vulnerabilities found.

## Target choice

**Embedded device** is quite a broad term, and it encompasses many different type of systems, from huge solar inverters to tiny IoT cameras. These devices are designed to perform a handful of **specific** tasks, and often have ad-hoc hardware and software to do so.

The requirements for low **power consumption** (they are designed to not be powered off) and low **memory consumption** (system resources are kept to a minimum to reduce cost and size) make implementing a lot of the modern memory corruption mitigations impossible. This makes them a prime target to gain a foothold in a network.

Since there are a miriad of devices which could be classified as “embedded systems”, we have to find the type of device which better suits our needs.
I wanted a device which:

1. Exposes a number of services to the network.
2. Whose compromise could lead to having further access to user data or to the network on which it’s installed.
3. It’s cheap enough that if I accidentally break it, it won’t break the bank.

For this reasons I chose to target a router.

Commercial routers have to handle a lot of different network services as well as services to manage them, making their attack surface quite extended. Also, compromising one could grant access to different sections of the network.

So I headed to Amazon and chose the one reported as “most purchased” at the time which was the **DSL-3788** by **D-Link**[2](#fn:2), a router designed with home use in mind.

## Studying hardware configuration

Luckily someone uploaded pictures of their damaged router on a support forum[3](#fn:3), which allowed me to research the PCB and the components before even buying the router.
From the uploaded pictures we can note a few things.

![Photo of the PCB displaying the text DSL-3785 painted and underlined as well as a CPU component with EcoNet EN7513GT engraved on it](/assets/img/dsl-3788_pcb_reuse.png)

The PCB is engraved with the model number of **another router**. This make it more probable that code is also reused, meaning that a vulnerability found could affect multiple models.
We can also identify single components like CPUs, memories and available interfaces.
Identifying this components is fundamental to perform hardware attacks and gain important information which we will use during the analysis of the software.
As an example, by identifying the **CPU model** as *EcoNet EN7513GT* we can determine the architecture used, which in this case it’s **MIPS**. This will prove to be really important (and a real pain) later.

We can also see a potential **UART** interface. Exposed **serial communication interfaces** (e.g., UART, JTAG) are **the** low hanging fruit for firmware extraction. Extracting firmware using this interfaces usually requires low to none hardware modification, and relatively cheap hardware to interact with them.

If none are found, it might be necessary to dump the firmware directly from memory. This is done by either **detaching** the flash memory chip completely and attaching it to a memory reader, or by **sniffing** the traffic between the integrated circuit and flash memory. Firmware isn’t **usually** encrypted at rest, but high-security devices might have it as a feature, making dumping the flash memory useless.

![Photo of connector on the PCB with 4 exposed pins labelled RX,TX,GND,VCC](/assets/img/UART_online.jpg)

An alleged UART port is visible (just guessing, based on the 4 pins in a row) in the pictures provided, and engraved right below the pins are the (alleged) use of the pins.

### Testing the UART port

A UART port can be used to communicate through serial with the **integrated circuit** and it’s used by vendors to debug the device. Usually the pins are not installed on production devices, and only the pads are exposed. These pads have sometimes their traces interrupted to stop end users from interacting with it.

I first tested if the pins found were connected and the engraving on the PCB was correct by using a multimeter on each of them.
There are also other more physical techniques to check if the pads are connected, like shining a bright light oh the backside of the PCB as detailed here[4](#fn:4).
I then used a *logic analyzer* to verify if the port was communicating correctly, and which was the correct *baudrate* which the interface uses to communicate.
The logic analyzer shows some logs as output! Meaning it does in fact communicate through serial (thankfully, because my soldering skills are almost non-existant).

![Screenshot of Logic Pro software displaying some text which looks like startup logs from a Linux based system](/assets/img/logic_analyser_UART.png)

## Obtaining firmware

Firmware is typically distributed by vendor in **encrypted form**, to prevent users from reversing it or modifying the code run on the system.
Usually this leads to interacting with hardware to get the software, but there are software-only ways to get it.
If even only **one** past version of the firmware did not have encryption, we could decrypt the following versions using its code as detailed in this ZDI article[5](#fn:5).
This has the added benefit of being able to decrypt different firmwares of the same vendor, by writing just one decryptor.

Sometimes firmware is distributed in unencrypted form through **update systems** directly on the device or, for modern embedded systems, through a mobile application. It might be worth trying to intercept the traffic (especially if you already have a mobile app testing laboratory) and check if it’s possible to get an unencrypted firmware update this way.

In this case I decided, for future debugging purposes, to go with the hardware route and interact with the UART port we discovered previously.
We can now connect using our favorite serial communication tool, and interact with an exposed (root) shell.

![Photo of Shikra device connected using small cables to the previously shown 4-pin connector on the PCB](/assets/img/shikra_cut.png)

There are many different tools available to do this (Glasgow, Shikra, Buspirate, JTAGulator, etc.) with different prices ranges according to the number of supported protocols. The one shown in the picture and used during the research is a Shikra.

![Screenshot of Linux shell displaying version 1.6.1 of busybox as well as enviroment variables showing the shell is logged in as root](/assets/img/UART_root_shell.png)

After connecting the pins as instructed by the Shikra documentation we can see an **interactive root shell**, we can use this to explore the firmware and dump it to our machine to get information more easily.
The commands available are often really limited (as seen in the picture above), uploading a more versatile version of *Busybox* will lift the limitations and give us the tools to actually analyse and dump the system.

In my specific case I used `wget` on the device and a local *Python* webserver on my machine to download my Busybox on the device (it’s important to note that a reboot will delete the file), and then used `dd` to download a...