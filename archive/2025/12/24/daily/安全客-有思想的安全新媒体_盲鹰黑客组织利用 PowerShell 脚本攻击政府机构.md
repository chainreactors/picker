---
title: 盲鹰黑客组织利用 PowerShell 脚本攻击政府机构
url: https://www.anquanke.com/post/id/313980
source: 安全客-有思想的安全新媒体
date: 2025-12-24
fetch_date: 2025-12-25T03:24:47.957859
---

# 盲鹰黑客组织利用 PowerShell 脚本攻击政府机构

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

# 盲鹰黑客组织利用 PowerShell 脚本攻击政府机构

阅读量**15120**

发布时间 : 2025-12-24 15:03:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/blindeagle-hackers-attacking-government-agencies/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

南美威胁组织**盲鹰（BlindEagle）** 针对哥伦比亚政府机构发起了一系列精密的攻击行动，其攻击手段的演进程度令人警惕。

2025 年 9 月初，该组织通过协同钓鱼邮件与多阶段恶意软件投递的方式，将目标锁定在哥伦比亚工商旅游部（MCIT）下属的一家政府机构。

此次攻击标志着盲鹰组织的作战模式在复杂度与技术含量上实现大幅升级，其攻击方式已从基础的恶意软件部署，升级为包含多个恶意组件、经过精心策划的攻击链路。

攻击始于一封经过策略性构造的钓鱼邮件，该邮件伪装成哥伦比亚司法系统的官方通知。

![]()

邮件中使用法律术语与政府公文格式营造紧迫感，迫使收件人确认查收一份看似是劳动诉讼的通知文件。

值得注意的是，这封钓鱼邮件是通过该机构内部一个已被入侵的账户发送，不仅增强了邮件的可信度，还绕过了常规的邮件安全防护措施。

这种内部账户沦陷的情况，让攻击者得以利用机构内部的信任关系，避开那些通常会标记外部威胁的安全协议检测。

泽斯卡尔（Zscaler）的分析人员还原了完整的攻击链路，并确认盲鹰组织采用了一种罕见的无文件攻击方法，以此规避各类检测系统。

钓鱼邮件的初始附件是一个可缩放矢量图形（SVG）文件，其中嵌入了经过编码的超文本标记语言（HTML）代码，该代码会引导用户访问一个仿冒哥伦比亚司法部门的钓鱼网站。

一旦用户与该钓鱼网站进行交互，攻击链路便会通过三个 JavaScript 文件与一条 PowerShell 命令逐步展开。在每一个攻击阶段，恶意组件都会借助包括 Base64 编码与自定义混淆算法在内的多种编码技术，对下一个组件进行逐层解密。

### 感染机制

该攻击的感染机制极具技术深度，融合了隐写术与合法服务来投递恶意载荷。

攻击链路中的 JavaScript 文件搭载了复杂的解混淆程序，能够将整数数组转换为可执行代码。

PowerShell 命令会从互联网档案馆下载一个图像文件，提取隐藏在其中的 Base64 编码恶意载荷，再通过.NET 反射技术将该载荷直接加载至内存中运行。

![]()

这种内存执行的方式，可避免任何恶意文件写入磁盘，极大地增加了传统基于文件检测的安全解决方案的识别难度。

该 PowerShell 脚本会执行一款名为**卡米尼奥（Caminho）** 的下载器恶意软件，其代码中包含葡萄牙语特征。随后，该下载器会通过 Discord 的内容分发网络获取**DCRAT 远程控制工具**。DCRAT 具备先进的规避能力，尤其是能够对微软反恶意软件扫描接口（AMSI）进行补丁修改，从而禁用相关检测机制。

![]()

恶意软件通过创建计划任务与修改注册表的方式实现持久化驻留，让攻击者能够长期控制被入侵的系统。

此次攻击行动充分展现了盲鹰组织作为威胁行为体的成熟化发展：其既掌握精湛的社会工程学攻击技巧，又具备混淆处理、隐写术及滥用合法服务的技术能力，能够以极低的被检测风险，对政府基础设施实施定向攻击。

是否需要我帮你整理这份译文中的**核心攻击步骤清单**，方便你快速梳理盲鹰组织的攻击流程？

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/blindeagle-hackers-attacking-government-agencies/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313980](/post/id/313980)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/blindeagle-hackers-attacking-government-agencies/)

如若转载,请注明出处： <https://cybersecuritynews.com/blindeagle-hackers-attacking-government-agencies/>

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

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **850**

* 粉丝
* **6**

### TA的文章

* ##### [慧与 OneView 产品高危漏洞（CVE-2025-37164）：可被用于远程代码执行](/post/id/314010)

  2025-12-24 15:06:42
* ##### [罗马尼亚水务部门证实遭遇网络攻击，核心供水系统未受影响](/post/id/314000)

  2025-12-24 15:05:40
* ##### [苹果公司因借隐私规则实施反垄断行为 在意大利被罚 9860 万欧元](/post/id/314005)

  2025-12-24 15:05:37
* ##### [谷歌推迟安卓端 Gemini AI 全面推送至 2026 年](/post/id/313994)

  2025-12-24 15:04:55
* ##### [人工智能初创公司奎尔特：仅用 40 小时人工投入，一周内完成 Linux 开发板设计](/post/id/313999)

  2025-12-24 15:04:21

### 相关文章

* ##### [慧与 OneView 产品高危漏洞（CVE-2025-37164）：可被用于远程代码执行](/post/id/314010)

  2025-12-24 15:06:42
* ##### [罗马尼亚水务部门证实遭遇网络攻击，核心供水系统未受影响](/post/id/314000)

  2025-12-24 15:05:40
* ##### [苹果公司因借隐私规则实施反垄断行为 在意大利被罚 9860 万欧元](/post/id/314005)

  2025-12-24 15:05:37
* ##### [谷歌推迟安卓端 Gemini AI 全面推送至 2026 年](/post/id/313994)

  2025-12-24 15:04:55
* ##### [人工智能初创公司奎尔特：仅用 40 小时人工投入，一周内完成 Linux 开发板设计](/post/id/313999)

  2025-12-24 15:04:21
* ##### [零日漏洞警报：Linksys 身份验证绕过漏洞致黑客可无密码劫持路由器](/post/id/313984)

  2025-12-24 15:03:45
* ##### [M-Files 身份窃取漏洞：高危缺陷致内部人员可劫持用户账户、获取敏感数据](/post/id/313972)

  2025-12-24 15:02:59

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