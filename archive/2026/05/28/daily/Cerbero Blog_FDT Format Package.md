---
title: FDT Format Package
url: https://blog.cerbero.io/fdt-format-package/
source: Cerbero Blog
date: 2026-05-28
fetch_date: 2026-05-29T06:04:48.384046
---

# FDT Format Package

[Skip to content](#content)

[Cerbero Blog](https://blog.cerbero.io/)

Menu

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

# FDT Format Package

We are happy to announce support for the Flattened Device Tree (FDT / DTB) format. The new FDT Format package lets you parse and explore device tree blobs directly within the application, with an interactive tree navigator and per-node binary view.

![](/wp-content/uploads/2026/04/fdt.png)

FDT is the binary format that bootloaders hand to the Linux kernel (and other operating systems) to describe non-discoverable hardware on ARM, ARM64, RISC-V, PowerPC and similar platforms. A DTB encodes the entire hardware topology of a board: CPUs and their cache hierarchy, physical memory regions, on-chip peripherals like UARTs, I²C and SPI controllers, GPIO banks, USB hosts, MMC/SD, Ethernet MACs and GPUs, interrupt routing, clock and power domains, kernel boot arguments and reserved memory regions. The same blob is used as device tree overlays (.dtbo) to patch a base tree at boot for HATs, capes and optional peripherals. DTBs are routinely pulled from boot partitions, firmware images and recovery dumps during security research, IoT analysis and forensic investigations. Having native FDT support in Cerbero Suite means analysts can read out a device’s hardware description — the same information the OS uses to bring the system up — without leaving the analysis environment.

![](https://secure.gravatar.com/avatar/7a86aa69922858b8d41989621fc1ea364aae1e027546f88a54d94ab1ec2187fc?s=49&d=mm&r=g)Author [Erik Pistelli](https://blog.cerbero.io/author/cerbero/)Posted on [May 28, 2026](https://blog.cerbero.io/fdt-format-package/)Categories [Package](https://blog.cerbero.io/category/package/)Tags [Boot](https://blog.cerbero.io/tag/boot/), [Firmware](https://blog.cerbero.io/tag/firmware/), [Linux](https://blog.cerbero.io/tag/linux/)

## Leave a Reply [Cancel reply](/fdt-format-package/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

## Post navigation

[Previous Previous post: LittleFS Format Package](https://blog.cerbero.io/littlefs-format-package/)

Search for:

Search

## Recent Posts

* [FDT Format Package](https://blog.cerbero.io/fdt-format-package/)
* [LittleFS Format Package](https://blog.cerbero.io/littlefs-format-package/)
* [CDEX Format Package](https://blog.cerbero.io/cdex-format-package/)
* [VDEX Format Package](https://blog.cerbero.io/vdex-format-package/)
* [SPIFFS Format Package](https://blog.cerbero.io/spiffs-format-package/)
* [WASM Format & Decompiler Packages](https://blog.cerbero.io/wasm-format-decompiler-packages/)
* [F2FS Format Package](https://blog.cerbero.io/f2fs-format-package/)
* [DotNETBinaryFormatter Format Package](https://blog.cerbero.io/dotnetbinaryformatter-format-package/)
* [EROFS Format Package](https://blog.cerbero.io/erofs-format-package/)
* [ROMFS Format Package](https://blog.cerbero.io/romfs-format-package/)

## Archives

Archives

Select Month
 May 2026  (8)
 April 2026  (13)
 March 2026  (3)
 February 2026  (3)
 January 2026  (2)
 December 2025  (6)
 November 2025  (8)
 October 2025  (9)
 September 2025  (2)
 August 2025  (2)
 July 2025  (2)
 June 2025  (3)
 May 2025  (7)
 April 2025  (4)
 March 2025  (2)
 October 2024  (3)
 September 2024  (1)
 August 2024  (3)
 July 2024  (5)
 June 2024  (2)
 April 2024  (4)
 March 2024  (1)
 February 2024  (1)
 January 2024  (4)
 December 2023  (3)
 November 2023  (7)
 October 2023  (3)
 September 2023  (1)
 July 2023  (1)
 May 2023  (11)
 March 2023  (9)
 February 2023  (3)
 January 2023  (1)
 November 2022  (1)
 September 2022  (2)
 August 2022  (2)
 July 2022  (3)
 June 2022  (2)
 May 2022  (5)
 April 2022  (3)
 March 2022  (4)
 February 2022  (6)
 January 2022  (1)
 November 2021  (4)
 October 2021  (5)
 September 2021  (7)
 June 2021  (1)
 April 2021  (1)
 March 2021  (4)
 February 2021  (1)
 December 2020  (1)
 November 2020  (1)
 October 2020  (1)
 September 2020  (2)
 July 2020  (2)
 January 2020  (1)
 September 2019  (1)
 August 2019  (2)
 July 2019  (1)
 June 2019  (1)
 May 2019  (3)
 April 2019  (2)
 June 2018  (1)
 April 2018  (1)
 March 2018  (1)
 January 2018  (1)
 November 2017  (2)
 March 2017  (5)
 July 2016  (2)
 May 2016  (2)
 April 2016  (1)
 October 2015  (2)
 September 2015  (2)
 June 2015  (2)
 December 2014  (2)
 October 2014  (1)
 September 2014  (3)
 August 2014  (1)
 July 2014  (1)
 December 2013  (2)
 November 2013  (5)
 October 2013  (5)
 September 2013  (6)
 August 2013  (6)
 July 2013  (1)
 June 2013  (4)
 May 2013  (7)
 April 2013  (5)
 March 2013  (3)
 February 2013  (4)
 January 2013  (3)
 December 2012  (3)
 November 2012  (5)
 October 2012  (3)
 September 2012  (1)
 August 2012  (2)
 July 2012  (2)
 June 2012  (2)
 May 2012  (2)
 April 2012  (1)
 March 2012  (6)
 February 2012  (5)
 January 2012  (8)
 November 2011  (1)
 August 2011  (1)

* [Home](https://cerbero.io)
* Products
  + [Cerbero Suite](https://cerbero.io/suite/)
  + [Cerbero Engine](https://cerbero.io/engine/)
* [Packages](https://cerbero.io/packages/)
* [E-Zine](https://cerbero.io/e-zine/)
* [Blog](/)
* Support
  + [User Manual](https://cerbero.io/manual/)
  + [SDK Documentation](https://sdk.cerbero.io/)
  + [FAQ](https://cerbero.io/faq/)
  + [Contact](https://cerbero.io/contact/)
* [Shop](https://cerbero.io/shop/)
  + [My account](https://cerbero.io/my-account/)
  + [Cart](https://cerbero.io/cart/)

[Cerbero Blog](https://blog.cerbero.io/)  [Proudly powered by WordPress](https://wordpress.org/)