---
title: 日本CERT提醒：IO-Data 路由器中的多个0day已遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521692&idx=2&sn=adb3ff5ba3ff65807012edd28d90be20&chksm=ea94a4f6dde32de0aa4388ab79e16c2747401cfbe56fea1c1445d852c6c6e6561fc639e183a1&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-06
fetch_date: 2025-10-06T19:39:00.894820
---

# 日本CERT提醒：IO-Data 路由器中的多个0day已遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSOYGCXGx4P2NLnUOdmXpXaEVicVVwKJBHgkMD4HyFciaHtg4UzfqNfxzkIy8j4Q7Sh4ruicz8icI5p3g/0?wx_fmt=jpeg)

# 日本CERT提醒：IO-Data 路由器中的多个0day已遭利用

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**日本应急响应中心 (CERT) 提醒称，黑客正在利用 I-O Data 路由器设备中的多个0day漏洞，修改设备设置、执行命令、甚至关闭防火墙。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSOYGCXGx4P2NLnUOdmXpXa6ia0Jltj3CwSQd7Meelu1ia9v9TL4yibBTeib9ibH2libdwQQwXWP4P8K4aw/640?wx_fmt=png&from=appmsg)

I-O Data 公司在网站发布安全通告，证实了这些漏洞的存在。然而，修复方案在2024年12月18日才能推出，因此用户只有启用缓解措施才会避免暴露到风险中。

**3个0day漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSOYGCXGx4P2NLnUOdmXpXaYf54qCHCCOhj6uqOrd1aiazqdYibFDXrqFUCfdANoHdgMoPQ75DjOJrQ/640?wx_fmt=gif&from=appmsg)

这三个0day漏洞在2024年11月13日发现，分别是信息泄露、远程任意OS命令执行和导致防火墙禁用的漏洞。概述如下：

* CVE-2024-45841：敏感资源上的许可配置不当，导致低权限用户可访问关键文件。例如，了解guest 账号凭据的第三方可访问包含认证信息的文件。
* CVE-2024-47133：可导致认证的管理员用户在设备上注入并执行任意操作系统命令，利用配置管理中的输入验证不充分漏洞。
* CVE-2024-52464：固件中的未记录特性或后门可导致远程攻击者在无需认证的情况下，关闭设备防火墙并修改设置。

这三个漏洞影响 UD-LT1和UD-LT1/EX设备，前者是为多功能连接解决方案设计的混合 LTE 路由器，而后者是工业级版本。该固件的最新版本v2.1.9仅解决CVE-2024-52564。I-O Data 公司提到，其它两个漏洞的修复方案将在 v2.2.0中发布，计划在2024年12月18日发布。

在厂商发布通告证实这些漏洞时，客户已报道称这些漏洞已被用于攻击中。该安全公告提到，“近期我们收到混合LTE路由器’UD-LT1’和’UD-LT1/EX’客户的问询，他们反映称在无需VPN的情况下可从互联网访问配置界面。这些客户报告了来自外部来源的越权访问权限。”

在安全更新发布前，I-O Data 公司建议用户执行如下缓解措施：

* 禁用所有网络连接方法的远程管理特性，包括 WAN Port、Modem 和VPN设置。
* 仅限连接VPN网络的访问，阻止未授权的外部访问。
* 将默认的 “guest” 用户密码修改为更复杂的长度超过10个字符的密码。
* 定期监控和验证设备设置，提前检测未授权变更，并将设备重置为出厂默认设置，检测到攻陷时进行重新配置。

I-O Data UD-LT1和UD-LT1/EX LTE 路由器主要在日本国内营销和出售，支持多个运营商如 NTT Docomo 和 KDDI，并兼容主流的MVNO SIM卡。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[QNAP修复NAS、路由器软件中的严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521595&idx=1&sn=d9644a20742d498ecf898b968d561b3f&scene=21#wechat_redirect)

[合勤提醒注意路由器中的严重OS命令注入漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=2&sn=a47864fc0328391d921ce4629b3bac8b&scene=21#wechat_redirect)

[D-Link 不打算修复 DIR-846W 路由器中的这四个RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=1&sn=33ddf9ab82fd7db2d5c560e478add189&scene=21#wechat_redirect)

[华硕：严重的远程绕过漏洞影响7款路由器](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519766&idx=1&sn=e5617e80059a29c20c16b011271e8511&scene=21#wechat_redirect)

[美国超60万台路由器遭神秘攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519644&idx=2&sn=d8a9e69c892d69704a1ce3fc0d49ebf7&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/japan-warns-of-io-data-zero-day-router-flaws-exploited-in-attacks/

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