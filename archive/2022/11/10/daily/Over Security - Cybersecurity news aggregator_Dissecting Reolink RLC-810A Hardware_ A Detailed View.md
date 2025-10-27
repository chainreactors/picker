---
title: Dissecting Reolink RLC-810A Hardware: A Detailed View
url: https://serhack.me/articles/dissecting-reolink-rlc810a-hardware-detailed-view/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-10
fetch_date: 2025-10-03T22:16:36.997260
---

# Dissecting Reolink RLC-810A Hardware: A Detailed View

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/dissecting-reolink-rlc810a-hardware-detailed-view/ "en version")
[IT](https://serhack.me/it/articles/analisi-esplorare-hardware-reolink-rlc-810-a/ "it version")

# Dissecting Reolink RLC-810A Hardware: A Detailed View

Published at November 9, 2022 – 17 min read – 3558 words

![Hardware of an IP camera Reolink RLC-810-A](https://serhack.me/images/articles/reolink-firmware/reolink_3_800px.jpg)

Now that we know [how device booting works](https://serhack.me/articles/os-embedded-booting-phase-uboot/), let’s try to extract some parts from the firmware that we downloaded in [Part 1](https://serhack.me/articles/introduction-firmware-analysis-ip-camera-reolink/) of our series. Here, we are interested in two main sections: the Linux kernel (which takes care of booting the device services) and the flattened device tree (which allows the kernel to know the hardware configuration a priori without inspecting each device).

During the course of this article, we will also proceed as hardware manufacturers and, with a critical eye, comment on each choice made by the manufacturer.

## Extracting Image with dd

To begin, we will try to do a manual extraction using the `dd` tool and the result obtained from an analysis with Binwalk. From there, we will use the tools already provided with Binwalk.

The `dd` tool is part of a set of utilities already provided on Linux for copying the contents of a file verbatim by specifying the offset. `dd` can duplicate data from files, various devices, partitions, and volumes. Its syntax is simple enough to understand:

```
dd if=input_file of=output_file bs=1 skip=offset count=how_many_blocks
```

We identify which of the parts from the previous result we want to use. Specifically, we want both the flattened device tree and the initial Linux executable:

```
34600         0x8728          Flattened device tree, size: 17375 bytes, version: 17
624319        0x986BF         uImage header, header size: 64 bytes, header CRC: 0x7B9F6E31, created: 2021-06-19 06:29:15, image size: 3153472 bytes, Data Address: 0x8000, Entry Point: 0x8000, data CRC: 0xD7FC213, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: none, image name: "Linux-4.19.91"
```

Let’s remember what data we are interested in: the offset (at the beginning of the line) and the size of the file we are going to extract (image size). We also specify the unit of measurement (i.e. 1 byte `bs=1`). The command to extract the kernel image will be:

```
dd if=firmware_rlc_810_a.pak of=linux_image bs=1 skip=624319 count=3153472
```

Another simple command (`file linux_image`) will show confirmation of the extraction:

```
linux_image: u-boot legacy uImage, Linux-4.19.91, Linux/ARM, OS Kernel Image (Not compressed), 3153472 bytes, Sat Jun 19 06:29:15 2021, Load Address: 0X008000, Entry Point: 0X008000, Header CRC: 0X7B9F6E31, Data CRC: 0XD7FC213
```

Whereas, the one for the flattened device tree is:

```
dd if=firmware_rlc_810_a.pak of=device_tree bs=1 skip=34600 count=17375
```

Again, the `file device_tree` confirms successful extraction:

```
device_tree: Device Tree Blob version 17, size=17375, boot CPU=0, string block size=1495, DT structure block size=15824
```

A careful reader might wonder whether it was worthwhile to tackle this manual analysis section instead of running Binwalk. It turns out, however, that manual analysis is exactly what Binwalk does. Simply put, it analyzes the raw bytes and if it finds a match with a particular signature, it tries to unpack the header file. If the data is valid, then it tries to extract the image from the analyzed file.

## Flattened Device Tree of Reolink

Before continuing with the more serious analysis using Binwalk, it is useful to explain the flattened device tree file format, which allows the operating system to know in advance the hardware devices that are present within the embedded system.

In general-purpose environments, when the operating system is loaded into memory, it proceeds to inspect all connected devices to populate a table indicating the information of each device. For example, what should the operating system do when the keyboard is running? Or when the mouse is moving?

In order to match a real action to a virtual (input) event, the operating system tracks all devices so that it knows how to handle any event from the hardware devices. It must also know how to transfer virtual events into physical actions for output. In order to avoid having to query every single hardware device every time at start-up, we can take two approaches: one is to write the individual devices to be loaded directly into the code and the other is to read the various configurations from a file in the file system. Both approaches do not seem to be the right way: the former inevitably suffers from problems (How can we dynamically configure a device?) while the latter may be slow (the operating system should at least know the device to read from).

The solution lies somewhere in between the two approaches seen in the previous paragraph: the **flattened device tree**, a section specifying the board’s set of devices. This section is loaded immediately at boot time and allows the operating system to understand which drivers to load and which not to load. The operating system only needs to check the status of the devices, instead of inspecting each hardware controller.

We then proceed to analyze the flattened device tree. Once extracted, we can view its contents using a tool called the `device-tree-compiler`. From there, we install the package and proceed to explore the ReoLink camera hardware:

```
dtc -I dtb -O dts -o - device_tree
```

The flags specify what file format to use ― in input `DTB` (Device Tree Blob) and in output DTS (Device Tree Source). A very useful guide to the `device-tree-compiler` can be found at [git.kernel.org](https://git.kernel.org/pub/scm/utils/dtc/dtc.git/plain/Documentation/manual.txt?id=HEAD). The complete file can instead be found at [Github](https://gist.github.com/serhack/0daade875651f2f50d11fc4641aaf3b1).

So let’s begin by inspecting the hardware of the Reolink RLC-810A IP camera. What follows is a fairly technical overview, as it would take many articles to fully explain each device in detail. I suggest that you dwell and delve into what you are interested in.

Each device tree starts with some specification of the type of board or system-on-a-chip used. These files are produced by the manufacturer of the board on which the system is built, so they can be useful to understand what kind of hardware has been placed inside the product.

```
model = "Novatek NA51055";
compatible = "novatek,na51055\0nvt,ca9";
```

The `model` field reports a rather popular Taiwanese company named Novatek Microelectronics Corp that designs and manufactures integrated circuits. The board is called NA51055 and appears to be a variant of the more commercially known NT9852x model. Through a Google search, the board seems to have been used not only for Reolink, but also for some dashcams of the company [Viofo](https://viofo.com). It is indeed not uncommon for one type of board to be used by more than one company, since many embedded devices are similar in functionality (whether it be a dashcam or camera, it only changes what to record).

After this brief specification, all hardware devices on the board are summarized. Each device follows a precise pattern; although, not all parameters are always specified:

```
device_name {
	reg = // registers value
	interrupts = // interrupts to which the device responds
	compatible = // string allowing the kernel to identify the device driver capable of handling the device
	clock = // reference to the clock used by the d...