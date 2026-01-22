---
title: 新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）
url: https://www.anquanke.com/post/id/314414
source: 安全客-有思想的安全新媒体
date: 2026-01-21
fetch_date: 2026-01-22T03:34:40.867580
---

# 新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）

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

# 新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）

阅读量**16462**

发布时间 : 2026-01-21 18:09:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/new-spear-phishing-attack-leveraging-argentine-federal-court-rulings/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一场针对阿根廷司法系统的**高精准鱼叉式钓鱼攻击**已悄然出现，攻击者利用人们对合法法院通信的信任，投放危险的远程访问木马（RAT）。

该攻击活动使用看似真实的联邦法院预防性羁押复审文件，诱使法律专业人士下载恶意软件。

安全专家已将此次攻击归类为**高度定向攻击**，它采用多阶段感染技术，旨在长期获取敏感法律与机构系统的访问权限。

攻击始于收件人收到包含 ZIP 压缩包的邮件，该压缩包伪装成官方司法通知。

压缩包内，攻击者植入了一个伪装成 PDF 的恶意 Windows 快捷方式文件（LNK），同时包含一个批处理脚本加载器和一份看似真实的法院裁决文件。

当受害者点击看似标准的 PDF 文件时，恶意执行链随即启动，同时会显示一份极具迷惑性的诱饵文档以避免引起怀疑。这种社会工程学手法让该攻击在日常处理法院文件的司法人员中**格外有效**。

Seqrite 的分析人员发现了这一攻击活动，并揭露了其复杂的多阶段传播机制。

研究团队发现，该恶意软件专门针对阿根廷法律行业，包括司法机构、法律专业人士以及与司法系统相关的政府部门。

![]()

诱饵文档以极高的精度模仿阿根廷联邦法院的真实裁决文件，使用正式的法律西班牙语、规范的案件编号、司法签名，并引用真实机构（如刑事与矫正口头法庭）。

这种高度的细节还原**大幅提升了攻击在目标受害者中的成功率**。

---

### 感染机制：从快捷方式到远程访问木马（RAT）的部署

该攻击采用三阶段感染流程，旨在规避检测。恶意 LNK 文件会以隐藏模式启动 PowerShell，绕过执行策略以运行批处理脚本，该脚本连接到托管在 GitHub 上的基础设施。

![]()

此脚本会下载第二阶段载荷，该载荷伪装成 “msedge\_proxy.exe”，存储在 Microsoft Edge 用户数据目录中以显得合法。

最终载荷是一个基于 Rust 语言开发的远程访问木马（RAT），具备强大的反分析能力。

![]()

该 RAT 在执行前会进行全面的环境检查，扫描虚拟机、沙箱和调试工具。如果检测到分析工具，恶意软件会立即终止运行以避免被调查。

一旦成功运行，它会建立加密的命令与控制通信，为攻击者提供包括**文件窃取、持久化安装、凭证窃取**，甚至通过模块化 DLL 组件部署勒索软件等多种功能。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/new-spear-phishing-attack-leveraging-argentine-federal-court-rulings/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314414](/post/id/314414)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/new-spear-phishing-attack-leveraging-argentine-federal-court-rulings/)

如若转载,请注明出处： <https://cybersecuritynews.com/new-spear-phishing-attack-leveraging-argentine-federal-court-rulings/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **940**

* 粉丝
* **6**

### TA的文章

* ##### [珠穆朗玛峰勒索软件团伙据称宣称入侵了麦当劳印度系统](/post/id/314403)

  2026-01-21 18:10:24
* ##### [Google Gemini漏洞可被攻击者利用获取私人日历数据](/post/id/314409)

  2026-01-21 18:09:50
* ##### [新型鱼叉式钓鱼攻击借阿根廷联邦法院裁决掩护，植入远程访问木马（RAT）](/post/id/314414)

  2026-01-21 18:09:24
* ##### [密码学基础被攻破：GNU libtasn1中存在一字节溢出漏洞（CVE-2025-13151）](/post/id/314411)

  2026-01-21 18:08:43
* ##### [Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险](/post/id/314423)

  2026-01-21 18:07:57

### 相关文章

* ##### [珠穆朗玛峰勒索软件团伙据称宣称入侵了麦当劳印度系统](/post/id/314403)

  2026-01-21 18:10:24
* ##### [Google Gemini漏洞可被攻击者利用获取私人日历数据](/post/id/314409)

  2026-01-21 18:09:50
* ##### [密码学基础被攻破：GNU libtasn1中存在一字节溢出漏洞（CVE-2025-13151）](/post/id/314411)

  2026-01-21 18:08:43
* ##### [Apache Airflow漏洞导致敏感工作流数据面临潜在攻击风险](/post/id/314423)

  2026-01-21 18:07:57
* ##### [亚马逊 100 亿美元押注 OpenAI，旨在推动AI驱动零售的变革](/post/id/314435)

  2026-01-21 18:07:21
* ##### [德以两国承诺共建网络安全联盟](/post/id/314401)

  2026-01-21 18:06:40
* ##### [X开源Grok驱动的算法代码，揭秘内容传播机制](/post/id/314428)

  2026-01-21 18:06:03

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