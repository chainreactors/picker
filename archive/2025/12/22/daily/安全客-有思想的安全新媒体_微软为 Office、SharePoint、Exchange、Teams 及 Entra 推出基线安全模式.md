---
title: 微软为 Office、SharePoint、Exchange、Teams 及 Entra 推出基线安全模式
url: https://www.anquanke.com/post/id/313926
source: 安全客-有思想的安全新媒体
date: 2025-12-22
fetch_date: 2025-12-23T03:23:46.813304
---

# 微软为 Office、SharePoint、Exchange、Teams 及 Entra 推出基线安全模式

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 微软为 Office、SharePoint、Exchange、Teams 及 Entra 推出基线安全模式

阅读量**13885**

发布时间 : 2025-12-22 16:30:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/microsoft-baseline-security-mode/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软已开始为 Microsoft 365 租户部署 **基线安全模式（Baseline Security Mode）**—— 这是 M365 管理中心内的一个全新控制面板，可集中管理 Office、SharePoint、Exchange、Teams 以及 Entra 的**推荐安全配置**。

该可选功能于 2025 年 Ignite 大会上发布，能够帮助管理员快速评估漏洞、运行影响报告，并且应用基于风险的安全强化配置，同时**不会对用户造成即时干扰**。

截至 2025 年 12 月，该功能已在部分租户的「组织设置 > 安全与隐私」选项中上线，计划于 2026 年 1 月下旬在全球范围内完成全面推送。

基线安全模式会在三个核心领域强制执行 **18 至 20 项安全策略**，这些策略的制定参考了微软的威胁情报，以及微软响应中心过去二十年积累的数据。

1. **身份验证策略（共 12 项）**：阻止基础身份验证（basic auth）、Exchange Web 服务（EWS）、IDCRL 等传统协议，同时要求管理员使用 FIDO2 或通行密钥（passkeys），配置**抗钓鱼多因素身份验证（MFA）**
2. **文件保护策略**：限制高风险操作，例如通过不安全的 HTTP/FTP 协议打开文档、在受保护视图外使用 ActiveX、DDE 或旧版文件格式，同时会禁用存在安全漏洞的工具（比如将于 2026 年停用的 Microsoft Publisher）

该功能的公开预览版与正式版已于 2025 年 11 月中旬推出，针对 GCC、DoD 以及 GCCH 云环境的分阶段部署将于 2026 年 3 月完成。

拥有安全管理员或全局管理员角色的用户可直接启用该功能：

* 选择「自动应用默认策略」，可启用 7 项低影响的安全控制
* 选择「生成报告」，可对其余策略进行模拟运行，并且在 24 小时内查看基于审计的影响数据

  在更改获得批准前，租户不会受到任何干扰，同时可通过进度追踪查看「存在风险」或「符合标准」的状态。

这种「默认安全」的模式，能够解决常见的配置错误问题，填补在**凭证填充攻击、钓鱼攻击、供应链攻击**中被攻击者利用的安全漏洞。

通过简化多服务的安全配置流程，该功能可帮助企业为「安全未来计划（Secure Future Initiative）」应对 AI 驱动的威胁做好准备，微软还计划在未来将该功能扩展至 Purview、Intune 以及 Azure。目前已启用该功能的租户，将在勒索软件与高级持续性威胁（APT）攻击日益增多的环境中，获得**主动防御的优势**。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/microsoft-baseline-security-mode/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313926](/post/id/313926)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/microsoft-baseline-security-mode/)

如若转载,请注明出处： <https://cybersecuritynews.com/microsoft-baseline-security-mode/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **840**

* 粉丝
* **6**

### TA的文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34

### 相关文章

* ##### [电视中的 “狼”：规模达 180 万的 Kimwolf 僵尸网络流量超谷歌，称霸物联网领域](/post/id/313933)

  2025-12-22 16:32:27
* ##### [“脚本麻雀” 组织利用自动化技术生成并发送攻击邮件](/post/id/313954)

  2025-12-22 16:32:15
* ##### [黑客窃取数百万 PornHub 用户数据用于敲诈勒索](/post/id/313929)

  2025-12-22 16:31:50
* ##### [黑客发起定向钓鱼攻击，HubSpot 用户成攻击目标](/post/id/313948)

  2025-12-22 16:31:30
* ##### [微软发布紧急带外更新修复影响 IIS 站点的 MSMQ 漏洞](/post/id/313944)

  2025-12-22 16:30:34
* ##### [人工智能超级应用横空出世：OpenAI 推出 ChatGPT 应用目录，剑指数字生活核心入口](/post/id/313938)

  2025-12-22 16:29:53
* ##### [Exim 恶意记录漏洞：失败补丁与 SQL 注入如何引发严重堆溢出漏洞](/post/id/313923)

  2025-12-22 16:29:19

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)