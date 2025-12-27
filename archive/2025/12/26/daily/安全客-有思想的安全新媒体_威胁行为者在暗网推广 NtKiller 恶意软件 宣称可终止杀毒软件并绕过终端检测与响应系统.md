---
title: 威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统
url: https://www.anquanke.com/post/id/314037
source: 安全客-有思想的安全新媒体
date: 2025-12-26
fetch_date: 2025-12-27T03:20:20.651254
---

# 威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统

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

# 威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统

阅读量**20636**

发布时间 : 2025-12-26 14:51:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/threat-actors-advertised-ntkiller-malware-on-dark-web/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一名代号为 “阿尔法食尸鬼”（AlphaGhoul）的恶意行为者，已开始推广一款名为 NtKiller 的工具。该工具旨在悄无声息地关闭杀毒软件与终端检测工具。

这款工具被发布在一个供犯罪分子交易黑客服务的地下论坛上。根据相关广告内容，NtKiller 能够帮助攻击者在受感染的计算机上运行恶意程序时，规避安全检测。

NtKiller 的出现，对依赖传统安全工具的各类机构构成了严峻挑战。

该威胁行为者声称，这款工具可针对多款主流安全解决方案生效，其中包括微软防御者（Microsoft Defender）、ESET 杀毒软件、卡巴斯基、比特梵德（Bitdefender）以及趋势科技（Trend Micro）等产品。

更令人担忧的是，其宣称该工具在激进模式下运行时，能够绕过企业级终端检测与响应（EDR）系统。海妖实验室（KrakenLabs）的分析师指出，这款恶意软件可借助启动初期持久化机制隐藏自身踪迹，一旦激活，安全团队将极难对其进行检测与清除。

海妖实验室的研究人员发现，NtKiller 采用模块化定价模式：核心功能定价为 500 美元，而额外功能如根工具包功能、用户账户控制（UAC）绕过功能，每项需另行支付 300 美元。

这种定价模式表明，该工具是为在网络犯罪圈内进行商业化售卖而专门设计的。

这款工具宣称具备的能力，远超单纯的进程终止功能，还支持各类高级规避技术，例如禁用基于虚拟化的安全强制代码完整性（HVCI）、操控虚拟基本输入输出系统（VBS）以及绕过内存完整性保护等。

### 技术特性

NtKiller 所宣称的技术特性，使其一旦落入经验丰富的攻击者手中，便会具备极高的危险性。

![]()

该工具的启动初期持久化机制，可在系统启动阶段、多数安全监控系统完全激活之前完成驻留。

这一时间差优势，能让恶意载荷在检测概率极低的环境中顺利执行。

此外，其内置的反调试与反分析防护功能，会阻碍研究人员与自动化工具对恶意软件的行为进行剖析，导致该工具的实际性能与宣传效果之间存在巨大的认知空白。

静默式用户账户控制绕过功能，是其另一项关键技术特性。用户账户控制绕过功能，可让恶意软件在不触发 Windows 标准提示的情况下获取系统高级权限，而这类提示本可以提醒用户注意可疑活动。

一旦与根工具包功能相结合，攻击者就能在受感染的系统中维持持久化访问权限，同时避开常规安全监控的检测。

需要指出的是，上述各项功能均未经过第三方研究人员的独立验证，NtKiller 的实际效能目前仍不明确。

各类机构应保持高度警惕，并确保其安全工具除了基于特征码的识别功能外，还具备行为检测能力，以此应对这类新型威胁。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/threat-actors-advertised-ntkiller-malware-on-dark-web/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314037](/post/id/314037)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/threat-actors-advertised-ntkiller-malware-on-dark-web/)

如若转载,请注明出处： <https://cybersecuritynews.com/threat-actors-advertised-ntkiller-malware-on-dark-web/>

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

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **860**

* 粉丝
* **6**

### TA的文章

* ##### [威胁行为者在暗网推广 NtKiller 恶意软件 宣称可终止杀毒软件并绕过终端检测与响应系统](/post/id/314037)

  2025-12-26 14:51:33
* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24

### 相关文章

* ##### [“lc” 漏洞泄露事件：LangChain 框架 9.3 级高危漏洞致提示注入沦为机密窃取工具](/post/id/314050)

  2025-12-26 14:51:08
* ##### [零点击漏洞攻击元年：2025 年带给现代恶意软件防御的启示](/post/id/314023)

  2025-12-26 14:50:45
* ##### [TeamViewer DEX 高危漏洞暴露风险 攻击者可劫持 Nomad 服务](/post/id/314053)

  2025-12-26 14:50:09
* ##### [Zimbra 遭攻击：高危本地文件包含漏洞致未授权攻击者可读取内部文件](/post/id/314043)

  2025-12-26 14:49:24
* ##### [潜伏熊猫 APT 组织：劫持Dictionary.com+ 应用更新，展开长达两年疯狂攻击](/post/id/314062)

  2025-12-26 14:49:22
* ##### [“莲花陷阱”（LotusBail）恶意软件：5.6 万开发者下载假 WhatsApp API，功能正常却暗中窃取全部数据](/post/id/314059)

  2025-12-26 14:48:34
* ##### [英特尔 14A/18A 超级芯片：挑战台积电的 AI “系统代工” 标杆](/post/id/314055)

  2025-12-26 14:47:49

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