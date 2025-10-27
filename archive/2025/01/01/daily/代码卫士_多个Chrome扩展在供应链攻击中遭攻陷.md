---
title: 多个Chrome扩展在供应链攻击中遭攻陷
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521944&idx=2&sn=8d1b7899e6da840d037a71c74451e5c2&chksm=ea94a7f2dde32ee47681b3338b436c10dd41fd616efaf27c4fb436972b39445667b27089c0d9&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-01
fetch_date: 2025-10-06T20:07:28.958250
---

# 多个Chrome扩展在供应链攻击中遭攻陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRY63n6TucscvY5bTEFCsibNL70H6jN4icElk9RReH3KNrX2ibL6y8ZhkQ7AMRQyamJ0vF00dsqVRUlg/0?wx_fmt=jpeg)

# 多个Chrome扩展在供应链攻击中遭攻陷

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Cyberhaven 和其它多个 Chrome 扩展的恶意版本被发布在谷歌 Chrome Web Store 中，组成攻击 Facebook 广告用户的供应链的一部分。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRY63n6TucscvY5bTEFCsibNGUiaXEFukLaJbzJeSe7U7lkzbLwEuoVVsMa6b9lLqttWTxvfN6luCow/640?wx_fmt=png&from=appmsg)

数据扩展安全公司 Cyberhaven 的一名员工遭钓鱼攻击之后，授权一款恶意 OAuth 应用 Privacy Policy Extension 在Cyberhaven 的 Chrome Web Store 账户发布。

钓鱼消息假装来自 Chrome Web Store，被发送到注册的支持邮件，声称该扩展的描述中因包含过多的关键词而将被从商店中删除。点击消息中的链接后，这名员工通过标准的谷歌授权流程被攻击，使得恶意第三方应用获得访问开发者账户的权限。

Cyberhaven 公司解释称，“这名员工启用了谷歌高阶保护功能，并开启了账号的多因素认证机制。这名员工并未收到多因素认证提示，他的谷歌凭据并未失陷。”

之后，攻击者利用这些权限在 Chrome Web Store 中发布了该扩展的恶意版本，并在12月25日至12月26日期间的存在时间超过24小时。该恶意版本24.10.4 之后被删除并替换为干净版本24.10.5。当该恶意版本存在于 Chrome Web Store 中时，被分发给启动了自动更新特性的用户。研究人员表示，“调查显示，Chberhaven 的其它系统，包括CI/CD流程和代码签名密钥并未遭攻陷。”

该恶意扩展似乎针对的是 Facebook.com 的广告用户，收集和提取访问令牌、用户ID、通过Facebook API 获得账户信息、商业账户以及广告账号信息。另外，该恶意代码为Facebook.com 增加了一个鼠标点击监听，因此当用户点击相关页面时它会检索所有图片。根据它处理所检索图片的不同方式，该代码会搜索QR代码来绕过captcha 和/或 2FA授权请求。

Cyberhaven 公司的融资已超过1.36亿美元，在2024年6月的C轮融资中获得8800万美元后市值达到4.88亿美元。

Nudge Security 公司的联合创始人兼首席技术官 Jaime Blasco 在LinkedIn 帖子中提到，其它的 Chrome 扩展也失陷，威胁行动者在很短的时间内创建了多个欺诈性域名，所有这些域名都托管在相同的IP地址上。至少存在五款其它失陷的Chrome 扩展，包括 Internxt VPN、VPNCity、Uvoice和ParrotTalks。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[在线阅读版：《2024中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520484&idx=1&sn=8a845b39720a318c297075e98f5fe5e0&scene=21#wechat_redirect)

[谷歌修复代码测试工具Bazel 中的严重供应链漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518821&idx=1&sn=8a1a67b87d1bbad6e1c80390fe7c1c61&scene=21#wechat_redirect)

[谷歌推出开源计划GUAC，保护软件供应链安全](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514298&idx=2&sn=5971ca324b4d2fe15146eefac3a7192c&scene=21#wechat_redirect)

[ShadowLogic 技术利用AI模型图创建无代码后门，可引发供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=2&sn=78b278425ea0267c473467bfb24894f2&scene=21#wechat_redirect)

[RSAC 2024观察：软件供应链安全进入AI+时代](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519497&idx=1&sn=3f531af375c16bd26e01ca94f96d2f6b&scene=21#wechat_redirect)

[SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=2&sn=7b4dbeae684f3e9a1f79148a5bacf221&scene=21#wechat_redirect)

[Hugging Face 等AI即服务平台易受严重漏洞影响，遭AI供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519250&idx=2&sn=9683638aaf21b4d1d794837ff20dd0ab&scene=21#wechat_redirect)

**原文链接**

‍

https://www.securityweek.com/several-chrome-extensions-compromised-in-supply-chain-attack/‍

题图：Pexels License

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