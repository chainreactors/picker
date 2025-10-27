---
title: 谷歌修复由苹果报送的严重 Chrome 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521342&idx=1&sn=355a1e1a938422e3437d8a957f360c7e&chksm=ea94a554dde32c42e130665c527ed8a177be5afa09da92ec4ea9eb9f45b2b85a56062bff40b2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-01
fetch_date: 2025-10-06T19:17:50.692383
---

# 谷歌修复由苹果报送的严重 Chrome 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT4FJiad3PZ1j4Hib390AC7WDWN0YN8o6dClWY9VL0hEK3asTibKY1xvqN7fdCfpr4pga0hhY5BbX5Iw/0?wx_fmt=jpeg)

# 谷歌修复由苹果报送的严重 Chrome 漏洞

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT4FJiad3PZ1j4Hib390AC7WD3vCSzNMuLOMyUPF0v2pnEmGqbZSabUyticPPboVY6dTJJDf1CmOOCQA/640?wx_fmt=gif&from=appmsg)

**本周二，谷歌和 Mozilla 宣布为 Chrome 和 Firefox web 浏览器发布安全更新，其中一些漏洞为严重级别。**

谷歌发布 Chrome 130，修复了两个漏洞。其中一个漏洞是CVE-2024-10487，是位于 WebGPU 标准跨平台实现Dawn 中的一个严重的界外写问题。该漏洞由苹果公司的安全工程和架构 (SEAR) 团队在一周前报送。对 WebGPU 图形API 的不同实现也用于Firefox 和 Safari，但目前尚不清楚后者是否也受该漏洞影响。

虽然目前尚不清楚CVE-2024-10487的利用场景，但通常来讲利用界外写问题可导致任意代码执行后果。谷歌并未提到任何在野利用信息。

第二个漏洞是CVE-2024-10488，它是位于 WebRTC 中的高危释放后使用漏洞。谷歌尚未确定这两个漏洞的赏金金额。

周二，Mozilla 发布 Firefox 132 和 Thunderbird 132，均修复了11个相同的漏洞，其中两个是高危级别。其中一个漏洞是许可泄露漏洞CVE-2024-10458，另外一个漏洞是可导致可利用崩溃的UAF漏洞CVE-2024-10459。余下漏洞是中低危漏洞，如遭利用可导致欺骗、XSS攻击、数据泄露、DoS 条件和任意代码执行后果。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[谷歌：三星0day漏洞已遭活跃利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521255&idx=3&sn=a3d253a523be442f0e1f72789ba75fb2&chksm=ea94a28ddde32b9b8de1966962ff8445b3814e03944529cc5ba0b88db8ff3ee88e958cd066e8&scene=21#wechat_redirect)

[谷歌：2023年70%的已遭利用漏洞是0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521136&idx=1&sn=8dae0f9e90eb71b97f2e0b1158775cb8&chksm=ea94a21adde32b0cd92f1996cd9d86287351e84ca7c503267ffd83e79c363ced14eec5b768e0&scene=21#wechat_redirect)

[谷歌单个Chrome漏洞的最高赏金超25万美元](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520627&idx=1&sn=e98afd2bb604a7bc41cadce2c53f2ab3&chksm=ea94a019dde3290fe4adbad1106c57776b38ae4dd608564a94bb4be8c9881f87478eac1c79a0&scene=21#wechat_redirect)

[谷歌修复已遭利用的安卓内核0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520345&idx=2&sn=e480c7108b41c03d874e5bd6bc1c39bf&chksm=ea94a133dde3282563f26f94c29d3b95b05a082b1c377d83aa2ef24ce6e26794bc98899319d7&scene=21#wechat_redirect)

[研究员披露谷歌云平台上的 ConfusedFunction 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520228&idx=2&sn=e2baa4f853063d34474bdd1973b4b156&chksm=ea94be8edde33798101d04ab50a6066bd659de102e44e7f9e8a8a8d63f9a91f86499e33bffbd&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/google-patches-critical-chrome-vulnerability-reported-by-apple/

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