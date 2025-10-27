---
title: 16 款 Chrome 浏览器扩展程序遭黑客攻击，导致 60 多万用户数据被盗
url: https://www.anquanke.com/post/id/303104
source: 安全客-有思想的安全新媒体
date: 2024-12-31
fetch_date: 2025-10-06T19:38:02.259967
---

# 16 款 Chrome 浏览器扩展程序遭黑客攻击，导致 60 多万用户数据被盗

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

# 16 款 Chrome 浏览器扩展程序遭黑客攻击，导致 60 多万用户数据被盗

阅读量**92032**

发布时间 : 2024-12-30 10:39:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html>

译文仅供参考，具体内容表达以及含义原文为准。

一个新的攻击活动以已知的 Chrome 浏览器扩展为目标，导致至少 16 个扩展被入侵，超过 60 万用户的数据被暴露和凭证被盗。

这次攻击通过网络钓鱼活动锁定了 Chrome 网上商城的浏览器扩展发布者，并利用他们的访问权限在合法扩展中插入恶意代码，以窃取 cookie 和用户访问令牌。

第一家被曝光的公司是网络安全公司 Cyberhaven。

12 月 27 日，Cyberhaven 披露，一名威胁行为者入侵了其浏览器扩展，并注入恶意代码与位于 cyberhavenext[.]pro 域的外部命令与控制 (C&C) 服务器通信，下载额外的配置文件并外泄用户数据。

专门从事浏览器扩展安全的 LayerX Security 公司首席执行官 Or Eshed 说：“浏览器扩展是网络安全的软肋。尽管我们倾向于认为浏览器扩展是无害的，但实际上，它们经常被授予大量权限，以获取敏感的用户信息，如 cookie、访问令牌、身份信息等。”

Eshed说：“许多企业甚至不知道自己的终端上安装了哪些扩展程序，也不知道它们的暴露程度。”

Cyberhaven 遭到入侵的消息一经传出，很快就发现了其他同样遭到入侵并与同一 C&C 服务器通信的扩展程序。

SaaS 安全公司 Nudge Security 的首席技术官杰米-布拉斯科（Jamie Blasco）发现，还有一些域名解析到了用于 Cyberhaven 入侵的 C&C 服务器的相同 IP 地址。

目前怀疑被入侵的其他浏览器扩展包括：

* 人工智能助手 – Chrome 浏览器的 ChatGPT 和 Gemini
* 巴德人工智能聊天扩展
* 带有 OpenAI 的 GPT 4 摘要
* 用于 Chrome 浏览器的 Search Copilot AI 助手
* TinaMInd AI 助手
* Wayin AI
* VPNCity
* Internxt VPN
* Vindoz Flex 视频录制器
* VidHelper 视频下载器
* 书签图标更换器
* Castorus
* Uvoice
* 阅读模式
* 鹦鹉说话
* Primus

这些被入侵的扩展程序表明，Cyberhaven 并非一次性目标，而是针对合法浏览器扩展程序的大规模攻击活动的一部分。

对被入侵的 Cyberhaven 的分析表明，恶意代码的目标是 Facebook 账户，特别是 Facebook 商业账户的身份数据和访问令牌：

被入侵的 Cyberhaven 浏览器扩展收集的用户数据（来源：Cyberhaven）

Cyberhaven 表示，恶意版本的浏览器扩展在上线约 24 小时后被删除。其他一些被曝光的扩展也已经更新或从 Chrome 网上商城删除。

然而，Or Eshed 表示，该扩展从 Chrome 浏览器商店删除并不意味着暴露已经结束。他说：“只要被入侵的扩展版本仍然存在于终端上，黑客就仍然可以访问它并渗出数据。”

安全研究人员正在继续寻找更多被暴露的扩展程序，但这次攻击活动的复杂程度和范围已经提高了许多组织保护其浏览器扩展程序安全的要求。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303104](/post/id/303104)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [恶意活动](/tag/%E6%81%B6%E6%84%8F%E6%B4%BB%E5%8A%A8)

**+1**6赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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