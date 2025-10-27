---
title: Bootlicker - A Generic UEFI Bootkit Used To Achieve Initial Usermode Execution
url: https://buaq.net/go-166106.html
source: unSafe.sh - 不安全
date: 2023-05-29
fetch_date: 2025-10-04T11:36:51.983761
---

# Bootlicker - A Generic UEFI Bootkit Used To Achieve Initial Usermode Execution

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

![](https://8aqnet.cdn.bcebos.com/2ad5bb26c0cb8732f97f7ea5a2bdd4bd.jpg)

Bootlicker - A Generic UEFI Bootkit Used To Achieve Initial Usermode Execution

bootlicker is a legacy, extensible UEFI firmware rootkit targeting vmware hypervisor virtual
*2023-5-28 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-166106.htm)
阅读量:34
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiqmvN5TN1pOgXQNDoLAS5YXMM00eZDqHsOqgncNPAsblCSx9bVnI9XCygKz6aNfElH85ULA7-LkFMogExSf8KOQ3y-IqRECXWY2AMwwGXPdt4dusLyEfOsdo5W4A0hiBFCJwwrUgIJnX-XqYkRmL4NNACY5ZxSG6DrjpGnn0V_TiLxqKrUAP0dAhWlrA=w640-h234)](https://blogger.googleusercontent.com/img/a/AVvXsEiqmvN5TN1pOgXQNDoLAS5YXMM00eZDqHsOqgncNPAsblCSx9bVnI9XCygKz6aNfElH85ULA7-LkFMogExSf8KOQ3y-IqRECXWY2AMwwGXPdt4dusLyEfOsdo5W4A0hiBFCJwwrUgIJnX-XqYkRmL4NNACY5ZxSG6DrjpGnn0V_TiLxqKrUAP0dAhWlrA)

bootlicker is a legacy, extensible UEFI [firmware](https://www.kitploit.com/search/label/Firmware "firmware") rootkit targeting vmware [hypervisor](https://www.kitploit.com/search/label/Hypervisor "hypervisor") virtual machines. It is designed to achieve initial code execution within the context of the windows kernel, regardless of security settings configured.

## Architecture

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiqmvN5TN1pOgXQNDoLAS5YXMM00eZDqHsOqgncNPAsblCSx9bVnI9XCygKz6aNfElH85ULA7-LkFMogExSf8KOQ3y-IqRECXWY2AMwwGXPdt4dusLyEfOsdo5W4A0hiBFCJwwrUgIJnX-XqYkRmL4NNACY5ZxSG6DrjpGnn0V_TiLxqKrUAP0dAhWlrA=w640-h234)](https://blogger.googleusercontent.com/img/a/AVvXsEiqmvN5TN1pOgXQNDoLAS5YXMM00eZDqHsOqgncNPAsblCSx9bVnI9XCygKz6aNfElH85ULA7-LkFMogExSf8KOQ3y-IqRECXWY2AMwwGXPdt4dusLyEfOsdo5W4A0hiBFCJwwrUgIJnX-XqYkRmL4NNACY5ZxSG6DrjpGnn0V_TiLxqKrUAP0dAhWlrA)

bootlicker takes its design from the legacy CosmicStrain, MoonBounce, and ESPECTRE rootkits to achive arbitrary code excution without triggering [patchguard](https://www.kitploit.com/search/label/PatchGuard "patchguard") or other related security mechanisms.

After initial insertion into a UEFI driver firmware using the the [injection utility](https://github.com/realoriginal/bootlicker/blob/master/scripts/inject.py "injection utility"), the [shellcodes](https://www.kitploit.com/search/label/Shellcodes "shellcodes") [EfiMain](https://github.com/realoriginal/bootlicker/blob/master/bootkit/EfiMain.c "EfiMain") achieves execution as the host starts up, and inserts a hook into the UEFI firmware's [ExitBootServices routine](https://github.com/realoriginal/bootlicker/blob/master/bootkit/ExitBootServices.c "ExitBootServices routine"). The ExitBootServices routine will then, on execution, find the source caller of the function, and if it matches WinLoad.EFI, attempts to find the unexported winload.efi!OslArchTransferToKernel routine, which will allow us to att ack the booting kernel before it achieves its initial execution.

Once [OslArchTransferToKernel](https://github.com/realoriginal/bootlicker/blob/master/bootkit/OslArchTransferToKernel.c "OslArchTransferToKernel") executes, it will search for the ACPI.SYS driver, find the `.rsrc` PE section, and inject a small stager shellcode entrypoint called [DrvMain](https://github.com/realoriginal/bootlicker/blob/master/bootkit/DrvMain.c "DrvMain") to copy over a larger payload that will act as our kernel implant.

### Resources

Entirely based upon d\_olex / cr4sh's [DmaBackdoorBoot](https://github.com/Cr4sh/s6_pcie_microblaze/tree/master/python/payloads/DmaBackdoorBoot "DmaBackdoorBoot")

### Epilogue

This code is apart of a larger project I've been working on that on / off in between burnout, like most of the concepts I've produced over the years under various aliases, will never see the light of day. Some of the code comments I've been to lazy to strip out that refer to unrelated functiaonlity, despite it being previously present. Do not expect this to work out of the box, some slight modifications are certainly necessary.

Bootlicker - A Generic UEFI Bootkit Used To Achieve Initial Usermode Execution
![Bootlicker - A Generic UEFI Bootkit Used To Achieve Initial Usermode Execution](https://blogger.googleusercontent.com/img/a/AVvXsEiqmvN5TN1pOgXQNDoLAS5YXMM00eZDqHsOqgncNPAsblCSx9bVnI9XCygKz6aNfElH85ULA7-LkFMogExSf8KOQ3y-IqRECXWY2AMwwGXPdt4dusLyEfOsdo5W4A0hiBFCJwwrUgIJnX-XqYkRmL4NNACY5ZxSG6DrjpGnn0V_TiLxqKrUAP0dAhWlrA=s72-w640-c-h234)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/05/bootlicker-generic-uefi-bootkit-used-to.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)