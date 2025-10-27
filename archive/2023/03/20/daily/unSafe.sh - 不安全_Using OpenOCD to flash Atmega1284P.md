---
title: Using OpenOCD to flash Atmega1284P
url: https://buaq.net/go-154219.html
source: unSafe.sh - 不安全
date: 2023-03-20
fetch_date: 2025-10-04T10:04:40.193463
---

# Using OpenOCD to flash Atmega1284P

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

Using OpenOCD to flash Atmega1284P

Skip to contentAfter facing issues with avrdude using the native program
*2023-3-19 23:52:9
Author: [acassis.wordpress.com(查看原文)](/jump-154219.htm)
阅读量:28
收藏*

---

[Skip to content](#content)

After facing issues with avrdude using the native programmer from Mega1284P-Xplained board I decided to test OpenOCD to flash the board.

Using a J-Link V8 programmer connected to the board this way:

JLINK MEGA1284-XPLAINED

VTref VCC (5V)

TDI TDI

TMS TMS

TCK TCK

TDO TDO

RESET RESET

GND GND

```
$ sudo openocd -f interface/jlink.cfg -f target/atmega128.cfg -c init -c "reset halt" -c "flash write_image erase nuttx.hex 0x00000000"
Open On-Chip Debugger 0.11.0
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
Info : auto-selecting first available session transport "jtag". To override use 'transport select <transport>'.
Info : J-Link ARM V8 compiled Nov 28 2014 13:44:46
Info : Hardware version: 8.00
Info : VTarget = 3.319 V
Info : clock speed 4500 kHz
Info : JTAG tap: avr.cpu tap/device found: 0x1970503f (mfg: 0x01f (Atmel), part: 0x9705, ver: 0x1)
Warn : JTAG tap: avr.cpu       UNEXPECTED: 0x1970503f (mfg: 0x01f (Atmel), part: 0x9705, ver: 0x1)
Error: JTAG tap: avr.cpu  expected 1 of 1: 0x8970203f (mfg: 0x01f (Atmel), part: 0x9702, ver: 0x8)
Error: Trying to use configured scan chain anyway...
Warn : Bypassing JTAG setup events due to errors
Info : JTAG tap: avr.cpu tap/device found: 0x1970503f (mfg: 0x01f (Atmel), part: 0x9705, ver: 0x1)
Warn : JTAG tap: avr.cpu       UNEXPECTED: 0x1970503f (mfg: 0x01f (Atmel), part: 0x9705, ver: 0x1)
Error: JTAG tap: avr.cpu  expected 1 of 1: 0x8970203f (mfg: 0x01f (Atmel), part: 0x9702, ver: 0x8)
Error: Trying to use configured scan chain anyway...
Warn : Bypassing JTAG setup events due to errors
Info : device id = 0x1970503f
Info : target device is atmega1284p
auto erase enabled
wrote 55296 bytes from file nuttx.hex in 1.429967s (37.763 KiB/s)

Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
```

文章来源: https://acassis.wordpress.com/2023/03/19/using-openocd-to-flash-atmega1284p/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)