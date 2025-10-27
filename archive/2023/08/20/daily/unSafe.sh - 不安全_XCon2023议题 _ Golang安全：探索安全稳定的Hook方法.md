---
title: XCon2023议题 | Golang安全：探索安全稳定的Hook方法
url: https://buaq.net/go-174816.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:52.311724
---

# XCon2023议题 | Golang安全：探索安全稳定的Hook方法

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

![](https://8aqnet.cdn.bcebos.com/7e1fcc886c8fb4399f88f0227e29ebb0.jpg)

XCon2023议题 | Golang安全：探索安全稳定的Hook方法

导语：自动化，隐私保护，供应链安全，多云安
*2023-8-19 11:0:0
Author: [www.4hou.com(查看原文)](/jump-174816.htm)
阅读量:84
收藏*

---

导语：自动化，隐私保护，供应链安全，多云安全，深度学习的应用！

![640.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348389115781.jpg "1692348081164323.jpg")

**链链动未来·技术前瞻**

> 自动化，隐私保护，供应链安全，多云安全，深度学习的应用！
>
> **——腾讯云鼎实验室 高级安全研究员**
>
> **蒋浩天、王昊宇**

随着Golang在后端开发中的地位逐渐上升，**其高并发和多协程支持的优质特性让其成为了主流的后端开发语言**。然而，随之而来的是对于安全性的更高要求。为了满足这一需求，安全研究人员开始关注如何对基于Golang的后端服务进行安全加固和漏洞防御。在这个背景下，Hook技术变得不可或缺。

**Hook技术允许开发者通过修改或拦截代码的执行流程，实现对程序行为的监控和控制**。虽然可以对系统库或系统调用进行Hook，但这无法获得Golang内部更为详细的数据信息，尤其是有关程序上下文和执行流的信息。因此，**为了实现更高级别的监控和防御，我们需要深入到Golang内部进行Hook操作**。

在实践中，Hook技术也时刻面临着挑战。这些挑战涉及稳定性、兼容性、性能问题等多个层面，由于Golang的特殊性，Hook技术在其上的应用更为复杂，又因为Golang的并发模型、内存管理等方面与其他语言存在差异，也使得Hook变得更具难度。

为何在Golang中开发一个真正意义上的稳定的Hook框架如此困难？这其中的难点在哪里？现有的Hook框架存在哪些问题？Golang有哪些独特之处？在Hook的过程中又存在哪些不稳定因素？

为了解决这些问题，**本届XCon2023大会上，来自腾讯云鼎实验室的高级安全研究员 蒋浩天、王昊宇将带来议题《Golang安全：探索安全稳定的Hook方法》的分享，带领我们深入剖析Golang语言的特殊性，研究如何在Golang中实现真正意义上的安全稳定Hook，一同来探讨可能的解决方案，涵盖Hook框架的设计、实现和优化等方面**。最终，两位演讲者将分享他们开发的Golang Hook框架，该框架不仅考虑了Golang的特殊性，还解决了已有Hook框架存在的问题。

**议题简介**

**《Golang安全：探索安全稳定的Hook方法》**

Golang语言中，相对于C/C++等语言，存在很多特殊性的机制。这些机制方便了开发者，但是对于我们Hook来讲，还是会增加很多障碍。例如说Golang的协程栈迁移，扩容缩减，runtime变量逃逸分析，gc等机制都会影响我们Hook框架的健壮性。并且这些问题十分隐蔽，很难发现。**因此演讲者将在此次议题中，介绍如何发现各种潜在的问题，以及这些问题在现有Hook框架中存在的风险。**

**演讲人介绍**

**蒋浩天、王昊宇**

**腾讯云鼎实验室的高级安全研究员**

**![640 (1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348390396817.jpg "1692348304171409.jpg")**

**蒋浩天，现就职于腾讯云鼎实验室，曾任职360，字节跳动。主要研究方向云安全，二进制安全，虚拟化等相关领域。曾在国内安全峰会多次发表议题。**

![640 (2).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348391252292.jpg "1692348371309874.jpg")

**王昊宇，现就职于腾讯安全云鼎实验室**，毕业于中国科学院大学，主要研究方向**云安全、二进制安全、协议安全**。曾发表论文于DATE、Inscrypt等会议。

**XCon2023**

**会议日程全曝光**

![640 (3).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692348425136116.jpg "1692348425136116.jpg")

**☆购票通道同步开启**

**【链动者】¥0，展商互动区+XReward开放路演区可通行，不含闭门演讲、自助午餐及会刊**

**【先锋·造链者】¥2090，全场可通行，含闭门演讲+年度会刊（不含餐）。8月20日晚6点前购买，享此福利**

**【突围·造链者】¥2790，全场可通行，含闭门演讲+自助午餐+年度会刊**

**【全速·造链者】¥4500，仅限会议当日现场购买，不支持票券折扣**

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?uKE98tff)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/516e3c10f19d3f1a13fb3ad9d2198bc9.jpg)

  XCon2023议题 | Golang安全：探索安全稳定的Hook方法](https://www.4hou.com/posts/9ABB)
* [![](https://img.4hou.com/images/7d8495fbefc4657ce438baa8ab4da463.png)

  XCon2023议题：基于VxWorks系统的固件符号恢复方法研究](https://www.4hou.com/posts/5wxK)
* [![](https://img.4hou.com/images/eacb6e0789a93e7098ba998d7e3a0609.png)

  XCon2023议题：依托于SLSA框架的广义可信供应链安全建设实践](https://www.4hou.com/posts/WKvQ)
* [![](https://img.4hou.com/images/aa4f234ef43a40479f29880ba4db1f41.jpg)

  云计算攻击：网络攻击的新载体](https://www.4hou.com/posts/7yy1)
* [![](https://img.4hou.com/images/201810211415429849.jpg)

  Lazarus黑客以微软 IIS 服务器为目标传播恶意软件](https://www.4hou.com/posts/V2nX)
* [![](https://img.4hou.com/images/5fc5dabfe23e23e91ff235a77a740ad4.png)

  从网络安全场景模型交付谈机器学习平台实践](https://www.4hou.com/posts/PKl1)

![]()

文章来源: https://www.4hou.com/posts/9ABB
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)