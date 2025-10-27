---
title: Opera 浏览器修复严重漏洞，可泄露用户信息
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521342&idx=2&sn=f31a6cd39b33c9b2bd7cd10c19169e81&chksm=ea94a554dde32c4280fdfcb682ecbd81e1802f47e0b691b8784f9c448c03289cbcd65c02d0fb&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-01
fetch_date: 2025-10-06T19:17:51.488487
---

# Opera 浏览器修复严重漏洞，可泄露用户信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT4FJiad3PZ1j4Hib390AC7WDe8PB9TywOYDRKzWMjhLVIWsuez0NgfWNBxP9w6M5tYTRt2pia6N9nyw/0?wx_fmt=jpeg)

# Opera 浏览器修复严重漏洞，可泄露用户信息

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT4FJiad3PZ1j4Hib390AC7WD3vCSzNMuLOMyUPF0v2pnEmGqbZSabUyticPPboVY6dTJJDf1CmOOCQA/640?wx_fmt=gif&from=appmsg)

**Opera web 浏览器修复了一个漏洞，可导致恶意扩展获得对私密API的完全越权访问权限。**

Guardio Labs 提到，该攻击名为CrossBarking，可截屏、修改浏览器设备以及账户劫持。为演示该问题，该公司表示已在 Chrome Web Store设法发布看似无害的浏览器扩展，而一旦将其安装在 Opera 上即可利用该漏洞，使其成为跨浏览器存储 (cross-browser-store) 攻击的实例。

Guardio Labs 的负责人 Nati Tal 在报告中提到，“该案例不仅凸显了生产力与安全性之间的持久冲突，还让我们窥见现代威胁行动者所使用的技术。”Opera 在2024年9月24日修复了该漏洞。但该漏洞并未 Opera 修复的第一个漏洞。

今年1月初，一个名为 “MyFlaw” 的漏洞利用合法特性 My Flow 在底层操作系统上执行任意文件。最新发生的攻击说明多个由 Opera 所有的公开可访问子域对内嵌在该浏览器中的私有 API 拥有提升后的访问权限。这些域名用于支持Opera的特定特性如 Opera Wallet、Pinboard等以及用于内部开发中的特性。

其中一些域的名称中还包含一些第三方域名，如下：

* crypto-corner.op-test.net
* op-test.net
* gxc.gg
* opera.atlassian.net
* pinboard.opera.com
* instagram.com
* yandex.com

虽然沙箱逃逸确保浏览器上下文与余下的操作系统隔离，但 Guardio 的研究结果显示，浏览器扩展中的内容脚本也可被用于将恶意 JavaScript 注入权限过多的域名中并访问私有API。Tal 解释称，“内容脚本确实拥有访问 DOM（文档对象模型）的权限，包括通过增加一些元素对其进行突然变更。”

攻击者通过该访问权限能够截屏所有打开的标签，提取会话 cookie 劫持账户，甚至修改浏览器的 DoH 设置，通过攻击者控制的 DNS 服务器解析域。之后当受害者尝试访问银行或社交媒体站点时，就会发动中间人攻击，将受害者重定向到恶意站点。

该恶意扩展可在任何扩展分类中发布，包括谷歌 Chrome Web Store 在内。用户可从中下载并将其添加到自己的浏览器中，实际上是触发了该攻击。不过，执行攻击要求具有在任何网页上运行 JavaScript 的权限，尤其是能够访问私有API的域的权限。

恶意浏览器扩展一直都在渗透官方商店，更不用说对数据收集实践缺乏透明度的合法扩展，本次发现强调了在安装这些扩展前保持警惕的重要性。Tal表示，“浏览器扩展掌握着巨大能力，不管这种能力能造成或好或坏的结果。因此策略执行者必须对它们进行严密监控。当前的审计模式不起作用，我们建议通过更多的人工和持续分析方式，在批准后也对扩展活动进行监控，进行支持。另外，为开发者账户执行真实身份验证至关重要，因此只通过一封免费邮件和预付款信用卡进行注册是不够的。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Opera 文件共享特性中存在RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518689&idx=2&sn=f6a9ea96b68970bcf3bac320b9b70aeb&chksm=ea94b88bdde3319d56d7ec033b60e8a4c709203172307dc7eb3aafefc99a51291f6403a28549&scene=21#wechat_redirect)

[开发人员：Opera浏览器的VPN等同于代理服务器](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485772&idx=5&sn=8f47bc6d1d8ec16c5a37571894827af8&chksm=ea973826dde0b130ee7a6e7aa52d4cdc5c47b9353f39c7cebbe7776bb0a72f1f9e4c3477ddb9&scene=21#wechat_redirect)

[Crowdfense 出价3000万美元收购安卓、iOS和浏览器0day利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519250&idx=1&sn=a9eb759176bc25d080dd038567016edc&chksm=ea94bd78dde3346e8571088ffb3e1104df63785be22cebfc4b338fab213de9a5a83aec96d089&scene=21#wechat_redirect)

[Chrome 漏洞多：web 浏览器还安全吗？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516843&idx=2&sn=08d47901f423ad544f407dead0344eef&chksm=ea94b3c1dde33ad7879cb6a504aa623576e7d749f80f139f04f047b1e28a6e6d949bea885041&scene=21#wechat_redirect)

[谷歌决定不修复这个Chromium浏览器XSS漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514671&idx=1&sn=61fcdf93bfac81f15a8003972cd54cfd&chksm=ea948b45dde3025344d546821417c7d84002e20f4ce07d501debfcd2eb37b63ca343e65307ca&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/opera-browser-fixes-big-security-hole.html

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