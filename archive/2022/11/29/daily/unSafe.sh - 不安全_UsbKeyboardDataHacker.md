---
title: UsbKeyboardDataHacker
url: https://buaq.net/go-137605.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:09.314882
---

# UsbKeyboardDataHacker

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

UsbKeyboardDataHacker

UsageUsage : python UsbKeyboardHacker.py data.pcapTips : To use thi
*2022-11-28 18:49:0
Author: [github.com(查看原文)](/jump-137605.htm)
阅读量:32
收藏*

---

## Usage

```
Usage :
        python UsbKeyboardHacker.py data.pcap
Tips :
        To use this python script , you must install the tshark first.
        You can use `sudo apt-get install tshark` to install it
Author :
        WangYihang <[email protected]>
        If you have any questions , please contact me by email.
        Thank you for using.
```

## Example

### Step1: Get data

```
[email protected]:~/UsbKeyboardDataHacker$ tshark -r ./example.pcap -T fields -e usb.capdata
00:00:09:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0f:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:04:00:00:00:00:00
00:00:00:00:00:00:00:00
00:00:0a:00:00:00:00:00
00:00:00:00:00:00:00:00
20:00:00:00:00:00:00:00
20:00:2f:00:00:00:00:00
...
```

### Step2: decode

```
[email protected]:~/UsbKeyboardDataHacker$ python UsbKeyboardDataHacker.py ./example.pcap
[-] Unknow Key : 01
[-] Unknow Key : 01
[+] Found : flag{pr355_0nwards_a2fee6e0}
```

### Additional Video

* <https://www.youtube.com/watch?v=unBwmcpXbhE>

## Acknowledgment

* [@ChristopherKai](https://github.com/ChristopherKai)
* [@seadog007](https://github.com/seadog007)
* [@hurricane618](https://github.com/hurricane618)

文章来源: https://github.com/y35uishere/UsbKeyboardDataHacker
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)