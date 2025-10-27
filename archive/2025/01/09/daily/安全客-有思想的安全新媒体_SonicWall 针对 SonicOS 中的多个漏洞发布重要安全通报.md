---
title: SonicWall 针对 SonicOS 中的多个漏洞发布重要安全通报
url: https://www.anquanke.com/post/id/303351
source: 安全客-有思想的安全新媒体
date: 2025-01-09
fetch_date: 2025-10-06T20:06:09.641456
---

# SonicWall 针对 SonicOS 中的多个漏洞发布重要安全通报

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

# SonicWall 针对 SonicOS 中的多个漏洞发布重要安全通报

阅读量**60890**

发布时间 : 2025-01-08 14:24:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/sonicwall-issues-important-security-advisory-for-multiple-vulnerabilities-in-sonicos/>

译文仅供参考，具体内容表达以及含义原文为准。

![SonicOS vulnerability - CVE-2024-53704]()

领先的网络安全提供商 SonicWall 发布重要安全公告，警告其 SonicOS 操作系统存在多个漏洞。 这些漏洞影响到 Gen6 和 Gen7 防火墙，从身份验证旁路到权限升级，使设备暴露于潜在的网络攻击。

**漏洞详情：**

公告详细说明了四个重大漏洞：

* **CVE-2024-40762 （CVSS 7.1）：** SSLVPN 身份验证令牌生成器中的一个弱点可能允许攻击者预测令牌并绕过身份验证，从而获得未经授权的访问。
* **CVE-2024-53704 （CVSS 8.2）：** SSLVPN 机制中的不当认证漏洞，可让远程攻击者绕过认证。
* **CVE-2024-53705 （CVSS 6.5）：** SSH 管理接口中的服务器端请求伪造 （SSRF） 漏洞，可让攻击者建立到任意 IP 地址和端口的 TCP 连线。
* **CVE-2024-53706 （CVSS 7.8）：** Gen7 SonicOS 云平台 NSv（仅限 AWS 和 Azure 版本）中的权限升级漏洞可能允许攻击者获得 root 权限并可能执行代码。

**降低风险：**

SonicWall 强烈建议所有受影响 SonicOS 版本的用户立即升级到最新的固定发布版本。

* **Gen6 硬件防火墙：** 升级到 6.5.5.1-6n 或更高版本。
* **Gen7 防火墙：** 升级到 7.1.3-7015 或更高版本。
* **Gen7 NSv：** 升级到 7.0.1-5165 或更高版本。
* **TZ80：**升级到 8.0.0-8037 或更高版本。

**解决方法：**

除更新外，SonicWall 还建议采用几种变通方法来最大限度地降低潜在风险：

* **限制访问：** 将 SSLVPN 和 SSH 管理访问限制为可信来源，或完全禁止从互联网访问。

**没有证据表明存在主动利用：**

SonicWall 表示，目前没有证据表明这些漏洞在野外被利用。 不过，该公司敦促用户立即采取行动保护自己的系统。

本文翻译自securityonline [原文链接](https://securityonline.info/sonicwall-issues-important-security-advisory-for-multiple-vulnerabilities-in-sonicos/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303351](/post/id/303351)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/sonicwall-issues-important-security-advisory-for-multiple-vulnerabilities-in-sonicos/)

如若转载,请注明出处： <https://securityonline.info/sonicwall-issues-important-security-advisory-for-multiple-vulnerabilities-in-sonicos/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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