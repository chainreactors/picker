---
title: 攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道
url: https://www.anquanke.com/post/id/312953
source: 安全客-有思想的安全新媒体
date: 2025-10-31
fetch_date: 2025-11-01T03:08:37.648922
---

# 攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道

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

# 攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道

阅读量**21782**

发布时间 : 2025-10-31 17:43:54

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/nation-state-espionage-airstalk-malware-hijacks-vmware-airwatch-mdm-api-for-covert-c2-channel/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

帕洛阿尔托网络（Palo Alto Networks）旗下Unit 42威胁情报团队发现了一个名为**Airstalk**的复杂新型恶意软件家族，该家族利用VMware AirWatch（现称Workspace ONE）移动设备管理（MDM）API作为**隐蔽的命令与控制（C2）通道**。

根据Unit 42的报告：“我们发现了一个名为Airstalk的新型Windows恶意软件家族，存在PowerShell和.NET两种变体。我们**中等置信度**评估，某威胁行为者可能在一次供应链攻击中使用了该恶意软件。”

该恶意软件被归类为威胁活动集群CL-STA-1009，是一个**高度适应性的间谍工具包**，旨在窃取浏览器数据、凭证和截图，同时通过滥用合法云服务规避检测。

攻击活动被认为源自**供应链入侵**，通过受信任的第三方供应商和服务提供商瞄准目标组织。

Unit 42解释：“供应链攻击针对组织日常运营依赖的商品和服务，包括硬件、受托管理组织最敏感数据的云服务，以及专业业务流程外包（BPO）人员。”

这类BPO实体（为多个客户管理敏感业务的承包商）是对手的**高价值入口点**。报告警告，入侵一个供应商可能打开通往数百个下游目标的访问权限。

### **恶意软件架构与核心特性**

Airstalk存在两个主要变体：PowerShell版本和.NET版本。两者共享相同的**隐蔽C2机制**，但在复杂度和功能上有所差异。

PowerShell变体代表初始开发阶段，而.NET版本则增加了**多线程通信、版本控制和增强的持久化控制**。

![]()

#### **滥用AirWatch API：伪装成MDM流量的C2通道**

恶意软件的标志性特征是对AirWatch API的滥用。Unit 42写道：

“Airstalk滥用用于移动设备管理的AirWatch API（现称Workspace ONE统一端点管理）。它利用该API建立隐蔽C2通道，主要通过AirWatch的**自定义设备属性管理**和**文件上传功能**。”

这种滥用将受信任的MDM基础设施转化为恶意软件操作者的通信枢纽，使恶意活动**混入合法管理流量**。

在两种变体中，Airstalk均通过AirWatch的`/api/mdm/devices/`端点，将命令嵌入已注册设备的自定义属性中，实现与操作者的通信。

每台受感染机器发送伪装成合法MDM更新的序列化JSON消息，威胁行为者随后检索这些消息——形成一种“**死信投递**”（dead drop）系统，这是间谍活动中经典的非直接连接信息交换技术。

Unit 42描述：“死信投递是一种秘密通信方法，用于在个体间传递物品或信息而无需直接接触。对手通常在间谍活动中使用此技术：一方将物品留在隐藏位置，另一方随后取回。”

这种隐蔽交换使恶意软件能够通过AirWatch的合法二进制大对象（blob）上传功能（`/api/mam/blobs/uploadblob`）接收任务，例如截取屏幕、收集Chrome cookie和泄露文件。

### **.NET变体的高级功能**

Airstalk的.NET变体代表恶意软件的更高级阶段，支持多线程操作，包括任务执行、调试日志泄露和每10分钟一次的常规信标（beaconing）。

Unit 42指出：“.NET变体的开发阶段似乎比PowerShell变体更成熟”，并包含MISMATCH、DEBUG和PING等新型C2消息类型，以实现更好的错误处理和持久化。

其功能不仅限于Chrome，还针对Microsoft Edge和Island Browser，可窃取cookie、书签、浏览历史和截图。

### **高级规避技术**

