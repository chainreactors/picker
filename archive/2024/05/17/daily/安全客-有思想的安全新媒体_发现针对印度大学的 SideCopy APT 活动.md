---
title: 发现针对印度大学的 SideCopy APT 活动
url: https://www.anquanke.com/post/id/296541
source: 安全客-有思想的安全新媒体
date: 2024-05-17
fetch_date: 2025-10-06T17:14:33.799956
---

# 发现针对印度大学的 SideCopy APT 活动

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

# 发现针对印度大学的 SideCopy APT 活动

阅读量**304081**

发布时间 : 2024-05-16 11:47:09

**x**

##### 译文声明

本文是翻译文章

原文地址：<https://thecyberexpress.com/sidecopy-campaign-targets-indian-universities/>

译文仅供参考，具体内容表达以及含义原文为准。

Cyble 研究与情报实验室 (CRIL) 研究人员发现了一项新的 SideCopy 活动。此前曾观察到该威胁组织针对南亚国家，特别是印度和阿富汗的政府和军​​事目标。

该活动自 2023 年 5 月开始活跃，通过复杂的感染链针对大学生，其中包括恶意 LNK 文件、HTAs 和伪装成合法文档的加载程序 DLL。最终，该活动部署了Reverse RAT 和 Action RAT 等恶意软件负载，使攻击者能够对受感染的设备进行广泛的控制。

该研究探讨了 SideCopy 所采用的策略，例如他们最近对大学生的关注，以及与透明部落 APT 组织的活动可能重叠。

**SideCopy活动感染链的技术分析**
5 月初，CRIL 发现了 SideCopy 组织在其运营中使用的恶意域。该网站被发现托管一个名为“files.zip”的 ZIP 存档文件，其中包含标记为“economy”、“it”和“survey”的子目录。调查目录包含与 SideCopy 之前在其早期活动中使用的文件类似的文件。
![]()
来源：Cyble
该活动可能使用垃圾邮件来分发通过受感染网站托管的恶意 ZIP 存档作为初始感染媒介。这些档案包含伪装成合法文档的恶意 LNK 文件，例如“IT Trends.docx.lnk”。

执行后，LNK 文件会触发一系列命令，然后继续下载并执行恶意 HTA 文件。下载的 HTA 文件包含附加诱饵文档和 DLL 文件中的嵌入有效负载。诱惑文件通常以时事或相关学术主题为主题，以使目标人群显得合法。

![]()
来源：Cyble 博客
![]()
来源：Cyble 博客
该恶意软件具有适应不同防病毒软件（例如 Avast、Kaspersky 和 ​​Bitdefender）的功能，通过将 LNK 快捷方式文件放置在启动文件夹中，进一步增强了其逃避检测并确保持久性的能力。

攻击过程最终会导致在受害者系统上部署恶意负载，例如反向 RAT 和操作 RAT，然后连接到远程命令和控制 (C&C) 服务器以开始恶意活动。

**与透明部落活动的交集**
该研究进一步表明 SideCopy 和透明部落（另一个以印度军事和学术机构为目标而闻名的 APT 组织）之间可能存在重叠或合作。这种交叉暗示了两个群体之间可能的合作努力或共同目标，研究人员此前指出 SideCopy 可能充当透明部落的一个分支。

SideCopy 还模仿 Sidewinder APT 组织传播恶意软件文件的策略，例如使用伪装的 LNK 文件来启动复杂的感染链。

CRIL 研究人员建议使用强大的电子邮件过滤系统、谨慎行事、部署网络级监控并禁用 PowerShell、MSHTA、cmd.exe 等脚本语言，以防止这种潜在威胁。

本文翻译自 [原文链接](https://thecyberexpress.com/sidecopy-campaign-targets-indian-universities/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/296541](/post/id/296541)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处： <https://thecyberexpress.com/sidecopy-campaign-targets-indian-universities/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [APT](/tag/APT)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [猎影计划：从密流中捕获 Cobalt Strike 的隐秘身影](/post/id/310538)

  2025-07-24 12:50:35
* ##### [APT-C-55（Kimsuky）组织在RandomQuery活动中投递开源RAT的攻击活动分析](/post/id/297233)

  2024-06-13 10:15:14
* ##### [Andariel APT 使用 DoraRAT 和 Nestdoor 恶意软件监视韩国企业](/post/id/297004)

  2024-06-03 10:52:13
* ##### [Turla APT 组织涉嫌利用 MSBuild 微小后门进行隐秘攻击](/post/id/296639)

  2024-05-21 10:31:48
* ##### [俄罗斯黑客 APT28 对波兰政府发动恶意软件攻击](/post/id/296335)

  2024-05-09 11:10:37
* ##### [透明部落：针对印度国防部门的难以捉摸的威胁](/post/id/295858)

  2024-04-22 11:09:46
* ##### [沙鹰：源自中东还是美国？](/post/id/293799)

  2024-03-12 10:54:16

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