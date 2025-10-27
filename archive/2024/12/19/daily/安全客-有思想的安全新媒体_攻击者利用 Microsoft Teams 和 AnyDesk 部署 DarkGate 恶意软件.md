---
title: 攻击者利用 Microsoft Teams 和 AnyDesk 部署 DarkGate 恶意软件
url: https://www.anquanke.com/post/id/302810
source: 安全客-有思想的安全新媒体
date: 2024-12-19
fetch_date: 2025-10-06T19:34:36.708459
---

# 攻击者利用 Microsoft Teams 和 AnyDesk 部署 DarkGate 恶意软件

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

# 攻击者利用 Microsoft Teams 和 AnyDesk 部署 DarkGate 恶意软件

阅读量**87975**

|评论**1**

发布时间 : 2024-12-18 10:56:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html>

译文仅供参考，具体内容表达以及含义原文为准。

一个新的社交工程活动利用微软团队（Microsoft Teams）作为一种方式，促进了一种名为 “黑暗之门”（DarkGate）的已知恶意软件的部署。

趋势科技研究人员 Catherine Loveria、Jovit Samaniego 和 Gabriel Nicoleta 表示：“攻击者通过 Microsoft Teams 通话使用社交工程技术冒充用户的客户端，远程访问他们的系统。”

“攻击者未能安装微软远程支持应用程序，但成功指示受害者下载了AnyDesk，这是一种常用的远程访问工具。”

正如网络安全公司 Rapid7 最近记录的那样，这次攻击涉及用 “成千上万封电子邮件 ”轰炸目标的电子邮件收件箱，之后，威胁者通过 Microsoft Teams 伪装成外部供应商的一名员工接近目标。

攻击者随后指示受害者在他们的系统上安装 AnyDesk，远程访问随后被滥用来传输多个有效载荷，包括一个凭证窃取程序和 DarkGate 恶意软件。

DarkGate 是一种远程访问木马（RAT），自 2018 年以来在野外被积极使用，后来发展成为一种恶意软件即服务（MaaS）产品，客户数量受到严格控制。其功能多种多样，包括窃取凭证、键盘记录、屏幕捕捉、录音和远程桌面。

对过去一年中各种 DarkGate 活动的分析表明，已知它是通过采用 AutoIt 和 AutoHotKey 脚本的两个不同攻击链传播的。在趋势科技检查的事件中，恶意软件是通过 AutoIt 脚本部署的。

虽然这次攻击在发生任何数据外渗活动之前就被阻止了，但这些发现表明威胁行为者正在使用一系列不同的初始访问路径来传播恶意软件。

建议各组织启用多因素身份验证 (MFA)，允许使用经批准的远程访问工具，阻止未经验证的应用程序，并彻底审查第三方技术支持提供商，以消除网络钓鱼风险。

随着各种网络钓鱼活动的激增，这些活动利用各种诱饵和伎俩诱骗受害者提供他们的数据。

* 以 YouTube 为中心的大规模活动：不良分子假冒流行品牌，通过电子邮件向内容创作者寻求潜在的促销、合作建议和营销合作，并敦促他们点击链接签署协议，最终导致 Lumma Stealer 的部署。YouTube 频道的电子邮件地址是通过解析器提取的。
* 利用含有二维码附件的 PDF 附件的网络钓鱼电子邮件开展网络钓鱼活动，扫描后会将用户引导至虚假的 Microsoft 365 登录页面以获取凭证。
* 网络钓鱼攻击利用与 Cloudflare 页面和 Workers 相关联的信任，建立模仿 Microsoft 365 登录页面和虚假 CAPTCHA 验证检查的虚假网站，以进行所谓的审查或下载文档。
* 使用 HTML 电子邮件附件进行网络钓鱼攻击，这些附件伪装成发票或人力资源政策等合法文档，但包含嵌入式 JavaScript 代码，用于执行恶意操作，如将用户重定向到钓鱼网站、获取凭据，以及以修复错误为借口欺骗用户运行任意命令（即 ClickFix）。
* 利用可信平台（如 Docusign、Adobe InDesign 和 Google Accelerated Mobile Pages (AMP)）让用户点击恶意链接以获取凭证的电子邮件钓鱼活动。
* 自称来自 Okta 支持团队的网络钓鱼企图，目的是获取用户的凭据并入侵组织的系统。
* 通过 WhatsApp 发布针对印度用户的网络钓鱼信息，指示接收者为安卓设备安装可窃取财务信息的恶意银行或实用程序。

据了解，威胁行为者还会迅速利用全球事件，将其纳入网络钓鱼活动，往往利用紧迫感和情绪反应来操纵受害者，说服他们采取意想不到的行动。这些活动还辅以特定事件关键词的域名注册。

Palo Alto Networks 第 42 部门表示：“包括体育锦标赛和产品发布会在内的高调全球活动，吸引了网络犯罪分子试图利用公众的兴趣。这些犯罪分子模仿官方网站注册欺骗性域名，销售假冒商品并提供欺诈性服务。”

“通过监控域名注册、文本模式、DNS异常和变更请求趋势等关键指标，安全团队可以及早识别和缓解威胁。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302810](/post/id/302810)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/attackers-exploit-microsoft-teams-and.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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