---
title: 丰田、奔驰、宝马等API漏洞暴露车主个人信息
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515203&idx=3&sn=1ce2594fe8a272445e3b52a3598227f3&chksm=ea948d29dde3043f06e675d6f61647db3b51b77bc3191575c8ab8aec96e8f443eab259a28d5f&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-06
fetch_date: 2025-10-04T03:10:13.953807
---

# 丰田、奔驰、宝马等API漏洞暴露车主个人信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRWK42xqr5Pr25UUF1Xc5fic2Gh8AK70cfHLSErx37F26zxgT7eERQicxfaVqYX35gqic1O2S7sl7q2w/0?wx_fmt=jpeg)

# 丰田、奔驰、宝马等API漏洞暴露车主个人信息

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究人员发现，近20家汽车制造商和服务中包含API漏洞，可使黑客执行恶意活动如解锁车门、启动汽车并追踪车辆，暴露客户的个人信息。这些漏洞影响多家知名车厂，包括宝马、劳斯莱斯、奔驰、法拉利、保时捷、捷豹、路虎、福特、起亚、本田、英菲尼迪、日产、讴歌、现代、丰田和捷尼赛思等。**

这些漏洞也影响多个汽车技术品牌Spireon和Reviver以及流服务SiriusXM。2022年11月，这些研究员曾披露了现代、捷尼赛思、本田、讴歌、日产、英菲尼迪以及SiriusXM中存在的漏洞问题。虽然在此前的研究中，研究人员解释了黑客可如何利用这些漏洞解锁和启动汽车，不过由于90天的最后期限已到，因此他们披露了关于这些API漏洞的更详细内容。

**0****1**

**访问内部门户网站**

最严重的API漏洞位于宝马和奔驰，它们均受企业范围内SSO漏洞的影响，可导致内部系统遭访问。对于奔驰，分析师可访问多个私有GitHub 实例、Mattermost上的多个聊天信道、服务器、Jenkins 和 AWS实例、连接客户汽车的XENTRY系统等。对于宝马，研究人员可访问内部交易门户，查询任何汽车的VIN以及检索包含敏感车主详情的销售文档。另外，他们还能利用这些SSO漏洞以任意员工或交易商的身份登录，并访问专为内部使用的应用程序。

**0****2**

**暴露车主详情**

利用其它API漏洞可使研究人员访问起亚、本田、英菲尼迪、日产、讴歌、奔驰、现代、捷尼赛思、宝马、劳斯莱斯、法拉利、福特、保时捷和丰田汽车的车主个人可识别信息。

在豪车案例中，披露车主信息非常危险，因为在某些情况下这些数据包括销售信息、物理位置信息以及客户地址信息。法拉利在CMS上的SSO执行非常糟糕，可泄露后台API路由并可导致攻击者从JavaScript代码片段中提取凭据。攻击者可利用这些漏洞访问、修改或删除任意法拉利客户账户、管理车辆信息或将它们自己设为车主。

**0****3**

**追踪车辆GPS信息**

这些漏洞可导致黑客实时追踪汽车、引入潜在的物理风险并影响数百万名车主的隐私。

保时捷是受影响的品牌之一，漏洞位于其遥测系统中，可导致攻击者检索车辆位置并发送命令。GPS追踪解决方案Spireon 还易受车辆位置披露影响，对使用其服务的1550万辆汽车造成影响，甚至可能导致攻击者对其远程管理面板具有完全的管理员访问权限，导致攻击者解锁汽车、启动引擎或禁用起动机。第三个受影响的是Reviver，它是一家数字化车牌厂商，其管理员面板易遭未认证的远程访问，可导致其GPS数据和用户记录遭任何人访问，许可车牌通信遭修改等。

研究人员说明了如何利用这些漏洞在Reviver面板上将车辆标记为“被盗”，而这一标记行为将自动向警察通知该事件，导致车主/司机处于不必要的风险中。

**0****4**

**最少化暴露**

车主可通过限制汽车或移动伴侣应用中存储的个人信息量来免受此类漏洞影响。同时也有必要在可用的最私密模式中设置车载信息服务，并阅读隐私策略，了解数据的使用方式。

研究人员还给出了购车建议，他们指出，“当购买二手车时，确保之前车主的账号已被清除。在可能的情况下为与汽车相连的应用和服务使用强密码并设置双因素认证。”

Spireon 公司的一名发言人回应称，“我们的网络安全专业人员和研究人员见面，讨论并评估了系统漏洞并立即执行了必要的修复措施。我们也采取积极主动的措施，进一步增强了产品安全性，并作为零件市场车载信息服务解决方案的领先提供商，继续竭诚为客户服务。Spireon 严肃对待所有安全问题并利用业内领先的工具集监控并扫描产品和服务中的已知和潜在的安全风险。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[丰田承认外包开发误将源代码上传至GitHub公开库且已泄露五年](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514172&idx=2&sn=0fb1816d6e9903c2ce310381d6841a3f&chksm=ea948956dde30040ff072e904e012909ec0b339d074b71c629fb5e6f7749a9af196f5cda19fd&scene=21#wechat_redirect)

[丰田汽车顶级供应商 Denso 疑遭勒索攻击，被威胁泄露商业机密](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510883&idx=1&sn=a3a7de413f3ddebaea440dbbd3c14870&chksm=ea949a09dde3131f99ad55605d1d77058e166be0b3fdacf7d0a6765ba464d5d46e9efb6c99bd&scene=21#wechat_redirect)

[因供应商遭不明网络攻击，丰田汽车宣布停产](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510707&idx=1&sn=66432bea8eda7ad73db1a0406b5f3c31&chksm=ea949bd9dde312cfdc46f04b0dcafcfdeb0a2022bc179af8a2483ab6ffe1b13231b2e9791bc5&scene=21#wechat_redirect)

[金融服务业遭受的 web 应用和API攻击活动增长257%](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514824&idx=2&sn=c6d8e281f203f65df2bf6fd6e305246b&chksm=ea948ba2dde302b49f7a2d3b916af7bdde8e62730c4479a72e8c7a041088d4013c99507dfb84&scene=21#wechat_redirect)

[Chromium 原型污染漏洞导致Sanitizer API 被绕过](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514074&idx=2&sn=69d12874944c58027b021bc2110113e1&chksm=ea9486b0dde30fa679fa1c66c7721ecea6485a6a51d6238c008ca0a4d85e28eb1181d83d6e7d&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/toyota-mercedes-bmw-api-flaws-exposed-owners-personal-info/

题图：Pexels License‍

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