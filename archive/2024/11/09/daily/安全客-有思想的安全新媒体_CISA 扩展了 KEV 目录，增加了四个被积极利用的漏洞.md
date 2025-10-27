---
title: CISA 扩展了 KEV 目录，增加了四个被积极利用的漏洞
url: https://www.anquanke.com/post/id/301652
source: 安全客-有思想的安全新媒体
date: 2024-11-09
fetch_date: 2025-10-06T19:14:27.862701
---

# CISA 扩展了 KEV 目录，增加了四个被积极利用的漏洞

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

# CISA 扩展了 KEV 目录，增加了四个被积极利用的漏洞

阅读量**65236**

发布时间 : 2024-11-08 14:11:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/cisa-expands-kev-catalog-with-four-actively-exploited-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

![Actively Exploited Vulnerabilities]()

网络安全和基础设施安全局（CISA）发布了关于四个在野外被积极利用的安全漏洞的最新公告。这些漏洞现已列入已知漏洞（KEV）目录，对私营和公共部门组织构成重大风险。

**CVE-2024-43093： 安卓框架权限升级漏洞**

该漏洞可在 Android 框架内实现权限升级，可能允许未经授权访问 “Android/data”、“Android/obb ”和 “Android/sandbox ”等敏感目录。虽然确切的攻击载体仍未披露，但谷歌承认有证据表明存在有限的、有针对性的利用。

**CVE-2024-51567 (CVSS 10)： CyberPanel 不正确默认权限漏洞**

广泛使用的网络托管控制面板 CyberPanel 存在一个关键漏洞，允许远程攻击者绕过身份验证机制并执行任意命令。该漏洞已在野外被发现，因此急需修复。受影响的版本包括 2.3.6 及 2.3.7（未修补）版本。

**CVE-2019-16278 (CVSS 9.8)： Nostromo nhttpd 目录遍历漏洞**

Nostromo nhttpd Web 服务器存在目录遍历漏洞，尽管该漏洞最初于 2019 年披露，但仍继续被利用。成功利用漏洞可导致远程代码执行，使攻击者能够控制受影响的服务器，并可能外泄数据或中断服务。

**CVE-2024-5910 (CVSS 9.3)： Palo Alto Expedition 身份验证缺失漏洞**

Palo Alto Networks 的 Expedition 軟件存在遺失驗證漏洞，允許未經授權存取管理帳戶。该漏洞已于 2024 年 7 月修补，但仍在被积极利用。攻击者可利用此漏洞控制 Expedition 服务器，从而可能访问敏感的配置数据和凭证。

**降低威胁**

CISA 敦促所有联邦文职行政部门 (FCEB) 机构在 2023 年 11 月 28 日前优先修补这些漏洞。强烈建议所有组织，无论属于哪个部门，立即采取行动来减轻这些威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/cisa-expands-kev-catalog-with-four-actively-exploited-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/301652](/post/id/301652)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/cisa-expands-kev-catalog-with-four-actively-exploited-vulnerabilities/)

如若转载,请注明出处： <https://securityonline.info/cisa-expands-kev-catalog-with-four-actively-exploited-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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