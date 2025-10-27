---
title: Testing RISC-V 64-bit on NuttX RTOS running on QEMU
url: https://buaq.net/go-163660.html
source: unSafe.sh - 不安全
date: 2023-05-17
fetch_date: 2025-10-04T11:37:12.603194
---

# Testing RISC-V 64-bit on NuttX RTOS running on QEMU

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

![]()

Testing RISC-V 64-bit on NuttX RTOS running on QEMU

After cloning nuttx and nuttx-apps repositories:$ cd nuttxspace/nuttx$ .
*2023-5-16 23:25:20
Author: [acassis.wordpress.com(查看原文)](/jump-163660.htm)
阅读量:40
收藏*

---

After cloning nuttx and nuttx-apps repositories:

```
$ cd nuttxspace/nuttx
$ ./tools/configure.sh rv-virt:nsh64
$ make -j

/* Lets see its size */

$ ls -l nuttx
-rwxrwxr-x 1 alan alan 3019360 mai 16 12:19 nuttx

$ riscv64-unknown-elf-size nuttx
   text	   data	    bss	    dec	    hex	filename
 164688	    677	   8544	 173909	  2a755	nuttx
```

Time to run it!

```
$ qemu-system-riscv64 -semihosting -M virt,aclint=on -cpu rv64 -smp 8 -bios none -kernel nuttx -nographic

NuttShell (NSH) NuttX-12.1.0
nsh> uname -a
NuttX 12.1.0 76ece3cf8d May 16 2023 12:19:28 risc-v rv-virt
nsh>
```

文章来源: https://acassis.wordpress.com/2023/05/16/testing-risc-v-64-bit-on-nuttx-rtos-running-on-qemu/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)