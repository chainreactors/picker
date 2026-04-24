---
title: 微软紧急修复严重的 ASP.NET 漏洞
url: https://mp.weixin.qq.com/s/7GZgED4pCSwGFicuaQo5xA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:52:28.007668
---

# 微软紧急修复严重的 ASP.NET 漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXl58OYG2Nr3PegXkcKbichLV3qNmKVTo9wBfm42zQ88oBqQ9HuPMvPNbYEch4cenFkT5CQO4m8tL7bcfV0umNiaYCfkyJAI3aWQ/0?wx_fmt=jpeg)

# 微软紧急修复严重的 ASP.NET 漏洞

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**微软发布紧急更新，修复了一个严重的 ASP.NET Core 权限提升漏洞 CVE-2026-40372。该漏洞位于 ASP.NET Core Data Protection 加密 API 中，可导致未经身份认证的攻击者通过伪造身份认证 cookie，在受影响设备上获得系统权限。**

在本月补丁星期二期间，用户报告安装 .NET 10.0.6 更新后应用程序中出现解密失败问题后，微软发现该漏洞。微软在 .NET 10.0.7 的发布说明中表示：“Microsoft.AspNetCore.DataProtection 10.0.0 至 10.0.6 NuGet 包中存在一个回归问题，导致托管认证加密器在对负载的错误字节计算 HMAC 验证标签，并且在某些情况下会丢弃计算出的哈希值。在这些情况下，该认证漏洞可导致攻击者伪造能够通过 DataProtection 真实性检查的负载，并解密身份验证 cookie、防伪令牌、TempData、OIDC 状态等中先前受保护的负载。”

微软在周二发布的安全公告中进一步解释称：“如果攻击者在存在漏洞的时间窗口内，利用伪造的负载以特权用户身份通过身份认证，可能诱使应用程序向自己颁发合法签名的令牌（如会话刷新令牌、API 密钥、密码重置链接等）。这些令牌在升级到 10.0.7 后仍然有效，除非更换 DataProtection 密钥环。”该漏洞还可能使攻击者泄露文件和修改数据，但不会影响系统的可用性。

周二，微软高级项目经理 Rahul Bhandari 警告所有使用 ASP.NET Core Data Protection 的客户，尽快将 Microsoft.AspNetCore.DataProtection 包更新到 10.0.7，然后重部署，修复验证逻辑并确保任何伪造的负载都被自动拒绝。有关受影响平台、软件包及应用程序配置的更多信息，可参阅原始公告。

去年十月份，微软还修复了 Kestrel Web 服务器中的一个 HTTP 请求走私漏洞（CVE-2025-55315），它被评定为ASP.NET Core 中“有史以来最高”的严重漏洞。成功利用 CVE-2025-55315 可使经过身份认证的攻击者劫持其它用户的凭据、绕过前端安全控制或导致服务器崩溃。

本周一，微软发布了另一组带外更新，解决在安装 2026 年 4 月安全更新后影响 Windows Server 系统的问题。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[微软4月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525778&idx=2&sn=b5edef54c4ece70f1affe656616e58df&scene=21#wechat_redirect)

[微软3月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525382&idx=1&sn=a2fde96ec371ca6512bbfc25b9f18f99&scene=21#wechat_redirect)

[微软：AI已用于攻击的每个阶段](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525365&idx=2&sn=dff79e089be7ac2054e918366b567b52&scene=21#wechat_redirect)

[微软2月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525101&idx=2&sn=973a3ab33cfe6290521da6d90b4c743e&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-security-updates-for-critical-aspnet-flaw/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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