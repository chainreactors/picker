---
title: CocoaPods 严重漏洞导致 iOS 和 macOS 应用易受供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519949&idx=2&sn=4951a0b220cf599191f950ae82909410&chksm=ea94bfa7dde336b19e411b9455b63b9d21ae84069ef0a118254f7f6b31c0ea710d0d2d333d1e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-03
fetch_date: 2025-10-06T17:43:22.474866
---

# CocoaPods 严重漏洞导致 iOS 和 macOS 应用易受供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMScDwDbicqqelIwhMSyOfp4V2t73QibDdu0rAOLiaRawI0oFpsrQaK6LKLszSJNN5I8UnqmPa7qlgR0Q/0?wx_fmt=jpeg)

# CocoaPods 严重漏洞导致 iOS 和 macOS 应用易受供应链攻击

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMScDwDbicqqelIwhMSyOfp4VDm49xdxhbzwgNyoVTD68ibAWxPXlzqdbkm95VoqFLUPhOjxvMyIsS1w/640?wx_fmt=gif&from=appmsg)

**Swift 和 Objective-C 的 Cocoa 项目的依赖管理器 CocoaPods 中存在三个漏洞，可用于发动软件供应链攻击，导致下游客户面临严重风险。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMScDwDbicqqelIwhMSyOfp4VDMvVfaVM5v24oIGwhjlYu1IVCYJLIPhcXcvoHahLGzqCcrVlYSlvrQ/640?wx_fmt=gif&from=appmsg)

以色列E.V.A Information Security公司的安全研究员 Reef Spektor 和 Eran Vaknin 在一份报告中提到，这些漏洞可导致“任何恶意人员获得数千个未声明pod 的所有权，并将恶意代码注入到很多最流行的iOS 和 macOS 应用程序中。”该公司指出，这些漏洞已由 CocoaPods 在2023年10月修复，并在当时重置了所有的用户会话。

其中一个漏洞是CVE-2024-38368（CVSS评分9.3），可导致攻击者滥用 “声明你的 Pods (Claim Your Pods)” 进程并控制包，从而篡改源代码并引入恶意变更。不过，它要求所有之前的维护人员已被删除。

该漏洞的根因可追溯至2014年，当时迁移到 Trunk 服务器导致数千个包拥有未知（或未声明的）所有人，使攻击者通过公开API声明 pod，CocoaPods 源代码 ("unclaimed-pods@cocoapods.org") 中的一个邮件地址就能接管控制。

第二个漏洞更为严重（CVE-2024-38366，CVSS评分10），攻击者可利用不安全的邮件验证工作流，在 Trunk 服务器上运行任意代码，之后用于操纵或替换这些包。

该服务中的第二个问题存在于邮件地址验证组件中（CVE-2024-38367，CVSS评分8.2），它诱骗收件人点击看似无害的验证链接，而实际上会将请求重新路由到受攻击者控制的域名，获得对开发者会话令牌的访问权限。更糟糕的是，可通过欺骗HTTP 标头即修改 X-Forwarded-Host 标头字段，升级为零点击账户接管攻击，并利用配置不当的邮件安全工具。

研究人员表示，“我们发现几乎每个pod的所有人在 Trunk 服务器上注册自己的组织机构邮件，使得他们易受零点击接管漏洞利用攻击。”

这并非 CocoaPods 首次被扫描到。2023年3月，Checkmarx 公司披露称，与依赖管理器 (“cdn2.cocoapods[.]org”) 存在关联的被弃用子域名可被攻击者通过 GitHub Pages 劫持，目的是托管其多个 payload。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[利用 CocoaPods 服务器中的一个 RCE 漏洞，投毒数百万款app](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503775&idx=3&sn=a01956f660295eda90f816f8b4a0b483&chksm=ea94fef5dde377e312d65574b4704b820710de0978ebf853152e6f475bd711a5c90f4e959f4c&scene=21#wechat_redirect)

[Rapid7：0day攻击和供应链攻陷剧增，MFA利用率仍较低](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519603&idx=1&sn=70cfaf8c8f867ef05e90b02ea49b69ae&chksm=ea94bc19dde3350fd636b698281e577e34e7510ecf18833876de77f3ad1d5564e797c26a5fe2&scene=21#wechat_redirect)

[AI Python 包中存在缺陷 “Llama Drama” ，威胁软件供应链](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519566&idx=1&sn=991956bfd062dfe52e9fe722b821d358&chksm=ea94bc24dde335320179ca3ef8f51d217570e92946c74792f58bd0cc3104290b3db59cfa67fc&scene=21#wechat_redirect)

[RSAC 2024观察：软件供应链安全进入AI+时代](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519497&idx=1&sn=3f531af375c16bd26e01ca94f96d2f6b&chksm=ea94bc63dde33575a6c7f4e47536c932046c465934273303f37535c57d30f3fe32e5335b2de5&scene=21#wechat_redirect)

[在线阅读版：《2023中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517225&idx=1&sn=8154b433ae2be87ccbae15bc0fb09a00&chksm=ea94b543dde33c55c168c44e830d62b03e9b34ca072871d10156273a3f282cab7ccc42b9b430&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/07/critical-flaws-in-cocoapods-expose-ios.html

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