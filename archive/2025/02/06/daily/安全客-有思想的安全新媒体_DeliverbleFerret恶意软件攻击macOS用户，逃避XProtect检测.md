---
title: DeliverbleFerret恶意软件攻击macOS用户，逃避XProtect检测
url: https://www.anquanke.com/post/id/303829
source: 安全客-有思想的安全新媒体
date: 2025-02-06
fetch_date: 2025-10-06T20:34:31.034786
---

# DeliverbleFerret恶意软件攻击macOS用户，逃避XProtect检测

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

# DeliverbleFerret恶意软件攻击macOS用户，逃避XProtect检测

阅读量**363902**

发布时间 : 2025-02-05 15:26:28

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/flexibleferret-malware-attacking-macos-users/>

译文仅供参考，具体内容表达以及含义原文为准。

一种名为 “灵活雪貂”（FlexibleFerret）的新型恶意软件变体已被识别，它以 macOS 用户为目标，且能躲避苹果 XProtect 工具的检测。

该恶意软件是一场更大规模攻击活动的一部分，幕后黑手被认为是朝鲜的威胁行为者，他们一直采用复杂策略诱骗受害者安装恶意软件。

“雪貂” 恶意软件家族，包括 “冰冷雪貂\_用户界面”（FROSTYFERRET\_UI）和 “友好雪貂\_安全”（FRIENDLYFERRET\_SECD）等变体，于 2023 年 12 月首次被报道。

### SIEM 即服务

这些恶意软件组件与 “传染性面试” 攻击活动有关，在该活动中，威胁行为者将恶意软件伪装成虚拟面试所需软件，诱骗求职者安装。

#### “灵活雪貂” 恶意软件组件（来源：SentinelOne）

此外，SentinelOne 的网络安全专家发现，苹果最近更新了 XProtect 以阻止其中一些变体，但 “灵活雪貂” 仍未被检测到。

### “灵活雪貂” 分析

“灵活雪貂” 通过一个名为 versus.pkg 的苹果安装包进行传播，该安装包包含多个恶意组件，如 InstallerAlert.app、versus.app 以及一个名为 zoom 的独立二进制文件。

#### 安装后脚本执行（来源：SentinelOne）

安装后，postinstall.sh 脚本用于执行这些组件，并将执行进度记录到 /tmp/postinstall.log。

# Log the start of the script
echo “$(date): Running post-installation script…” >> /tmp/postinstall.log
# Check if the zoom file exists and execute it
if [ -f /var/tmp/zoom ]; then
echo “$(date): Zoom file exists, executing…” >>/tmp/postinstall.log
/var/tmp/zoom >> /tmp/postinstall.log 2>&1 &
else
echo “$(date): Zoom file not found” >> /tmp/postinstall.log
fi

名为 zoom 的虚假二进制文件会与域名 zoom.callservice [.] us 进行通信，而这并非合法的 Zoom 域名。

与此同时，InstallerAlert.app 通过显示一条错误消息，诱使用户认为它是一个合法应用程序，同时在用户的 “资源库 / LaunchAgents” 文件夹中秘密安装一个名为 com.zoom.plist 的常驻项。

#### InstallerAlert 错误消息（来源：SentinelOne）

“传染性面试” 攻击活动已从单纯针对求职者扩大到针对 GitHub 等平台上的开发者。威胁行为者利用合法代码库中的虚假问题来分发恶意软件释放器。

建议用户在从不可信来源安装软件时保持谨慎，并及时更新安全软件。

### 入侵指标（IoCs）

* versus.pkg：388ac48764927fa353328104d5a32ad825af51ce
* InstallerAlert Mach – Os：1a28013e4343fddf13e5c721f91970e942073b88，3e16c6489bac4ac2d76c555eb1c263cd7e92c9a5，76e3cb7be778f22d207623ce1907c1659f2c8215

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/flexibleferret-malware-attacking-macos-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303829](/post/id/303829)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/flexibleferret-malware-attacking-macos-users/)

如若转载,请注明出处： <https://cybersecuritynews.com/flexibleferret-malware-attacking-macos-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**9赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

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