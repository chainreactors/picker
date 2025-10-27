---
title: PyPI 启用新防护机制：阻止利用“域名复活”进行的账户劫持攻击
url: https://www.anquanke.com/post/id/311362
source: 安全客-有思想的安全新媒体
date: 2025-08-21
fetch_date: 2025-10-07T00:47:38.980886
---

# PyPI 启用新防护机制：阻止利用“域名复活”进行的账户劫持攻击

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

# PyPI 启用新防护机制：阻止利用“域名复活”进行的账户劫持攻击

阅读量**62926**

发布时间 : 2025-08-20 17:53:06

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/pypi-now-blocks-domain-resurrection-attacks-used-for-hijacking-accounts/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Python 软件包索引（**PyPI**）近日引入了新的安全防护措施，以防御“域名复活攻击”——这种攻击方式可能通过密码重置劫持开发者账户。

作为开源 Python 软件包的官方仓库，PyPI 被广泛应用于软件开发者、项目维护者以及依赖 Python 库、工具和框架的企业。

在 **PyPI** 上发布软件的维护者账户通常与电子邮箱绑定，而部分邮箱则依赖于特定的域名。

一旦相关域名过期，攻击者即可重新注册该域名，并通过搭建邮件服务器发起密码重置，从而接管受害者在 **PyPI** 上的项目。

这一风险带来的后果是典型的供应链攻击：被劫持的项目可能被用来投放恶意版本的热门 Python 软件包，而这些软件包在许多情况下会被 pip 工具自动安装，从而造成大范围安全威胁。

2022 年 5 月，曾发生一起典型的“域名复活攻击”案例：攻击者成功入侵了 **“ctx”** 软件包，并在其中植入恶意代码，专门窃取 Amazon AWS 的密钥和账户凭证。

为应对此类风险，PyPI 现已开始对平台上已验证邮箱所依赖的域名进行检测，以判断其是否已经过期或即将进入过期阶段，并将相关邮箱标记为“未验证”。

在技术实现上，PyPI 使用 **Domainr 的 Status API** 来判定域名所处的生命周期阶段（如：活跃期、宽限期、赎回期、待删除期），从而决定是否需要对某个账户采取措施。一旦邮箱对应的域名进入这些状态，该邮箱将无法再用于密码重置或账户恢复，即使攻击者重新注册该域名，也无法利用其发起劫持。

![]()

这一新措施的研发始于 2025 年 4 月，当时 PyPI 首次开展了试探性扫描，以评估整体风险态势。最终在 2025 年 6 月，平台引入了每日扫描机制。截至目前，已有超过 **1,800 个邮箱地址** 在新系统下被标记为未验证。

虽然该措施并不能彻底杜绝所有攻击场景，但它显著降低了攻击者通过过期域名接管 PyPI 账户的风险。PyPI 同时建议用户在账户中添加非自定义域的备用邮箱，以避免可能的使用中断，并启用双重身份验证，以进一步增强账户防护能力。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/pypi-now-blocks-domain-resurrection-attacks-used-for-hijacking-accounts/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311362](/post/id/311362)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/pypi-now-blocks-domain-resurrection-attacks-used-for-hijacking-accounts/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/pypi-now-blocks-domain-resurrection-attacks-used-for-hijacking-accounts/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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