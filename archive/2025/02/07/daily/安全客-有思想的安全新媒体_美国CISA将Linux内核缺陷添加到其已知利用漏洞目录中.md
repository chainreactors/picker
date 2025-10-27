---
title: 美国CISA将Linux内核缺陷添加到其已知利用漏洞目录中
url: https://www.anquanke.com/post/id/303883
source: 安全客-有思想的安全新媒体
date: 2025-02-07
fetch_date: 2025-10-06T20:33:44.593778
---

# 美国CISA将Linux内核缺陷添加到其已知利用漏洞目录中

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

# 美国CISA将Linux内核缺陷添加到其已知利用漏洞目录中

阅读量**307380**

发布时间 : 2025-02-06 11:22:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs 2

原文地址：<https://securityaffairs.com/173897/hacking/u-s-cisa-adds-linux-kernel-flaw-to-its-known-exploited-vulnerabilities-catalog.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

美国网络安全与基础设施安全局（CISA）将 Linux 内核漏洞纳入其已知被利用漏洞目录。

美国网络安全与基础设施安全局（CISA）把一个追踪编号为 CVE – 2024 – 53104 的 Linux 内核漏洞，添加到了其已知被利用漏洞（KEV）目录中。

2025 年 2 月的安卓安全更新修复了 48 个漏洞，其中包括零日漏洞 CVE – 2024 – 53104，该漏洞在实际攻击中已被积极利用。

谷歌的公告中写道：“有迹象表明，CVE – 2024 – 53104 可能正遭受有限的、有针对性的利用。”

和往常一样，谷歌并未透露利用上述漏洞进行攻击的细节。

该漏洞是内核 USB 视频类驱动中的一个权限提升安全缺陷。已认证的本地攻击者可以在低复杂度的攻击中利用此缺陷提升权限。

该问题源于对 UVC\_VS\_UNDEFINED 帧的解析不当，导致对帧缓冲区大小的计算错误，并有可能引发任意代码执行或拒绝服务攻击。

安全公告中写道：“在 Linux 内核中，以下漏洞已得到修复：media: uvcvideo: 在 uvc\_parse\_format 中跳过对 UVC\_VS\_UNDEFINED 类型帧的解析。由于在 uvc\_parse\_streaming 中计算帧缓冲区大小时未考虑这种类型的帧，这可能导致越界写入。”

根据《约束性操作指令（BOD）22 – 01：降低已知被利用漏洞的重大风险》，联邦民用执行部门（FCEB）各机构必须在截止日期前修复已识别的漏洞，以保护其网络免受利用该目录中漏洞的攻击。

专家们还建议私营企业查看该目录，并修复其基础设施中的相关漏洞。

CISA 命令联邦机构在 2025 年 2 月 26 日前修复此漏洞。

本文翻译自securityaffairs 2 [原文链接](https://securityaffairs.com/173897/hacking/u-s-cisa-adds-linux-kernel-flaw-to-its-known-exploited-vulnerabilities-catalog.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303883](/post/id/303883)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs 2](https://securityaffairs.com/173897/hacking/u-s-cisa-adds-linux-kernel-flaw-to-its-known-exploited-vulnerabilities-catalog.html)

如若转载,请注明出处： <https://securityaffairs.com/173897/hacking/u-s-cisa-adds-linux-kernel-flaw-to-its-known-exploited-vulnerabilities-catalog.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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