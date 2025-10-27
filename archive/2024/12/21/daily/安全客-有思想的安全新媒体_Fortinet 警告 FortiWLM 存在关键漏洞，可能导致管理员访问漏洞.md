---
title: Fortinet 警告 FortiWLM 存在关键漏洞，可能导致管理员访问漏洞
url: https://www.anquanke.com/post/id/302870
source: 安全客-有思想的安全新媒体
date: 2024-12-21
fetch_date: 2025-10-06T19:36:17.929674
---

# Fortinet 警告 FortiWLM 存在关键漏洞，可能导致管理员访问漏洞

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

# Fortinet 警告 FortiWLM 存在关键漏洞，可能导致管理员访问漏洞

阅读量**76010**

|评论**1**

发布时间 : 2024-12-20 10:11:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/fortinet-warns-of-critical-fortiwlm.html>

译文仅供参考，具体内容表达以及含义原文为准。

Fortinet 发布公告，纠正影响Wireless LAN Manager （FortiWLM） 的严重安全漏洞，该漏洞可能导致敏感信息外泄。

该漏洞被追踪为 CVE-2023-34990，CVSS 得分为 9.6（最高 10.0）。

该公司在周三发布的警报中说：“FortiWLM 中的相对路径遍历 [CWE-23] 可能允许远程未认证攻击者读取敏感文件。”

不过，根据 NIST 国家漏洞数据库（NVD）对该安全漏洞的描述，路径遍历漏洞也可能被攻击者利用，“通过特制的 Web 请求执行未经授权的代码或命令。”

该漏洞影响以下版本的产品

* FortiWLM 版本 8.6.0 至 8.6.5（已在 8.6.6 或以上版本中修复）
* FortiWLM 版本 8.5.0 至 8.5.4（已在 8.5.5 或以上版本中修复）

该公司感谢 Horizon3.ai 安全研究员 Zach Hanley 发现并报告了这一漏洞。 值得一提的是，CVE-2023-34990 指的是网络安全公司在 3 月份披露的 “未经验证的有限文件读取漏洞”，它是 FortiWLM 中更广泛的六个缺陷的一部分。

“这个漏洞允许未经验证的远程攻击者访问和滥用内置功能，这些功能的目的是通过向/ems/cgi-bin/ezrf\_lighttpd.cgi端点发出精心设计的请求来读取系统上的特定日志文件，”Hanley当时说。

“这个问题是由于请求参数缺乏输入验证造成的，允许攻击者遍历目录并读取系统上的任何日志文件。”

成功利用CVE-2023-34990后，威胁者可以读取FortiWLM日志文件，掌握用户的会话ID并登录，从而也可以利用经过验证的端点。

更糟糕的是，攻击者可以利用网络会话 ID 在用户会话之间是静态的这一事实，劫持它们并获得设备的管理权限。

这还不是全部。 攻击者还可以将 CVE-2023-34990 与 CVE-2023-48782 （CVSS 得分：8.8）（FortiWLM 8.6.6 中也修复了这一验证命令注入漏洞）结合起来，在 root 上下文中执行远程代码。

Fortinet 还修补了 FortiManager 中的一个高严重性操作系统命令注入漏洞，该漏洞可能允许经过验证的远程攻击者通过 FGFM 创建的请求执行未经授权的代码。

该漏洞（CVE-2024-48889，CVSS 得分：7.2）已在以下版本中得到解决 – FortiManager 7.6.0、FortiManager 7.6.1 和 FortiManager 7.6.2。

* FortiManager 7.6.0（已在 7.6.1 或以上版本中修复）
* FortiManager 7.4.0 至 7.4.4 版本（已在 7.4.5 或以上版本中修复）
* FortiManager 云版本 7.4.1 至 7.4.4（已在 7.4.5 或更高版本中修复）
* FortiManager 版本 7.2.3 至 7.2.7（已在 7.2.8 或更高版本中修复）
* FortiManager 云版本 7.2.1 至 7.2.7（已在 7.2.8 或更高版本中修复）
* FortiManager 版本 7.0.5 至 7.0.12（已在 7.0.13 或更高版本中修复）
* FortiManager 云版本 7.0.1 至 7.0.12（已在 7.0.13 或更高版本中修复）
* FortiManager 版本 6.4.10 至 6.4.14（已在 6.4.15 或以上版本中修复）

Fortinet 还指出，一些旧型号（1000E、1000F、2000E、3000E、3000F、3000G、3500E、3500F、3500G、3700F、3700G 和 3900E）受 CVE-2024-48889 影响，前提是启用了 “fmg-status”。

随着 Fortinet 设备成为威胁行为者的攻击磁铁，用户必须保持其实例的更新，以防范潜在威胁。

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/fortinet-warns-of-critical-fortiwlm.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302870](/post/id/302870)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/fortinet-warns-of-critical-fortiwlm.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/fortinet-warns-of-critical-fortiwlm.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**3赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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