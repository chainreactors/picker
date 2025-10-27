---
title: Apache 修复 Apache HTTP Server 中的源代码泄露漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520009&idx=1&sn=b958a0460ffa3e890f8c189660f04487&chksm=ea94be63dde337752a7dace28761adae32e92abbff78ddbb4dba723691c1d4eb489dd3e5deb2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-09
fetch_date: 2025-10-06T17:45:53.688284
---

# Apache 修复 Apache HTTP Server 中的源代码泄露漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQdyYTLlPv1TvF5IQZhfksIpMBUq1t4JyV6aCQvbIqTIhTVibCwDJthP9Qj9aHxiaJkicszaUbnLPibyw/0?wx_fmt=jpeg)

# Apache 修复 Apache HTTP Server 中的源代码泄露漏洞

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**作者：****Pierluigi Paganini**

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQdyYTLlPv1TvF5IQZhfksIoPkccnZ5kH4Ahx82uk0klPgm1SLWcLaQRMOSoFHwEeUlRBDkUBz9aA/640?wx_fmt=gif&from=appmsg)

**Apache 软件基金会修复了Apache HTTP Server 中的多个漏洞，其中包括拒绝服务 (DoS)、远程代码执行和越权访问等问题。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQdyYTLlPv1TvF5IQZhfksIJwpicyuJ7GWlUsCNIl7VqyicCic4jB610aT7PMVGTMx2DTNIDtRBK11yg/640?wx_fmt=gif&from=appmsg)

其中一个漏洞是严重的源代码披露漏洞，编号为CVE-2024-39884。安全公告提到，“Apache HTTP Server 2.4.60内核中的回归忽视了句柄的基于遗留内容类型配置的某些使用。’AddType’和类似配置在一定的情况下即间接请求文件时，可导致本地内容的源代码遭泄露。例如，PHP脚本会被提供而非被翻译。”

CVE-2024-39884由处理遗留内容类型配置的回归导致。在一定条件下，当 “AddType” 指令和类似设置被使用时，可无意间暴露将被处理的文件（如服务器端脚本和配置文件）的源代码，从而导致敏感数据被暴露给攻击者。

Apache 软件基金会建议用户升级至版本2.4.61。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[【已复现】Apache OFBiz 路径遍历漏洞(CVE-2024-36104)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519685&idx=5&sn=cd7840386d236e97bc419b0a943f9d25&chksm=ea94bcafdde335b99fff79a2689e78cb78922997a12f87792bff03a1861af54f7ec49cf32f44&scene=21#wechat_redirect)

[Apache 项目中存在依赖混淆漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519338&idx=2&sn=c65a447c216d55afbb9483c48c34f453&chksm=ea94bd00dde334161df74aa1e15e2b728e866bddfe2a1e21bfb5e44dfcf65213634e19fe8ad7&scene=21#wechat_redirect)

[Apache Superset 漏洞导致服务器易遭RCE攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517599&idx=3&sn=f9b4133a88826774ba2370f315ddb483&chksm=ea94b4f5dde33de31fafd6622cb2b37398ceb935de72fe956bfdb5dc3d1b4a4ae61195437351&scene=21#wechat_redirect)

[Apache Ivy 注入漏洞可导致攻击者提取敏感数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517437&idx=2&sn=b43eb67509ce31f1726c7bb953adb331&chksm=ea94b597dde33c816cc6b6b60429447908b3cbafd3b5194aa4e547412a0c05805aa001546707&scene=21#wechat_redirect)

[Apache Superset 会话验证漏洞可导致攻击者访问未授权资源](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516346&idx=2&sn=c84ae42d9a4eab4b30b8eba4a27130a5&chksm=ea94b1d0dde338c6da3cc189e548d10cc3511c1ef2d59f067bd428a6efae2df174b66c93b0f6&scene=21#wechat_redirect)

**原文链接**

https://securityaffairs.com/165422/security/apache-source-code-disclosure-flaw-apache-http-server.html

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