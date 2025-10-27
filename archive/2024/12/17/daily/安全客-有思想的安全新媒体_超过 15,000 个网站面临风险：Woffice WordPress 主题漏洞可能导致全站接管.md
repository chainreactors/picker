---
title: 超过 15,000 个网站面临风险：Woffice WordPress 主题漏洞可能导致全站接管
url: https://www.anquanke.com/post/id/302733
source: 安全客-有思想的安全新媒体
date: 2024-12-17
fetch_date: 2025-10-06T19:34:47.214705
---

# 超过 15,000 个网站面临风险：Woffice WordPress 主题漏洞可能导致全站接管

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

# 超过 15,000 个网站面临风险：Woffice WordPress 主题漏洞可能导致全站接管

阅读量**53219**

|评论**1**

发布时间 : 2024-12-16 10:51:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/over-15000-sites-at-risk-woffice-wordpress-theme-vulnerabilities-could-lead-to-full-site-takeovers/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2024-43153 & CVE-2024-43234]()

Patchstack 在广泛使用的 Woffice WordPress 主题中披露了两个关键漏洞，该主题是一种高级内联网/外联网解决方案，销售量超过 15000 个。Woffice 主题由 Xtendify 开发，提供团队和项目管理功能，是高级业务工作流程的热门选择。然而，最近发现的这些漏洞被评为 CVSS 9.8 严重级别，给受影响的网站带来了巨大的安全风险。

Patchstack 在该主题功能所需的 Woffice Core 插件中发现了两个关键漏洞：

1. **权限升级漏洞 (CVE-2024-43153)：** 该漏洞允许未经身份验证的用户在受影响的网站上注册任何角色，包括权限极高的管理员角色。据报告称，“该漏洞可能导致攻击者完全接管网站并在服务器上安装恶意代码”。该问题存在于位于 inc/classes/Woffice\_Register.php 文件中的注册函数中。当启用 Woffice 的自定义登录选项（如自动登录和表单中的角色字段）时，攻击者可在 $\_POST[“reg\_role”] 参数中提交任意角色，从而获得更高的权限。
2. **未经身份验证的账户接管 (CVE-2024-43234)：** 该漏洞利用被破坏的身份验证机制，使攻击者能够在未经授权的情况下以任何现有用户的身份登录。该漏洞与同一 Woffice\_Register.php 文件中的 register\_redirect 函数有关。攻击者通过从自定义注册页面提取 WofficeRegisterRedirect 安全非密钥，并发送带有非密钥和 $\_POST[‘user\_id’] 设置为现有用户 ID（例如，管理员为 1）的请求，即可获得未经授权的访问权限。

这两个漏洞一旦被利用，可能会导致整个网站受到攻击，部署恶意代码，并给使用该主题的企业带来潜在的声誉和经济损失。

Woffice的开发商Xtendify已分别在5.4.12和5.4.15版本中解决了这些漏洞。我们强烈呼吁所有用户立即将其主题至少更新到 5.4.15 版本。

本文翻译自securityonline [原文链接](https://securityonline.info/over-15000-sites-at-risk-woffice-wordpress-theme-vulnerabilities-could-lead-to-full-site-takeovers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302733](/post/id/302733)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/over-15000-sites-at-risk-woffice-wordpress-theme-vulnerabilities-could-lead-to-full-site-takeovers/)

如若转载,请注明出处： <https://securityonline.info/over-15000-sites-at-risk-woffice-wordpress-theme-vulnerabilities-could-lead-to-full-site-takeovers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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