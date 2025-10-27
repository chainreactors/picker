---
title: 法庭录音平台 JAVS 遭遇供应链攻击
url: https://www.anquanke.com/post/id/296787
source: 安全客-有思想的安全新媒体
date: 2024-05-25
fetch_date: 2025-10-06T17:17:08.202231
---

# 法庭录音平台 JAVS 遭遇供应链攻击

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

# 法庭录音平台 JAVS 遭遇供应链攻击

阅读量**146226**

发布时间 : 2024-05-24 11:56:44

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.darkreading.com/cyberattacks-data-breaches/courtroom-recording-platform-javs-hijacked-for-supply-chain-attack>

译文仅供参考，具体内容表达以及含义原文为准。

Windows 版本的 RustDoor 安装程序正在通过受感染的视听软件包进行传播，该软件包由全国各地的法庭、监狱、议会、听证会和演讲厅使用的视听录制平台托管和分发。

Rapid7 的研究人员今天发布了有关供应链网络攻击活动的调查结果，称威胁行为者破坏了 Justice AV 的 Viewer v8.3.7，该程序用于访问 Justice AV 平台生成的媒体和日志文件。

报告称，一旦部署，RustDoor 安装程序将允许攻击者完全接管受感染的系统。研究人员解释说，Viewer“可以通过供应商的网站下载，并以基于 Windows 的安装程序包的形式提供，执行时会提示高权限”。

**Justice AV Solutions、RustDoor 的供应链攻击历史**

RustDoor 于 2023 年 12 月首次被发现，针对的是 macOS 机器。据发现该病毒的研究人员称，Windows 版本（也称为 GateDoor）不久后被发现，使用 Golang 而不是 Rust 编写。追溯其起源，RustDoor 和 GateDoor被部署在伪装成合法软件的供应链网络攻击中。过去的 RustDoor 活动与ALPHV/BlackCat 勒索软件组织有关。

JAVS Viewer 软件包的第一个恶意版本于 2 月 21 日出现，Rapid7 于 5 月 10 日首次开始对其进行调查。

JAVS 此后删除了损坏的查看器文件，并告诉 Rapid7，“在这次事件中，没有任何源代码、证书、系统或其他软件版本受到损害。”

Rapid7 建议，Justice AV Solutions 软件的客户不应只是删除和替换软件，而应完全重新映像受影响的端点，并重置凭据。研究人员警告称，JAVS Viewer v8.3.7 用户面临“高风险，应立即采取行动”。

尽管 RustDoor 恶意软件不再通过 JAVS 平台传播，但 Rapid7 指出，供应链攻击背后的对手正在不断更新和改进其命令和控制 (C2) 基础设施。

本文翻译自 [原文链接](https://www.darkreading.com/cyberattacks-data-breaches/courtroom-recording-platform-javs-hijacked-for-supply-chain-attack)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296787](/post/id/296787)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.darkreading.com/cyberattacks-data-breaches/courtroom-recording-platform-javs-hijacked-for-supply-chain-attack>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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