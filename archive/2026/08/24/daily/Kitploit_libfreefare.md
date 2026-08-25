---
title: libfreefare
url: https://kitploit.com/en/tools/github/nfc-tools/libfreefare
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:59:07.972155
---

# libfreefare

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/nfc-tools/libfreefare

![](https://assets.kitploit.com/production/public/tools/50771/3aa0261fc116fef0b72c8ee931d77dac3f63f7e049f3af78b36aa4d026a0fc51-display-v1.webp)

[Embedded Systems Security](/en/categories/embedded-systems-security)[IoT Security](/en/categories/iot-security)[RFID/NFC Tools](/en/categories/rfid-nfc-tools)[Hardware Security](/en/categories/hardware-security)[Hardware & IoT Security](/en/categories/hardware-iot-security)[Top in RFID/NFC Tools #14](/en/categories/rfid-nfc-tools)

![GitHub](/providers/github.png)nfc-tools/libfreefare

# libfreefare

A convenience API for NFC cards manipulations on top of libnfc.

[View Repository](https://github.com/nfc-tools/libfreefare)

4751142 years ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Introduction

[![Build Status](https://travis-ci.org/nfc-tools/libfreefare.svg?branch=master)](https://travis-ci.org/nfc-tools/libfreefare)
[![Join the chat at https://gitter.im/nfc-tools/libfreefare](https://badges.gitter.im/nfc-tools/libfreefare.svg)](https://gitter.im/nfc-tools/libfreefare?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

The *libfreefare* project provides a convenient API for MIFARE card manipulations.

It is part of the *nfc-tools*, you can find more info on them on the [nfc-tools wiki](http://nfc-tools.org/).

If you are new to *libfreefare* or the *nfc-tools*, you should collect useful information on the [project website](http://nfc-tools.org/) and the [dedicated forums](http://www.libnfc.org/community).

# Feature matrix

## Tags

| Tag | Status |
| --- | --- |
| FeliCa Lite | Supported |
| MIFARE Classic 1k | Supported |
| MIFARE Classic 4k | Supported |
| MIFARE DESFire 2k | Supported |
| MIFARE DESFire 4k | Supported |
| MIFARE DESFire 8k | Supported |
| MIFARE DESFire EV1 | Supported |
| MIFARE Mini | Supported |
| MIFARE Plus S 2k | Not supported |
| MIFARE Plus S 4k | Not supported |
| MIFARE Plus X 2k | Not supported |
| MIFARE Plus X 4k | Not supported |
| MIFARE Ultralight | Supported |
| MIFARE Ultralight C | Supported |
| NTAG21x | Supported |

## Specifications

| Specification | Status |
| --- | --- |
| Mifare Application Directory (MAD) v1 | Supported |
| Mifare Application Directory (MAD) v2 | Supported |
| Mifare Application Directory (MAD) v3 | Supported (part of Mifare DESFire support) |

# Installation

## For \*NIX systems

You can use released version (see **Download** section) or development version:

First, ensure all dependencies are installed:

* [libnfc](https://github.com/nfc-tools/libnfc);
* git;
* Autotools (autoconf, automake, libtool);
* OpenSSL development package.

root@kitploit:~

```
apt-get install autoconf automake git libtool libssl-dev pkg-config
```

Clone this repository:

root@kitploit:~

```
git clone https://github.com/nfc-tools/libfreefare.git
cd libfreefare
```

Before compiling, remember to run:

root@kitploit:~

```
autoreconf -vis
```

You can now compile **libfreefare** the usual autotools way:

root@kitploit:~

```
./configure --prefix=/usr
make
sudo make install
```

## For Windows Systems

### Requirements

* cmake
* make
* mingw{32,64}-gcc

### Building

root@kitploit:~

```
mingw64-cmake -DLIBNFC_INCLUDE_DIRS=/path/to/libnfc-source/include  -DLIBNFC_LIBRARIES=/path/to/libnfc.dll
mingw64-make
```

# Debug

In order to debug using gdb, you should tune the CFLAGS:

root@kitploit:~

```
CFLAGS="-O0 -ggdb" ./configure --prefix=/usr
make clean all
```

It is then possible to debug examples using this kind of command from the root of the repository:

root@kitploit:~

```
./libtool --mode=execute gdb examples/mifare-classic-write-ndef
```

If you are only interested in viewing transfert traces between the PCD and the PICC, simply use the `--enable-debug` configure flag:

root@kitploit:~

```
./configure --enable-debug
make clean all
```

[Download Tool](https://github.com/nfc-tools/libfreefare)