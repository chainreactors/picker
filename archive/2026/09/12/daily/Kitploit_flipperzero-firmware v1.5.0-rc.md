---
title: flipperzero-firmware v1.5.0-rc
url: https://kitploit.com/en/posts/github-flipperdevices-flipperzero-firmware-150-rc
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:28.170433
---

# flipperzero-firmware v1.5.0-rc

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/47650/c34882bd225a2220a9ca4cb52c7d82954dc516c45a921101c0bbe3a30a318b09.png)

New releaseSep 12, 2026

# flipperzero-firmware v1.5.0-rc

Firmware for a portable hardware hacking device with RFID/NFC, sub-GHz, infrared, and BLE support for wireless security testing and signal emulation.

Share

![A pixel art of a Dophin with text: Flipper Zero Official Repo](https://assets.kitploit.com/production/public/readmes/47650/c34882bd225a2220a9ca4cb52c7d82954dc516c45a921101c0bbe3a30a318b09.png)

# Flipper Zero Firmware

* [Flipper Zero Official Website](https://flipper.net) - A simple way to explain to your friends what Flipper Zero can do.
* [Flipper Zero Firmware Update](https://flipper.net/pages/downloads) - Improvements for your dolphin: latest firmware releases, upgrade tools for PC and mobile devices.
* [User Documentation](https://docs.flipper.net/zero) - Learn more about your dolphin: specs, usage guides, and anything you want to ask.
* [Developer Documentation](https://developer.flipper.net/flipperzero/doxygen) - Dive into the Flipper Zero Firmware source code: build system, firmware structure, and more.

# Contributing

Our main goal is to build a healthy and sustainable community around Flipper, so we're open to any new ideas and contributions. We also have some rules and taboos here, so please read this page and our [Code of Conduct](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/CODE_OF_CONDUCT.md) carefully.

## I need help

The best place to search for answers is our [User Documentation](https://docs.flipper.net/zero). If you can't find the answer there, check our [Discord Server](https://flipp.dev/discord). If you want to contribute to the firmware development or modify it for your own needs, you can also check our [Developer Documentation](https://developer.flipper.net/flipperzero/doxygen).

## I want to report an issue

If you've found an issue and want to report it, please check our [Issues](https://github.com/flipperdevices/flipperzero-firmware/issues) page. Make sure the description contains information about the firmware version you're using, your platform, and a clear explanation of the steps to reproduce the issue.

## I want to propose a new feature

If you have a feature request or want to vote on an existing one, please use [Discussions](https://github.com/flipperdevices/flipperzero-firmware/discussions) and follow our [Discussion Guidelines](https://github.com/flipperdevices/flipperzero-firmware/discussions/4395).

## I want to contribute code

Before opening a PR, please confirm that your changes must be contained in the firmware. Many ideas can easily be implemented as external applications and published in the [Flipper Application Catalog](https://github.com/flipperdevices/flipper-application-catalog). If you are unsure, reach out to us on the [Discord Server](https://flipp.dev/discord) or the [Issues](https://github.com/flipperdevices/flipperzero-firmware/issues) page, and we'll help you find the right place for your code.

Also, please read our [Contribution Guide](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/CONTRIBUTING.md) and our [Coding Style](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/CODING_STYLE.md), and make sure your code is compatible with our [Project License](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/LICENSE).

Finally, open a [Pull Request](https://github.com/flipperdevices/flipperzero-firmware/pulls) and make sure that CI/CD statuses are all green.

# Development

Flipper Zero Firmware is written in C, with some bits and pieces written in C++ and armv7m assembly languages. An intermediate level of C knowledge is recommended for comfortable programming. C, C++, and armv7m assembly languages are supported for Flipper applications.

## Requirements

Supported development platforms:

* Windows 10+ with PowerShell and Git (x86\_64)
* macOS 12+ with Command Line tools (x86\_64, arm64)
* Ubuntu 20.04+ with build-essential and Git (x86\_64)

Supported in-circuit debuggers (optional but highly recommended):

* [Flipper Zero Wi-Fi Development Board](https://flipper.net/products/wifi-devboard)
* CMSIS-DAP compatible: Raspberry Pi Debug Probe and etc...
* ST-Link (v2, v3, v3mods)
* J-Link

Flipper Build System will take care of all the other dependencies.

## Cloning source code

Make sure you have enough space and clone the source code:

root@kitploit:~

```
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
```

## Building

Build firmware using Flipper Build Tool:

root@kitploit:~

```
./fbt
```

## Flashing firmware using an in-circuit debugger

Connect your in-circuit debugger to your Flipper and flash firmware using Flipper Build Tool:

root@kitploit:~

```
./fbt flash
```

## Flashing firmware using USB

Make sure your Flipper is on, and your firmware is functioning. Connect your Flipper with a USB cable and flash firmware using Flipper Build Tool:

root@kitploit:~

```
./fbt flash_usb
```

## Documentation

* [Flipper Build Tool](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/fbt.md) - building, flashing, and debugging Flipper software
* [Applications](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/AppsOnSDCard.md), [Application Manifest](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/AppManifests.md) - developing, building, deploying, and debugging Flipper applications
* [Hardware combos and Un-bricking](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/KeyCombo.md) - recovering your Flipper from the most nasty situations
* [Flipper File Formats](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/file_formats) - everything about how Flipper stores your data and how you can work with it
* [Universal Remotes](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/UniversalRemotes.md) - contributing your infrared remote to the universal remote database
* And much more in the [Developer Documentation](https://developer.flipper.net/flipperzero/doxygen)

# Project structure

* `applications` - Applications and services used in firmware
* `applications_users` - Place for your additional applications and services
* `assets` - Assets used by applications and services
* `documentation` - Documentation generation system configs and input files
* `furi` - Furi Core: OS-level primitives and helpers
* `lib` - Our and 3rd party libraries, drivers, tools and etc...
* `site_scons` - Build system configuration and modules
* `scripts` - Supplementary scripts and various python libraries
* `targets` - Firmware targets: platform specific code

Also, see `ReadMe.md` files inside those directories for further details.

# Links

* Discord: [flipp.dev/discord](https://flipp.dev/discord)
* Reddit: [reddit.com/r/flipperzero](https://www.reddit.com/r/flipperzero/)
* Website: [flipper.net](https://flipper.net)
* Kickstarter: [kickstarter.com](https://www.kickstarter.com/projects/flipper-devices/flipper-zero-tamagochi-for-hackers)

## SAST Tools

* [PVS-Studio](https://pvs-studio.com/pvs-studio/?utm_source=website&utm_medium=github&utm_campaign=open_source) - static analyzer for C, C++, C#, and Java code.

[Read more](/en/tools/github/flipperdevices/flipperzero-firmware?expand=1)

## Categories

[Embedded Systems Security](/en/categories/embedded-systems-security)[Bluetooth Security](/en/categories/bluetooth-security)[IoT Security](/en/categories/iot-security)[RFID/NFC Tools]...