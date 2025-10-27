---
title: 【安全圈】谷歌 Chrome 将于 6 月 3 日开始进行削弱广告拦截功能的更改
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652061026&idx=4&sn=9176703110ebf28cc00d36c3b30f2164&chksm=f36e1122c4199834b0d63daebf65142ff60af9ac5aa2dee5c6f31a78526db0ae3f2232816b7d&scene=58&subscene=0#rd
source: 安全圈
date: 2024-06-03
fetch_date: 2025-10-06T17:32:28.489675
---

# 【安全圈】谷歌 Chrome 将于 6 月 3 日开始进行削弱广告拦截功能的更改

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgd2WeWFg1PxmcuNFekLZwTftqc4qtY39Niadr4rGfOXfsISGu0obF7zvXbxQ6xD5wOqh6TZpxsylA/0?wx_fmt=jpeg)

# 【安全圈】谷歌 Chrome 将于 6 月 3 日开始进行削弱广告拦截功能的更改

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

广告拦截

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgd2WeWFg1PxmcuNFekLZwTwh8iczbDPg5ursTgmwR1J3ibZokwFulJZ0Rncm2D36vUqQ4Nkql3qU9A/640?wx_fmt=jpeg&from=appmsg)

谷歌将继续执行其计划，从 2024 年 6 月初开始逐步淘汰 Chrome 中的 Manifest V2 扩展，从而削弱广告拦截器的功能。

谷歌表示，这一决定是根据社区的进展和反馈做出的，社区认为这些进展和反馈令人满意，因此不会再拖延。

从 2024 年 6 月 3 日开始，使用 Chrome 版本 127 的用户将在 Chrome Beta、Dev 和 Canary 渠道上看到警告，而仍在使用 Manifest V2 的扩展程序将失去“精选”徽章。

在 Chrome 稳定版发布后，V2 扩展程序将逐步停用，并推荐使用 V3 替代程序。用户可以暂时重新启用 Manifest V2 扩展程序，但此选项最终将被删除。

使用“ExtensionManifestV2Availability”政策的企业将获得豁免直至 2025 年 6 月，因此他们将获得额外一年的时间来过渡到与 Manifest V3 兼容的附加组件。

什么是 Manifest V3？

Manifest V3 是 Google Chrome 扩展平台的最新版本，旨在增强 Chrome 扩展程序的安全性、隐私性、性能和整体可信度。

总而言之，Google 希望通过 Manifest V3 实现以下目标：

限制扩展对用户网络请求的访问。

强制开发人员将所有功能包含在扩展中，从而结束远程托管代码的做法。

将网络请求修改从扩展移至浏览器（服务工作者）。

使用专用服务工作者替换后台页面以提高浏览器性能。

虽然这对最终用户来说似乎是积极的，但新的框架给扩展开发人员带来了重大的技术挑战，特别是对于那些需要更好地控制浏览器功能（如广告拦截器）的开发人员来说，他们现在必须实施复杂的机制才能保持有效性。

uBlock Origin 被认为是最受欢迎的广告拦截器之一，它被迫创建一个名为uBO Lite (uBOL)的新项目，这是一个无需许可的 Manifest V3 浏览器扩展。

虽然此扩展可能对许多用户来说都很好用，但开发人员表示，对于更高级的用途，可能需要配置其他设置或向特定站点授予额外的权限。

一个明显的缺点是，扩展程序不再通过自动更新频繁更新规则集。相反，只有当扩展程序的新版本发布时，才会更新规则集。

uBlock 开发人员 创建了一个常见问题解答，解释了当前扩展和新 Manifest V3 版本之间的差异。

谷歌表示，它在此期间听取了扩展开发人员的反馈，并做出了有针对性的改进，例如支持用户脚本、屏幕外文档以及扩大“declarativeNetRequest”允许的规则集数量。

最近实施的关键变化包括跳过安全规则更新和版本回滚的审核，为开发人员提供更好的更新控制。

谷歌声称，由于其采取的加速采用的行动，超过 85% 的积极维护的 Chrome 扩展程序（包括 AdBlock、Adblock Plus、uBlock Origin 和 AdGuard 等流行的广告拦截器）都已迁移或发布支持 Manifest V3 的版本。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljZ1jGTpY6rXdUMmVLxZZbEXdxmAa2uOQDt7ZaIlnjC2uLqSYK2w0lGtT44wd9ZuFdvnRD0RPfaxg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljKXaHAiabApRD9oHyND5ztCmIZhXNo2603T6OmOcW7hrXqCLciaqBbojhGYgyPuibibKkCLD1Sn4QKAg/640?wx_fmt=jpeg&from=appmsg)[【安全圈】一天超 300 台设备受害，僵尸网络 CatDDoS 向思科 / 华为等厂商发起攻击](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652060950&idx=2&sn=6c46f175211ff24635a1871085235752&chksm=f36e1156c419984093dedba6b6215f67cceda57674ac7190dbe510901f9b55277e91406a605f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljZ1jGTpY6rXdUMmVLxZZbEkLiajcu8H0HS0QOa6vI2M4RC1RCY6y0tqIPpWf5o32qZFZLCeHff8OA/640?wx_fmt=jpeg&from=appmsg)[【安全圈】103GB，黑客声称已窃取酷冷至尊 50 万 Fanzone 会员信息](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652060950&idx=3&sn=2a7b2214e037eda8b7095ddab9444414&chksm=f36e1156c4199840328b125e2b7426b805c3b2f60df902b43708a53ae9277d6a8531d8d4bc84&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljZ1jGTpY6rXdUMmVLxZZbEiceSAowNfQJNYGE0pagRb91prZWJssg22ETy5B7tbftRIIswxVFqTMg/640?wx_fmt=jpeg&from=appmsg)[【安全圈】黑客利用 Check Point VPN 入侵企业网络](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652060950&idx=4&sn=6209469daa8943a8341d0ce4e3d41ad8&chksm=f36e1156c419984065940069a5ac216d79d781996db77d4fd4006829dbc3f3d8311900d977e0&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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