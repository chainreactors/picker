---
title: PerfektBlue漏洞链曝光：汽车面临蓝牙黑客攻击风险，或致信息娱乐系统遭劫持
url: https://www.anquanke.com/post/id/310048
source: 安全客-有思想的安全新媒体
date: 2025-07-16
fetch_date: 2025-10-06T23:39:10.786538
---

# PerfektBlue漏洞链曝光：汽车面临蓝牙黑客攻击风险，或致信息娱乐系统遭劫持

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

# PerfektBlue漏洞链曝光：汽车面临蓝牙黑客攻击风险，或致信息娱乐系统遭劫持

阅读量**55606**

发布时间 : 2025-07-15 18:15:42

**x**

##### 译文声明

本文是翻译文章，文章原作者 Anviksha More，文章来源：govinfosecurity

原文地址：<https://www.govinfosecurity.com/perfektblue-bug-chain-exposes-cars-to-bluetooth-hacking-a-28958>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

*一系列严重的蓝牙漏洞存在于用于帮助汽车连接手机及其他设备的软件中，这可能使攻击者远程控制梅赛德斯 – 奔驰、斯柯达和大众等主流汽车制造商所使用的车载信息娱乐系统。*

最新研究显示，汽车中**用于连接手机及其他设备的软件**存在一系列严重蓝牙漏洞，攻击者可能借此**远程控制**多家主流汽车制造商（包括梅赛德斯 – 奔驰、斯柯达、大众等）所使用的**车载信息娱乐系统**。

PCA 安全公司将这组漏洞链命名为 **“PerfektBlue”**，其存在于 OpenSynergy 公司开发的一款广泛应用的蓝牙软件栈（Blue SDK）中。这些漏洞允许曾配对过的设备通过**一次用户交互**（如点击提示框）触发远程代码执行攻击，进而可能让攻击者控制信息娱乐系统的**音频、导航及个人数据访问**等功能。

现代汽车配备多个互联的计算机系统（即 **“车载网络”**），信息娱乐系统接入该网络，通常通过**以太网（Ethernet）或控制器局域网（CAN bus）**等共享数据通道与其他车辆部件通信。理论上，这些通道应设有数字 **“检查点”（如网关或防火墙）**，限制信息娱乐系统的通信范围。

但不同制造商的 “检查点” 设计差异显著，部分车辆的信息娱乐系统与其他系统的数据交换**过于自由**。这意味着，一旦攻击者通过PerfektBlue等蓝牙漏洞侵入信息娱乐系统，就能以此为跳板，尝试向更广泛的车载网络发送**未授权指令**。

此类攻击的关键在于利用**曾与汽车蓝牙系统配对过的设备**（通常是驾驶员的智能手机）。配对关系会使设备获得系统内**更高的信任级别和访问权限**，绕过首次连接或不可信连接所需的多项安全验证。利用PerfektBlue漏洞时，攻击者需处于车辆蓝牙**信号范围内**（通常约 10 米）。若攻击者持有或能伪造曾配对的设备，甚至在某些情况下恢复设备数据，就能借助已建立的连接信任关系**绕过重新认证步骤**，仅通过近距离接触即可触发攻击。此外，攻击者还可能在停车场、车库等场所，在车辆附近放置小型蓝牙设备，无需亲自在场即可实施攻击。

PerfektBlue漏洞链包含 **4 个协同作用的漏洞**，通过组合利用可绕过安全机制并执行任意代码。PCA 安全公司已向受影响厂商及相关机构私下披露技术细节，相关 CVE 编号正在申请中，尚未公开。这些漏洞包括：**内存损坏问题（可导致程序运行不稳定或执行流程被篡改）、蓝牙通信中输入长度验证的逻辑缺陷、获取初始访问权限后的权限提升方法，以及曾配对或伪造设备无需用户交互即可重新连接的漏洞**。

这些漏洞共同削弱了信息娱乐系统中**本应通过配对限制、内存安全检查和权限隔离所保护的攻击面**。只要驾驶员在不当时机轻触屏幕（如确认某个提示框），处于蓝牙范围内的攻击者就能执行任意代码，可能获取麦克风、GPS 数据乃至远程信息处理系统的访问权限。在信息娱乐系统与其他功能隔离不足的车辆架构中，攻击者甚至可能尝试侵入与**物理安全**功能相关的系统。

本文翻译自govinfosecurity [原文链接](https://www.govinfosecurity.com/perfektblue-bug-chain-exposes-cars-to-bluetooth-hacking-a-28958)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310048](/post/id/310048)

安全KER - 有思想的安全新媒体

本文转载自: [govinfosecurity](https://www.govinfosecurity.com/perfektblue-bug-chain-exposes-cars-to-bluetooth-hacking-a-28958)

如若转载,请注明出处： <https://www.govinfosecurity.com/perfektblue-bug-chain-exposes-cars-to-bluetooth-hacking-a-28958>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**5赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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