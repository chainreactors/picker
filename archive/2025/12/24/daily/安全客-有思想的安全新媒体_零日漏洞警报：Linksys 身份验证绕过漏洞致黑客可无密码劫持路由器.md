---
title: 零日漏洞警报：Linksys 身份验证绕过漏洞致黑客可无密码劫持路由器
url: https://www.anquanke.com/post/id/313984
source: 安全客-有思想的安全新媒体
date: 2025-12-24
fetch_date: 2025-12-25T03:24:45.679815
---

# 零日漏洞警报：Linksys 身份验证绕过漏洞致黑客可无密码劫持路由器

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

# 零日漏洞警报：Linksys 身份验证绕过漏洞致黑客可无密码劫持路由器

阅读量**15681**

发布时间 : 2025-12-24 15:03:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源： securityonline

原文地址：<https://securityonline.info/zero-day-alert-linksys-auth-bypass-lets-hackers-hijack-routers-without-passwords/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款数千家庭中广泛使用的 Wi-Fi 6 路由器被安全研究人员发现存在重大安全漏洞 —— 该**高危缺陷**允许攻击者绕过登录界面，夺取设备的完全控制权。

新加坡战略信息通信技术中心（Centre for Strategic Infocomm Technologies, CSIT）披露了 Linksys E9450-SG 路由器中的一个**零日漏洞**（漏洞编号：CVE-2025-52692）。这款设备于 2021 年由新加坡电信（Singtel）大规模配发，其存在的逻辑错误使得局域网内的任何人都能启用路由器的**隐藏 Telnet 服务器**，且**无需密码**。

报告指出：“消费级路由器是极具吸引力的攻击目标，因为它们直接暴露内部网络，且通常存在可被利用的漏洞。” 这也凸显了家庭网络安全的高风险性。

研究人员将重点放在了路由器的 Web 管理界面（设备设置的控制中心）。尽管该界面通常受密码保护，且仅对本地管理员开放，但研究团队找到了欺骗系统的方法。

该漏洞源于路由器解析 Web 请求的方式：研究人员发现，通过**篡改 URL**，无需进行任何身份验证即可访问受限制的端点。

具体而言，攻击者只需访问路径 `/LOGIN/API/obj/en_telnet`，就能跳过整个登录流程。

研究人员解释道：“请求 URL 的解析过程，以及后续相关 HTTP 请求的处理环节中存在一系列逻辑错误。这使得攻击者能够构造恶意请求，在没有有效凭据的情况下访问受身份验证保护的端点。”

一旦触发该特定 URL，路由器会**静默启用**其 Telnet 服务器 —— 这是一种老旧且未加密的远程控制协议。随着 Telnet 激活且身份验证被绕过，攻击者可直接登录，并以**最高权限**执行命令。

报告明确：“通过该漏洞启用 Telnet 服务器后，局域网内的攻击者可获取路由器的完全 root 命令行访问权限。”

届时，黑客可能窃听网络流量、安装恶意软件，或以此为跳板攻击家庭网络中的其他设备。

该漏洞已在 **1.2.00.052 版本固件**中得到验证，CSIT 指出这是 “该特定型号目前唯一已发布的固件版本”。

不过存在一个积极因素：该攻击默认情况下**无法通过互联网远程利用**。报告澄清：“攻击者必须能够访问路由器的管理 Web 界面，而该界面默认不会暴露在互联网上。” 这意味着威胁主要局限于已侵入受害者 Wi-Fi 网络的攻击者。

本文翻译自 securityonline [原文链接](https://securityonline.info/zero-day-alert-linksys-auth-bypass-lets-hackers-hijack-routers-without-passwords/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313984](/post/id/313984)

安全KER - 有思想的安全新媒体

本文转载自:  [securityonline](https://securityonline.info/zero-day-alert-linksys-auth-bypass-lets-hackers-hijack-routers-without-passwords/)

如若转载,请注明出处： <https://securityonline.info/zero-day-alert-linksys-auth-bypass-lets-hackers-hijack-routers-without-passwords/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **850**

* 粉丝
* **6**

### TA的文章

* ##### [慧与 OneView 产品高危漏洞（CVE-2025-37164）：可被用于远程代码执行](/post/id/314010)

  2025-12-24 15:06:42
* ##### [罗马尼亚水务部门证实遭遇网络攻击，核心供水系统未受影响](/post/id/314000)

  2025-12-24 15:05:40
* ##### [苹果公司因借隐私规则实施反垄断行为 在意大利被罚 9860 万欧元](/post/id/314005)

  2025-12-24 15:05:37
* ##### [谷歌推迟安卓端 Gemini AI 全面推送至 2026 年](/post/id/313994)

  2025-12-24 15:04:55
* ##### [人工智能初创公司奎尔特：仅用 40 小时人工投入，一周内完成 Linux 开发板设计](/post/id/313999)

  2025-12-24 15:04:21

### 相关文章

* ##### [慧与 OneView 产品高危漏洞（CVE-2025-37164）：可被用于远程代码执行](/post/id/314010)

  2025-12-24 15:06:42
* ##### [罗马尼亚水务部门证实遭遇网络攻击，核心供水系统未受影响](/post/id/314000)

  2025-12-24 15:05:40
* ##### [苹果公司因借隐私规则实施反垄断行为 在意大利被罚 9860 万欧元](/post/id/314005)

  2025-12-24 15:05:37
* ##### [谷歌推迟安卓端 Gemini AI 全面推送至 2026 年](/post/id/313994)

  2025-12-24 15:04:55
* ##### [人工智能初创公司奎尔特：仅用 40 小时人工投入，一周内完成 Linux 开发板设计](/post/id/313999)

  2025-12-24 15:04:21
* ##### [盲鹰黑客组织利用 PowerShell 脚本攻击政府机构](/post/id/313980)

  2025-12-24 15:03:36
* ##### [M-Files 身份窃取漏洞：高危缺陷致内部人员可劫持用户账户、获取敏感数据](/post/id/313972)

  2025-12-24 15:02:59

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