---
title: 谷歌修复已遭利用的两个安卓 0day 漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521406&idx=1&sn=af981c3476e81115ffa11866a0bb7b7d&chksm=ea94a514dde32c02776e9a8a0d78022cfa4b713f7c32259d90a550950b10f2b9692a01826316&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-07
fetch_date: 2025-10-06T19:18:32.197772
---

# 谷歌修复已遭利用的两个安卓 0day 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQVmpD50IhTBGmu5ZtFZ0vDkUicdmrXnGJXX70b3mYBvf0ys6ichrEJzqs8oZt8cmWJdqfL6PVTK2MA/0?wx_fmt=jpeg)

# 谷歌修复已遭利用的两个安卓 0day 漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**谷歌在十一月补丁更新中修复了两个已遭活跃利用的安卓 0day，共计修复51个漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQVmpD50IhTBGmu5ZtFZ0vD90fom0T4XQxgfHwmlarbn4crR8ddxvY7GqWCjpFr3H4PmqeicU49p2A/640?wx_fmt=png&from=appmsg)

这两个漏洞是CVE-2024-43047和CVE-2024-43093，已被标记为遭有限的针对性攻击。CVE-2024-43047是位于安卓内核中闭源高通组件中的一个高危释放后使用漏洞，可用于提升权限。该漏洞由高通在2024年10月早些时候首次披露，表示它存在于 Digital Signal Processor (DSP) 服务中。

CVE-2024-43093也是一个高危的提权漏洞，影响安卓 Framework 组件和 Google Play 系统更新，尤其是 Documents UI。谷歌并未披露该漏洞的发现者信息。

虽然谷歌并未分享这些漏洞遭利用的方式，但 Amnesty International 是CVE-2024-43047的发现方，这表明该漏洞用于针对性监控攻击中。

在余下的49个漏洞中，只有CVE-2024-38408被列为严重级别，也影响高通的专有组件。

本月修复的这些漏洞影响安卓12至15之间的版本，其中一些漏洞仅影响其中的一些特定版本。

谷歌每个月都会发布两个补丁级别，本月发布的是11月1日（2024-11-01 补丁级别）和11月5日（2024-11-05补丁级别）。第一个级别修复了17个严重的安卓漏洞，而第二个补丁级别除此以外还修复了特定厂商（高通、联发科等）的漏洞，即34个。

用户可到“设置＞系统＞软件更新＞系统更新”或者“设置＞安全和隐私＞系统和更新＞安全更新”应用最新更新。应用更新需重启设备。虽然安卓11和更早版本已不再受支持，但可通过 Google Play 系统更新接收遭活跃利用漏洞的安全更新。仍然运行这些老旧发布的设备应当更新为更新机型或者使用第三方安卓发布集成最新的安全修复方案。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[谷歌：三星0day漏洞已遭活跃利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521255&idx=3&sn=a3d253a523be442f0e1f72789ba75fb2&chksm=ea94a28ddde32b9b8de1966962ff8445b3814e03944529cc5ba0b88db8ff3ee88e958cd066e8&scene=21#wechat_redirect)

[谷歌：2023年70%的已遭利用漏洞是0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521136&idx=1&sn=8dae0f9e90eb71b97f2e0b1158775cb8&chksm=ea94a21adde32b0cd92f1996cd9d86287351e84ca7c503267ffd83e79c363ced14eec5b768e0&scene=21#wechat_redirect)

[谷歌修复今年第10个已遭利用0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520605&idx=1&sn=943de838e9f963febbf06e2dc05dfbba&chksm=ea94a037dde32921bb888a382fcc01e0e960aa5da6886b69fdf2684bfcae4490cf02d45828e5&scene=21#wechat_redirect)

[谷歌修复已遭利用的安卓内核0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520345&idx=2&sn=e480c7108b41c03d874e5bd6bc1c39bf&chksm=ea94a133dde3282563f26f94c29d3b95b05a082b1c377d83aa2ef24ce6e26794bc98899319d7&scene=21#wechat_redirect)

[谷歌修复已遭利用的安卓 0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517584&idx=1&sn=37b84a3349271c0f40eb59108b6ebf14&chksm=ea94b4fadde33decfc9df5392f6bb398a7c9f557bfde7dc94564b2459d97d2285e8da38936db&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/google-fixes-two-android-zero-days-used-in-targeted-attacks/

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