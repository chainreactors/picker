---
title: TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效
url: https://www.anquanke.com/post/id/312872
source: 安全客-有思想的安全新媒体
date: 2025-10-29
fetch_date: 2025-10-30T03:10:30.122355
---

# TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效

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

# TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效

阅读量**24520**

发布时间 : 2025-10-29 17:28:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Bill Toulas，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

学术研究人员开发了一种名为**TEE.Fail**的侧信道攻击，能够从CPU中的可信执行环境（TEE）——系统中安全性极高的区域（如英特尔的SGX和TDX，以及AMD的SEV-SNP）——提取机密信息。

该方法是针对DDR5系统的**内存总线介入攻击**，计算机爱好者仅需不到1000美元成本即可成功实施。

可信执行环境（TEE）是主处理器内的“机密计算”硬件，确保敏感数据（如用于身份验证和授权的加密密钥）的机密性和完整性。

这一环境与操作系统隔离，并创建受保护的内存区域，使代码和数据能够在其中安全运行。

佐治亚理工学院和普渡大学的研究人员指出，由于最新几代产品的架构权衡，英特尔SGX、英特尔TDX和AMD SEV-SNP的现代实现**不再像宣传的那样安全**。

具体而言，TEE已从客户端CPU转向采用DDR5内存的服务器级硬件，后者采用确定性AES-XTS内存加密，并为提升性能和可扩展性**移除了内存完整性和重放保护机制**。

他们的实验证实，利用这些弱点可实现密钥提取和认证伪造。TEE.Fail是首个基于DDR5的密文攻击，扩展了此前针对DDR4的WireTap和BatteringRAM等研究成果。

### **攻击原理与影响**

该攻击需要对目标设备的物理访问权限，以及修改内核驱动程序的root级权限，但**无需芯片级专业知识**。

技术论文中，研究人员解释称，他们通过将系统内存时钟降至3200 MT/s（1.6 GHz），实现了信号的可靠捕获。为此，他们在DDR5 DIMM与主板之间连接了RDIMM转接卡和定制探针隔离网络。

![]()

通过将介入器连接到逻辑分析仪，攻击者可记录DDR5命令/地址和数据突发，从而观察物理DRAM位置的密文写入与读取操作。

![]()

为针对英特尔SGX实现攻击目标，研究人员需将虚拟地址中的数据强制路由至单个内存通道，以便通过介入器观测。

借助英特尔向内存地址转换组件公开的物理地址接口，研究人员能够“通过sysfs将此解码接口进一步暴露给用户空间”，从而获取确定物理地址对应DIMM位置的信息。

然而，SGX依赖操作系统内核进行物理内存分配，因此研究人员“修改了内核SGX驱动程序，以接受虚拟地址与物理地址对作为参数存储在全局内核内存中”。

研究人员创建了一个SGX enclave，通过对特定内存虚拟地址进行密集读写操作，验证内存介入器上观测到的加密密文是物理内存地址及其内容的**确定性函数**。

“为验证加密的确定性，我们指示enclave对enclave内存中的固定虚拟地址执行一系列写入和读取操作，并使用逻辑分析仪捕获每一步后的密文读取数据。”他们解释道。

由于AES-XTS加密会使同一信息每次加密均产生相同输出，研究团队向可观测物理地址写入已知值，构建密文与原始值的映射关系。

![]()

随后，通过触发并记录目标加密操作，观测中间表项的加密访问，恢复每个签名的nonce值。

结合恢复的nonce和公开签名，他们可重构私有签名密钥，进而伪造有效的SGX/TDX quote，**冒充合法TEE**。

相同方法被用于从AMD SEV-SNP保护的虚拟机中运行的OpenSSL提取签名密钥。值得注意的是，即使启用“密文隐藏”（Ciphertext Hiding）安全选项，针对AMD SEV-SNP的攻击**依然有效**。

研究人员展示的攻击场景包括：

1. 在以太坊BuilderNet上伪造TDX认证，访问机密交易数据和密钥，实现**未被检测的抢先交易**。
2. 伪造英特尔和NVIDIA认证，使工作负载在TEE外部运行却显示为合法。
3. 直接从enclave提取ECDH私钥，恢复网络主密钥，**完全破坏机密性**。

通过TEE.Fail，研究人员证明可控制TEE执行并观测特定虚拟地址。他们还针对Xeon服务器实施攻击，获取了用于验证设备身份的**配置证书密钥（PCK）**。

TEE.Fail是一种需要物理访问的复杂攻击，在现实场景中实用性较低，其复杂度**远非普通用户面临的直接威胁**。

研究人员已于4月向英特尔、8月向AMD、6月向NVIDIA报告了相关发现。三家厂商均确认问题存在，并表示正在开发缓解措施，调整机密计算威胁模型，计划在TEE.Fail论文公开时发布官方声明。

BleepingComputer已请求英特尔、AMD和NVIDIA分享声明以纳入本报告，但截至发布时尚未收到回复。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312872](/post/id/312872)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **630**

* 粉丝
* **6**

### TA的文章

* ##### [重磅！网络安全法迎来重大修改，人工智能治理迈出关键一步](/post/id/312934)

  2025-10-29 17:30:44
* ##### [OpenAI宣布启动重组，非营利基金会将重新掌握公司核心控制权](/post/id/312864)

  2025-10-29 17:29:30
* ##### [威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制](/post/id/312867)

  2025-10-29 17:29:15
* ##### [TEE.Fail攻击导致英特尔、AMD与NVIDIA CPU的机密计算技术失效](/post/id/312872)

  2025-10-29 17:28:56
* ##### [新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码](/post/id/312878)

  2025-10-29 17:27:44

### 相关文章

* ##### [重磅！网络安全法迎来重大修改，人工智能治理迈出关键一步](/post/id/312934)

  2025-10-29 17:30:44
* ##### [OpenAI宣布启动重组，非营利基金会将重新掌握公司核心控制权](/post/id/312864)

  2025-10-29 17:29:30
* ##### [威胁行为体正结合FileFix与缓存走私攻击，以规避安全防护机制](/post/id/312867)

  2025-10-29 17:29:15
* ##### [新型安卓恶意软件GhostGrab可静默窃取网银登录凭证并拦截短信验证码](/post/id/312878)

  2025-10-29 17:27:44
* ##### [Docker Compose 中存在路径遍历漏洞（CVE-2025-62725），通过OCI制品可导致任意文件被覆盖](/post/id/312882)

  2025-10-29 17:27:07
* ##### [Wear OS 信息应用存在权限漏洞 (CVE-2025-12080)，可导致无权限应用在未经用户授权的情况下发送短信/RCS消息，且POC已公开](/post/id/312885)

  2025-10-29 17:26:40
* ##### [Magento 中存在严重漏洞（CVE-2025-54236），可导致会话劫持与RCE，且已被活跃利用](/post/id/312888)

  2025-10-29 17:26:05

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