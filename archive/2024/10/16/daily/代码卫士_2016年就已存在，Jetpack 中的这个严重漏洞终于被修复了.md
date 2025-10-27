---
title: 2016年就已存在，Jetpack 中的这个严重漏洞终于被修复了
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521093&idx=2&sn=0e8722e391f5315692fb46494ee4c4b9&chksm=ea94a22fdde32b39c594e884c3d9c1189f426e88c963cd7073b26e7d547a6f3b1ceabdf1498e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-16
fetch_date: 2025-10-06T18:54:00.876451
---

# 2016年就已存在，Jetpack 中的这个严重漏洞终于被修复了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNsibBR1mwd2jORzHFYGnWtkkiatjmBYTe8rxGibJs3xCUbTdkHic8SXl7Bg/0?wx_fmt=jpeg)

# 2016年就已存在，Jetpack 中的这个严重漏洞终于被修复了

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT41yHviaIUUg8Vhiafe3BhDNQCyjgiaGSFotcrEucz7ibW6rIo7dkHM3nwmpbfxH2y2Qv9SleiayVmOJg/640?wx_fmt=gif&from=appmsg)

**WordPress 插件 Jetpack 发布重要安全更新，修复了一个2016年就已存在的严重漏洞，它可导致已登录用户访问其它访客提交的表单，影响2700万个站点。**

Jetpack 是由 Automattic 研发的流行 WordPress 插件。该公司专门提供用于增强网站功能、安全和性能的工具。该漏洞是在一次内部审计时发现的，影响自2016年发布的3.9.9起的所有版本，位于 Contact Form 特性中。

Jetpack 安全公告提到，“该漏洞可由网站上任何一个已登录用户利用，读取由其它访客提交的表单。”

Automattic 公司已为受影响的101个版本发布了修复方案。这些版本包括：

13.9.1、13.8.2、13.7.1、13.6.1、13.5.1、13.4.4、13.3.2、13.2.3、13.1.4、13.0.1、12.9.4、12.8.2、12.7.2、12.6.3、12.5.1、12.4.1、12.3.1、12.2.2、12.1.2、12.0.2、11.9.3、11.8.6、11.7.3、11.6.2、11.5.3、11.4.2、11.3.4、11.2.2、11.1.4、11.0.2、10.9.3、10.8.2、10.7.2、10.6.2、10.5.3、10.4.2、10.3.2、10.2.3、10.1.2、10.0.2、9.9.3、9.8.3、9.7.3、9.6.4、9.5.5、9.4.4、9.3.5、9.2.4、9.1.3、9.0.5、8.9.4、8.8.5、8.7.4、8.6.4、8.5.3、8.4.5、8.3.3、8.2.6、8.1.4、8.0.3、7.9.4、7.8.4、7.7.6、7.6.4、7.5.7、7.4.5、7.3.5、7.2.5、7.1.5、7.0.5、6.9.4、6.8.5、6.7.4、6.6.5、6.5.4、6.4.6、6.3.7、6.2.5、6.1.5、6.0.4、5.9.4、5.8.4、5.7.5、5.6.5、5.5.5、5.4.4、5.3.4、5.2.5、5.1.4、5.0.3、4.9.3、4.8.5、4.7.4、4.6.3、4.5.3、4.4.5、4.3.5、4.2.5、4.1.4、4.0.7、3.9.10。

网站所有人和管理员用户应当检查该软件是否已经更新到上述版本，如尚未更新，则需手动升级。

Jetpack 表示，目前尚未有证据表明该漏洞已遭利用，但仍然建议用户尽快升级至已修复版本，以免有心之人利用该漏洞。

鉴于不存在针对该漏洞的缓解措施或应变措施，因此唯一可用且推荐的解决方案就是应用可用更新。目前该漏洞的详情和利用方式尚未公布。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[WordPress 插件被安后门，用于发动供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519884&idx=2&sn=394599c6e622c656ae34d0c38cb671fa&chksm=ea94bfe6dde336f0971c21b57ed4c97af0185fd27f42cbe3f54350b5600357533a0d61ab1a94&scene=21#wechat_redirect)

[WordPress 插件 Forminator 中存在严重漏洞，影响30多万站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519350&idx=1&sn=44cdd16335bfd4e16c8f57397e448771&chksm=ea94bd1cdde3340a03401c5d3c557a9d7ed61164d414c3cf30a1707f0002703fe0d7559b1840&scene=21#wechat_redirect)

[热门Wordpress 插件 LayerSlider 中存在严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519223&idx=2&sn=a927e2b6bd81218102ea07e2de3133d7&chksm=ea94ba9ddde3338bf760ba11cb2fb665b8ad6e728bcc5b21ea7c1c1bf46968a037b5e55499a3&scene=21#wechat_redirect)

[WordPress 插件 LiteSpeed 漏洞影响500万个站点](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518947&idx=3&sn=a79e0235f3e78c2f4980247b4e0a365d&chksm=ea94bb89dde3329f127d8c01ddbfd59e454133a12f03962b70d34129434f08d38529852aa820&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/jetpack-fixes-critical-information-disclosure-flaw-existing-since-2016/

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