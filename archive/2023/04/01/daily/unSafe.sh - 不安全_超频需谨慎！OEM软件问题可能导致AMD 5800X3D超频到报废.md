---
title: 超频需谨慎！OEM软件问题可能导致AMD 5800X3D超频到报废
url: https://buaq.net/go-156371.html
source: unSafe.sh - 不安全
date: 2023-04-01
fetch_date: 2025-10-04T11:19:23.594770
---

# 超频需谨慎！OEM软件问题可能导致AMD 5800X3D超频到报废

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

![](https://8aqnet.cdn.bcebos.com/49798141925aee865f142478c2df6e70.jpg)

超频需谨慎！OEM软件问题可能导致AMD 5800X3D超频到报废

据 Igor Lab 发布的消息，目前最好的游戏处理器之一，AMD RYZEN 7 5800X3D 可能会在超频时彻底报废，原因似乎是 OEM 超频软件存在问题。Igor Lab 首先
*2023-3-31 22:34:37
Author: [www.landiannews.com(查看原文)](/jump-156371.htm)
阅读量:14
收藏*

---

据 Igor Lab 发布的消息，目前最好的游戏处理器之一，AMD RYZEN 7 5800X3D 可能会在超频时彻底报废，原因似乎是 OEM 超频软件存在问题。

Igor Lab 首先在 MSI Center 中发现一个错误，这个错误可以让玩家在允许值的上限继续超压和超频，也就是绕过了 AMD 设置的超压超频限制，但本身对用户来说这没有什么异常提醒：MSI 软件里提供的正常设置场景，也就是用户可能会在不知情的情况下超频到报废。

[![超频需谨慎！OEM软件问题可能导致AMD 5800X3D超频到报废](https://img.lancdn.com/landian/2023/03/98097.png)](https://img.lancdn.com/landian/2023/03/98097.png)

值得注意的是不止 MSI 存在问题，测试发现华硕、技嘉、华擎提供的 OEM 软件里也存在类似问题，因此这应该是个广泛问题。

在尝试将 5800X3D 超压到 1.3v + 后，5800X3D 会立即崩溃，Igor Lab 测试了两次，第一次超压到 1.3v 好像问题不大，第二次超过 1.3v 后电脑直接黑了，而且也没法再启动了。

实际上 5800X3D 的额定电压是 1.5v，甚至可以在此基础上超压到 1.55v，但 5800X3D 采用 3D-VCache 缓存，芯片自带 32MB 缓存，外挂 64MB L3 缓存后提升到 96MB。

但之前 AMD 发现这个外挂缓存会严重影响 CPU 散热，导致 CPU 自动以较低的频率运行，影响实际性能，后来 AMD 发布固件将额定电压从 1.5v 降到 1.35v，这也基本坐实了外挂的 L3 缓存影响 CPU 散热，这属于硬伤无法通过软件层面解决。

所以现在尝试超压和超频导致 CPU 报废很有可能也是散热问题，只不过问题在于之前 1.55v 时也只是频率降低，并没有出现完全挂掉的情况。

前两周在 YouTube 上也有 UP 尝试超频 7950X3D 时导致 CPU 报废，不知道这些原因是否相同，但无论如何 AMD 应该都会发布固件或指导 OEM 更新软件，避免绕过 AMD 添加的限制。

版权声明：感谢您的阅读，本文由山外的鸭子哥转载或编译自[Igors Lab](https://www.igorslab.de/en/and-saying-goodbye-quiet-servus-ryzen-7-5800x3d-with-msi-center-overclocked-and-executed/)，如需转载本文请联系原作者获取授权，谢谢理解。

文章来源: https://www.landiannews.com/archives/98097.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)