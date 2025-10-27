---
title: 微软 MFA 中存在AuthQuake 漏洞，可导致无限次暴力攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521773&idx=1&sn=3e980835ea6ecc3e1562c951bb038730&chksm=ea94a487dde32d91d33e375aa8b72490a1daf1a3640f08c77409be3a66062af25a407b909384&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-13
fetch_date: 2025-10-06T19:38:39.724773
---

# 微软 MFA 中存在AuthQuake 漏洞，可导致无限次暴力攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQaYHjeLoEv3R4T7PI8tFRoInwj9Rh97jHb2ZgUef7ZxmHnnADiclL0KeRibu4aobucJPw4aPqn7zPw/0?wx_fmt=jpeg)

# 微软 MFA 中存在AuthQuake 漏洞，可导致无限次暴力攻击

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**作者：****Ravie Lakshmanan**

**编译：代码卫士**

**网络安全研究员在微软的多因素认证 (MFA) 实现中发现了一个严重漏洞，可导致攻击者轻易绕过防御措施，越权访问受害者账户。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQaYHjeLoEv3R4T7PI8tFRoFaLuscYbbvpwRXczVlBGxJ40tiaRM3iawxic54cvj0icN2xk5yiaSbQVvFA/640?wx_fmt=gif&from=appmsg)

Oasis 安全公司的研究人员 Elad Luz 和 Tal Hason 在一份报告中提到，“绕过很简单：大概需要一小时左右执行，无需用户交互，也无需生成任何通知或向账户持有者提供任何告警信息。”该漏洞被称为“AuthQuake（认证地震）”，已由微软在2024年10月修复。

虽然微软支持多种通过MFA的用户认证方式，但其中一种方法涉及在提供凭据后，从一款认证工具app中输入一个六位数代码。一次单独的会话允许最多10次的失败尝试。

从本质上而言，该漏洞与在提供和验证这些一次性代码过程中缺乏速率限制以及时间间隔延长有关，因此可导致恶意人员快速触发新会话并枚举所有可能的代码组合，但甚至不会提醒受害者登录尝试失败。

值得注意的是，这类代码与时间有关，也被称为“基于时间的一次性密码（TOTPs）”，即将当前时间作为随机性来源生成密码。另外，这些代码的有效时间仅为30秒。研究人员提到，“然而，由于验证器与用户之间存在可能的时间差和延迟，因此验证器会被推荐接受更大的代码窗口期。简言之，这意味着一个TOTP代码的有效时间可能超过30秒。”

而对于微软而言，该代码的有效期可长达3分钟，因此可导致攻击者有机会利用延长的时间窗口，同时触发更多的暴力攻击进行破解。研究人员提到，“引入速率限制并确保得到正确执行至关重要。速率限制可能还不够，后续出现尝试失败应处罚账户锁定。”

微软随后执行了更严格的速率限制并在多次尝试失败后被触发。研究人员也表示新的速率限制持续了大概半天的时间。

Keeper Security 公司的首席信息安全官 James Scobey 在一份声明中提到，“最近从微软MFA中发现 AuthQuake 漏洞提醒我们，安全不仅仅是关于MFA部署，它必须获得正确配置。虽然MFA无疑是一种强大的防御措施，但其有效性取决于关键设置如速率限制用于阻止暴力尝试，而用户通知用于失败的登录尝试。这些特性并非可选项，而是为了增强可见性，从而使用户能够提前发现可疑活动并进行快速响应。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Rapid7：0day攻击和供应链攻陷剧增，MFA利用率仍较低](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519603&idx=1&sn=70cfaf8c8f867ef05e90b02ea49b69ae&scene=21#wechat_redirect)

[微软十二月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521758&idx=3&sn=65f54ac400f184b0f2f9f4ec9c298658&scene=21#wechat_redirect)

[ProxyToken：微软 Exchange 服务器中的认证绕过新漏洞，可窃取用户邮件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507548&idx=1&sn=8bb0ef890eeea9a16bf623e46f1cc905&scene=21#wechat_redirect)

[微软强制 Azure AD 管理员账户启用多因素认证机制](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247487462&idx=2&sn=a4b76c222fc71b6471a1bd0365e8a1eb&scene=21#wechat_redirect)

[微软发布带外更新，紧急修复 Kerberos 认证问题](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247497950&idx=3&sn=da87daff20810c5e2db4c1739a91798e&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/microsoft-mfa-authquake-flaw-enabled.html

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