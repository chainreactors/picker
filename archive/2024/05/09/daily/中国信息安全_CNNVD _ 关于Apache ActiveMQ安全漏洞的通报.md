---
title: CNNVD | 关于Apache ActiveMQ安全漏洞的通报
url: https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664212629&idx=3&sn=241cd3d5ab30432e0d5d0cac9d887350&chksm=8b59aa6cbc2e237ae319acd99af69a4a40ae2309839d0ae9716dc6f491f4dc5fa6be5fea9c02&scene=58&subscene=0#rd
source: 中国信息安全
date: 2024-05-09
fetch_date: 2025-10-06T17:17:04.794250
---

# CNNVD | 关于Apache ActiveMQ安全漏洞的通报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgwUqGyfeESSiaf6E4LbZAPMBA8ibG5RUrUFF1ovrujqqWJo9IngOHDs9Q/0?wx_fmt=jpeg)

# CNNVD | 关于Apache ActiveMQ安全漏洞的通报

中国信息安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgEGIJ8mS7oDiaHEawiczicp0OiblXNRgicdc0fZ16iaJyic8s7WiauuFgVme4rQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgEGIJ8mS7oDiaHEawiczicp0OiblXNRgicdc0fZ16iaJyic8s7WiauuFgVme4rQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgibkONTkK2yUHTbS5FTzMOjPwKsWwnGCXS50s8Wb6tWib22Dao65ws4LA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgEGIJ8mS7oDiaHEawiczicp0OiblXNRgicdc0fZ16iaJyic8s7WiauuFgVme4rQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgEGIJ8mS7oDiaHEawiczicp0OiblXNRgicdc0fZ16iaJyic8s7WiauuFgVme4rQ/640?wx_fmt=gif&from=appmsg)

**扫码订阅《中国信息安全》**

邮发代号 2-786

征订热线：010-82341063

近日，国家信息安全漏洞库（CNNVD）收到关于Apache ActiveMQ安全漏洞（CNNVD-202405-256、CVE-2024-32114）情况的报送。成功利用漏洞的攻击者，可能在未经身份验证的情况下使用Jolokia JMX REST API与代理交互，或使用Message REST API向消息队列和主题中发送消息、接收消息、删除消息队列和主题等。Apache ActiveMQ 6.0.0-6.1.1版本均受此漏洞影响。目前，Apache官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。

**一、漏洞介绍**

Apache ActiveMQ是美国阿帕奇（Apache）基金会的一套开源的消息中间件，它支持Java消息服务、集群、Spring Framework等。Apache ActiveMQ存在安全漏洞，该漏洞源于程序未对 Jolokia JMX REST API 和 Message REST API 添加身份校验，导致攻击者可能在未经身份验证的情况下使用Jolokia JMX REST API与代理交互，或使用Message REST API向消息队列和主题中发送消息、接收消息、删除消息队列和主题等。

**二、危害影响**

Apache ActiveMQ 6.0.0-6.1.1版本均受此漏洞影响。

**三、修复建议**

目前，Apache官方已发布新版本修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。

**官方参考链接：**https://github.com/apache/activemq/tags

本通报由CNNVD技术支撑单位——北方实验室（沈阳）股份有限公司、西安交大捷普网络科技有限公司、深圳市魔方安全科技有限公司等技术支撑单位提供支持。

CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。

**联系方式：** cnnvdvul@itsec.gov.cn

（来源：CNNVD）

**分享网络安全知识 强化网络安全意识**

**欢迎关注《中国信息安全》杂志官方抖音号**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgo6Wm4L2BibeHzwhRTicRuJs1Z0OFdWiczbPI1cUs9Z9uePyz4hcOYicG7A/640?wx_fmt=jpeg&from=appmsg)

**《中国信息安全》杂志倾力推荐**

**“企业成长计划”**

**点击下图 了解详情**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5wpDbAx9CtalymyWvYQUqCgEZa3XU2m5TicISD2dSgu5pYn64JiaDdR5GiccwFq41ALk0NyQjlWLw9Gg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664162643&idx=1&sn=fcc4f3a6047a0c2f4e4cc0181243ee18&chksm=8b5ee7aabc296ebc7c8c9b145f16e6a5cf8316143db3edce69f2a312214d50a00f65d775198d&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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