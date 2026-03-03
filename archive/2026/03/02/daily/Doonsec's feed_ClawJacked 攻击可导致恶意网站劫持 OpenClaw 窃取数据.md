---
title: ClawJacked 攻击可导致恶意网站劫持 OpenClaw 窃取数据
url: https://mp.weixin.qq.com/s/AUHl68W6qMjjaOasi9tTZA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:08:42.146918
---

# ClawJacked 攻击可导致恶意网站劫持 OpenClaw 窃取数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUCHibAUTJo4p9xprMKnriaVztYZeiaJGhQKQTzicAw466ejM9w7YEWicNianibSO0wlu3ibhvngXkTd4Y6d2GDcnQiaHfwvqClAnvbewtQ/0?wx_fmt=jpeg)

# ClawJacked 攻击可导致恶意网站劫持 OpenClaw 窃取数据

Lawrence Abrams
Lawrence Abrams

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Oasis****公司的安全研究员披露了热门AI代理 OpenClaw 中的一个高危漏洞，可导致恶意网站悄悄暴力访问并控制在本地运行的实例。OpenClaw 已在2026年2月26日发布2026.2.26版本予以修复。**

OpenClaw 是一款自托管AI平台，最近因可使AI智能体自动发送信息、执行命令和管理多个平台的任务而备受关注。该漏洞由OpenClaw网关服务默认绑定到本地主机并暴露了一个WebSocket接口所导致。

由于浏览器的跨域策略不会阻止与本地主机的WebSocket连接，当OpenClaw用户访问恶意网站时，该网站便可利用JavaScript静默打开一个通往本地网关的连接并尝试进行身份验证，且不会触发任何警告。尽管OpenClaw设置了速率限制以防止暴力破解攻击，但回环地址（127.0.0.1）默认不受此限制，避免误将本地CLI会话锁定。

研究人员发现，他们可以以每秒数百次的速度暴力破解OpenClaw的管理密码，而这些失败的尝试既不会被限速，也不会被记录。一旦猜中正确密码，攻击者便可悄无声息地注册成为受信任设备，因为无需用户确认，网关就会自动批准来自本地主机的设备配对。研究人员解释道：“在我们的实验室测试中，仅通过浏览器JavaScript，我们就实现了每秒数百次密码猜测的持续速率。照此速度，一秒钟之内就能试完一个常见密码列表，而一个大型字典库也只需要几分钟。人为设置的密码根本无法抵挡。”

获得经过身份验证的会话和管理员权限后，攻击者现在可以直接与AI平台交互，转储凭据、列出已连接的节点、窃取凭据以及读取应用程序日志，从而导致攻击者指示智能体在消息历史记录中搜索敏感信息，从已连接的设备中窃取文件，或在配对的节点上执行任意Shell命令，最终可仅从一个浏览器标签页就能导致整个工作站被攻陷。研究人员还演示了如何通过OpenClaw漏洞窃取敏感数据。

研究人员向OpenClaw报告了该问题，并提供了技术细节和概念验证代码，该漏洞在披露后24小时内即被修复。修复方案加强了WebSocket的安全检查，并增加了额外的保护措施，以防止攻击者滥用本地主机的回环连接进行暴力破解登录或劫持会话——即使这些连接被配置为不受速率限制的豁免。运行OpenClaw的组织机构和开发者应立即更新至2026.2.26或更高版本，以防止其安装的实例被劫持。

随着OpenClaw的广泛流行，安全研究人员一直专注于识别针对该平台的漏洞和攻击。已有威胁行为者被指滥用"ClawHub" OpenClaw技能仓库，推广恶意技能，部署信息窃取型恶意软件，或诱骗用户在其设备上运行恶意命令。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[AI 编程助手 Cline CLI 2.3.0遭篡改，悄悄安装 OpenClaw](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525250&idx=2&sn=0896fff8eb0f9f9e2369a299930ff6c4&scene=21#wechat_redirect)

[AI 助手OpenClaw 易遭一次点击 RCE 攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525048&idx=1&sn=cdf70fc2422b01678c8735e83fc62b3b&scene=21#wechat_redirect)

[Apache Syncope 漏洞可用于劫持用户会话](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525048&idx=2&sn=58b797888d5027994282725ccb9f23de&scene=21#wechat_redirect)

[SmarterMail 认证绕过新漏洞被用于劫持管理员账号](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524955&idx=1&sn=34fffd85602bd5f7fa445177131ff399&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/clawjacked-attack-let-malicious-websites-hijack-openclaw-to-steal-data/

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