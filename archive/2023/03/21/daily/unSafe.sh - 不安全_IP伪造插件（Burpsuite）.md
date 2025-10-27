---
title: IP伪造插件（Burpsuite）
url: https://buaq.net/go-154414.html
source: unSafe.sh - 不安全
date: 2023-03-21
fetch_date: 2025-10-04T10:06:16.879846
---

# IP伪造插件（Burpsuite）

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

![](https://8aqnet.cdn.bcebos.com/1cbc0cca06848402031ec667f3f31e91.jpg)

IP伪造插件（Burpsuite）

下载使用：Releases2021/09/24修复M00nBack反馈的一个bug。添加了AutoXFF的开关,并将AutoXFF默认设置不开启,如
*2023-3-20 23:32:49
Author: [blog.upx8.com(查看原文)](/jump-154414.htm)
阅读量:76
收藏*

---

下载使用：[Releases](https://github.com/TheKingOfDuck/burpFakeIP/releases/tag/1.0)

**2021/09/24**

1. 修复[M00nBack](https://github.com/M00nBack)反馈的一个bug。
2. 添加了AutoXFF的开关,并将AutoXFF默认设置不开启,如需让插件给每个请求头添加一个随机的XFF请求头可在右键菜单中选择ON开启

**2021/05/21**

使用Java重构，增加了[issue](https://github.com/TheKingOfDuck/burpFakeIP/issues/8)中提到的功能特性，新增给每个请求自动添加XFF头以及随机IP的功能，具体可见右键菜单AutoXFF,默认情况下自动添加的xff头为X-Forwarded-For,值为生成的随机IP,均可自定义。

**2020/04/25**

优化代码，新增9种请求头。

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597179485863.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597179485863.png)

四个小功能

* 伪造指定ip
* 伪造本地ip
* 伪造随机ip
* 随机ip爆破

### 0x01 伪造指定ip

在`Repeater`模块右键选择`fakeIp`菜单,然后点击`inputIP`功能,然后输入指定的ip：

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597184839805.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597184839805.png)

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597185444300.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597185444300.png)

程序会自动添加所有可伪造得字段到请求头中。

### 0x02 伪造本地ip

在`Repeater`模块右键选择`fakeIp`菜单,然后点击`127.0.0.1`功能：

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597186627939.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597186627939.png)

### 0x03 伪造随机ip

在`Repeater`模块右键选择`fakeIp`菜单,然后点击`randomIP`功能：

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597187304576.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597187304576.png)

### 0x04 随机ip爆破

**伪造随机ip爆破是本插件最核心的功能。**

将数据包发送到`Intruder`模块,在`Positions`中切换`Attack type`为`Pitchfork`模式,选择好有效的伪造字段,以及需要爆破的字段:

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597190596991.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597190596991.png)

按照箭头顺序将Payload来源设置为`Extensin-generated`,并设置负载伪`fakeIpPayloads`,然后设置第二个变量。 [![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597191239161.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597191239161.png)

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597192426317.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597192426317.png)

点击`Start attack`开始爆破.

[![](https://github.com/TheKingOfDuck/BurpFakeIP/raw/master/images/15597193222287.png)](https://github.com/TheKingOfDuck/BurpFakeIP/blob/master/images/15597193222287.png)

如上图,实现每次爆破都使用不同的伪ip进行,避免被ban。

> PS：伪造随机ip爆破的先决条件可以伪造ip绕过服务器限制。

文章来源: https://blog.upx8.com/3317
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)