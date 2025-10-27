---
title: A Patchdiffing Journey – TP-Link Omada
url: https://blog.compass-security.com/2024/08/a-patchdiffing-journey-tp-link-omada/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-21
fetch_date: 2025-10-06T18:18:10.572810
---

# A Patchdiffing Journey – TP-Link Omada

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [A Patchdiffing Journey – TP-Link Omada](https://blog.compass-security.com/2024/08/a-patchdiffing-journey-tp-link-omada/ "A Patchdiffing Journey – TP-Link Omada")

[August 20, 2024](https://blog.compass-security.com/2024/08/a-patchdiffing-journey-tp-link-omada/ "A Patchdiffing Journey – TP-Link Omada")
 /
[Yves Bieri](https://blog.compass-security.com/author/ybieri/ "Posts by Yves Bieri")
 /
[0 Comments](https://blog.compass-security.com/2024/08/a-patchdiffing-journey-tp-link-omada/#respond)

## Introduction

Last year we participated in the Pwn2Own 2023 Toronto competition and successfully exploited the Synology BC500 camera.

The competition featured a wide range of targets, including popular routers in the SOHO (Small Office/Home Office) Smashup category. This category consists of two stages. An initial stage, where you have to compromise a router on the WAN side, and a second stage where you pivot to one of the other targets (e.g. the Synology BC500 camera) in the LAN. Finding two exploits and chaining them together is challenging but significantly increases the bounty payout.

Once we had an exploitable bug for the Synology camera, we decided to try to participate in the SOHO Smashup category and bought the TP-Link Omada Gigabit VPN Router ER605 (TL-R605) V2 router. But, finalizing the camera exploit took more time than we hoped, thus due to time constraints, we were unable to thoroughly examine the TP-Link router before the event.

However, the DEVCORE Internship Program team managed to exploit a bug in the TP link router during Pwn2Own. So I was naturally curious and wanted to figure out how difficult it would be to recreate that exploit having access only to a high-level bug description and the firmware.

## Patch Diffing Process

### Extract Binaries

To start off, I read the ZDI advisory for the discovered weakness: <https://www.zerodayinitiative.com/advisories/ZDI-24-085/>

> **Title: *(Pwn2Own) TP-Link Omada ER605 DHCPv6 Client Options Stack-based Buffer Overflow Remote Code Execution Vulnerability***
>
> Vulnerability Details:
> *The specific flaw exists within the handling of DHCP options. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.*
>
> *This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Omada ER605 routers. Authentication is not required to exploit this vulnerability.*

This provides first valuable information. It describes that no authentication is required to exploit this bug. It also mentions that a stack buffer overflow occurs when handing DHCP options and finally, the title mentions that the vulnerability is in the DHCPv6 client.

The advisory also mentions that the bug was fixed in firmware version `ER605(UN)_V2_2.2.4 Build 20240119`. Armed with this information, we can start the patch diffing process.

The first step is to download the two firmware versions we want to diff. Luckily, the firmware can be downloaded directly from the TP-link website: <https://www.tp-link.com/en/support/download/er605/#Firmware>

From the advisory, we know that in version `ER605(UN)_V2_2.2.4 Build 20240119` the bug was fixed. There exists a version `2.2.3` that was released in December, so after the Pwn2Own competition. I ignored this version and instead downloaded version `ER605(UN)_V2_2.2.2 Build 20231017` that was released just a few days prior to Pwn2Own.

The downloaded ZIP file contains a license and a `.bin` file:

```
$ unzip ER605\(UN\)_v2_2.2.4\ Build\ 20240119.zip
Archive:  ER605(UN)_v2_2.2.4 Build 20240119.zip
  inflating: ER605v2_un_2.2.4_20240119-rel44368_up_2024-01-19_12.21.20.bin
  inflating: GPL License Terms.pdf
```

I used [`unblob`](https://unblob.org/) to analyze and extract the `.bin` file:

```
$ ls ER605v2_un_2.2.2_20231017-rel68869_up_2023-10-17_19.23.22.bin_extract
0-594735.unknown  20879997-21238478.unknown  2438047-2495051.unknown  2495051-20879997.squashfs_v4_le  _2495051-20879997.squashfs_v4_le.extracted  594735-2438047.lzma_extract
```

The extraction is not perfect but reveals that there is a squashfs embedded in the .bin file. Using binwalk, the squashfs can be extracted:

```
$ binwalk -eM 2495051-20879997.squashfs_v4_le
```

```
$ ls _2495051-20879997.squashfs_v4_le.extracted/squashfs-root
bin  dev  etc  lib  mnt  overlay  proc  rom  root  sbin  sys  tmp  usr  var  www
```

After doing this for both firmware versions, we now can retrieve both the vulnerable and patched DHCPv6 client binaries. The DHCPv6 client binary is called `dhcp6c` and located at `/usr/sbin/dhcp6c`.

### BinDiff

To compare the two binaries, I used BinDiff (<https://www.zynamics.com/bindiff.html>). BinDiff is a tool designed to compare binary files and highlight the differences between them. It integrates with multiple disassemblers and shows where code changed between two versions of the binary.

The result of comparing the two dhcp6c binaries looks like this:

[![](https://blog.compass-security.com/wp-content/uploads/2024/06/bindiff.png)](https://blog.compass-security.com/wp-content/uploads/2024/06/bindiff.png)

We can see that functions `sub_404364` and `sub 405F08` changed while the rest of the code stayed the same. Thus, I started analyzing those two functions to see what changed. The diagram below shows that function `sub_404364` added some checks around the `vsprintf` call.

[![](https://blog.compass-security.com/wp-content/uploads/2024/06/bindiff_sub_404364.png)](https://blog.compass-security.com/wp-content/uploads/2024/06/bindiff_sub_404364.png)

The disassembly from BinDiff is not perfect but when looking at the decompilation it becomes clear, that the `vsprintf` has been replaced by a `vsnprintf`.

The code in the new version:

```
int __fastcall sub_404364(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8)
{
  char v9[4096]; // [sp+18h] [-1010h] BYREF
  int *v10; // [sp+1018h] [-10h]

  a6 = a2;
  a7 = a3;
  a8 = a4;
  v10 = &a6;
  vsnprintf(v9, 0x1000, a1);
  return sub_4042FC(v9);
}
```

The code in the old version:

```
int __fastcall sub_404364(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8)
{
  char v9[4096]; // [sp+18h] [-1010h] BYREF
  int *v10; // [sp+1018h] [-10h]

  a6 = a2;
  a7 = a3;
  a8 = a4;
  v10 = &a6;
  vsprintf(v9, a1);
  return 4042FC ((int)v9);
}
```

But then this function is never called by anyone. Thus, this probably is not the function that was exploited. Interesting though is that `vsprintf` was replaced by a `vsnprintf` in `sub_404364`, but in the parent function there still remains a vsprintf call with potentially untrusted input. This looks like a partial fix in some testing functionality.

As `sub_404364` is not interesting, hopefully `sub 405F08` will reveal the original bug.

The function is large and BinDiff thus fails to display the differences. Thus, it took some manual effort to compare the disassembly and decompilation. This function consists of a large switch statement. After some reversing, I discovered that there was a change introduced in case 0x40.

In the vulnerable binary, the code looks like this:

```
case 0x40:
        if ( v61 )
        {
          v65 = (const char *)(a3 + 0xE8);
          if ( a3 != 0xFFFFFF18 )
        ...