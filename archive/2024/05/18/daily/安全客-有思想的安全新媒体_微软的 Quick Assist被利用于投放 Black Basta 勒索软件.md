---
title: 微软的 Quick Assist被利用于投放 Black Basta 勒索软件
url: https://www.anquanke.com/post/id/296580
source: 安全客-有思想的安全新媒体
date: 2024-05-18
fetch_date: 2025-10-06T16:48:26.658903
---

# 微软的 Quick Assist被利用于投放 Black Basta 勒索软件

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

# 微软的 Quick Assist被利用于投放 Black Basta 勒索软件

阅读量**133055**

发布时间 : 2024-05-17 11:23:39

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://www.scmagazine.com/news/microsofts-quick-assist-used-in-scam-to-drop-black-basta-ransomware>

译文仅供参考，具体内容表达以及含义原文为准。

威胁行为者正在滥用 Windows 中的 Quick Assist 客户端管理工具，并结合社会工程技巧，在受害者的系统上植入恶意软件和勒索软件。

在5 月 15 日的通报中，微软警告各组织警惕语音网络钓鱼 (vishing)骗局，网络犯罪分子会诱骗受害者打开 Quick Assist 会话。

自 4 月中旬以来，该供应商的威胁情报部门一直在监控一个名为 Storm-1811 的恶意行为者。该团伙使用远程监控和管理 (RMM) 工具来安装恶意软件，包括Qakbot、Cobalt Strike 以及最终的Black Basta 勒索软件。

该骗局通常始于 Storm-1811 对受害者发起 电子邮件轰炸攻击，通过使用其凭据间接注册订阅服务，使受害者的收件箱充满电子邮件。

然后，威胁行为者假装是技术支持人员给受害者打电话，并提出通过 Quick Assist 来解决他们的电子邮件过载问题，该工具默认安装在运行 Windows 11 的设备上。

微软的通报称：“一旦用户允许访问和控制，威胁行为者就会运行脚本化的 cURL 命令来下载一系列用于传递恶意负载的批处理文件或 ZIP 文件。”

“在一些情况下，微软威胁情报发现此类活动会导致下载 Qakbot、ScreenConnect 和 NetSupport Manager 等 RMM 工具以及 Cobalt Strike。”

安装初始工具并结束与受害者的电话通话后，Storm-1811 攻击者执行了进一步的“键盘操作”活动，包括域枚举和横向移动，然后使用 PsExec 在整个受感染网络中部署 Black Basta。

该咨询称：“自 Black Basta于 2022 年 4 月首次出现以来，Black Basta 攻击者在收到 Qakbot 和其他恶意软件分发者的访问权限后就部署了勒索软件，这凸显了组织需要在部署勒索软件之前关注攻击阶段，以减少威胁。” 。

“微软正在调查 Quick Assist 在这些攻击中的使用情况，并致力于提高帮助者和共享者之间的透明度和信任，并在 Quick Assist 中加入警告消息，以提醒用户可能存在技术支持诈骗。”

在上周的一篇文章中，Rapid7 的研究人员报告说，他们观察到同样的骗局被用来针对该网络安全公司的几位客户。

Rapid7 观察到的威胁行为者除了滥用 Quick Assist 之外，还尝试使用其他流行的 RMM 工具，包括 AnyDesk。

“虽然在 Rapid7 响应的任何案例中都没有观察到勒索软件的部署，但我们观察到的妥协指标之前与基于 OSINT（开源情报）和 Rapid7 处理的其他事件响应活动的 Black Basta 勒索软件运营商有关，”研究人员说。

微软表示，为了防止攻击，组织应考虑阻止或卸载 IT 部门未使用的 Quick Assist 和其他 RMM 工具。

它还建议培训员工警惕技术支持诈骗。

“仅当您通过直接联系 Microsoft 支持或您的 IT 支持人员发起交互时，才允许帮助者使用 Quick Assist 连接到您的设备。不要向任何声称迫切需要访问您的设备的人提供访问权限，”该建议称。

Rapid7 的进一步建议包括阻止与所有未经批准的 RMM 解决方案相关的域，并确保员工有权报告来自内部 IT 员工的可疑电话和短信。

本文翻译自 [原文链接](https://www.scmagazine.com/news/microsofts-quick-assist-used-in-scam-to-drop-black-basta-ransomware)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296580](/post/id/296580)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://www.scmagazine.com/news/microsofts-quick-assist-used-in-scam-to-drop-black-basta-ransomware>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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