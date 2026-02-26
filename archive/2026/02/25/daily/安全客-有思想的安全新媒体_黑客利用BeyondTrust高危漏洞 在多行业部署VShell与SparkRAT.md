---
title: 黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT
url: https://www.anquanke.com/post/id/314825
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:50.576465
---

# 黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT

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

# 黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT

阅读量**28138**

发布时间 : 2026-02-25 14:19:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/hackers-exploit-critical-beyondtrust-flaw-to-deploy-vshell-and-sparkrat-across-multiple-sectors/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款广泛使用的企业权限管理平台存在**高危安全漏洞**，目前正遭到黑客主动利用，网络安全研究机构与联邦机构均已发布紧急预警。

根据帕洛阿尔托网络公司 Unit 42 发布的最新威胁情报报告，**高级威胁组织**正大规模利用 BeyondTrust 远程协助软件中最新披露的安全漏洞，部署后门程序并窃取敏感数据。

该漏洞编号为 **CVE-2026-1731**，官方已于 2026 年 2 月 6 日在安全公告中详细披露。

作为主流的身份与权限管理平台，BeyondTrust 基础设施掌控着大量企业核心权限，使其成为网络犯罪分子眼中**极高价值的攻击目标**。

问题的核心在于，该软件会在用户登录**之前**就处理外部传入的连接。

Unit 42 报告指出：**该漏洞属于 BeyondTrust 远程协助软件中的预认证远程代码执行（RCE）漏洞**。

这意味着攻击者**无需有效凭据**即可攻陷目标系统。

研究人员还原出了已在真实攻击中被武器化的精确利用方式：

**通过操控 `remoteVersion` 参数，攻击者可绕过现有校验机制，并借助 `thin-scc-wrapper` 执行命令行指令。**

这使得攻击者能够以站点用户身份执行系统命令，**直接获取设备控制权**。

Unit 42 正在持续追踪该漏洞带来的影响，并指出相关利用并非理论演示，而是**已形成完整、规模化的攻击行动**。

攻击者利用 **CVE-2026-1731** 突破边界防护后，会迅速扩大攻击范围。调查人员已梳理出清晰的攻击链：

* 开展网络侦察，并创建恶意账户
* 部署网页后门（如 **VShell**）以维持持久化访问
* 建立命令与控制（C2）通信
* 部署远程管理工具与 **SparkRAT** 等后门程序
* 实施横向移动，深入受害者内网并窃取数据

此次攻击的影响范围已十分广泛，**美国、法国、德国、澳大利亚、加拿大**均已出现受害目标。

涉及行业包括：金融服务、法律服务、高科技、高等教育、批发零售、医疗健康等。

这一攻击面的危险程度无论如何强调都不为过，结合历史漏洞利用情况尤为明显。

Unit 42 报告提到，该软件此前存在的漏洞 **CVE-2024-12356**，曾被臭名昭著的国家级黑客组织 **Silk Typhoon（APT27/UNC5221/Emissary Panda）** 大规模利用，成功入侵包括美国财政部在内的多个高价值目标。

研究人员警告：**从历史情况来看，CVE-2026-1731 极有可能被高级威胁组织盯上，用于发起同类高权限攻击。**

意识到威胁迫在眉睫，美国网络安全与基础设施安全局（CISA）已于 **2026 年 2 月 13 日** 将 **CVE-2026-1731** 加入**已知被利用漏洞目录（KEV）**，要求联邦机构立即修复。

使用 BeyondTrust 相关产品的机构必须迅速行动。

SaaS 客户已于 2026 年 2 月 2 日前完成自动补丁更新，但**本地自建环境**若未及时维护仍处于高危状态。

建议管理员尽快升级：

* 本地版 Remote Support 升级至 **25.3.2 及以上版本**
* 本地版 Privileged Remote Access 升级至 **25.1.1 及以上版本**

  以此封堵这一高危**预认证权限绕过漏洞**。

本文翻译自securityonline [原文链接](https://securityonline.info/hackers-exploit-critical-beyondtrust-flaw-to-deploy-vshell-and-sparkrat-across-multiple-sectors/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314825](/post/id/314825)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/hackers-exploit-critical-beyondtrust-flaw-to-deploy-vshell-and-sparkrat-across-multiple-sectors/)

如若转载,请注明出处： <https://securityonline.info/hackers-exploit-critical-beyondtrust-flaw-to-deploy-vshell-and-sparkrat-across-multiple-sectors/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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