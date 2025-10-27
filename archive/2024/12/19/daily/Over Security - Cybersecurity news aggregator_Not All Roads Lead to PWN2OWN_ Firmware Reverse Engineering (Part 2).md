---
title: Not All Roads Lead to PWN2OWN: Firmware Reverse Engineering (Part 2)
url: https://www.hacktivesecurity.com/index.php/2024/12/18/not-all-roads-lead-to-pwn2own-firmware-reverse-engineering-part-2/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-19
fetch_date: 2025-10-06T19:41:41.720088
---

# Not All Roads Lead to PWN2OWN: Firmware Reverse Engineering (Part 2)

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Reverse Engineering](https://www.hacktivesecurity.com/blog/category/reverse-engineering/)
* Not All Roads Lead to PWN2OWN: Firmware Reverse Engineering (Part 2)

[Reverse Engineering](https://www.hacktivesecurity.com/blog/category/reverse-engineering/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/12/noPWN2OWN_2.jpg)

\_ [December 18, 2024](https://www.hacktivesecurity.com/blog/2024/12/18/not-all-roads-lead-to-pwn2own-firmware-reverse-engineering-part-2/)\_ [Alessandro Groppo](https://www.hacktivesecurity.com/blog/author/kiks/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2024/12/18/not-all-roads-lead-to-pwn2own-firmware-reverse-engineering-part-2/#respond)

### Not All Roads Lead to PWN2OWN: Firmware Reverse Engineering (Part 2)

## Introduction

In the [previous blog post](https://www.hacktivesecurity.com/index.php/2024/12/10/not-all-roads-lead-to-pwn2own-hardware-hacking-part-1/), we have dissected the Lorex 2K IP Camera from an hardware perspective. The main objectives were to obtain an an interactive shell and extract the firmware for further analysis. Although the first point was not achieved due to the target hardening, we [were able](https://www.hacktivesecurity.com/index.php/2024/12/10/not-all-roads-lead-to-pwn2own-hardware-hacking-part-1/) to extract the firmware. Since we also had the capability to re-flash the firmware with a modified version of it, we could re-create a new version (a custom firmware) with extra debug capabilities to finally embrace the Vulnerability Discovery phase with a solid target. However, as we have introduced in the first post of this series, this was also our sentence to the overall objective (0day) failure. We were able to re-create a custom firmware with custom binaries and with an interactive shell, but with a limit of 40 seconds. The limit was, presumably, some sort of integrity validation at later stages of the booting process. Since we were able to execute arbitrary commands to the target system through a customized firmware, we were thinking that we were just a little bit far from a stable shell. This “little far” turns out into the reversing (and emulation) of the whole filesystem image, multiple ARM32 binaries and kernel modules that were also patched to bypass what we thought was the root cause of the reboot trigger. This whole process took us too much time and effort (~75%) compared to what we have allocated for the whole project (two weeks). However, it was a really instructive, fun and interesting experience and that’s why today we are sharing further details. If you are interested in using binwalk, qemu, bash/python scripting, dd, Binary Ninja, Ghidra, cross compiling and these topics, hope you will enjoy this post.

## Firmware analysis

From the [last blog post](https://www.hacktivesecurity.com/index.php/2024/12/10/not-all-roads-lead-to-pwn2own-hardware-hacking-part-1/), we have extracted the firmware blob that we have directly passed to [binwalk](https://github.com/ReFirmLabs/binwalk) to search for the first signals of self contained images. binwalk is a really interesting and helpful tool that can be used to identify images mainly through magic bytes inside a blob of data. Usually, a [firmware](https://en.wikipedia.org/wiki/Firmware) is a just series of bytes that comprehends at least the boot loader, the kernel, the root filesystem and a series of filesystem images that can be mounted and used to store multiple types of data based on the needs.

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/12/Pasted-image-20241216121043-1024x312.png)

With this output, we have clearer overview of self contained images in the firmware. binwalk offers the `-E` option that permits to automatically extract all images that it is able to identify in the data. Usually, this is enough to have a valid working image but you have to trust its extraction process (more on that later). By extracting the whole content, an interesting file called `partitionV2.txt`, part of the firmware image, contains the partitioning map of the image:

```
# Version=3
#       name                cs         offset              size         mask_flags     fs_flags      fs_type         mount_cmd                                                        backup_off
  U-Boot,             0, 0x0000000000000000,    0x0000000000030000,             RW,                ,             ,                           ,                 ...