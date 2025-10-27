---
title: Netis 路由器中的三个关键漏洞导致未经验证的 RCE
url: https://www.anquanke.com/post/id/303362
source: 安全客-有思想的安全新媒体
date: 2025-01-10
fetch_date: 2025-10-06T20:07:08.643055
---

# Netis 路由器中的三个关键漏洞导致未经验证的 RCE

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

# Netis 路由器中的三个关键漏洞导致未经验证的 RCE

阅读量**73138**

发布时间 : 2025-01-09 10:06:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/trio-of-critical-vulnerabilities-in-netis-routers-enables-unauthenticated-rce/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-48455, CVE-2024-48456, and CVE-2024-48457]()

安全研究员H00die.Gr3y最近的一份报告揭示了一系列影响多款Netis路由器以及GLCtec和Stonet的同类产品的关键漏洞。 这些漏洞被追踪为 CVE-2024-48455、CVE-2024-48456 和 CVE-2024-48457，它们可以串联在一起，允许未经验证的远程代码执行 （RCE），从而使成千上万的设备受到攻击。

* **CVE-2024-48455**：这个信息泄露漏洞可让未认证的攻击者取得敏感的配置数据，包括固件版本和网络设定。 攻击者可利用 /cgi-bin/skk\_get.cgi 网络端点查询易受攻击的设备，并评估其是否适合进一步攻击。
* **CVE-2024-48456**： 这是路由器密码更改功能中的验证命令注入漏洞。 恶意行为者可利用密码和新密码参数，注入 base64 编码的命令来获取远程 shell 访问权限。 与其他漏洞结合使用时，此漏洞可实现对路由器的完全控制。
* **CVE-2024-48457**：一个身份验证绕过漏洞，允许未经身份验证的攻击者重置路由器和 WiFi 密码。 利用这个问题可让攻击者有效控制设备，为利用 CVE-2024-48456 铺平道路。

通过连锁这些漏洞，攻击者可以绕过身份验证、重置设备凭据并执行任意命令，从而完全控制受影响的路由器。 这些漏洞影响多个固件版本，包括但不限于

* **netis\_MW5360\_V1.0.1.3031\_fw.bin**
* **netis\_NC65v2-V3.0.0.3800.bin**
* **Netis\_NX10-V3.0.1.4205.bin**

受影响固件版本的完整列表请参见 Netis 固件支持文档。

H00die.Gr3y 使用固件仿真工具 FirmAE 和二进制分析工具 Ghidra 等工具演示了漏洞利用链，并强调了将路由器的管理员密码与其根系统密码关联等不良安全做法。

Netis 及其改名后的合作伙伴尚未发布解决这些漏洞的官方补丁。

本文翻译自securityonline [原文链接](https://securityonline.info/trio-of-critical-vulnerabilities-in-netis-routers-enables-unauthenticated-rce/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303362](/post/id/303362)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/trio-of-critical-vulnerabilities-in-netis-routers-enables-unauthenticated-rce/)

如若转载,请注明出处： <https://securityonline.info/trio-of-critical-vulnerabilities-in-netis-routers-enables-unauthenticated-rce/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

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