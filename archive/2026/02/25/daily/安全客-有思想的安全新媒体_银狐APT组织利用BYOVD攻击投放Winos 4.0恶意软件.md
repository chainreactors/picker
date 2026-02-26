---
title: 银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件
url: https://www.anquanke.com/post/id/314847
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:58.648056
---

# 银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件

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

# 银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件

阅读量**17726**

发布时间 : 2026-02-25 14:18:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/silver-fox-apt-unleashes-winos-4-0-malware-via-byovd-attacks/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

最新威胁情报报告显示，一个组织化程度极高的**高级持续性威胁（APT）组织**，正对台湾地区机构发起一系列复杂网络攻击，其攻击手段甚至将企业日常管理流程也变成了入侵工具。

“FortiGuard 实验室近期监测到多起针对台湾地区的定向钓鱼攻击，攻击主题高度贴合当地业务流程。” 研究人员表示。

此次攻击中出现了**进化版 Winos 4.0（ValleyRat）恶意软件**，攻击者借助**动态轮换的云基础设施、内存驻留执行**以及**漏洞驱动程序**入侵企业内网。

该攻击组织深知，**紧迫感与官方权威性**是最有效的社会工程学手段。为诱骗受害者运行攻击载荷，攻击者制作了极具本地化伪装度的诱饵文件。

“攻击者通过带毒附件或内嵌链接传播 **Winos 4.0（ValleyRat）** 及其后续恶意插件。”FortiGuard 实验室在报告中指出。

这些诱饵文件经过精心设计，**高度模仿官方公文样式**，例如**税务稽查通知、报税软件安装包、云端电子发票下载**等。

为进一步提升欺骗性，攻击者还会**注册与官方主题高度相似的域名**，强化税务、官方文件类诱饵的可信度。

由于这类基础设施**变动频繁、生命周期极短**，分析人员警告：**仅依靠传统静态域名封禁已不足以作为主要防御手段**。

受害者一旦中招，就会触发**多阶段感染流程**。在为期两个月的监测中，研究人员发现攻击者使用了一整套投递手法：

包括**用于下载器的恶意 LNK 文件**、**利用正常可执行文件进行 DLL 侧加载以执行 Shellcode**，以及**借助 `wsftprm.sys` 驱动实施的 BYOVD（自带漏洞驱动）攻击**。

通过 **BYOVD 攻击**，黑客向目标系统投放**合法签名但存在已知漏洞的驱动**，绕过 Windows 内核防护，以**最高系统权限**执行恶意代码。

此外，攻击者的隐蔽性也在持续增强。

“该组织的技术演进十分明显，其后续插件已全面转向**内存驻留执行**，在本地磁盘几乎不留下实体痕迹。” 报告解释道。

尽管攻击者极力隐藏恶意行为，却在**运营安全**上犯下关键失误。

在 2025 年 8 月捕获的一段环境自检行为中，调查人员发现了**重叠的基础设施**与**固定的开发机器标识**。

这一疏漏让研究人员确认，该活动与活跃在亚洲地区的知名 APT 组织 ——**银狐（Silver Fox）旗下一支专业子团队**直接相关。

调查还曝光了其**内部项目代号**，如**大馬專案**。

FortiGuard 实验室表示，这种协同水平**表明这是一次组织严密、工具成熟、规划清晰的定向攻击行动**。

随着银狐子团队战术不断迭代，亚洲地区安全团队必须同步升级防御能力。

由于攻击者专门利用**日常业务流程**实施入侵，**员工安全意识**已成为第一道防线。

报告最后提醒：

“随着该攻击组织持续优化逃逸技术与基础设施，个人与机构必须保持高度警惕。对任何非可信来源的文档与链接都应严格甄别，严防被这类不断进化的威胁感染。”

本文翻译自securityonline [原文链接](https://securityonline.info/silver-fox-apt-unleashes-winos-4-0-malware-via-byovd-attacks/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314847](/post/id/314847)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/silver-fox-apt-unleashes-winos-4-0-malware-via-byovd-attacks/)

如若转载,请注明出处： <https://securityonline.info/silver-fox-apt-unleashes-winos-4-0-malware-via-byovd-attacks/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

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
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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