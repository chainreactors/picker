---
title: 用户名太长的坏处：Okta 修复认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521392&idx=1&sn=5ed582159f171db2001138a8ba65e297&chksm=ea94a51adde32c0c02371dadb481e0b6f1d6763dc98bc2b323c974300a40d061d2aa67a43277&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-06
fetch_date: 2025-10-06T19:18:46.638483
---

# 用户名太长的坏处：Okta 修复认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRcr7DLhfnx9TwWNonGoZ997VWOByE6qI6F3eibRCs2hoz26PVFfRf5TZUWcXUOOROdsjOuy3YZicQg/0?wx_fmt=jpeg)

# 用户名太长的坏处：Okta 修复认证绕过漏洞

Darkreading

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRcr7DLhfnx9TwWNonGoZ996RUkkD93CHViaau6cdO5OhY5jAXpSjjHSBMz3PgibsoBAM5fjGrPOqVA/640?wx_fmt=gif&from=appmsg)

**Okta 修复了一个认证绕过漏洞，影响拥有长用户名或长域名的用户。**

该漏洞可导致犯罪分子仅通过一个用户名就通过 Okta 公司的 AD/LDAP 授权验证。不过，只有当满足了一系列条件时，该漏洞才会被利用。其中一个条件是用户名为52个字符或更长。

虽然这么长的字符不常见，但一些用户会将邮件地址作为用户名，从而造成了这种可能性。Okta 在安全公告中提到，其它需要满足的条件是，用户此前是否认证，创造认证缓存；以及该缓存是否为首次使用，而“如果 AD/LDAP 代理因网络流量较高而宕机或者无法获取”则可能发生这种情况。

该漏洞由 Okta 公司在10月30日发现，当时该漏洞已在系统中游荡了三个月。虽然已修复，但Okta 仍然建议用户查看自7月23日起的日志中是否存在任何异常的认证尝试情况。

Okta 还建议客户至少执行多因素认证机制，而这并非利用的前提条件。目前尚不清楚是否存在在野利用尝试。Okta 尚未回复相关问题。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Okta：CORS 特性遭凭据填充攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519622&idx=2&sn=b8b517a2726066b4a82f1ac6165f9aa4&chksm=ea94bcecdde335fa5f395b2751bc2ba27979db6795ad534100d7e3407a5e64e7f28420a24227&scene=21#wechat_redirect)

[Okta提醒客户注意“史无前例”的凭据填充攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519374&idx=2&sn=707e7d24d6c7e479a253a74384db5b8a&chksm=ea94bde4dde334f222523bd1a7cb8c157f66a7831179295c3724db4fcdf295d23fe7cbd62f58&scene=21#wechat_redirect)

[在公司电脑登录个人谷歌账户，Okta 支持系统受陷134家客户受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518068&idx=2&sn=f43aa3c83fab809bc74afc70bb2e5901&chksm=ea94b61edde33f0875e8a63897c3c9426cdfbbd544831ab1cca8526efa64bc87c1f9a426752a&scene=21#wechat_redirect)

[因第三方遭攻击，Okta的5000名员工个人数据被泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518061&idx=1&sn=731606b45f2a344f1de6e4107a9822a5&chksm=ea94b607dde33f1116f225eb82eab688041bd860991750852896f3c8067c7299eb65f7775890&scene=21#wechat_redirect)

**原文链接**

https://www.darkreading.com/vulnerabilities-threats/okta-fixes-auth-bypass-bug-three-month-lull

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