---
title: Roundcube Webmail XSS 漏洞被用于窃取登录凭据
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521165&idx=2&sn=7bfb29f17ff7d1e5ee3a692d0325509c&chksm=ea94a2e7dde32bf194da0ee3afbb6e7b53ba6046185343d45732773ec0b1c7298b65203944a5&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-22
fetch_date: 2025-10-06T18:51:56.606052
---

# Roundcube Webmail XSS 漏洞被用于窃取登录凭据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQMmELRlnGCmKmc9MJEIRgibFOj2uI0CkmseMMJnicFReuGYgtRxk7Fia6Z1QQZO1xJ5GWMtjHicSLqrw/0?wx_fmt=jpeg)

# Roundcube Webmail XSS 漏洞被用于窃取登录凭据

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQMmELRlnGCmKmc9MJEIRgibibyn5HwHicewAFT52I312H7R9YM4L1CO2ShlZFyvOSFADf1WMKERIypA/640?wx_fmt=gif&from=appmsg)

**未知威胁行动者们被指利用开源网络邮箱软件 Roundcube 中的一个漏洞，发动钓鱼攻击以窃取用户凭据。目前该漏洞已修复。**

俄罗斯网络安全公司 Positive Technologies 表示，上个月发现一份邮件被发送到位于一个独联体国家的某个政府组织机构。然而，该邮件最初已在2024年6月发送。该公司在本周早些时候发布的一份分析报告中提到，“该邮件看似是一条没有文本的消息，里面仅包含一份附件文档。然而，该邮箱客户端并未显示附件。邮件主体包含具有 eval (atob(…))语句的唯一标记，能够解码和执行 JavaScript 代码。”

Positive Technologies公司提到，该攻击链是为了通过 SVG 动画属性利用存储型XSS漏洞 (CVE-2024-37383)，在受害者的 web 浏览器上下文中执行任意 JavaScript。换句话说，远程攻击者能够加载任意 JavaScript 代码并通过诱骗邮件收件人打开特殊构造信息的方式访问敏感信息。该问题已在2024年5月发布的1.5.7和1.6.7版本中修复。

Positive Technologies 公司提到，“通过将 JavaScript 代码作为插入 ‘href’ 的值，不管 Roundcube 客户端何时打开恶意邮件，我们能够在 Roundcube 页面执行它。”

在本案例中，该 JavaScript payload 将空白的微软 Word 附件 (“Road map.docx”) 保存，之后使用插件 ManageSieve 获取邮件服务器的消息。它还在向用户显示的 HTML 页面中显示登录表单，欺骗受害者提供 Roundcube 凭据。在最后一个阶段，被捕获的用户名和密码信息被提取到托管在 Cloudflare 的远程服务器中。

目前尚不清楚谁发动了利用活动，尽管Roundcube 漏洞已遭多个黑客组织利用如 APT 28等。该公司表示，“虽然 Roundcube 网络邮箱可能并不是使用最广泛的邮件客户端，但因得到政府机构的广泛应用，因此仍然是黑客目标。针对该软件的攻击可造成重大损失，导致网络犯罪分子窃取敏感信息。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[利用Roundcube缺陷仅需发送一份邮件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485624&idx=1&sn=d78df4d6e24b0123f2e980628759ffe9&chksm=ea9739d2dde0b0c4432ee95f5dfc887e6d8598edb7fb2d399b9862f54bb52c3740997541c89c&scene=21#wechat_redirect)

[CISA、FBI督促消除XSS漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520856&idx=2&sn=e42af408ee177430c69f52668c7cc6eb&chksm=ea94a332dde32a247ff4d6cdf023ddf6f8317162ed60c534809d8bcaff0fc7ce94e472f08532&scene=21#wechat_redirect)

[思科服务器管理工具中存在 XSS 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516356&idx=1&sn=3a870e38244c8f43090fe23f54c81fa7&chksm=ea94b1aedde338b8242499091a2cb37dec7924bffa0bde2f1dc62c5d42e10242fb0125850d86&scene=21#wechat_redirect)

[思科提醒注意Small Business路由器中的XSS漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519231&idx=2&sn=b7b32d73cbe2046719780c03304729ce&chksm=ea94ba95dde333834c93da6e263ab3af72ce14f2a171799c65802dab992336cd0c1a96492159&scene=21#wechat_redirect)

[SolarWinds 修复 Web Help Desk 中的硬编码凭据漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520566&idx=2&sn=2201f2665ef471e47e5dc87762920af5&chksm=ea94a05cdde3294a691fb126918df1c46abe77fac1ddc817f2deafa7344a6764133a7ef02167&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/hackers-exploit-roundcube-webmail-xss.html

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