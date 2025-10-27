---
title: Zenbleed攻击从AMD Zen2处理器窃取敏感数据
url: https://buaq.net/go-173191.html
source: unSafe.sh - 不安全
date: 2023-07-30
fetch_date: 2025-10-04T11:51:16.401201
---

# Zenbleed攻击从AMD Zen2处理器窃取敏感数据

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

![](https://8aqnet.cdn.bcebos.com/896c81d02d3cbe6bc8e3ef6d62b7194b.jpg)

Zenbleed攻击从AMD Zen2处理器窃取敏感数据

导语：​Zenbleed攻击从AMD Ze
*2023-7-29 12:0:0
Author: [www.4hou.com(查看原文)](/jump-173191.htm)
阅读量:20
收藏*

---

导语：​Zenbleed攻击从AMD Zen2处理器窃取敏感数据。

Zenbleed攻击从AMD Zen2处理器窃取敏感数据。

谷歌安全研究人员Tavis Ormandy发现了一个影响AMD Zen2 CPU处理器的安全漏洞——Zenbleed，漏洞CVE编号为CVE-2023-20593。攻击者利用该漏洞可以以30Kb/s的速度从CPU中窃取密码、加密密钥等敏感数据。

**漏洞概述**

推测执行是主流处理器使用的一种增强处理器性能的方法。Zenbleed漏洞产生的原因是推测执行过程中名为'vzeroupper'的指令处理不当导致的。

Ormandy使用和模糊和性能计数器发现了特定硬件事件，并使用Oracle序列化方法验证了结果。使用该方法可以检测到随机生成的程序和其序列化Oracle之间的不一致，最终成功发现了Zen2 CPU中的漏洞。

触发该漏洞后，研究人员成功从系统中窃取了敏感信息，包括虚拟机、隔离沙箱、容器等环境。30kb/s的信息窃取速度足以监控加密密钥和用户的登录密码等。

**漏洞影响**

虽然漏洞利用PoC是针对Linux系统的，但是该漏洞是操作系统无关，因此所有影响在Zen 2 CPU上的操作系统都受到该漏洞的影响。漏洞影响所有基于Zen 2架构的AMD CPU，包括Ryzen 3000、Ryzen 4000U/H ("Renoir")、Ryzen 5000U ("Lucienne")、Ryzen 7020、ThreadRipper 3000 和Epyc 服务器处理器。

但该漏洞对普通用户的实际影响并不大，因为漏洞利用需要对受影响的系统有物理访问权限，并且漏洞的利用需要很高程度的专业知识。

**漏洞补丁**

5月15日，研究人员将该漏洞提交给了AMD。7月24日，AMD针对受影响的系统发布了微代码。研究人员建议使用AMD Zen 2 CPU的用户尽快应用AMD的微代码更新。此外，研究人员称还可以通过将"chicken bit"设置为DE\_CFG来缓解该漏洞的影响，但这一操作会降低CPU的性能。

Ormandy称检测Zenbleed漏洞利用基本不可能，因为'vzeroupper'的不当使用并不需要很高的权限或特殊的系统调用，因此非常隐秘。

完整技术分析参见：https://lock.cmpxchg8b.com/zenbleed.html

本文翻译自：https://www.bleepingcomputer.com/news/security/zenbleed-attack-leaks-sensitive-data-from-amd-zen2-processors/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?ewvX9ZCu)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/3801213fb80e7bec5237ec4026fe2f3099506bfe.jpeg)

  Zenbleed攻击从AMD Zen2处理器窃取敏感数据](https://www.4hou.com/posts/xzLB)
* [![](https://img.4hou.com/images/微信截图_20230724100044.png)

  恶意软件伪装成漏洞PoC进行传播](https://www.4hou.com/posts/0oO5)
* [![](https://img.4hou.com/images/1688604477749995.jpg)

  被大肆利用的漏洞导致数百个太阳能发电站面临威胁](https://www.4hou.com/posts/9ALz)
* [![](https://img.4hou.com/images/微信截图_20230626101557.png)

  Win32k的内部结构以及可能出现的漏洞](https://www.4hou.com/posts/z4B2)
* [![](https://img.4hou.com/images/84ab889448fe96360135682ecd48e8056fd786.jpg)

  2023年十佳开源漏洞评估工具](https://www.4hou.com/posts/xz2z)
* [![](https://img.4hou.com/images/be6df50a44e51725fe23453e75cfaeb5.jpg)

  本田电子商务平台漏洞暴露客户数据](https://www.4hou.com/posts/OXZQ)

![]()

文章来源: https://www.4hou.com/posts/xzLB
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)