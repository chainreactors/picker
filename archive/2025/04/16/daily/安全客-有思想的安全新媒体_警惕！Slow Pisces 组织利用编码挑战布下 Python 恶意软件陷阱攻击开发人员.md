---
title: 警惕！Slow Pisces 组织利用编码挑战布下 Python 恶意软件陷阱攻击开发人员
url: https://www.anquanke.com/post/id/306551
source: 安全客-有思想的安全新媒体
date: 2025-04-16
fetch_date: 2025-10-06T22:02:49.739432
---

# 警惕！Slow Pisces 组织利用编码挑战布下 Python 恶意软件陷阱攻击开发人员

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

# 警惕！Slow Pisces 组织利用编码挑战布下 Python 恶意软件陷阱攻击开发人员

阅读量**44640**

发布时间 : 2025-04-15 10:59:57

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/slow-pisces-hackers-attacking-developers/>

译文仅供参考，具体内容表达以及含义原文为准。

一个被称为 Slow Pisces的复杂威胁行为者组织，已成为对软件开发人员的重大威胁，他们利用具有欺骗性的编码挑战作为初始攻击手段，来传播基于 Python 的恶意软件。

该攻击活动专门通过专业社交网站、编码论坛和开发平台，向软件开发人员发起攻击。攻击者提供看似无害的编程谜题，而这些谜题中隐藏着恶意有效载荷。

安全研究人员发现，自 2025 年 1 月以来，这类攻击的频率不断增加，受害者主要位于北美和欧洲的科技中心地区。攻击者采用多阶段感染策略，首先向开发人员发送个性化消息，邀请他们参加编码竞赛或合作解决问题的活动。

这些消息包含指向 GitHub 代码库或开发平台的链接，这些链接所指向的内容看似是合法的 Python 编码挑战。

然而，当开发人员执行这些挑战代码时，代码会在偷偷部署一个复杂的 Python 后门程序的同时，显示预期的输出结果，以避免引起怀疑。

Palo Alto Networks 公司的研究人员在调查了多起影响金融科技公司软件开发团队的事件后，发现了这一攻击活动。

他们的分析显示，这些威胁行为者对软件开发工作流程有着深入的了解，他们的目标很可能是知识产权以及对开发环境的访问权限，而并非为了直接获取经济利益。

这些攻击的影响不仅局限于个体开发人员，还可能对整个软件供应链造成潜在的危害。

通过攻击那些有权访问代码库和构建系统的人员，Slow Pisces 组织创造了将漏洞引入广泛分发的软件中的机会。

受到这些攻击影响的组织报告称，出现了知识产权被盗、未经授权访问开发环境的情况，在某些案例中，甚至随后还发生了勒索软件攻击事件。

研究人员将恶意软件组件命名为 PySlowDrop，它采用了复杂的混淆技术，并利用合法的 Python 库来躲避检测。

该后门程序通过修改启动脚本和计划任务来实现持续运行，同时与托管在受攻击的云基础设施上的命令与控制服务器保持加密通信。

****感染机制分析****

感染过程始于开发人员收到并接受一个编码挑战，这些挑战通常表现为需要进行优化或调试的 Python 实现谜题。

当受害者运行初始的挑战文件时，经过解混淆处理的有效载荷会与命令与控制服务器建立加密连接，然后启动完整的 PySlowDrop 恶意软件的无文件安装过程。

该后门程序通过修改开发人员的配置文件或系统启动文件来实现持续运行，并监控特定的开发活动。它专门针对包含应用程序编程接口（API）密钥、SSH密钥和代码库凭据的环境变量。

PySlowDrop 采用了先进的反分析技术，其中包括环境检测功能，当在虚拟机或沙盒环境中运行时，它会终止执行。

该恶意软件还实施了一种延迟执行策略，研究人员将其称为 “缓慢燃烧”—— 即恶意活动只会在对受害者的开发模式进行长时间观察后才会触发。

安全专家建议开发人员实施严格的代码执行策略，使用隔离的开发环境，并且在运行来自外部来源的代码时要谨慎，即使这些代码看似来自合法的编码平台或专业联系人。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/slow-pisces-hackers-attacking-developers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306551](/post/id/306551)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/slow-pisces-hackers-attacking-developers/)

如若转载,请注明出处： <https://cybersecuritynews.com/slow-pisces-hackers-attacking-developers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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