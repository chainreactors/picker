---
title: 新型VMScape攻击突破AMD、英特尔CPU的客户机-主机隔离
url: https://www.anquanke.com/post/id/312079
source: 安全客-有思想的安全新媒体
date: 2025-09-13
fetch_date: 2025-10-02T20:04:22.680056
---

# 新型VMScape攻击突破AMD、英特尔CPU的客户机-主机隔离

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

# 新型VMScape攻击突破AMD、英特尔CPU的客户机-主机隔离

阅读量**72300**

发布时间 : 2025-09-12 17:35:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-vmscape-attack-breaks-guest-host-isolation-on-amd-intel-cpus/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一种名为VMScape的新型类Spectre攻击允许恶意虚拟机（VM）从运行在现代AMD或英特尔CPU上的未修改QEMU hypervisor进程中窃取加密密钥。

该攻击打破了VM与云hypervisor之间的隔离，绕过现有Spectre缓解措施，并利用推测执行威胁泄露敏感数据。

研究人员强调，VMScape**无需攻陷主机**，且在硬件默认启用缓解措施的情况下，对未修改的虚拟化软件依然有效。他们指出，威胁行为者只需租用一台虚拟机，即可对云服务商发起此类攻击，从hypervisor或其他VM中窃取机密。

VMScape由瑞士苏黎世联邦理工学院（ETH Zurich）的研究团队开发，研究发现其影响**AMD Zen 1至Zen 5全系列处理器**以及英特尔“Coffee Lake”CPU，但较新的“Raptor Cove”和“Gracemont”架构不受影响。

### **从QEMU中窃取机密的原理**

现代CPU通过扩展客户机与主机之间分支预测单元（BPU）的隔离来防御推测攻击，但研究人员发现这种隔离并不完整。客户机用户可通过共享的BTB（分支目标缓冲区）、IBP/ITA、BHB（分支历史缓冲区）等BPU结构，影响主机用户进程的间接分支预测。

![]()

攻击目标是用户态hypervisor组件QEMU，其将客户机内存映射到自身地址空间，使攻击者可利用“FLUSH+RELOAD”缓存侧信道。苏黎世联邦理工学院研究人员通过Spectre-BTI（分支目标注入）攻击，误导QEMU中的目标间接分支，使其推测执行泄露gadget，将机密数据泄露到共享的reload缓冲区中。

![]()

为延长推测执行窗口，攻击者通过构建针对AMD Zen 4 CPU末级缓存（LLC）的驱逐集，从客户机内部驱逐相关缓存条目。

地址空间布局随机化（ASLR）——一种随机化进程中数据加载内存地址的安全机制——被攻击者通过探测分支冲突定位目标gadget，并暴力破解reload缓冲区虚拟地址的方式绕过。

苏黎世联邦理工学院研究人员展示，VMScape能以**32字节/秒**的速率从QEMU中泄露任意内存数据，字节级准确率达**98.7%**，整体利用成功率为**43%**。按此速率，4KB机密（如磁盘加密密钥）可在128秒内泄露；若包含ASLR绕过过程，端到端总耗时约772秒（近13分钟）。

### **影响与应对措施**

虚拟化是云计算的基石，若客户机可读取主机内存，将威胁多租户云安全。但需强调的是，VMScape等攻击需**高级知识、深厚技术专长和持续执行时间**，因此即便可行，也不会对广大用户构成威胁。

![]()

苏黎世联邦理工学院团队于6月7日向AMD和英特尔报告了研究结果，该问题被分配CVE编号**CVE-2025-40300**。AMD已发布相关安全公告。

Linux内核开发者发布补丁，通过在VMEXIT时添加间接分支预测屏障（IBPB）缓解VMScape，即在客户机切换至主机时刷新BPU。研究人员表示，该缓解措施在常见工作负载中性能影响极小。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-vmscape-attack-breaks-guest-host-isolation-on-amd-intel-cpus/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312079](/post/id/312079)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-vmscape-attack-breaks-guest-host-isolation-on-amd-intel-cpus/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-vmscape-attack-breaks-guest-host-isolation-on-amd-intel-cpus/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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