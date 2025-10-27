---
title: LiteSpeed Cache 插件中的严重漏洞正遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520597&idx=1&sn=9b3ac1b3b69c7d221bc720fd7a3db778&chksm=ea94a03fdde3292902b6c3d7139405802f57a749310705af7fc05e5a069ef6f28ccd0544c717&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-27
fetch_date: 2025-10-06T18:06:09.930942
---

# LiteSpeed Cache 插件中的严重漏洞正遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRFuCammbdewv1coewdhuxAVyNh0jzfrLlRKzl9j1YVItvudzF7GdQmCpNH2RYOg9eQreeUwPnKVA/0?wx_fmt=jpeg)

# LiteSpeed Cache 插件中的严重漏洞正遭利用

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**黑客正在利用 WordPress 插件 LiteSpeed Cache 中的一个严重漏洞 (CVE-2024-28000)，而距离技术详情公开仅一天的时间。**

LiteSpeed Cache 是一款用于加速响应时间的插件。攻击者可在无需认证的情况下，在其6.3.0.1及之前版本上实现提权。该漏洞产生的原因是模拟特性中存在弱哈希检查，可被攻击者暴力破解哈希值，创建恶意管理员账户，从而完全控制受影响网站，安装恶意插件、修改重要设置、将流量重定向至恶意网站并窃取用户数据。

Patchstack 公司的研究员 Rafie RMuhammad 共享了如何触发哈希生成的详情，展示了如何暴力破解哈希以提升权限，之后通过 REST API 创建新的管理员账户。

Muhammad 的方法表明，暴力破解可以每秒三个请求的速度遍历所有100万个可能得安全哈希值，并仅需几小时或最多一周的时间，就能够以任何用户ID的身份获得站点访问权限。

LiteSpeed Cache 用于500多万个网站。截止目前，仅有30%的站点运行安全版本，即数百万个易受攻击的网站成为攻击面。

WordPress 安全公司 Wordfence 报道称，在过去24小时内检测并拦截了针对该漏洞的超过48500次攻击，反映了密集的利用活动。Wordfence 公司的研究员 Chloe Charmberland 提醒称，“毫无疑问，该漏洞将很快遭活跃利用。”

这是今年黑客第二次针对 LiteSpeed Cache。五月份，攻击者利用一个跨站点脚本漏洞 (CVE-2023-40000) 创建恶意管理员账户并接管易受攻击的网站。当时，WPScan 报道称，威胁行动者们在4月份开始扫描目标，从单个恶意IP地址检测到超过120万次。

建议 LiteSpeed Cache 用户尽快升级至最新可用版本，或者从网站卸载该插件。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[WordPress 插件被安后门，用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519884&idx=2&sn=394599c6e622c656ae34d0c38cb671fa&chksm=ea94bfe6dde336f0971c21b57ed4c97af0185fd27f42cbe3f54350b5600357533a0d61ab1a94&scene=21#wechat_redirect)

[WordPress 插件 Forminator 中存在严重漏洞，影响30多万站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519350&idx=1&sn=44cdd16335bfd4e16c8f57397e448771&chksm=ea94bd1cdde3340a03401c5d3c557a9d7ed61164d414c3cf30a1707f0002703fe0d7559b1840&scene=21#wechat_redirect)

[WordPress 插件 LiteSpeed 漏洞影响500万个站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518947&idx=3&sn=a79e0235f3e78c2f4980247b4e0a365d&chksm=ea94bb89dde3329f127d8c01ddbfd59e454133a12f03962b70d34129434f08d38529852aa820&scene=21#wechat_redirect)

[备份插件存在严重RCE漏洞，可导致WordPress网站遭接管](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518349&idx=2&sn=da5a15622c08723ed8cacf81f9a2dd55&chksm=ea94b9e7dde330f1ebb50e99491cbc925e6e932730363f189179878a4dc2b3a4ccb480badb86&scene=21#wechat_redirect)

[黑客利用WordPress 插件中的提权0day攻陷网站](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516908&idx=1&sn=3861a45ade1fc801daa3c767fef3f318&chksm=ea94b386dde33a90582ec8599b01780524bb88c9f1a2cd4cfd9874889611594313e5443e60b1&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-are-exploiting-critical-bug-in-litespeed-cache-plugin/

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