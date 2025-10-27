---
title: Linux 内核受新的SLUBStick 跨缓存攻击影响
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=1&sn=836f6bce19d0adc20c9deedfee1cf1de&chksm=ea94a124dde32832012485df5d575f8d74fed00fade2844c634cae2f6527ef7413e015c25df4&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-06
fetch_date: 2025-10-06T18:04:58.709594
---

# Linux 内核受新的SLUBStick 跨缓存攻击影响

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ3pWqbH6icKXUSKcDUm1VTtDuNvFLp3KnTZGD1tfh482BAnIXFb98ywww/0?wx_fmt=jpeg)

# Linux 内核受新的SLUBStick 跨缓存攻击影响

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**奥地利格拉茨工业大学的研究人员提到，一种名为 “SLUBStick” 的新型 Linux Kernel 跨缓存 (cross-cache) 攻击在将限制性堆漏洞转换为任意内存读写能力方面的成功率达到99%，可使研究人员提升权限或逃逸容器。**

研究人员利用32位和64位系统中存在的9个已有CVE漏洞，演示了针对 Linux 内核版本5.9和6.2（最新）的攻击。另外，该攻击适用于启用了所有的现代内核防御措施如 SMEP、SMAP和KASLR等。

研究员将在本月晚些时候举行的 Usenix 安全峰会上详述SLUBStick，演示如何在启用了现代防御措施的最新版 Linux 中实现提权和容器逃逸。目前研究员已发布该漏洞的技术论文。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ3aqGia8IXXb4l0xUUNA1ZODdsCkrZmZzTu2nHl2fLvI08Kic4uf6lOrow/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ3rGW3Jjicb4fQvGXFEJvP1jgNGibsa1mOwA3cbkHR7wFCfibgTGgyn39aA/640?wx_fmt=png&from=appmsg)

**SLUBStick 详情**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ34hgbHMuC1lN25uMruMnkZ8ngIQj7ohak5PKbkZicTkzoOlhnpRTYCDw/640?wx_fmt=png&from=appmsg)

Linux 内核有效且安全地管理内存的方式是为不同的数据结构类型分配和取消分配内存块 “slab”。

该内存管理流程中存在的缺陷可使攻击者损坏或操纵数据结构即跨缓存攻击。然而，这些攻击的有效性大约是40%，一般可导致系统崩溃。SLUBStick 利用堆漏洞如双重释放、释放后使用或界外写等操纵内存分配流程。接着，它使用定时侧信道来判断内存块分配/取消分配的实际时间，从而使攻击者预测和控制内存复用。使用这种定时信息将成功率提升至99%，使得 SLUBStick 非常具有实践性。

将堆漏洞转变为任意内存读写原语分三个步骤：

* 释放特定内存块并等待内核复用
* 以受控方式重新分配这些块，确保它们为重要的数据结构如页面表进行重新利用。
* 一旦重新获取，攻击者将覆写页面表条目，从而获得读写任意内存位置的能力。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ3aqGia8IXXb4l0xUUNA1ZODdsCkrZmZzTu2nHl2fLvI08Kic4uf6lOrow/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ3rGW3Jjicb4fQvGXFEJvP1jgNGibsa1mOwA3cbkHR7wFCfibgTGgyn39aA/640?wx_fmt=png&from=appmsg)

**实际影响**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMS5NTZ8H2MSpAXo4B3xTYZ34hgbHMuC1lN25uMruMnkZ8ngIQj7ohak5PKbkZicTkzoOlhnpRTYCDw/640?wx_fmt=png&from=appmsg)

与涉及侧信道的多数攻击一样，SLUBStick 要求在具有代码执行能力的目标机器上具有本地访问权限。此外，攻击要求Linux 内核中具有堆漏洞，以用于获得对内存的读写权限。虽然这样的要求看似使攻击难以应用，但却为攻击者带来一些好处。

甚至对于拥有代码执行能力的攻击者而言，SLUBStick 提供了实现提权、绕过内核防御措施、执行容器逃逸或将其纳入复杂攻击链的能力。提权可用于将权限提升至root，从而获得不受限制的操作能力，而容器逃逸可用于脱离沙箱环境并访问主机系统。

此外，在利用后阶段，SLUBStick 可修改内核结构或钩子来维持可持久性，从而使防御人员更难以检测到恶意软件。

用户如想深入探索 SLUBStick 并对利用进行实验，可查看相关 GitHub 仓库。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[恶意软件攻击Windows、Linux 和 macOS 开发人员](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520290&idx=2&sn=0dff9cae5a9ad1a39be2e6da027f70a9&chksm=ea94a148dde3285e6c15219e90179e8424cf1b202221d471b6c705e4dba7127f593b4fd64b80&scene=21#wechat_redirect)

[Falcon Sensor 在数周前导致 Linux 内核崩溃 恢复工具已推出](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520157&idx=2&sn=a93459b30ee5e2a9c5d7fde92fbadf1f&chksm=ea94bef7dde337e10afa600f28254053392253623ae5fc070b7b622dcdff148744cc5c6cc9cf&scene=21#wechat_redirect)

[CISA：速修复已遭利用的 Linux 内核缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519633&idx=2&sn=d2931cf44b52e715fd91a3f5e913bb65&chksm=ea94bcfbdde335edb849eb308ac9de9051112b083fb97213435745ec26be7a167056faa7fda5&scene=21#wechat_redirect)

[Fortinet 修复严重的 FortiClientLinux 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519274&idx=1&sn=0db6fdb46bf03ada98af3901110ee37b&chksm=ea94bd40dde3345638c4a1918ae58b2b830c15fa030942af921b1d39679824af6b8da3f82d60&scene=21#wechat_redirect)

[Spectre v2 新型攻击影响 Intel CPU 上的 Linux 系统](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519269&idx=1&sn=df797138ea4772753f1a9237b16f527d&chksm=ea94bd4fdde33459413196c03e1f7d44bf0ed89a2e054dc64117fe4b88820df18b356b897761&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/linux-kernel-impacted-by-new-slubstick-cross-cache-attack/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过