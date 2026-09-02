---
title: nDPI v6.0
url: https://kitploit.com/en/posts/github-ntop-ndpi-60
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:10.792984
---

# nDPI v6.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2395/3ba682651663e77c3997f6aa53cdc5812403fb3238912cce3caa13e9e32e081d.png)

New releaseSep 1, 2026

# nDPI v6.0

Open Source Deep Packet Inspection Software Toolkit

Share

# nDPI

[![Build Status](https://img.shields.io/github/actions/workflow/status/ntop/nDPI/build.yml?branch=dev&logo=github)](https://github.com/ntop/nDPI/actions?query=workflow%3ABuild)
[![Fuzzing Status](https://oss-fuzz-build-logs.storage.googleapis.com/badges/ndpi.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:ndpi)

## What is nDPI ?

nDPI® is an open source LGPLv3 library for deep-packet inspection.

A generic FAQ about nDPI is available [here](https://github.com/ntop/nDPI/blob/dev/doc/FAQ.rst)

### How To Compile nDPI

In order to compile this project do

* ./autogen.sh && ./configure
* make

If you get some errors while compiling `croaring.c`, try:

* ./autogen.sh && ./configure --enable-old-croaring
* make

To compile the library w/o any tools or tests:

* ./autogen.sh && ./configure --with-only-libndpi
* make

Out-of-tree builds are supported:

* ./autogen.sh
* mkdir build
* cd build
* ../configure && make

To run tests do additionally:

* ./tests/do.sh # Generate and check for diff's in PCAP files
* ./tests/do-unit.sh # Run unit tests
* ./tests/do-dga.sh # Run DGA detection test

or run all with: `make check`

Please note that the (minimal) pre-requisites for compilation include:

* GNU tools (autoconf automake libtool pkg-config gettext flex bison)
* GNU C compiler (gcc) or Clang

On Debian/Ubuntu systems do:

* sudo apt-get install build-essential git gettext flex bison libtool autoconf automake pkg-config libpcap-dev libjson-c-dev libnuma-dev libpcre2-dev libmaxminddb-dev librrd-dev

On Arch Linux:

* sudo pacman -S gcc git gettext flex bison libtool autoconf automake pkg-config libpcap json-c numactl pcre2 libmaxminddb rrdtool

On FreeBSD:

* sudo pkg install gcc git gettext flex bison libtool autoconf automake devel/pkgconf gmake libpcap json-c pcre2 libmaxminddb rrdtool

Remember to use `gmake` and not `make` on FreeBSD

On MacOS:

* brew install coreutils gcc git gettext flex bison libtool autoconf automake pkg-config libpcap json-c pcre2 libmaxminddb rrdtool

On Windows:

There are three supported ways to build nDPI:

1. MSYS2 (assuming [MSYS2](https://www.msys2.org/) already installed):

* msys2 -c "pacman --noconfirm -S --needed --overwrite '\*' git mingw-w64-x86\_64-toolchain automake1.16 automake-wrapper autoconf libtool make mingw-w64-x86\_64-json-c mingw-w64-x86\_64-crt-git mingw-w64-x86\_64-pcre2 mingw-w64-x86\_64-libpcap"

2. Mingw-w64
3. Visual Studio (see `windows/nDPI.sln`)

Note: All Windows versions require [npcap](https://npcap.com/#download) with WinPcap compatibility mode enabled.

### How To Build The Documentation

* pip install --upgrade pip
* pip install -r doc/requirements.txt
* make doc

Use the builtin python3 webserver to view documentation:

* make doc-view

### How To Add A New Protocol Dissector

The entire procedure of adding new protocols in detail:

1. Add new protocol together with its unique ID to: `src/include/ndpi_protocol_ids.h`
2. Create a new protocol in: `src/lib/protocols/`
3. Variables to be kept for the duration of the entire flow (as state variables) need to be placed in: `src/include/ndpi_typedefs.h` in `ndpi_flow_tcp_struct` (for TCP only), `ndpi_flow_udp_struct` (for UDP only), or `ndpi_flow_struct` (for both).
4. Add a new entry for the search function for the new protocol in: `src/include/ndpi_private.h`
5. Choose (do not change anything) a selection bitmask from: `src/include/ndpi_define.h`
6. Set protocol default ports in `ndpi_init_protocol_defaults` in: `src/lib/ndpi_main.c`
7. Be sure to have nBPF support, cloning `PF_RING` in the same directory where you cloned `nDPI`: `git clone https://github.com/ntop/PF_RING/ && cd PF_RING/userland/nbpf && ./configure && make`. You can ignore the `/bin/sh: 1: ../lib/pfring_config: not found` error
8. From the `nDPI` root directory, `./autogen.sh && ./configure --with-pcre2` (nBPF and PCRE2 are usually optional, but they are needed to run/update *all* the unit tests)
9. `make`
10. `make check`
11. Update the documentation, adding this new protocol to `doc/protocols.rst`
12. Update the Windows Visual Studio configuration, adding the new c file in `windows/nDPI.vcxproj`

### How to use nDPI to Block Selected Traffic

You can use nDPI to selectively block selected Internet traffic by embedding it onto an application (remember that nDPI is just a library). Both [ntopng](https://github.com/ntop/ntopng) and [nProbe cento](http://www.ntop.org/products/netflow/nprobe-cento/) can do this.

### nDPI Paper Citation

* Deri, Luca, et al. [nDPI: Open-source high-speed deep packet inspection](http://luca.ntop.org/nDPI.pdf) 2014 International Wireless Communications and Mobile Computing Conference (IWCMC). IEEE, 2014.

### Videos and Presentations

* [The Ultimate Guide to nDPI](https://www.youtube.com/watch?v=NndEp7__Y1A) [2025]
* [Using nDPI to solve real life problems: from First Packet Classification to Obfuscated Traffic detection](https://packetfest.ntop.org/slides/Nardi.pdf) [PacketFest, 2025]
* [Passive Network Traffic Fingerprinting](https://fosdem.org/2025/schedule/event/fosdem-2025-5461-passive-network-traffic-fingerprinting/) [FOSDEM, 2025]
* [A Deep Dive Into Traffic Fingerprints using Wireshark](https://www.dropbox.com/scl/fo/zm5amy8fkwz2pj3ojz12a/AMKbeuIToNPH9wCAqB1OWdQ?rlkey=ihnva3yz5heonw59m8br3lxvj&e=2&dl=0) [SharkFest, 2024]
* [Network Traffic Classification for Cybersecurity and Monitoring](https://fosdem.org/2022/schedule/event/using_ndpi_to_efficiently_classify_network_traffic/) [FOSDEM, 2022]
* [Using nDPI for Monitoring and Security](https://archive.fosdem.org/2021/schedule/event/nemondpi/) [FOSDEM, 2021]
* [Knowing the Unknown: How to Monitor and Troubleshoot an Unfamiliar Network](https://www.ntop.org/wp-content/uploads/2017/06/nDPI_Sharkfest_2017.pdf) [SharkFest, 2017]

### nDPI-Related Projects

* [nfstream](https://github.com/aouinizied/nfstream)
* [nDPId](https://github.com/utoni/nDPId)

### DISCLAIMER

While we do our best to detect network protocols, we cannot guarantee that our software is error free and 100% accurate in protocol detection. Please make sure that you respect the privacy of users and you have proper authorization to listen, capture and inspect network traffic.

nDPI is a registered trademark in the US and EU.

[Read more](/en/tools/github/ntop/ndpi?expand=1)

## Categories

[Packet Sniffing & Analysis](/en/categories/packet-sniffing-analysis)[Network Mapping](/en/categories/network-mapping)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Fuzzing](/en/categories/fuzzing)[Network Security](/en/categories/network-security)[Machine Learning](/en/categories/machine-learning)[Intrusion Detection](/en/categories/intrusion-detection)[DNS Analysis](/en/categories/dns-analysis)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories