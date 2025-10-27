---
title: UNI-T UTD2062CE USB Device
url: https://buaq.net/go-169081.html
source: unSafe.sh - 不安全
date: 2023-06-17
fetch_date: 2025-10-04T11:46:48.972662
---

# UNI-T UTD2062CE USB Device

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

![](https://8aqnet.cdn.bcebos.com/799e4ca6a6e4456c959897ce6eb912bf.jpg)

UNI-T UTD2062CE USB Device

Skip to contentThis is the dmesg output for my UNI-T UTD2062CE:[ 220
*2023-6-16 20:49:50
Author: [acassis.wordpress.com(查看原文)](/jump-169081.htm)
阅读量:18
收藏*

---

[Skip to content](#content)

This is the dmesg output for my UNI-T UTD2062CE:

```
[ 2206.973955] usb 2-3: new high-speed USB device number 10 using xhci_hcd
[ 2207.196271] usb 2-3: New USB device found, idVendor=5656, idProduct=0834, bcdDevice= 0.00
[ 2207.196282] usb 2-3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 2207.196286] usb 2-3: Product: DSO
[ 2207.196290] usb 2-3: Manufacturer: DSO
```

And lsusb show more some info:

```
$ lsusb -v
Bus 002 Device 010: ID 5656:0834 Uni-Trend Group Limited DSO
Couldn't open device, some information will be missing
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass            0
  bDeviceSubClass         0
  bDeviceProtocol         0
  bMaxPacketSize0        64
  idVendor           0x5656 Uni-Trend Group Limited
  idProduct          0x0834
  bcdDevice            0.00
  iManufacturer           1 DSO
  iProduct                2 DSO
  iSerial                 0
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x0020
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0
    bmAttributes         0x40
      (Missing must-be-set bit!)
      Self Powered
    MaxPower              100mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass       255 Vendor Specific Class
      bInterfaceSubClass      0
      bInterfaceProtocol      0
      iInterface              0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x06  EP 6 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
```

We can use the ut2XXX project to interface with the oscilloscope:

```
$ git clone https://github.com/mandl/ut2XXX
$ cd ut2XXX
$ sudo cp ./udev_rules/99-uni-t.rules /etc/udev/rules.d/
$ sudo udevadm control --reload-rules && sudo udevadm trigger
$ sudo apt-get install python-qt5
$ sudo apt install pyqt5-dev-tools
$ sudo apt install python3-usb
```

Finally run the python script:

```
$ ./simpleDSO.py -v
```

[![](https://live.staticflickr.com/65535/52978732979_268f5300de_o.png)](https://live.staticflickr.com/65535/52978732979_268f5300de_o.png)

文章来源: https://acassis.wordpress.com/2023/06/16/uni-t-utd2062ce-usb-device/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)