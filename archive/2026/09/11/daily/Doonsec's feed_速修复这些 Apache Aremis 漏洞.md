---
title: 速修复这些 Apache Aremis 漏洞
url: https://mp.weixin.qq.com/s/LIu2Lci38T6ThERDeN03SQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:42:19.359071
---

# 速修复这些 Apache Aremis 漏洞

# 速修复这些 Apache Aremis 漏洞

Do Son
Do Son

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

**Apache Artemis****的协议处理和核心身份验证机制受五个“重要”级别漏洞影响。这些****ActiveMQ Artemis****缺陷导致恶意人员窃取会话、暴露凭据并执行拒绝服务攻击。因此，管理员必须升级到****2.57.0****版本以保护消息代理。**

Apache Artemis 和 ActiveMQ Artemis 是企业应用程序的关键消息骨干。未经身份验证的攻击者可以利用这些 Apache Artemis 漏洞破坏关键通信。如威胁行动者获取管理凭据或窃取会话，就能获得对代理状态的未经授权控制。这种中断会导致依赖应用程序出现严重停机，并阻止用户访问关键服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUqa8uSBo56iby7JYakNicdZS7uzD93JPWHFeywGMoeUNbVe878TZAVxeCuYpJShpgKEttbdvwlnVB6aNgnMnhKdxhia6h0MUDRDE/640?wx_fmt=gif&from=appmsg)

**攻击如何运作**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXl3O0GichicdLCBk6KNP4z7xRqoRsWxb095TM6LaYd536s5ejsC3kCHVgt0iax0CkTUSHickNPmA8Ptxe8ATZrQcg7AsYfh7Jb9Jw/640?wx_fmt=gif&from=appmsg)

这些缺陷源于整个平台中身份验证检查缺失和不正确的协议处理。例如，攻击者通过发送 Openwire RemoveSubscriptionInfo 命令来利用 CVE-2026-67593。该操作会在连接身份验证阶段之前删除队列。

同时，CVE-2026-57967 针对的是 CORE 协议。公告称：“未经身份验证的远程攻击者可以构造一个 CORE 协议 SESSION\_REATTACH 数据包，窃取现有会话并假定继续执行先前已通过身份验证的会话。”同样，CVE-2026-49362 允许攻击者在未经身份验证的情况下创建任意持久队列。

此外，CVE-2026-49364 在初始连接握手期间暴露集群管理凭据。最后，CVE-2026-57822 涉及 Java 反序列化。已通过身份验证的用户发送特定管理请求以触发过度计算。该操作会占用处理线程并导致拒绝服务。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUibt7CCp7phkzZIP4uD9zKBVobx7YUibJgEPrmDRQaR3foVXrbaFfFpJZgb5NKrrrLpkw7JTia5GRicpGmiaxOopdkSA0JuIsO0bww/640?wx_fmt=gif&from=appmsg)

**受影响版本**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVvKqdXiak8kaHYp3WGPhWQ65ODmRRPN3wnmAwZVtdAYtv1aicmS5BeM4iaXqcibTBWDqlWDQQiabs3fs6Ol8rEnEJBC1sqjhkribloY/640?wx_fmt=gif&from=appmsg)

这些 ActiveMQ Artemis 缺陷影响广泛的部署版本。具体而言，它们影响 Apache Artemis 2.50.0 至 2.56.0 版本。它们还影响 Apache ActiveMQ Artemis 1.0.0 至 2.44.0 版本。虽然尚未核实确切的安装数量，但该软件广泛用于在企业网络中。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWzspXx9KdzEbbQQXqBM9s7n3FxVISomH9J6xeK8iapG5GqRygTQYRzLg0po3wBhDzjVDQwlhnicSFKEFFskIs9Tf7PpbVytk24c/640?wx_fmt=gif&from=appmsg)

**补丁和缓解步骤**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUhUdJLThetmcVuRBO0ia2rh1bwDT0traXCdj2YO2PxiaUkd7xibkiavzdlxEOE2HrTNlyK10BIGDtGbk2vUj81ibibTCd2J9icmjZCWs/640?wx_fmt=gif&from=appmsg)

目前，研究人员尚未确认任何在野主动利用。此外，这些漏洞不存在公开的概念验证漏洞利用。管理员必须立即部署官方补丁，升级到 2.57.0 版本可解决所有五个问题。用户可以访问官方下载页面保护系统安全。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[Apache HTTP/2 严重漏洞可导致 DoS 和 RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525945&idx=2&sn=6c90b2a2b1a68169a53e78b17473ff15&scene=21#wechat_redirect)

[Apache Tomcat 紧急修复多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525768&idx=1&sn=1c34f092d86b657532a27c79a93f83a3&scene=21#wechat_redirect)

[已存在13年的Apache ActiveMQ 严重漏洞可用于远程执行命令](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525686&idx=1&sn=51e7e391e06000c6fad494187241de39&scene=21#wechat_redirect)

[Apache Syncope 漏洞可用于劫持用户会话](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525048&idx=2&sn=58b797888d5027994282725ccb9f23de&scene=21#wechat_redirect)

[Apache Struts 2 严重 XXE 漏洞可用于窃取敏感数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524857&idx=1&sn=7d98b989a61c9b25103ccef5b0524560&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/apache-artemis-vulnerabilities/

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