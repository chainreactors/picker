---
title: 苹果紧急修复已遭利用的 WebKit 0day
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515546&idx=1&sn=f9311f04f319e12385edbfcd698fa495&chksm=ea948cf0dde305e697564ae3c0b973831eece5c572326a20990546b6bacf3bef67450345d514&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-15
fetch_date: 2025-10-04T06:38:01.519259
---

# 苹果紧急修复已遭利用的 WebKit 0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2eLJXXAakjqDbHJykRr3qibys7AgiccDhlScQXxe7GlxYzCHVWQPqlnhQZX3EaXQjRGDIiaQ7gOorQ/0?wx_fmt=jpeg)

# 苹果紧急修复已遭利用的 WebKit 0day

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**苹果公司发布紧急安全更新，修复了被用于攻击iPhone、iPad和Mac等设备的新0day。**

该0day的编号为CVE-2023-23529，是一个WebKit混淆漏洞，可用于在受陷设备上触发OS崩溃并获得代码执行权限。当用户打开恶意网页时，攻击者可利用该漏洞在运行易受攻击 iOS、iPadOS和macOS版本的设备上执行任意代码。该漏洞还影响macOS Big Sur 和 Monterey 上的Safari 16.3.1。

苹果公司对该0day的说明是“处理恶意构造的web内容可导致任意代码执行。苹果已发现该漏洞遭活跃利用的报告。”

苹果公司已推出iOS 16.3.1、iPadOS 16.3.1和macOS Ventura 13.2.1版本，修复了上述漏洞。受影响设备数量很多，因为该漏洞同时影响老旧版本和新版本，包括：

* iPhone 8和后续版本
* iPad Pro（所有机型）、iPad Air第三代及后续版本、iPad第五代及后续版本以及iPad mini第五代及后续版本。
* 运行macOS Ventura 的Mac设备

另外，苹果还修复了一个释放后使用漏洞 (CVE-2023-23514)，攻击者可通过在Mac和iPhone 上的内核权限执行任意代码。

**苹果今年修复的第一个0day**

尽管苹果公司披露称已发现该漏洞遭在野利用的报告，但尚未发布关于这些攻击的信息。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[苹果修复已遭利用的第10个0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515027&idx=1&sn=93ebe9404e1ead6aa5f784abf7fab31a&chksm=ea948af9dde303ef597a5e12dd8faab95e3127a6e8214fe9cdfba93dbcd4e59095001090e30f&scene=21#wechat_redirect)

[苹果修复已遭利用的第9枚0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=1&sn=10f6c5afa8be65b7ccac62c9ab73645c&chksm=ea9489a5dde300b312a93ec52a321f835baed001465326883dd6cdbbe70fecd5b94b1b8000c7&scene=21#wechat_redirect)

[苹果修复今年以来影响iPhone 和 Mac设备的第8枚0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513963&idx=1&sn=3a8ab8ac432bb3abbc5bd61a3ab0a8e0&chksm=ea948601dde30f1754006cf1ea040292e836f87e7c0b1ca21a7b07e8a3e2884ff932a45a1d2a&scene=21#wechat_redirect)

[苹果紧急修复两个0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513606&idx=1&sn=7ef2bbe710ecd61f87d32d3a53d28db7&chksm=ea94876cdde30e7a698417a1e60f215d5f74440aeb15e6238bef618870a8d31d953006005405&scene=21#wechat_redirect)

[苹果紧急修复影响 Mac 和 Apple Watch 的 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511813&idx=1&sn=dc16d2c1c8707eaed97dde4a0dfa7750&chksm=ea949e6fdde31779bfd96864b6be586636189da2c4799ddda06ccf2bb25c009aece718ee55d6&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/apple-fixes-new-webkit-zero-day-exploited-to-hack-iphones-macs/

题图：Pixabay License‍

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