---
title: 二进制供应链安全平台Binarly Transparency Platform 3.5发布，新增对Java归档文件与JVM字节码的深度支持
url: https://www.anquanke.com/post/id/313053
source: 安全客-有思想的安全新媒体
date: 2025-11-07
fetch_date: 2025-11-08T03:01:01.627351
---

# 二进制供应链安全平台Binarly Transparency Platform 3.5发布，新增对Java归档文件与JVM字节码的深度支持

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

# 二进制供应链安全平台Binarly Transparency Platform 3.5发布，新增对Java归档文件与JVM字节码的深度支持

阅读量**20486**

发布时间 : 2025-11-07 10:26:40

**x**

##### 译文声明

本文是翻译文章，文章原作者 Industry News，文章来源：helpnetsecurity

原文地址：<https://www.helpnetsecurity.com/2025/11/06/binarly-transparency-platform-3-5-now-supports-java-archives-and-jvm-bytecode/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Binarly发布了**Binarly Transparency Platform 3.5版本**，新增**Java生态系统支持**、**企业级YARA集成**及**运维升级**功能。

通过此次更新，Binarly的**加密算法识别引擎**现已支持**Java归档文件（JAR）和JVM字节码**，可扫描Docker容器或固件中的独立文件及嵌入式文件。这意味着组织无需访问源代码，即可清晰掌握其Java产品所依赖的**加密原语**。

该新引擎基于**代码属性图（CPG）分析**，通过跨函数数据流追踪消除误报，并将所有发现映射至**NIST IR 8457分类**，助力衡量**后量子密码学（PQC）就绪状态**。目前支持的库包括Bouncy Castle、Apache Commons、Google Tink和Guava，Android包分析功能将于今年晚些时候推出。

平台更新还深度集成了行业标准的**YARA签名检测技术**，可覆盖大规模软件和固件组合。

传统上，跨团队和供应商维护YARA规则时，常面临**语法漂移、规则膨胀和执行不一致**等问题。Binarly通过以下功能消除这些痛点：

1. **交互式YARA Playground**：支持规则开发（YARA及Binarly自研的FwHunt）。
2. **受治理的规则管理器**：提供基于角色的细粒度访问控制。
3. **实时Rust-based YARA-X引擎**：在部署前验证规则有效性。

最终形成**单一治理管道**，使产品安全事件响应团队（PSIRT）、第三方风险管理（TPRM）团队和采购部门能够在企业范围内推动**一致的检测和基于证据的决策**。

“Java支持和企业级YARA集成解决了产品安全中两个最棘手的盲点。大多数团队难以了解Java堆栈的真实内容，也难以在复杂环境中一致地运维YARA规则。我们率先构建了连接现有威胁情报源数据的工具，此次发布将两个世界融合，提供深度加密可见性和可扩展的威胁狩猎能力。”Binarly首席执行官兼研究主管Alex Matrosov表示。

### **Binarly Transparency Platform 3.5新增功能**

1. **自定义规则管理**：安全团队可使用YARA和FwHunt规则定义和部署检测逻辑（与Binarly内部用于漏洞和威胁检测的架构相同，支持更高级的代码驱动规则）。这架起了研究与产品安全之间的桥梁，允许针对供应商风险、硬编码密钥或策略执行进行定制化检查。
2. **组织配额**：通过集中分配和跨分布式团队的可见性简化许可证管理。
3. **分诊增强**：支持添加可分配状态、带Markdown支持的线程化评论及动态图表。
4. **后端升级**：提升性能速度，增强Android处理能力，深化加密工件提取（从JAR到UEFI Secure Boot密钥）。

从固件到JVM字节码，Binarly Transparency Platform 3.5由安全研究专家打造，为防御者提供跨复杂软件生态系统的**漏洞、加密态势和可达性统一视图**。

对于采购和第三方供应商风险团队，Binarly通过支持**私有威胁情报摄入、范围化规则执行和透明的证据支持风险报告**，显著改进供应商评估工作流。安全团队则受益于**更快的规则验证、一致的检测和简化的分诊流程**，同时降低了大规模YARA项目通常带来的隐性运营成本。

本文翻译自helpnetsecurity [原文链接](https://www.helpnetsecurity.com/2025/11/06/binarly-transparency-platform-3-5-now-supports-java-archives-and-jvm-bytecode/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313053](/post/id/313053)

安全KER - 有思想的安全新媒体

本文转载自: [helpnetsecurity](https://www.helpnetsecurity.com/2025/11/06/binarly-transparency-platform-3-5-now-supports-java-archives-and-jvm-bytecode/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2025/11/06/binarly-transparency-platform-3-5-now-supports-java-archives-and-jvm-bytecode/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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
* ##### [远程控制木马EndClient通过滥用遭泄露的代码签名证书来规避防病毒软件检测](/post/id/313056)

  2025-11-07 10:26:52

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