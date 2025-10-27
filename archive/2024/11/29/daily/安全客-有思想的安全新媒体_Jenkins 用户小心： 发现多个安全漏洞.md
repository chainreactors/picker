---
title: Jenkins 用户小心： 发现多个安全漏洞
url: https://www.anquanke.com/post/id/302258
source: 安全客-有思想的安全新媒体
date: 2024-11-29
fetch_date: 2025-10-06T19:14:45.507765
---

# Jenkins 用户小心： 发现多个安全漏洞

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

# Jenkins 用户小心： 发现多个安全漏洞

阅读量**71957**

发布时间 : 2024-11-28 14:39:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/jenkins-users-beware-multiple-security-vulnerabilities-discovered/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-47855]()

广泛使用的开源自动化服务器 Jenkins 发布了一份安全公告，解决了影响其核心系统和相关插件的多个漏洞。这些漏洞从拒绝服务到跨站脚本，如果不及时修补，将给 Jenkins 用户带来重大风险。

**通过 JSON 处理拒绝服务 (CVE-2024-47855)**

在 Jenkins 的 JSON 处理库中发现了一个拒绝服务漏洞（CVSS 7.5）。正如公告所述，“在 Jenkins（不含插件）中，这允许拥有 Overall/Read 权限的攻击者无限期地保持 HTTP 请求处理线程繁忙，从而占用系统资源并阻止合法用户使用 Jenkins。”这意味着恶意行为者可以有效地关闭 Jenkins 实例，中断关键的开发流水线并造成严重的停机。

令人担忧的是，该公告还强调：“Jenkins 安全团队已经发现多个插件允许缺乏 Overall/Read 权限的攻击者进行同样的操作。这些插件包括 SonarQube Scanner 和 Bitbucket。”这扩大了攻击面，增加了安装了这些插件的 Jenkins 用户的风险。

**简单队列插件中的存储 XSS (CVE-2024-54003)**

在 Simple Queue 插件中发现了一个高度严重的存储 XSS 漏洞（CVSS 8.0）。该漏洞允许具有 “查看/创建 ”权限的攻击者注入恶意脚本，这些脚本可由其他用户执行，可能导致数据窃取、会话劫持或进一步的系统危害。

**文件系统列表参数插件中的路径遍历 (CVE-2024-54004)**

文件系统列表参数插件还包含一个漏洞（CVSS 4.3），允许拥有 “Item/Configure ”权限的攻击者 “枚举 Jenkins 控制器文件系统上的文件名”。虽然该漏洞被评为中等严重性，但它仍可为攻击者提供用于进一步攻击的宝贵信息。

**缓解和补救措施**

Jenkins 已发布更新版本来解决这些漏洞。强烈建议用户立即升级到最新版本：

* **Jenkins 每周更新一次：** 更新至版本 2.487
* **Jenkins LTS：**更新至版本 2.479.2
* **文件系统列表参数插件：** 更新至版本 0.0.15
* **简单队列插件：**更新至版本 1.4.5 更新至版本 1.4.5

公告强调：“这些版本包含对上述漏洞的修复。除非另有说明，否则所有先前版本均被视为受这些漏洞的影响。”

依赖 Jenkins 满足自动化需求的组织应优先考虑这些更新，以确保其 CI/CD 管道的安全性和完整性。

本文翻译自securityonline [原文链接](https://securityonline.info/jenkins-users-beware-multiple-security-vulnerabilities-discovered/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302258](/post/id/302258)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/jenkins-users-beware-multiple-security-vulnerabilities-discovered/)

如若转载,请注明出处： <https://securityonline.info/jenkins-users-beware-multiple-security-vulnerabilities-discovered/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

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