---
title: cURL 严重漏洞已存在25年，影响300亿台设备
url: https://mp.weixin.qq.com/s/DAN_bR1UF8m3Ew6FbouGaQ
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:49:44.393762
---

# cURL 严重漏洞已存在25年，影响300亿台设备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfVBafeEv20JKpgAomsvsfBey8ug1ldxriamjzgJ8hWY5EbclUqA5piczMtDAyh9SDTuCz3YmynN8fgEs0qcrrLJflV5p045uG59U/0?wx_fmt=jpeg)

# cURL 严重漏洞已存在25年，影响300亿台设备

Ionut Arghire
Ionut Arghire

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**开源数据传输工具及库cURL本周修复了多达18个CVE漏洞（4个中危和14个低危），是单个curl版本中修复数量最多的一次。其中包括一个长达25年之久的严重漏洞 (CVE-2026-8932)，它最早于2001年3月22日随curl 7.7版本一同发布，是cURL有史以来报告的最古老的安全问题。这些漏洞是 Anthropic 公司 Mythos 于5月初发现一个curl漏洞后，社区共同努力发现的成果。**

CVE-2026-8932被描述为mTLS连接复用问题，可能导致身份验证绕过。该漏洞影响libcurl应用程序，而不影响cURL命令行工具。漏洞管理公司Aisle表示，该漏洞产生的原因在于“当客户端证书或私钥设置发生变化后，libcurl仍可能复用已有连接”。Aisle利用其AI平台识别出了curl和libcurl中的多个弱点，其中6个于今年获得了CVE编号，CVE-2026-8932是其中之一。其它识别出的漏洞包括凭据混淆（CVE-2026-8926）、双重释放（CVE-2026-8925）、释放后使用（CVE-2026-9080和CVE-2026-10536）以及主机验证不当（CVE-2026-9547）。

正如该公司所言，Mythos发现了一个curl漏洞，且只被曝存在少量安全问题，并不令人意外。Aisle表示：“curl对安全研究人员来说尤为值得关注：简单的漏洞早已被挖完，剩下的都是难以发现的问题：老旧协议路径、状态复用、回调行为、凭证选择，以及那些容易被遗忘的代码路径。”

目前有超过300亿台设备使用curl进行数据传输，包括服务器、手机和汽车，因此该漏洞对攻击者来说可能极具价值。不过，目前尚未有公开报告称 cURL 漏洞遭在野利用。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[【已复现】curl SOCKS5 堆溢出漏洞(CVE-2023-38545)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517841&idx=3&sn=293bea247f7876c2973e8d2f07c79be8&scene=21#wechat_redirect)

[注意！开源命令行工具Curl 中存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517813&idx=1&sn=d93b115c2f34ccedd19200ec3263c342&scene=21#wechat_redirect)

[掰开揉碎，讲讲这个已存在近24年的CURL漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513869&idx=1&sn=feae038c1dfbadfa3704dbab9000aed0&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/25-year-old-vulnerability-patched-in-curl/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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