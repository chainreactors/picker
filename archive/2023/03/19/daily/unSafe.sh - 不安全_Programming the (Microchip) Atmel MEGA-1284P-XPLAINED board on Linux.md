---
title: Programming the (Microchip) Atmel MEGA-1284P-XPLAINED board on Linux
url: https://buaq.net/go-154082.html
source: unSafe.sh - 不安全
date: 2023-03-19
fetch_date: 2025-10-04T10:01:54.600041
---

# Programming the (Microchip) Atmel MEGA-1284P-XPLAINED board on Linux

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

Programming the (Microchip) Atmel MEGA-1284P-XPLAINED board on Linux

Skip to contentFirst check if your board is detected (after connecting t
*2023-3-18 22:55:6
Author: [acassis.wordpress.com(查看原文)](/jump-154082.htm)
阅读量:36
收藏*

---

[Skip to content](#content)

First check if your board is detected (after connecting the miniusb cable in the board and your computer)

```
$ dmesg
...
[23916.604107] usb 3-3: new full-speed USB device number 11 using xhci_hcd
[23916.753688] usb 3-3: New USB device found, idVendor=03eb, idProduct=2122, bcdDevice=10.00
[23916.753691] usb 3-3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[23916.753692] usb 3-3: Product: XPLAINED CDC
[23916.753693] usb 3-3: Manufacturer: ATMEL
[23916.753695] usb 3-3: SerialNumber: 124XXX000XXX
[23922.052622] cdc_acm 3-3:1.0: ttyACM0: USB ACM device
[23922.052654] usbcore: registered new interface driver cdc_acm
[23922.052655] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
```

So it created the /dev/ttyACM0 device, now we can use it to flash a new firmware or to dump the content of flash memory.

Atmel created an [avrosp](https://maker.pro/forums/threads/atmel-avr-programming-using-avrosp-on-linux-does-avrdude-supportself-programming-bootloaders.186934/) programmer to use with this board and according with their documentation it uses the avr911 protocol. But unfortunately the avrosp is not maintained anymore and we need to find an alternative.

I tried to use avrdude, since it supports the avr911 protocol, but for some strange reason it doesn’t work with this board. First you need to press and hold the SW0 button in the board, press and release the RESET button and after 1 second release the SW0 button. Now you can try:

```
$ avrdude -p atmega1284p -c avr911 -P /dev/ttyACM0 -b57600 -U flash:r:dump.hex:i

Connecting to programmer: .
Found programmer: Id = "AVRBOOT"; type = S
    Software Version = 1.5; No Hardware Version given.
Programmer supports auto addr increment.
Programmer supports buffered memory access with buffersize=256 bytes.

Programmer supports the following devices:

avrdude: error: programmer did not respond to command: select device
avrdude: initialization failed, rc=-1
         Double check connections and try again, or use -F to override
         this check.

avrdude done.  Thank you.
```

After many tests I discovered that avr910 protocol works, but it prints a lot of error messages:

```
$ sudo avrdude -p atmega1284p -c avr910 -P /dev/ttyACM0 -b57600 -F -u -U flash:r:dump.hex:i

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
avrdude: reading flash memory:

Reading |                                                    | 0% 0.00savrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
Reading | #                                                  | 1% 0.35savrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
Reading | #                                                  | 2% 0.60savrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
Reading | ##                                                 | 3% 0.85savrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
Reading | ##                                                 | 4% 1.10savrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
avrdude: error: programmer did not respond to command: set addr
Reading | ###                                                | 5% 1.35savrdude: error: programmer did not respond to command: set addr
```

Note that the progress bar of Reading is advancing! Then if you wait it will finish and read the flash correctly.

文章来源: https://acassis.wordpress.com/2023/03/18/programming-the-microchip-atmel-mega-1284p-xplained-board-on-linux/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)