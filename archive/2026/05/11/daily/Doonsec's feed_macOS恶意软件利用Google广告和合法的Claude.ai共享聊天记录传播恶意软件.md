---
title: macOS恶意软件利用Google广告和合法的Claude.ai共享聊天记录传播恶意软件
url: https://mp.weixin.qq.com/s/LqpDkh5ljtoMo2CBgeZgRg
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:45.675781
---

# macOS恶意软件利用Google广告和合法的Claude.ai共享聊天记录传播恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7P6FkicvAaIEVEubb6ZdddDHEUD7GywSic2jbh5rOib1suebEwGW3xR2TmhpDoIEZUatVAHuDFcJYYATShAibyT8bL7fZtyibBkBUbg/0?wx_fmt=jpeg)

# macOS恶意软件利用Google广告和合法的Claude.ai共享聊天记录传播恶意软件

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

威胁行为者正在通过植入恶意代码的谷歌广告和欺骗性人工智能应用程序，对 macOS 用户发起复杂的恶意广告活动。

研究人员最近发现了一种通过赞助搜索结果将受害者重定向到欺诈性着陆页的运作方式。

攻击者将受信任的托管平台与臭名昭著的“ Clickfix ”社会工程策略相结合，成功传播了MacSync有效载荷和危险的macOS信息窃取程序。

攻击链始于用户搜索热门软件，特别是像 Claude 这样的 AI 工具。

## **macOS恶意软件广告**

攻击者通过购买出现在搜索结果页面顶部的赞助广告来操纵搜索引擎结果。

由于这些广告经常模仿合法商家，最终用户很难将它们与真实链接区分开来。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NTvoAyagx1UqghGpNLvia0aicEozqkriaKNWkRZhA5vlOvgBOEPYiaviaFiaSTiaJgqdaqNibQL7G06m2XcOgSPIIJKxfpfec7NdmecLM/640?wx_fmt=jpeg)

点击这些赞助广告后，受害者会被引导至托管在可信基础设施上的欺骗性网站。

为了绕过初始域名信誉检查和企业网络过滤器，威胁行为者正在利用Google Sites、Framer 等服务，甚至是合法的 claude.ai 共享聊天。

这些登录页面经过精心设计，看起来像是 Claude AI 的官方下载门户网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NELFUFibl71Fxf3IvbetvVCDCWiceasj1spCsP9ia3vDdpe71LonFjpB5VWeqibJQ0Hgy44NFsMY3rVQyNpAC5H0eiaPsiaOelu39Jw/640?wx_fmt=jpeg)

当用户尝试与网站互动或下载所谓的桌面应用程序时，会弹出 Clickfix 提示。

此提示使用欺骗性的警告对话框，诱骗受害者手动执行恶意终端命令或下载被篡改的安装程序，伪装成“修复”显示错误。

研究人员 Berk Albayrak 和 g0njxa 发表了关于追踪目标恶意软件攻击背后基础设施的研究成果。

威胁行为者频繁轮换域名和托管平台，以逃避检测并最大限度地提高搜索引擎优化效果。

该活动严重依赖 Google Sites 来托管初始欺骗性页面，研究人员已识别出恶意 URL `such as sites[.]google[.]com/view/cloud-version-08, sites[.]google[.]com/view/brewshka-page`，以及 `sites[.]google[.]com/view/claud-version-0505`。

除了 Google Sites 之外，攻击者还利用了 Framer 平台，在 c 上托管虚假应用程序`laude-desktop-app[.]framer[.]ai`。

## **有效载荷交付与执行**

一旦受害者与虚假的 Claude AI 门户网站进行交互，该网站就会将他们重定向到最终的有效载荷交付服务器。

已观察到初始着陆页将流量重定向到外部 IP 地址，例如 `2[.]26[.]75[.]112/Hokojol`，以及域名，例如`pieoneer[.]org and greenactiv[.]com`。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7P2K5Z19SDchKym0vN0iaYNsiaLW4h3Gj3vz3tdGItKkniagW2TMkYucw4qV5RibEfGEym9gN8icSGepecbctsnjwU7T8RoM1P81qdY/640?wx_fmt=jpeg)

这些目标服务器会将 MacSync clickfix 有效载荷直接投放到受害者的计算机上。执行后，该恶意软件会充当一个功能全面的 macOS 窃取程序。

它专门用于从受感染的苹果系统中窃取敏感信息，包括已保存的浏览器凭据、加密货币钱包数据和活动会话令牌。

随后，被盗数据被泄露回攻击者的命令与控制基础设施。

为了防范这些欺骗性的恶意广告活动，组织和个人用户在与赞助搜索结果互动时必须格外谨慎。

安全团队应在网络层面阻止已知的入侵指标，并监控 macOS端点遥测数据，以发现源自 Web 浏览器的异常脚本执行。

请教育用户避免点击赞助软件下载广告。他们应该始终直接访问官方供应商网站。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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