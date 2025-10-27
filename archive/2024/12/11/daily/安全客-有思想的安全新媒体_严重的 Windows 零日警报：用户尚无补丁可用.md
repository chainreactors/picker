---
title: 严重的 Windows 零日警报：用户尚无补丁可用
url: https://www.anquanke.com/post/id/302559
source: 安全客-有思想的安全新媒体
date: 2024-12-11
fetch_date: 2025-10-06T19:36:51.491692
---

# 严重的 Windows 零日警报：用户尚无补丁可用

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

# 严重的 Windows 零日警报：用户尚无补丁可用

阅读量**52836**

发布时间 : 2024-12-10 10:22:39

**x**

##### 译文声明

本文是翻译文章，文章原作者 Uzair Amir，文章来源：hackread

原文地址：<https://hackread.com/windows-zero-day-alert-no-patch-available-for-users/>

译文仅供参考，具体内容表达以及含义原文为准。

**利用自动补丁和服务器加固策略保护系统，抵御 NTLM 零日漏洞。保持积极主动，确保业务安全。**

新发现的 Windows 零日漏洞使多个 Windows 版本的用户面临凭证被盗的风险。由 0patch 研究人员发现的这一关键安全漏洞允许攻击者通过一种具有欺骗性的简单方法窃取 NTLM 凭据。

**是什么导致了这一漏洞的危险性？**

**广泛影响**

该漏洞影响广泛的 Windows 系统，包括

* Windows Server 2022
* Windows 11（最高版本 24H2）
* Windows 10（多个版本）
* Windows 7 and Server 2008 R2

**漏洞利用机制**

该漏洞的技术细节暂不公布，以尽量降低利用风险，直至微软发布修复程序，将进一步的利用风险降至最低。

利用该漏洞，攻击者可诱使用户在 Windows 资源管理器中打开恶意文件，从而窃取用户的 NTLM 凭据。

攻击者可以通过极少的用户交互触发该漏洞：

* 打开共享文件夹
* 访问 USB 磁盘
* 在 Windows 资源管理器中查看恶意文件
* 使用策略性放置的文件访问下载文件夹

**未修补漏洞的大背景**

这并非孤立事件。同一研究小组此前已发现多个未解决的 Windows 漏洞，包括

* Windows 主题文件问题
* “网络标记”漏洞
* “EventLogCrasher ”漏洞
* 三个与 NTLM 相关的漏洞（PetitPotam、PrinterBug/SpoolSample 和 DFSCoerce）

**0patch 微型补丁**

0patch 为所有在其平台上注册的用户免费提供最新 NTLM 零日漏洞的微补丁，直到微软发布官方修复程序。除配置明确阻止自动更新的情况外，该安全微补丁已自动部署到专业版和企业版账户。

网络安全公司Saviynt的首席信任官吉姆-劳斯（Jim Routh）说：“对使用过时和遗留基础设施的企业造成的影响比单纯的运营成本影响更为重要。在这种情况下，MS过时的身份验证应用程序（NTLM）使威胁行为者能够窃取Windows凭证，从而有可能损害客户体验。”

**注重主动出击**

自动补丁管理（如通过 0patch 为专业版和企业版账户提供的保护）是一个良好的开端，但企业还需要做得更多。通过在所有系统中设置一致的安全配置，实施强大的服务器加固策略可以增加多层防御。

这种积极主动的方法不仅仅是对漏洞做出反应，还能帮助企业抵御威胁，如最近的 NTLM 零日漏洞。

本文翻译自hackread [原文链接](https://hackread.com/windows-zero-day-alert-no-patch-available-for-users/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302559](/post/id/302559)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/windows-zero-day-alert-no-patch-available-for-users/)

如若转载,请注明出处： <https://hackread.com/windows-zero-day-alert-no-patch-available-for-users/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

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