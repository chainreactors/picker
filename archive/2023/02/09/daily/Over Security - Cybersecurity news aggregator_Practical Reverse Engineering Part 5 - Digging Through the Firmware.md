---
title: Practical Reverse Engineering Part 5 - Digging Through the Firmware
url: https://jcjc-dev.com/2016/12/14/reversing-huawei-5-reversing-firmware/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:09:14.655852
---

# Practical Reverse Engineering Part 5 - Digging Through the Firmware

# [Hack The World](https://jcjc-dev.com)

Projects and learnt lessons on Systems Security, Embedded Development, IoT and anything worth writing about

[Archive](/archive/)
[Consulting](/consulting/)
[Juan Carlos Jimenez](https://uk.linkedin.com/in/juan-carlos-jim%C3%A9nez-bba49033/en)
[Twitter](https://twitter.com/Palantir555)
[GitHub](https://github.com/Palantir555)
e-mail

# Practical Reverse Engineering Part 5 - Digging Through the Firmware

14 Dec 2016

* [Part 1](https://jcjc-dev.com/2016/04/08/reversing-huawei-router-1-find-uart/):
  Hunting for Debug Ports
* [Part 2](https://jcjc-dev.com/2016/04/29/reversing-huawei-router-2-scouting-firmware/):
  Scouting the Firmware
* [Part 3](https://jcjc-dev.com/2016/05/23/reversing-huawei-3-sniffing/):
  Following the Data
* [Part 4](https://jcjc-dev.com/2016/06/08/reversing-huawei-4-dumping-flash/):
  Dumping the Flash
* **Part 5**: Digging Through the Firmware

In part 4 we extracted the entire firmware from the router and decompressed it.
As I explained then, you can often get most of the firmware directly from
the manufacturer’s website: Firmware upgrade binaries often contain partial or
entire filesystems, or even entire firmwares.

In this post we’re gonna dig through the firmware to find potentially
interesting code, common vulnerabilities, etc.

I’m gonna explain some basic theory on the Linux architecture, disassembling
binaries, and other related concepts. Feel free to skip some of the parts
marked as [Theory]; the real hunt starts at ‘Looking for the Default WiFi
Password Generation Algorithm’. At the end of the day, we’re just: obtaining
source code in case we can use it, using `grep` and common sense to find
potentially interesting binaries, and disassembling them to find out how they
work.

One step at a time.

## Gathering and Analysing Open Source Components

#### GPL Licenses - What They Are and What to Expect [Theory]

Linux, U-Boot and other tools used in this
router are licensed under the
**[General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License)**.
This license mandates that the source code for any binaries built with GPL’d
projects must be made available to anyone who wants it.

Having access to all that source code can be a massive advantage during the
reversing process. The kernel and the bootloader are particularly interesting,
and not just to find security issues.

When hunting for GPL’d sources you can usually expect one of these scenarios:

1. The code is freely available on the manufacturer’s website, nicely ordered
   and completely open to be tinkered with. For instance:
   [apple products](https://opensource.apple.com/) or the
   [amazon echo](https://www.amazon.com/gp/help/customer/display.html?nodeId=201626480)
2. The source code is available by request
   * They send you an email with the sources you requested
   * They ask you for “a reasonable amount” of money to ship you a CD with
     the sources
3. They decide to (illegally) ignore your requests. If this happens to you,
   [consider being nice over trying to get nasty](https://lists.linuxfoundation.org/pipermail/ksummit-discuss/2016-August/003580.html).

In the case of this router, the source code was available on their website, even
though it was a huge pain in the ass to find; it took me a long time of manual
and automated searching but I ended up finding it in the mobile version of the
site:

* [Huawei’s GPL compliance search page](http://m.huawei.com/enmobile/consumer/support/downloads/index.htm).
* [HG533 GPL release](http://download-c.huawei.com/download/downloadCenter?downloadId=17643&siteCode=worldwide)
* [Mirror of the HG533 release](https://drive.google.com/file/d/1B34sUGo36I3pXOEbD4---3KmAVNOpN16/view?usp=sharing).

![ls -lh gpl_source](https://jcjc-dev.com/assets/practical-reversing/rqWb3Jj.png)

**But what if they’re hiding something!?** How could we possibly tell whether
the sources they gave us are the same they used to compile the production
binaries?

#### Challenges of Binary Verification [Theory]

Theoretically, we could try to compile the source code ourselves and compare
the resulting binary with the one we extracted from the device. In practice,
that is extremely more complicated than it sounds.

The exact contents of the binary are strongly tied to the toolchain and overall
environment they were compiled in. We could try to replicate the environment
of the original developers, finding the exact same versions of everything they
used, so we can obtain the same results. Unfortunately, most compilers are not
built with output replicability in mind; even if we managed to find the exact
same version of everything, details like timestamps, processor-specific
optimizations or file paths would stop us from getting a byte-for-byte
identical match.

*If you’d like to read more about it, I can recommend
[this paper](https://madiba.encs.concordia.ca/~x_decarn/papers/verifiable-build-acsac2014.pdf).
The authors go through the challenges they had to overcome in order to verify
that the official binary releases of the application ‘TrueCrypt’ were not
backdoored.*

#### Introduction to the Architecture of Linux [Theory]

In multiple parts of the series, we’ve discussed the different components found
in the firmware: bootloader, kernel, filesystem and some protected memory to
store configuration data. In order to know where to look for what, it’s
important to understand the overall architecture of the system. Let’s quickly
review this device’s:

![Linux Architecture](https://jcjc-dev.com/assets/practical-reversing/2lwcSjA.png)

The bootloader is the first piece of code to be executed on boot. Its job is to
prepare the kernel for execution, jump into it and stop running. From that point
on, the kernel controls the hardware and uses it to run user space logic.
A few more details on each of the components:

1. **Hardware**: The CPU, Flash, RAM and other components are all physically
   connected
2. **Linux Kernel**: It knows how to control the hardware. The developers take
   the Open Source Linux kernel, write *drivers* for their specific device
   and compile everything into an executable Kernel. It manages memory, reads and
   writes hardware registers, etc. In more complex systems, “kernel modules”
   provide the possibility of keeping device drivers as separate entities in the
   file system, and dynamically load them when required; most embedded systems
   don’t need that level of versatility, so developers save precious resources by
   compiling everything into the kernel
3. **libc** (“*The C Library*”): It serves as a general purpose wrapper for the
   System Call API, including extremely common functions like `printf`, `malloc`
   or `system`. Developers are free to call the system call API directly, but in
   most cases, it’s MUCH more convenient to use libc. Instead of the extremely
   common `glibc` (GNU C library) we usually find in more powerful systems, this
   device uses a version optimised for embedded devices:
   [`uClibc`](https://www.uclibc.org/).
4. **User Applications**: Executable binaries in `/bin/` and *shared objects*
   in `/lib/` (libraries that contain functions used by multiple binaries) comprise
   most of the high-level logic. Shared objects are used to save space by storing
   commonly used functions in a single location

#### Bootloader Source Code

As I’ve mentioned multiple times over this series, this router’s bootloader is
U-Boot. U-Boot is GPL licensed, but Huawei failed to include the source code in
their website’s release.

Having the source code for the bootloader can be very useful for some projects,
where it can help you figure out how to run a custom firmware on the device
or modify something; some bootloaders are much more feature-rich than others.
In this case, I’m not interested in anything U-Boot has to offer, so I didn’t
bother following up on the source code.

#### Kernel Source Code

Let’s just check out the source code and look for a...