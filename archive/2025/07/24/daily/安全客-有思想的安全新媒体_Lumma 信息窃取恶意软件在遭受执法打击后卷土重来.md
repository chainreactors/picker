---
title: Lumma 信息窃取恶意软件在遭受执法打击后卷土重来
url: https://www.anquanke.com/post/id/310417
source: 安全客-有思想的安全新媒体
date: 2025-07-24
fetch_date: 2025-10-06T23:16:53.936077
---

# Lumma 信息窃取恶意软件在遭受执法打击后卷土重来

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

# Lumma 信息窃取恶意软件在遭受执法打击后卷土重来

阅读量**62662**

发布时间 : 2025-07-23 17:16:46

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-returns-after-law-enforcement-disruption/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络安全研究人员发现，Lumma信息窃取木马在5月遭遇大规模执法打击后，**近期活动正逐步恢复**。此次执法行动查封了该团伙2300个域名及部分基础设施。

尽管这次执法行动对Lumma的MaaS（ malware-as-a-service）平台造成重大打击，但据6月初报告显示，该平台并未完全关闭。运营者随即在XSS论坛上承认情况，但声称其**核心服务器虽被远程擦除数据但未被查封，并已开始恢复工作**。

![]()

*执法行动后Lumma管理员的首条消息*
*来源：趋势科技*

趋势科技分析师指出，Lumma的活动水平已接近打击前的状态，该公司的监测数据显示其基础设施正在快速重建。”在针对Lumma窃密木马及其相关基础设施的执法行动后，我们的团队已观察到其运营明显复苏的迹象，”趋势科技报告称，”网络监测数据显示，**Lumma的基础设施在打击行动后数周内就开始重新活跃**。”

![]()

*新的Lumma C2 域名*
*来源：趋势科技*

目前，Lumma仍在使用**合法云基础设施**来隐藏恶意流量，但已从Cloudflare转向其他服务商，特别是Selectel，以避免再次被查封。

该恶意软件主要通过四种渠道传播：

**1. 虚假破解软件**：通过恶意广告和搜索引擎优化手段传播仿冒软件破解程序，诱导用户下载包含恶意代码的”Lumma Downloader”

**2. ClickFix欺诈**：在遭劫持网站展示虚假验证页面，诱骗用户执行恶意PowerShell命令实现内存驻留

**3. GitHub平台滥用**：创建包含AI生成内容的代码仓库，以”游戏辅助工具”为名分发”TempSpoofer.exe”等恶意载荷

**4. 社交媒体传播**：通过YouTube视频和Facebook帖子推广含恶意代码的破解软件，并冒用Google Sites等可信服务增强迷惑性

![]()

*分发Lumma恶意程序载荷的恶意 GitHub 仓库（左）和 YouTube 视频（右）*
*来源：趋势科技*

Lumma的卷土重来表明，在缺乏对犯罪嫌疑人实施抓捕或起诉的情况下，单纯的技术打击难以彻底遏制此类高收益的网络犯罪活动。MaaS运营者通常将执法部门的打击行动**视为常规运营风险**予以应对。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-returns-after-law-enforcement-disruption/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310417](/post/id/310417)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-returns-after-law-enforcement-disruption/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-returns-after-law-enforcement-disruption/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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