---
title: 保护您的网络： Zyxel 发布固件更新
url: https://www.anquanke.com/post/id/302411
source: 安全客-有思想的安全新媒体
date: 2024-12-05
fetch_date: 2025-10-06T19:33:12.945201
---

# 保护您的网络： Zyxel 发布固件更新

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

# 保护您的网络： Zyxel 发布固件更新

阅读量**64795**

发布时间 : 2024-12-04 11:02:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/protect-your-network-zyxel-issues-firmware-updates/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2023-33009 & CVE-2024-8748 - CVE-2024-9200]()

Zyxel Networks 发布固件更新，以解决影响其一系列网络产品的多个漏洞，包括 4G LTE/5G NR CPE、DSL/以太网 CPE、光纤 ONT 和 WiFi 扩展器。这些漏洞有可能使攻击者中断服务，甚至在受影响的设备上执行恶意代码。

其中一个关键漏洞被识别为 CVE-2024-8748，它是一个缓冲区溢出漏洞，可允许远程攻击者对受影响设备的 Web 管理界面发起拒绝服务 (DoS) 攻击。此漏洞存在于 Zyxel 某些固件版本中使用的第三方库 “libclinkc ”的数据包解析器中。

另一个重大漏洞（CVE-2024-9200）是一个验证后命令注入漏洞，可允许通过验证的攻击者在易受攻击的设备上执行任意操作系统命令。该漏洞影响某些 DSL/Ethernet CPE 固件版本中诊断功能的 “host ”参数。

CVE-2024-9197 是一个中等严重性漏洞，它是 CGI 程序 “action ”参数中的验证后缓冲区溢出漏洞，影响多个固件版本。拥有管理权限的验证攻击者可通过恶意 HTTP GET 请求造成 DoS 状况。Zyxel 指出，有漏洞的功能和 WAN 访问均 “默认禁用”，从而进一步限制了漏洞的暴露。

受影响的Zyxel产品范围广泛，包括LTE3301-PLUS、DX3300-T0和VMG3927-B50B等流行型号。已确定特定固件版本存在漏洞，可立即部署修补程序。有关受影响机型的完整列表和补丁详情，请用户查阅 Zyxel 的官方公告。

Zyxel 强调，许多漏洞都有缓解因素。例如，CVE-2024-8748 只有在启用广域网访问时才能被利用，而广域网访问在默认情况下是禁用的。此外，要成功利用 CVE-2024-9200 漏洞，需要破坏强大、唯一的管理员密码。

尽管存在这些缓解因素，但该公司仍敦促用户尽快安装最新的固件补丁，以确保获得最佳保护。Zyxel 在其官方安全公告中提供了受影响产品和相应固件版本的详细列表。

Zyxel 在其公告中表示：“经过彻底调查，我们已经在漏洞支持期内确定了受影响的产品，并发布了固件补丁来解决这些漏洞。”

即使有缓解因素，如果不加以解决，漏洞也会带来重大风险。我们鼓励用户查看 Zyxel 的公告，并采取必要行动确保设备安全。

本文翻译自securityonline [原文链接](https://securityonline.info/protect-your-network-zyxel-issues-firmware-updates/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302411](/post/id/302411)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/protect-your-network-zyxel-issues-firmware-updates/)

如若转载,请注明出处： <https://securityonline.info/protect-your-network-zyxel-issues-firmware-updates/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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