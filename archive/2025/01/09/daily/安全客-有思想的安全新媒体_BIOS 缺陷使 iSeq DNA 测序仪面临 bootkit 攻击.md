---
title: BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击
url: https://www.anquanke.com/post/id/303346
source: 安全客-有思想的安全新媒体
date: 2025-01-09
fetch_date: 2025-10-06T20:06:11.373564
---

# BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击

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

# BIOS 缺陷使 iSeq DNA 测序仪面临 bootkit 攻击

阅读量**52661**

发布时间 : 2025-01-08 11:19:37

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ionut Ilascu，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/bios-flaws-expose-iseq-dna-sequencers-to-bootkit-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![Bios flaws and no Secure Boot expose Illumina DNA sequencers to attacks]()

美国生物技术公司Illumina的iSeq 100 DNA测序仪存在BIOS/UEFI漏洞，可能让攻击者破坏用于检测疾病和开发疫苗的设备。

Illumina iSeq 100 被宣传为一种 DNA 测序系统，医疗和研究实验室可利用它进行 “快速、经济的基因分析”。

固件安全公司Eclypsium对Illumina设备的BIOS固件进行了分析，发现它在启动时没有标准的写入保护措施，因而容易被覆盖，导致系统 “变砖 ”或植入长期存在的植入物。

**老旧而脆弱的 BIOS**

研究人员发现，iSeq 100 运行的是过时版本的 BIOS 固件，该固件在兼容支持模式（CSM）下运行，以支持旧设备，而且没有安全启动技术的保护。

Eclypsium 的分析发现了五个主要问题，这些问题允许利用九个高、中严重程度的漏洞，其中一个漏洞早在 2017 年就存在了。

除了缺少 BIOS 写保护外，iSeq 100 设备还容易受到 LogoFAIL、Spectre 2 和微架构数据采样 (MDS) 攻击。

![Vulnerabilities discovered in iSeq 100 DNA sequencing devices]()
**在 Illumina 的 iSeq 100 DNA 测序设备中发现 BIOS/UEFI 问题**
来源：Eclypsium 来源：Eclypsium

虽然在 CSM 模式下启动允许支持传统设备，但不建议敏感设备使用，尤其是新一代设备。

研究人员发现，iSeq 100 上存在漏洞的 BIOS（B480AM12 – 04/12/2018）没有启用固件保护，这就允许修改启动设备的代码。

再加上缺乏安全启动（Secure Boot）功能（可检查启动代码的有效性和完整性），任何恶意更改都不会被发现。

Eclypsium 在今天的报告中强调，他们的分析 “仅限于 iSeq 100 测序仪设备”，其他医疗或工业设备也可能存在类似问题。

研究人员解释说，医疗设备制造商使用外部供应商提供系统的计算能力。就 iSeq 100 而言，该设备依赖于 IEI Integration 公司的 OEM 主板。

由于 IEI Integration Corp 开发了多种工业计算机产品，并且是医疗设备的原始设计制造商（ODM），Eclypsium 表示，“这些问题或类似问题极有可能出现在使用 IEI 主板的其他医疗或工业设备中”。

研究人员还解释说，已经入侵设备的攻击者可以利用这些漏洞修改固件，使系统崩溃。掌握必要知识的威胁者还可以篡改测试结果。

“如果数据被这些设备中的植入/后门篡改，那么威胁者就可能篡改一系列结果，包括伪造存在或不存在遗传病、篡改医学治疗或新疫苗、伪造祖先DNA研究等。” – Eclypsium

Eclypsium 向 Illumina 通报了 iSeq 100 设备的 BIOS 问题，该生物技术公司通知他们已向受影响的客户发布了补丁。

BleepingComputer 联系了Illumina公司，要求其就修复程序的交付方式和应收到修复程序的iSeq 100系统数量发表评论。

该公司发言人表示，Illumina 正在遵循其 “标准流程，如果需要采取任何缓解措施，将通知受影响的客户”。

“我们的初步评估表明，这些问题的风险并不高，”Illumina 的一位代表告诉 BleepingComputer。

“Illumina致力于我们产品的安全和基因组数据的隐私，我们已经建立了监督和问责流程，包括我们产品开发和部署的安全最佳实践。

“作为这一承诺的一部分，我们一直在努力改进为现场仪器提供安全更新的方式。”

Eclypsium 的研究人员在报告中警告说，威胁者如果能覆盖 iSeq 100 的固件，就能 “轻易地使设备瘫痪”。

通过破坏高价值系统来扰乱业务正是勒索软件攻击者的目的，因为他们的目标是通过尽可能增加恢复难度来迫使受害者支付赎金。

除了出于经济动机的攻击者，Eclypsium 表示，国家行为者也可能发现 DNA 测序系统很有吸引力，因为它们 “对于检测遗传疾病、癌症、识别耐药细菌和生产疫苗至关重要”。

2023年，美国网络安全基础设施安全局（CISA）和食品药品管理局（FDA）发布了一份紧急公告，指出Illumina公司的通用复制服务（UCS）存在两个漏洞。

其中一个问题（CVE-2023-1968）获得了最高严重性评分，而另一个问题（CVE-2023-1966）则获得了高严重性评分。当时，Illumina 做出了反应，提供了有关如何缓解安全问题的更新和说明。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/bios-flaws-expose-iseq-dna-sequencers-to-bootkit-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/303346](/post/id/303346)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/bios-flaws-expose-iseq-dna-sequencers-to-bootkit-attacks/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/bios-flaws-expose-iseq-dna-sequencers-to-bootkit-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞](/tag/%E6%BC%8F%E6%B4%9E)
* [漏洞情报](/tag/%E6%BC%8F%E6%B4%9E%E6%83%85%E6%8A%A5)

**+1**2赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [CISA称黑客利用GeoServer漏洞成功入侵一联邦机构](/post/id/312347)

  2025-09-24 16:45:06
* ##### [SolarWinds紧急发布补丁，修复高危远程代码执行漏洞CVE-2025-26399](/post/id/312357)

  2025-09-24 16:43:11
* ##### [Chrome浏览器存在高危漏洞，可致攻击者窃取敏感信息并引发系统崩溃](/post/id/312366)

  2025-09-24 16:42:08
* ##### [CVE-2025-55241：CVSS评分10.0的Microsoft Entra ID漏洞可能危及全球所有租户](/post/id/312294)

  2025-09-22 18:14:51

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