---
title: Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包
url: https://www.anquanke.com/post/id/315032
source: 安全客-有思想的安全新媒体
date: 2026-03-06
fetch_date: 2026-03-07T03:54:46.985750
---

# Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包

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

# Coruna席卷全球威胁格局的高性能iOS漏洞利用工具包

阅读量**18921**

发布时间 : 2026-03-06 10:52:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/coruna-the-high-powered-ios-exploit-kit-proliferating-across-the-global-threat-landscape/#google_vignette>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

谷歌威胁情报小组（GTIG）正式披露了名为**Coruna**的高危 iOS 漏洞利用工具包。该工具已从商业监控厂商手中，扩散至**国家级间谍组织**与**以牟利为目的的网络攻击者**的武器库中。

该工具最早被发现针对运行 **iOS 13.0 至 iOS 17.2.1** 的 iPhone 设备，是现代漏洞利用技术的典型代表。正如 GTIG 报告所述：**该漏洞利用工具包的核心技术价值，在于其汇集了全套 iOS 漏洞，其中最先进的漏洞采用了非公开利用技术与防护绕过机制**。

Coruna 工具包的扩散 timeline，揭示了高端网络攻击能力向各类威胁组织下沉的危险趋势。2025 年 2 月，GTIG 首次捕获到该攻击链的部分代码，由某商业监控公司的客户使用。到 2025 年 7 月，该工具包出现在**UNC6353（疑似俄罗斯间谍组织）针对乌克兰用户的水坑攻击**中。最终，完整工具包在**UNC6691（境内威胁组织）针对加密货币用户的大规模攻击活动**中被获取。

GTIG 警告称，这一扩散路径**表明存在活跃的 “二手” 零日漏洞交易市场**，先进攻击技术被多个组织复用、修改并持续传播。

Coruna 是一套**综合性漏洞利用套件**，包含**5 条完整攻击链**与**共计 23 个漏洞利用模块**。该框架**工程化程度极高**，通过复杂的 JavaScript 投放系统对设备进行指纹识别，再发动精准攻击。

---

### 已识别关键漏洞列表

| 类型 | 代号 | 影响版本（含） | 修复版本 | CVE 编号 |
| --- | --- | --- | --- | --- |
| WebContent 读写 | buffout | 13 → 15.1.1 | 15.2 | CVE-2021-30952 |
| WebContent 读写 | jacurutu | 15.2 → 15.5 | 15.6 | CVE-2022-48503 |
| WebContent 读写 | bluebird | 15.6 → 16.1.2 | 16.2 | 无 CVE |
| WebContent 读写 | terrorbird | 16.2 → 16.5.1 | 16.6 | CVE-2023-43000 |
| WebContent 读写 | cassowary | 16.6 → 17.2.1 | 16.7.5、17.3 | CVE-2024-23222 |
| WebContent PAC 绕过 | breezy | 13 → 14.x | 未知 | 无 CVE |
| WebContent PAC 绕过 | breezy15 | 15 → 16.2 | 未知 | 无 CVE |
| WebContent PAC 绕过 | seedbell | 16.3 → 16.5.1 | 未知 | 无 CVE |
| WebContent PAC 绕过 | seedbell\_16\_6 | 16.6 → 16.7.12 | 未知 | 无 CVE |
| WebContent PAC 绕过 | seedbell\_17 | 17 → 17.2.1 | 未知 | 无 CVE |
| WebContent 沙箱逃逸 | IronLoader | 16.0 → 16.3.1 / 16.4.0（A12 及以下） | 15.7.8、16.5 | CVE-2023-32409 |
| WebContent 沙箱逃逸 | NeuronLoader | 16.4.0 → 16.6.1（A13–A16） | 17.0 | 无 CVE |
| 内核提权（PE） | Neutron | 13.X | 14.2 | CVE-2020-27932 |
| 内核信息泄露（PE） | Dynamo | 13.X | 14.2 | CVE-2020-27950 |
| 内核提权（PE） | Pendulum | 14 → 14.4.x | 14.7 | 无 CVE |
| 内核提权（PE） | Photon | 14.5 → 15.7.6 | 15.7.7、16.5.1 | CVE-2023-32434 |
| 内核提权（PE） | Parallax | 16.4 → 16.7 | 17.0 | CVE-2023-41974 |
| 内核提权（PE） | Gruber | 15.2 → 17.2.1 | 16.7.6、17.3 | 无 CVE |
| PPL 绕过 | Quark | 13.X | 14.5 | 无 CVE |
| PPL 绕过 | Gallium | 14.x | 15.7.8、16.6 | CVE-2023-38606 |
| PPL 绕过 | Carbone | 15.0 → 16.7.6 | 17.0 | 无 CVE |
| PPL 绕过 | Sparrow | 17.0 → 17.3 | 16.7.6、17.4 | CVE-2024-23225 |
| PPL 绕过 | Rocket | 17.1 → 17.4 | 16.7.8、17.5 | CVE-2024-23296 |

