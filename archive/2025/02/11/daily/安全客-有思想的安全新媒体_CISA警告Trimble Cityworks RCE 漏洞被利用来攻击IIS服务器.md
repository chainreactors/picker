---
title: CISA警告Trimble Cityworks RCE 漏洞被利用来攻击IIS服务器
url: https://www.anquanke.com/post/id/304021
source: 安全客-有思想的安全新媒体
date: 2025-02-11
fetch_date: 2025-10-06T20:34:55.516900
---

# CISA警告Trimble Cityworks RCE 漏洞被利用来攻击IIS服务器

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

# CISA警告Trimble Cityworks RCE 漏洞被利用来攻击IIS服务器

阅读量**281816**

发布时间 : 2025-02-10 11:09:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/cityworks-rce-iis-servers/>

译文仅供参考，具体内容表达以及含义原文为准。

美国网络安全与基础设施安全局（CISA）针对影响 Trimble Cityworks 的一个严重远程代码执行（RCE）漏洞发布了警告。Trimble Cityworks 是一款广泛应用于地方政府和公共工程资产管理的软件解决方案。

该漏洞编号为 CVE – 2025 – 0994，外部攻击者可利用一个反序列化缺陷，在客户的微软互联网信息服务（IIS）网络服务器上执行任意代码。

Trimble 已发布 Cityworks 的更新版本（15.8.9 和 23.10）来修复此漏洞。该公司敦促本地部署的客户立即安装更新。所有 Cityworks 在线（CWOL）部署已自动应用这些更新。

### ****针对目标 IIS 的远程代码执行****

此漏洞源于一个反序列化缺陷，攻击者可利用该缺陷在目标 IIS 网络服务器上实现远程代码执行（RCE）。

一旦成功利用此漏洞，攻击者可能未经授权访问敏感数据、扰乱关键服务，甚至有可能控制受影响的系统。

除了应用安全更新，Trimble 还建议客户检查并强化 IIS 身份权限。该公司注意到，一些本地部署的 IIS 身份权限可能过高。

为遵循安全最佳实践，IIS 不应以本地或域级别的管理员权限运行。有关如何更新 IIS 身份权限的详细说明，可在 Cityworks 支持门户的最新发行说明中找到。

CWOL 客户无需采取此行动，因为他们的 IIS 身份权限已正确配置。

Trimble 还建议检查附件目录配置。该公司建议，附件目录根配置应仅限于仅包含附件的文件夹 / 子文件夹，以防止潜在的安全风险。

在披露该漏洞的同时，Trimble 提供了一份入侵指标（IOC）列表，以帮助各机构检测潜在的利用尝试。

这些入侵指标包括与攻击相关的恶意文件的 SHA256 哈希值、文件路径、IP 地址和域名。

CISA 强烈建议 Cityworks 客户采取以下行动：

**1.应用最新安全更新**：尽快升级到 Cityworks 15.8.9 或 10 版本。

**2.检查并强化 IIS 身份权限**：确保 IIS 运行时不具备过多权限。

**3.验证附件目录配置**：将附件目录根配置限制为仅包含附件的文件夹 / 子文件夹。

**4.监控入侵指标**：利用提供的入侵指标检测网络内的潜在恶意活动。

有一个 Nuclei 模板可用于协助检测存在漏洞的实例。该模板提取存储在 HTML 主体中的版本信息，并判断是否存在 CVE – 2025 – 0994 漏洞。使用 Nuclei 模板的步骤如下：

1.下载 Nuclei。

2.将模板复制到本地系统。

3.运行命令：nuclei -u <https://yourHost.com>-t template.yaml。

CISA 鼓励各机构迅速采取行动，降低与 CVE – 2025 – 0994 相关的风险，并通过官方渠道及时了解 Trimble 发布的任何进一步更新或补丁信息。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/cityworks-rce-iis-servers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304021](/post/id/304021)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/cityworks-rce-iis-servers/)

如若转载,请注明出处： <https://cybersecuritynews.com/cityworks-rce-iis-servers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)

**+1**4赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [微软 Office 漏洞允许攻击者执行远程代码](/post/id/308412)

  2025-06-12 15:43:53
* ##### [人工智能可能修复帮助传播了 15 年的漏洞](/post/id/308401)

  2025-06-12 15:19:33
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [微软修补被阿联酋黑客利用的零日漏洞](/post/id/308384)

  2025-06-12 14:28:52
* ##### [西门子能源紧急警报：专用 5G 核心中的关键漏洞 (CVSS 9.9) 暴露了敏感数据！](/post/id/308380)

  2025-06-12 14:24:14
* ##### [Adobe 发布补丁修复 254 个漏洞，填补高严重性安全漏洞](/post/id/308359)

  2025-06-11 16:37:24
* ##### [Stealth Falcon 在复杂的网络间谍活动中利用新的零日漏洞 (CVE-2025-33053)](/post/id/308352)

  2025-06-11 16:12:52

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