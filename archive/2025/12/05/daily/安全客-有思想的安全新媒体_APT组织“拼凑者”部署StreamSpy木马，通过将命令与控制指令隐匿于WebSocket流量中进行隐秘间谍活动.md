---
title: APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动
url: https://www.anquanke.com/post/id/313606
source: 安全客-有思想的安全新媒体
date: 2025-12-05
fetch_date: 2025-12-06T03:10:00.303820
---

# APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动

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

# APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动

阅读量**22443**

发布时间 : 2025-12-05 17:31:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/patchwork-apt-deploys-streamspy-trojan-hiding-c2-commands-in-websocket-traffic-for-stealth-espionage/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Patchwork APT组织**（又称“白象”）——一个被认为源自南亚的网络间谍活动组织——已发起新一轮攻击，使用名为 **StreamSpy** 的复杂木马。该组织至少自2009年起活跃，通常针对亚洲各地的政府、军事和工业部门。

奇安信威胁情报中心近期检测到这款新型恶意软件，其显著特点是通过“**WebSocket与HTTP协议组合**”规避传统网络检测。Patchwork利用WebSocket进行命令控制（C2），将恶意流量有效隐藏在看似正常的Web活动中。

StreamSpy设计旨在 **隐蔽性和持久性**。它伪装成ZIP文件（如OPS-VII-SIR.zip ），内含模仿PDF图标的可执行文件，“诱使受害者不加辨别地运行恶意程序”。

侵入系统后，恶意软件会拆分通信渠道：

1. **指令与结果**：通过WebSocket协议获取命令并传输结果，连接包含“stream”字符串的接口。
2. **文件传输**：利用标准HTTP协议处理文件上传/下载等大型操作。

该恶意软件高度可配置。执行时，它会“从资源部分解密配置数据”，包括网络C2详情、身份标签和持久化设置。

StreamSpy不仅是被动监听器，更是功能完备的间谍工具包。它收集广泛的设备数据，包括“主机名、用户名、操作系统版本和防病毒软件详情”。

其支持的命令类型多样：

1. **terminal\_input**：将命令传递给shell进程（CMD或PowerShell）执行。
2. **文件操作**：通过“F1A5C3”“D1E2F3”等特定代码实现文件下载、打开或删除。
3. **信息收集**：枚举受感染机器上的所有驱动器和目录内容。

为确保长期驻留，StreamSpy采用多种持久化方法，如创建计划任务、设置“RunOnce”注册表项，或在Startup目录放置LNK文件。

分析显示，StreamSpy并非孤立工具。研究人员发现“该木马与Patchwork使用的Spyder下载器存在相似性”。此外，存在跨组织协作证据：StreamSpy的数字签名与另一区域威胁组织Donot的样本相关联。

这种重叠表明更深层次的协调，“Mahagra（Patchwork）与Donot攻击组织在资源共享方面存在联系”。

本文翻译自securityonline [原文链接](https://securityonline.info/patchwork-apt-deploys-streamspy-trojan-hiding-c2-commands-in-websocket-traffic-for-stealth-espionage/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313606](/post/id/313606)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/patchwork-apt-deploys-streamspy-trojan-hiding-c2-commands-in-websocket-traffic-for-stealth-espionage/)

如若转载,请注明出处： <https://securityonline.info/patchwork-apt-deploys-streamspy-trojan-hiding-c2-commands-in-websocket-traffic-for-stealth-espionage/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **780**

* 粉丝
* **6**

### TA的文章

* ##### [AI boom 催生全球存储芯片荒 价格将涨三倍至 2027 年](/post/id/313587)

  2025-12-05 17:36:12
* ##### [哈维 AI 完成 7.6 亿美元融资 估值达 80 亿美元](/post/id/313583)

  2025-12-05 17:35:29
* ##### [Cacti 中存在高危漏洞（CVE-2025-66399），通过SNMP团体字符串注入可导致远程代码执行](/post/id/313602)

  2025-12-05 17:34:09
* ##### [“PDF陷阱”：Apache Tika核心组件存在严重漏洞（CVE-2025-66516，CVSS 10.0）](/post/id/313590)

  2025-12-05 17:33:30
* ##### [APT组织“拼凑者”部署StreamSpy木马，通过将命令与控制指令隐匿于WebSocket流量中进行隐秘间谍活动](/post/id/313606)

  2025-12-05 17:31:23

### 相关文章

* ##### [AI boom 催生全球存储芯片荒 价格将涨三倍至 2027 年](/post/id/313587)

  2025-12-05 17:36:12
* ##### [哈维 AI 完成 7.6 亿美元融资 估值达 80 亿美元](/post/id/313583)

  2025-12-05 17:35:29
* ##### [Cacti 中存在高危漏洞（CVE-2025-66399），通过SNMP团体字符串注入可导致远程代码执行](/post/id/313602)

  2025-12-05 17:34:09
* ##### [“PDF陷阱”：Apache Tika核心组件存在严重漏洞（CVE-2025-66516，CVSS 10.0）](/post/id/313590)

  2025-12-05 17:33:30
* ##### [Splunk中存在高危漏洞，因Windows平台上的不当文件权限设置，可导致本地攻击者实现权限提升](/post/id/313598)

  2025-12-05 17:30:23
* ##### [智能可观测平台Dynatrace深化其AWS服务集成，新增多项AI与云原生监控功能](/post/id/313610)

  2025-12-05 17:29:29
* ##### [捕食者间谍软件采用新感染途径 实施零点击攻击](/post/id/313604)

  2025-12-05 17:28:25

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