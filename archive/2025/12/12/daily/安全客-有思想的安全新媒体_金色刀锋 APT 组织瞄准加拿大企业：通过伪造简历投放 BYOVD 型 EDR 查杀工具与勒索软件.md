---
title: 金色刀锋 APT 组织瞄准加拿大企业：通过伪造简历投放 BYOVD 型 EDR 查杀工具与勒索软件
url: https://www.anquanke.com/post/id/313707
source: 安全客-有思想的安全新媒体
date: 2025-12-12
fetch_date: 2025-12-13T03:14:15.110723
---

# 金色刀锋 APT 组织瞄准加拿大企业：通过伪造简历投放 BYOVD 型 EDR 查杀工具与勒索软件

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

# 金色刀锋 APT 组织瞄准加拿大企业：通过伪造简历投放 BYOVD 型 EDR 查杀工具与勒索软件

阅读量**13914**

发布时间 : 2025-12-12 16:44:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/gold-blade-apt-hits-canadian-firms-with-byovd-edr-killer-and-ransomware-delivered-via-fake-resumes/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()
一个臭名昭著的威胁组织已将攻击重心转向加拿大，发起了一场融合企业间谍活动与勒索软件暴力攻击的精密网络攻击行动。安全厂商**Sophos**发布的一份新报告显示，代号为**GOLD BLADE**（又名 RedCurl 或 RedWolf）的威胁行为者，正凭借其精良的工具与战术组合，持续针对加拿大境内机构发起攻击。

2024 年 2 月至 2025 年 8 月期间，安全分析师共调查了近**40 起与该组织 “STAC6565” 攻击行动相关的入侵事件**。此次攻击的地域集中度相当惊人：“该攻击行动体现出该组织罕见的精准地域聚焦策略，**近 80% 的攻击目标均为加拿大境内机构**。”

GOLD BLADE 历来以 “黑客雇佣” 模式窃取企业敏感商业机密，如今已演变为一类复合型威胁组织。尽管间谍活动仍是其核心攻击手段，该组织还开始 \*\*“选择性投放 QWCrypt 勒索软件”\*\*，借此将非法入侵直接转化为经济收益。

这种策略转变，凸显出该组织务实且高度专业化的运作模式。报告指出：“**GOLD BLADE 能够不断迭代攻击投递方式并优化技术手段，这体现出其将网络入侵视作核心业务的专业化运作思路**。” 不同于传统勒索软件团伙 “广撒网、碰运气” 的攻击模式，GOLD BLADE 的攻击行动具有极强的计划性与针对性。

该组织摒弃了传统钓鱼邮件攻击手段，转而采用一种更隐蔽的入侵路径 ——**招聘平台**。攻击者滥用**Indeed**、**JazzHR**及**ADP Workforce Now**等公信力较高的招聘服务平台，将植入恶意代码的简历直接投递至目标企业的人力资源部门。

Sophos 分析师指出：“**这种通过招聘平台投递恶意简历的方式，标志着以人力资源为主题的社会工程学攻击手段实现了显著升级**。”

一旦受害者打开这份恶意简历，一个多阶段感染链便会被触发，最终在目标设备上部署该组织的定制化恶意软件**RedLoader**。这款加载器已历经多次快速迭代，攻击方式从最初简单的**DLL 侧加载**，发展为融合**WebDAV 服务器**、**Cloudflare Workers**及伪装系统文件的复杂攻击链。

为确保恶意软件能够不受阻碍地运行，GOLD BLADE 采用了 \*\*“自带漏洞驱动（Bring Your Own Vulnerable Driver，BYOVD）”**攻击技术。他们会同步部署定制版**Terminator EDR 查杀工具 \*\*，以及一款经过数字签名但存在漏洞的**Zemana 反恶意软件驱动程序**。

这种组合攻击手段，能够让攻击者在**内核层面直接禁用安全防护软件**。更嚣张的是，攻击者还会修改 Windows 注册表，**“禁用两项核心 Windows 安全机制：漏洞驱动黑名单…… 以及虚拟机监控器强制代码完整性（Hypervisor-Enforced Code Integrity）”**。

尽管攻击手法极为张扬，GOLD BLADE 的真实身份依旧成谜。可以确定的是，该组织具备极强的攻击持续性与技术适应性。其运作模式呈现出 “**蛰伏期与突发活跃期交替**” 的特征，通过持续优化攻击战术，始终领先于安全防御方的应对手段。

本文翻译自securityonline [原文链接](https://securityonline.info/gold-blade-apt-hits-canadian-firms-with-byovd-edr-killer-and-ransomware-delivered-via-fake-resumes/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313707](/post/id/313707)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/gold-blade-apt-hits-canadian-firms-with-byovd-edr-killer-and-ransomware-delivered-via-fake-resumes/)

如若转载,请注明出处： <https://securityonline.info/gold-blade-apt-hits-canadian-firms-with-byovd-edr-killer-and-ransomware-delivered-via-fake-resumes/>

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
* **800**

* 粉丝
* **6**

### TA的文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30

### 相关文章

* ##### [利用薪资评审诱饵实施精密钓鱼攻击：绕过防御窃取 Okta 单点登录会话令牌](/post/id/313745)

  2025-12-12 18:24:46
* ##### [高危漏洞预警 | CVE-2025-64188（CVSS 9.8）：WordPress “Soledad” 主题存在严重缺陷，订阅用户可直接接管网站](/post/id/313703)

  2025-12-12 18:05:27
* ##### [OpenAI 严阵以待：下一代 AI 模型或具备突破防御体系的能力](/post/id/313710)

  2025-12-12 18:04:59
* ##### [恶意 Visual Studio Code 扩展程序藏身虚假 PNG 文件，内置特洛伊木马](/post/id/313712)

  2025-12-12 18:04:19
* ##### [2022 年数据泄露致 160 万用户受影响，英国对 LastPass 处以 120 万英镑罚款](/post/id/313715)

  2025-12-12 18:03:30
* ##### [Notepad++ 漏洞存在重大风险：攻击者可劫持网络流量，通过更新通道植入恶意软件](/post/id/313725)

  2025-12-12 18:02:46
* ##### [新型恶意软件 DroidLock 现身：锁定安卓设备并索要赎金](/post/id/313730)

  2025-12-12 18:01:37

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