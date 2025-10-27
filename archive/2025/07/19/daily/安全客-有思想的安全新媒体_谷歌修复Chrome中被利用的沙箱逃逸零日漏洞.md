---
title: 谷歌修复Chrome中被利用的沙箱逃逸零日漏洞
url: https://www.anquanke.com/post/id/310244
source: 安全客-有思想的安全新媒体
date: 2025-07-19
fetch_date: 2025-10-06T23:39:05.801882
---

# 谷歌修复Chrome中被利用的沙箱逃逸零日漏洞

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

# 谷歌修复Chrome中被利用的沙箱逃逸零日漏洞

阅读量**96970**

发布时间 : 2025-07-18 17:31:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-sandbox-escape-zero-day-in-chrome/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌已发布Chrome浏览器安全更新，修复包括一处被攻击者主动利用的漏洞在内的六个安全缺陷。

该漏洞编号为**CVE-2025-6558**，严重性评级为高**（CVSS分数8.8）**，由谷歌威胁分析团队（TAG）于6月23日发现。

该安全问题表现为ANGLE和GPU组件对不可信输入校验不足，影响Chrome版本低于138.0.7204.157。攻击者通过精心构造的HTML页面，可能成功实现逃逸浏览器沙箱保护的攻击。

ANGLE（Almost Native Graphics Layer Engine）是Chrome使用的开源图形抽象层，负责将OpenGL ES API调用转换为Direct3D、Metal、Vulkan和OpenGL。

由于ANGLE处理来自WebGL等不可信网站的GPU指令，该组件的漏洞可能带来极高的安全风险。

此漏洞允许远程攻击者通过特制HTML页面，在浏览器的GPU进程中执行任意代码。谷歌尚未公开触发漏洞并逃逸沙箱的具体技术细节。

谷歌安全公告指出：“在大部分用户完成更新前，漏洞细节和相关链接可能保持限制访问。”

“如果漏洞存在于其他项目同样依赖但尚未修复的第三方库中，限制措施也将持续。”

Chrome的沙箱机制是核心安全防护，隔离浏览器进程与操作系统，防止恶意软件通过浏览器扩散并危害设备安全。

鉴于**CVE-2025-6558**风险高且正被积极利用，建议Chrome用户尽快升级至138.0.7204.157/.158版本，具体取决于操作系统。

用户可通过访问 chrome://settings/help，等待自动检测更新并安装，更新完成后重启浏览器即可生效。

![]()

此次Chrome安全更新还修复了另外五个漏洞，其中包括V8引擎中的一个高危缺陷（编号**CVE-2025-7656**）和WebRTC中的一个使用后释放漏洞（编号**CVE-2025-7657**）。这五个漏洞均未被标记为正在被主动利用。

**CVE-2025-6558**是今年以来Chrome浏览器中发现并修复的第五个被积极利用的漏洞。

今年3月，谷歌修补了一个高危沙箱逃逸漏洞**CVE-2025-2783**，该漏洞由卡巴斯基研究人员发现，曾被用于针对俄罗斯政府机构和媒体组织的定向间谍攻击，传播恶意软件。

两个月后的5月，谷歌发布更新，修复了**CVE-2025-4664**，一个允许攻击者劫持用户账户的Chrome零日漏洞。

6月，公司又解决了另一个严重漏洞**CVE-2025-5419**，这是**Chrome V8 JavaScript**引擎中的越界读写漏洞，由谷歌威胁分析团队（TAG）的Benoît Sevens和Clément Lecigne报告。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-sandbox-escape-zero-day-in-chrome/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310244](/post/id/310244)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-sandbox-escape-zero-day-in-chrome/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/google-fixes-actively-exploited-sandbox-escape-zero-day-in-chrome/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**8赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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