其中核心漏洞为 **CVE-2024-23222**，这是一个 WebKit 漏洞，苹果已于 2024 年初修复，但对未更新设备而言，它仍是 Coruna 武器库中的强力武器。

与传统用于静默监控的间谍软件不同，该工具包的最终载荷 —— 名为 **PlasmaLoader** 的加载器，**核心目标直指金融盗窃**。

该恶意软件会注入到 `powerd` 守护进程，以**root 权限**运行，并加载以下攻击模块：

* **敏感信息扫描**：分析文本中的 BIP39 助记词，或在苹果备忘录中检索 “银行账户” 等关键词。
* **二维码解析**：从设备存储的图片中提取信息。
* **加密货币应用劫持**：专门针对**19 款主流加密货币钱包**，包括 MetaMask、Trust Wallet、Phantom 等，窃取数字资产。

研究人员还发现一个值得注意的细节：**所有模块均包含规范的日志输出，且语句为中文**，例如载荷管理器初始化成功的提示字符串。部分内部注释甚至呈现出大模型生成的特征，为其开发流程增添了现代化色彩。

尽管 Coruna 威胁极强，但对**最新版 iOS 系统无效**。官方强烈建议用户**立即更新系统**。对于无法升级的高风险用户，GTIG 建议**开启锁定模式（Lockdown Mode）以强化安全防护**。

本文翻译自securityonline [原文链接](https://securityonline.info/coruna-the-high-powered-ios-exploit-kit-proliferating-across-the-global-threat-landscape/#google_vignette)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315032](/post/id/315032)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/coruna-the-high-powered-ios-exploit-kit-proliferating-across-the-global-threat-landscape/#google_vignette)

如若转载,请注明出处： <https://securityonline.info/coruna-the-high-powered-ios-exploit-kit-proliferating-across-the-global-threat-landscape/#google_vignette>

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

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1060**

* 粉丝
* **6**

### TA的文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13

### 相关文章

* ##### [Django发布安全补丁 修复拒绝服务与权限类漏洞](/post/id/315047)

  2026-03-06 10:56:33
* ##### [攻击者借日历邀请入侵 Perplexity Comet 浏览器并泄露敏感数据](/post/id/315044)

  2026-03-06 10:54:37
* ##### [伊朗关联黑客瞄准监控摄像头漏洞](/post/id/315041)

  2026-03-06 10:54:12
* ##### [癌症中心研究数据遭黑客攻击120万人信息受影响](/post/id/315038)

  2026-03-06 10:53:46
* ##### [Outlook.com为何大量误拦正常商业邮件](/post/id/315035)

  2026-03-06 10:53:13
* ##### [Grammarly 从文字纠错转向文学模仿](/post/id/315029)

  2026-03-06 10:52:13
* ##### [Cisco Secure FMC曝出10分高危漏洞 攻击者可获取企业防火墙Root权限](/post/id/315023)

  2026-03-06 10:51:30

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