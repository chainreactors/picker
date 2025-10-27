---
title: Mozilla 修复已遭利用的 Firefox 0day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521019&idx=1&sn=9271b20273e3b193c059558ab4844fcf&chksm=ea94a391dde32a87f79666c661628c4452d6cdc35a07001450db6ed6c017dd177937fd6328ed&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-11
fetch_date: 2025-10-06T18:52:38.096419
---

# Mozilla 修复已遭利用的 Firefox 0day漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSAsjnjia0h6rTzh5oDdsH9vicqrCUlM3e7KZ9qvrezETSKr3lBdpCG5DPpc0ayW5ic0mk2ypUcib5uVw/0?wx_fmt=jpeg)

# Mozilla 修复已遭利用的 Firefox 0day漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Mozilla 发布紧急安全更新，修复了 Firefox 浏览器中的一个严重的释放后使用漏洞 (CVE-2024-9680)，目前该漏洞已遭利用。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSAsjnjia0h6rTzh5oDdsH9vf0WibkPfqYxJGHw5Tu0pG6PT1lBNysZPfVppZ8KFvaAeIZvTlGLoJ3A/640?wx_fmt=gif&from=appmsg)

该漏洞由 ESET 公司的研究员 Damien Schaeffer发现，是位于 Animation 时间线中的一个释放后使用 (UAF) 漏洞。当被释放的内存仍由程序所使用时就会发生这类漏洞，可导致恶意人员将恶意数据添加到内存区域，进行代码执行操作。Animation 时间线是 Firefox Web Animation API 的组成部分，用于控制和同步网页上的动画。

安全公告提到，“攻击者能够通过利用 Animation 时间线中的UAF漏洞，在内容流程中实现代码执行。我们已收到关于该漏洞遭在野利用的报告。”该漏洞影响最新版 Firefox（标准发布）和扩展支持发布 (ESR)。

如下版本已修复这些漏洞，建议用户立即升级：

* Firefox 131.0.2
* Firefox ESR 115.16.1
* Firefox ESR 128.3.1

鉴于CVE-2024-9680已遭活跃利用，且遭攻击的人员情况尚不明确，因此用户应立即升级至最新版本。用户可启动火狐浏览器，去往“设置->帮助->关于Firefox”，更新应会自动启动。需要重启程序才能应用这些变更。

Mozilla 和ESET 公司尚未给出更多详情。

3月22日，Mozilla 公司发布安全更新，修复CVE-2024-29943和CVE-2024-29944。它们均由Manfred Paul 在2024温哥华 Pwn2Own大赛上发现和演示。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Mozilla 修复Pwn2Own大赛发现的两个 Firefox 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519154&idx=1&sn=3f4209efe9a510274abec479b51dcceb&chksm=ea94bad8dde333cec265a5c93f4ed89b687c3a2301fd4d5045252f76ea8505a6aa3b125f9070&scene=21#wechat_redirect)

[Mozilla 修复Firefox 漏洞，可导致RCE和沙箱逃逸](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518467&idx=2&sn=a4b556d25e18fde4859318143fe831f9&chksm=ea94b869dde3317f0c3e37352a2db057bc26f539dfef7de56f39049b1a8ae269888c76c12e48&scene=21#wechat_redirect)

[Mozilla 修复Firefox 浏览器的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515956&idx=2&sn=7870f9607adf1541eef5be5402a82ab4&chksm=ea948e5edde307489a6b2a77b80ba248729a3d0dbfd20a6b65ee00d181f4b422bc09fa95eb1c&scene=21#wechat_redirect)
[Firefox 97.0.2 修复两个已遭利用的0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510779&idx=2&sn=ebffc30f51572f1abd513f92b810858b&chksm=ea949b91dde31287dee367059f7db5e2dd338e600e25a7139b08463e0b1acc74d939bf9baf0c&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/mozilla-fixes-firefox-zero-day-actively-exploited-in-attacks/

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