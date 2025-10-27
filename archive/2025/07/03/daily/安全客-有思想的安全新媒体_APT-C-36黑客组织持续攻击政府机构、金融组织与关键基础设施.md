---
title: APT-C-36黑客组织持续攻击政府机构、金融组织与关键基础设施
url: https://www.anquanke.com/post/id/309258
source: 安全客-有思想的安全新媒体
date: 2025-07-03
fetch_date: 2025-10-06T23:49:34.878074
---

# APT-C-36黑客组织持续攻击政府机构、金融组织与关键基础设施

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

# APT-C-36黑客组织持续攻击政府机构、金融组织与关键基础设施

阅读量**36648**

发布时间 : 2025-07-02 14:51:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源： cybersecuritynews

原文地址：<https://cybersecuritynews.com/apt-c-36-hackers-attacking-government-institutions/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

自2018年以来，APT-C-36（又名 Blind Eagle，盲鹰）这一高级持续性威胁组织，已成为拉丁美洲多个关键行业面临的重要网络对手。该组织持续针对哥伦比亚的政府机构、金融组织以及关键基础设施发起有组织的攻击，攻击方式主要依赖精心设计的钓鱼邮件活动及远程访问木马（RAT）部署。

该组织的主要作战方法以社会工程为核心，常通过包含恶意链接的钓鱼邮件引导目标点击，从而启动攻击链。Blind Eagle 在攻击手段上的适应性极强，近期尤其善于利用 CVE-2024-43451 等漏洞 —— 这是一个微软 Windows 漏洞，仅需极少用户交互即可导致 NTLMv2 密码哈希值泄露。

尽管微软已于2024年11月发布补丁，但该组织仍持续利用低交互机制，演化其攻击方式以保持作战有效性。

自2024年11月以来的最新威胁情报显示，Blind Eagle 正在持续推进一项活跃攻击行动，并对其投递机制进行了优化。当受害者点击恶意链接后，攻击链便会发起 WebDAV 请求（使用 HTTP 80端口），其 User-Agent 特征为“Microsoft-WebDAV-MiniRedir/10.0.19044”。

WebDAV 是一种支持通过互联网传输文件和目录的协议，被该组织用于执行下一阶段恶意载荷投递和在受害系统中执行恶意程序。

Darktrace 分析师于2025年2月底，在哥伦比亚某客户网络中识别到一次规模较大的 Blind Eagle 行动。攻击者从发起攻击到完成全过程，仅耗时五小时，显示出极高的效率。

分析显示，受害设备连接至外部 IP 地址 62[.]60[.]226[.]112（地理位置在德国），并从 URL `hxxp://62[.]60[.]226[.]112/file/3601_2042.exe` 下载可执行恶意文件。

**命令与控制（C2）基础设施分析：**

此次攻击的命令控制架构展示了该组织高度专业的操作安全措施。在实现初始入侵后，受感染设备通过动态 DNS 域名与C2服务器通信，包括 `21ene.ip-ddns[.]com` 和 `diciembrenotasenclub[.]longmusic[.]com`，并通过 TCP 端口 1512 执行命令控制。

动态 DNS 服务为攻击者提供了高度弹性的基础设施，使其在 IP 变更时依然能够保持对受害设备的持续访问，绕过传统防御机制。

调查还发现，该组织在攻击过程中进行数据渗漏，累计外传数据量达 65.6 MiB，其中约 60 MiB 被传送至主控服务器，另有 5.6 MiB 发往辅助基础设施，体现出其对被攻陷环境中数据窃取的系统化策略。

本文翻译自 cybersecuritynews [原文链接](https://cybersecuritynews.com/apt-c-36-hackers-attacking-government-institutions/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309258](/post/id/309258)

安全KER - 有思想的安全新媒体

本文转载自:  [cybersecuritynews](https://cybersecuritynews.com/apt-c-36-hackers-attacking-government-institutions/)

如若转载,请注明出处： <https://cybersecuritynews.com/apt-c-36-hackers-attacking-government-institutions/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

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