---
title: #BadgeLife @ Off-By-One Conference 2024
url: https://starlabs.sg/blog/2024/07-badgelife-at-off-by-one-conference-2024/
source: Blogs on STAR Labs
date: 2024-07-23
fetch_date: 2025-10-06T17:42:23.432988
---

# #BadgeLife @ Off-By-One Conference 2024

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# #BadgeLife @ Off-By-One Conference 2024

July 22, 2024 · 13 min · Manzel Joseph Seet

Table of Contents

* [Introduction](#introduction)
* [Hardware Design](#hardware-design)
* [Hardware CTF Challenges](#hardware-ctf-challenges)
  + [1. USB String Descriptors](#1-usb-string-descriptors)
  + [2. C-compiled internal library](#2-c-compiled-internal-library)
  + [3. Hardware Random Number Generator](#3-hardware-random-number-generator)
  + [4. Arduino Coprocessor](#4-arduino-coprocessor)
  + [5. Timing Attack](#5-timing-attack)
  + [6. Voltage Glitching](#6-voltage-glitching)
* [Conclusion](#conclusion)

## Introduction[#](#introduction)

As promised, we are releasing the firmware and this post for the Off-By-One badge about one month after the event, allowing interested participants the opportunity to explore it. If you’re interested in learning more about the badge design process, please let us know. We were thrilled to introduce the Octopus Badge at the first-ever Off-By-One Conference 2024. The badge was a one of the highlight at the conference, as it included hardware-focused CTF challenges. In this post, we will explore the ideation and design process of the badge and discuss the concepts needed to solve the challenges.

![](/blog/2024/images/obo2024-intro.jpg)

## Hardware Design[#](#hardware-design)

The artwork was designed by [Sarah Tan](https://x.com/buttburner) and features an adorable octopus with googly eyes. After brainstorming various designs, we decided to incorporate two separate round displays for the eyes. Here is one of the sketches from the early prototypes:

![](/blog/2024/images/obo2024-sketch.png)

Transforming the concept into a circuit design, the badge is centered around an **ESP32-S3 Main Processor** that drives a pair of **GC9A01 OLED Displays**. Users can interact with the badge using **Push Buttons** and a **Directional Joystick**. Additionally, a small coprocessor, the **ATmega328P**, communicates via the **I2C protocol**.

The electronics design was created in KiCad, and here are the 3D renders. The badge comes in three color variants to distinguish different groups of people, such as participants, crew members, and volunteers.

![](/blog/2024/images/obo2024-badge-purple.png)

![](/blog/2024/images/obo2024-badge-black.png)

![](/blog/2024/images/obo2024-badge-blue.png)

The original plan was to include a rechargeable LiPo battery that could last the entire length of the conference. However, due to supply chain difficulties, we opted for AAA batteries instead. Hopefully, we can incorporate the LiPo battery in next year’s badge.

Finally, this is how the actual badge turned out to be!

![](/blog/2024/images/obo2024-badge-actual.jpg)

## Hardware CTF Challenges[#](#hardware-ctf-challenges)

Like any conference badge, ours includes CTF challenges. In this section, I will explain the inspiration behind these challenges and the intended solutions.

In particular, an embedded system is very different from full-fledged computers, in which it was originally designed for resource-constrained applications. For example, the ESP32-S3 processor has no Memory Management Unit (MMU). This means that embedded engineers write code very differently from software engineers.

Our goal is to expose participants to hardware hacking techniques, rather than just providing software challenges within a portable hardware device. We also learned how to improve our electronic badge throughout this process.

### 1. USB String Descriptors[#](#1-usb-string-descriptors)

The first step is to determine what kind of device it is. Therefore, the welcome flag was hidden in the ***USB string descriptors***.

The USB descriptor will tell us where the device is from, such as the vendor and product identifiers, and also is used by your PC to determine what drivers to load.

In Linux, you may print out the kernel debugging messages using `dmesg`. One may also take a look at the device manager in Windows.

```
$ dmesg -w
  [3240249.488872] usb 3-3.2: New USB device found, idVendor=303a, idProduct=4001, bcdDevice= 1.00
  [3240249.488883] usb 3-3.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
  [3240249.488887] usb 3-3.2: Product: #BadgeLife
  [3240249.488889] usb 3-3.2: Manufacturer: STAR LABS SG
  [3240249.488892] usb 3-3.2: SerialNumber: {Welcome_To_OffByOne_2024}
```

Alternatively, you may also use `lsusb` to print out all the devices attached to the PC.

```
$ lsusb -vd 303a:
  iManufacturer           1 STAR LABS SG
  iProduct                2 #BadgeLife
  iSerial                 3 {Welcome_To_OffByOne_2024}
```

### 2. C-compiled internal library[#](#2-c-compiled-internal-library)

The next flag is hidden in a library called `flaglib`. This is seen by showing all the modules through the MicroPython REPL

```
>>> help('modules')
[...] flaglib [...]

>>> import flaglib
>>> dir(flaglib)
['__class__', '__name__', '__dict__', 'getflag']
```

The naive solution is to write a script to exfilterate each character through bruteforce.

```
>>> flaglib.getflag("")
''
>>> flaglib.getflag("{____________________________}")
'{??_????????_??????_??????????'

>>> flaglib.getflag("{my_compiled_python_library}")
'{my_compiled_python_library}'
```

However, knowing that that this is a **C-compiled internal library** which is bundled together in the firmware, it means that its contents can be retrieved if the flash memory is dumped out. Especially so in low-cost systems where encryption is resource heavy, we may uncover passwords or keys which may be saved in plaintext by dumping out the firmware or flash memory.

When trying to dump the firmware, first identify the type of device it is. From the label on the circuit board, we see that it is an `ESP32-S3-WROOM-1-N4`. We can search for [the datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf) which tells us it has `4MiB` of flash memory.

![](/blog/2024/images/obo2024-esp32s3.png)

The firmware can be dumped from an ESP32-S3 using the `esptool.py` package. Put it into bootloader mode by holding down the `BOOT` button and pressing the `RESET` button. Run the following command to save the full contents into a file:

```
$ esptool.py --baud 115200 --port /dev/serial/by-id/usb-** read_flash 0x0 0x400000 fw-backup-4M.bin
```

Following which, one will typically do a simple static analysis of the dumped firmware of an IoT device.

```
$ strings fw-backup-4M_black.bin | strings | grep {
{my_compiled_python_library}
```

### 3. Hardware Random Number Generator[#](#3-hardware-random-number-generator)

Through the display menu, a broken Roulette game is shown. Many people solved it by reversing the **MicroPython-compiled library** which can be extracted from the device as `roulette.mpy`. The files can be easily extracted MicroPython IDE such as [Thonny](https://thonny.org/) or [Mu Editor](https://codewith.mu/).

```
>>> from starlabs import roulette
>>> roulette.roulette()
([1, 0, 1, 2, 1, 2, 2, 1, 2, 2], None)
```

Nevertheless, our intended solution is to understand that naive-method of RNG is to use the noise generated from an analog-to-digital converter (ADC). This is particularly relevant for older microcontrollers that lack hardware RNG peripherals.

> An analog-to-digital converter (ADC) is a commonly used to converts analog signals from external sensors into digital formats that the processor can use in the digital domain.

This is an...