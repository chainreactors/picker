---
title: 7个 Android & Pixel 漏洞暴露：研究人员发布 PoC 漏洞
url: https://www.anquanke.com/post/id/302183
source: 安全客-有思想的安全新媒体
date: 2024-11-27
fetch_date: 2025-10-06T19:12:21.064450
---

# 7个 Android & Pixel 漏洞暴露：研究人员发布 PoC 漏洞

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

# 7个 Android & Pixel 漏洞暴露：研究人员发布 PoC 漏洞

阅读量**64807**

发布时间 : 2024-11-26 11:01:55

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/7-android-pixel-vulnerabilities-exposed-researcher-publishes-poc-exploits/>

译文仅供参考，具体内容表达以及含义原文为准。

![Baseband Security]()

知名网络安全公司 Oversecured 发现了安卓操作系统和谷歌 Pixel 设备中的七个漏洞。其中两个漏洞特别危及谷歌 Pixel 用户，其余五个漏洞则对所有安卓设备构成威胁，无论其制造商是谁。

对于谷歌 Pixel 用户，报告强调了允许未经授权的应用程序访问地理位置数据和绕过 VPN 保护的漏洞。前者被识别为CVE-2024-0017，它利用了安卓相机应用程序中不当的地理位置权限，使攻击者能够从用户照片中提取位置元数据。报告称，相机应用程序的 LegacyLocationProvider 处理程序在特定条件下错误地将地理位置数据传递给了无权限应用程序。

另一个漏洞（CVE-2023-21383）利用了安卓设置应用程序中未声明的权限，允许攻击者将应用程序添加到 VPN 旁路列表中。这个漏洞可能会将敏感数据流量暴露在安全的 VPN 通道之外，从而带来重大风险。

![Pixel Vulnerabilities]()
图片 过密保护

其余漏洞对所有安卓设备都构成威胁，无论其制造商是谁。主要问题包括：

* **WebView 文件盗窃**： WebChromeClient.FileChooserParams 中配置错误的默认设置使攻击者能够拦截文件共享意图，导致未经授权的数据访问。
* **蓝牙漏洞利用**： 蓝牙 API 中的错误权限检查 (**CVE-2024-34719**) 允许恶意应用程序获得蓝牙功能的系统级权限访问。
* **设备管理屏幕上的 HTML 注入**： 设备管理请求屏幕中存在一个长期存在的漏洞 (**CVE-2021-0600**)，允许攻击者在管理提示中注入恶意 HTML 元素。
* **内容提供程序安全绕过**： ContentProvider.openFile() 方法绕过了内部安全检查，使攻击者能够在未经授权的情况下访问受保护的应用程序组件。

一个名为 **CVE-2023-20963** 的漏洞被 Temu 应用程序的开发商 Pinduoduo 应用程序在 “野外 ”利用，使攻击者能够代表 Android 系统访问任意组件。报告指出，这一漏洞在 2023 年被修补之前已经存在了近一年时间。

研究人员公布了所有这些漏洞的技术细节和概念验证利用代码。

所有已发现的漏洞都已通过修补程序得到解决，修补程序在 2023 年底至 2024 年间陆续推出。如果这些漏洞危及关键工作流程，强烈建议用户安装最新的安全更新或考虑使用替代工具。

本文翻译自securityonline [原文链接](https://securityonline.info/7-android-pixel-vulnerabilities-exposed-researcher-publishes-poc-exploits/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302183](/post/id/302183)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/7-android-pixel-vulnerabilities-exposed-researcher-publishes-poc-exploits/)

如若转载,请注明出处： <https://securityonline.info/7-android-pixel-vulnerabilities-exposed-researcher-publishes-poc-exploits/>

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