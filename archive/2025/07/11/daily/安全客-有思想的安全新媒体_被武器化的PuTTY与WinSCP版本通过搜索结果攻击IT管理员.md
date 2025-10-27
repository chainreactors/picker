---
title: 被武器化的PuTTY与WinSCP版本通过搜索结果攻击IT管理员
url: https://www.anquanke.com/post/id/309727
source: 安全客-有思想的安全新媒体
date: 2025-07-11
fetch_date: 2025-10-06T23:16:32.011632
---

# 被武器化的PuTTY与WinSCP版本通过搜索结果攻击IT管理员

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

# 被武器化的PuTTY与WinSCP版本通过搜索结果攻击IT管理员

阅读量**69540**

发布时间 : 2025-07-10 16:19:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/trojan-versions-of-putty-and-winscp/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场针对系统管理员的**复杂搜索引擎优化（SEO）投毒及恶意广告活动**浮出水面，其借助带有后门的恶意软件实施攻击。

Arctic Wolf安全研究人员发现，自2025年6月初以来，一场危险的搜索引擎优化投毒与恶意广告活动持续针对着**IT专业人员**。

该活动利用虚假网站托管植入木马的热门IT工具（特别是**PuTTY和WinSCP**），在受害者系统上安装后门恶意软件。

##### ****活动概述****

此恶意活动通过操纵搜索引擎，推广模仿正规软件仓库的**虚假下载站点**。当IT专业人员搜索这些必备工具时，会看到赞助广告和被投毒的搜索结果，这些结果会**将其重定向至攻击者控制的域名**。

主要目标工具包括：

* **PuTTY：**一款用于安全远程连接的热门SSH客户端
* **WinSCP：**一款用于安全文件传输的SFTP/FTP客户端

##### ****攻击技术细节****

受害者下载并执行植入木马的安装程序后，会在不知情的情况下安装名为**Oyster/Broomstick**的复杂后门。该恶意软件采用**高级持久化机制**，对企业环境构成严重威胁。

后门通过以下方式实现持久化：

1. **每三分钟执行一次的计划任务**
2. **通过exe执行恶意DLL（twain\_96.dll）**
3. **利用DllRegisterServer导出函数进行DLL注册**

该活动专门针对**IT专业人员和系统管理员**，因为这些用户在企业网络中通常拥有**高级权限**。这使其成为威胁actors的重要目标，攻击者旨在：

1. 在**企业网络**中快速传播
2. 访问组织**敏感数据**
3. 控制**域控制器**
4. 部署**额外恶意软件载荷**，包括勒索软件

此次攻击利用了IT专业人员频繁下载管理工具的需求，使得社会工程学手段尤为奏效。许多管理员依赖**搜索引擎快速查找软件**，这为攻击者创造了通过恶意结果拦截搜索的机会。

Arctic Wolf已识别出与该活动相关的多个域名，各组织应**立即屏蔽**：

* **updaterputty[.]com**
* **zephyrhype[.]com**
* **putty[.]run**
* **putty[.]bet**
* **puttyy[.]org**

##### ****给组织的建议****

* **实施可信软件获取规范：**

1. 禁止员工使用搜索引擎查找管理工具
2. 建立经过审核的内部软件仓库
3. 要求直接访问官方供应商网站
4. 实施严格的IT工具下载政策

* **部署网络级防护：**

1. 在防火墙层面屏蔽已识别的恶意域名
2. 实施DNS过滤，防止访问已知恶意域名
3. 监控可疑计划任务和DLL执行情况
4. 部署端点检测与响应（EDR）解决方案

该活动标志着针对IT基础设施的定向攻击出现了令人担忧的新变化。类似的搜索引擎优化投毒活动已大幅增加，网络安全专家指出，**2024年相关攻击增幅达103%**。

对必备IT工具的攻击表明，威胁actors正不断调整策略，利用受害者的日常工作流程实施攻击。

此次活动的发现凸显了**实施强健网络安全措施的极端重要性**，尤其是在**软件获取和端点防护**方面。各组织必须保持警惕，因为攻击者正持续改进技术，以绕过传统安全措施，并将目标对准那些负责维护网络安全的专业人员。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/trojan-versions-of-putty-and-winscp/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309727](/post/id/309727)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/trojan-versions-of-putty-and-winscp/)

如若转载,请注明出处： <https://cybersecuritynews.com/trojan-versions-of-putty-and-winscp/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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