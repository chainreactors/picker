---
title: Palo Alto 提醒注意严重的 PAN-OS RCE漏洞
url: https://mp.weixin.qq.com/s/VqaBYT8TN6xcERGTqvKi8w
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:38.853950
---

# Palo Alto 提醒注意严重的 PAN-OS RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfURy0dbXONRUK8SbxiaV1yMBVQRSeF2pDjFlYBglVeePbaIFCM8CNeyfCB3gnD2JvdH23SXNAQguVUAib5H1Ud04XJ1rOrsfZ5fk/0?wx_fmt=jpeg)

# Palo Alto 提醒注意严重的 PAN-OS RCE漏洞

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Palo Alto Networks****公司发布公告称，PAN-OS软件中存在一个严重的缓冲区溢出漏洞 (CVE-2026-0300) 且已遭在野利用。**

该漏洞被描述为一个未认证的远程代码执行案例。如果将User-ID认证门户配置为允许来自互联网或任何非可信网络的访问，其CVSS评分为9.3；若仅允许可信内部IP地址访问该门户，严重程度则降至8.7。

Palo Alto Networks 公司表示：“Palo Alto Networks PAN-OS软件的User-ID认证门户（即Captive Portal）服务中存在一个缓冲区溢出漏洞，允许未认证的攻击者通过发送特制的数据包，在PA系列和VM系列防火墙上以root权限执行任意代码。”

根据Palo Alto Networks的说法，该漏洞已被“有限利用”，特别是针对那些User-ID认证门户已暴露于公网的实例。以下版本受该漏洞影响：

* PAN-OS 12.1 -低于12.1.4-h5和低于12.1.7的版本
* PAN-OS 11.2 - 低于11.2.4-h17、低于11.2.7-h13、低于11.2.10-h6和低于11.2.12的版本
* PAN-OS 11.1 - 低于11.1.4-h33、低于11.1.6-h32、低于11.1.7-h6、低于11.1.10-h25、低于11.1.13-h5和低于 11.1.15的版本
* PAN-OS 10.2 - 低于 10.2.7-h34、低于10.2.10-h36、低于10.2.13-h21、低于10.2.16-h7和低于10.2.18-h6的版本

目前该漏洞尚未修复，Palo Alto Networks公司计划从2026年5月13日开始发布修复程序。该公司还表示，该漏洞仅适用于配置为使用User-ID认证门户的PA系列和VM系列防火墙。

Palo Alto Networks 公司提到，“遵循标准安全最佳实践的客户，例如将敏感门户限制在可信内部网络，其风险将大大降低。” 在补丁发布之前，建议用户将User-ID认证门户的访问限制在仅可信区域，或者如果不需要该功能，则完全禁用。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Palo Alto Networks 修复PAN-OS 中的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522232&idx=2&sn=3bc7a4466c3c33ff643ca604524fa401&scene=21#wechat_redirect)

[Palo Alto 修复已遭利用的严重PAN-OS DoS 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521932&idx=1&sn=518332fa38f3263ee23df7a70c1187d3&scene=21#wechat_redirect)

[Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&scene=21#wechat_redirect)

[Palo Alto：注意！PAN-OS 防火墙 0day 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=1&sn=86e226003b5da9dd0d6867f4b45fcb1a&scene=21#wechat_redirect)

[Palo Alto Networks：PAN-OS DDoS 漏洞已遭在野利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513567&idx=1&sn=181b3bb7e1b34dc9dd67bfde798f4c7d&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/05/palo-alto-pan-os-flaw-under-active.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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