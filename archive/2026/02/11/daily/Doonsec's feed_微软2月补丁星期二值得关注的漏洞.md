---
title: 微软2月补丁星期二值得关注的漏洞
url: https://mp.weixin.qq.com/s/i5FZNLdBCd7G9dKQ3diutA
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:19:47.648566
---

# 微软2月补丁星期二值得关注的漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfVsMkKCx5X7UCAia8TvegvClXOTwybFE9D7kOVPNnriaqFauLgpv5nCXbtrHqdacaNRupFSvboeG5BAo8K3OCiaZsDHywibeJhcAlk/0?wx_fmt=jpeg)

# 微软2月补丁星期二值得关注的漏洞

综合编译
综合编译

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**微软发布2026年2月补丁星期二，共修复58个漏洞，其中包含6个已遭活跃利用的 0day 漏洞（3个已公开披露）。**

具体如下：

* 25个提权漏洞
* 5个安全特性绕过漏洞
* 12个远程代码执行漏洞
* 6个信息泄露漏洞
* 3个拒绝服务漏洞
* 7个欺骗漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfX4x1dfMB179UG5pFFcRoA4chxuAG0DfL1RtX9icJMv4qAen36de8Bkbyib8EPiaRNmqMNcA9Q5Y2HQ853WLNP2JG19NTjJUEOXE8/640?wx_fmt=gif&from=appmsg)

**6个已遭活跃利用的 0day 漏洞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfURYtp7sOHfxicXCynHiaqyt7iac0CGgDEfuA0cRR4waUYqNctH9fqhywiaXScBruLuuXqBhZO7xXST6Ph5OKwwKDuQ6jKsFDzuam8/640?wx_fmt=gif&from=appmsg)

**CVE-2026-21510****是Windows Shell 安全特性绕过漏洞，也可归类为代码执行漏洞。**攻击者可绕过 Windows SmartScreen 和 Windows Shell 安全提示，在目标系统上执行代码。 漏洞已列为公开已知，但微软并未透露更多信息。由于客户需要点击链接或快捷文件，因此需要用户交互，但一次点击就实现代码执行的漏洞仍然少见。

**CVE-2026-21513****是位于 Internet Explorer 中的安全特性绕过漏洞。**该漏洞和前面提到的 Shell 漏洞类似，因为它也需要用户交互但可导致代码执行后果。该绕过漏洞可启动IE浏览器，用户应尽快测试并部署补丁。

**CVE-2026-21514****是微软 Word 安全特性绕过漏洞。**该漏洞也需要用户打开一份 Word 文档，但仅需如此便可绕过 COM/OLE 控制的防护措施。幸运的是预览面板此处并非攻击向量，但用户经常会打开通过邮件接收到的很多文档。如果COM/OLE控制遭攻击则可导致代码执行后果。该漏洞也已被列为公开已知，因此用户需尽快测试和部署补丁。

**CVE-2026-21519****是位于Desktop Windows 管理器中的提权漏洞。**和上个月披露的另外一个DWM 漏洞一样，该漏洞可导致攻击者以系统权限运行代码。这类漏洞通常和代码执行漏洞结合利用，可导致系统遭接管。和往常一样，微软并未说明利用的影响范围。

**CVE-2026-21525****是位于 Windows Remote Access Connection 管理器中的拒绝服务漏洞。**多数空指针解引用漏洞可导致应用或服务崩溃，但目前尚不清楚相关服务是否会自动重启。

**CVE-2026-21533****是位于 Windows Remote Desktop Services 中的提权漏洞。**该漏洞是一个本地漏洞，可导致攻击者以系统权限运行代码。值得关注的是，微软将“权限管理不当”列为该漏洞的根因。如系统正在运行 Remote Desktop Services，则可能成为攻击者在第一次攻陷后实现横向移动的目标。用户应立即测试并部署相关补丁。

在这六个0day漏洞中，CVE-2026-21513、CVE-2026-21510和CVE-2026-21514已被公开披露。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[微软2026年1月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524868&idx=1&sn=511dcdb0c6fcd3cd07ef7783b225bcf4&scene=21#wechat_redirect)

[微软12月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524622&idx=2&sn=ba8c3120218ed455901938344a91aa4f&scene=21#wechat_redirect)

[微软2025年11月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524369&idx=2&sn=07fedd121d307d4b3867834ea9b25395&scene=21#wechat_redirect)

[微软十月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524187&idx=2&sn=2160856486a6416a175e6542e8ea1394&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/microsoft/microsoft-february-2026-patch-tuesday-fixes-6-zero-days-58-flaws/

https://www.zerodayinitiative.com/blog/2026/2/10/the-february-2026-security-update-review

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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