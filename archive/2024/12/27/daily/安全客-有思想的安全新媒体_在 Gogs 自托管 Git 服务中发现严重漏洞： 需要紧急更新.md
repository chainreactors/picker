---
title: 在 Gogs 自托管 Git 服务中发现严重漏洞： 需要紧急更新
url: https://www.anquanke.com/post/id/303032
source: 安全客-有思想的安全新媒体
date: 2024-12-27
fetch_date: 2025-10-06T19:35:05.996602
---

# 在 Gogs 自托管 Git 服务中发现严重漏洞： 需要紧急更新

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

# 在 Gogs 自托管 Git 服务中发现严重漏洞： 需要紧急更新

阅读量**102635**

发布时间 : 2024-12-26 11:04:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-vulnerabilities-found-in-gogs-self-hosted-git-service-urgent-update-required/>

译文仅供参考，具体内容表达以及含义原文为准。

在流行的开源自托管 Git 服务 Gogs 中发现了多个严重的安全漏洞。 这些漏洞的 CVSS 得分从 7.7 到 9.9 不等，攻击者可利用漏洞执行任意代码、获得未经授权的访问权限并窃取敏感数据。

**漏洞和影响：**

* **CVE-2024-55947（CVSS 8.7）：** 允许攻击者将文件写入任意路径，可能会授予服务器 SSH 访问权限。
* **CVE-2024-39930（CVSS 9.9）：** 当内置 SSH 服务器启用时，未授权用户能够以较高的权限执行指令。
* **CVE-2024-39931 （CVSS 9.9）：** 允许未授权用户删除内部文件，可能导致系统受损。
* **CVE-2024-39932 （CVSS 9.9）：** 允许攻击者写入任意文件，可能导致强制重新安装和赋予管理员权限。
* **CVE-2024-39933（CVSS 7.7）：** 未授权用户可读取任意文件，包括包含数据库凭据和 TLS 证书的配置文件。
* **CVE-2024-54148 （CVSS 8.7）：**允许攻击者获取 SSH 证书： 允许攻击者通过操作符号链接文件获得服务器的 SSH 访问权限。

**需要采取紧急行动：**

强烈建议 Gogs 用户立即将其安装更新至 0.13.1 版或最新的 0.14.0+dev。 这些更新可解决已发现的漏洞并提供重要的安全修复。

**变通方法：**

在没有立即更新的情况下，限制只有受信任用户才能访问 Gogs 实例至关重要。 对于 CVE-2024-39930，建议在非 Windows 系统上禁用内置 SSH 服务器。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-vulnerabilities-found-in-gogs-self-hosted-git-service-urgent-update-required/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303032](/post/id/303032)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-vulnerabilities-found-in-gogs-self-hosted-git-service-urgent-update-required/)

如若转载,请注明出处： <https://securityonline.info/critical-vulnerabilities-found-in-gogs-self-hosted-git-service-urgent-update-required/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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