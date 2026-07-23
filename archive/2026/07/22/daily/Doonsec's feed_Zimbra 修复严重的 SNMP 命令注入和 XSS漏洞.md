---
title: Zimbra 修复严重的 SNMP 命令注入和 XSS漏洞
url: https://mp.weixin.qq.com/s/LMbgRdFqa4CxKR3xveDXtA
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:45.355157
---

# Zimbra 修复严重的 SNMP 命令注入和 XSS漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfUDRRDrJZFWoJy67TEwW0JGy3RYG0Pv4F6Fek3JmRc1hSPV1r682iaX8VyOk4H1icQMWM3b48qugILKwufqLoCGhNtPYdam8EIF0/0?wx_fmt=jpeg)

# Zimbra 修复严重的 SNMP 命令注入和 XSS漏洞

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Zimbra****修复了多个严重漏洞，其中包括位于简单网络管理协议（****SNMP****）监控组件中的一个命令注入漏洞。**

Zimbra 10.1.20共修复了九个安全漏洞。其中最为严重的是当 SNMP 通知启用时，SNMP 监控组件中的命令注入漏洞。另外，该厂商还修复了位于 Classic Web Client 中的四个XSS漏洞：

* 一个存储型XSS漏洞，在特定条件下可导致恶意附件文件名执行脚本。
* 一个 XSS 漏洞，在特定条件下，特殊构造的字段可能执行恶意脚本。
* 一个 XSS 漏洞，特殊构造的字段可能执行恶意脚本。
* 一个 XSS 漏洞，渲染时特殊构造的附件可能执行恶意脚本。

另外，该公司还发布了针对邮件转发限制绕过漏洞（CVE-2026-50055）的修复方案，该漏洞可能导致已认证用户在启用转发限制的情况下泄露邮件内容。该漏洞由Rapid7 安全研究员 Jonah Burgess 发现并报送。

该公司未透露更多具体细节，并表示“按照行业最佳实践，针对安全漏洞修复的信息披露受到限制”。

此次发布距离 Zimbra 修补 Classic Web Client 中一个可导致任意代码执行的严重存储型 XSS 漏洞仅过去一周多。尽管这些漏洞并未标记为遭活跃利用，但过去该邮件软件中的 XSS 漏洞屡次被不法分子利用，因此客户应安装更新，保障环境安全。

开源卫士试用地址：https://oss.qianxin.com/

代码卫士试用地址：https://sast.qianxin.com/

---

**推荐阅读**

[Zimbra：速修复这个严重的 Web Client XSS 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526606&idx=1&sn=98ad31e009af96d9536be560cb9f7fa3&scene=21#wechat_redirect)

[Zimbra 紧急修复 Chat Proxy 配置中的严重SSRF漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524221&idx=2&sn=098a25797ac4273cffca0263a429835e&scene=21#wechat_redirect)

[Zimbra 紧急提醒手动修复已遭利用的0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517057&idx=1&sn=3cc4f03b1925ae57509bdbf2be1dd327&scene=21#wechat_redirect)

[Fortra 访问管理器漏洞可导致远程命令注入攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526330&idx=2&sn=634ff7aee7d1db205f90e279a8c74f64&scene=21#wechat_redirect)

[W3 Total Cache 插件存在严重的命令注入漏洞，百万网站易受RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524451&idx=2&sn=40767e9bab88232789546a1dcf703529&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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