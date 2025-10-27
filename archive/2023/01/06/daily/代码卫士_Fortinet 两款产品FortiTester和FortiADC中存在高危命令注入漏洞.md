---
title: Fortinet 两款产品FortiTester和FortiADC中存在高危命令注入漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515203&idx=1&sn=0154c72722b8b2c44432c3c779bc5ce6&chksm=ea948d29dde3043f88a8f390467e5fe9417ffdbb15210cc62b5ca63cb1bb7d11d80897439b47&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-06
fetch_date: 2025-10-04T03:10:11.862677
---

# Fortinet 两款产品FortiTester和FortiADC中存在高危命令注入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRWK42xqr5Pr25UUF1Xc5ficQVGBxMjiapeufkszGdj9JxVfKyRtIGKfTW0AibkuiaKqdX2pc1bBjdx4w/0?wx_fmt=jpeg)

# Fortinet 两款产品FortiTester和FortiADC中存在高危命令注入漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周，网络安全解决方案提供商Fortinet 发布了产品中多个漏洞的补丁，并将FortiADC中的高危命令注入漏洞告知客户。该漏洞的编号是CVE-2022-39947，位于FortiADC web接口中，可导致任意代码执行后果。**

Fortinet 公司解释称，“FortiADC中操作系统命令漏洞中使用的特殊元素中和不当，可导致能够访问 web GUI的认证攻击者通过特殊构造的HTTP请求执行越权代码或命令。”

Fortinet公司提到，该漏洞影响FortiADC 版本5.4.x、6.0.x、6.1.x、6.2.x和7.0.x，将在FortiADC 6.2.4和7.0.2中修复。

Fortinet 公司还发布了FortiTester 中多个高危命令注入漏洞的补丁。这些漏洞被统称为 CVE-2022-35845（CVSS评分7.6），是对特殊元素的中和不当问题，可导致在底层shell中执行任意命令。利用该漏洞要求认证。Fortinet 公司指出，该问题影响FortiTester 版本2.x.x、3.x.x、4.x.x、7.x 和7.1.0，已在FortiTester 版本3.9.2、4.2.1、7.1.1和7.2.0中修复。

本周，Fortinet 公司还修复了其它三个中危漏洞，它们是位于FortiManager 中的用户管理不正确问题，可导致FortiGate 中的无密码管理员后果；FortiPortal 中的输入中和不当漏洞，可导致XSS；以及FortiWeb中的CRLF序列中和不当导致任意标头注入欧国。

Fortinet 公司并未提到这些漏洞已遭利用。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Fortinet 紧急修复已遭利用的VPN漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514989&idx=1&sn=d69be3f378da5be4993977d510a35a5b&chksm=ea948a07dde303111a95aab98531af127bcaa9ad279aa46a8fbf4f7e56f0053a9bc6ba7c4ac8&scene=21#wechat_redirect)

[Fortinet 修复6个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514392&idx=2&sn=d3a167944c3d8a1d891c716450e26210&chksm=ea948872dde3016465bc0576d1de3d5f0be89e0a4cf7ef01370a82224cb557ef613a3252ccd8&scene=21#wechat_redirect)

[Fortinet：立即修复这个严重的认证绕过漏洞！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514120&idx=2&sn=e9b6c1a8e128a9eee70880b0fc3cce94&chksm=ea948962dde300745ee1435a5b05de3016d29440d127c2f0dad65ea6b5b80bc83b6a301afaec&scene=21#wechat_redirect)

[Fortinet 修复多个路径遍历漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512788&idx=3&sn=894340534673ba25a49c72eec950b0d7&chksm=ea9483bedde30aa8e9c0b3355eeee1ce56ec6cb1f2d55b60888cea9487bd8397fff4294a955d&scene=21#wechat_redirect)

[黑客利用老旧安全缺陷攻破数万未打补丁的 Fortinet VPN 设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507850&idx=3&sn=2ef6c8e24754e7f6c84db9a5eebc9841&chksm=ea94eee0dde367f6cc369d9e7480161d5b32ed4fd175215145390fd16c0d196639a57d4f0bbe&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/high-severity-command-injection-flaws-found-fortinets-fortitester-fortiadc

题图：Pexels License‍

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