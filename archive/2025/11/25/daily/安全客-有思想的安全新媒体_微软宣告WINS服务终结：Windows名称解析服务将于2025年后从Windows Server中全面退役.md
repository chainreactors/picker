---
title: 微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役
url: https://www.anquanke.com/post/id/313348
source: 安全客-有思想的安全新媒体
date: 2025-11-25
fetch_date: 2025-11-26T03:15:21.967161
---

# 微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役

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

# 微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役

阅读量**25005**

发布时间 : 2025-11-25 17:46:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/wins-is-dead-microsoft-to-fully-retire-wins-name-resolution-from-windows-server-post-2025/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

微软通常会从 Windows SKU 中淘汰某些功能或组件，原因通常包括安全隐患、使用率下降或出现更优替代方案。现在，**WINS 名称解析服务** 将被完全且永久弃用。

WINS（Windows Internet Name Service）于 1994 年随 Windows NT 3.5 首次推出。随着时间推移，其用户群大幅减少，因为现代网络不再依赖 WINS 进行名称解析。

如今的互联网基础设施主要依赖 **域名系统（DNS）**，这促使越来越多的企业完全放弃 WINS。微软在 Windows Server 2022 发布时宣布弃用 WINS，现在又发布博客概述该服务的长期前景。

由于该服务已过时，从 Windows Server 2022 开始被弃用；**Windows Server 2025 仍将支持 WINS，但这将是最后一个支持该服务的版本**。在此之后，WINS 将从 Windows Server 中彻底移除。

根据产品的固定生命周期，未来的 Windows Server 版本将不再包含 WINS，但现有 WINS 部署将继续获得支持，直至 **2034 年 11 月**。此后，微软将停止提供所有安全更新和错误修复。

实际上，WINS 已进入仅维护状态：微软不再开发新功能，仅提供基本支持。其固定生命周期与 Windows Server 2025 一致，这意味着 WINS 和 Windows Server 2025 都将在 2034 年 11 月达到支持终止日期。

微软认为，给予企业十年的提前通知将帮助他们及时完成从 WINS 到 DNS 的迁移。该公司还强调了 DNS 的优势：**符合现代标准、与当代软件兼容、安全性更强**。

为规划有效的 DNS 过渡，微软建议组织：

1. 审计依赖关系
2. 现代化或淘汰依赖 WINS 的遗留应用
3. 避免临时解决方法
4. 采用可扩展的 DNS 解决方案

一旦 WINS 从 Windows Server 中移除，以下组件将不再可用：

1. WINS 服务器角色及相关二进制文件
2. WINS Microsoft 管理控制台 snap-in
3. WINS 自动化 API 和相关管理接口

本文翻译自securityonline [原文链接](https://securityonline.info/wins-is-dead-microsoft-to-fully-retire-wins-name-resolution-from-windows-server-post-2025/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313348](/post/id/313348)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/wins-is-dead-microsoft-to-fully-retire-wins-name-resolution-from-windows-server-post-2025/)

如若转载,请注明出处： <https://securityonline.info/wins-is-dead-microsoft-to-fully-retire-wins-name-resolution-from-windows-server-post-2025/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **728**

* 粉丝
* **6**

### TA的文章

* ##### [微软宣告WINS服务终结：Windows名称解析服务将于2025年后从Windows Server中全面退役](/post/id/313348)

  2025-11-25 17:46:05
* ##### [美国CISA发布警告：Oracle身份管理器中的远程代码执行漏洞正遭攻击者积极利用](/post/id/313352)

  2025-11-25 17:45:43
* ##### [美国司法部诉谷歌广告技术反垄断案进入最终阶段，预计将迎来快速裁决](/post/id/313356)

  2025-11-25 17:44:55
* ##### [NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁](/post/id/313359)

  2025-11-25 17:44:33
* ##### [TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身](/post/id/313362)

  2025-11-25 17:43:43

### 相关文章

* ##### [美国CISA发布警告：Oracle身份管理器中的远程代码执行漏洞正遭攻击者积极利用](/post/id/313352)

  2025-11-25 17:45:43
* ##### [美国司法部诉谷歌广告技术反垄断案进入最终阶段，预计将迎来快速裁决](/post/id/313356)

  2025-11-25 17:44:55
* ##### [NVIDIA Isaac-GROOT机器人平台存在代码注入漏洞，对系统安全构成严重威胁](/post/id/313359)

  2025-11-25 17:44:33
* ##### [TamperedChef黑产借壳上市！冒用美企身份为带毒应用“洗白”，利用有效证书实现完美隐身](/post/id/313362)

  2025-11-25 17:43:43
* ##### [vLLM框架存在漏洞（CVE-2025-62164），通过恶意提示嵌入可导致远程代码执行](/post/id/313366)

  2025-11-25 17:43:02
* ##### [复杂WhatsApp蠕虫攻击通过伪造“阅后即焚”诱饵实施会话劫持，并投放Astaroth银行木马](/post/id/313369)

  2025-11-25 17:42:46
* ##### [PyPI拼写劫持投递多层Python木马，利用异或加密绕过扫描器](/post/id/313372)

  2025-11-25 17:41:58

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