---
title: Root Shell on Credit Card Terminal
url: https://stefan-gloor.ch/yomani-hack
source: Over Security - Cybersecurity news aggregator
date: 2025-06-04
fetch_date: 2025-10-06T22:55:27.152360
---

# Root Shell on Credit Card Terminal

# stefan-gloor.ch

[Projects](/) [About me](about-me) [芒聠聴Github](https://github.com/stgloorious)

# Root Shell on Credit Card Terminal

![Voip phone](img/yomani.jpg)

In this project, I started to reverse engineer payment card
terminals because they seemed to be an interesting target for security
research, given the high stakes involved. Although I initially didn芒聙聶t
know much about this industry, I did expect a ton of security features
and a very security-hardened device. And to some degree, this was also
correct.

## First Look

The model I went with is a Worldline Yomani XR terminal. Although it
seems to be discontinued at the time of writing, this is the model that
is *everywhere* in Switzerland. From big grocery chains to the
small repair shop on the corner, everyone has one or a whole fleet of
this exact terminal.

After booting it up and aimlessly clicking through the UI, I did a
quick port scan, but couldn芒聙聶t find anything interesting. So naturally,
I started to take it apart.

[![Picture of the main PCB of the Yomani XR terminal with annotation of different board components.](img/yomani_pcb.jpg)](img/yomani_pcb.jpg)

The housing and the PCBs appear to be well-made. The design consists
of multiple PCBs: a small connector board for the outward-facing
connectors, the main board, and a vertical board the card slot sits on.
The main SoC seems to be a custom ASIC, a dual-core Arm processor
code-named 芒聙聹Samoa II芒聙聺 in the firmware, but I am jumping ahead.
According to Worldline documentation, this seems to indeed be a custom
ASIC, rather than just a rebranded off-the-shelf chip. Next to it,
there is a small external flash and RAM.

## Tamper Protections

During disassembly, I kept looking for a tamper switch that would
detect when the device芒聙聶s housing was opened, like I had seen previously
on laptops and other devices. However, I couldn芒聙聶t find such a switch.
Rather, they use the board-to-board interconnects as a way of detecting
when the device is opened. Because they use relatively
pressure-sensitive Zebra strips between the boards, they have to be
tightly screwed together. Even unscrewing some of the screws is enough
to break contact and trigger a tamper event. Of course, the tamper
detection must also work when the power is disconnected, so that芒聙聶s the
purpose of the coin cell battery.

But this is not all in terms of tamper resistance: The 芒聙聹vulnerable芒聙聺
PCBs are covered by zig-zag traces that act as a tamper detection
mechanism. Accidentally breaking a single copper trace during a
physical penetration attempt (hole drill etc.) is enough to trigger the
tamper detection.

[![PCB showing a zig-zag line pattern across the whole board, acting as a temper detection mechanism.](img/yomani_mesh2.jpg)](img/yomani_mesh2.jpg)

Trace meander on the display PCB acting as tamper detection.

The card slot itself is contained in an additional, internal
housing. Wrapped around this housing, there is a flex PCB acting as
tamper protection.

[![Inner plastic housing is wrapped in a flex PCB with zig-zag traces, acting as a temper detection mechanism.](img/yomani_mesh.jpg)](img/yomani_mesh.jpg)

Card reader assembly wrapped in a tamper detection flex PCB.

After putting the device back together, it was clear that my
intrusion had not gone undetected. Sure enough, the device would now
only show a big red screen screaming 芒聙聹TAMPER DETECTED芒聙聺. In this mode,
the device seems to be fully unresponsive to any kind of external
input. So, game over?

[![Yomani Credit Card terminal showing an all-red screen saying OUT OF ORDER, TAMPERED STATE, no key loaded.](img/yomani_tampered.jpg)](img/yomani_tampered.jpg)

## Chip-Off Firmware Extraction

Since any 芒聙聹runtime芒聙聺 exploration seems to be futile now, I wanted to
take a look a the firmware. For this, I desoldered the on-board flash
chip, soldered some wires to it in 芒聙聹dead bug芒聙聺 style and proceeded to
dump the contents.

[![Flash chip in BGA housing mounted upside-down on a perfboard. Thin copper wires are connected from the chip芒聙聶s contacts to a flash reader.](img/yomani_chipoff.jpg)](img/yomani_chipoff.jpg)

BGA flash chip of the card terminal desoldered and connected to a
flash reader.

To my surprise, the contents seemed to be entirely unencrypted!
However, the contents seemed to have a strange ECC layout. Instead of
following the flash chip芒聙聶s inherent page layout and putting the ECC
data in the interleaved spare areas, it appeared as if the some ECC
data was present in the page and some clear text was in the spare
areas. With the help of some friends, I figured out the layout: instead
of using the standard 2048 byte payload + 64 byte ECC/spare layout, it
uses 3x 694 byte chunks of data each followed by 10 ECC bytes. The ECC
bytes do not appear to be all used. Instead, the last 16 bytes of the
spare area seem to act as metadata for the YAFFS2 file system. Now
normally, there are less ECC bytes per page and therefore the usable
metadata area for the filesystem is larger than 16 bytes. For this
reason, the YAFFS2 filesystem had to be patched to work with smaller
metadata structures.

I implemented a compatible filesystem reader and with it, I could
successfully dump the filesystem contents!

[View
yomani-unpacker on Github](https://github.com/stgloorious/yomani-unpacker)

Now it was clear that this device runs Linux. I found a standard
Linux filesystem with a lot of interesting files to browse through. The
system runs a 3.6 kernel, built with Buildroot 2010.02 (!) in February
of 2023. The system seems to use a custom bootloader, 芒聙聹Booter v1.7芒聙聺.
Although I don芒聙聶t know how recent the firware version was that I ended
up dumping, it must have been released after February 2023. So finding
such an ancient kernel is rather concerning. Userspace-wise, the system
uses classy init scripts, busybox, and uClibc (final release was 13
years ago). libcrypt has version 0.9.26, ouch.

## Finding a Root Shell by Accident

Having seen the firmware gave me some new confidence that there
might be more stuff to find. So I reattached the flash chip using
wires, ignoring everything I know about signal integrity. To my
surprise the device booted up again (showing the tamper message).

[![BGA flash chip attached to PCB using wires](img/yomani_flash_attached.jpg)](img/yomani_flash_attached.jpg)

Flash chip reunited with the PCB, as good as new.

My next goal was to find the serial console of the Linux system.
Surely, it must have one for debugging. By looking at a boot log, I
might get some more valuable information. So, equipped with a logic
analyzer, I started poking.

[![PCB with needle probes attached to a logic analyzer](img/yomani_probing.jpg)](img/yomani_probing.jpg)

Probing the debug connector.

It didn芒聙聶t take long until I found some activity on one pad of the
unpopulated debug connector. Bingo!

```
------------------------------------------------------------------------
Booter: 1.7b+00002:gbe6b338 Jun  3 2014 08:51:58 owi
Reset reason: Tamper
Start USB boot ...
Got address 0x00000015
Enumerated.
Dfu timeout
yaffs: checkpoint restore ... KO!
yaffs: clean up the mess caused by an aborted checkpoint
file "hwinfo-l0" found
file "hwinfo-l1" found
file "hwinfo-l2" found
file "loadercode" found
file "mp1.img" found
file "linux" found
Uncompressing Linux... done, booting the kernel.
Linux version 3.6.0-samoa-01844-g1f05798 (ppd@debian) (gcc version 4.3.4 (Buildroot 2010.02) ) #0 Fri, 10 Feb 2023 16:26:07 +0100
cpufreq: initial frequency: 264000 kHz
MAC-1G DMA: 430ab000 - 430ab9ff
MAC addr = 00:08:19:4e:56:2c
eth0: ioaddr: d00d0000, dev: c30ac000
probing samoafb: rc = 0
  DMA = 4F500000->c3a00000, IO =   (null)
UART 1 probing
UART 1 probing OK
UART 2 probing
UART 2 probing OK
UART 3 probing
UART 3 probing OK
pca953x 0-0049: failed reading register
ba315 ba315.0: NAND ID: id[0-3]=芒聙聶EF A1 00 95芒聙聶, manu=芒聙聶Winbond芒聙聶, dev=芒聙聶NAND 128MiB 1,8V 8-bit芒聙聶
drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
yaffs: Attemptin...