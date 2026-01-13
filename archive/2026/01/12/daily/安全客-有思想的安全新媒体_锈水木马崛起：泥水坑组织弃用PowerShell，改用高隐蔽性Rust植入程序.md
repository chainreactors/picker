---
title: 锈水木马崛起：泥水坑组织弃用PowerShell，改用高隐蔽性Rust植入程序
url: https://www.anquanke.com/post/id/314289
source: 安全客-有思想的安全新媒体
date: 2026-01-12
fetch_date: 2026-01-13T03:26:27.617900
---

# 锈水木马崛起：泥水坑组织弃用PowerShell，改用高隐蔽性Rust植入程序

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

# 锈水木马崛起：泥水坑组织弃用PowerShell，改用高隐蔽性Rust植入程序

阅读量**17686**

发布时间 : 2026-01-12 17:00:03

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/rustywater-rising-muddywater-drops-powershell-for-stealthy-rust-implants/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

臭名昭著的**高级持续性威胁（APT）组织泥水坑（MuddyWater）** 完成了武器库的全面升级，摒弃传统脚本工具，转而采用一款专为规避检测而设计的精密新型恶意程序。云安实验室（CloudSEK）旗下 TRIAD 研究团队发布的一份新报告显示，该组织发起了一场定向鱼叉式钓鱼攻击，针对中东核心关键行业展开渗透，所使用的恶意软件变种为首次发现，代号 \*\*“锈水（RustyWater）”\*\*。

此次攻击精准锁定 \*\*“外交、海事、金融及电信领域机构”\*\*，与该组织既往的攻击模式相比，呈现出显著的转向特征。

长期以来，被认为与伊朗相关势力存在关联的泥水坑组织，一直依赖 \*\*“PowerShell 和 VBS 脚本加载器”\*\* 实现对受害网络的初始访问。而此次最新攻击行动则标志着其战略转型 —— 朝着打造**更强抗打击能力、更高隐蔽性的恶意程序**方向演进。

![]()

报告指出：“这款基于 Rust 语言开发的植入程序的推出，标志着该组织的工具链迎来显著升级，朝着**架构更规整、模块化程度更高、隐蔽性更强的远程访问木马（RAT）** 能力方向发展。”

攻击者选择 Rust 编程语言开发恶意程序，主要获得两大核心优势：一是**跨平台兼容性**；更关键的一点在于，能够大幅降低被现代终端防护系统检测到的概率 —— 这类防护系统通常针对该组织此前使用的脚本攻击手段设置了特征检测规则。

该攻击的感染流程始于一种经典却极具杀伤力的鱼叉式钓鱼手段：受害者会收到包含恶意 Word 文档的邮件，这些文档往往被伪装成官方沟通文件。监测到的其中一个钓鱼诱饵邮件，主题为 \*\*《新版网络安全防护指南》\*\*。

完整的攻击链步骤清晰且环环相扣：

1. **恶意钓鱼邮件**：受害者收到钓鱼诱饵邮件。
2. **恶意宏代码**：打开附件文档后触发恶意代码执行。
3. **投放程序**：一个中间可执行文件（例如以`Cybersecurity.doc`为载体，进而从`nomercys.it.com`下载恶意载荷）完成攻击铺垫。
4. **植入程序部署**：锈水木马植入程序被成功投放，该程序具备**异步命令与控制（C2）、反分析、注册表持久化，以及模块化的入侵后功能扩展**能力。

尽管此前已有关于 “射手远程访问木马（Archer RAT）” 或 “RUSTRIC” 等 Rust 语言恶意工具的零星报道，但云安实验室分析师强调，此次发现的这款变种具有**独特性**。

研究人员指出：“为避免命名冲突，同时确保表述清晰，本报告中将该恶意软件变种统一称为锈水（RustyWater）。”

随着泥水坑组织持续推进其工具库的现代化升级，相关机构提醒，被攻击目标区域的各类组织需突破传统入侵指标的检测局限，及时更新防护策略，重点加强对**编译型恶意软件威胁**的防御能力。

本文翻译自securityonline [原文链接](https://securityonline.info/rustywater-rising-muddywater-drops-powershell-for-stealthy-rust-implants/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314289](/post/id/314289)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/rustywater-rising-muddywater-drops-powershell-for-stealthy-rust-implants/)

如若转载,请注明出处： <https://securityonline.info/rustywater-rising-muddywater-drops-powershell-for-stealthy-rust-implants/>

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

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **910**

* 粉丝
* **6**

### TA的文章

* ##### [XML陷阱：Struts 2高危漏洞CVE-2025-68493致数据泄露](/post/id/314266)

  2026-01-12 17:05:06
* ##### [“粉河豚”攻击行动：银行恶意软件Astaroth转战WhatsApp发起新型攻击](/post/id/314279)

  2026-01-12 17:01:39
* ##### [CVE-2026-22184(CVSS 评分 9.3)zlib高危漏洞引发全球性缓冲区溢出风险](/post/id/314276)

  2026-01-12 17:00:43
* ##### [锈水木马崛起：泥水坑组织弃用PowerShell，改用高隐蔽性Rust植入程序](/post/id/314289)

  2026-01-12 17:00:03
* ##### [执法打击力度加大，2025年勒索软件攻击仍激增47%](/post/id/314260)

  2026-01-12 16:58:40

### 相关文章

* ##### [XML陷阱：Struts 2高危漏洞CVE-2025-68493致数据泄露](/post/id/314266)

  2026-01-12 17:05:06
* ##### [“粉河豚”攻击行动：银行恶意软件Astaroth转战WhatsApp发起新型攻击](/post/id/314279)

  2026-01-12 17:01:39
* ##### [CVE-2026-22184(CVSS 评分 9.3)zlib高危漏洞引发全球性缓冲区溢出风险](/post/id/314276)

  2026-01-12 17:00:43
* ##### [执法打击力度加大，2025年勒索软件攻击仍激增47%](/post/id/314260)

  2026-01-12 16:58:40
* ##### [泥水坑组织借助鱼叉式钓鱼，在中东多行业部署“锈水”远程访问木马](/post/id/314257)

  2026-01-12 16:58:01
* ##### [数据投毒：2026年新兴人工智能安全防护策略](/post/id/314275)

  2026-01-12 16:56:53
* ##### [印度以应对网络威胁为由要求审查智能手机源代码](/post/id/314272)

  2026-01-12 16:56:12

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