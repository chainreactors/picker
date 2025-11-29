---
title: 遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态
url: https://www.anquanke.com/post/id/313453
source: 安全客-有思想的安全新媒体
date: 2025-11-28
fetch_date: 2025-11-29T03:11:27.038875
---

# 遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态

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

# 遗留Python包中的代码漏洞，可通过劫持其依赖域名进而危及整个PyPI软件生态

阅读量**12780**

发布时间 : 2025-11-28 18:00:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/vulnerable-codes-in-legacy-python-packages/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

遗留代码中的 **隐藏漏洞** 常为现代开发环境带来无形风险。

Python 生态系统近期就暴露了此类问题：与 **zc.buildout 工具** 相关的过时引导脚本使用户面临 **域名劫持攻击** 风险。这些用于自动安装包依赖的脚本包含 **硬编码的外部域名引用**，而这些域名已不再受原维护者控制。

![]()

问题核心在于脚本的特定行为：它们会尝试从 `python-distribute[.]org` 获取已弃用的 `distribute` 包。该域名自 2014 年起被遗弃，目前处于停放状态且可被购买。若威胁行为者收购此域名，即可分发恶意 payload，任何运行受影响引导脚本的开发者都会 **自动下载并执行恶意代码**。这为供应链攻击提供了直接路径，可绕过标准安全检查。

### 受影响范围与触发条件

ReversingLabs 安全分析师发现，此漏洞影响多个知名包，包括 **slapos.core 、pypiserver 和 tornado**。尽管许多开发者已迁移至新版本打包标准，但这些遗留文件仍常存在于代码库中。

漏洞不会在标准 `pip install` 过程中触发，通常需通过手动执行或构建流程（如 Makefile）调用。一旦激活，脚本会 **盲目信任外部源**，造成类似于 npm 仓库中 `fsevents` 事件的重大供应链风险。

### 执行机制分析

![]()

该漏洞的技术核心在于引导脚本处理依赖解析的不安全方式：代码逻辑会检查 `distribute` 包是否存在，若未找到，则使用 Python 内置 `urllib` 库启动下载例程。如上图所示，`bootstrap.py` 会从已失效的 `python-distribute[.]org` 获取并执行 `distribute` 安装程序，且 **直接将 URL 响应传递给 exec() 函数**，未经任何完整性检查或签名验证即立即运行代码。

![]()

为验证攻击向量，研究人员针对 `slapos.core` 构建了概念验证（PoC）漏洞利用脚本。该 PoC 通过操纵命令行参数迫使脚本进入易受攻击的下载路径，终端输出结果证实脚本成功连接外部域名，表明托管于该域名的任何代码都将以 **用户完全权限** 执行。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/vulnerable-codes-in-legacy-python-packages/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313453](/post/id/313453)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/vulnerable-codes-in-legacy-python-packages/)

如若转载,请注明出处： <https://cybersecuritynews.com/vulnerable-codes-in-legacy-python-packages/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **750**

* 粉丝
* **6**

### TA的文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22

### 相关文章

* ##### [大规模npm供应链攻击“亡命开关”正驱动恶意软件攻击，其持久化机制依赖特定激活条件](/post/id/313473)

  2025-11-28 18:08:08
* ##### [GitLab发布安全更新，修复可导致认证绕过与拒绝服务攻击的多重漏洞](/post/id/313477)

  2025-11-28 18:07:38
* ##### [Apache SkyWalking 中存在漏洞，可导致攻击者发起跨站脚本攻击](/post/id/313482)

  2025-11-28 18:07:08
* ##### [Next.js服务器存在未授权拒绝服务漏洞，单次请求即可致服务崩溃](/post/id/313486)

  2025-11-28 18:05:53
* ##### [高级威胁“Shai Hulud”升级至v2版本，利用GitHub Actions工作流作为攻击载体窃取敏感机密](/post/id/313468)

  2025-11-28 18:04:22
* ##### [逾390个被弃用的iCalendar同步域名存在安全隐患，可能导致近400万台设备暴露于安全风险之下](/post/id/313462)

  2025-11-28 18:02:37
* ##### [纳闽再保险启用绿色数据中心，实现效能提升与运营成本优化](/post/id/313459)

  2025-11-28 18:00:45

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