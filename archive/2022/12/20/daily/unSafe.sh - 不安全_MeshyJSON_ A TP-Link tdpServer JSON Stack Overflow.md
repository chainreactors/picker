---
title: MeshyJSON: A TP-Link tdpServer JSON Stack Overflow
url: https://buaq.net/go-140622.html
source: unSafe.sh - 不安全
date: 2022-12-20
fetch_date: 2025-10-04T01:58:02.462703
---

# MeshyJSON: A TP-Link tdpServer JSON Stack Overflow

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/058b5f4ad0a08826ae98d025aa51582b.jpg)

MeshyJSON: A TP-Link tdpServer JSON Stack Overflow

SummaryTarget BinarytdpServerArchitecture &MitigationsForksUnderstanding TheVulnerabi
*2022-12-19 19:50:39
Author: [research.nccgroup.com(查看原文)](/jump-140622.htm)
阅读量:25
收藏*

---

* [Summary](#summary)
* [Target Binary](#target-binary)
  + [tdpServer](#tdpserver)
  + [Architecture &
    Mitigations](#architecture-mitigations)
  + [Forks](#forks)
* [Understanding The
  Vulnerability](#understanding-the-vulnerability)
  + [Reaching The Vulnerable
    Function](#reaching-the-vulnerable-function)
    - [Broadcast Fork Flow](#broadcast-fork-flow)
    - [Server Fork Flow](#server-fork-flow)
  + [JSON Array Stack
    Overflow](#json-array-stack-overflow)
* [Triggering The Bug](#triggering-the-bug)
  + [Broadcast Fork Response](#broadcast-fork-response)
  + [Server Fork Request](#server-fork-request)
* [Vulnerability
  Constraints](#vulnerability-constraints)
* [Storing Arbitrary
  Content In Memory](#storing-arbitrary-content-in-memory)
  + [cJSON Summarized](#cjson-summarized)
    - [cJSON Struct](#cjson-struct)
    - [cJSON Data](#cjson-data)
    - [cJSON Heap Memory](#cjson-heap-memory)
      * [Single cJSON](#single-cjson)
      * [cJSON structure and
        key/value elements](#cjson-structure-and-keyvalue-elements)
  + [cJSON Object Memory
    Leak](#cjson-object-memory-leak)
  + [Heap](#heap)
    - [Chunk](#chunk)
    - [Bin](#bin)
    - [Mal](#mal)
  + [Bypassing Heap ASLR](#bypassing-heap-aslr)
* [Virtualized Heap (VHeap)
  Grooming](#virtualized-heap-vheap-grooming)
  + [Dumping The Initial
    State](#dumping-the-initial-state)
  + [Tracking The Current
    State](#tracking-the-current-state)
  + [VHeap Commands](#vheap-commands)
  + [Dynamic Spray
    Generation](#dynamic-spray-generation)
* [Exploitation](#exploitation)
  + [Crashing the
    Broadcast Fork to Avoid Noise](#crashing-the-broadcast-fork-to-avoid-noise)
  + [Hole Filling](#hole-filling)
  + [Faking
    onemeshSupportVersionArray](#faking-onemeshsupportversionarray)
  + [Stack Variable
    Overwrites](#stack-variable-overwrites)
  + [Triggering the Stack
    Overflow](#triggering-the-stack-overflow)
  + [Sprayed cJSON Arrays](#sprayed-cjson-arrays)
  + [Executing an Arbitrary
    Command](#executing-an-arbitrary-command)
* [Final notes](#final-notes)
  + [Further
    Payload Generation VHeap Requirements](#further-payload-generation-vheap-requirements)
  + [Reliability /
    Limitations](#reliability-limitations)
  + [Patch](#patch)
  + [Pwn2Own Note](#pwn2own-note)

This blog post describes a vulnerability found and exploited in
November 2022 by NCC Group. The target was the TP-Link AX1800 WiFi 6
Router (Archer AX21). It was running hardware version 3.6 and firmware
version 1.1.1 (Archer AX21(US)\_V3.6\_1.1.1 Build 20220603). The
vulnerability was patched on 2nd of December 2022 with firmware version
1.1.3 (Archer AX21(US)\_V3.6\_1.1.3 Build 20221125).

The firmware files are accessible via the following links:

* [Archer
  AX21(US)\_V3.6\_1.1.1 Build 20220603 (zip)](https://static.tp-link.com/upload/firmware/2022/202208/20220802/Archer%20AX21%28US%29_V3_220603.zip)
* [Archer
  AX21(US)\_V3.6\_1.1.3 Build 20221125 (zip)](https://static.tp-link.com/upload/firmware/2022/202212/20221202/Archer%20AX21%28US%29_V3_221125.zip)

## tdpServer

The vulnerability detailed in this post exists in the
`tdpServer` binary. This binary sends a probe broadcast
request out every 30 seconds, and additionally recieves requests on LAN
20002/udp. Our understanding is that this proprietary TDP protocol is a
part of [TP-Link’s Mesh
Wi-Fi](https://www.tp-link.com/uk/mesh-wifi/) technology.

Various vulnerabilities have previously been found in this binary
which detail how the TDP protocol works:

* [Exploiting
  the TP-Link Archer A7 at Pwn2Own Tokyo](https://www.thezdi.com/blog/2020/4/6/exploiting-the-tp-link-archer-c7-at-pwn2own-tokyo)
* [TP-Link
  AC1750 (Pwn2Own 2019)](https://labs.f-secure.com/advisories/tp-link-ac1750-pwn2own-2019/)
* [Pwn2Own
  Tokyo 2020: Defeating the TP-Link AC1750](https://www.synacktiv.com/en/publications/pwn2own-tokyo-2020-defeating-the-tp-link-ac1750.html)

To summarise, a TDP packet contains a 0x10-byte header with
information about the request type and body. The body is encrypted with
either AES-128 CBC or XOR, depending on the header type and opcode. Both
encryption algorithms use a hard-coded key which can be retrieved from
the binary. It means we can decrypt existing packets and craft our own
packets. The decrypted body format is a JSON string containing the
request or response parameters. The structure of the TDP network packet
is as follows:

```
struct TdpPacket
{
    uint8_t version;     // 0x00
    uint8_t type;        // 0x01
    uint16_t opcode;     // 0x02
    uint16_t length;     // 0x04
    uint8_t flags;       // 0x06
    uint8_t align;       // 0x07
    uint32_t sn;         // 0x08
    uint32_t checkSum;   // 0x0C - last header's field
    uint8_t body[0x400]; // 0x10
}; // 0x410
```

## Architecture & Mitigations

Checking the mitigations of `tdpServer` using [checksec.py](https://github.com/Wenzel/checksec.py):

```
[*] '/usr/bin/tdpServer'
    Arch:     arm-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x10000)
```

Checking the Address Space Layout Randomization (ASLR) settings of
the kernel:

```
/ # cat /proc/sys/kernel/randomize_va_space
2
```

The [Oracle
Linux Address Space Layout Randomization](https://docs.oracle.com/cd/E37670_01/E36387/html/ol_aslr_sec.html) docs state the following
value meanings:

* 0 – Disable ASLR. This setting is applied if the kernel is booted
  with the `norandmaps` boot parameter.
* 1 – Randomize the positions of the stack, virtual dynamic shared
  object (VDSO) page, and shared memory regions. The base address of the
  data segment is located immediately after the end of the executable code
  segment.
* 2 – Randomize the positions of the stack, VDSO page, shared memory
  regions, and the data segment. This is the default setting.

To summarize:

* Architecture: ARM 32-bit (Little Endian)
* `tdpServer`: not randomized, no stack canary
  + `.text`: `r-x`
  + `.data`: `rw-`
* Libraries: randomized
* Heap: randomized, `rw-`
* Stack: randomized, `rw-`

## Forks

The `tdpServer` binary calls the `fork` system
call twice during the main method which separates the process into the
main process and two child processes:

* The first process is responsible for sending a network broadcast
  probe request on port 20002/udp every 30 seconds. This process can
  receive a probe response after the probe request is sent to the
  broadcast address. This process will be called the “broadcast fork” in
  this blog.
* The second process acts as a server and starts the 20002/udp port
  listener to receive requests from any client. This process can receive a
  probe request as well as all other types of requests. This fork will be
  called the “server fork” in this blog.

The final process is not required as part of this exploit and
therefore can be ignored.

## Reaching The Vulnerable Function

The vulnerability occurs within the `processProbePacket`
(`0x00029360`) function which can be reached from two
different network flows. One network flow can be triggered immediately
by sending a “probe” packet to the server fork. The other network flow
can be triggered by responding to a probe broadcast request (sent by the
broadcast fork) with a “probe\_response” packet.

### Broadcast Fork Flow

The `main` (`0x00024c7c`)...