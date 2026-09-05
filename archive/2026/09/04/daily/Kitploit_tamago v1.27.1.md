---
title: tamago v1.27.1
url: https://kitploit.com/en/posts/github-usbarmory-tamago-v1271
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:58.016786
---

# tamago v1.27.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/6581/e1e1c833d1419d63136af6986b50b7a8839b2412bbe5049ad680d683e15409f2.png)

New releaseSep 4, 2026

# tamago v1.27.1

Framework for compiling and executing Go applications on bare metal processors, enabling secure firmware development with reduced attack surface through OS and C dependency removal.

Share

# TamaGo - bare metal Go

tamago | <https://github.com/usbarmory/tamago>

Copyright (c) The TamaGo Authors. All Rights Reserved.

![TamaGo gopher](https://github.com/usbarmory/tamago/wiki/images/tamago.svg?sanitize=true)

# Introduction

TamaGo is a framework that enables compilation and execution of unencumbered Go
applications on bare metal processors (AMD64, ARM, ARM64, RISCV64).

The projects spawns from the desire of reducing the attack surface of embedded
systems firmware by removing any runtime dependency on C code and Operating
Systems.

The TamaGo framework consists of the following components:

* A modified [Go distribution](https://github.com/usbarmory/tamago-go)
  which extends `GOOS` support to the `tamago` target, allowing bare metal
  execution through a [runtime/goos](https://github.com/usbarmory/tamago-go/tree/latest/src/runtime/goos)
  overlay set by `GOOSPKG`.
* Go packages for processor/SoC support.
* Go packages for board support.

The modifications are minimal against the original Go compiler, runtime and the
target application (one import required), with a clean separation from other
architectures.

Strong emphasis is placed on code re-use from existing architectures already
included within the standard Go runtime, see
[Internals](https://github.com/usbarmory/tamago/wiki/Internals).

The modifications maintain [complete standard library support](https://github.com/usbarmory/tamago/wiki/Compatibility).

Such aspects are motivated by the desire of providing a framework that allows
secure Go firmware development on embedded systems.

# Current releases

The following links are the latest releases for the
[TamaGo modified Go distribution](https://github.com/usbarmory/tamago-go),
which adds `GOOS=tamago` support to the corresponding Go version, and
[TamaGo library](https://github.com/usbarmory/tamago):

[![GitHub release](https://img.shields.io/github/v/release/usbarmory/tamago-go)](https://github.com/usbarmory/tamago-go/releases/latest) [![Build Status](https://github.com/usbarmory/tamago-go/workflows/Build%20Go%20compiler/badge.svg)](https://github.com/usbarmory/tamago-go/actions)
[![GitHub release](https://img.shields.io/github/v/release/usbarmory/tamago)](https://github.com/usbarmory/tamago/releases/latest)

# Documentation

[![Go Reference](https://pkg.go.dev/badge/github.com/usbarmory/tamago.svg)](https://pkg.go.dev/github.com/usbarmory/tamago)

The main documentation can be found on the
[project wiki](https://github.com/usbarmory/tamago/wiki).

The package API documentation can be found on
[pkg.go.dev](https://pkg.go.dev/github.com/usbarmory/tamago).

# Supported AMD64 targets

The following table summarizes currently supported x86-64 targets
(`GOOS=tamago GOARCH=amd64`).

| CPU | Platform | CPU package | Platform package |
| --- | --- | --- | --- |
| AMD/Intel 64-bit | [Cloud Hypervisor](https://www.cloudhypervisor.org) | [amd64](https://github.com/usbarmory/tamago/tree/master/amd64) | [cloud\_hypervisor/vm](https://github.com/usbarmory/tamago/tree/master/board/cloud_hypervisor/vm) |
| AMD/Intel 64-bit | [Firecracker microvm](https://firecracker-microvm.github.io) | [amd64](https://github.com/usbarmory/tamago/tree/master/amd64) | [firecracker/microvm](https://github.com/usbarmory/tamago/tree/master/board/firecracker/microvm) |
| AMD/Intel 64-bit | [QEMU microvm](https://www.qemu.org/docs/master/system/i386/microvm.html) | [amd64](https://github.com/usbarmory/tamago/tree/master/amd64) | [qemu/microvm](https://github.com/usbarmory/tamago/tree/master/board/qemu/microvm) |
| AMD/Intel 64-bit | [UEFI](https://uefi.org/) | [amd64](https://github.com/usbarmory/tamago/tree/master/amd64) | [uefi/x64](https://github.com/usbarmory/go-boot/tree/main/uefi/x64) |
| AMD/Intel 64-bit | [Google Compute Engine](https://cloud.google.com/products/compute) | [amd64](https://github.com/usbarmory/tamago/tree/master/amd64) | [google/gcp](https://github.com/usbarmory/tamago/tree/master/board/google/gcp), [uefi/x64](https://github.com/usbarmory/go-boot/tree/main/uefi/x64) |

# Supported ARM targets

The following table summarizes currently supported ARM SoCs and boards
(`GOOS=tamago GOARCH=arm`).

| SoC | Board | SoC package | Board package |
| --- | --- | --- | --- |
| NXP i.MX6ULZ/i.MX6UL | [USB armory Mk II](https://github.com/usbarmory/usbarmory/wiki/Mk-II-Introduction) | [imx6ul](https://github.com/usbarmory/tamago/tree/master/soc/nxp/imx6ul) | [usbarmory/mk2](https://github.com/usbarmory/tamago/tree/master/board/usbarmory) |
| NXP i.MX6ULL/i.MX6UL | [USB armory Mk II LAN](https://github.com/usbarmory/usbarmory/wiki/Mk-II-LAN) | [imx6ul](https://github.com/usbarmory/tamago/tree/master/soc/nxp/imx6ul) | [usbarmory/mk2](https://github.com/usbarmory/tamago/tree/master/board/usbarmory) |
| NXP i.MX6ULL/i.MX6ULZ | [MCIMX6ULL-EVK](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-6ull-and-6ulz-applications-processor%3AMCIMX6ULL-EVK) | [imx6ul](https://github.com/usbarmory/tamago/tree/master/soc/nxp/imx6ul) | [mx6ullevk](https://github.com/usbarmory/tamago/tree/master/board/nxp/mx6ullevk) |
| Broadcom BCM2835 | [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero) | [bcm2835](https://github.com/usbarmory/tamago/tree/master/soc/bcm2835) | [pi/pizero](https://github.com/usbarmory/tamago/tree/master/board/raspberrypi) |
| Broadcom BCM2835 | [Raspberry Pi 1 Model A+](https://www.raspberrypi.org/products/raspberry-pi-1-model-a-plus/) | [bcm2835](https://github.com/usbarmory/tamago/tree/master/soc/bcm2835) | [pi/pi1](https://github.com/usbarmory/tamago/tree/master/board/raspberrypi) |
| Broadcom BCM2835 | [Raspberry Pi 1 Model B+](https://www.raspberrypi.org/products/raspberry-pi-1-model-b-plus/) | [bcm2835](https://github.com/usbarmory/tamago/tree/master/soc/bcm2835) | [pi/pi1](https://github.com/usbarmory/tamago/tree/master/board/raspberrypi) |
| Broadcom BCM2836 | [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b) | [bcm2835](https://github.com/usbarmory/tamago/tree/master/soc/bcm2835) | [pi/pi2](https://github.com/usbarmory/tamago/tree/master/board/raspberrypi) |
| Nuvoton NUC980 | [NuMaker-IIoT-NUC980G2](https://www.nuvoton.com/products/iot-solution/iot-platform/numaker-iiot-nuc980g2) | [nuc980](https://github.com/usbarmory/tamago/tree/master/soc/nuvoton/nuc980) | [nuc980iiot](https://github.com/usbarmory/tamago/tree/master/board/nuvoton/nuc980iiot) |

# Supported ARM64 targets

The following table summarizes currently supported ARM64 SoCs and boards
(`GOOS=tamago GOARCH=arm64`).

| SoC | Board | SoC package | Board package |
| --- | --- | --- | --- |
| NXP i.MX8M Plus | [8MPLUSLPD4-EVK](https://www.nxp.com/design/design-center/development-boards-and-designs/8MPLUSLPD4-EVK) | [imx8mp](https://github.com/usbarmory/tamago/tree/master/soc/nxp/imx8mp) | [imx8mpevk](https://github.com/usbarmory/tamago/tree/master/board/nxp/imx8mpevk) |
| Microchip LAN969x | [EVB-LAN9696-24port](https://www.microchip.com/en-us/development-tool/ev23x71a) | [lan969x](https://github.com/usbarmory/tamago/tree/master/soc/microchip/lan969x) | [lan9696evb](https://github.com/usbarmory/tamago/tree/master/board/microchip/lan9696evb) |

# Supported RISC-V targets

The f...