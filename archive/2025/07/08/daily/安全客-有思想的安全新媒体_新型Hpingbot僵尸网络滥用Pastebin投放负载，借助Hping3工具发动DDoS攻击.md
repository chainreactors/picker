---
title: 新型Hpingbot僵尸网络滥用Pastebin投放负载，借助Hping3工具发动DDoS攻击
url: https://www.anquanke.com/post/id/309483
source: 安全客-有思想的安全新媒体
date: 2025-07-08
fetch_date: 2025-10-06T23:18:01.460416
---

# 新型Hpingbot僵尸网络滥用Pastebin投放负载，借助Hping3工具发动DDoS攻击

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

# 新型Hpingbot僵尸网络滥用Pastebin投放负载，借助Hping3工具发动DDoS攻击

阅读量**49199**

发布时间 : 2025-07-07 15:52:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-hpingbot-abusing-pastebin-for-payload-delivery-and-hping3-tool/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款设计精良的新型僵尸网络家族在网络安全领域浮出水面，展现了前所未有的恶意软件设计和攻击手法创新。

Hpingbot恶意软件首次被发现于2025年6月，**明显区别于传统僵尸网络架构，**它巧妙利用合法的在线服务和网络测试工具，**在保持隐蔽运营的同时发动分布式拒绝服务攻击（DDoS）。**

与通常源自Mirai或Gafgyt等知名僵尸网络泄露源代码的恶意软件不同，**hpingbot完全由Go语言从零开发，具备跨平台特性，覆盖Windows及Linux/物联网环境，且支持多种处理器架构，包括amd64、mips、arm和80386。**

**该恶意软件开发者展现出极高的资源整合能力**，利用流行的文本分享平台Pastebin进行负载分发，并结合合法的网络诊断工具hping3发动DDoS攻击。

通过NSFOCUS全球威胁狩猎系统（Fuying Lab Global Threat Hunting System），分析师发现该僵尸网络自首次部署以来**不断迭代升级**。

**攻击者重点瞄准德国目标，美国和土耳其也遭受相关攻击。**

该僵尸网络的特别之处在于其双重用途设计：除能发动多种DDoS攻击外，核心价值还在于其能够下载并执行任意负载，使其成为更危险恶意软件（如勒索软件或高级持续性威胁组件）的潜在分发平台。

**hpingbot支持超过十种不同的DDoS攻击方式，**包括ACK FLOOD、TCP FLOOD、SYN FLOOD、UDP FLOOD以及复杂的混合攻击模式。监测数据显示，自2025年6月17日起，**攻击者已下发数百条DDoS指令，但僵尸网络在攻击间歇期大多保持休眠状态，显示出其具有战略性运营规划，而非持续攻击。**

### 基于Pastebin的负载投放机制

hpingbot最具创新性的部分在于其精巧的负载投放系统，该系统利用了Pastebin这一合法平台的基础设施。**恶意软件在其二进制文件中硬编码了4个Pastebin URL，形成动态指挥控制（C2）机制，有效绕过传统C2检测手段。**

这种设计使攻击者能够无需通过常规渠道直接与被感染主机通信，即可远程更新指令、分发新负载及调整攻击参数。

负载投放流程始于hpingbot访问其嵌入的Pastebin链接以获取最新指令。

这些链接的内容频繁变化，涵盖从简单IP地址到包含下载额外恶意组件的复杂Shell脚本。

恶意软件内置专用的UPDATE模块处理这些Pastebin上的指令，允许攻击者远程推送新功能或完全替换现有组件。

**此系统反映出攻击者高度的运营安全意识，使其能迅速调整基础设施，同时通过Pastebin平台保持对被控系统的持续访问。**

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-hpingbot-abusing-pastebin-for-payload-delivery-and-hping3-tool/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/309483](/post/id/309483)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-hpingbot-abusing-pastebin-for-payload-delivery-and-hping3-tool/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-hpingbot-abusing-pastebin-for-payload-delivery-and-hping3-tool/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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