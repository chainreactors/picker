---
title: libpng 官方参考库中的这两个严重漏洞已存在30年之久
url: https://mp.weixin.qq.com/s/4fycSuE1mqanf8MFqWlrEQ
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:25:14.061931
---

# libpng 官方参考库中的这两个严重漏洞已存在30年之久

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXibfUUCSn0TLUK5eP555H9VT9gicnrmicJ6lbZ4qvPPiajDtRxxoYRibewey19sYMuDrc478fqeRMnj8L6u02dEP2piaOY3INUoWhXA/0?wx_fmt=jpeg)

# libpng 官方参考库中的这两个严重漏洞已存在30年之久

Ddos
Ddos

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究人员披露了位于 libpng 官方参考库中的两个严重漏洞。libpng 是便携式网络图形格式的官方参考库。这些漏洞影响了跨越数十年开发历程的多个版本，可能允许攻击者触发进程崩溃、泄露敏感信息，甚至实现任意代码执行。**

作为一个与平台无关的 C 语言库，libpng 是无数应用程序中图像渲染的基石，涵盖从网页浏览器到嵌入式系统的广泛领域。这两个漏洞凸显了传统 C 语言代码库中内存管理长期存在的风险。

第一个漏洞CVE-2026-33636，针对的是使用 Neon SIMD 指令的 ARM/AArch64 架构中用于性能优化的代码。调色板扩展路径中存在一处越界读取和写入漏洞。当库将 8 位索引调色板行扩展为 RGB 或 RGBA 时，Neon 循环在处理最后一组像素时未验证是否有足够的剩余输入数据。由于该实现是从行尾反向处理的，最后一次迭代会解引用缓冲区起始位置之前的指针。攻击者可通过提供特制的 PNG 图片轻易导致进程崩溃。由于调色板内容由攻击者控制，堆内存内容可能通过解码后的像素输出被泄露。

此漏洞仅影响启用了硬件优化的系统（具体文件为 arm/palette\_neon\_intrinsics.c）。基于 Intel（SSE2）、PowerPC 的实现以及通用的 C 语言实现均不受影响。

第二个漏洞CVE-2026-33416，是一个涉及两个内部结构体 png\_struct 和 png\_info 之间指针别名（别名使用）的经典逻辑错误。此漏洞自 1.0 版本（针对透明数据）和 1.2.1 版本（针对调色板）以来就一直存在于代码库中。

像 png\_set\_tRNS 和 png\_set\_PLTE 这样的函数会在两个不同结构体之间共享同一个堆分配的缓冲区。如果应用程序调用 png\_free\_data，它会通过其中一个结构体释放缓冲区，而另一个结构体则仍持有一个悬空指针。随后的转换操作会读取——有时甚至写入——这块已被释放的内存。

研究人员已在一些环境中演示了远程代码执行。在像 glibc tcache 这样的现代内存分配器上，被释放的 256 字节缓冲区通常会立即被新对象重新使用。如果攻击者控制（通过 tRNS 数据块）重新写入该内存的值，他们就可以劫持应用程序的控制流。这些特殊构造的 PNG 文件 100% 符合标准规范，这意味着传统的验证工具或 Web 应用防火墙在不屏蔽所有 PNG 文件的情况下无法检测到此类攻击。

用户应升级到已修复这两个漏洞的 libpng v1.6.56 或 v1.8.0（主干分支）版本。如果无法立即更新，可以通过在编译时使用以下标志来禁用 ARM Neon 漏洞的硬件优化缓解措施：-DPNG\_ARM\_NEON\_OPT=0。至于第二个释放后使用漏洞，建议开发者审查在 png\_read\_info() 和 png\_read\_update\_info() 阶段之间调用 png\_free\_data() 的应用程序模式。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Telegram 创始人 Pavel Durov 因缺乏内容审核被捕](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520597&idx=2&sn=770e8cc62ae6c306013787851b80f66e&scene=21#wechat_redirect)

[Telegram 0day可导致攻击者将恶意安卓APK以视频形式发送](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520167&idx=2&sn=7d6a9321b744778cdce41dc0464f4c3d&scene=21#wechat_redirect)

[Telegram 修复Windows 版中的0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=2&sn=4c3fb5e7519056c3adfbd18c7a6561d3&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/libpng-vulnerability-rce-arm-neon-cve-2026-33636-cve-2026-33416/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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