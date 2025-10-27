---
title: 12年来最严重的 WordPress 漏洞，可大规模接管管理员权限
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521513&idx=1&sn=b60ee79ea2fbcfeaae560373faa7a2cf&chksm=ea94a583dde32c95779d3ac2afec31953b99e514551aec14bfc515de9ced953efb77c5563092&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-19
fetch_date: 2025-10-06T19:18:42.956061
---

# 12年来最严重的 WordPress 漏洞，可大规模接管管理员权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeibfrzaakCRTWC0LtIE5ic7fpB0KyonbgxETJtaGZMlbGKzGh2AEIsBrvg/0?wx_fmt=jpeg)

# 12年来最严重的 WordPress 漏洞，可大规模接管管理员权限

BILL TOULAS

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**WordPress 插件 “Really Simple Security”（此前被称为 “Really Simple SSL”）的免费和专业版本均受一个严重的认证绕过漏洞影响。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeibvxd5tc1COE4kUV1E9ZmEQiaHvJ1Wicapmnu7L9zKeSN2xB8WnBrRMYJg/640?wx_fmt=gif&from=appmsg)

Really Simple Security 是 WordPress 平台的一个安全插件，提供SSL配置、登录暴露、双因素认证层以及实时漏洞检测服务。其免费版本已用于超过400多万个网站上。

Wordfence 公司公开披露了该漏洞，称其为12年来报送的最严重的漏洞，并提醒称该漏洞可导致远程攻击者获得对受影响网站的完整管理员访问权限。更糟糕的是，可通过自动化脚本大规模利用该漏洞，从而可能导致大规模网站遭接管后果。

而这也是Wordfence 提醒托管提供商更新客户网站上的插件并扫描数据库以确保未运行易受攻击版本的原因所在。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMS2FjkxTbyib7OBoPjgGDeeibI1DRe3GvlbfrWtHb3ZAlNLSsZZJ2IqdOZ4NaxjmzFL6B1KzYobmjew/640?wx_fmt=gif&from=appmsg)

**2FA导致更脆弱的安全性**

该漏洞的编号是CVE-2024-10924，是由 Wordfence 公司的研究员 István Márton 在2024年11月6日发现的。该漏洞由该插件的双因素REST API 操作中的用户认证处理不当造成的，可导致任何用户账户包括管理员在内的账户遭越权访问。

具体而言，漏洞位于 “check\_login\_and\_get\_user()”函数中。该函数通过检查 “user\_id”和 “login\_nonce” 参数对用户身份进行验证。当 “login\_nonce” 不合法时，该请求本应但并未遭到拒绝，而是调用“authenticate\_and\_redirect()” 只基于 “user\_id” 对用户进行认证，从而导致认证绕过后沟。

当双因素认证启用时，该漏洞可遭利用，而且即使默认是禁用状态，很多管理员将允许启用以便获得更强的账户安全性。该漏洞影响Really Simple Security 9.0.0至9.1.1.1的免费、专业以及多网站专业 (Pro Multisite) 版本。

目前，开发人员已经正确处理 “login\_nonce” 验证失败情况，即会立即退出 “check\_login\_and\_get\_user()” 函数。该修复方案已经应用到该插件的9.1.2版本，已在11月12日发布在Pro版本以及在11月14日为免费用户发布。厂商与 WordPress.org 协作，强制用户进行安全更新，不过网站管理员仍然应当检查并确保自己运行的是最新版本9.1.2。专业版用户在许可过期时已禁用自动更新功能，因此必须手动更新至9.1.2。

截止到昨天，WordPress.org 数据显示，该插件的免费版本的下载次数约为45万次，即350万个网站易受攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[WordPress 插件被安后门，用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519884&idx=2&sn=394599c6e622c656ae34d0c38cb671fa&chksm=ea94bfe6dde336f0971c21b57ed4c97af0185fd27f42cbe3f54350b5600357533a0d61ab1a94&scene=21#wechat_redirect)

[WordPress 插件 Forminator 中存在严重漏洞，影响30多万站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519350&idx=1&sn=44cdd16335bfd4e16c8f57397e448771&chksm=ea94bd1cdde3340a03401c5d3c557a9d7ed61164d414c3cf30a1707f0002703fe0d7559b1840&scene=21#wechat_redirect)

[热门Wordpress 插件 LayerSlider 中存在严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519223&idx=2&sn=a927e2b6bd81218102ea07e2de3133d7&chksm=ea94ba9ddde3338bf760ba11cb2fb665b8ad6e728bcc5b21ea7c1c1bf46968a037b5e55499a3&scene=21#wechat_redirect)

[热门 WordPress 插件 Ultimate Member 中存在严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518957&idx=1&sn=8d096042c0c0ab672b2763c4be529085&chksm=ea94bb87dde332919301d11f7a8c23002f628ae325511713f594d8afae88da1d90d44818421f&scene=21#wechat_redirect)

[WordPress 插件 LiteSpeed 漏洞影响500万个站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518947&idx=3&sn=a79e0235f3e78c2f4980247b4e0a365d&chksm=ea94bb89dde3329f127d8c01ddbfd59e454133a12f03962b70d34129434f08d38529852aa820&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/security-plugin-flaw-in-millions-of-wordpress-sites-gives-admin-access/

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