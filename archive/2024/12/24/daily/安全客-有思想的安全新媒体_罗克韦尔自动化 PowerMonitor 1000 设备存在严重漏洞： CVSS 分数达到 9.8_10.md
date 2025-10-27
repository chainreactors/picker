---
title: 罗克韦尔自动化 PowerMonitor 1000 设备存在严重漏洞： CVSS 分数达到 9.8/10
url: https://www.anquanke.com/post/id/302929
source: 安全客-有思想的安全新媒体
date: 2024-12-24
fetch_date: 2025-10-06T19:36:40.324226
---

# 罗克韦尔自动化 PowerMonitor 1000 设备存在严重漏洞： CVSS 分数达到 9.8/10

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

# 罗克韦尔自动化 PowerMonitor 1000 设备存在严重漏洞： CVSS 分数达到 9.8/10

阅读量**65564**

|评论**1**

发布时间 : 2024-12-23 11:22:11

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/critical-flaws-in-rockwell-automation-powermonitor-1000-devices-cvss-scores-hit-9-8-10/>

译文仅供参考，具体内容表达以及含义原文为准。

罗克韦尔自动化（Rockwell Automation）发布重要安全公告，强调了影响其 PowerMonitor 1000 设备的三个严重漏洞。这些漏洞由 Claroty Research – Team82 的 Vera Mens 发现，具有重大风险，包括远程代码执行、拒绝服务 (DoS) 和设备接管。

这些漏洞被追踪为 CVE-2024-12371、CVE-2024-12372 和 CVE-2024-12373，每个漏洞的 CVSS v3.1 基本分值均为 9.8/10，凸显了其严重性。

* **CVE-2024-12371**： 该漏洞使攻击者能够通过未经验证的 API 调用配置新的特权 “保单持有人 ”用户。正如罗克韦尔自动化所指出的，“保单持有人用户是权限最高的用户，可以执行编辑操作、创建管理员用户和执行出厂重置”。
* **CVE-2024-12372**： 此漏洞涉及堆内存损坏，可能危及系统完整性。利用此漏洞可能导致远程代码执行或拒绝服务攻击。
* **CVE-2024-12373**： 缓冲区溢出问题，可能导致拒绝服务情况，中断设备功能，并可能导致工业运行。

该公告列出了受这些漏洞影响的多个 PowerMonitor 1000 型号，包括 PM1k 1408-BC3A-485 和 PM1k 1408-EM3A-ENT。运行固件版本低于 4.020 的设备存在漏洞。罗克韦尔自动化强烈建议更新至固件版本 4.020 或更高版本，以降低这些风险。

尽管这些漏洞目前未被列入已知漏洞 (KEV) 数据库，但鉴于其关键性质，被利用的可能性仍然很高。鼓励使用这些设备的工业环境迅速采取行动。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-flaws-in-rockwell-automation-powermonitor-1000-devices-cvss-scores-hit-9-8-10/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302929](/post/id/302929)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-flaws-in-rockwell-automation-powermonitor-1000-devices-cvss-scores-hit-9-8-10/)

如若转载,请注明出处： <https://securityonline.info/critical-flaws-in-rockwell-automation-powermonitor-1000-devices-cvss-scores-hit-9-8-10/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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