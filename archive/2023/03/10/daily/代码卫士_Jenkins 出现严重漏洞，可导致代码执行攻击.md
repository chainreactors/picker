---
title: Jenkins 出现严重漏洞，可导致代码执行攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=2&sn=559cb44fa0529b875f5361b1112c5b60&chksm=ea948fbcdde306aaba8058c93f2a95d0d723359a0d01dee3fa2e873d99d65d6a7d5d0c5bdae4&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-10
fetch_date: 2025-10-04T09:10:35.305672
---

# Jenkins 出现严重漏洞，可导致代码执行攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRMrrWLnahV80FeT4ZDEGsIkE6pOhk9s6gIibia1ric55DX7yHo4kEeAmFcjppGeQ257ialwMB6wHfjew/0?wx_fmt=jpeg)

# Jenkins 出现严重漏洞，可导致代码执行攻击

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**开源自动化服务器 Jenkins 中存在两个严重漏洞（CVE-2023-27898和CVE-2023-27905），可导致攻击者在目标系统上执行代码。**

这两个漏洞影响 Jenkins 服务器和Update Center，它们被Aqua公司统称为 ‘CorePlague"。Jenkins 2.319.2之前的版本均受影响。

Aqua公司在报告中指出，“利用这些漏洞可导致未认证攻击者在受害者Jenkins服务器上执行任意代码，有可能导致Jenkins服务器完全受陷。”这些漏洞是由Jenkins处理源自Update Center的可用插件方式不当造成的，因此可能导致威胁行动者上传具有恶意payload的插件，并触发跨站点脚本攻击。

报告还指出，“受害者在Jenkins服务器上打开‘可用插件管理器’时，就会触发XSS，从而导致攻击者在使用Script Console API的Jenkins Server上运行任意代码。”

由于XSS攻击也是存储型XSS攻击的一种，因此在无需安装插件甚至无需访问插件URL的情况下，也可触发该漏洞。令人担忧的是，这些漏洞也影响自托管的Jenkins服务器，甚至在无法从互联网中公开访问服务器的场景下也不例外，因为公开的Jenkins Update Center可“遭攻击者注入”。不过攻击的前提是，恶意插件与Jenkins服务器兼容且位于“可用插件管理器”页面的顶端。攻击者提到，可通过“上传描述中所内嵌的所有插件名称和流行关键字的插件”，或提交源自虚假实例的请求，人为地提高插件的下载次数来操纵。

研究人员在2023年1月24日将漏洞告知Jenkins 公司，后者已为 Update Center和服务器发布补丁。建议用户尽快将Jenkins服务器升级至最新可用版本。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Jenkins 披露插件中未修复的XSS、CSRF等18个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513380&idx=3&sn=643da5e5ad5ec30250e2a3e9dca17e51&chksm=ea94844edde30d581814ce1b634ebb01aa1bda2917e2a9fc451329302585db1df9aa7b51fd8d&scene=21#wechat_redirect)

[Jenkins 披露多个组件中的29个未修复0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512696&idx=1&sn=5cc055e6e0d20676ecdd7c4f69dbef58&chksm=ea948312dde30a04f59e7b9ce79f1435ebf6d7aca4b7f21aaa31c408a774f19337d54bf0fe68&scene=21#wechat_redirect)

[开源自动化服务器软件 Jenkins 被曝严重漏洞，可泄露敏感信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247494725&idx=1&sn=6bf29dab175c73db77b72934be87d9a0&chksm=ea94dd2fdde35439bd8c3b7485f574d8020d07f6614e4b0ab18aeb58270939e2f498b50612c0&scene=21#wechat_redirect)

[开源服务器 Jenkins 曝漏洞，可用于发动 DDoS 攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492309&idx=3&sn=59873a77a41d3216fa315e16d40dde39&chksm=ea94d3bfdde35aa94eb842b53fc793cfbb0512112c1624ac2c32062c7813a79371c62d95ac9f&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/03/jenkins-security-alert-new-security.html

题图：Pexels License

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