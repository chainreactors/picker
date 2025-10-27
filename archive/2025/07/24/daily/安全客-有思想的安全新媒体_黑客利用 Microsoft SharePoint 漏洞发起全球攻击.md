---
title: 黑客利用 Microsoft SharePoint 漏洞发起全球攻击
url: https://www.anquanke.com/post/id/310438
source: 安全客-有思想的安全新媒体
date: 2025-07-24
fetch_date: 2025-10-06T23:16:46.604880
---

# 黑客利用 Microsoft SharePoint 漏洞发起全球攻击

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

# 黑客利用 Microsoft SharePoint 漏洞发起全球攻击

阅读量**77718**

发布时间 : 2025-07-23 17:20:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 Deeba Ahmed，文章来源：hackread

原文地址：<https://hackread.com/hackers-exploit-microsoft-sharepoint-flaws-breaches/>

译文仅供参考，具体内容表达以及含义原文为准。

有关微软本地部署的 SharePoint 服务器正在遭受的网络攻击的更多细节已浮出水面，显示其影响范围远超最初预期。据 Hackread.com 昨日报道，微软就两个关键漏洞（**CVE-2025-53770 和 CVE-2025-53771**）发布紧急安全警告和更新补丁，这些漏洞可能被利用执行恶意代码。

目前，网络安全研究人员已确认攻击事件显著升级：全球已有约 100 家机构遭到成功入侵。此次广泛的漏洞利用活动已波及全球多地的政府、企业及其他组织。

受害者包括欧洲和中东的国家政府，以及美国政府机构，如美国教育部、佛罗里达州税务局和罗德岛州议会等。

此外，一家位于美国的医疗服务机构和一所东南亚的公立大学也成为攻击目标。在巴西、加拿大、印度尼西亚、西班牙、南非、瑞士和英国等国家，亦监测到攻击企图。

据悉，攻击者正利用“零日漏洞”进行攻击，这类漏洞在此前尚未公开披露，**攻击者可借此深度访问目标系统，甚至可能植入持久性后门**。CrowdStrike、Mandiant Consulting、Shadowserver Foundation 和 Eye Security 等多家网络安全公司目前正追踪多个参与此次攻击的黑客组织。

Shadowserver Foundation 于 2025 年 7 月 20 日发布预警称：“SharePoint CVE-2025-53770 漏洞事件警报！我们正与 @eyesecurity 和 @watchtowrcyber 合作，通知受影响单位。”该组织指出，目前每天约有 9300 个 SharePoint IP 地址暴露在互联网上（仅为暴露数量统计，不代表已评估漏洞风险）。

总部位于荷兰的 Eye Security 最早于上周五发现该漏洞被积极利用，并指出尽管微软已于 7 月初发布了初始修复补丁，但攻击者依然“找到绕过补丁的方法”实施入侵。CrowdStrike 也在 2025 年 7 月 18 日观察到活跃的漏洞利用行为，已在 160 多个客户环境中拦截了数百次攻击尝试。

![]()

据 CrowdStrike 发现，受感染系统的常见特征之一，是存在名为“**spinstall0.aspx**”的可疑文件。该文件通常通过 **PowerShell 命令**被写入服务器，攻击者借此窃取 IIS（Internet 信息服务）机器密钥。

**紧急行动呼吁**

所泄露的信息极为敏感，涉及包括用户名、密码及哈希码在内的登录凭据。由于 SharePoint 与 Microsoft Office、Teams、OneDrive 及 Outlook 等其他微软服务深度集成，一旦被攻陷，攻击者便可“打开整个网络的大门”，Palo Alto Networks 的 Michael Sikorski 表示。

尽管微软已于上周末发布了 SharePoint 2019 和 Subscription Edition 的安全补丁，但 SharePoint 2016 的补丁仍在开发中。各组织被强烈建议不仅要尽快应用已发布的补丁，还需轮换服务器机器密钥，并重启 IIS 服务，以实现完整的威胁缓解。

美国网络安全与基础设施安全局（CISA）于 2025 年 7 月 20 日发布了相关安全指引，建议在 SharePoint 环境中启用反恶意软件扫描接口（AMSI），并在所有 SharePoint 服务器上部署 Microsoft Defender 防病毒软件。如 AMSI 无法启用，则建议暂时断开受影响的对公网产品，直至官方缓解措施完全到位。

全球暴露于互联网的 SharePoint 服务器数量被搜索引擎 Shodan 估算超过 8000 台，进一步凸显出当前亟需加强整体安全防护。此次大规模漏洞利用事件也再次引发外界对微软网络安全机制的质疑。美国政府于 2024 年发布的报告中已明确提出，微软亟需对其安全文化进行改革。

Entrust 全球技术解决方案副总裁 Robert Hann 指出：“加密资产的窃取，正在成为新的‘网络钓鱼’。攻击者发现，相比暴力破解，窃取 API 密钥或机器身份等关键加密资产要容易得多。”

Robert 强调，要保护敏感数据，必须先清楚了解哪些系统和信息由哪些加密资产（如私钥、数字证书、加密算法）进行保护。“对于涉及敏感数据或合规要求的数据，利用硬件安全模块（HSM）尤为关键。”

本文翻译自hackread [原文链接](https://hackread.com/hackers-exploit-microsoft-sharepoint-flaws-breaches/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310438](/post/id/310438)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/hackers-exploit-microsoft-sharepoint-flaws-breaches/)

如若转载,请注明出处： <https://hackread.com/hackers-exploit-microsoft-sharepoint-flaws-breaches/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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