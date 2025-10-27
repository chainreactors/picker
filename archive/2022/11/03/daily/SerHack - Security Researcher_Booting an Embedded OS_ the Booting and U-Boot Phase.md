---
title: Booting an Embedded OS: the Booting and U-Boot Phase
url: https://serhack.me/articles/os-embedded-booting-phase-uboot/
source: SerHack - Security Researcher
date: 2022-11-03
fetch_date: 2025-10-03T21:41:36.755420
---

# Booting an Embedded OS: the Booting and U-Boot Phase

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/os-embedded-booting-phase-uboot/ "en version")
[IT](https://serhack.me/it/articles/avvio-di-os-embedded-booting-fase-uboot/ "it version")

# Booting an Embedded OS: the Booting and U-Boot Phase

Published at November 2, 2022 – 12 min read – 2372 words

![Telecamera IP con U-Boot](https://serhack.me/images/articles/reolink-firmware/reolink_2_800px.jpg)

[In the first post](https://serhack.me/articles/introduction-firmware-analysis-ip-camera-reolink/), we introduced embedded devices and started to scour through and extract information from Reolink IP camera firmware. At the end of the post, we ran Binwalk, which showed various types of files such as Flattened Device Tree, uImage Header, and UBI File System.

For the second article in this [Reolink](https://serhack.me/tags/reolink/) series, we are going to introduce the theory regarding the various stages of booting the operating system and explore the different types of files. So, let’s begin our analysis.

## Booting

The [booting phase](https://it.wikipedia.org/wiki/Boot) (i.e., loading) constitutes a critical phase of our operating system. When we turn on any device, be it a TV or a general-purpose computer, the system must execute a series of routines to load modules and executables that will be needed later to continue executing other tasks. Network management, routines to load executables ― these are all services that ensure the stability of the operating system and, therefore, are essential to start using the device.

Just before starting the operating system, all devices are in a reset state. The RAM interior is empty and I/O devices are ready to be called and executed. As soon as the power button is pressed, however, this is when a series of actions are performed by the device(s) to load the OS.

Each time a device is turned on, execution starts from a module called read-only memory (ROM), provided by the manufacturer, which takes care of some tests and starts loading the operating system. Once it is loaded, control passes to the operating system, which has full authority to create, modify, and delete any data structure and value in the CPU, memory, and I/O devices. The bootloader is also responsible for running a series of tests (such as the [Power On Self Test](https://it.wikipedia.org/wiki/Power-on_self-test)) to check whether everything is actually working at the hardware level. Tests include low-level checks (e.g., voltage or circuitry) to see whether or not the ROM can proceed with the actual boot.

Without going into too much technical detail, we can think of the ROM or bootloader as a program. The bootloader is executed by the CPU, which loads a number of other components of the operating system. With embedded devices, consisting of a specific board (thus, a particular hardware configuration), we can optimize the booting of the operating system. The *bootstrap* (i.e., the loading phase) must be very fast and must require as few resources as possible to avoid wasting power. A core requirement that the development of embedded-based designs must consider is time. Since these devices interface and are used in a real-world context, the response time must be very short ― from microseconds to tens of nanoseconds.

## U-Boot

Most embedded operating systems use [U-Boot](https://www.denx.de/wiki/U-Boot/) (also called Das U-Boot, from a pun based on the classic 1981 movie [Das Boot](https://en.wikipedia.org/wiki/Das_Boot), set on a German submarine) as their booloader. Written primarily in C and Assembly, U-Boot is an open-source project developed by Magnus Damm, considered to this day to be the richest, most flexible and most actively developed bootloader. It supports various architectures such as ARM, MicroBlaze, MIPS, PPC, RISC-V, x86, and also contains some drivers for embedded device development boards. It is used by a wide number of devices made by Nintendo, along with Chromebooks, Raspberry PI, and not to mention automotive boards.

U-Boot supports FAT, ext2/3/4, CramFS, SquashFS, JFFS2, UBIF, ZFS, and many others as file systems. This mainly means that U-Boot is very powerful ― supporting both different hardware configurations and multiple operating systems. The bootloader implements a subset of specifications compatible with UEFI systems and starts the operating system through a number of environment variables (one in particular, the most important, `bootargs`) that we will address later in this article.

U-Boot requires that commands specified on bootargs be low-level and, therefore, explicitly specify physical memory addresses as the destination for copying data. This, on the one hand, adds complexity for the developer who must know the technical details, but, on the other hand, allows for minimal *overhead* (i.e., overhead time).

Another feature that U-Boot supports is the Flattened Device Tree file, a data structure that is used to describe hardware configuration. In general-purpose devices, when the power button is pressed, the bootloader polls all the devices to get information about the manufacturer ― what kind of device it is, its state, and a lot of other information. In embedded devices, we cannot afford to waste valuable time! So, I include within my bootloader a device tree to allow the machine to already load all the information about my hardware. The device tree will be explored in depth during the third part of this series.

### Loading Phase

Having concluded the more technical part of U-Boot, let’s specify what happens during the loading of a unix-based operating system in the points below. To better describe the booting phase, let’s break it down into seven distinct points.

1. **Booting the device** and hardware routines that serve to stabilize the voltage inside the board:

   The CPU as well as many other devices within a board are controlled through electrical signals ― this current is generated by a potential. Once the circuit is turned on, this potential must be constant over time (or at least its fluctuations must remain minimal) to avoid damaging the circuit. The only concern for this phase is bringing electric current to each component. Components (such as the CPU) are in the reset state and ready to be used. If there are broken or damaged components (i.e., if the potential is not the standard one), the power-up will not continue.
2. **Performance of POST (*Power-On Self-Test*)**:

   This phase involves running a series of tests that verify hardware integrity before proceeding to the next phase. In the event that this test fails, the machine will not power-on and show no signs of life.
3. **Hardware device initialization**:

   Once the tests are done, device controllers such as static random access memory (SRAM), serial ports, and the interrupt service table are initialized. When a CPU starts up, it performs some internal consistency checks and transfers control to a programmable read-only memory (PROM) or erasable programmable read-only memory (EPROM) device that contains non-volatile code (which is intended to survive a power loss). Everything is ready to load the first booting stage.
4. **Loading the minimal bootloader (first part)**:

   Reading a set of routines from the ROM that initializes a RAM internal to the chip. This step allows you to use the minimal bootloader, which will read our device and load the second part of the bootloader. Once the procedure is done, the CPU jumps to a predefined memory address to continue execution. Dynamic random access memory (DRAM, i.e., main RAM memory as we understand it) is prepared, filling the entire area of uninitialized data with zeros. It allocates space for the stack and initializes registers (such as the stack pointer).
5. **Reading t...