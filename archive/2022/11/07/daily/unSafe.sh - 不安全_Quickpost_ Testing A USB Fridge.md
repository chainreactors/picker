---
title: Quickpost: Testing A USB Fridge
url: https://buaq.net/go-134422.html
source: unSafe.sh - 不安全
date: 2022-11-07
fetch_date: 2025-10-03T21:51:23.365416
---

# Quickpost: Testing A USB Fridge

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

![](https://8aqnet.cdn.bcebos.com/0c10a7965075dbaa1c2a96badff026ee.jpg)

Quickpost: Testing A USB Fridge

Quickpost: Testing A USB Fridge A couple years ago, I received a USB fridge from N
*2022-11-6 22:50:1
Author: [blog.didierstevens.com(查看原文)](/jump-134422.htm)
阅读量:17
收藏*

---

### Quickpost: Testing A USB Fridge

A couple years ago, I received a USB fridge from NVISO’s Secret Santa.

![](https://didierstevens.files.wordpress.com/2022/11/20221106-144944.png)

It uses a [Peltier element](https://en.wikipedia.org/wiki/Thermoelectric_cooling) with a fan.

I did the following test: overnight, I let the fridge run for 12 hours. It contained an Aluminum can filled with water at room temperature (around 17° C).

I used a power meter to measure the electric energy consumption, and a multimeter with a [thermocouple](https://en.wikipedia.org/wiki/Thermocouple) (type K) to measure the water temperature. The thermocouple was at the bottom of the water, not touching the bottom of the can.

The USB fridge consumed 60.717 Wh over that period, and the water temperature (at the bottom) was around 14.7 °C when I stopped the test. After the test, I moved the thermocouple to the top of the water, and there the temperature was 16.9 °C.

My multimeter logged the temperature every 60 seconds, resulting in this chart:

![](https://didierstevens.files.wordpress.com/2022/11/image.png)

Notice that the first 12 minutes, the temperature rises a bit, and then starts to lower (I’ll do more experiments to try to figure out why it rises first). And then, when the cooling starts, it gradually slows down. Around 8 hours 45 minutes into the test, the water temperature reaches 14.80 °C and from then on barely changes.

The can is coolest at the bottom, as can be observed in this thermal image:

![](https://didierstevens.files.wordpress.com/2022/11/20221106-153544.png)

More pictures:

![](https://didierstevens.files.wordpress.com/2022/11/screen02.bmp)
![](https://didierstevens.files.wordpress.com/2022/11/20221106-153959.png)
![](https://didierstevens.files.wordpress.com/2022/11/20221106-154118.png)

You don’t get much cooling from this USB fridge for the amount of energy it takes. I didn’t RTFM, so maybe its purpose is not to cool a can from ambient temperature down to a nice cool drink, but to keep a can cooled in a real fridge, cool when it’s sitting on your desk.

But most likely it’s an inefficient USB gadget 🙂

---

No comments yet.

文章来源: https://blog.didierstevens.com/2022/11/06/quickpost-testing-a-usb-fridge/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)