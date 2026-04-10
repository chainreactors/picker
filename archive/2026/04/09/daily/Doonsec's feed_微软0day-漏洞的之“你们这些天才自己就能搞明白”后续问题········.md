---
title: 微软0day-漏洞的之“你们这些天才自己就能搞明白”后续问题········
url: https://mp.weixin.qq.com/s/wBvlYltxQoV-rNsho9qzlQ
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:43:07.667167
---

# 微软0day-漏洞的之“你们这些天才自己就能搞明白”后续问题········

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16VeiaD2G0HZjbcVtIrKZFQvv3vAsKicEd99iaytriaiaLiaV6txbYVBmOJfVlBe2p259IdvndgrarDzG7u8micOr573Wo9RS2C3Y3IyKVAU/0?wx_fmt=jpeg)

# 微软0day-漏洞的之“你们这些天才自己就能搞明白”后续问题········

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器中沉浸阅读

[各位天才们,这应该是暴躁“研究人员”最快公开的一个0day漏洞！我相信你会有方法实现的！](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492550&idx=1&sn=679f8794bf12ac978342745319fb33d3&scene=21#wechat_redirect)

目前我使用的是Linux所以我暂时没有关于Windows是否修补漏洞的相关信息。。。所以MSRC这群天才漏洞问题解决了吗？

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehLeLJhAKbkKvXIsLf6YdeAIGtkHT4JsNywRo3pATnJUZee70xhapKibcujjDCUaCO937hvwjvAMcGI4wpSicMtcibVh5gQBVicn5I/640?wx_fmt=png&from=appmsg)

原话翻译中文：

这位化名为“Chaotic Eclipse”的研究人员究竟是出于什么原因才发布这个漏洞利用程序，目前尚不清楚。他在一篇简短的帖子中写道：“微软，我可没吹牛，我又来了。”他还讽刺地感谢了微软研究委员会（MSRC）的管理层，并补充说，与以往不同的是，他这次不会解释漏洞的运作原理：“你们这些天才自己就能搞明白。”

漏洞介绍：

lueHammer是一种基于TOCTOU（检查时间到使用时间）和路径混淆的本地权限提升（LPE）漏洞。

想要利用此漏洞并非易事，但一旦成功，攻击者即可访问安全帐户管理器 (SAM) 数据库，该数据库存储着本地帐户的密码哈希值。由此，他们可以提升权限至系统级别，并完全控制目标计算机。

但是在Windows 服务器上 代码无法按预期运行。Dormann 澄清说，在服务器平台上，BlueHammer 并不会将权限提升到 SYSTEM，而是将权限从普通用户级别提升到具有提升权限的管理员级别（也就是说，它绕过了通常需要用户手动确认请求完全访问权限的操作的机制）。

猜测据爆出来的原因：

微软安全响应中心（MSRC）在提交漏洞报告时要求提供演示漏洞利用的视频。一方面，这有助于微软更快地处理收到的报告；另一方面，这大大增加了提交流程的复杂性，这或许是这位研究人员感到沮丧的原因之一。

最关心的问题来了：

微软已经在调查漏洞的关键问题，并将“尽快”发布更新，并重申了其对协调漏洞披露原则的承诺，即只有在发布修复程序后才会公布漏洞的详细信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Veg54DeciavtU8R50DslDPXNT9c4YZXCUyatdIHAhxRudlMLQw35lYVgmPGDIlTDlIZYxZIo2XAWJEeTLLCEmYtM8sOKNZAAGcTA/640?wx_fmt=png&from=appmsg)

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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