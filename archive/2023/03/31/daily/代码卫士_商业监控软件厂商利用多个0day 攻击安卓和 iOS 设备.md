---
title: 商业监控软件厂商利用多个0day 攻击安卓和 iOS 设备
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516096&idx=1&sn=1b7557f7a2683f3f9e215004fb1e4922&chksm=ea948eaadde307bc2c035530c28e9af2f550d85dccbde7413bdd71c3c755aeaea56acc4d9dc4&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-31
fetch_date: 2025-10-04T11:15:26.677103
---

# 商业监控软件厂商利用多个0day 攻击安卓和 iOS 设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibO6DpzuJwQ82u5TEDWofgsJJLCg5DRp1rdd2U8tVZOtZf4CiazO39ic5Q/0?wx_fmt=jpeg)

# 商业监控软件厂商利用多个0day 攻击安卓和 iOS 设备

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibXqBhdw2GVBJzfJov21nNwdTICSnaT2B8a0Jley7gByJAXg7ZypPeqQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQic1chVVVoYoMiatrqFxJo7ibRxuOIwscjgDA8rFZCIwVNoAbV3rqdRYbjqMLzkHicEudB8OeMTFMPbA/640?wx_fmt=gif)

**谷歌威胁分析团队 (TAG) 披露称，商业监控软件厂商利用去年修复的多个0day 漏洞攻击安卓和 iOS 设备。**

研究人员表示，这两起攻击活动影响范围有限且针对性强，利用补丁发布和部署之间的时间差发动攻击。报告指出，“这些厂商可快速传播危险的黑客工具，使政府能够开发无法自研的能力。虽然按照国家或国际法律来说，使用监控技术可能是合法的，但这些技术通常被政府用于攻击异见人士、记者、人权工作人员以及反对党政客。”

在这两起攻击活动中，第一起发生在2022年11月，涉及通过SMS信息向位于意大利、马来西亚和哈萨克斯坦的用户发送短链接。点击这些URL后，用户会被重定向到托管着安卓或 iOS 利用的网页，之后他们才会被重定向至合法的新闻或运输追踪网站。iOS 利用链利用多个漏洞如CVE-2022-42856（当时是0day）、CVE-2021-30900和一个指针认证代码绕过，在可疑设备上安装 .IPA 文件。安卓利用链由CVE-2022-3723、CVE-2022-4135（当时是0day）和CVE-2022-38181 组成，用于传播未指定 payload。虽然影响 Mali GPU 内核驱动的提权漏洞CVE-2022-38181已由 Arm 公司在2022年8月修复，但目前尚不清楚攻击者是否在补丁发布前就已经拥有该漏洞的 exploit。另外值得注意的是，点击该链接并在三星 Internet 浏览器中打开的安卓用户会被通过意图重定向的方法重定向到 Chrome。

第二起攻击发生在2022年12月，由多个0day和nday 组成，用于攻击三星 Internet Browser 的最新版本，exploit 被以一次性链接的方式通过SMS发送到位于阿联酋的设备上。网页类似于西班牙监控软件公司 Variston IT所使用的网页，它最终植入能够从聊天应用和浏览器应用中收割数据的基于C++的恶意工具包中。这些遭利用的漏洞包括 CVE-2022-4262、CVE-2022-3038、CVE-2022-22706、CVE-2023-0266以及CVE-2023-26083。该利用链被指由 Variston 的客户或合作伙伴所使用。

这两起攻击活动和目标的性质情况尚不明朗。

就在几天前，美国政府发布行政令，限制联邦政府机构使用存在国家安全风险的商业监控软件。

研究人员指出，“这些攻击活动说明商业监控软件行业继续发展。即使规模更小的监控厂商也可以访问0day，厂商秘密囤积并利用 0day 为互联网产生严重风险。这些攻击活动还表明，监控厂商之间共享 exploit 和技术，使危险的黑客工具得以传播。”

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[美国总统签署行政令，限制联邦政府机构使用商业监控软件](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516076&idx=1&sn=20640a149cf1ceff69f69fd521a4003b&chksm=ea948ec6dde307d072ef5cd6de84dfffc330f978056b8f08168c1d064f37cd0dd4ec78b401f9&scene=21#wechat_redirect)

[Chromium 漏洞可用于绕过安卓设备上的安全特性](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515762&idx=2&sn=d0544e7c040ded8d269077260cf6dd17&chksm=ea948f18dde3060e3aeb1b186df35346212a396dafcdc58377d0aad3d492d5483edf1b72a7cb&scene=21#wechat_redirect)

[监控软件厂商勾结互联网服务提供商感染iOS和安卓用户](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512563&idx=2&sn=6582e83c3243a6d3bf6629a491add967&chksm=ea948099dde3098ff28bbb7d7f6e5634d3d0f29556ffb7aa7ec4f4088d596796e590016efe43&scene=21#wechat_redirect)

[还挖吗？0day 买卖商 Zerodium 更新价格表：安卓0day 价格首超 iOS，最高250万美元](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247490754&idx=1&sn=5258dc9e9128b7f1d7d3fe20a92b0106&chksm=ea972da8dde0a4be303b100076391e1bb3a4de49195ddf000451fc3e9d8d14a31d74244f8266&scene=21#wechat_redirect)

[强大的间谍软件 FinSpy 被指攻击缅甸 iOS 和安卓用户](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247490401&idx=3&sn=54ed242a9a74bf1e3f3e052e969efd7b&chksm=ea972a0bdde0a31dea0368a5f4c8e0723c409037d2e0cbb94c157019823243ea8d154f6c3609&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/03/spyware-vendors-caught-exploiting-zero.html

题图：Pixabay License

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