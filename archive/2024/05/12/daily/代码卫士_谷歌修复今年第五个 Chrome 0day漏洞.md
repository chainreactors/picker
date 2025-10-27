---
title: 谷歌修复今年第五个 Chrome 0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519462&idx=1&sn=1f7824cfd17d3489bc4ba1b37c5d974c&chksm=ea94bd8cdde3349a09b38fe57ced58ecc0d6aa9cd8270a10e3ef522071c83b0a7ae0fc2e14a6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-12
fetch_date: 2025-10-06T17:16:36.403613
---

# 谷歌修复今年第五个 Chrome 0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSkp2YNGDLVoDIYxbia6Ld7oOKQnXduFRQtVYQOUVUPkSsXJnVPPMxzHZP7LzFQYl6VYTggZfaibysA/0?wx_fmt=jpeg)

# 谷歌修复今年第五个 Chrome 0day漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**谷歌发布 Chrome 安全更新，修复了今年以来遭利用的第5个 0day 漏洞 (CVE-2024-4671)。**

该高危漏洞是位于 Visuals 组件中的“释放后使用”漏洞，负责处理渲染和在浏览器上展示内容。该漏洞由一名匿名研究人员发现并报送，谷歌表示可能已遭活跃利用。谷歌在安全公告中表示，“谷歌发现 CVE-2024-4671遭在野利用。”

当程序在区域完成合法操作后，在指针所指向的内存已被释放但仍然继续使用该指针时，就会发生释放后使用漏洞。因为所释放的内存可能包含不同的数据或被其它软件或组件使用，因此访问该内存可能导致数据泄露、代码执行或崩溃。

谷歌在124.0.6367.201/.202（Mac/Windows）和124.0.6367.201 (Linux) 的发布修复了该漏洞，更新将在数天或数周时间内推出。

对于“Extended Stable”渠道的用户，修复方案将在 124.0.6367.201（Mac和 Windows）中发布，将在后续推出。

Chrome 会自动更新安全更新，不过用户可确认是否运行最新版本。

这一漏洞是今年Chrome修复的第五个已遭利用漏洞，而在前五个中有三个是在2024年3月 Pwn2Own温哥华大赛中发现的。其它四个漏洞如下：

* CVE-2024-0519：Chrome V8 JavaScript 引擎中存在一个高危界外内存访问漏洞，可导致远程攻击者通过特殊构造的 HTML 页面利用堆损坏，从而导致敏感信息遭越权访问。
* CVE-2024-2887：WebAssembly (Wasm) 标准中存在一个高危的类型混淆漏洞，可导致攻击者利用构造的HTML页面实现远程代码执行后果。
* CVE-2024-2886：web应用使用的WebCodecs API中存在一个释放后使用漏洞，可导致远程攻击者通过构造的HTML页面执行任意读写，导致远程代码执行后果。
* CVE-2024-3159：Chrome V8 JavaScript 引擎中存在一个高危的界外读漏洞。远程攻击者可通过特殊构造的HTML页面访问所分配内存缓冲区之外的数据，导致堆损坏，从而导致敏感信息遭提取。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[谷歌修复 Pwn2Own 2024大赛发现的两个 Chrome 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519170&idx=1&sn=31612ff9461ff59184a818b76f04c198&chksm=ea94baa8dde333be86a1b2054ea40407dfa5a45d469b948ac55085e5f64e7872f7e2007c90ad&scene=21#wechat_redirect)

[谷歌修复2024年首个已遭利用的 Chrome 0day 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518705&idx=2&sn=1f6ee90c31f7b70d13390d0a735fe85f&chksm=ea94b89bdde3318da0dc7cd16e5e35198256a22c9c7f0dfa9132e438f6a90fa78fc85e7a63bf&scene=21#wechat_redirect)

[CISA：注意 Chrome 和 Excel 解析库中已遭利用的开源漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518582&idx=2&sn=3e7fcf93d7c3d8fa193fcb72ed6c2347&chksm=ea94b81cdde3310af6e572040db0f7c2aba6bf5314cdb417d0ad4e7fffa194153e99860228a1&scene=21#wechat_redirect)

[谷歌紧急修复今年第8个已遭利用的 Chrome 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518459&idx=1&sn=16639910e34f9b7b38277934cf352d7e&chksm=ea94b991dde330870c970cec3c63ccbdb8634f61116a675b4e1ec25c90e9fc4ae7bd5fd02a04&scene=21#wechat_redirect)

[谷歌紧急修复已遭利用的 Chrome 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517626&idx=1&sn=516906d0d9c95466942c198e8b3644eb&chksm=ea94b4d0dde33dc68afa3a330f73b5e599c28832120edd5bd8f61ef250cf8d2ea50d208b5591&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/google-fixes-fifth-chrome-zero-day-vulnerability-exploited-in-attacks-in-2024/

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