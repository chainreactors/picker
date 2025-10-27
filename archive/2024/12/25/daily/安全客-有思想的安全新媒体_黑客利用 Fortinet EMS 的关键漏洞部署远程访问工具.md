---
title: 黑客利用 Fortinet EMS 的关键漏洞部署远程访问工具
url: https://www.anquanke.com/post/id/302954
source: 安全客-有思想的安全新媒体
date: 2024-12-25
fetch_date: 2025-10-06T19:34:21.191242
---

# 黑客利用 Fortinet EMS 的关键漏洞部署远程访问工具

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

# 黑客利用 Fortinet EMS 的关键漏洞部署远程访问工具

阅读量**59906**

发布时间 : 2024-12-24 10:46:09

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：TheHackersNews

原文地址：<https://thehackernews.com/2024/12/hackers-exploiting-critical-fortinet.html>

译文仅供参考，具体内容表达以及含义原文为准。

在安装 AnyDesk 和 ScreenConnect 等远程桌面软件的网络攻击活动中，恶意攻击者正在利用一个已修补的影响 Fortinet FortiClient EMS 的重要安全漏洞。

该漏洞是CVE-2023-48788（CVSS评分：9.3），是一个SQL注入漏洞，允许攻击者通过发送特制数据包执行未经授权的代码或命令。

俄罗斯网络安全公司卡巴斯基（Kaspersky）称，2024 年 10 月的这次攻击针对的是一家未具名公司的 Windows 服务器，该服务器暴露在互联网上，并且有两个与 FortiClient EMS 相关的开放端口。

该公司在周四的一份分析报告中说：“目标公司采用了这项技术，允许员工将特定策略下载到他们的公司设备上，使他们能够安全地访问 Fortinet VPN。”

对该事件的进一步分析发现，威胁行为者利用 CVE-2023-48788 作为初始访问载体，随后投放 ScreenConnect 可执行文件，以获取对受攻击主机的远程访问权限。

卡巴斯基说：“在初始安装之后，攻击者开始向被入侵系统上传额外的有效载荷，以开始发现和横向移动活动，如枚举网络资源、试图获取凭证、执行防御规避技术，以及通过 AnyDesk 远程控制工具生成更多类型的持久性。”

下面列出了在攻击过程中投放的其他一些值得注意的工具–Webbrowserpassview.exe。

* webbrowserpassview.exe，这是一款密码恢复工具，可揭示存储在 Internet Explorer（4.0 – 11.0 版）、Mozilla Firefox（所有版本）、谷歌浏览器、Safari 和 Opera 中的密码。
* Mimikatz
* netpass64.exe，密码恢复工具
* netscan.exe，网络扫描器

据信，幕后的威胁分子利用不同的 ScreenConnect 子域名（如 infinity.screenconnect[.]com），将巴西、克罗地亚、法国、印度、印度尼西亚、蒙古、纳米比亚、秘鲁、西班牙、瑞士、土耳其和阿联酋的多家公司作为攻击目标。

卡巴斯基说，它在 2024 年 10 月 23 日检测到了将 CVE-2023-48788 武器化的进一步尝试，这次是在扫描易受该漏洞影响的系统时，执行托管在 webhook[.]site 域上的 PowerShell 脚本，以 “收集来自易受攻击目标的响应”。

网络安全公司 Forescout 在八个多月前发现了一个类似的活动，利用 CVE-2023-48788 发送 ScreenConnect 和 Metasploit Powerfun 有效载荷。

研究人员说：“对这一事件的分析帮助我们确定，攻击者目前用于部署远程访问工具的技术在不断更新，复杂性也在不断增加。”

本文翻译自TheHackersNews [原文链接](https://thehackernews.com/2024/12/hackers-exploiting-critical-fortinet.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302954](/post/id/302954)

安全KER - 有思想的安全新媒体

本文转载自: [TheHackersNews](https://thehackernews.com/2024/12/hackers-exploiting-critical-fortinet.html)

如若转载,请注明出处： <https://thehackernews.com/2024/12/hackers-exploiting-critical-fortinet.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

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