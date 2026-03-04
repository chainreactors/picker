---
title: 黑客如何将Windows文件管理器变为远程控制木马的隐蔽入口
url: https://www.anquanke.com/post/id/314921
source: 安全客-有思想的安全新媒体
date: 2026-03-03
fetch_date: 2026-03-04T04:01:53.278903
---

# 黑客如何将Windows文件管理器变为远程控制木马的隐蔽入口

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

# 黑客如何将Windows文件管理器变为远程控制木马的隐蔽入口

阅读量**25484**

发布时间 : 2026-03-03 10:03:07

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-explorer-trap-how-hackers-turn-windows-file-explorer-into-a-silent-portal-for-remote-access-trojans/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Cofense Intelligence 安全研究人员发现了一类**隐蔽性持续增强**的恶意软件传播活动，其攻击过程**完全绕过传统浏览器**。攻击者利用 Windows 中一项被忽视的旧版协议，将用户熟悉的**Windows 文件资源管理器**变成了隐蔽通道，用于投放极具破坏力的**远程控制木马（RAT）**。

此次攻击的核心，是滥用 \*\*WebDAV（基于 Web 的分布式创作与版本控制）\*\* 协议。

Cofense 在报告中指出：“研究团队持续监测到，攻击者正在滥用 Windows 文件资源管理器通过 WebDAV 协议加载远程文件的能力，借助这种基于 HTTP 的文件管理协议，诱骗用户下载恶意程序。”

WebDAV 是一套基于 HTTP 运行的旧式文件管理协议。尽管如今已被现代云存储方案大量替代，但**Windows 文件资源管理器仍原生支持**，可用于访问远程文件服务器。黑客正是看中了这种系统级集成能力，将其作为完美伪装。

![]()

当受害者被诱导打开 WebDAV 链接（通常伪装成无害的`.url`或`.lnk`快捷方式）时，文件资源管理器会弹出一个**与本地文件夹完全一致**的窗口。

危险之处在于用户心理：Cofense 提到，**在文件资源管理器中打开 WebDAV 链接，远比在浏览器中下载文件更隐蔽，用户几乎察觉不到文件正在被下载**。

更危险的是，这种手段可以**绕过标准边界防御**。

由于恶意文件直接通过操作系统的文件管理器加载，该攻击**完全绕过浏览器安全控制**，同时因利用了非常见攻击向量，**还可能绕过部分终端检测与响应（EDR）系统**。

此类攻击最危险的特性之一，与 Windows 处理**UNC 路径 URL 快捷方式**的机制缺陷有关。

研究人员表示：“当用户浏览包含 UNC 路径 URL 快捷方式的目录时，该文件会**自动向外发起连接**，尝试访问攻击者服务器，从而直接提醒攻击者：Payload 已在目标主机上线。”

这意味着受害者**甚至无需点击恶意文件**，仅打开所在文件夹就会触发 DNS 查询，直接暴露自己。

为托管恶意 WebDAV 服务，攻击者大量借助**合法基础设施**隐藏行踪。

报告显示：“多个相似攻击活动均滥用 Cloudflare Tunnel 的演示实例（trycloudflare [.] com）搭建 WebDAV 服务。”

由于流量经过可信的 Cloudflare 域名，安全分析师很难一眼识别出恶意行为。

一旦连接建立，攻击者便会投放 Payload。

Cofense 数据显示，**使用该战术的高级威胁报告中，高达 87% 最终会投递多款远程控制木马**，包括知名的 **XWorm RAT、Async RAT、DcRAT** 等。

主要攻击目标集中在**欧洲企业环境**。数据显示，50% 的攻击使用**德语邮件**伪装成财务发票，其次为英语（30%）、意大利语和西班牙语。

本文翻译自securityonline [原文链接](https://securityonline.info/the-explorer-trap-how-hackers-turn-windows-file-explorer-into-a-silent-portal-for-remote-access-trojans/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314921](/post/id/314921)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-explorer-trap-how-hackers-turn-windows-file-explorer-into-a-silent-portal-for-remote-access-trojans/)

如若转载,请注明出处： <https://securityonline.info/the-explorer-trap-how-hackers-turn-windows-file-explorer-into-a-silent-portal-for-remote-access-trojans/>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1050**

* 粉丝
* **6**

### TA的文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26

### 相关文章

* ##### [OneUptime命令注入漏洞可致服务器被完全接管](/post/id/314962)

  2026-03-04 10:37:18
* ##### [Windows错误报告服务ALPC权限提升漏洞PoC已公开](/post/id/314970)

  2026-03-04 10:36:48
* ##### [Google推出iOS版Quick Share，打通安卓到苹果设备的文件传输壁垒](/post/id/314975)

  2026-03-04 10:36:19
* ##### [Zerobotv9僵尸网络开始劫持企业自动化系统](/post/id/314979)

  2026-03-04 10:35:51
* ##### [MS-Agent存在未修复漏洞（CVE-2026-2256），攻击者可劫持AI助手](/post/id/314985)

  2026-03-04 10:35:26
* ##### [Anthropic推出记忆导入功能，助力QuitGPT浪潮下用户迁移对话数据](/post/id/314990)

  2026-03-04 10:34:57
* ##### [Chrome Gemini漏洞可被攻击者远程访问用户摄像头与麦克风](/post/id/314994)

  2026-03-04 10:34:28

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