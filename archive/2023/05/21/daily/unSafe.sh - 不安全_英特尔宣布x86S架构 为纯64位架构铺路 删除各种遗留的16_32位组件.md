---
title: 英特尔宣布x86S架构 为纯64位架构铺路 删除各种遗留的16/32位组件
url: https://buaq.net/go-164763.html
source: unSafe.sh - 不安全
date: 2023-05-21
fetch_date: 2025-10-04T11:36:49.323628
---

# 英特尔宣布x86S架构 为纯64位架构铺路 删除各种遗留的16/32位组件

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

![](https://8aqnet.cdn.bcebos.com/4ad8336be69306c04720b17c6f6fe3b1.jpg)

英特尔宣布x86S架构 为纯64位架构铺路 删除各种遗留的16/32位组件

英特尔日前对外公开发布了一篇名为《构想简化的英特尔架构》白皮书，在白皮书中英特尔宣布 Intel x86S 架构，这是一种纯 64 位模式架构，旨在将英特尔指令集架构 (ISA) 过渡
*2023-5-20 23:29:55
Author: [www.landiannews.com(查看原文)](/jump-164763.htm)
阅读量:32
收藏*

---

英特尔日前对外公开发布了一篇名为《构想简化的英特尔架构》白皮书，在白皮书中英特尔宣布 Intel x86S 架构，这是一种纯 64 位模式架构，旨在将英特尔指令集架构 (ISA) 过渡到纯 64 位模式架构。

Intel 64 位架构已经有 20 多年历史，不过微软已经在其最新操作系统中放弃 32 位架构，英特尔固件也不再原生支持非 UEFI64 操作系统。

64 位操作系统是当今事实上的标准，这种 64 位系统保留了运行 32 位应用程序的能力，但停止原生支持 16 位应用程序。

[![英特尔宣布x86S架构 为纯64位架构铺路 删除各种遗留的16/32位组件](https://img.lancdn.com/landian/2023/05/98718.png)](https://img.lancdn.com/landian/2023/05/98718.png)

目前无论是 Windows 10 还是 Windows 11 的 64 位版都可以运行 32 位应用程序，而且至少就目前来说，32 位应用程序仍然占据着极高的份额，所以保留 64 位操作系统对 32 位软件的兼容性依然非常重要。

**趋势是朝着纯 64 位发展：**

纯 64 位模式 (64-bit mode-only architecture) 简称 x86S 架构，这里的 S 指的是 Simplification，也就是简化，这个 S 说明了英特尔想要达到的目的。

英特尔认为随着技术发展，硬件和软件生态系统有机会进行简化，除了将 CPU 引导至 64 位模式外，某些传统模式在现代操作系统中几乎没什么用处。

既然如此，是否可以删除架构中这些使用很少的组件以简化 64 位架构？

**x86S 架构有什么好处：**

* x86S 架构删除了一些旧的组件，从而降低软件和硬件体系架构的整体复杂性，通过探索 x86S 架构，可以进行与现代软件部署的一致性更改，例如：
* 使用 64 位简化分段模型为 32 位应用程序提供分段支持
* 删除 Ring 1 和 2，这些在现代操作系统中并未使用
* 删除 16 位寻址支持
* 取消对 Ring 3 I/O 端口访问的支持
* 消除字符串端口 I/O，它使用过时的 I/O 模型
* 将 APIC 的使用限制改为 X2APIC，并删除旧版 8259 支持
* 删除一些未使用的其他组件

英特尔发布这份白皮书算是倡议，希望整个业界能够对此提出建议、评估对软件的影响、探索将 ISA 过渡到 x86S 模式的好处。

如果你对 x86S 及软件生态系统有反馈意见，请发送到：[[email protected]](https://www.landiannews.com/cdn-cgi/l/email-protection)

白皮书下载地址：<https://cdrdv2.intel.com/v1/dl/getContent/776648>

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98718.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98718.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)