---
title: 新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联
url: https://www.anquanke.com/post/id/313760
source: 安全客-有思想的安全新媒体
date: 2025-12-15
fetch_date: 2025-12-16T03:22:00.524446
---

# 新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联

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

# 新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联

阅读量**17714**

发布时间 : 2025-12-15 17:41:05

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源： securityonline

原文地址：<https://securityonline.info/new-nanoremote-backdoor-uses-google-drive-api-for-covert-c2-and-links-to-finaldraft-espionage-group/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Elastic 安全实验室**发现了一款技术先进的新型 Windows 后门程序，该程序借助谷歌云端硬盘（Google Drive）这一受信任的基础设施，实现躲避检测与窃取敏感数据的攻击目的。这款恶意软件被命名为**NANOREMOTE**，最早于 2025 年 10 月被监测到，其开发者被认定为经验丰富的间谍威胁攻击者，且该组织曾参与多起备受关注的攻击行动。

这款后门程序的显著特点，在于它利用**合法云服务开展命令与控制（C2）操作**，能够将恶意流量完全混入正常的网络活动中，从而规避检测。

NANOREMOTE 最独特的功能，是可以 \*\*“借助谷歌云端硬盘 API，在受害终端与攻击者之间双向传输数据”\*\*。该恶意软件通过 OAuth 2.0 令牌向谷歌服务器完成身份验证，以此搭建起隐秘的数据窃取与载荷投放通道，而这类通道极难被传统安全工具识别。

这款恶意软件搭载了一套完善的任务管理系统，专门用于处理数据传输工作。它可对下载和上传任务进行排队管理、支持文件传输的暂停与恢复，甚至能生成刷新令牌，在无需用户交互的前提下持续维持访问权限。

该恶意软件的感染链路，由一个名为**WMLOADER**的诱骗型加载器组件启动。此加载器会伪装成一款合法的安全程序，具体是名为`BDReinit.exe`的比特梵德（Bitdefender）崩溃处理程序。但与正版程序不同的是，这个恶意文件携带的是**无效的数字签名**。

WMLOADER 被执行后，会依次完成一系列复杂的解密步骤：

1. **Shellcode 解密**：采用滚动异或（XOR）算法，对嵌入自身的 Shellcode 进行解密。
2. **载荷加载**：解密后的 Shellcode 会在同一目录下搜索名为`wmsetup.log`的文件。
3. **最终解密**：通过**AES-CBC 加密算法**，使用一个硬编码的 16 字节密钥（`3A5AD78097D944AC`）对该日志文件进行解密，最终在内存中释放并执行 NANOREMOTE 后门程序。

NANOREMOTE 是一款基于 C++ 编写的全功能恶意植入程序，它整合了多个开源项目的高级功能，以此提升自身的隐蔽性与稳定性：

* **自定义 PE 文件加载**：借助`libPeConv`库，直接从磁盘或内存中加载并执行可移植可执行文件（PE），绕过 Windows 标准加载器，从而躲避检测。
* **API 挂钩**：利用微软`Detours`工具，对`ExitProcess`和`FatalExit`等关键进程终止函数实施挂钩。这一弹性机制可防止单个工作线程故障导致整个恶意软件进程崩溃。

Elastic 安全实验室已证实，**NANOREMOTE 与威胁集群 REF7707 存在关联**，而该威胁集群此前就与 FINALDRAFT 恶意软件家族有牵连。多项强有力的取证证据支撑了这一关联结论：

1. **代码复用**：两款恶意植入程序中，用于生成 GUID 并通过 Fowler-Noll-Vo（FNV）算法进行哈希计算的代码完全相同。
2. **加密密钥复用**：最确凿的证据是，NANOREMOTE 与 FINALDRAFT 在解密载荷时，使用的是**完全相同的 AES 密钥（`3A5AD78097D944AC`）**。

报告的结论指出：“这一关联再次提供了强有力的信号，表明 FINALDRAFT 与 NANOREMOTE 两款恶意软件**共享代码库与开发环境**。”

本文翻译自 securityonline [原文链接](https://securityonline.info/new-nanoremote-backdoor-uses-google-drive-api-for-covert-c2-and-links-to-finaldraft-espionage-group/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313760](/post/id/313760)

安全KER - 有思想的安全新媒体

本文转载自:  [securityonline](https://securityonline.info/new-nanoremote-backdoor-uses-google-drive-api-for-covert-c2-and-links-to-finaldraft-espionage-group/)

如若转载,请注明出处： <https://securityonline.info/new-nanoremote-backdoor-uses-google-drive-api-for-covert-c2-and-links-to-finaldraft-espionage-group/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

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
* **810**

* 粉丝
* **6**

### TA的文章

* ##### [类人智能赋能：谷歌翻译获 Gemini 升级，实现俚语精准翻译与语气还原](/post/id/313754)

  2025-12-15 17:42:30
* ##### [高危 pgAdmin 远程代码执行漏洞（CVE-2025-13780）绕过此前修复：可通过恶意数据库恢复实现服务器接管](/post/id/313757)

  2025-12-15 17:41:52
* ##### [新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联](/post/id/313760)

  2025-12-15 17:41:05
* ##### [攻击组织 SHADOW-VOID-042 仿冒趋势科技发起钓鱼攻击，目标直指关键基础设施](/post/id/313762)

  2025-12-15 17:40:27
* ##### [高危 Plesk 漏洞（CVE-2025-66430）风险通告：可通过本地权限提升与 Apache 配置注入实现服务器完全接管](/post/id/313765)

  2025-12-15 17:39:47

### 相关文章

* ##### [类人智能赋能：谷歌翻译获 Gemini 升级，实现俚语精准翻译与语气还原](/post/id/313754)

  2025-12-15 17:42:30
* ##### [高危 pgAdmin 远程代码执行漏洞（CVE-2025-13780）绕过此前修复：可通过恶意数据库恢复实现服务器接管](/post/id/313757)

  2025-12-15 17:41:52
* ##### [攻击组织 SHADOW-VOID-042 仿冒趋势科技发起钓鱼攻击，目标直指关键基础设施](/post/id/313762)

  2025-12-15 17:40:27
* ##### [高危 Plesk 漏洞（CVE-2025-66430）风险通告：可通过本地权限提升与 Apache 配置注入实现服务器完全接管](/post/id/313765)

  2025-12-15 17:39:47
* ##### [Apache StreamPark 漏洞风险通告：硬编码密钥与 AES ECB 模式致数据解密及令牌伪造风险](/post/id/313768)

  2025-12-15 17:39:22
* ##### [VS Code 供应链攻击事件：19 款恶意扩展借拼写欺骗与隐写术投放 Rust 木马](/post/id/313771)

  2025-12-15 17:38:25
* ##### [新型 BlackForce 钓鱼工具包：攻击者借浏览器中间人（MitB）攻击窃取凭证并绕过多因素认证（MFA）](/post/id/313774)

  2025-12-15 17:37:50

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