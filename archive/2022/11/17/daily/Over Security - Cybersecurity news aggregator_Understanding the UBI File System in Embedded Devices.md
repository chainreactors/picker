---
title: Understanding the UBI File System in Embedded Devices
url: https://serhack.me/articles/understanding-ubi-file-system-embedded-devices-reolink/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-17
fetch_date: 2025-10-03T23:01:50.890620
---

# Understanding the UBI File System in Embedded Devices

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/understanding-ubi-file-system-embedded-devices-reolink/ "en version")
[IT](https://serhack.me/it/articles/ubi-filesystem-reolink-firmware-dispositivi-embedded/ "it version")

# Understanding the UBI File System in Embedded Devices

Published at November 16, 2022 – 11 min read – 2300 words

![UBI file system reolink](https://serhack.me/images/articles/reolink-firmware/reolink_4_800px.jpg)

In [Part 3](https://serhack.me/articles/dissecting-reolink-rlc810a-hardware-detailed-view/) of our series, we explored the hardware device elements of the Reolink RLC-810A ― focusing on the NAND memory. We continue with Part 4 of our exploration into an IP camera firmware through introducing the concept of a file system. Furthermore, we will explore the technical reasons for choosing the UBI File System (UBIFS), a file system used especially for a category of mass storage, and we will unpack the UBIFS part using the `ubi-extract` tool.

## An Introduction to File Systems

Once the booting phase has been introduced, we need to understand which components detected by Binwalk can be useful for our investigation and which cannot. From [Part 1](https://serhack.me/articles/introduction-firmware-analysis-ip-camera-reolink/), we have seen that Binwalk shows a number of results. In particular, we are interested in the kernel image and the file system image.

Empirically, we can see that within the image that Reolink provides to its customers, there is a part dedicated to the UBI file system. It is imperative to understand the peculiarities of this file system in order to get to the bottom of the design choices.

Let’s begin by explaining what a file system is. All information processed by an electronic device can be divided into two categories: volatile information (when the device is switched off, it is lost) and non-volatile information. Depending on the mass storage used, non-volatile information (which remains even in the absence of electrical power) can be stored sequentially or randomly. Put another way, content can be written and read in multiple ways: sequentially (the file is memorized bit by bit) or randomly (pieces of file are placed in random places). Additionally, the operation of reading and writing can be executed by laser or by magnetic heads. In short, there are many different technologies to make a piece of data fixed.

At a high-level, however, we find a set of abstractions common among all memory types: the concept of files, write operations, read operations, creation of new files, and many other operations. Between this set of abstractions and the low-level controllers that only deal with input/output operations, there is a particular architectural layer called the file system that organizes information logically, structuring it into files and folders.

Conceptually, among all devices, there is no distinction between files. A file within a computer has the same logical structure as another file located, for example, within a mobile phone. This is always the case if both devices use the same file system. However, it does not matter where the devices write the contents of the files ― whether on two different media (computer on hard-disk and mobile phone on microSD) or on the same type. The abstraction that a file system provides is very powerful, since no process ever has to interface with low-level controllers.

The tasks of a file system are innumerable and range from managing physical space (how I allocate space for a file: whether contiguous or fragmented) to managing metadata (e.g., file name, size, permissions and various attributes). Maintaining the integrity of the content, file security, and the most trivial write and read operations ― all those characteristics are implemented through a file system.

Choosing a file system has a great influence on the performance of the operating system and on the management of free space. It is very important to get the choice of file system right with respect to requirements (type of media you are writing to, design limitations, etc.) because otherwise you risk having an underperforming operating system or even damaging the storage medium.

For example, just think of the unique feature of the Apple File System (APFS) which, when copying a folder, does not perform the operation on the total content. Rather, it creates a link to the original folder and stores only the differences between the original folder and the newly copied folder on the medium. This technique is called [Delta extents](https://en.wikipedia.org/wiki/Delta_encoding) and saves a lot of space!

### MicroSD and NAND flash memory

Another clear example of where the choice of a file system is critical is present in this investigation: we have an IP camera running an operating system from a microSD. This being the case, let’s highlight the technological features. Compared to media such as magnetic disks, microSDs are based on NAND flash technology ― an electronic memory medium that can be erased and reprogrammed (using low-level NAND ports that retain information).

To better understand the advantages of file systems, we need to introduce a couple of concepts related to how flash memory works.

Each flash memory uses a process called “program/erase” to store data. Without getting too much into detail, there are three main limitations of this memory:

* **Block Deletion**: I can act with read and write operations in an almost surgical manner; however, to delete an entire file, I am forced to delete the entire block. If there are N files within a block, I have to perform multiple operations to delete even a single file.
* **Limited Write Cycles**: Each flash memory has a limited number of write cycles, usually this value is close to 100,000. Above this average value, there is a risk that write operations are not as effective as they should be. The data I am writing, although correct at first, may become incorrect when writing to memory.
* **Contiguous Data Disturbance**: The method of reading NAND flash memory can cause cells close to the block I am reading to change state (from 0 to 1 or vice versa). To avoid this disturbance (also known as read disturbance), certain file system-side actions can be taken, such as keeping track of how many reads I have taken.

These problems are common to all media that use flash memory technology. In addition, from a physical point of view, a microSD is very small (15×11×1 millimeters). This means that a short circuit or high temperature could have disastrous consequences, as you are operating on a very small contact surface compared to an SSD.

### UBI File system

Due to the peculiarities of flash technology, it is best to prefer a specific file system that can communicate with the controller for error correction and wear leveling. The UBI file system is a perfect example of a file system that elegantly handles all the above mentioned problems.

Developed by Nokia and the University of Szeged (Hungary) in early 2008, UBIFS is a file system designed specifically for unmanaged flash memory devices. It has two main purposes:

* to track damaged blocks of flash memory, so that it can no longer rewrite into and/or read from a damaged block and thus prevent error propagation; and
* to provide wear leveling ― not concentrating all operations in one part of physical memory, but distributing the erasures and writes over the entire flash device.

#### Flash Translation Layer

To be more technically correct, not all file systems act at the same level. Between the part closest to the hardware and the high-level part, there are a number of secondary file systems that handle specific tasks such as the organization of blocks, the partitioning of blocks within m...