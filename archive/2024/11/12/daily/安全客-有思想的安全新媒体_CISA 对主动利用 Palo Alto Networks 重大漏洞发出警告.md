---
title: CISA 对主动利用 Palo Alto Networks 重大漏洞发出警告
url: https://www.anquanke.com/post/id/301706
source: 安全客-有思想的安全新媒体
date: 2024-11-12
fetch_date: 2025-10-06T19:12:18.281499
---

# CISA 对主动利用 Palo Alto Networks 重大漏洞发出警告

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

# CISA 对主动利用 Palo Alto Networks 重大漏洞发出警告

阅读量**53754**

发布时间 : 2024-11-11 15:04:10

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/11/cisa-alerts-to-active-exploitation-of.html>

译文仅供参考，具体内容表达以及含义原文为准。

美国网络安全和基础设施安全局（CISA）周四将一个影响 Palo Alto Networks Expedition 的重大安全漏洞添加到其已知漏洞（KEV）目录中，并指出有证据表明该漏洞正在被利用。

该漏洞被追踪为 CVE-2024-5910（CVSS 得分：9.3），涉及 Expedition 迁移工具中的一个身份验证缺失案例，可能导致管理员账户被接管。

CISA 在一份警报中说：“Palo Alto Expedition 存在一个身份验证缺失漏洞，允许具有网络访问权限的攻击者接管 Expedition 管理帐户，并可能访问配置机密、凭证和其他数据。”

这一缺陷影响到 1.2.92 版之前的所有 Expedition 版本，该版本于 2024 年 7 月发布，以解决这一问题。

目前还没有关于该漏洞如何在实际攻击中被武器化的报告，但 Palo Alto Networks 已经修改了其最初的公告，承认 “从 CISA 的报告中了解到有证据表明该漏洞正在被利用”。

KEV目录中还增加了另外两个漏洞，包括谷歌本周披露的Android框架组件中的权限升级漏洞（CVE-2024-43093），该漏洞已被 “有针对性地有限利用”。

另一个安全缺陷是 CVE-2024-51567（CVSS 得分：10.0），这是一个影响 CyberPanel 的关键漏洞，允许未经认证的远程攻击者以 root 身份执行命令。该问题已在 2.3.8 版本中得到解决。

2023 年 10 月下旬，据 LeakIX 和一位化名为 Gi7w0rm 的安全研究人员称，恶意行为者利用该漏洞在超过 22,000 个暴露在互联网上的 CyberPanel 实例上大规模部署 PSAUX 勒索软件。

LeakIX 还指出，有三个不同的勒索软件小组迅速利用了这一漏洞，在某些情况下文件被多次加密。

已建议联邦文职行政部门（FCEB）机构在 2024 年 11 月 28 日前修复已发现的漏洞，以确保其网络免受主动威胁。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/11/cisa-alerts-to-active-exploitation-of.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301706](/post/id/301706)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/11/cisa-alerts-to-active-exploitation-of.html)

如若转载,请注明出处： <https://thehackernews.com/2024/11/cisa-alerts-to-active-exploitation-of.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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