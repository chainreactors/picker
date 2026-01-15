---
title: 攻击者借助伪造PDF将合法远程监控管理工具武器化
url: https://www.anquanke.com/post/id/314309
source: 安全客-有思想的安全新媒体
date: 2026-01-14
fetch_date: 2026-01-15T03:27:58.056596
---

# 攻击者借助伪造PDF将合法远程监控管理工具武器化

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

# 攻击者借助伪造PDF将合法远程监控管理工具武器化

阅读量**26750**

发布时间 : 2026-01-14 13:01:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/attackers-weaponize-legitimate-rmm-tools-via-fake-pdfs/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安恒实验室安全情报中心（ASEC）在一份新报告中发出警示，称威胁攻击者正出现一种新型攻击趋势 ——**劫持功能强大的远程监控管理（RMM）软件以侵入受害者网络**。攻击者通过滥用 Syncro、SuperOps、NinjaOne 以及 ScreenConnect 等受信任工具，绕过安全检测雷达，在受感染系统上建立持久化远程控制权限。

这一轮攻击活动至少自 2025 年 10 月起便处于活跃状态，其攻击链路的核心伪装手段，是从一份看似无害的 PDF 文件开始。

攻击的起始环节是典型的钓鱼诱饵：受害者会收到携带 PDF 附件的钓鱼邮件，附件名称往往带有紧急属性，例如《产品缺陷订单.pdf》《发票明细.PDF》《视频付款异常.pdf》等。

但这些文件本质上都是诱饵。报告中提到：“当用户打开这份 PDF 文档时，会被引导点击一个谷歌云端硬盘链接”。文档会显示 “加载失败” 的提示，进而诱导用户访问一个外部网站 —— 该网站通常会伪装成 Adobe 的官方页面，以此骗取用户信任，让其点击查看内容。

安恒实验室安全情报中心的分析人员指出：“这一行为表明，威胁攻击者正通过仿冒 Adobe 的方式，让用户误以为自己正在下载一份合法的 PDF 文件”。

一旦用户点击该链接，下载到本地的并非传统意义上的病毒，而是一款**合法的、或经过轻微篡改的企业级远程监控管理软件安装程序**。这类工具的设计初衷，是供 IT 管理员对计算机进行远程运维管理，如今却被攻击者当作 “就地取材式” 攻击武器。它们带有正规数字签名，往往能被杀毒软件信任，且默认具备强大的远程访问能力。

报告着重强调：“威胁攻击者分发的 PDF 文件，会诱导用户从伪装的分发页面下载并运行这款远程监控管理工具”。

此次攻击活动中被武器化的具体工具包括：

* Syncro
* SuperOps
* NinjaOne
* ScreenConnect

从对攻击下载器的分析结果来看，这轮攻击的技术成熟度颇高。已监测到的一个 NinjaOne 下载器样本，是基于 \*\*Nullsoft 脚本安装系统（NSIS）\*\* 开发的。

报告指出：“该下载器由 NSIS 开发而成，其内置的 NSI 脚本中包含一条用于下载额外载荷的命令”。它会在用户不知情的情况下，从恶意域名[anhemvn124.com](https://anhemvn124.com)获取远程监控管理工具的代理程序，并自动完成静默安装。

恶意软件的开发者甚至留下了可供追溯的数字线索。用于为恶意文件签名的证书显示，**这类攻击活动至少从 2025 年 10 月起就已持续开展**。

这类攻击的检测难度极大，原因在于其最终投放的载荷，通常是一款被数千家正规企业广泛使用的、合法且经过签名的应用程序。安恒实验室安全情报中心建议用户，应对 PDF 文件中出现的任何 “加载失败” 提示保持高度警惕，同时务必核实任何来历不明的发票类邮件的发件人信息。

“在打开来自未知发件人的邮件时，用户必须格外谨慎。核实发件人是否可信、不点击可疑链接或附件，这两点至关重要”。

报告同时敦促各类组织机构，需加强对未经授权的远程监控管理软件安装行为的监测，并阻断与这类攻击分发活动相关的已知恶意域名访问。

本文翻译自securityonline [原文链接](https://securityonline.info/attackers-weaponize-legitimate-rmm-tools-via-fake-pdfs/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314309](/post/id/314309)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/attackers-weaponize-legitimate-rmm-tools-via-fake-pdfs/)

如若转载,请注明出处： <https://securityonline.info/attackers-weaponize-legitimate-rmm-tools-via-fake-pdfs/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **920**

* 粉丝
* **6**

### TA的文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [攻击者借助伪造PDF将合法远程监控管理工具武器化](/post/id/314309)

  2026-01-14 13:01:19
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22

### 相关文章

* ##### [双重严重：Ruckus IoT控制器因硬编码密钥泄露面临root权限远程代码执行](/post/id/314315)

  2026-01-14 13:01:25
* ##### [蜜罐陷阱(HoneyTrap)——抵御越狱攻击的全新大语言模型防御框架](/post/id/314328)

  2026-01-14 13:00:52
* ##### [高危漏洞CVE-2025-52694：研华设备存在 SQL 注入，可导致 IoT设备被完全攻陷](/post/id/314324)

  2026-01-14 13:00:38
* ##### [n8n供应链攻击：滥用社区节点窃取OAuth令牌](/post/id/314316)

  2026-01-14 13:00:22
* ##### [高危警报：Moxa交换机存在OpenSSH远程代码执行漏洞（CVSS 9.8）](/post/id/314327)

  2026-01-14 12:59:46
* ##### [ValleyRAT\_S2病毒攻击组织：投放隐匿恶意软件，窃取金融敏感信息](/post/id/314334)

  2026-01-14 12:59:44
* ##### [苹果确认谷歌 Gemini 将为 Siri 提供技术支持，强调隐私仍是核心优先级](/post/id/314310)

  2026-01-14 12:58:29

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