Airstalk通过**签名二进制文件**和**时间戳操纵**进一步增强隐蔽性。部分样本使用从奥腾工业自动化（廊坊）有限公司窃取的证书进行数字签名，该证书在签发后不久被吊销——这是其他国家资助恶意软件家族中常见的规避策略。

Airstalk采用的高级规避技术包括：

1. 滥用受信任MDM基础设施伪装网络流量
2. 使用合法API进行命令与控制
3. 用窃取的证书对载荷进行数字签名以伪装合法性
4. 操纵PE文件时间戳阻碍取证关联

PowerShell变体通过计划任务实现持久化，而.NET版本则为无文件型，在数据泄露后自删除以最大程度减少检测。

Unit 42警告，恶意软件的隐蔽性使其能够**长期未被发现**——尤其当托管在第三方供应商环境中时，传统端点防护可能无法覆盖。

Unit 42将该活动归因于疑似国家资助的威胁行为者：

“根据内部评估，我们中等置信度认为，某国家资助威胁行为者在供应链攻击中使用了Airstalk恶意软件。我们将已识别活动归类为CL-STA-1009活动集群。”

研究人员强调，攻击者的目标似乎是**长期间谍活动和数据收集**，而非即时破坏。对BPO提供商的瞄准表明，其意图通过受感染的第三方工具间接渗透多个高价值组织，在企业网络中维持持久访问。

本文翻译自securityonline [原文链接](https://securityonline.info/nation-state-espionage-airstalk-malware-hijacks-vmware-airwatch-mdm-api-for-covert-c2-channel/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312953](/post/id/312953)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/nation-state-espionage-airstalk-malware-hijacks-vmware-airwatch-mdm-api-for-covert-c2-channel/)

如若转载,请注明出处： <https://securityonline.info/nation-state-espionage-airstalk-malware-hijacks-vmware-airwatch-mdm-api-for-covert-c2-channel/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **641**

* 粉丝
* **6**

### TA的文章

* ##### [Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中](/post/id/312947)

  2025-10-31 17:44:46
* ##### [安全威胁“幻影乌鸦”被披露：126个恶意npm包通过隐藏依赖项窃取开发者令牌与敏感信息](/post/id/312950)

  2025-10-31 17:44:25
* ##### [攻击组织实施网络间谍活动：Airstalk恶意软件劫持VMware AirWatch MDM API以构建隐秘C2信道](/post/id/312953)

  2025-10-31 17:43:54
* ##### [Progress公司为其MOVEit Transfer的AS2模块发布补丁，修复高危漏洞 (CVE-2025-10932)](/post/id/312957)

  2025-10-31 17:42:55
* ##### [身份安全公司ConductorOne完成7900万美元融资，致力于革新现代化身份安全管理方案](/post/id/312961)

  2025-10-31 17:42:27

### 相关文章

* ##### [Magecart团伙“剑齿虎”刷卡器通过恶意插件渗透WooCommerce，并将其有效载荷隐藏在伪造的PNG图片中](/post/id/312947)

  2025-10-31 17:44:46
* ##### [安全威胁“幻影乌鸦”被披露：126个恶意npm包通过隐藏依赖项窃取开发者令牌与敏感信息](/post/id/312950)

  2025-10-31 17:44:25
* ##### [Progress公司为其MOVEit Transfer的AS2模块发布补丁，修复高危漏洞 (CVE-2025-10932)](/post/id/312957)

  2025-10-31 17:42:55
* ##### [身份安全公司ConductorOne完成7900万美元融资，致力于革新现代化身份安全管理方案](/post/id/312961)

  2025-10-31 17:42:27
* ##### [OpenAI官方证实：GPT-5处理心理与情感困扰的能力已获显著优化](/post/id/312964)

  2025-10-31 17:42:05
* ##### [Chromium内核浏览器Blink渲染引擎中存在高危漏洞，可致攻击者在数秒内引发浏览器崩溃](/post/id/312968)

  2025-10-31 17:40:59
* ##### [360助力石家庄市教育行业网络安全运营中心启航，共筑教育安全新防线](/post/id/312971)

  2025-10-31 17:39:50

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