---
title: 谷歌安卓应用的RCE漏洞最高赏金45万美元
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519411&idx=2&sn=ce0a25d6937eabdc487272441bd3019d&chksm=ea94bdd9dde334cfe771b6fd011febb7616a978a4699a95ed386884efc11435c75b8f9cdf67a&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-07
fetch_date: 2025-10-06T17:18:11.998035
---

# 谷歌安卓应用的RCE漏洞最高赏金45万美元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTDfMJ0ibTuJxSUG2QK9icP3eopUVVODOqEuibghaIW8zw97DwlV4UrFlaswlyNVibztGhw9h9Tyq6Bgg/0?wx_fmt=jpeg)

# 谷歌安卓应用的RCE漏洞最高赏金45万美元

Zeljka Zorz

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**谷歌大幅增加了赏金猎人能通过从谷歌所开发和维护的安卓应用中找到漏洞能获得的赏金。**

谷歌信息安全工程师 Kristoffer Blasiak 指出，“我们对某些类别内的赏金额最高增加到原来的10倍（如第一级别应用中的远程任意代码执行漏洞的赏金从3万美元增加到30万美元）。”谷歌还准备为高质量漏洞报告支付更高赏金，助力移动漏洞奖励计划团队更快做出决策。

**赏金增多**

谷歌移动漏洞奖励计划在2023年5月推出，涵盖由谷歌及其下属公司（如Fitbit、Waymo、Waze等）所开发的安卓应用。

这些应用分为三个级别：

* 第1级包括 Google Play Services、Android Google Search App (AGSA)、Google Cloud 和 Gmail；
* 第2级包括与第1级应用、用户数据或谷歌服务交互的应用；
* 第3级包括不处理用户数据或不与谷歌服务交互的应用；

第1级别 app 中的漏洞如可导致任意代码执行且可远程触发、无需用户交互，则可发现该漏洞的赏金猎人可获得30万美元的奖励。如需用户交互（如跟踪链接），则赏金减半。Blasiak 表示，“我们还借此机会增加希望研究人员能够特别关注的类别的赏金，确保我们妥善地为最具影响力的报告提供奖励。其中的一个例子是数据盗取，我们大幅增加了该类别的奖励，但我们同时也确保给出数据盗取所能产生的不同类别的影响示例，从而有助于澄清所购买的数据如何影响最终的赏金额。”

如漏洞可导致攻击者窃取敏感信息的情况：如漏洞可遭远程利用且无需用户交互，则最高可获得赏金7.5万美元 ；如需用户交互，则最高可获得赏金3.75万美元。

第2级别和第3级别所涵盖的漏洞所获赏金更少。

谷歌还希望激励漏洞猎人能够提交质量上乘的报告，即附加补丁/缓解措施的报告、根因分析和清晰展现漏洞影响的报告，这些报告可获得1.5倍的赏金。该团队指出，“请知晓：你的报告是由安全工程师分类的，简短的PoC要比解释某个漏洞后果的视频更有价值。”

**激励研究员从谷歌开发的安卓应用中找到漏洞**

Blasiak 白哦是，这些变化是根据顶级漏洞猎人的反馈而做出的。一年前，谷歌就曾宣布为组合利用多个漏洞实现完全利用 Chrome 的漏洞研究员颁发大额奖励。

显然，谷歌已经了解并接受了匹兹堡大学和卡内基梅隆大学研究团队最近的漏洞奖励计划研究结果，“更高的奖励激励道德黑客付出更多努力，从而增加了他们首先发现漏洞的概率，同时降低了恶意黑客的成功概率。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[谷歌修复多个严重的安卓 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493998&idx=3&sn=8614c59ede5671d799158d2078af6150&chksm=ea94d804dde351124b3039831cfac241f421d6423a3390e1af029aff5d661bcee1ccaff1c82e&scene=21#wechat_redirect)

[谷歌安卓 RCE 漏洞可导致攻击者完全访问设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492938&idx=2&sn=8c4c7c9856627edfda57c44dfb0f8347&chksm=ea94d420dde35d36f2147d3e5c8a2964b3814cfcca376be8463dade83019f0c01409e9a48929&scene=21#wechat_redirect)

[谷歌修复安卓System 组件中的多个 RCE 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492664&idx=3&sn=1310ae593d8179254cf5df0bd8fa01e7&chksm=ea94d552dde35c44ddf4977687baa00be94ab6cf79100d0908c35a976cab6afbc5b814dce092&scene=21#wechat_redirect)

[安卓2020年1月更新发布40个补丁，含修复1个严重的 Media 框架 RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492094&idx=1&sn=93400a77d84bfec2fe9a84c9534e90a5&chksm=ea94d094dde359822b3e0a1df42c728490095c66a8e6a87b8984718f133ef1490a2273eb0a52&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisa-urges-software-devs-to-weed-out-path-traversal-vulnerabilities/

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