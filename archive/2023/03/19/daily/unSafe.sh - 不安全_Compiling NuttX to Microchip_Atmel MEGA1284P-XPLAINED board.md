---
title: Compiling NuttX to Microchip/Atmel MEGA1284P-XPLAINED board
url: https://buaq.net/go-154094.html
source: unSafe.sh - 不安全
date: 2023-03-19
fetch_date: 2025-10-04T10:01:50.623552
---

# Compiling NuttX to Microchip/Atmel MEGA1284P-XPLAINED board

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

Compiling NuttX to Microchip/Atmel MEGA1284P-XPLAINED board

Skip to contentI just ported NuttX to Atmel MEGA1284P-XPLAINED board usi
*2023-3-18 23:48:29
Author: [acassis.wordpress.com(查看原文)](/jump-154094.htm)
阅读量:31
收藏*

---

[Skip to content](#content)

I just ported NuttX to Atmel MEGA1284P-XPLAINED board using as base the moteino-mega board that is very similar. Main difference is the 16MHz crystal that became 11.0592MHz in the MEGA1284P-XPLAINED.

These are the steps to compile NuttX:

1) Install the AVR GCC toolchain:

```
$ sudo apt install gcc-avr avr-libc
```

2) Configure NuttX to compile to this board:

```
$ ./tools/configure.sh mega1284p-xplained:nsh
$ make
```

3) Flash the generated nuttx.hex file:

```
$ sudo avrdude -p atmega1284p -c avr910 -P /dev/ttyACM0 -b57600 -F -u -U flash:w:nuttx.hex:i
```

For some strange reason it is failing:

```
avrdude: avr910_recv(): programmer is not responding
Found programmer: Id = "AVRBOOT"; type = S
    Software Version = 1.5; Hardware Version = ?.
Programmer supports auto addr increment.
Programmer supports buffered memory access with buffersize = 256 bytes.

Programmer supports the following devices:

avrdude: warning: selected device is not supported by programmer: m1284p
avrdude: error: programmer did not respond to command: select device
avrdude: AVR device initialized and ready to accept instructions

Reading | ################################################## | 100% 0.09s

avrdude: Device signature = 0x97050d
avrdude: Expected signature for ATmega1284P is 1E 97 05
avrdude: NOTE: "flash" memory has been specified, an erase cycle will be performed
         To disable this feature, specify the -D option.
avrdude: erasing chip
avrdude: error: programmer did not respond to command: chip erase
avrdude: reading input file "nuttx.hex"
avrdude: writing flash (55260 bytes):

Writing | ################################################## | 100% 23.64s

avrdude: 55260 bytes of flash written
avrdude: verifying flash memory against nuttx.hex:
avrdude: load data flash data from input file nuttx.hex:
avrdude: input file nuttx.hex contains 55260 bytes
avrdude: reading on-chip flash data:

Reading
...
Reading | ################################################## | 100% 10.89s

avrdude: verifying ...
avrdude: verification error, first mismatch at byte 0x0000
         0x0d != 0x0c
avrdude: verification error; content mismatch
avrdude: error: programmer did not respond to command: leave prog mode

avrdude done.  Thank you.
```

So, it is not working yet, but we are near!!! Stay tuned!

文章来源: https://acassis.wordpress.com/2023/03/18/compiling-nuttx-to-microchip-atmel-mega1284p-xplained-board/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)