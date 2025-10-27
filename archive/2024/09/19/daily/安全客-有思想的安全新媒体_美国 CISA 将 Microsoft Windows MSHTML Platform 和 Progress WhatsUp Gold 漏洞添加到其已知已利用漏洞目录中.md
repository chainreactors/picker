---
title: 美国 CISA 将 Microsoft Windows MSHTML Platform 和 Progress WhatsUp Gold 漏洞添加到其已知已利用漏洞目录中
url: https://www.anquanke.com/post/id/300145
source: 安全客-有思想的安全新媒体
date: 2024-09-19
fetch_date: 2025-10-06T18:24:11.894732
---

# 美国 CISA 将 Microsoft Windows MSHTML Platform 和 Progress WhatsUp Gold 漏洞添加到其已知已利用漏洞目录中

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

# 美国 CISA 将 Microsoft Windows MSHTML Platform 和 Progress WhatsUp Gold 漏洞添加到其已知已利用漏洞目录中

阅读量**92214**

发布时间 : 2024-09-18 15:01:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/168505/security/u-s-cisa-microsoft-windows-mshtml-platform-progress-whatsup-gold-bugs-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 美国网络安全和基础设施安全局 （CISA） 将 Microsoft Windows MSHTML Platform 和 Progress WhatsUp Gold 错误添加到其已知被利用漏洞目录中。

美国网络安全和基础设施安全局 （CISA） 将 SonicWall、SonicOS、ImageMagick 和 Linux 内核漏洞添加到其已知利用漏洞 （KEV） 目录中。

以下是这些漏洞的描述：

* CVE-2024-43461：Microsoft Windows MSHTML 平台欺骗漏洞
* CVE-2024-6670：Progress WhatsUp Gold SQL 注入漏洞

CVE-2024-43461 – Microsoft 本周**警告**说，攻击者在 2024 年 7 月之前将 Windows 漏洞 CVE-2024-43461 作为零日漏洞积极利用。

漏洞 CVE-2024-43461 是一个 Windows MSHTML 平台欺骗问题。MSHTML 是 Internet Explorer 使用的平台。尽管浏览器已停用，但 MSHTML 仍保留在 Windows 中，并且仍由某些应用程序使用。

ZDI 威胁搜寻团队发现了一个新的漏洞，类似于之前修补的 7 月漏洞，该漏洞被跟踪为 CVE-2024-38112。

*“此漏洞允许远程攻击者在受影响的 Microsoft Windows 安装上执行任意代码。利用此漏洞需要用户交互，因为目标必须访问恶意页面或打开恶意文件。“Internet Explorer 在下载文件后提示用户的方式中存在特定缺陷。构建的文件名可能会导致隐藏真实的文件扩展名，从而误导用户认为该文件类型是无害的。攻击者可以利用此漏洞在当前用户的上下文中执行代码。*

尽管在 6 月份向 Microsoft 报告了它，但威胁行为者很快就想出了一种绕过补丁的方法。尽管被积极使用，但 Microsoft 并未将其标记为受到攻击。该漏洞会影响所有受支持的 Windows 版本。

*“是的。CVE-2024-43461 在 2024 年 7 月之前被作为与 CVE-2024-38112 相关的攻击链的一部分被利用Microsoft。“我们在 2024 年 7 月的安全更新中发布了 CVE-2024-38112 的修复程序，该修复程序打破了这一攻击链。请参阅 [CVE-2024-38112 – 安全更新指南 – Microsoft – Windows MSHTML 平台欺骗漏洞[（https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38112）。客户应同时更新 2024 年 7 月和 2024 年 9 月的安全更新，以充分保护自己。*

2024 年 9 月的 Patch Tuesday 安全更新解决了 CVE-2024-43461 漏洞。

WhatsUp Gold 中的漏洞 CVE-2024-6670 是 SQL 注入身份验证绕过问题。

未经身份验证的攻击者可能会触发此漏洞以检索用户的加密密码。该漏洞会影响 2024.0.0 之前发布的 WhatsUp Gold 版本。

根据具有约束力的操作指令 （BOD） 22-01：降低已知被利用漏洞的重大风险，FCEB 机构必须在截止日期前解决已识别的漏洞，以保护其网络免受利用目录中缺陷的攻击。

专家还建议私营组织查看 Catalog 并解决其基础设施中的漏洞。

CISA 命令联邦机构在 2024 年 10 月 7 日之前修复此漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/168505/security/u-s-cisa-microsoft-windows-mshtml-platform-progress-whatsup-gold-bugs-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300145](/post/id/300145)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/168505/security/u-s-cisa-microsoft-windows-mshtml-platform-progress-whatsup-gold-bugs-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/168505/security/u-s-cisa-microsoft-windows-mshtml-platform-progress-whatsup-gold-bugs-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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

* [美国网络安全和基础设施安全局 （CISA） 将 Microsoft Windows MSHTML Platform 和 Progress WhatsUp Gold 错误添加到其已知被利用漏洞目录中。](#h2-0)

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