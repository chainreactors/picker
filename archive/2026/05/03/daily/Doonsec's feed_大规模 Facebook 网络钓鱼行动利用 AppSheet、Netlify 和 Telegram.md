---
title: 大规模 Facebook 网络钓鱼行动利用 AppSheet、Netlify 和 Telegram
url: https://mp.weixin.qq.com/s/4WunBAH-nO2X6PtdyOvnrA
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:27:43.450234
---

# 大规模 Facebook 网络钓鱼行动利用 AppSheet、Netlify 和 Telegram

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PSfYrndcia9KT3yrom4PT4SFQPrYTlptNK2LcTSQgmwqg7q9wLEgX8pm8CWIx0Y6lmvic3BJjBiaNe1jpTr6oViaGjz5nV0K0icWBw/0?wx_fmt=jpeg)

# 大规模 Facebook 网络钓鱼行动利用 AppSheet、Netlify 和 Telegram

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Guardio Labs 的网络安全研究人员发现了一项名为 AccountDumpling 的大规模网络钓鱼行动，该行动已导致全球超过 30,000 个 Facebook 帐户被盗用。

与依赖伪造域名或被入侵的 SMTP 服务器的传统网络钓鱼活动不同，这种与越南有关的行动滥用 Google AppSheet 来发送完全经过身份验证的恶意电子邮件。

由于这些消息源自合法的 Google 基础设施，特别是自动化工作流通知系统，因此它们完全符合 SPF、DKIM 和 DMARC 身份验证协议。

这种固有的信任反转使得电子邮件能够绕过传统的安全电子邮件网关和垃圾邮件过滤器，直接向高价值企业帐户所有者发送具有欺骗性的 Facebook 政策违规警告，而不会触发安全警报。

## **多层网络钓鱼集群和实时互动**

威胁行为者开发了一种复杂的多集群攻击基础设施，以最大限度地提高其对各种目标的成功率。

最初的攻击集群将受害者引导至 Netlify 托管的静态页面，这些页面完美地克隆了 Facebook 帮助中心。

这些独特的针对每个受害者的子域名可以绕过标准的 URL 屏蔽列表，同时不仅能收集凭据，还能收集完整的身份信息包，包括出生日期和政府颁发的身份证照片。

第二个攻击集群从基于恐惧的诱饵转向基于奖励的社会工程，通过 Vercel 托管的环境提供虚假的蓝徽章验证。

这些动态页面采用了先进的规避技术，包括使用不可见的Unicode字符来绕过自然语言处理检测。它们能够实时拦截多因素身份验证码。

该行动的技术复杂程度在第三个集群中达到顶峰，该集群使用 Google 云端硬盘托管恶意 PDF 文件。

打开这些文件的受害者会遇到一个用 Canva 创建的、极具迷惑性的 Meta 通知，其中包含嵌入的链接，这些链接会将用户重定向到一个基于 Socket.IO 的网络钓鱼面板。

这种架构使攻击者能够控制实时 WebSocket 流量，允许人工操作人员主动管理受害者的会话，请求特定的双因素身份验证码，并动态捕获浏览器屏幕截图。

第四个集群依靠直接的社会工程，冒充主要科技品牌的企业招聘人员，逐步建立信任，并将对话转移到平台外、攻击者控制的渠道。

## **Telegram 数据泄露和越南归因**

为了管理大量涌入的被盗数据，运营者实施了由 Telegram 机器人驱动的集中式指挥控制基础设施。

泄露的凭证和会话令牌会实时传输到管理员监控的私人 Telegram 频道，从而在受害者启动恢复程序之前迅速接管帐户。

对该数据泄露管道的分析揭示了此次攻击活动的广泛范围，发现约有 30,000 条被泄露的记录，这些记录主要集中在美国和欧洲。

Guard Labs 的调查通过分析 Google 云端硬盘 PDF 的元数据，在归因方面取得了重大突破。

文档的作者字段显示了一个真实的越南名字，将技术基础设施与一家位于越南的面向公众的实体联系起来。

恶意 JavaScript 和 HTML 源代码中嵌入的越南开发者评论进一步证实了这一归因。

AccountDumpling 活动代表了一种高度工业化的访问经济，在这种经济模式下，被盗用的社交媒体账户被大规模收集和变现。

被盗页面经常被重新利用来发起二次欺诈活动，这表明攻击者如何不断利用受信任的企业平台来维持庞大的网络犯罪生态系统。

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