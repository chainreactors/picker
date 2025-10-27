---
title: PostgreSQL 发布安全更新解决多个漏洞
url: https://www.anquanke.com/post/id/301918
source: 安全客-有思想的安全新媒体
date: 2024-11-19
fetch_date: 2025-10-06T19:13:46.163251
---

# PostgreSQL 发布安全更新解决多个漏洞

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

# PostgreSQL 发布安全更新解决多个漏洞

阅读量**54163**

发布时间 : 2024-11-18 10:24:15

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/postgresql-releases-security-update-addressing-multiple-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-10979 PostgreSQL vulnerability]()

PostgreSQL 全球开发小组发布了一个重要更新，以解决这个流行的开源数据库系统所有支持版本中的四个安全漏洞。这包括 17.1、16.5、15.9、14.14、13.17 和 12.21 版本。强烈建议用户立即更新其安装，以降低潜在风险。

漏洞的严重程度不一，其中最严重的漏洞（**CVE-2024-10979，CVSS 8.8**）可在 PostgreSQL 服务器的上下文中执行任意代码。该漏洞存在于 PL/Perl 程序语言中，允许攻击者操纵环境变量，有可能导致系统完全崩溃。正如公告所述：”PostgreSQL PL/Perl中对环境变量的不正确控制允许无权限数据库用户更改敏感的进程环境变量（如PATH）。即使攻击者没有数据库服务器操作系统用户，这通常也足以实现任意代码执行。

此更新解决的其他漏洞包括

* **CVE-2024-10976**： 该漏洞涉及行安全策略，可能允许攻击者绕过预定的限制，访问或修改他们本不应该访问或修改的数据。“应用不正确的策略可能会允许用户完成禁止的读取和修改。
* **CVE-2024-10977**：该漏洞影响 libpq 客户端库，可能允许中间人攻击者注入错误信息，诱使用户泄露敏感信息。
* **CVE-2024-10978**： 此漏洞涉及 SET ROLE 和 SET SESSION AUTHORIZATION 命令中不正确的权限分配，可能允许攻击者未经授权访问数据。

本次更新还包括对超过 35 个非安全相关漏洞的修复。值得注意的是，这是 PostgreSQL 12 的最终版本，该版本现已达到生命周期终点。强烈建议仍在运行 PostgreSQL 12 的用户尽快迁移到受支持的版本。

本文翻译自securityonline [原文链接](https://securityonline.info/postgresql-releases-security-update-addressing-multiple-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301918](/post/id/301918)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/postgresql-releases-security-update-addressing-multiple-vulnerabilities/)

如若转载,请注明出处： <https://securityonline.info/postgresql-releases-security-update-addressing-multiple-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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