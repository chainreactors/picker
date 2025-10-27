---
title: WordPress LiteSpeed 缓存插件中的一个漏洞允许账户被接管
url: https://www.anquanke.com/post/id/299907
source: 安全客-有思想的安全新媒体
date: 2024-09-10
fetch_date: 2025-10-06T18:23:54.935472
---

# WordPress LiteSpeed 缓存插件中的一个漏洞允许账户被接管

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

# WordPress LiteSpeed 缓存插件中的一个漏洞允许账户被接管

阅读量**91434**

发布时间 : 2024-09-09 16:02:30

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/168145/security/litespeed-cache-plugin-wordpress-flaw.html>

译文仅供参考，具体内容表达以及含义原文为准。

## WordPress 的 LiteSpeed Cache 插件中的一个严重缺陷可能允许未经身份验证的用户控制任意帐户。

LiteSpeed Cache 插件是一种流行的 WordPress 缓存插件，活跃安装量超过 500 万次。该插件通过服务器级缓存和各种优化功能提供站点加速。

LiteSpeed Cache 插件受到未经身份验证的帐户接管漏洞的影响，该漏洞被跟踪为 CVE-2024-44000（CVSS 评分：7.5），该漏洞可能允许任何访客访问已登录的用户，并可能将权限升级到管理员级别。攻击者可以利用此漏洞上传恶意插件。

Patchstack 研究人员解释说，该漏洞源于 HTTP 响应标头泄漏，该泄漏在登录尝试后在调试日志文件 （） 中暴露了“Set-Cookie”标头。`/wp-content/debug.log`

未经身份验证的攻击者可以查看敏感信息，包括来自 HTTP 响应标头的用户 Cookie 数据。这可能使攻击者能够使用任何有效会话登录。只有当 WordPress 网站的调试功能处于启用状态并且默认情况下禁用此功能时，才能利用该漏洞。

*Patchstack 发布的报告写道：“该漏洞利用了调试日志文件上的 HTTP 响应标头泄漏，该漏洞还会在用户执行登录请求后泄漏”Set-Cookie“标头。“主要易受攻击的代码存在于 `ended` 的函数上”*

漏洞CVE-2024-44000影响6.4.1之前版本（含6.4.1）。此问题已在版本 6.5.0.1 中得到解决。

该插件背后的开发人员通过将日志文件移动到 LiteSpeed 插件文件夹 （“/wp-content/litespeed/debug/”） 中的专用文件夹、随机化文件名以及删除在文件中记录 cookie 的选项来修复该问题。

为了提高调试日志功能的安全性，研究人员还建议实施适当的规则来阻止直接访问日志文件。尽管 LiteSpeed 团队已经努力通过在补丁中应用此类规则来解决此问题，但它仍然不够。知道日志文件名称的用户仍然可以访问它，这表明当前规则需要进一步优化。`.htaccess`

专家还建议定期清除或删除旧文件中的内容，以避免未经授权访问文件中包含的先前泄露的 cookie 数据。`debug.log`

建议用户检查其安装中是否存在“/wp-content/debug.log”，如果已启用（或已经）启用调试功能，请采取措施清除它们。

此外，还建议设置 .htaccess 规则以拒绝对日志文件的直接访问，因为如果恶意行为者通过试错法知道新文件名，他们仍然可以直接访问新的日志文件。

*“此漏洞凸显了确保执行调试日志过程的安全性、不应记录哪些数据以及如何管理调试日志文件的极端重要性。一般来说，我们强烈建议不要使用插件或主题将与身份验证相关的敏感数据记录到调试日志文件中。“该报告总结道。“我们还强烈建议插件和主题开发人员将他们的调试日志数据正确存储在安全的调试日志文件中，并使用适当随机的日志文件名和额外的 .htaccess 规则来阻止直接访问。”*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/168145/security/litespeed-cache-plugin-wordpress-flaw.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299907](/post/id/299907)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/168145/security/litespeed-cache-plugin-wordpress-flaw.html)

如若转载,请注明出处： <https://securityaffairs.com/168145/security/litespeed-cache-plugin-wordpress-flaw.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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

* [WordPress 的 LiteSpeed Cache 插件中的一个严重缺陷可能允许未经身份验证的用户控制任意帐户。](#h2-0)

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