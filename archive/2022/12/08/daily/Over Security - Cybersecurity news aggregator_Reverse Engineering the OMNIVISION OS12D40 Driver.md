---
title: Reverse Engineering the OMNIVISION OS12D40 Driver
url: https://serhack.me/articles/reverse-engineering-omnivision-os12d40-driver/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-08
fetch_date: 2025-10-04T00:54:53.190454
---

# Reverse Engineering the OMNIVISION OS12D40 Driver

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/reverse-engineering-omnivision-os12d40-driver/ "en version")
[IT](https://serhack.me/it/articles/analisi-omnivision-os12d40-driver/ "it version")

# Reverse Engineering the OMNIVISION OS12D40 Driver

Published at December 7, 2022 – 17 min read – 3584 words

![Reverse Engineering OMNIVISION OS12D40 Driver](https://serhack.me/images/articles/reolink-firmware/reolink_7_800px.jpg)

In [Part 6](https://serhack.me/articles/techniques-setting-up-pheripherals-dma-pio/) of our series, we structured a theoretical discussion regarding the devices, how they communicate, and the hardware elements that enable this.

Another very interesting folder that we come across during our investigation is `/lib`, which includes all the libraries for executables and device drivers developed by Novatek that allow the operating system to properly configure and set up all the hardware devices connected to the board. To begin, let’s introduce the topic by explaining what device drivers are and how they work on Linux-based systems.

### Development of a Device Driver in Linux

The development of a device driver is done through the creation of a kernel module. Kernel modules are pieces of code that can be loaded at runtime dynamically. To load a kernel module, you can use the `insmod name_module_to_load` tool, which represents the path to the .ko file where the module is compiled and linked.

As the name implies, the main advantage of adopting modules is modularity. Each module is a unit in itself, each of which performs a specific task and is capable of interacting with the others. Do we need to disable a peripheral? We can only disable one module. Are we installing another one? We can enable another module. All of this without losing the other modules that manage entirely other peripherals. The concept of software modularity is very close, if not completely, to physical modularity ― in an “open” machine, I am free to install the peripherals I want with the devices I want.

The development of a device driver, however, is not risk-free. In fact, a device driver sits at the level between the applications, the operating system, and the devices to be controlled. So, it has privileged access over certain structures of the operating system. This can present problems such as race-condition and deadlock. Another issue concerns system integrity: If, by enabling a kernel extension, the module is able to access privileged sections, how can we prevent cyber attacks in case of intrusion? Challenges such as these remain open to this day.

Returning to Reolink, all kernel modules and extensions are contained within the `/lib/modules` folder and are loaded at system startup. Technically, a kernel module is an object file that is a fragment of executable code, which references external functions. .ko files are nothing more than executable files, so it is possible to reverse engineer them without adopting any special gimmicks.

For those interested in developing new modules for Linux, there is an excellent resource on the subject named ["*The Linux Kernel Module Programming Guide*"](https://sysprog21.github.io/lkmpg/) which gives an excellent introduction to device driver development. This is recommended reading!

## OMNIVISION Sensor Device Driver

The modules are loaded dynamically by the `/etc/init.d/S10_SysInit2` script, which is started as soon as the operating system is loaded. Enumerated within this file are a number of modules to control, operate, and set up the various devices on the board ― including the optical sensor, artificial intelligence engine, and external peripherals.

```
[...]
insmod module_to_load.ko
[...]
```

What we want to do in this section is to choose a device driver and try-through some reverse engineering actions to understand how it works and how it interfaces with the system. For this purpose, we have chosen to explore one of the device drivers par excellence, the device driver for the [OMNIVISION](https://www.ovt.com/) optical sensor.

The device driver for the optical sensor `nvt_sen_os12d40.ko` is located within the `/lib/modules/4.19.91/hdal/sen_os12d40` folder, where `os12d40` is the model of the sensor equipped in the Reolink RLC-810A camera. A quick inspection within the `file` utility shows that it is an ELF file for the ARM architecture.

```
nvt_sen_os12d40.ko: ELF 32-bit LSB relocatable, ARM, EABI5 version 1 (SYSV), BuildID[sha1]=01ccd81e7f0982593f7ca5b5c8c31f79e0e5f0aa, not stripped
```

In addition, we find that the binary contains some useful information since it is “not stripped.” Let’s take a step back to better understand what “stripped” means. When we create a program, if specified, the compiler makes sure to put some useful debugging information inside the file. This includes the name of the function used, the name of the variables. This is very valuable information for reverse engineering.

Is it useful to leave non-stripped binaries in production? Yes and no. On the one hand, it allows those who are more experienced to be able to better understand how a binary works and to be able to generate a more detailed core dump, but on the other hand it is all overhead that weighs on the size of each binary. Knowing this, it is practical for developers to include kernel modules with debug information to get more details in case of an error.

We gather more information regarding the kernel extension through the `modinfo` utility.

```
filename:       /lib/modules/4.19.91/hdal/sen_os12d40/nvt_sen_os12d40.ko
license:        GPL
description:    sen_os12d40
author:         Novatek Corp.
version:        1.40.000
srcversion:     E22953EBFA0A94EB836FD2B
depends:        kdrv_builtin,kwrap,kflow_videocapture
name:           nvt_sen_os12d40
vermagic:       4.19.91 SMP preempt mod_unload modversions ARMv7
parm:           sen_cfg_path:Path of cfg file (charp)
parm:           sen_debug_level:Debug message level (int)
```

Let’s spend some time commenting on the result of the tool. The driver was developed by Novatek and GPL was specified as the license. At the moment, we can ignore the `version` field and the `srcversion`. The `depends` field is very important, because it specifies any dependencies of the kernel module on others ― in this case, the optical sensor module depends on `kdrv_builtin`, `kwrap`, and `kflow_videocapture`. There are two parameters that the extension accepts: the absolute path to the configuration file (`charp`: pointer to a char array) and the debug level (`int`: an integer), which specifies how verbose the module should be.

Speaking of licensing, when a module is declared GPL-compliant, the manufacturer should attach the original source code along with the object modules to allow end users to modify or add new functionality. In this case, it is not clear as to why Novatek did not release the source code despite having declared a GPL license.

### Reverse Engineering via Ghidra

[Ghidra](https://ghidra-sre.org/) represents another essential set of tools for reverse engineering. Developed by [NSA](https://nsa.com) through [Java](https://java.com), Ghidra allows us to analyze, investigate, and perform various forms of analysis on a binary file.

We can extract the module and upload it to Ghidra. To do this, we create a new Ghidra project (`Create new Project`) and load it through the handy GUI (`Load new binary...`). Ghidra will ask us what kind of analysis should be performed on the binary. For now, let’s leave the ones it proposes by default, which are more than sufficient. To start the analysis, simply click the `Analyze` button.

Once the analysis by Ghidra is finished, we can start the exploration via the `Symbol Tree` panel at the bottom left. It is interesting to be a...