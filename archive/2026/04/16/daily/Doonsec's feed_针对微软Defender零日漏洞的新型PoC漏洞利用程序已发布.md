---
title: 针对微软Defender零日漏洞的新型PoC漏洞利用程序已发布
url: https://mp.weixin.qq.com/s/OpJb8PcEQviqh54EuW8NpQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:38.191424
---

# 针对微软Defender零日漏洞的新型PoC漏洞利用程序已发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MV4AZdHM0rlLmgT5ibcgKjMzWfVW5vzerlRKxjcM2aTZcIdyB73zXvnt0jLHA22OIx5CNyB60tbLdmkErcIialiaKzH9aUXqzdKg/0?wx_fmt=jpeg)

# 针对微软Defender零日漏洞的新型PoC漏洞利用程序已发布

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一位化名为“Chaotic Eclipse”的安全研究人员公开发布了针对微软Defender漏洞的概念验证（PoC）攻击程序。

该漏洞利用程序于 2026 年 4 月 15 日发布，针对的是 CVE-2026-33825 中的一个缺陷，该漏洞此前已被修复。此次未经协调的发布凸显了独立安全研究人员与微软漏洞披露计划之间日益加剧的冲突。

这种性质的公开泄露大大缩短了安全团队在恶意行为者利用代码攻击系统之前保护系统的时间。

## **RedSun漏洞利用程序发布**

该研究人员将新发布的漏洞利用程序“RedSun”上传到了公共GitHub存储库。

此次泄露与同一人近期披露的漏洞模式一致，此前他还泄露过名为“BlueHammer”的拒绝服务攻击工具。Chaotic Eclipse 通过其个人博客上发布的 PGP 签名消息公布了 RedSun 代码。

他们将此次发布描述为对微软近期针对 CVE-2026-33825 的安全更新的直接回应。通过直接向公众提供原始代码，该研究人员完全绕过了标准的行业协议。

研究人员详细解释了他们为何选择公开漏洞利用程序，而不是公开与供应商合作。

Chaotic Eclipse 声称，他们最初曾尝试按照标准流程，向微软安全响应中心 (MSRC) 提交漏洞报告。但根据该博客文章，尽管 MSRC 完全意识到漏洞可能被公开的风险，却仍然驳回了这份初始报告。

该研究人员声称遭到该公司的严重虐待，并表示微软积极破坏他们的生计，并玩弄他们的投稿。

他们公开批评微软在协调漏洞披露问题上的官方立场，称微软安全响应中心（MSRC）的公开声明轻蔑且脱离现实。

这一事件与以往的争议类似，独立研究人员曾与大型科技公司就漏洞赏金评估和披露时间表发生冲突。

## **未来威胁及应对措施**

此次事件立即引发了依赖 Microsoft Defender 进行终端安全防护的企业安全团队的担忧。Chaotic Eclipse 明确威胁将在不久的将来发布更严重的漏洞。

该博客文章警告说，与微软持续不断的摩擦正迫使研究人员发布关键的远程代码执行 (RCE) 漏洞利用程序。

作者声明他们打算发布新的漏洞利用程序，以干扰微软未来的补丁发布。

各组织必须对这些无序投放保持警惕，并立即采取积极措施。安全团队应实施以下防御策略：

* 立即在所有企业环境中应用针对 CVE-2026-33825 的官方 Microsoft 补丁。
* 监控网络流量和端点检测系统，查找与 RedSun 和 BlueHammer GitHub 存储库相关的特征码。
* 持续审查安全日志，以发现与 Microsoft Defender 进程相关的异常活动。
* 保持严格的访问控制并划分网络，以限制任何即将发生的远程代码执行攻击的潜在影响。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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