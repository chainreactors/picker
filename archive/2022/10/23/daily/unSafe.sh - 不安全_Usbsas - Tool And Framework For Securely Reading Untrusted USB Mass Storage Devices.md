---
title: Usbsas - Tool And Framework For Securely Reading Untrusted USB Mass Storage Devices
url: https://buaq.net/go-132124.html
source: unSafe.sh - 不安全
date: 2022-10-23
fetch_date: 2025-10-03T20:40:14.902137
---

# Usbsas - Tool And Framework For Securely Reading Untrusted USB Mass Storage Devices

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

![](https://8aqnet.cdn.bcebos.com/11b4c99e6747a4cdc926d897331b6328.jpg)

Usbsas - Tool And Framework For Securely Reading Untrusted USB Mass Storage Devices

usbsas is a free and open source (GPLv3) tool and framework for securely reading untrusted
*2022-10-22 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-132124.htm)
阅读量:54
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYfZGUAbG_8_B6dpmiMz3AfMBv7BfeuecxSlyd2QiAVSu4Iwr1Jc41fPvD3A2qeBC0XU3SF7LJ2MhuF2NKMfWSreQfj3fNV-Fu1HhvjnBcwP0dgbLzg6MWU8TAM86zId6iP7X2_kUh4tdgLcVsEcmVS08IeEQee7vnJSF6Ixq8cC0GU8lbp47U9eL8ew/w640-h302/usbsas.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYfZGUAbG_8_B6dpmiMz3AfMBv7BfeuecxSlyd2QiAVSu4Iwr1Jc41fPvD3A2qeBC0XU3SF7LJ2MhuF2NKMfWSreQfj3fNV-Fu1HhvjnBcwP0dgbLzg6MWU8TAM86zId6iP7X2_kUh4tdgLcVsEcmVS08IeEQee7vnJSF6Ixq8cC0GU8lbp47U9eL8ew/s853/usbsas.png)

usbsas is a free and open source (GPLv3) tool and framework for securely reading untrusted USB mass storage devices.

## Description

Following the concept of [defense](https://www.kitploit.com/search/label/Defense "defense") in depth and the principle of least privilege, usbsas's goal is to reduce the attack surface of the USB stack. To achieve this, most of the USB related tasks (parsing USB packets, SCSI commands, file systems etc.) usually executed in (privileged) [kernel](https://www.kitploit.com/search/label/Kernel "kernel") space has been moved to user space and separated in different processes (microkernel style), each being executed in its own restricted [secure computing mode](https://en.wikipedia.org/wiki/Seccomp "secure computing  mode").

The main purpose of this project is to be deployed as a kiosk / [sheep dip](https://en.wikipedia.org/wiki/Sheep_dip_%28computing%29 "sheep  dip") station to securely transfer files from an untrusted USB device to a trusted one.

It works on GNU/Linux and is written in Rust.

## Features

usbsas can:

* read files from an untrusted USB device (without using kernel modules like `uas`, `usb_storage` and the file system ones). Supported file systems are `FAT`, `exFat`, `ext4`, `NTFS` and `ISO9660`
* analyze files with a remote antivirus
* copy files on a new file system to a trusted USB device. Supported file systems are `FAT`, `exFAT` and `NTFS`
* upload files to a remote server
* make an image of a USB device
* wipe a USB device

## Applications

Applications built on top of usbsas:

* **Web [client](https://www.kitploit.com/search/label/Client "client") / server**: This is the main application of usbsas, for deploying a secure USB to USB [file transfer](https://www.kitploit.com/search/label/File%20Transfer "file transfer") kiosk.
* **[Fuse](https://en.wikipedia.org/wiki/Filesystem_in_Userspace "Fuse") implementation**: mount USB devices (read-only) with usbsas.
* **Python**: usbsas can also be used with Python, a script that copies everything from a device to another is given as example.

## Documentation

* [Architecture and technical](https://github.com/cea-sec/usbsas/blob/main/doc/architecture.md "Architecture and technical") documentation
* [Build and usage](https://github.com/cea-sec/usbsas/blob/main/doc/build_usage.md "Build and usage") documentation
* [Kiosk deployment](https://github.com/cea-sec/usbsas/blob/main/doc/kiosk.md "Kiosk deployment") documentation
* [Live ISO](https://github.com/cea-sec/usbsas/blob/main/doc/live-iso.md "Live ISO") documentation
* Developer documentation can be generated with `$ cargo doc`

## Contributing

Any contribution is welcome, be it code, bug report, packaging, documentation or translation.

## License

Dependencies included in this project:

* `ntfs3g` is GPLv2 (see ntfs3g/src/ntfs-3g/COPYING).
* `FatFs` has a custom BSD-style license (see ff/src/ff/LICENSE.txt)
* `fontawesome` is CC BY 4.0 (icons), SIL OFL 1.1 (fonts) and MIT (code) (see client/web/static/fontawesome/LICENSE.txt)
* `bootstrap` is MIT (see client/web/static/bs/LICENSE)
* `Lato` font is SIL OFL 1.1 (see client/web/static/fonts/LICENSE.txt)

usbsas is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

usbsas is [distributed](https://www.kitploit.com/search/label/Distributed "distributed") in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License [along with usbsas](https://github.com/cea-sec/usbsas/blob/main/LICENSE "along with  usbsas"). If not, see [the gnu.org web site](https://www.gnu.org/licenses/ "the gnu.org web  site").

Usbsas - Tool And Framework For Securely Reading Untrusted USB Mass Storage Devices
![Usbsas - Tool And Framework For Securely Reading Untrusted USB Mass Storage Devices](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYfZGUAbG_8_B6dpmiMz3AfMBv7BfeuecxSlyd2QiAVSu4Iwr1Jc41fPvD3A2qeBC0XU3SF7LJ2MhuF2NKMfWSreQfj3fNV-Fu1HhvjnBcwP0dgbLzg6MWU8TAM86zId6iP7X2_kUh4tdgLcVsEcmVS08IeEQee7vnJSF6Ixq8cC0GU8lbp47U9eL8ew/s72-w640-c-h302/usbsas.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/10/usbsas-tool-and-framework-for-securely.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)