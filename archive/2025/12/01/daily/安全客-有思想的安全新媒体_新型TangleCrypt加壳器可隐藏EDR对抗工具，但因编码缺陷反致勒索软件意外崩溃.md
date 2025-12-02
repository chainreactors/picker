---
title: 新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃
url: https://www.anquanke.com/post/id/313501
source: 安全客-有思想的安全新媒体
date: 2025-12-01
fetch_date: 2025-12-02T03:17:04.680834
---

# 新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃

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

# 新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃

阅读量**24075**

发布时间 : 2025-12-01 17:48:27

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/new-tanglecrypt-packer-hides-edr-killer-but-coding-flaws-cause-ransomware-to-crash-unexpectedly/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在勒索软件的高风险博弈中，威胁者不断优化伪装手段。WithSecure 旗下 STINGR 小组的最新报告披露了一款名为“**TangleCrypt**”的新型恶意软件打包器，该工具在近期麒麟（Qilin）勒索软件攻击调查中被首次发现。尽管它采用先进加密技术隐藏“EDR 杀手”，但分析师发现其代码存在大量缺陷，可能导致恶意软件意外崩溃。

此次发现源于 2025 年 9 月初的一起事件：调查人员在加密开始前恢复了用于瘫痪防御系统的攻击组件。该打包器被用于隐藏 **STONESTOP**——一个专门用于强制终止安全软件的可执行文件。

分析显示：“打包器存在于近期勒索软件攻击中使用的两个可执行文件中，其 payload 均被识别为 EDR 杀手 STONESTOP，该工具利用恶意驱动 **ABYSSWORKER** 实现功能。”

STONESTOP 的工作原理是注册内核驱动 ABYSSWORKER，将其伪装成合法组件。在此次攻击活动中，恶意驱动被发现“伪装成 CrowdStrike Falcon Sensor 驱动”。激活后，恶意软件“包含可执行文件名称列表，并通过驱动终止所有匹配列表项的运行进程”。

TangleCrypt 得名于其复杂的多层混淆方法：它并非将数据附加在文件末尾，而是将恶意载荷深度嵌入文件的 **资源节（PE Resources）** 中。

WithSecure 研究人员详细描述了混淆链：“payload 通过 **Base64 编码、LZ78 压缩和 XOR 加密** 多层嵌套存储在 PE 资源中。”

该打包器最显著的特性之一是灵活性——攻击者可通过代码中隐藏的简单配置字符串决定恶意软件的运行方式。“加载器支持两种 payload 启动方法：在同一进程中或子进程中。”研究人员证实，“所选方法由附加在嵌入式 payload 后的字符串定义”，使威胁者能轻松切换注入技术。

尽管具备先进的隐身特性，TangleCrypt 显然仍处于 **开发阶段**。分析显示，恶意软件开发者在重新实现标准 Windows 函数时犯了关键错误，导致稳定性问题。

“虽然打包器整体设计有趣，但我们在加载器实现中发现了多个缺陷，可能导致 payload 崩溃或出现其他意外行为。”

一个典型缺陷与恶意软件处理管理员权限的方式有关：若在无必要权限的情况下执行，打包器无法正确初始化特定环境变量，进而自我销毁。“加载器实现中的不一致可能导致某些打包后的可执行文件行为异常，这或许解释了为何 TangleCrypt 在野外尚未广泛出现。”

TangleCrypt 的发现成为网络犯罪地下市场工具质量差异的典型案例：尽管加密概念合理，但执行过程暴露了 **缺乏严格测试** 的问题。

“然而，这也凸显了恶意软件开发能力的参差不齐：快速开发、有限测试和普遍的粗心可能引入漏洞，最终降低其有效性。”

对防御者而言，TangleCrypt 的出现强化了 **超越已知文件签名检测** 的必要性。“随着 EDR 杀手及其支持基础设施的不断演变，防御者不仅要应对复杂技术，还需警惕真实攻击中可能出现的快速迭代但不完善的实现。”

本文翻译自securityonline [原文链接](https://securityonline.info/new-tanglecrypt-packer-hides-edr-killer-but-coding-flaws-cause-ransomware-to-crash-unexpectedly/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313501](/post/id/313501)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/new-tanglecrypt-packer-hides-edr-killer-but-coding-flaws-cause-ransomware-to-crash-unexpectedly/)

如若转载,请注明出处： <https://securityonline.info/new-tanglecrypt-packer-hides-edr-killer-but-coding-flaws-cause-ransomware-to-crash-unexpectedly/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **760**

* 粉丝
* **6**

### TA的文章

* ##### [Devolutions Server 中存在严重漏洞（CVE-2025-13757），已认证的攻击者可利用SQL注入窃取所有存储的密码](/post/id/313498)

  2025-12-01 17:48:48
* ##### [新型TangleCrypt加壳器可隐藏EDR对抗工具，但因编码缺陷反致勒索软件意外崩溃](/post/id/313501)

  2025-12-01 17:48:27
* ##### [GeoServer 中存在高危漏洞（CVE-2025-58360），可利用未授权的XXE攻击实现文件窃取与服务端请求伪造](/post/id/313505)

  2025-12-01 17:48:01
* ##### [新型恶意软件即服务运营商 TAG-150 利用 ClickFix 诱饵及自定义 CastleLoader，已入侵美国境内 469 台设备](/post/id/313509)

  2025-12-01 17:47:16
* ##### [OpenAI在ChatGPT安卓测试版中启动广告功能测试，引发用户对数据隐私的担忧](/post/id/313514)

  2025-12-01 17:46:49

### 相关文章

* ##### [Devolutions Server 中存在严重漏洞（CVE-2025-13757），已认证的攻击者可利用SQL注入窃取所有存储的密码](/post/id/313498)

  2025-12-01 17:48:48
* ##### [GeoServer 中存在高危漏洞（CVE-2025-58360），可利用未授权的XXE攻击实现文件窃取与服务端请求伪造](/post/id/313505)

  2025-12-01 17:48:01
* ##### [新型恶意软件即服务运营商 TAG-150 利用 ClickFix 诱饵及自定义 CastleLoader，已入侵美国境内 469 台设备](/post/id/313509)

  2025-12-01 17:47:16
* ##### [OpenAI在ChatGPT安卓测试版中启动广告功能测试，引发用户对数据隐私的担忧](/post/id/313514)

  2025-12-01 17:46:49
* ##### [美国CISA已将OpenPLC ScadaBR系统中正遭积极利用的XSS漏洞（CVE-2021-26829）列入其关键漏洞目录](/post/id/313517)

  2025-12-01 17:46:23
* ##### [“哈希劫持”攻击手法通过操纵URL片段标识符（#）来操控AI浏览器的行为](/post/id/313521)

  2025-12-01 17:45:53
* ##### [“河内窃贼”攻击行动：黑客利用伪多语言LNK/图像混合文件，通过DLL侧加载投送LOTUSHARVEST窃密木马](/post/id/313495)

  2025-12-01 17:45:09

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