---
title: CISA警告：N-able N-central 平台漏洞被用于零日攻击
url: https://www.anquanke.com/post/id/311245
source: 安全客-有思想的安全新媒体
date: 2025-08-16
fetch_date: 2025-10-07T00:13:15.395944
---

# CISA警告：N-able N-central 平台漏洞被用于零日攻击

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

# CISA警告：N-able N-central 平台漏洞被用于零日攻击

阅读量**73550**

发布时间 : 2025-08-15 17:21:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Sergiu Gatlan，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/cisa-warns-of-n-able-n-central-flaws-exploited-in-zero-day-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）本周三发布警告称，**攻击者正积极利用 N-able 公司 N-central 远程监控与管理（RMM）平台中的两个安全漏洞发起零日攻击**。

N-central 是许多托管服务提供商（MSP）和企业 IT 部门常用的平台，用于**在中心化的网页控制台中管理客户的网络与设备**。

据 CISA 介绍，这两个漏洞分别涉及：

**· 反序列化处理不安全，允许经过身份认证的攻击者远程执行命令（CVE-2025-8875）**

**· 输入校验不足，可被利用进行命令注入（CVE-2025-8876）**

N-able 已证实这些漏洞目前已在实际攻击中被利用，并已在版本 N-central 2025.3.1 中发布补丁。同时，公司建议管理员尽快加固系统，以防漏洞详情曝光后被进一步利用。

N-able 在回应媒体 BleepingComputer 时表示：

> “安全调查显示，这类攻击主要出现在少数本地部署环境中，我们尚未发现 N-able 托管的云环境受到影响。”
>
> “所有本地部署客户必须升级到 N-central 2025.3.1。根据我们的安全政策，漏洞细节将在发布三周后公开。”

虽然 CISA 尚未公开相关攻击活动的细节，但目前没有证据表明这些漏洞被用于勒索软件攻击。

根据 Shodan 的搜索结果，全球大约有 **2000 个** N-central 实例暴露在公网（部分可能已经更新修复），其中主要分布在美国、澳大利亚和德国。

![]()

*在线暴露的 N-able N-central 设备（通过 Shodan 平台发现）*

CISA 已将这两个漏洞加入“已知被利用漏洞目录”（KEV Catalog），并要求美国联邦文职行政机构（FCEB）在 8 月 20 日之前完成修补，这是根据 2021 年 11 月发布的约束性运营指令 BOD 22-01 作出的要求。

虽然该指令主要面向美国联邦机构，CISA 仍鼓励所有组织（包括私营企业）优先修复这一被主动利用的漏洞：

> “请按照厂商指南尽快实施缓解措施，遵循 BOD 22-01 适用于云服务的指导；若无法实施缓解，则建议停止使用该产品。”

CISA 警告称，**这类漏洞经常成为恶意黑客的入侵入口，对联邦网络安全构成重大风险。**

就在上周，CISA 还发布了一项紧急指令，要求美国非军事政府机构在本周一上午 9 点（美东时间）前修复 Microsoft Exchange 混合部署中的一个关键漏洞（CVE-2025-53786）。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/cisa-warns-of-n-able-n-central-flaws-exploited-in-zero-day-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311245](/post/id/311245)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/cisa-warns-of-n-able-n-central-flaws-exploited-in-zero-day-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/cisa-warns-of-n-able-n-central-flaws-exploited-in-zero-day-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**0赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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