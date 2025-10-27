---
title: GFI KerioControl 防火墙存在严重的RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522044&idx=1&sn=71bbcad32c9a0753d8385256ee5dad03&chksm=ea94a796dde32e80febb13e46990720e4748e375842d7d932e99d76c82cb55e561bf2219c17c&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-14
fetch_date: 2025-10-06T20:11:00.047653
---

# GFI KerioControl 防火墙存在严重的RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTicSxCiaH3vW2G3Ga7NqIWC1gE8syHQL48LEURKYIJtKZicbic4HOmMraic5Rdp0Fbpz352rdBcJsTqAg/0?wx_fmt=jpeg)

# GFI KerioControl 防火墙存在严重的RCE漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**威胁行动者们正在利用最近披露的 GFI KerioControl 防火墙中的一个漏洞 (CVE-2024-52875)，如成功利用则可实现远程代码执行 (RCE)。**

该漏洞是指回车换行（CRFL）攻击，可为HTTP响应截断攻击做铺垫，从而造成跨站脚本 (XSS) 缺陷。成功利用该一次点击RCE漏洞可导致攻击者通过引入回车和换行字符，将恶意输入注入HTTP响应头。

研究员 Egidio Romano 在2024年11月初发现并报送该漏洞，它影响 KeriioControl 9.2.5至9.4.5版本。

这些HTTP 响应截断漏洞存在于如下 URI路径中：

* /nonauth/addCertException.cs
* /nonauth/guestConfirm.cs
* /nonauth/expiration.cs

Romano 表示，“通过GET参数’dest’ 传递到这些页面的用户输入在被用于生成 302 HTTP 响应中的’Location’ HTTP 标头时未得到正确清理。具体而言，该应用并未正确过滤/删除换行符，从而可被用于执行HTTP响应截断攻击，进而导致攻击者执行反射型XSS攻击以及其它攻击。”

GFI 已在2024年12月19日发布版本9.4.5 Patch 1修复该漏洞。目前网络已存在相关 PoC 利用。具体而言，攻击者可构造一个恶意URL，管理员用户点击该URL导致托管在受攻击者控制的服务器上的 PoC 被执行，之后攻击者通过固件升级功能上传恶意 .img 文件，从而获得该防火墙的root 访问权限。

威胁情报公司 GreyNoise 在2024年12月28日报道了针对该漏洞的利用尝试。Censys表示，存在超过2.38万个暴露到互联网的GFI KerioControl 实例。多数服务器位于伊朗、乌兹别克斯坦、意大利、德国、美国、捷克、白俄罗斯、乌克兰、俄罗斯和巴西。

目前尚不清楚这些漏洞利用攻击的性质。建议 KerioControl 用户尽快采取措施保护实例安全，缓解潜在威胁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[速更新！Sophos 热修复严重的防火墙漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521868&idx=1&sn=62d6c6882cbe7ca4516d3b679eea7dfa&scene=21#wechat_redirect)

[超2.5万SonicaWall VPN 防火墙易受严重漏洞影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521836&idx=1&sn=1ac593b2544b8e1e86da611a669fe6f3&scene=21#wechat_redirect)

[Palo Alto 防火墙 0day 由低级开发错误引发](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521617&idx=2&sn=0e9ac32a3223e727cd6cd99460e0387e&scene=21#wechat_redirect)

[Palo Alto 修复多个严重的防火墙漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=1&sn=2987012f618a751eabf08e620add0615&scene=21#wechat_redirect)

[Palo Alto：注意！PAN-OS 防火墙 0day 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=1&sn=86e226003b5da9dd0d6867f4b45fcb1a&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/01/microsoft-sues-hacking-group-exploiting.html

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