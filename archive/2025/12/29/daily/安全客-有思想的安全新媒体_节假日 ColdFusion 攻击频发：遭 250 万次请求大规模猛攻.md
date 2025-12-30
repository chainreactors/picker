---
title: 节假日 ColdFusion 攻击频发：遭 250 万次请求大规模猛攻
url: https://www.anquanke.com/post/id/314079
source: 安全客-有思想的安全新媒体
date: 2025-12-29
fetch_date: 2025-12-30T03:25:39.319912
---

# 节假日 ColdFusion 攻击频发：遭 250 万次请求大规模猛攻

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

# 节假日 ColdFusion 攻击频发：遭 250 万次请求大规模猛攻

阅读量**17315**

发布时间 : 2025-12-29 15:37:21

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/holiday-coldfusion-attacks-reveal-massive-2-5-million-request-onslaught/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场看似针对 Adobe ColdFusion 服务器发起的节假日定向攻击，最终演变为规模庞大、工业化级别的网络攻击行动。灰度噪声（GreyNoise）发布最新情报更新指出，2025 年圣诞假期期间首次监测到的这场攻击，不过是冰山一角，其背后隐藏着一场**针对全球几乎所有主流技术栈的大规模协同初始访问代理攻击行动**。

当安全防护人员忙着拆圣诞礼物时，某单一威胁攻击者正忙着挖掘各类漏洞 —— 短短数日内就发起超 250 万次恶意请求。

该攻击行动最初进入研究人员视野，源于针对 Adobe ColdFusion 服务器的漏洞利用尝试出现协同性激增。攻击者系统性针对 2023 至 2024 年间披露的 10 余个不同漏洞（对应 CVE 编号）发起攻击，试图攻陷这类服务器。

而随着分析师深入调查，攻击的波及范围令人震惊。

报告明确：“进一步分析显示，ColdFusion 相关攻击仅占这场大型攻击行动的冰山一角。攻击源两台核心 IP（134.122.136.119、134.122.136.96）针对 47 类以上技术栈的 767 个不同漏洞，发起了超 250 万次攻击请求。”

此次攻击行动呈现高度集中化特征。灰度噪声确认，攻击源于**单一威胁攻击者**，依托日本境内基础设施开展操作，且明确指出攻击跳板为托管服务商 CTG Server Limited。

该单一攻击源的攻击强度惊人，此期间监测到的攻击流量中，约 98% 均来自该来源。攻击者动用了近 1 万个唯一 Interactsh OAST 域名，这一技术的核心作用是诱导目标服务器主动连接攻击者控制的域名，以此确认漏洞利用是否成功。

攻击目标覆盖面极广，可见攻击者采用自动化 “广撒网、碰运气” 战术，目的是从所有联网的脆弱设备中窃取访问凭证与网页后门。攻击针对 47 类以上不同技术栈，具体包括：

・Java 应用服务器：Tomcat、WebLogic、JBoss（攻击请求 132113 次）

・Web 开发框架：Apache、Struts、Spring（攻击请求 91253 次）

・内容管理系统：WordPress、Joomla、Drupal（攻击请求 72711 次）

・网络设备：思科、网件、F5、友讯（攻击请求 36355 次）

攻击者的目标不仅限于各类服务器，还针对性攻击监控系统（大华、海康威视）及企业级监控工具（Nagios、Grafana）。

尽管此次攻击覆盖面极广，但部分漏洞成为攻击者重点利用对象。报告指出，**侦察探测行为占总攻击活动的 56.4%**，其次是直接漏洞利用，占比 17.1%。

被滥用最多的高危漏洞包括：

CVE-2023-26360：Adobe ColdFusion 远程代码执行（RCE）漏洞

CVE-2017-9841：PHPUnit 组件高危远程代码执行漏洞

CVE-2018-11776：臭名昭著的 Apache Struts 2 远程代码执行漏洞

灰度噪声最终判定：“这显然是一场大规模、高度协同的初始访问代理攻击行动”，同时警示，被攻陷的系统近期可能会被打包出售给勒索软件团伙或其他网络犯罪分子，用于发起二次攻击。

本文翻译自securityonline [原文链接](https://securityonline.info/holiday-coldfusion-attacks-reveal-massive-2-5-million-request-onslaught/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314079](/post/id/314079)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/holiday-coldfusion-attacks-reveal-massive-2-5-million-request-onslaught/)

如若转载,请注明出处： <https://securityonline.info/holiday-coldfusion-attacks-reveal-massive-2-5-million-request-onslaught/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **870**

* 粉丝
* **6**

### TA的文章

* ##### [EmEditor 遭攻陷：“沃尔沙姆” 伪装者篡改官方安装包，植入间谍软件](/post/id/314096)

  2025-12-29 15:40:16
* ##### [性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线](/post/id/314100)

  2025-12-29 15:39:28
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37

### 相关文章

* ##### [EmEditor 遭攻陷：“沃尔沙姆” 伪装者篡改官方安装包，植入间谍软件](/post/id/314096)

  2025-12-29 15:40:16
* ##### [性能推进器：谷歌提议将高性能优化器纳入 LLVM 上游主线](/post/id/314100)

  2025-12-29 15:39:28
* ##### [圣诞洗劫：Trust Wallet v2.68 版本后门如何盗走 700 万美元](/post/id/314091)

  2025-12-29 15:39:18
* ##### [70 美元芯片争夺战：谷歌缘何高管换人，苹果又为何要直面 230% 的价格暴涨](/post/id/314077)

  2025-12-29 15:38:41
* ##### [CVE-2025-54322（CVSS 10 分满分）：AI 智能体发现全球网络设备高危零日漏洞](/post/id/314086)

  2025-12-29 15:38:37
* ##### [终结 “内存占用税”：微软新方案让文件资源管理器搜索速度翻倍](/post/id/314084)

  2025-12-29 15:38:15
* ##### [黑客攻陷 Trust Wallet 谷歌浏览器插件，用户称数百万资产被盗](/post/id/314073)

  2025-12-29 15:37:47

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