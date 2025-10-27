---
title: MediaTek 发布关键安全更新，全面修复多设备芯片组漏洞
url: https://www.anquanke.com/post/id/306263
source: 安全客-有思想的安全新媒体
date: 2025-04-09
fetch_date: 2025-10-06T22:03:45.558899
---

# MediaTek 发布关键安全更新，全面修复多设备芯片组漏洞

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

# MediaTek 发布关键安全更新，全面修复多设备芯片组漏洞

阅读量**54127**

发布时间 : 2025-04-08 10:27:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Guru Baran，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/mediatek-security-update-patch-for-vulnerabilities/>

译文仅供参考，具体内容表达以及含义原文为准。

MediaTek 发布了一项关键安全更新，旨在修复其芯片组中的多个漏洞。其中一个严重漏洞可能使攻击者在无需用户交互的情况下，远程在受影响设备上执行恶意代码。

今日发布的安全公告着重指出，这些漏洞会对众多设备构成重大安全风险，涉及智能手机、平板电脑、物联网设备、智能显示屏以及各类多媒体设备。

### ****严重漏洞详情****

此次安全更新主要针对 CVE-2025-20654 这一严重漏洞，它存在于多款 MediaTek 芯片组的无线局域网（WLAN）服务组件中。

该漏洞源于边界检查错误导致的越界写入问题，被归类为 CWE-787（越界写入）。

此漏洞可让攻击者在无需额外执行权限或用户交互的情况下实现远程代码执行。

受影响的芯片组包括广泛应用的 MT6890、MT7622、MT7915、MT7916、MT7981 和 MT7986 等。

受影响的软件版本涵盖：MT7622 和 MT7915 芯片组的 SDK 版本 7.4.0.1；MT7916、MT7981 和 MT7986 芯片组的 SDK 版本 7.6.7.0；以及 MT6890 芯片组的 OpenWrt 版本 19.07 和 21.02。

### ****其他安全隐患****

安全公告还提及了多个高严重级别的漏洞，如 CVE-2025-20655、CVE-2025-20656、CVE-2025-20657 和 CVE-2025-20658。

这些漏洞可能会在受影响设备的各个组件中引发远程代码执行、本地权限提升或拒绝服务等问题。

此外，还发现并修复了六个中等级别的漏洞（CVE-2025-20659 至 CVE-2025-20664）。

强烈建议使用受影响 MediaTek 芯片组的制造商仔细阅读完整的产品安全公告，并立即实施推荐的补丁。

终端用户应通过检查并安装可用更新，确保其设备运行的是最新固件版本。

此次安全更新体现了 MediaTek 持续致力于维护其技术生态系统的完整性和安全性，保护全球数百万台设备及其用户免受潜在攻击。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/mediatek-security-update-patch-for-vulnerabilities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306263](/post/id/306263)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/mediatek-security-update-patch-for-vulnerabilities/)

如若转载,请注明出处： <https://cybersecuritynews.com/mediatek-security-update-patch-for-vulnerabilities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**1赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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