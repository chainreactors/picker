---
title: LiteSpeed 缓存插件漏洞给 WordPress 网站带来重大风险
url: https://www.anquanke.com/post/id/301496
source: 安全客-有思想的安全新媒体
date: 2024-11-02
fetch_date: 2025-10-06T19:12:13.619260
---

# LiteSpeed 缓存插件漏洞给 WordPress 网站带来重大风险

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

# LiteSpeed 缓存插件漏洞给 WordPress 网站带来重大风险

阅读量**69986**

发布时间 : 2024-11-01 11:03:50

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/10/litespeed-cache-plugin-vulnerability.html>

译文仅供参考，具体内容表达以及含义原文为准。

WordPress 的 LiteSpeed Cache 插件中存在一个高度严重的安全漏洞，未经身份验证的威胁行为者可利用该漏洞提升权限并执行恶意操作。

该漏洞被追踪为 CVE-2024-50550（CVSS 得分：8.1），已在插件 6.5.2 版本中得到解决。

Patchstack 安全研究员拉菲-穆罕默德（Rafie Muhammad）在一份分析报告中说：“该插件存在一个未经身份验证的权限升级漏洞，任何未经身份验证的访问者都可以通过该漏洞获得管理员级别的访问权限，然后上传并安装恶意插件。”

LiteSpeed Cache 是一款流行的 WordPress 网站加速插件，顾名思义，它具有高级缓存功能和优化特性。该插件已被安装在 600 多万个网站上。

根据 Patchstack 的说法，新发现的问题源于一个名为 is\_role\_simulation 的函数，与 2024 年 8 月公开记录的早期漏洞（CVE-2024-28000，CVSS 得分：9.8）类似。

该漏洞源于使用了一个薄弱的安全散列检查，可被恶意行为者暴力破解，从而使爬虫功能被滥用来模拟登录用户，包括管理员。

然而，成功的漏洞利用依赖于以下插件配置

* 爬虫 -> 常规设置 -> 爬虫： 开启
* 爬虫 -> 常规设置 -> 运行持续时间：2500 – 4000
* 爬虫 -> 常规设置 -> 运行间隔：2500 – 4000
* 爬虫 -> 常规设置 -> 服务器负载限制：0
* 爬虫 -> 模拟设置 -> 角色模拟： 1（具有管理员角色的用户 ID）
* 爬虫 -> 摘要 -> 激活： 将除管理员外的每一行都设置为关闭

LiteSpeed 发布的补丁删除了角色模拟程序，并使用随机值生成器更新了哈希生成步骤，以避免将哈希值限制在 100 万种可能性。

Muhammad 说：“这个漏洞凸显了确保用作安全哈希值或非ces 的值的强度和不可预测性的极端重要性。”

“PHP中的rand()和mt\_rand()函数返回的值对于许多用例来说可能’足够随机’，但它们的不可预测性不足以用于与安全相关的功能，尤其是在mt\_srand被用于有限可能性的情况下。”

CVE-2024-50550 是 LiteSpeed 在过去两个月内披露的第三个安全漏洞，另外两个是 CVE-2024-44000（CVSS 得分：7.5）和 CVE-2024-47374（CVSS 得分：7.2）。

Patchstack 在几周前详细介绍了 Ultimate Membership Pro 中两个可能导致权限升级和代码执行的关键漏洞。但这些缺陷已在 12.8 及更高版本中得到解决。

* CVE-2024-43240（CVSS 得分：9.4）- 一个未经身份验证的权限升级漏洞，允许攻击者注册任何会员级别并获得其附加角色
* CVE-2024-43242 (CVSS 分數：9.0) – 未經驗證的 PHP 物件注入漏洞，攻擊者可利用漏洞執行任意程式碼。

Patchstack 还警告说，WordPress 母公司 Automattic 与 WP Engine 之间持续不断的法律纠纷已促使一些开发人员放弃 WordPress.org 存储库，因此用户有必要监控适当的通信渠道，以确保他们收到有关可能的插件关闭和安全问题的最新信息。

Patchstack首席执行官奥利弗-西尔德（Oliver Sild）说：“用户如果不手动安装从WordPress.org资源库中删除的插件，就有可能收不到新的更新，而这些更新可能包括重要的安全修复。“这可能会使网站暴露在黑客面前，而黑客通常会利用已知的漏洞，并可能在这种情况下乘虚而入。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/10/litespeed-cache-plugin-vulnerability.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301496](/post/id/301496)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/10/litespeed-cache-plugin-vulnerability.html)

如若转载,请注明出处： <https://thehackernews.com/2024/10/litespeed-cache-plugin-vulnerability.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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