---
title: 远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测
url: https://www.anquanke.com/post/id/313056
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:01:00.224554
---

# 远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测

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

# 远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测

阅读量**20908**

发布时间 : 2025-11-07 10:26:52

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/endclient-rat/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款复杂的**远程访问木马（RAT）** 正通过利用**被盗代码签名证书**绕过 antivirus 检测。

新发现的“**EndClient RAT**”通过伪装为“**StressClear.msi** ”的恶意 Microsoft Installer 包传播。

此次披露源于独立安全研究人员与具有联合国经社理事会特别咨商地位的非政府组织**PSCORE**的联合调查。

该恶意软件的检测率极低：**64款 antivirus 引擎中仅7款标记了投放器（dropper），仅1款检测到 payload 脚本**，凸显当前安全防御的重大漏洞。

### **攻击链：从账户劫持到定向传播**

攻击始于9月，威胁行为者入侵了一名知名人权活动家的 Google 账户，并利用“查找、保护或擦除丢失的 Android 设备”功能远程擦除受害者手机。

同时，攻击者劫持受害者的 KakaoTalk 账户，向**39名已确认目标**分发基于 AutoIT 的 RAT。

分发方式为**系统性、非自动化的一对一对话**：威胁行为者冒充受信任的受害者，指示联系人下载并执行恶意 MSI 文件。

这种定向社会工程手段显示出对人权捍卫者社区的深入了解，以及对既有信任关系的恶意利用。

![]()

### **被盗证书与合法伪装**

这份由 SSL.com EV Code Signing Intermediate CA RSA R3 颁发的有效代码签名证书（有效期2024年10月25日至2025年10月17日），使恶意软件对 antivirus 软件呈现合法性，并阻止 Windows SmartScreen 警报触发——这是攻击成功的关键因素。

#### **持久化与反分析机制**

恶意软件通过多种机制建立持久化：

1. 创建名为“IoKlTr”的计划任务，每分钟执行一次；
2. 在 Windows 启动目录中放置 LNK 文件。

执行时，恶意软件启用多项反分析功能，包括使用互斥体（mutex）标识符“**Global\AB732E15-D8DD-87A1-7464-CE6698819E701**”检查，防止多实例同时运行。

值得注意的是，RAT 包含**特定反 Avast 功能**：当检测到 Avast antivirus 时，会用垃圾数据和新文件名创建文件的多态变异体。考虑到 Avast 在韩国的市场份额远低于 AhnLab，这一实现颇为特殊。

#### **命令与控制（C2）通信**

恶意软件通过**自定义 JSON 协议**与 IP 地址 **116.202.99.218:443** 建立 C2 通信，使用独特标记：

1. 客户端到服务器：“**endClient9688**”
2. 服务器到客户端：“**endServer9688**”

![]()

这种基于标记的帧结构使 RAT 能够传输系统信息、执行远程 shell 命令，并传输最大30MB的文件。

### **内存执行与高级功能**

EndClient RAT 部署四个**内存中执行的机器码模块**，处理协议标记解析及 C2 命令编解码：

1. 网络数据模式匹配的二进制搜索功能；
2. Base64 编解码能力；
3. LZMA 解压算法。

这些模块通过 AutoIT 存根（stub）运行：分配具有读-写-执行权限的内存，并执行 raw shellcode（含 x86 和 x64 独立变体）。

分析发现，内存存根并非此攻击独有——威胁情报平台上的其他样本中存在类似代码块。这与**Kimsuky 组织**（又称 APT43）从多源整合代码组件的已知手法一致，但其具体来源尚不明确。

攻击中还异常捆绑了**WIZVERA VeraPort 的 Delfino 包。**

### **归因与影响**

![]()

攻击手法（偏好 AutoIT、重用组件、针对 HRD 社区的复杂社会工程）与**Kimsuky 威胁组织**（APT43）的特征高度吻合。

### **缓解建议**

安全团队应：

1. 监控网络流量中独特协议标记“**endClient9688**”和“**endServer9688**”；
2. 检查 C:\Users\Public\Music 目录中的计划任务痕迹，以及随机前缀的可疑命名管道；
3. 将全局互斥体标识符“**Global\AB732E15-D8DD-87A1-7464-CE6698819E701**”作为检测指标。

组织应将签名 MSI 文件视为不可信，除非验证其来源（尤其是通过社会工程渠道传播的文件）。

此次攻击的低检测率和对目标社区的大规模渗透，凸显**加强威胁情报共享**及为高风险民间组织提供**专门安全支持**的迫切需求。

本文翻译自gbhackers [原文链接](https://gbhackers.com/endclient-rat/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313056](/post/id/313056)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/endclient-rat/)

如若转载,请注明出处： <https://gbhackers.com/endclient-rat/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **663**

* 粉丝
* **6**

### TA的文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13

### 相关文章

* ##### [黑客正滥用Windows Hyper-V功能隐匿Linux虚拟机，以规避终端检测与响应机制的检测](/post/id/313062)

  2025-11-07 10:27:48
* ##### [谷歌发出警告：新型PROMPTFLUX恶意软件正利用Gemini API实现源代码自我重写](/post/id/313072)

  2025-11-07 10:27:39
* ##### [开源安全模型OpenGuardrails发布，旨在为现实世界AI应用保驾护航](/post/id/313066)

  2025-11-07 10:27:29
* ##### [为遵循欧盟监管要求，苹果将于欧盟地区关闭Apple Watch的自动Wi-Fi同步功能](/post/id/313079)

  2025-11-07 10:27:22
* ##### [美国CISA发布警告：Gladinet CentreStack与Triofox文件共享软件中的漏洞正遭攻击利用](/post/id/313069)

  2025-11-07 10:27:13
* ##### [恶意软件Gootloader重出江湖，采用ZIP文件新策略隐匿恶意负载](/post/id/313076)

  2025-11-07 10:27:01
* ##### [二进制供应链安全平台Binarly Transparency Platform 3.5发布，新增对Java归档文件与JVM字节码的深度支持](/post/id/313053)

  2025-11-07 10:26:40

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