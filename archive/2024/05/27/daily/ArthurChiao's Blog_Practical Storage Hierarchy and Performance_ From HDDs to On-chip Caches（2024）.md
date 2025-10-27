---
title: Practical Storage Hierarchy and Performance: From HDDs to On-chip Caches（2024）
url: https://arthurchiao.github.io/blog/practical-storage-hierarchy/
source: ArthurChiao's Blog
date: 2024-05-27
fetch_date: 2025-10-06T16:49:17.964182
---

# Practical Storage Hierarchy and Performance: From HDDs to On-chip Caches（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# Practical Storage Hierarchy and Performance: From HDDs to On-chip Caches（2024）

Published at 2024-05-26 | Last Update 2024-05-28

This post summarizes bandwidths for local storage media, networking
infra, as well as remote storage systems. Readers may find this helpful when
**`identifying bottlenecks in IO-intensive applications`**
(e.g. AI training and LLM inference).

![](/assets/img/practical-storage-hierarchy/storage-bandwidth-3.png)

Fig. Peak bandwidth of storage media, networking, and distributed storage solutions.

Note: this post may contain inaccurate and/or stale information.

---

* [1 Fundamentals](#1-fundamentals)
  + [1.1 SATA](#11-sata)
    - [1.1.2 Real world pictures](#112-real-world-pictures)
    - [1.1.1 Revisions and data rates](#111-revisions-and-data-rates)
  + [1.2 PCIe](#12-pcie)
    - [1.1.2 Real world pictures](#112-real-world-pictures-1)
    - [1.2.2 Generations and data rates](#122-generations-and-data-rates)
  + [1.3 Summary](#13-summary)
* [2 Disk](#2-disk)
  + [2.1 HDD: **`~200 MB/s`**](#21-hdd-200-mbs)
    - [2.1.1 Real world pictures](#211-real-world-pictures)
    - [2.1.2 Supported interfaces (bus types)](#212-supported-interfaces-bus-types)
    - [2.1.3 Bandwidth: constrained by **`machanical factors`**](#213-bandwidth-constrained-by-machanical-factors)
    - [2.1.4 Typical latencies](#214-typical-latencies)
  + [2.2 SATA SSD: **`~600MB/s`**](#22-sata-ssd-600mbs)
    - [2.2.1 Real world pictures](#221-real-world-pictures)
    - [2.2.2 Bandwidth: constrained by **`SATA bus`**](#222-bandwidth-constrained-by-sata-bus)
  + [2.3 NVME SSD: **`~7GB/s, ~13GB/s`**](#23-nvme-ssd-7gbs-13gbs)
    - [2.3.1 Real world pictures](#231-real-world-pictures)
    - [2.3.2 Bandwidth: contrained by **`PCIe bus`**](#232-bandwidth-contrained-by-pcie-bus)
  + [2.4 Summary](#24-summary)
* [3 DDR SDRAM (CPU Memory): **`~400GB/s`**](#3-ddr-sdram-cpu-memory-400gbs)
  + [3.1 Real world pictures](#31-real-world-pictures)
  + [3.2 Bandwidth: contrained by **`memory clock, bus width, channel`**, etc](#32-bandwidth-contrained-by-memory-clock-bus-width-channel-etc)
  + [3.3 Summary](#33-summary)
* [4 GDDR SDRAM (GPU Memory): **`~1000GB/s`**](#4-gddr-sdram-gpu-memory-1000gbs)
  + [4.1 GDDR vs. DDR](#41-gddr-vs-ddr)
  + [4.2 Real world pictures](#42-real-world-pictures)
  + [4.3 Bandwidth: contrained by **`lanes & clock rates`**](#43-bandwidth-contrained-by-lanes--clock-rates)
  + [4.4 Summary](#44-summary)
* [5 HBM: **`1~5 TB/s`**](#5-hbm-15-tbs)
  + [5.1 What’s new](#51-whats-new)
  + [5.2 Real world pictures](#52-real-world-pictures)
  + [5.3 Bandwidth: contrained by **`lanes & clock rates`**](#53-bandwidth-contrained-by-lanes--clock-rates)
  + [5.4 HBM-powered CPUs](#54-hbm-powered-cpus)
  + [5.5 Summary](#55-summary)
* [6 SRAM (on-chip): **`20+ TB/s`**](#6-sram-on-chip-20-tbs)
  + [6.1 SRAM vs. DRAM](#61-sram-vs-dram)
  + [6.2 Cache hierarchy (L1/L2/L3/…)](#62-cache-hierarchy-l1l2l3)
  + [6.3 **`Groq LPU`**: eliminating memory bottleneck by using SRAM as main memory](#63-groq-lpu-eliminating-memory-bottleneck-by-using-sram-as-main-memory)
  + [6.4 Bandwidth: contrained by **`clock rates`**, etc](#64-bandwidth-contrained-by-clock-rates-etc)
  + [6.5 Summary](#65-summary)
* [7 Networking bandwidth: **`400GB/s`**](#7-networking-bandwidth-400gbs)
  + [7.1 Traditional data center: `2*{25,100,200}Gbps`](#71-traditional-data-center-225100200gbps)
  + [7.2 AI data center: GPU-interconnect: `8*{100,400}Gbps`](#72-ai-data-center-gpu-interconnect-8100400gbps)
  + [7.3 Networking bandwidths](#73-networking-bandwidths)
  + [7.4 Summary](#74-summary)
* [8 Distributed storage: aggregated **`2+ TB/s`**](#8-distributed-storage-aggregated-2-tbs)
  + [8.1 AlibabaCloud CPFS](#81-alibabacloud-cpfs)
  + [8.2 NVME SSD powered Ceph clusters](#82-nvme-ssd-powered-ceph-clusters)
  + [8.3 Summary](#83-summary)
* [9 Conclusion](#9-conclusion)
* [References](#references)

---

# 1 Fundamentals

Before delving into the specifics of storage, let’s first go through some
fundamentals about data transfer protocols.

## 1.1 SATA

From wikepedia [SATA](https://en.wikipedia.org/wiki/SATA):

> SATA (**`Serial AT Attachment`**) is a
> computer **`bus interface`** that connects host bus
> adapters to mass storage devices such as hard disk drives, optical drives,
> and solid-state drives.

### 1.1.2 Real world pictures

![](/assets/img/practical-storage-hierarchy/SATA2-pic.jpg)

Fig. SATA interfaces and cables on a computer motherboard. Image source [wikipedia](https://en.wikipedia.org/wiki/SATA)

### 1.1.1 Revisions and data rates

The SATA standard has evolved through multiple revisions.
The current prevalent revision is 3.0, offering a maximum IO bandwidth of **`600MB/s`**:

Table: SATA revisions. Data source: [wikipedia](https://en.wikipedia.org/wiki/SATA)

| Spec | Raw data rate | Data rate | Max cable length |
| --- | --- | --- | --- |
| SATA Express | 16 Gbit/s | 1.97 GB/s | 1m |
| SATA revision 3.0 | 6 Gbit/s | **`600 MB/s`** | 1m |
| SATA revision 2.0 | 3 Gbit/s | 300 MB/s | 1m |
| SATA revision 1.0 | 1.5 Gbit/s | 150 MB/s | 1m |

## 1.2 PCIe

From wikipedia [PCIe (PCI Express)](https://en.wikipedia.org/wiki/PCI_Express):

> PCI Express is high-speed serial computer expansion bus standard.

PCIe (**`Peripheral Component Interconnect Express`**)
is another kind of system bus, designed to connect a variety of peripheral
devices, including **`GPUs, NICs, sound cards`**,
and certain storage devices.

### 1.1.2 Real world pictures

![](/assets/img/practical-storage-hierarchy/pcie-pic.jpg)

Fig.
Various slots on a computer motherboard, from top to bottom:
PCIe x4 (e.g. for NVME SSD)
PCIe x16 (e.g. for GPU card)
PCIe x1
PCIe x16
Conventional PCI (32-bit, 5 V)
Image source [wikipedia](https://en.wikipedia.org/wiki/PCI_Express)

As shown in the above picture,
PCIe electrical interface is measured by the number of **`lanes`**.
A lane is a **`single data send+receive line`**,
functioning similarly to a “one-lane road” with traffic in **`both directions`**.

### 1.2.2 Generations and data rates

Each new PCIe generation doubles the bandwidth of a lane than the previous generation:

Table: PCIe Unidirectional Bandwidth.
Data source: [trentonsystems.com](https://www.trentonsystems.com/en-us/resource-hub/blog/pcie-gen4-vs-gen3-slots-speeds)

| Generation | Year of Release | Data Transfer Rate | Bandwidth x1 | Bandwidth x16 |
| --- | --- | --- | --- | --- |
| PCIe 1.0 | 2003 | 2.5 GT/s | 250 MB/s | 4.0 GB/s |
| PCIe 2.0 | 2007 | 5.0 GT/s | 500 MB/s | 8.0 GB/s |
| PCIe 3.0 | 2010 | 8.0 GT/s | 1 GB/s | 16 GB/s |
| PCIe 4.0 | 2017 | 16 GT/s | 2 GB/s | **`32 GB/s`** |
| PCIe 5.0 | 2019 | 32 GT/s | 4 GB/s | **`64 GB/s`** |
| PCIe 6.0 | 2021 | 64 GT/s | 8 GB/s | 128 GB/s |

Currently, the most widely used generations are **`Gen4 and Gen5`**.

Note: Depending on the document you’re referencing, PCIe bandwidth may be presented
as **`either unidirectional or bidirectional`**,
with the latter indicating a bandwidth that is twice that of the former.

## 1.3 Summary

With the above knowledge, we can now proceed to discuss the
performance characteristics of various storage devices.

# 2 Disk

## 2.1 HDD: **`~200 MB/s`**

From wikipedia [HDD](https://en.wikipedia.org/wiki/Hard_disk_drive):

> A hard disk drive (HDD) is an **`electro-mechanical`**
> data storage device that stores and retrieves digital data using
> **`magnetic storage`** with one or more rigid
> **`rapidly rotating platters`** coated with magnetic material.

### 2.1.1 Real world pictures

A real-world picture is shown below:

![](/assets/img/practical-storage-hierarchy/hdd-internal.jpg)

Fig. Internals of a real world HDD. Image source [hardwaresecrets.com](https://hardwaresecrets.com/anatomy-of-a-hard-disk-drive/)

### 2.1.2 Supported...