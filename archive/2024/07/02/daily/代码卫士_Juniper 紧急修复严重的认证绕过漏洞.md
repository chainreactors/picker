---
title: Juniper 紧急修复严重的认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519930&idx=1&sn=fb9fb97863d38cac47e2e8c94fdfc267&chksm=ea94bfd0dde336c6cc905b39fdfcd6192b649ef99de88faa7d5c707a3eedf44f88820ce1fbee&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-02
fetch_date: 2025-10-06T17:46:06.464004
---

# Juniper 紧急修复严重的认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIcfu3ianZSuTokYGlW1spic3XTGw15nmAVQaEWqUv0a9iaZmSwxyTY90icg/0?wx_fmt=jpeg)

# Juniper 紧急修复严重的认证绕过漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIgicmyV2uPHgCahcKFAjGX3XpEZ1sLSJnP7smNHv9wukia0xczgE9EXwA/640?wx_fmt=gif&from=appmsg)

**Juniper Networks 公司发布紧急更新，修复了Session Smart Router (SSR)、Session Smart Conductor 和 WAN Assurance Router 产品中的一个严重漏洞 (CVE-2024-2973)，可导致认证绕过后果。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIOwbFttNmrCoQ69NYia8OnAuJEibDE29pLTicX6GaPictHkvnUMfFkEvUmw/640?wx_fmt=gif&from=appmsg)

攻击者可利用该漏洞完全控制设备。漏洞描述提到，“Juniper Networks 通过冗余对等体运行的Session Smart Router 或 Conductor中存在通过 Alternate Path 或 Channel 实现认证绕过的漏洞，可导致基于网络的攻击者绕过认证并完全控制设备。”

安全公告提到，“只有运行在高可用性冗余配置的Routers 或 Conductors 才受该漏洞影响。” Web 管理员应用对服务可继续性至关重要的“高可用性冗余配置”。该配置对于维护不受破坏的服务和提升对不可见、具有破坏性的事件的弹性。这使得易受攻击的配置在重要的网络基础设施中非常常见，包括在大型企业环境、数据中心、电信、电子商务和政府或公共服务等。

受影响的版本如下：

Session Smart Router 和 Conductor：

* 所有早于5.6.15的版本
* 自早于6.1.9-lts的6.0版本起
* 自早于6.2.5-sts的6.2版本起

WAN Assurance Router：

* 早于 6.1.9-lts 的6.0版本
* 早于6.3.5-sts 的6.2版本

Session Smart Router 的安全更新已在 5.6.15、6.1.9-lts 和 6.2.5-sts 中发布。WAN Assurance Routers 在连接到 Mist Cloud 时就会自动打补丁，但高可用性集群的管理员需要更新至SSR-6.1.9或SSR-6.2.5。

Juniper 公司还提到，升级 Conductor 节点足以将修复方案自动应用到联网路由器，但路由器应当被升级至最新可用版本。该厂商向客户保证称该修复方案的应用并不会破坏生产流量，对于基于web的管理和API的影响很小，出现大约30秒的停机。

目前尚不存在应变措施，建议措施只是应用可用修复方案。

**针对Juniper 的攻击活动**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRo7ibaa5icpfu7hIC0vDk7cIibAE3uRanMMwbOsLlDvP4rRxCmAia5B9hltYZD8fpTkD410VHS9RlcRQ/640?wx_fmt=gif&from=appmsg)

鉴于 Juniper 产品部署的重要且具有价值的环境，Juniper 产品是备受黑客欢迎的目标。

去年，Juniper EX 交换机和 SRX 防火墙被纳入由四个漏洞组成的利用链中。就在厂商发布相关公告的一周内，就出现了恶意活动。几个月后，CISA提醒注意这些漏洞遭规模更大的利用，督促联邦机构和重要组织机构在四天内应用这些安全更新，该短促的CISA最后期限是不太常见的。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Juniper Networks 修复交换机、防火墙中的多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518790&idx=2&sn=8654a2f71be0f352dbd073de6482ef88&chksm=ea94bb2cdde3323a808c47f00e4a82d449bdf6bfa0d08ea05135862eb834e999aafa2ff7b965&scene=21#wechat_redirect)

[Juniper 提醒注意防火墙和交换机中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=2&sn=0cbdae2b9be2d7406ffaea5ba7dc47d1&chksm=ea94b8a7dde331b1ffbd02134c098d7117b1af631461588e39a663cd6ee5834bc93977380167&scene=21#wechat_redirect)

[CISA 提醒注意已遭活跃利用的 Juniper 预认证 RCE 利用链](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518122&idx=1&sn=d6b5a20e45ee8897ed249a7bdde21ebb&chksm=ea94b6c0dde33fd6d3d93c996ad772d6f9f1d4744294db1c793f9f4cd69798f6515ac436fa3c&scene=21#wechat_redirect)

[Juniper Networks 修复Junos OS中的30多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517894&idx=2&sn=dfa23961cb9b4c490ab70b8e96d111c7&chksm=ea94b7acdde33ebaab16086f440a9e1bced5c6e4ff4629c4650ec7c2900ac81edeec34946ada&scene=21#wechat_redirect)

[上万台 Juniper 设备易受未认证RCE漏洞攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517693&idx=3&sn=cf7aebe9fc74cea2001da86238add0cb&chksm=ea94b497dde33d81e53986ae709bb0281448e059268e057b632beb1f3589b7d6b28b9dc32158&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/juniper-releases-out-of-cycle-fix-for-max-severity-auth-bypass-flaw/

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