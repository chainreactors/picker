---
title: Hacking the My Arcade Contra Pocket Player - Part II
url: https://trustedsec.com/blog/hacking-the-my-arcade-contra-pocket-player-part-ii
source: TrustedSec
date: 2026-11-17
fetch_date: 2026-11-18T09:22:30.911607
---

# Hacking the My Arcade Contra Pocket Player - Part II

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Hacking the My Arcade Contra Pocket Player - Part II](https://trustedsec.com/blog/hacking-the-my-arcade-contra-pocket-player-part-ii)

November 17, 2026

# Hacking the My Arcade Contra Pocket Player - Part II

Written by
Rob Simon

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HackingMyArcadeContraPocketPlayerPart2_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1794318214&s=cec7cad34d5982be3810d16767a3a24c)

Table of contents

* [Analyzing the Firmware Dump](#Dump)
* [Unpacking, Repacking, and Reflashing](#URR)
* [Inside the Root Filesystem](#Inside)
* [First Attempt: Swap the ROM](#First)
* [Second Attempt: Using FBAlpha](#Second)
* [Want to Mod Your Own?](#Own)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#4c733f392e26292f38710f24292f27697e7c233938697e7c3824253f697e7c2d3e38252f2029697e7c2a3e2321697e7c183e393f3829281f292f697e7d6a2d213c772e23283571042d2f2725222b697e7c382429697e7c0135697e7c0d3e2f2d2829697e7c0f2322383e2d697e7c1c232f272938697e7c1c202d35293e697e7c61697e7c1c2d3e38697e7c0505697f0d697e7c2438383c3f697f0d697e0a697e0a383e393f3829283f292f622f2321697e0a2e20232b697e0a242d2f2725222b61382429612135612d3e2f2d2829612f2322383e2d613c232f272938613c202d35293e613c2d3e38612525 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhacking-the-my-arcade-contra-pocket-player-part-ii "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Hacking%20the%20My%20Arcade%20Contra%20Pocket%20Player%20-%20Part%20II%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhacking-the-my-arcade-contra-pocket-player-part-ii "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhacking-the-my-arcade-contra-pocket-player-part-ii&mini=true "Share on LinkedIn")

Reports of my death have been greatly exaggerated.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ContraPrt2_RobSimon/update.png?w=320&q=90&auto=format&fit=max&dm=1794261390&s=ebc1ab53ac4fc65b93c202ac9059ea48)

Not Dead Yet

Sorry for the long delay. No, I didn't die. I just got busy and totally forgot to come back to this project 😁

In [Part I](https://trustedsec.com/blog/hacking-the-my-arcade-contra-pocket-player-part-i), we identified the Rockchip RK3128 SoC and Winbond SPI NAND flash inside the Contra Pocket Player, and dumped the full 128MB flash image over USB using RockUSB recovery mode. In this post, we'll analyze the firmware dump, explore the root filesystem, and work through the process of swapping in custom games.

## Analyzing the Firmware Dump

Looking at the NAND dump with a hex editor, the `0x55AA` boot signature at offset `0x1FE` signals a valid MBR. The single partition entry has type `0xEE`, marking it as a GPT protective MBR. At offset `0x200`, the `EFI PART` magic string confirms a GUID Partition Table.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ContraPrt2_RobSimon/EFI_PART.png?w=320&q=90&auto=format&fit=max&dm=1794261358&s=4e4c22b3addccaee920076017e2e7d45)

EFI PART Magic at Offset 0x200

The GPT contains five partitions:

| # | Name | Size | Offset | Magic | Content |
| --- | --- | --- | --- | --- | --- |
| 1 | `uboot` | 1.0 MiB | 0x400000 | `LOADER` | U-Boot bootloader |
| 2 | `trust` | 2.0 MiB | 0x500000 | `TOS` | ARM Trusted Firmware |
| 3 | `boot` | 9.0 MiB | 0x700000 | `ANDROID!` | Linux kernel + ramdisk |
| 4 | `rootfs` | 65.0 MiB | 0x1000000 | `hsqs` | SquashFS filesystem |
| 5 | `userdata` | 26.7 MiB | 0x5100000 |  | User data (ext2) |

There is a ~4 MiB gap between the GPT entries and the first partition. This region isn't listed in the partition table, but some research into Rockchip SoCs revealed it contains the IDB (ID Block) loader, a first-stage bootloader that the SoC's boot ROM loads from a hardcoded offset on the flash to initialize DDR memory and hand off to U-Boot. Five redundant copies are written starting at sector 64, with the rest of the gap as zero padding. Decrypting the first sector with Rockchip's RC4 key (documented in [U-Boot's rkcommon.c](https://github.com/u-boot/u-boot/blob/master/tools/rkcommon.c)) reveals the standard `0x0FF0AA55` IDBLOCK magic. While this isn't important for the mod, it's useful to document the full NAND layout.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ContraPrt2_RobSimon/firmware-layout.png?w=320&q=90&auto=format&fit=max&dm=1794261360&s=555bf0530c3d33b1aa2db0d5384b9353)

NAND Flash Layout

The first three partitions (`uboot`, `trust`, `boot`) handle the boot chain: U-Boot loads ARM Trusted Firmware, which launches the Linux kernel packaged as an Android boot image. From there, BusyBox init takes over and runs the startup scripts in `/etc/init.d/`....