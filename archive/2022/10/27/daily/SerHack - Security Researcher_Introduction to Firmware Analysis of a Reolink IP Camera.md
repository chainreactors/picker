---
title: Introduction to Firmware Analysis of a Reolink IP Camera
url: https://serhack.me/articles/introduction-firmware-analysis-ip-camera-reolink/
source: SerHack - Security Researcher
date: 2022-10-27
fetch_date: 2025-10-03T21:04:21.483595
---

# Introduction to Firmware Analysis of a Reolink IP Camera

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/introduction-firmware-analysis-ip-camera-reolink/ "en version")
[IT](https://serhack.me/it/articles/introduzione-analisi-firmware-telecamera-ip-reolink/ "it version")

# Introduction to Firmware Analysis of a Reolink IP Camera

Published at October 26, 2022 – 15 min read – 3004 words

![Introduction to Firmware Analysis of a Reolink IP Camera](https://serhack.me/images/articles/reolink-firmware/reolink_1_800px.jpg)

Embedded devices continue to increase in popularity and one category, in particular, that has become *en vogue* as of late is the Internet of Things (IoT). The emergence of these next generation technologies has driven the home automation evolution from simple light bulbs to cloud-connected printers, smart refrigerators, etc.

However, this evolution has some disadvantages: The perennial need to be connected to the Internet and an increase in the potential attack surface. Issues related (more broadly) to cybersecurity and (more specifically) your privacy are imperative to avoid, so that elements related to your private life are not exposed. For the time being, it appears that many IoT manufacturers simply ignore this.

In this series of articles, which will be published on a weekly basis, we will be taking an in-depth look at the technical functioning of an IP camera from the company [Reolink](https://reolink.com) ― in an effort to better understand the potential risks of an IoT device. Starting from higher level details, then onto the lowest level details, and then delving into the user interface, we will explain how the camera was created and developed. Now, let’s begin here by exploring an IP camera.

## Embedded Devices

To begin analyzing firmware, it is necessary to first introduce a few notions about embedded devices: *What are they?* and *Why have they been called that?*

We can identify two broad categories in everyday devices: Those that are designed for a specific purpose and those called general-purpose. As an example, devices that are designed for a specific purpose are household appliances, home automation, cameras, printers, heating systems, etc. In these examples, only one purpose can be identified ― in the case of a microwave oven, the device will only heat food and certainly not show a film.

In contrast, general-purpose devices, such as computers, mobile phones, and smartwatches are machines that can perform any kind of task ― from writing an email to watching a movie. Their purpose depends on what the user wants to do with them. One can develop projects, watch a film, compose music, and much more.

Generally, specific purpose devices have far fewer resources than what we expect from general-purpose devices. The main reason they have fewer resources available is that they are designed for a single purpose, so they only have one task to perform. The design of specific purpose devices is very critical and requires a lot of precision to avoid unnecessary expenditure of time and money.

Such devices are often called embedded devices because they are “immersed” in reality: They perform very specific jobs and tasks in a physical context. Let’s think, for example, of how many chips we could find in a house: air conditioning system, home automation to switch on/off a light bulb, burglar alarm system, household appliances, etc. Let’s now imagine a more complex environment, such as a car (control units, car radios) and industries (assembly line, sensors).

While all devices are based on the [Von Neumann Architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture), what actually varies and makes the difference is the type of architecture (16-bit/32-bit/64-bit and [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family)/MISP/Coldfire) and the available hardware resources. Furthermore, embedded devices do not work in isolation, as they are usually configured to work and perform a task that depends on information from other systems (like a heating controller controlling the heat pump).

For embedded device designers, the most complex challenges they face are working with limited resources and having to communicate with other systems in a standard way. In addition, there is another subtle problem that is overlooked and has only recently come to light.

At the end of the millennium, several people theorized about the application of Internet connectivity to embedded devices, calling the concept the “Internet Of Things”. Although wanting to be precise, in practice Internet-connected devices had already been developed in the early 1980s. One of the first embedded devices was a beverage dispensing machine ([*The “Only” Coke Machine on the Internet*](https://www.cs.cmu.edu/~coke/history_long.txt)), which was connected to the Internet at Carnegie Mellon University. Programmers would connect to the machine through the Internet to check if there was a beverage available.

Since the creation of the concept of the Internet of Things in the early 2000s, these devices have begun to spread ― first in an industrial setting and then into the homes of almost all of us. Thanks to extensive marketing campaigns, various embedded devices have entered our homes (alarms, printers, televisions, smart locks, etc.). However, it is not all “peaches and cream” as marketers would have us believe.

With the introduction of networking to embedded devices, several challenges have emerged and some are still being actively discussed today. Lack of security, short software lifecycle (with one update in five years), proprietary security protocols, and the mantra [“security by obscurity”](https://it.wikipedia.org/wiki/Sicurezza_tramite_segretezza) make IoT devices a target for attackers trying to break into an infrastructure. In addition, dependence on the manufacturer is a point of centralization that could potentially be a problem, especially when the manufacturer ceases to exist. Technical problems at data centers, proprietary servers, and infrastructure can also negatively impact an IoT experience. Isn’t it just wonderful to not be able to access your device because [AWS](https://it.wikipedia.org/wiki/Amazon_Web_Services) is momentarily down in your area?

Let’s point out that the Internet of Things category is a subcategory of embedded devices ― not all devices we see around the house are connected to the Internet (fortunately). However, this is not the case with [Reolink’s](https://reolink.com/) IP camera.

## Structure of the Article Series

Here is the timeline for the upcoming articles in this series. Our goal would be releasing one article per week on Wednesday. We have tried to divide the topics to be addressed into different sections:

* Part 1: [**Introduction to Firmware Analysis**](https://serhack.me/articles/introduction-firmware-analysis-ip-camera-reolink/)
  + Embedded Devices
  + The Reolink IP Camera
  + Software Part
  + Analysis through Binwalk
* Part 2: [**Booting an Embedded OS**](https://serhack.me/articles/os-embedded-booting-phase-uboot/)
  + Booting Phase
  + U-Boot
  + Loading Phase
* Part 3: [**Hardware Devices of Reolink**](https://serhack.me/articles/dissecting-reolink-rlc810a-hardware-detailed-view/)
  + Image Extraction with DD
  + Flattened Device Tree
  + Reolink Hardware Devices
* Part 4: [**File System of an Embedded Device**](https://serhack.me/articles/understanding-ubi-file-system-embedded-devices-reolink/)
  + Introduction to the File System
  + UBI File System
* Part 5: [**The Operating System**](https://serhack.me/articles/operating-system-reolink-rlc-810-a/)
  + Buildroot and Busybox
  + Typical Paths of an Embedded Linux Distribution
  + Configuration Files
* Part 6: [**Techniques for Setting up Peripherals via DMA and PIO**](https://serhack....