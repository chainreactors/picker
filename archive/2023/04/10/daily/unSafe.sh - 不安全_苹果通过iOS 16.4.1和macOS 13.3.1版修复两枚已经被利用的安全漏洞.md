---
title: 苹果通过iOS 16.4.1和macOS 13.3.1版修复两枚已经被利用的安全漏洞
url: https://buaq.net/go-157803.html
source: unSafe.sh - 不安全
date: 2023-04-10
fetch_date: 2025-10-04T11:29:24.464845
---

# 苹果通过iOS 16.4.1和macOS 13.3.1版修复两枚已经被利用的安全漏洞

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

![](https://8aqnet.cdn.bcebos.com/18543dafccf30a52bd49e0bc0055c3ac.jpg)

苹果通过iOS 16.4.1和macOS 13.3.1版修复两枚已经被利用的安全漏洞

昨天蓝点网发布有关苹果 iOS 16.4.1 版的时候还在奇怪，两个小问题怎么会让苹果这么快发布了一个新版本进行修复，除非有什么重大安全问题只是当时苹果没有公布。事实证明这个猜测是正确
*2023-4-9 22:39:12
Author: [www.landiannews.com(查看原文)](/jump-157803.htm)
阅读量:31
收藏*

---

[昨天蓝点网发布有关苹果 iOS 16.4.1 版的时候还在奇怪](https://www.landiannews.com/archives/98206.html)，两个小问题怎么会让苹果这么快发布了一个新版本进行修复，除非有什么重大安全问题只是当时苹果没有公布。

事实证明这个猜测是正确的，苹果通过 iOS 16.4.1、iPadOS 16.4.1 和 macOS Ventura 13.3.1 以及 Safari 16.4.1 修复了两枚已经在野外遭到黑客利用的安全漏洞。

![苹果发布iOS 16.4.1正式版 只修复了两个小问题 有点奇怪🤨](https://img.lancdn.com/landian/2023/04/98206.png)

第一个漏洞是 CVE-2023-28205，漏洞位于 WebKit 内核中，属于 Use-after-Free 漏洞，在重用释放的内存时可以破坏数据并执行任意代码。

攻击者利用该漏洞可以制作特定的网页诱导目标用户访问，这可能导致在目标设备上执行代码，危害程度极高。

第二个漏洞是 CVE-2023-28206，该漏洞属于 IOSurfaceAccelerator 越界写入，可能导致数据损坏、崩溃或代码执行。

攻击者利用该漏洞可以制作特定的应用程序诱导目标设备安装，之后可以以内核级别的权限执行任意代码，危害程度极高。

根据苹果说明，上面两枚安全漏洞在被发现前都已经在野外遭到黑客的利用，也就是属于 0day，受影响的设备也非常广泛，从 iPhone 8 + 到 iPad Pro 所有型号、iPad Air 3rd+、iPad 5th+、iPad mini 5th + 和运行 macOS Ventura 的所有 Mac。

鉴于上述漏洞危害程度如此高，苹果这才推出紧急更新进行修复，建议使用上述设备和系统的用户立即更新到最新版，这也是苹果今年修复的第三个 0day。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98240.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98240.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)